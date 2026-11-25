#!/usr/bin/env python3
"""e3.py · núcleo do motor do Estilo 03 (nasceu nesta pasta, do zero; não usa nada dos outros estilos).

Só numpy + OpenCV + Pillow (+ ffmpeg para codificar). Roda igual em Windows, macOS e Linux.

Modelo: uma "mesa" (plano do mundo, em px de tela com zoom 1, origem no centro do quadro), peças RGBA
pousadas nela (cartão, recorte, disco, etiqueta, documento) e uma câmera virtual (centro, zoom, giro).
Tudo é função do tempo em ms. Tela: 1080x1920. Giro positivo = horário.

    tela = zoom · R(giro_cam) · (mundo − centro_cam) + centro_da_tela
    mundo = pos + escala · R(giro) · (px_da_imagem − centro_da_imagem)
"""
import math
import numpy as np
import cv2

W, H = 1080, 1920
FPS_N, FPS_D = 24000, 1001
QUADRO_MS = 1000.0 * FPS_D / FPS_N


# ───────── curvas (u de 0 a 1) ─────────
def linear(u): return u
def sai_devagar(u): return 1 - (1 - u) ** 3                    # ease-out: chega freando
def entra_devagar(u): return u ** 3                            # ease-in: sai acelerando
def lento_rapido_lento(u): return u * u * (3 - 2 * u)           # smoothstep
def freio_longo(u): return 1 - (1 - u) ** 5


class Trilha:
    """Valor no tempo por chaves [(t_ms, valor, curva_até_esta_chave)]. `degrau` (ms) segura o tempo em passos
    (ex.: 2 quadros) para o movimento em degraus que a referência usa nos estalos."""
    def __init__(self, chaves, degrau=0.0, t0=0.0):
        self.c = [(float(t), float(v), (k[2] if len(k) > 2 else linear)) for k in chaves for t, v in [k[:2]]]
        self.degrau, self.t0 = degrau, t0

    def __call__(self, t):
        if self.degrau:
            t = self.t0 + math.floor((t - self.t0) / self.degrau + 1e-6) * self.degrau
        c = self.c
        if t <= c[0][0]: return c[0][1]
        if t >= c[-1][0]: return c[-1][1]
        for (t0, v0, _), (t1, v1, f) in zip(c, c[1:]):
            if t0 <= t <= t1:
                return v0 if t1 == t0 else v0 + (v1 - v0) * f((t - t0) / (t1 - t0))
        return c[-1][1]


def const(v): return lambda t: v
def como_funcao(x): return x if callable(x) else const(x)


class Camera:
    def __init__(self, cx=0, cy=0, zoom=1.0, giro=0.0):
        self.cx, self.cy, self.zoom, self.giro = map(como_funcao, (cx, cy, zoom, giro))


class Peca:
    """Imagem RGBA (uint8, alfa reto) pousada na mesa. `fixa=True` prende a peça à tela (ignora a câmera)."""
    def __init__(self, rgba, x=0, y=0, escala=1.0, giro=0.0, alfa=1.0, z=0, de=-1e12, ate=1e12, fixa=False, nome='',
                 modo='normal', revela=None, variantes=None, sem_grao=False):
        """modo='multiplica' = marca-texto (escurece o que está por baixo com a cor da peça).
        revela = função do tempo → fração da largura já visível, da esquerda para a direita (varredura).
        variantes = [(t_ms, rgba), ...] do mesmo tamanho: troca a imagem a seco a partir de cada t (traço em degraus,
        etiqueta que ganha palavras)."""
        self.troca = [(-1e12, self._mips(rgba))] + [(float(t), self._mips(r)) for t, r in (variantes or [])]
        self.w, self.h = rgba.shape[1], rgba.shape[0]
        self.x, self.y, self.escala, self.giro, self.alfa = map(como_funcao, (x, y, escala, giro, alfa))
        self.z, self.de, self.ate, self.fixa, self.nome, self.modo, self.revela = z, de, ate, fixa, nome, modo, revela
        self.sem_grao = sem_grao          # True = o grão vivo do perfil não cai sobre esta peça (texto do editor, traço)

    @staticmethod
    def _mips(rgba):
        a = rgba[:, :, 3:4].astype(np.float32) / 255.0
        mips = [np.dstack([rgba[:, :, :3].astype(np.float32) * a, a * 255.0])]     # pré-multiplicado, float32
        while min(mips[-1].shape[:2]) > 64:                                         # pirâmide p/ reduzir sem serrilhado
            m = mips[-1]
            mips.append(cv2.resize(m, (max(1, m.shape[1] // 2), max(1, m.shape[0] // 2)), interpolation=cv2.INTER_AREA))
        return mips

    def mips_em(self, t):
        atual = self.troca[0][1]
        for t0, m in self.troca:
            if t >= t0: atual = m
        return atual

    def matriz(self, t, cam):
        s, g = self.escala(t), math.radians(self.giro(t))
        px, py = self.x(t), self.y(t)
        if self.fixa: z, cg, ox, oy = 1.0, 0.0, 0.0, 0.0
        else: z, cg, ox, oy = cam.zoom(t), math.radians(cam.giro(t)), cam.cx(t), cam.cy(t)
        k = z * s; ang = g + cg
        c, sn = math.cos(ang), math.sin(ang)
        A = np.array([[k * c, -k * sn], [k * sn, k * c]])
        cc, cs = math.cos(cg), math.sin(cg)
        pos = z * (np.array([[cc, -cs], [cs, cc]]) @ np.array([px - ox, py - oy])) + np.array([W / 2, H / 2])
        tr = pos - A @ np.array([self.w / 2, self.h / 2])
        return np.hstack([A, tr[:, None]]), k


def compoe(tela, peca, t, cam, cob=None):
    """Pousa a peça na tela (float32 BGR 0..255), com alfa pré-multiplicado.
    `cob` (H, W) acumula onde há peça, para o grão vivo do perfil cair só sobre as peças, nunca na mesa."""
    if not (peca.de <= t < peca.ate): return
    op = peca.alfa(t)
    if op <= 0: return
    M, k = peca.matriz(t, cam)
    mips = peca.mips_em(t); nivel = 0
    while nivel + 1 < len(mips) and k < 0.5:            # usa o mip mais próximo acima da escala pedida
        k *= 2; nivel += 1
    src = mips[nivel]
    Mn = M.copy(); Mn[:, :2] *= peca.w / src.shape[1]
    if peca.revela is not None:
        fr = max(0.0, min(1.0, peca.revela(t)))
        if fr <= 0: return
        src = src[:, :max(1, int(round(src.shape[1] * fr)))]
    cant = np.array([[0, 0, 1], [src.shape[1], 0, 1], [0, src.shape[0], 1], [src.shape[1], src.shape[0], 1]]).T
    p = Mn @ cant
    x0, y0 = int(max(0, math.floor(p[0].min()))), int(max(0, math.floor(p[1].min())))
    x1, y1 = int(min(W, math.ceil(p[0].max()) + 1)), int(min(H, math.ceil(p[1].max()) + 1))
    if x1 <= x0 or y1 <= y0: return
    Mr = Mn.copy(); Mr[0, 2] -= x0; Mr[1, 2] -= y0
    out = cv2.warpAffine(src, Mr, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    a = out[:, :, 3:4] * (op / 255.0)
    reg = tela[y0:y1, x0:x1]
    if peca.modo == 'multiplica':
        cor = np.where(out[:, :, 3:4] > 1e-3, out[:, :, :3] / np.maximum(out[:, :, 3:4] / 255.0, 1e-3), 255.0)
        reg *= (1 - a) + a * cor / 255.0
    else:
        reg *= (1 - a); reg += out[:, :, :3] * op
        if cob is not None:
            c = cob[y0:y1, x0:x1]
            if peca.sem_grao: c *= (1 - a[:, :, 0])
            else: np.maximum(c, a[:, :, 0], out=c)


class Cena:
    """Fundo fixo na tela + peças + câmera. `borrao` = [(de_ms, ate_ms, n_amostras)] para borrão de movimento
    por média de subquadros nos trechos em que a referência borra.

    `perfil` (dict de perfis.py) liga o acabamento do reestudo:
      · grão vivo: ruído sorteado de novo a cada imagem, proporcional à luma, só onde há peça (nunca na mesa);
      · luz_por_cima: poça de luz da cena, presa à tela, por cima da mesa E das peças (perfil V04); `luz` troca a força
        desta cena (quanto sobra na borda, 0 a 1), porque na referência ela muda de cena para cena;
      · cadencia_q: a cena inteira anda de N em N quadros (perfil V01 = 2, isto é, 12 imagens por segundo).
    A mesa fica parada na tela: só as peças andam com a câmera."""
    def __init__(self, fundo, camera=None, borrao=(), vinheta=None, perfil=None, luz=None, semente=0):
        self.fundo = fundo.astype(np.float32); self.cam = camera or Camera(); self.pecas = []; self.borrao = list(borrao)
        self.vinheta = vinheta            # fator (H, W, 1) preso à tela, aplicado por cima das peças (acabamento antigo)
        self.perfil = perfil or {}; self.semente = semente
        self.grao = self.perfil.get('grao_vivo'); self.cad = int(self.perfil.get('cadencia_q', 1) or 1)
        lz = self.perfil.get('luz_por_cima')
        if lz:
            self.vinheta = luz_de_cena(lz['cx'], lz['cy'], lz['sobra'] if luz is None else luz, lz['inicio'])

    def poe(self, peca): self.pecas.append(peca); return peca

    def _quadro(self, t):
        tela = self.fundo.copy()
        cob = np.zeros((H, W), np.float32) if self.grao else None
        for p in sorted(self.pecas, key=lambda q: q.z):
            compoe(tela, p, t, self.cam, cob)
        if self.grao:
            g = self.grao
            n = int(math.floor(t / QUADRO_MS + 1e-6)) // int(g.get('passo_q', 1))
            r = np.random.default_rng(self.semente * 1000003 + n).standard_normal((H, W), dtype=np.float32)
            if g.get('desfoque', 0) > 0:
                r = cv2.GaussianBlur(r, (0, 0), g['desfoque']); r /= max(1e-6, float(r.std()))
            luma = 0.114 * tela[:, :, 0] + 0.587 * tela[:, :, 1] + 0.299 * tela[:, :, 2]
            tela += (r * luma * cob * (g['k'] * g.get('ganho', 1.0)))[:, :, None]
        if self.vinheta is not None: tela *= self.vinheta
        return tela

    def quadro(self, t):
        if self.cad > 1:                                            # a cena inteira em passos (12 imagens por segundo)
            t = math.floor(t / (QUADRO_MS * self.cad) + 1e-6) * QUADRO_MS * self.cad
        for de, ate, n in self.borrao:
            if de <= t < ate:
                ac = np.zeros_like(self.fundo)
                for i in range(n): ac += self._quadro(t + QUADRO_MS * (i + 0.5) / n * 0.5)   # obturador de 180°
                return np.clip(ac / n, 0, 255).astype(np.uint8)
        return np.clip(self._quadro(t), 0, 255).astype(np.uint8)


def luz_de_cena(cx=0.5, cy=0.42, sobra=0.55, inicio=0.2):
    """Poça de luz presa à tela (H, W, 1): 1 no centro (cx, cy em fração do quadro), caindo até `sobra` na borda mais
    distante. Perfil V04: fica por cima da mesa e das peças."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    dx = (xx / W - cx) / max(cx, 1 - cx); dy = (yy / H - cy) / max(cy, 1 - cy)
    r = np.sqrt(dx * dx + dy * dy) / math.sqrt(2)
    u = np.clip((r - inicio) / (1 - inicio), 0, 1); u = u * u * (3 - 2 * u)
    return (1 - (1 - sobra) * u)[..., None]


class ZoomPorTaxa:
    """Zoom de câmera descrito como a referência mede: TAXA em %/s ao longo do tempo (guia G12.3).
    chaves = [(t_ms, taxa_%_por_s), ...]; a taxa varia em linha reta entre as chaves e fica constante fora delas.
    zoom(t) = z0 · exp(∫ taxa/100 dt). Assim a câmera tem fases (repouso, pico na palavra, freio, recuo, pausa)
    em vez de um zoom igual do 1º ao último quadro."""
    def __init__(self, t0, chaves, z0=1.0):
        self.t0, self.z0 = float(t0), float(z0)
        self.c = sorted((float(t), float(r)) for t, r in chaves)

    def taxa(self, t):
        c = self.c
        if t <= c[0][0]: return c[0][1]
        if t >= c[-1][0]: return c[-1][1]
        for (ta, ra), (tb, rb) in zip(c, c[1:]):
            if ta <= t <= tb: return ra if tb == ta else ra + (rb - ra) * (t - ta) / (tb - ta)
        return c[-1][1]

    def _integral(self, t):                      # ∫ da taxa de t0 até t, em % (trapézios)
        pts = sorted({self.t0, t} | {tk for tk, _ in self.c if min(self.t0, t) < tk < max(self.t0, t)})
        s = sum((b - a) / 1000.0 * (self.taxa(a) + self.taxa(b)) / 2 for a, b in zip(pts, pts[1:]))
        return s if t >= self.t0 else -s

    def __call__(self, t): return self.z0 * math.exp(self._integral(t) / 100.0)


def fases_pico(t_ini, t_palavra, repouso=4.0, pico=30.0, atraso_ms=135.0, subida_ms=330.0, freio_ms=900.0, depois=None):
    """Chaves de taxa para a fase mais comum da referência: deriva de repouso, PICO de aproximação logo depois da
    palavra-chave (≈ 135 ms depois dela) e freio longo de volta ao repouso (`depois`, se a taxa final for outra).
    Use com ZoomPorTaxa; junte listas para cenas com mais de uma palavra de peso.
    Com os valores de fábrica o pico soma ≈ ×1,23 de zoom (referência: ×1,13 a ×1,39; picos de +11 a +61 %/s)."""
    tp = t_palavra + atraso_ms
    return [(t_ini, repouso), (tp - subida_ms, repouso), (tp, pico), (tp + freio_ms, repouso if depois is None else depois)]


def pausa(t_de, t_ate, antes=4.0, durante=0.3, depois=None, rampa_ms=250.0):
    """Chaves de taxa para a pausa da câmera enquanto a mão ou a ferramenta trabalha (traço, marca-texto, lista)."""
    return [(t_de - rampa_ms, antes), (t_de, durante), (t_ate, durante), (t_ate + rampa_ms, antes if depois is None else depois)]


def bezier(x1, y1, x2, y2):
    """cubic-bezier(x1, y1, x2, y2) como função u → v (as curvas de 00-globais.md §8)."""
    def f(u):
        if u <= 0: return 0.0
        if u >= 1: return 1.0
        a, b = 0.0, 1.0
        for _ in range(24):
            m = (a + b) / 2
            x = 3 * (1 - m) ** 2 * m * x1 + 3 * (1 - m) * m * m * x2 + m ** 3
            if x < u: a = m
            else: b = m
        m = (a + b) / 2
        return 3 * (1 - m) ** 2 * m * y1 + 3 * (1 - m) * m * m * y2 + m ** 3
    return f


viagem = bezier(0.45, 0, 0.55, 1)         # lento-rápido-lento (viagem, empurrão, push-in forte)
chega = bezier(0.16, 1, 0.3, 1)           # ease-out forte (chicote, cobertura)
sai = bezier(0.55, 0, 1, 0.45)            # ease-in (quem deixa a mesa)


def tabela(t0, valores, passo_q=1):
    """Chaves de Trilha a partir de uma lista de valores quadro a quadro medidos na referência
    (um valor a cada `passo_q` quadros, começando em t0)."""
    return [(t0 + i * passo_q * QUADRO_MS, v) for i, v in enumerate(valores)]
