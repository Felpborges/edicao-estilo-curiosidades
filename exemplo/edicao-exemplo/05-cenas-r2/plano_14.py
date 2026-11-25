#!/usr/bin/env python3
"""plano_14 · "Então, ao invés de você pagar pelo Gamma ou pelo Canva," · P16 · ref V04-A02.

Corte seco para a mesa já montada (ajuste adotado): o maço de três notas do trecho 3 (mesmo arranjo, reduzido à caixa
de 625 px e deitado a −5°) + o cartão de papel creme à direita, vazio. Logo do Gamma desliza da direita e pousa em
"Gamma" (i133); logo do Canva desliza de baixo-direita e pousa em "Canva" (i136); ambos recorte-adesivo.

2ª rodada (corte 04), perfil V03: cédulas com a sombra do perfil ('recorte', sem contorno), logos com
`pecas.recorte_do_perfil` (contorno branco ondulado + sombra do perfil), papel creme pontilhado do perfil com a sombra
de 'cartao'; mesa do perfil, grão vivo (semente 14). Câmera por fases medida na V04-A02 (reestudo 20/11 e remedida
agora com `ferr2.py camera`, região do objeto): repouso +8 %/s desde o corte; vira em ≈ 10 q e chega a −11 %/s 2 q
antes do 1º quadro do Gamma (na Ref: −11,2 %/s em f110–f122, 1º item em f118); passa um pouco do ponto (−12,7 %/s)
enquanto o Gamma desliza e assenta em −10,4 %/s até o corte, que é andando. Sem pico em "Canva": na Ref o 2º item
entra no recuo (−10,4 %/s em f130–f142). O zoom gira em torno da borda esquerda do objeto (o maço), à meia altura,
como na Ref, e por isso o conteúdo escorrega para a esquerda no recuo. Auditoria: `auditoria-r2-plano_14.md`.

Posições da spec = quadro do corte (câmera em ×1, mundo = tela). Os deslizes dos logos são em px de TELA (frações
quadro a quadro da spec) somados ao ponto de pouso, que anda com a câmera; os tamanhos dos logos (370 e 336 px, com o
contorno) são os da tela no quadro em que assentam.
"""
import math
import numpy as np
import cv2
import e3, pecas, base

Q = e3.QUADRO_MS
CX, CY = e3.W / 2, e3.H / 2

F_GAMMA = [0.0, 0.18, 0.53, 0.70, 0.81, 0.95, 0.99, 1.00]           # k = 0…7 (spec 14, medido em V04-A02)
F_CANVA = [0.0, 0.23, 0.40, 0.60, 0.73, 0.83, 0.90, 0.97, 1.00]     # k = 0…8


def plano(ctx):
    f0, f1 = base.CORTES['plano_14']
    t = ctx.t
    t0 = t(f0)

    # ── gatilhos, recalculados nos ataques reconferidos (iguais ao corte 03) ──
    qG1 = ctx.q_palavra(133, -213)        # 1º quadro visível do Gamma: 213 ms antes de "Gamma"
    qG0, qGa = qG1 - 1, qG1 - 1 + 7       # k = 0 (fora do quadro) e assentado (k = 7)
    qV1 = ctx.q_palavra(136, -291)        # 1º quadro visível do Canva: 291 ms antes de "Canva,"
    qV0, qVa = qV1 - 1, qV1 - 1 + 8

    # ── câmera por fases (V04-A02 medida; quadros da Ref levados ao 1º quadro do Gamma: f118 ↔ qG1) ──
    # taxa de zoom em %/s · Ref: f32–44 +8,1 · f100–112 +8,5 · f104–116 −2,8 · f110–122 −11,2 · f114–126 −12,7 ·
    # f122–134 −10,7 · f130–142 −10,4 · f140–152 −10,4 (centros das janelas: f106, f110, f116, f120, f128, f136, f146)
    tq = lambda d: t(qG1 + d)
    zoom = base.zoom_fases(t0, [(t0, 8.0), (tq(-12), 8.0), (tq(-8), -2.8), (tq(-2), -11.2), (tq(2), -12.7),
                                (tq(10), -10.7), (tq(18), -10.4)])
    # âncora do zoom: na Ref o ponto que fica parado na tela (o "centro anda" de cada janela dividido por s − 1) cai na
    # borda esquerda do objeto do tema, à meia altura dele: f32–44 (137, 532) em 720, com a borda do objeto em x 132;
    # no recuo f122–f152 entre x −69 e +75 e y 597–652 (o objeto sangra a borda esquerda). Aqui o objeto é o maço:
    # borda esquerda x ≈ 200, meia altura y 922. O conteúdo anda para a esquerda no recuo (−32 px no centro do maço até
    # o corte) e para a direita no repouso, como na Ref, sem um pan à parte.
    ax, ay = base.ancora(zoom, 200, 922)
    memo = {}
    def cam(tt):
        if tt not in memo: memo[tt] = (zoom(tt), ax(tt), ay(tt))
        return memo[tt]
    camera = e3.Camera(zoom=lambda tt: cam(tt)[0], cx=lambda tt: cam(tt)[1], cy=lambda tt: cam(tt)[2])
    c = base.cena(camera, semente=14)

    def tela(wx, wy, tt):                 # mundo → tela
        z, cx_, cy_ = cam(tt)
        return z * (wx - cx_) + CX, z * (wy - cy_) + CY

    # ── maço de notas (arranjo do trecho 3, escalado para 625 px de largura e girado −5° como um todo) ──
    # trecho 3: notas 735 × 312, centros (492, 664) −6°, (545, 774) +4°, (487, 867) −3°; monte x 108–932, y 465–1042
    # KM = 625/825 (caixa do monte do trecho 3 → 625 px); conferido: a caixa das 3 notas giradas dá 624 px de largura.
    # A caixa (extremos das três notas já giradas) é centrada em (511, 922).
    KM = 625 / 825.0
    G = math.radians(-5.0)
    NOTAS = [(492, 664, -6.0), (545, 774, 4.0), (487, 867, -3.0)]
    larg_nota = 735 * KM
    alt_nota = larg_nota / 2.35
    def no_grupo(nx, ny):
        ox, oy = nx * KM, ny * KM
        return ox * math.cos(G) - oy * math.sin(G), ox * math.sin(G) + oy * math.cos(G)
    pts = []
    for nx, ny, ng in NOTAS:
        rx, ry = no_grupo(nx, ny); g = math.radians(ng - 5.0)
        for sx, sy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
            px, py = sx * larg_nota / 2, sy * alt_nota / 2
            pts.append((rx + px * math.cos(g) - py * math.sin(g), ry + px * math.sin(g) + py * math.cos(g)))
    mx = (min(p[0] for p in pts) + max(p[0] for p in pts)) / 2
    my = (min(p[1] for p in pts) + max(p[1] for p in pts)) / 2
    KN = 1.15                             # raster 1,15× (folga para a câmera)
    nw, nh = int(round(larg_nota * KN)), int(round(alt_nota * KN))
    nota = ctx.rgba('nota-100', nw, nh, 'nota-100')
    nota = cv2.resize(nota, (nw, nh), interpolation=cv2.INTER_AREA)
    nota = pecas.com_sombra(nota, 'recorte', sombra=sombra_em('recorte', KN))   # recorte justo (trecho 3: sem adesivo)
    for i, (nx, ny, ng) in enumerate(NOTAS):
        rx, ry = no_grupo(nx, ny)
        wx, wy = base.mundo(511 + rx - mx, 922 + ry - my)
        c.poe(e3.Peca(nota, x=wx, y=wy, escala=1 / KN, giro=ng - 5.0, z=1 + i, nome=f'nota {i + 1}'))

    # ── cartão de apoio: papel creme, caixa NA TELA 267 × 642 (extremos x/y, já com o giro), centro (938, 789), +4° ──
    # a spec mede os extremos (x 536–714, y 312–740 em 720); sem giro isso dá 223,7 × 627,9 px
    KP = 1.15
    cor_papel = pecas.do_guia('#bca488')
    g4 = math.radians(4.0); den = math.cos(2 * g4)
    w_pap = (267 * math.cos(g4) - 642 * math.sin(g4)) / den
    h_pap = (642 * math.cos(g4) - 267 * math.sin(g4)) / den
    pw, ph = int(round(w_pap * KP)), int(round(h_pap * KP))
    pap = pecas.papel(pw, ph, cor_papel, grao=6, semente=14)          # perfil V03: já sai com o pontilhado fixo
    rng = np.random.default_rng(15)       # fibra: variação lenta de ±3 níveis (papel texturizado, não liso)
    lento = cv2.GaussianBlur(rng.normal(0, 1, (ph, pw)).astype(np.float32), (0, 0), 9)
    lento = lento / (np.abs(lento).max() + 1e-6) * 3
    pap = np.clip(pap.astype(np.float32) + lento[..., None], 0, 255).astype(np.uint8)
    pap = np.dstack([pap, np.full((ph, pw), 255, np.uint8)])
    pap = pecas.com_sombra(pap, 'cartao', sombra=sombra_em('cartao', KP))
    wx, wy = base.mundo(938, 789)
    c.poe(e3.Peca(pap, x=wx, y=wy, escala=1 / KP, giro=4.0, z=4, nome='papel creme'))

    # ── logos (recorte-adesivo do perfil: contorno branco ondulado + sombra do perfil) ──
    contorno = pecas.perfis.ativo().get('contorno', {}).get('px', 15)
    def logo(nome, total_tela, centro, giro_final, giro_extra, fr, qk0, desce, z, semente):
        fig = int(round(total_tela - 2 * contorno))                     # figura sem o contorno, px de tela assentado
        im = ctx.rgba(nome, fig, fig, nome)
        r = pecas.recorte_do_perfil(im, largura=fig, semente=semente)
        tk0, tka = t(qk0), t(qk0 + len(fr) - 1)
        s = 1 / cam(tka)[0]               # escala no mundo que dá `total_tela` px no quadro assentado
        wx, wy = base.mundo(*centro)
        ex, ey = tela(wx, wy, tk0)        # ponto de pouso, na tela, em k = 0
        meia = total_tela / 2 * cam(tk0)[0] / cam(tka)[0]
        dx0, dy0 = (e3.W + meia) - ex, desce   # começa com a borda esquerda em x = 1080
        n = len(fr) - 1
        def k_de(tt): return max(0, min(n, math.floor((tt - tk0) / Q + 1e-6)))
        def pos(tt):
            k = k_de(tt); f = fr[k]; z = cam(tt)[0]
            return wx + dx0 * (1 - f) / z, wy + dy0 * (1 - f) / z
        def giro(tt):
            k = k_de(tt); return giro_final + giro_extra * (1 - fr[k]) / (1 - fr[1])
        c.poe(e3.Peca(r, x=lambda tt: pos(tt)[0], y=lambda tt: pos(tt)[1], escala=s, giro=giro, z=z,
                      de=t(qk0 + 1), nome=nome))
    logo('logo-gamma', 370, (850, 706), -4.0, 6.0, F_GAMMA, qG0, -24.0, 5, 33)     # da direita, desce 24 px no caminho
    logo('logo-canva', 336, (798, 962), 5.0, 10.0, F_CANVA, qV0, 135.0, 6, 36)     # de baixo-direita, sobe 135 px

    return {'nome': 'plano_14 · maço + papel → logos Gamma e Canva', 'f0': f0, 'f1': f1, 'cena': c}


def sombra_em(tipo, k):
    """Sombra do perfil para uma peça rasterizada k× maior que a tela (a sombra sai na medida do perfil depois de
    reduzida pela escala 1/k)."""
    sp = pecas.perfis.ativo().get('sombra_' + tipo)
    return None if not sp else dict(dy=sp['dy'] * k, sigma=sp['sigma'] * k, op=sp['op'])
