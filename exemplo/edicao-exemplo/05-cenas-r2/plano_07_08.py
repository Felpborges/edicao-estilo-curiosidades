#!/usr/bin/env python3
"""plano_07_08 · O pedido em tela cheia com marca-texto (trecho 7 + trecho 8) · P20 layout B · Ref V04-A35.
Spec: `04-specs/trecho-07.md`. Corte seco do rosto para o print do compositor já no tamanho final; marca-texto 1 em
"apresentação" (i58), marca-texto 2 em "seu" (i61); corte seco para a parede de slides (plano_09_10).

2ª rodada (corte 04), perfil V03 (`../05-cenas/plano_07_08.py` é o corte 03):
· acabamento: saiu a vinheta-spot da tela cheia (vinha da luz de cena do V04); o print fica com o grão vivo do perfil
  sobre a mesa do perfil, sem sombra (tela cheia, sem borda, como a Ref). Marca-texto em multiplicar, sem grão próprio:
  pega o grão do papel por baixo (Ref: "não tem textura própria").
· câmera por fases (G12.3), tirada da câmera MEDIDA na V04-A35: aproximação lenta e quieta, +1,9 a +2,1 %/s nos pares
  medidos durante a varredura, depois dela e no fim; +2,7 %/s na cena toda. Sem pico: na Ref o marca-texto corre com a
  câmera quieta, por isso o pico de +20 %/s que o painel pedia em "apresentação comercial" não entra (vale a Ref).
  Repouso +2,7 %/s antes da 1ª varredura (a Ref não tem esse trecho: usa o valor da Ref na cena toda), freia para
  +2,0 %/s ao começar a 1ª varredura e fica assim nas duas, e segue freando até +1,9 %/s no corte (painel do trecho 8;
  Ref: fim +1,9 %/s). Corta andando."""
import numpy as np
import e3, pecas, base

Q = e3.QUADRO_MS

# ───────── o print (px do print JÁ ESCALADO para 1080 x 1649, origem no canto de cima à esquerda) ─────────
PRINT_W, PRINT_H = 1080, 1649          # spec §2: largura 100 %, altura 85,9 %
PRINT_TOPO = 151                       # topo do print na tela no 1º quadro (faixa escura de 151 px acima)

# Posição das palavras marcadas no print escalado: (x, y, largura, altura) da FAIXA do marca-texto, em px do print.
MARCA_1 = (268, 640, 459, 50)          # "apresentação comercial" (linha 1), medido na captura real em 20/11
MARCA_2 = (93, 696, 158, 50)           # "negócio" (linha 2; "meu" ficou no fim da linha 1 e não é marcado)

COR_MARCA = pecas.do_guia('#ecc039')   # spec §2 (V04-A35 f2700), convertida do caminho JPG do treino

# varredura da linha 1, fração do comprimento final quadro a quadro (spec §2, remedida no V04, 12 q)
VARRE_1 = [0.04, 0.11, 0.19, 0.27, 0.34, 0.44, 0.52, 0.59, 0.69, 0.77, 0.88, 1.00]
VARRE_2 = [k / 6 for k in range(1, 7)]  # linha 2: linear, 1/6 por quadro (6 q)

# câmera (%/s): valores medidos na V04-A35 (notes.md, "Câmera" e "Câmera em 3 pares")
REPOUSO = 2.7          # cena toda na Ref (f2666→f2712); aqui, antes da 1ª varredura
NA_VARREDURA = 2.0     # par do começo da Ref (f2665→f2671), com o marca-texto correndo
FIM = 1.9              # par do fim da Ref (f2707→f2713)
RAMPA_MS = 250.0       # troca de taxa em ≈ 6 q, terminando no 1º quadro da varredura


def _no_mundo(xp, yp):
    """px do print escalado → coordenadas do mundo (câmera em zoom 1 no 1º quadro)."""
    return base.mundo(xp, PRINT_TOPO + yp)


def plano(ctx):
    f0, f1 = base.CORTES['plano_07_08']
    t0 = ctx.t(f0)

    # marca-texto 1: "apresentação comercial", 1º pixel −2 ms de "apresentação" (i58), 12 q, curva constante do V04
    q1 = ctx.q_palavra(58, -2); t1 = ctx.t(q1)
    # marca-texto 2: "meu negócio" (fala "seu negócio"), 1º pixel −2 ms de "seu" (i61), 6 q linear; espera a fala
    q2 = ctx.q_palavra(61, -2); t2 = ctx.t(q2)
    t2_fim = ctx.t(q2 + len(VARRE_2))           # fim da 2ª varredura

    # câmera por fases, ancorada no centro do trecho marcado 1 (spec §2, I): repouso → quieta nas varreduras → freia
    chaves = [(t0, REPOUSO), (t1 - RAMPA_MS, REPOUSO), (t1, NA_VARREDURA),
              (t2_fim, NA_VARREDURA), (ctx.t(f1), FIM)]
    zoom = base.zoom_fases(t0, chaves)
    ax, ay = MARCA_1[0] + MARCA_1[2] / 2, PRINT_TOPO + MARCA_1[1] + MARCA_1[3] / 2
    cx, cy = base.ancora(zoom, ax, ay)
    c = base.cena(e3.Camera(zoom=zoom, cx=cx, cy=cy), semente=7)   # perfil V03: sem vinheta por cima

    # o print do compositor, tela cheia, sem borda, sem sombra, giro 0, já assentado no corte (passo 1); grão vivo
    img = ctx.img('print-pedido', 1310, 2000, 'print-pedido\n(caixa com o pedido\ndigitado, sem enviar)')
    img = pecas._cobre(img[:, :, :3], PRINT_W, PRINT_H)
    rgba = np.dstack([img, np.full((PRINT_H, PRINT_W), 255, np.uint8)])
    px, py = _no_mundo(PRINT_W / 2, PRINT_H / 2)
    c.poe(e3.Peca(rgba, x=px, y=py, z=1, de=t0, nome='print-pedido'))

    for (mx, my, mw, mh), tm, varre, sem, nome in ((MARCA_1, t1, VARRE_1, 11, 'marca-1 apresentação comercial'),
                                                   (MARCA_2, t2, VARRE_2, 12, 'marca-2 meu negócio')):
        faixa = pecas.marca_texto(mw, mh, cor=COR_MARCA, semente=sem)
        x, y = _no_mundo(mx + mw / 2, my + mh / 2)
        c.poe(e3.Peca(faixa, x=x, y=y, z=2, de=tm, modo='multiplica',
                      revela=e3.Trilha(e3.tabela(tm, varre), degrau=Q, t0=tm), nome=nome))

    return {'nome': 'plano_07_08 · pedido em tela cheia com marca-texto', 'f0': f0, 'f1': f1, 'cena': c,
            'eventos': {'corte_entrada': f0, 'marca_1': q1, 'marca_1_completa': q1 + len(VARRE_1) - 1,
                        'marca_2': q2, 'marca_2_completa': q2 + len(VARRE_2) - 1, 'corte_saida': f1}}
