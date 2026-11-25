#!/usr/bin/env python3
"""plano_02 · "três ferramentas de IA totalmente gratuitas" · 3 discos creme + recortes (P14) + etiqueta "GRÁTIS"
(P05 variante B). Spec: `04-specs/trecho-02.md`. Refs: V01-A28 (grupos), V04-A09 (etiqueta).
Disposição dos grupos: `comum_discos.py` (volta igual no plano_15).
2ª rodada (corte 04): discos e recortes no acabamento do perfil V03 (via comum_discos), etiqueta com a sombra do perfil
(tipo 'etiqueta') no lugar da sombra feita à mão, grão vivo do perfil, câmera por fases (G12.3) no lugar do
crescimento por grupo do corte 03 (+6 / +2 %/s, que era a câmera feita à mão). A disposição em q44 (os três
assentados) é a mesma do corte 03: zoom 1, sem deslocamento. Auditoria: `auditoria-r2-plano_02.md`."""
import math
import numpy as np
import e3, pecas, base
import comum_discos as cd

Q = e3.QUADRO_MS

# trecho-02 §2 · etiqueta variante B (V04-A09): tira 56 px, papel #ddc5b1, corpo 41 px, margem 16 px
PAPEL_ETIQUETA = pecas.do_guia(base.PERFIL['etiqueta']['cor'])   # papel de etiqueta do perfil (V03: cinza-claro), igual às outras etiquetas do reel
# deslize de entrada da etiqueta: restante até a posição final, por quadro (px 1080) e giro (°) (A09, medido)
DESLIZE = [(528, 77), (354, 69), (211, 47), (101, 23), (29, 8), (0, 0)]
GIRO_DESLIZE = [4.0, 4.0, 0.0, 0.0, -1.5, -1.5]
ETIQ_CENTRO = (617.5, 1183)          # x 522–713 × y 1155–1211 na disposição (atravessa a borda de baixo do recorte 3)
PISO_TEXTO_MS = 700

# ── câmera por fases (G12.3) · taxas em %/s ──
# Ref V01-A28 (reestudo 20/11, medido): aproxima +3,4 %/s enquanto há 1 recorte; com os 3 na mesa, RECUA −3,5 a −4,2 %/s
# (−3,6 no fim) derivando para a direita 1,07–1,65 px/q em 720 (1,45 no fim). A Ref não tem palavra-chave com pico:
# lá o grupo sai em cascata na palavra do anúncio. Em "gratuitas" vale o painel: pico de +25 %/s com freio longo.
REPOUSO = 3.4                        # A28: +3,4 %/s com o 1º recorte (painel: +3)
RECUO = -3.8                         # A28: −3,5 a −4,2 %/s com os três
PICO = 25.0                          # painel (faixa da referência: +11 a +61)
RAMPA_RECUO_MS = 2 * Q               # vira de aproximação para recuo em 2 q, logo depois de o 3º assentar
ATRASO_MS, SUBIDA_MS, FREIO_MS = 135.0, 135.0, 900.0   # pico 135 ms depois de "gratuitas"; a subida começa NA palavra
DERIVA_PX_Q = 1.45 * 1.5             # A28 f1906→f1918: +1,45 px/q em 720 → 2,2 px/q em 1080, para a direita
DESCE_PX_Q = 1.7                     # trecho-02 §2 (A28 f1876→f1900): o conjunto desce 1,7 px/q até os 3 assentarem
ANCORA = (525, 786)                  # centro do conjunto (x 44–1005 × y 307–1265 na disposição)


def etiqueta_b():
    """Tira de papel com borda levemente irregular (papel cortado), cantos retos, sem contorno; sombra do perfil."""
    tira = pecas.etiqueta('GRÁTIS', altura=56, cor=PAPEL_ETIQUETA, corpo=41, folga=16)
    h, w = tira.shape[:2]
    rng = np.random.default_rng(13)
    # papel cortado: topo e base variam até 1 px, de forma suave (sem serrilhado)
    for idx in (0, h - 1):
        borda = np.convolve(rng.uniform(0, 1.2, w + 8), np.ones(9) / 9, 'valid')
        tira[idx, :, 3] = np.round(255 * (1 - np.clip(borda[:w], 0, 1))).astype(np.uint8)
    return pecas.com_sombra(tira, 'etiqueta')


def plano(ctx):
    f0, f1 = base.CORTES['plano_02']
    t = ctx.t

    # ── gatilhos (palavras reconferidas) · iguais ao corte 03 ──
    q_g1 = max(f0, ctx.q_palavra(5, -42))          # "três" (i5): nasce no corte
    q_g2 = max(ctx.q_palavra(6, -42), q_g1 + 4)    # "ferramentas" (i6): −42 ms (molde §8), sem sobrepor o pop do grupo 1
    q_g3 = ctx.q_palavra(7, +32)                   # "de" (i7): +32 ms (spec)
    q_ref = q_g3 + 4                               # grupo 3 assentado = a disposição da tabela (q46 da spec)
    q_desce0 = q_g2 + 4                            # câmera desce do assentar do grupo 2 ao do grupo 3

    # etiqueta: assenta no máximo 19 ms antes de "gratuitas" (i10) e nunca com menos de 700 ms parada até o corte
    q_et_fim = min(ctx.q_palavra(10, -19), f1 - math.ceil(PISO_TEXTO_MS / Q))
    q_et0 = q_et_fim - (len(DESLIZE) - 1)

    # ── câmera: zoom por fases (zoom 1 em q_ref = a disposição) + deriva de tela ──
    t_ref, t_gr = t(q_ref), ctx.ataque(10)          # "gratuitas"
    chaves = [(t(f0), REPOUSO), (t_ref, REPOUSO), (t_ref + RAMPA_RECUO_MS, RECUO)] + \
        e3.fases_pico(t_ref + RAMPA_RECUO_MS, t_gr, repouso=RECUO, pico=PICO, atraso_ms=ATRASO_MS,
                      subida_ms=SUBIDA_MS, freio_ms=FREIO_MS, depois=REPOUSO)[1:]
    zoom = base.zoom_fases(t_ref, chaves, 1.0)

    def desloc(tt):                                 # deslocamento das peças na tela (px), 0 em q_ref
        n = tt / Q
        if n <= q_ref: return 0.0, -DESCE_PX_Q * (q_ref - max(n, q_desce0))
        return DERIVA_PX_Q * (n - q_ref), 0.0
    ax, ay = base.mundo(*ANCORA)
    cam = e3.Camera(zoom=zoom,
                    cx=lambda tt: ax * (1 - 1 / zoom(tt)) - desloc(tt)[0] / zoom(tt),
                    cy=lambda tt: ay * (1 - 1 / zoom(tt)) - desloc(tt)[1] / zoom(tt))
    c = base.cena(cam, semente=2)

    # ── os 3 grupos (disco e recorte no MESMO quadro; disco cresce, recorte encolhe; degraus de 2 q) ──
    S = [e3.const(1.0)] * 3                         # o crescimento por grupo do corte 03 virou a câmera acima
    pops_d = [cd.pop(t(q_g1), [0.95, 1.007, 1.0]), cd.pop(t(q_g2), [0.84, 1.005, 1.0]), cd.pop(t(q_g3), [0.84, 1.005, 1.0])]
    pops_r = [cd.pop(t(q_g1), [1.078, 1.026, 1.0]), cd.pop(t(q_g2), [1.06, 1.015, 1.0]), cd.pop(t(q_g3), [1.08, 1.025, 1.0])]
    de = [(t(q_g1), t(q_g1)), (t(q_g2), t(q_g2)), (t(q_g3), t(q_g3))]
    cd.poe(c, ctx, de, pops_d, pops_r, S)

    # ── etiqueta "GRÁTIS": presa ao grupo 3; entra pela borda direita subindo na diagonal ──
    ex, ey = cd.no_grupo(2, ETIQ_CENTRO[0], ETIQ_CENTRO[1], S[2])
    t_e = t(q_et0)
    dxs = e3.Trilha(e3.tabela(t_e, [d[0] for d in DESLIZE]), degrau=Q, t0=t_e)
    dys = e3.Trilha(e3.tabela(t_e, [d[1] for d in DESLIZE]), degrau=Q, t0=t_e)
    gir = e3.Trilha(e3.tabela(t_e, GIRO_DESLIZE), degrau=Q, t0=t_e)
    c.poe(e3.Peca(etiqueta_b(), x=lambda tt: ex(tt) + dxs(tt), y=lambda tt: ey(tt) + dys(tt), escala=S[2], giro=gir,
                  z=30, de=t_e, nome='etiqueta GRÁTIS'))

    return {'nome': 'plano_02 · 3 discos + recortes + GRÁTIS', 'f0': f0, 'f1': f1, 'cena': c,
            'gatilhos': {'grupo1': q_g1, 'grupo2': q_g2, 'grupo3': q_g3, 'desce': (q_desce0, q_ref),
                         'direita': (q_ref, f1), 'etiqueta': (q_et0, q_et_fim)}}
