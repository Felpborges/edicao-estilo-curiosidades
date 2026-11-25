#!/usr/bin/env python3
"""legenda.py · legenda do Estilo 03 (P01), molde de `04-specs/00-globais.md` §7.

Uma linha amarela em tarja preta translúcida, presa à tela, troca seca na 1ª palavra do bloco, sem vão nas pausas.
"""
import numpy as np
import cv2
from PIL import Image, ImageDraw
from pecas import fonte, bgr, LEGENDA, do_guia
import perfis

CURTAS = {'o', 'a', 'os', 'as', 'um', 'uma', 'de', 'do', 'da', 'em', 'no', 'na', 'e', 'que', 'pra', 'com', 'por', 'se', 'é',
          'dos', 'das', 'nos', 'nas', 'pro', 'ao'}           # as 6 últimas: contrações do mesmo tipo (inferido)
ALVO, MAX_PAL, MAX_CAR, TETO_CAR, MIN_MS, PAUSA_MS = 2, 4, 21, 28, 292, 100
CORPO, TARJA_Y0, TARJA_Y1, BASE_Y, RAIO, FOLGA, OPACIDADE = 52, 1266, 1336, 1322, 12, 9, 0.75


def _limpa(p): return p.strip('.,?!:;').lower()
def _pontua(p): return p[-1] in '.,?!:;'


def blocos(palavras, fim_clipe_ms, ajustes=None):
    """palavras: [{palavra, ataque_ms, fim_ms, silencio_antes_ms}]. ajustes: {índice: texto} (ex.: número em algarismo).
    Devolve [{i0, i1, texto, de_ms, ate_ms}]."""
    ws = [dict(w) for w in palavras]
    for k, v in (ajustes or {}).items():
        pont = ''.join(c for c in ws[int(k)]['palavra'] if c in '.,?!:;')
        ws[int(k)]['palavra'] = v + pont
    n = len(ws)
    car = lambda b: len(' '.join(ws[i]['palavra'] for i in b))
    # pausa curta depois de palavra de ligação ("e", "que", "pra"…) não quebra: ela gruda na palavra seguinte (regra 2)
    quebra = lambda i: _pontua(ws[i]['palavra']) or (i + 1 < n and ws[i + 1].get('silencio_antes_ms', 0) >= PAUSA_MS
                                                      and _limpa(ws[i]['palavra']) not in CURTAS)
    bs, i = [], 0
    while i < n:
        b = [i]
        while b[-1] < n - 1 and not quebra(b[-1]):
            cand = b + [b[-1] + 1]
            if len(cand) > MAX_PAL or car(cand) > MAX_CAR: break
            if _limpa(ws[b[-1]]['palavra']) in CURTAS or len(b) < ALVO: b = cand
            else: break
        while len(b) > 1 and _limpa(ws[b[-1]]['palavra']) in CURTAS and not quebra(b[-1]) and b[-1] < n - 1:
            b.pop()                                           # palavra curta não fica pendurada no fim: abre o bloco seguinte
        bs.append(b); i = b[-1] + 1
    # bloco curto demais se junta ao vizinho, se couber e não atravessar pontuação
    dur = lambda k: (ws[bs[k + 1][0]]['ataque_ms'] if k + 1 < len(bs) else fim_clipe_ms) - ws[bs[k][0]]['ataque_ms']
    k = 0
    while k < len(bs):
        if dur(k) < MIN_MS and len(bs) > 1:
            if k + 1 < len(bs) and not quebra(bs[k][-1]) and len(bs[k]) + len(bs[k + 1]) <= MAX_PAL and car(bs[k] + bs[k + 1]) <= TETO_CAR:
                bs[k] = bs[k] + bs.pop(k + 1); continue
            if k > 0 and not quebra(bs[k - 1][-1]) and len(bs[k - 1]) + len(bs[k]) <= MAX_PAL and car(bs[k - 1] + bs[k]) <= TETO_CAR:
                bs[k - 1] = bs[k - 1] + bs.pop(k); continue
        k += 1
    out = []
    for k, b in enumerate(bs):
        de = ws[b[0]]['ataque_ms']
        ate = ws[bs[k + 1][0]]['ataque_ms'] if k + 1 < len(bs) else min(fim_clipe_ms, ws[b[-1]]['fim_ms'] + MIN_MS)
        out.append({'i0': b[0], 'i1': b[-1], 'texto': ' '.join(ws[i]['palavra'] for i in b), 'de_ms': de, 'ate_ms': ate})
    return out


class Legenda:
    def __init__(self, blocos_, quadro_ms, cor=LEGENDA, opacidade=OPACIDADE):
        # geometria da tarja: a do perfil de acabamento ativo (guia G12.2 e "Sistema de legendas"); sem perfil, a antiga
        P = perfis.ativo(); T = None if P.get('antigo') else P['tarja']
        if T:
            self.y0, self.y1, self.base_y, self.raio, self.folga = T['y0'], T['y1'], T['base_y'], T['raio'], T['folga']
            corpo = int(round(T['maiuscula'] / 0.727))          # Inter: altura da maiúscula = 0,727 do corpo
            cor, opacidade = do_guia(T['cor']), T['op']
        else:
            self.y0, self.y1, self.base_y, self.raio, self.folga, corpo = TARJA_Y0, TARJA_Y1, BASE_Y, RAIO, FOLGA, CORPO
        self.f, self.nome_fonte = fonte(corpo)
        self.quadro_ms, self.opacidade, self.cor = quadro_ms, opacidade, tuple(reversed(bgr(cor)))
        self.some = []                      # [(q0, q1)] trechos sem legenda (ex.: plano com texto grande sobre o rosto)
        self.b = [dict(b, q0=int(round(b['de_ms'] / quadro_ms)), q1=int(round(b['ate_ms'] / quadro_ms))) for b in blocos_]
        for a, b in zip(self.b, self.b[1:]): a['q1'] = b['q0']           # troca seca, sem vão
        self.cache = {}

    def cola_nos_cortes(self, cortes, folga=2):
        """Troca de bloco que cairia até `folga` quadros DEPOIS de um corte passa para o quadro do corte, para a
        legenda da frase anterior não ficar 1 ou 2 quadros sobre o plano novo (o corte cai 42 ms antes da palavra;
        a referência aceita a legenda de −100 a +50 ms da palavra)."""
        for k in range(1, len(self.b)):
            for c in cortes:
                if c < self.b[k]['q0'] <= c + folga:
                    self.b[k]['q0'] = c; self.b[k - 1]['q1'] = c

    def _faixa(self, texto):
        if texto not in self.cache:
            FOLGA, RAIO, TARJA_Y0, TARJA_Y1, BASE_Y = self.folga, self.raio, self.y0, self.y1, self.base_y
            lt = int(np.ceil(self.f.getlength(texto))); w = lt + 2 * FOLGA; h = TARJA_Y1 - TARJA_Y0
            ss = 4
            m = Image.new('L', (w * ss, h * ss), 0)
            ImageDraw.Draw(m).rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], RAIO * ss, fill=255)
            tarja = np.asarray(m.resize((w, h), Image.LANCZOS), np.float32) / 255 * self.opacidade
            t = Image.new('L', (w, h), 0)
            ImageDraw.Draw(t).text((FOLGA, BASE_Y - TARJA_Y0), texto, font=self.f, fill=255, anchor='ls')
            self.cache[texto] = (tarja[..., None], (np.asarray(t, np.float32) / 255)[..., None], w, h)
        return self.cache[texto]

    def bloco_em(self, q):
        for b in self.b:
            if b['q0'] <= q < b['q1']: return b
        return None

    def poe(self, quadro_bgr, q):
        """Desenha a legenda do quadro q sobre a imagem (uint8 BGR), no lugar."""
        b = self.bloco_em(q)
        if not b or any(a <= q < z for a, z in self.some): return quadro_bgr
        TARJA_Y0, TARJA_Y1 = self.y0, self.y1
        tarja, txt, w, h = self._faixa(b['texto'])
        x0 = (quadro_bgr.shape[1] - w) // 2
        reg = quadro_bgr[TARJA_Y0:TARJA_Y1, x0:x0 + w].astype(np.float32)
        reg *= (1 - tarja)                                               # tarja preta translúcida
        cor = np.array(self.cor[::-1], np.float32)[None, None]           # BGR
        reg = reg * (1 - txt) + cor * txt
        quadro_bgr[TARJA_Y0:TARJA_Y1, x0:x0 + w] = np.clip(reg, 0, 255).astype(np.uint8)
        return quadro_bgr
