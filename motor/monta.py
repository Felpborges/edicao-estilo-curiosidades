#!/usr/bin/env python3
"""monta.py · Estilo 03 · junta rosto (clipe limpo), planos de cena e legenda, e codifica.

Uso (a partir de qualquer pasta):
  python3 monta.py <pasta da edição> --folha F0 F1 [--passo 1] [--cols 8] [--saida arquivo.jpg]   folha de quadros (leve)
  python3 monta.py <pasta da edição> --quadro N [--saida arquivo.png]                              um quadro cheio (leve)
  python3 monta.py <pasta da edição> --blocos                                                      lista os blocos de legenda
  python3 monta.py <pasta da edição> --render [--de F0 --ate F1] [--saida arquivo.mp4]             vídeo (PESADO: rodar pela trava leve.py)
  python3 monta.py <pasta da edição> --linha                                                       mostra a linha do tempo dos planos
  --so plano_02  carrega só os planos cujo arquivo contém esse texto (para testar um plano sem depender dos outros)

Planos de cena: `<edição>/05-cenas/plano_*.py`, cada um com `def plano(ctx)` que devolve
{'nome', 'f0', 'f1', 'cena'}: quadros [f0, f1) do clipe; `cena.quadro(t_ms)` recebe o tempo ABSOLUTO do clipe.
O que não for coberto por plano é rosto (A-roll), sem tratamento. A legenda vai por cima de tudo, presa à tela.
"""
import os, sys, json, glob, argparse, importlib.util, subprocess
import numpy as np
import cv2

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import e3, pecas, perfis, legenda as leg


class Ctx:
    """O que um plano de cena precisa: tempos das palavras, quadros, imagens (reais ou provisórias)."""
    def __init__(self, edicao):
        self.edicao = edicao
        self.ws = json.load(open(os.path.join(edicao, '02-corte', 'palavras-ataque.json'), encoding='utf-8'))['palavras']
        c = json.load(open(os.path.join(edicao, '02-corte', 'cortes.json'), encoding='utf-8'))
        self.n_quadros, self.Q = c['quadros_corte'], e3.QUADRO_MS
        self.provisorias = []

    def ataque(self, i): return self.ws[i]['ataque_ms']               # início da palavra i, reconferido no áudio (ms)
    def fim(self, i): return self.ws[i]['fim_ms']
    def q(self, ms): return int(round(ms / self.Q))                   # ms → quadro
    def t(self, q): return q * self.Q                                 # quadro → ms
    def q_palavra(self, i, desloc_ms=0.0): return self.q(self.ataque(i) + desloc_ms)   # quadro em que algo ligado à palavra i entra

    def _arq(self, nome):
        for ext in ('.png', '.jpg', '.jpeg', '.webp'):
            p = os.path.join(self.edicao, '05-imagens', 'tratadas', nome + ext)
            if os.path.exists(p): return p
        return None

    def img(self, nome, largura, altura, rotulo=None):
        """Imagem BGR de `05-imagens/tratadas/<nome>.*`; se ainda não existe, devolve uma provisória cinza com rótulo."""
        p = self._arq(nome)
        if p: return cv2.imread(p, cv2.IMREAD_COLOR)
        self.provisorias.append(nome)
        return pecas.provisoria(largura, altura, rotulo or nome)

    def rgba(self, nome, largura, altura, rotulo=None):
        """Recorte BGRA (fundo já removido) de `05-imagens/tratadas/<nome>.png`; provisório = retângulo cinza opaco."""
        p = self._arq(nome)
        if p:
            im = cv2.imread(p, cv2.IMREAD_UNCHANGED)
            if im.ndim == 3 and im.shape[2] == 4: return im
            return np.dstack([im[:, :, :3], np.full(im.shape[:2], 255, np.uint8)])
        self.provisorias.append(nome)
        im = pecas.provisoria(largura, altura, rotulo or nome, tom=150)
        return np.dstack([im, np.full(im.shape[:2], 255, np.uint8)])


def carrega(edicao, so=None, perfil=None, pasta_cenas='05-cenas'):
    perfis.usa(perfil or perfis.da_edicao(edicao))        # o perfil vem do plano de edição (03-plano/perfil.json)
    ctx = Ctx(edicao); planos = []
    sys.path.insert(0, os.path.join(edicao, pasta_cenas))
    for f in sorted(glob.glob(os.path.join(edicao, pasta_cenas, 'plano_*.py'))):
        if so and not any(s_ in os.path.basename(f) for s_ in so.split(',')): continue
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        p = mod.plano(ctx); p['arquivo'] = os.path.basename(f); planos.append(p)
    planos.sort(key=lambda p: p['f0'])
    for a, b in zip(planos, planos[1:]):
        if a['f1'] > b['f0']: sys.exit(f"planos sobrepostos: {a['nome']} (até {a['f1']}) e {b['nome']} (de {b['f0']})")
    aj = os.path.join(edicao, '02-corte', 'legenda-ajustes.json')
    aj = json.load(open(aj, encoding='utf-8')) if os.path.exists(aj) else {}
    L = leg.Legenda(leg.blocos(ctx.ws, ctx.n_quadros * ctx.Q, aj), ctx.Q)
    import base as _base                                   # os cortes valem mesmo quando só alguns planos são carregados
    L.cola_nos_cortes(sorted({q for par in _base.CORTES.values() for q in par}))
    return ctx, planos, L


class Rosto:
    """Lê o clipe limpo pelo ffmpeg (que respeita a matriz BT.709 do arquivo; o leitor do OpenCV decodifica como
    BT.601 e desloca as cores do rosto ≈ 3,5 níveis). Leitura em ordem; se pedirem um quadro fora de ordem, reabre."""
    def __init__(self, caminho):
        self.caminho, self.p, self.pos, self.tam = caminho, None, 0, e3.W * e3.H * 3

    def _abre(self, n):
        if self.p: self.p.kill(); self.p.wait()
        # accurate_rnd: sem ele a conversão padrão do ffmpeg escurece 1,6 nível de luma (medido em 20/11/2026)
        self.p = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{n * e3.FPS_D / e3.FPS_N:.6f}', '-i', self.caminho,
                                   '-sws_flags', 'accurate_rnd+full_chroma_int', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'],
                                  stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        self.pos = n

    def quadro(self, n):
        if self.p is None or n < self.pos or n > self.pos + 48: self._abre(n)
        while True:
            buf = self.p.stdout.read(self.tam)
            if len(buf) < self.tam: sys.exit(f'não li o quadro {n} do clipe limpo')
            self.pos += 1
            if self.pos - 1 == n: return np.frombuffer(buf, np.uint8).reshape(e3.H, e3.W, 3).copy()

    def fecha(self):
        if self.p: self.p.kill(); self.p.wait()


def yuv709(bgr):
    """BGR (0..255) → yuv420p BT.709, faixa limitada, com a conta exata (a conversão padrão do ffmpeg perde brilho)."""
    f = bgr.astype(np.float32); b, g, r = f[..., 0], f[..., 1], f[..., 2]
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    Y = 16 + 219 * y / 255; Cb = 128 + 224 * ((b - y) / 1.8556) / 255; Cr = 128 + 224 * ((r - y) / 1.5748) / 255
    h, w = Y.shape; sub = lambda c: c.reshape(h // 2, 2, w // 2, 2).mean(axis=(1, 3))
    q = lambda a: np.clip(np.rint(a), 0, 255).astype(np.uint8)
    return q(Y).tobytes() + q(sub(Cb)).tobytes() + q(sub(Cr)).tobytes()


def quadro(n, ctx, planos, L, rosto, com_legenda=True):
    for p in planos:
        if p['f0'] <= n < p['f1']:
            f = p['cena'].quadro(ctx.t(n)); break
    else:
        f = rosto.quadro(n)
    return L.poe(f, n) if com_legenda else f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('edicao'); ap.add_argument('--folha', nargs=2, type=int); ap.add_argument('--passo', type=int, default=1)
    ap.add_argument('--cols', type=int, default=8); ap.add_argument('--quadro', type=int); ap.add_argument('--blocos', action='store_true')
    ap.add_argument('--linha', action='store_true'); ap.add_argument('--render', action='store_true')
    ap.add_argument('--de', type=int, default=0); ap.add_argument('--ate', type=int); ap.add_argument('--saida')
    ap.add_argument('--so', help='carrega só os planos cujo arquivo contém este texto (vírgula separa vários)')
    ap.add_argument('--sem-legenda', action='store_true'); ap.add_argument('--final', action='store_true')
    ap.add_argument('--crf', type=int, default=14, help='qualidade do x264 (menor = arquivo maior). Com grão vivo, 14 dá ≈ 40 Mbit/s; 20 dá ≈ 15')
    ap.add_argument('--perfil', help='perfil de acabamento (V03, V01, V04); sem isto vale o do plano (03-plano/perfil.json)')
    ap.add_argument('--cenas', default='05-cenas', help='pasta dos planos de cena dentro da edição (padrão 05-cenas)')
    a = ap.parse_args()
    ed = os.path.abspath(a.edicao)
    ctx, planos, L = carrega(ed, a.so, a.perfil, a.cenas)
    print('perfil de acabamento:', perfis.nome_ativo(), '·', perfis.ativo()['nome'])
    rosto = Rosto(os.path.join(ed, '02-corte', 'clipe-limpo.mp4'))
    out_dir = os.path.join(ed, '06-render'); os.makedirs(out_dir, exist_ok=True)

    if a.linha:
        pos = 0
        for p in planos:
            if p['f0'] > pos: print(f"q{pos:>4}–q{p['f0']:<4} {(p['f0']-pos)*ctx.Q/1000:5.2f} s  ROSTO")
            print(f"q{p['f0']:>4}–q{p['f1']:<4} {(p['f1']-p['f0'])*ctx.Q/1000:5.2f} s  {p['nome']}  ({p['arquivo']})"); pos = p['f1']
        if pos < ctx.n_quadros: print(f"q{pos:>4}–q{ctx.n_quadros:<4} {(ctx.n_quadros-pos)*ctx.Q/1000:5.2f} s  ROSTO")
        if ctx.provisorias: print('imagens provisórias em uso:', ', '.join(sorted(set(ctx.provisorias))))
    if a.blocos:
        print(f'fonte da legenda: {L.nome_fonte} · {len(L.b)} blocos')
        for b in L.b: print(f"q{b['q0']:>4}–q{b['q1']:<4} {(b['q1']-b['q0'])*ctx.Q:5.0f} ms  [{len(b['texto'])} car]  {b['texto']}")
    if a.quadro is not None:
        dest = a.saida or os.path.join(out_dir, f'quadro-{a.quadro:04d}.png')
        cv2.imwrite(dest, quadro(a.quadro, ctx, planos, L, rosto, not a.sem_legenda)); print(dest)
    if a.folha:
        f0, f1 = a.folha; ns = list(range(f0, f1, a.passo)); cw, chh = 270, 480
        lin = (len(ns) + a.cols - 1) // a.cols
        folha = np.zeros((lin * (chh + 26), a.cols * cw, 3), np.uint8)
        for k, n in enumerate(ns):
            im = cv2.resize(quadro(n, ctx, planos, L, rosto, not a.sem_legenda), (cw, chh), interpolation=cv2.INTER_AREA)
            y, x = (k // a.cols) * (chh + 26), (k % a.cols) * cw
            folha[y + 26:y + 26 + chh, x:x + cw] = im
            cv2.putText(folha, f'q{n} {n*ctx.Q/1000:.2f}s', (x + 6, y + 19), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)
        dest = a.saida or os.path.join(out_dir, f'folha-{f0:04d}-{f1:04d}.jpg')
        cv2.imwrite(dest, folha, [cv2.IMWRITE_JPEG_QUALITY, 90]); print(dest, folha.shape[1], 'x', folha.shape[0])
    if a.render:
        if a.final and ctx.provisorias:
            sys.exit('entrega recusada: ainda há imagens provisórias: ' + ', '.join(sorted(set(ctx.provisorias))))
        f1 = a.ate or ctx.n_quadros
        dest = a.saida or os.path.join(out_dir, 'corte.mp4')
        audio = os.path.join(ed, '02-corte', 'audio-corte.wav')
        marca = ['-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
        cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-s', f'{e3.W}x{e3.H}', '-r', f'{e3.FPS_N}/{e3.FPS_D}', *marca, '-i', '-',
               '-ss', f'{a.de * ctx.Q / 1000:.6f}', '-t', f'{(f1 - a.de) * ctx.Q / 1000:.6f}', '-i', audio,
               '-c:v', 'libx264', '-crf', str(a.crf), '-preset', 'medium', '-pix_fmt', 'yuv420p', *marca, '-c:a', 'aac', '-b:a', '192k',
               '-movflags', '+faststart', '-shortest', dest]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for n in range(a.de, f1):
            p.stdin.write(yuv709(quadro(n, ctx, planos, L, rosto, not a.sem_legenda)))
        rosto.fecha(); p.stdin.close(); p.wait(); print('render:', p.returncode, dest, f'({f1 - a.de} quadros)')
        if ctx.provisorias: print('ATENÇÃO: corte PROVISÓRIO; imagens que faltam:', ', '.join(sorted(set(ctx.provisorias))))


if __name__ == '__main__':
    main()
