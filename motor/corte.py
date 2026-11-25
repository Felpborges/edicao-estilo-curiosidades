#!/usr/bin/env python3
"""corte.py · Estilo 03 · corte limpo: tira silêncios longos, mantém o respiro da referência, recorta em 9:16.

Uso: python3 corte.py <video> <pasta_01-bruto> <pasta_02-corte> --crop x0 [--largura 810] [--renderiza]

Regras (CONTEXTO-ESTILO-03.md, seção 4, e SOM.md): a referência deixa pausas medianas de 80 a 110 ms.
Silêncio (envelope abaixo de LIM por >= MIN ms) é encurtado para ALVO_FRASE no fim de frase e ALVO_MEIO no
meio da frase. O corte é feito em quadros inteiros e o áudio é cortado nos mesmos instantes (sem deriva),
com emenda de 5 ms. Erros de gravação (repetição, recomeço) entram em `manuais` no cortes.json.
"""
import os, sys, json, csv, wave, subprocess, argparse
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
LEVE = os.path.join(AQUI, '..', 'ferramentas', 'leve.py')   # trava: um comando pesado por vez, com teto de memória
LIM, MIN, ALVO_FRASE, ALVO_MEIO = -45.0, 140, 110, 90

ap = argparse.ArgumentParser()
ap.add_argument('video'); ap.add_argument('bruto'); ap.add_argument('saida')
ap.add_argument('--crop', type=int, required=True); ap.add_argument('--largura', type=int, default=810)
ap.add_argument('--renderiza', action='store_true')
ap.add_argument('--corrige', default='', help='índice=palavra,índice=palavra (correções de texto da transcrição)')
a = ap.parse_args()
os.makedirs(a.saida, exist_ok=True)

pr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate,nb_frames,width,height',
                     '-of', 'json', a.video], capture_output=True, text=True)
st = json.loads(pr.stdout)['streams'][0]
num, den = map(int, st['r_frame_rate'].split('/')); fps = num / den; fd = 1000 / fps; NQ = int(st['nb_frames']); H = st['height']
P = json.load(open(os.path.join(a.bruto, 'palavras.json'), encoding='utf-8'))
ws = P['palavras']
for par in [p for p in a.corrige.split(',') if p]:
    i, t = par.split('='); i = int(i)
    pont = ''.join(c for c in ws[i]['palavra'] if c in '.,?!;:')
    ws[i]['palavra_whisper'] = ws[i]['palavra']; ws[i]['palavra'] = t + pont
env = np.array([float(r['db']) for r in csv.DictReader(open(os.path.join(a.bruto, 'envelope.csv')))])

# silêncios
sil, i = [], 0
while i < len(env):
    if env[i] < LIM:
        j = i
        while j + 1 < len(env) and env[j + 1] < LIM: j += 1
        if (j - i + 1) * 10 >= MIN: sil.append((i * 10, (j + 1) * 10))
        i = j + 1
    else: i += 1
cortes = []
for s0, s1 in sil:
    if s0 == 0 or s1 >= len(env) * 10: continue          # cabeça e cauda ficam
    meio = (s0 + s1) / 2
    ant = [w for w in ws if w['ini_ms'] < meio]; dep = [w for w in ws if w['ini_ms'] >= meio - 1]
    if not ant: continue
    fim_frase = ant[-1]['palavra'][-1] in '.?!'
    alvo = ALVO_FRASE if fim_frase else ALVO_MEIO
    n = int((s1 - s0 - alvo) // fd)
    if n < 1: continue
    f0 = int(round((s0 + (s1 - s0 - n * fd) / 2) / fd))
    cortes.append({'f0': f0, 'n': n, 'de_ms': round(f0 * fd), 'ate_ms': round((f0 + n) * fd), 'tirou_ms': round(n * fd),
                   'silencio_ms': [s0, s1], 'sobrou_ms': round(s1 - s0 - n * fd), 'tipo': 'fim de frase' if fim_frase else 'meio de frase',
                   'entre': f"{ant[-1]['palavra']} | {dep[0]['palavra'] if dep else ''}"})
man = os.path.join(a.saida, 'manuais.json')
if os.path.exists(man): cortes += json.load(open(man, encoding='utf-8'))
cortes.sort(key=lambda c: c['f0'])

# segmentos mantidos e remapeamento
seg, p = [], 0
for c in cortes:
    seg.append((p, c['f0'])); p = c['f0'] + c['n']
seg.append((p, NQ))
NOVO = sum(b - x for x, b in seg)
def remap(ms):
    t = ms
    for c in cortes:
        ini, fim = c['f0'] * fd, (c['f0'] + c['n']) * fd
        if ms >= fim: t -= (fim - ini)
        elif ms > ini: t -= (ms - ini)
    return int(round(t))
for w in ws:
    w['ini_bruto_ms'], w['fim_bruto_ms'] = w['ini_ms'], w['fim_ms']
    w['ini_ms'], w['fim_ms'] = remap(w['ini_ms']), remap(w['fim_ms'])
out = {'video': a.video, 'fps': fps, 'fps_fracao': f'{num}/{den}', 'quadros_bruto': NQ, 'quadros_corte': NOVO, 'duracao_corte_ms': round(NOVO * fd),
       'crop': {'x0': a.crop, 'y0': 0, 'w': a.largura, 'h': H}, 'saida': '1080x1920',
       'parametros': {'limiar_db': LIM, 'silencio_minimo_ms': MIN, 'alvo_fim_de_frase_ms': ALVO_FRASE, 'alvo_meio_ms': ALVO_MEIO},
       'cortes': cortes, 'segmentos_quadros': seg}
json.dump(out, open(os.path.join(a.saida, 'cortes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'fps': fps, 'palavras': ws}, open(os.path.join(a.saida, 'palavras-corte.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
with open(os.path.join(a.saida, 'cortes.md'), 'w', encoding='utf-8') as f:
    f.write(f'# Corte limpo\n\nBruto: {NQ} quadros ({NQ*fd/1000:.2f} s) → corte: {NOVO} quadros ({NOVO*fd/1000:.2f} s). '
            f'Tirado: {sum(c["tirou_ms"] for c in cortes)} ms em {len(cortes)} cortes.\n\n'
            '| # | no bruto (s) | silêncio medido (ms) | tirou (ms · quadros) | sobrou (ms) | tipo | entre |\n|---|---|---|---|---|---|---|\n')
    for k, c in enumerate(cortes, 1):
        f.write(f"| {k} | {c['de_ms']/1000:.2f}–{c['ate_ms']/1000:.2f} | {c['silencio_ms'][1]-c['silencio_ms'][0]} | {c['tirou_ms']} · {c['n']} | {c['sobrou_ms']} | {c['tipo']} | {c['entre']} |\n")
print(open(os.path.join(a.saida, 'cortes.md'), encoding='utf-8').read())

if a.renderiza:
    w = wave.open(os.path.join(a.bruto, 'audio-48k.wav')); sr, ch = w.getframerate(), w.getnchannels()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, ch).astype(np.float32)
    partes, em = [], int(sr * 0.005)
    for x0, x1 in seg:
        s = x[int(round(x0 * fd / 1000 * sr)):int(round(x1 * fd / 1000 * sr))].copy()
        partes.append(s)
    y = partes[0]
    for s in partes[1:]:                                   # emenda de 5 ms (cruzada)
        r = np.linspace(0, 1, em)[:, None]
        y[-em:] = y[-em:] * (1 - r) + s[:em] * r
        y = np.concatenate([y, s[em:]])
    # repõe as amostras gastas nas emendas para o áudio não encurtar: estica nada, só completa com o fim real
    alvo = int(round(NOVO * fd / 1000 * sr))
    if len(y) < alvo: y = np.concatenate([y, np.zeros((alvo - len(y), ch), np.float32)])
    wav = os.path.join(a.saida, 'audio-corte.wav')
    wo = wave.open(wav, 'w'); wo.setnchannels(ch); wo.setsampwidth(2); wo.setframerate(sr); wo.writeframes(y.astype(np.int16).tobytes()); wo.close()
    sel = '+'.join(f'between(n,{x0},{x1-1})' for x0, x1 in seg)
    vf = f"select='{sel}',setpts=N/({num}/{den})/TB,crop={a.largura}:{H}:{a.crop}:0,scale=1080:1920:flags=lanczos"
    dest = os.path.join(a.saida, 'clipe-limpo.mp4')
    r = subprocess.run([sys.executable, LEVE, '--teto-gb', '4', '--min-livre-gb', '2.5', '--rotulo', 'e3-corte', '--',
                        'ffmpeg', '-v', 'error', '-y', '-i', a.video, '-i', wav, '-map', '0:v', '-map', '1:a', '-vf', vf,
                        '-r', f'{num}/{den}', '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                        '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', dest])
    print('render:', r.returncode, dest)
