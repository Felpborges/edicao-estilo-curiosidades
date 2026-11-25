#!/usr/bin/env python3
"""plano_12_13 · trechos 12 e 13 num plano só (sem corte entre eles). 2ª rodada (corte 04): acabamento do perfil V03
e câmera por fases. Composição, gatilhos e ordem das peças iguais ao corte 03 (`../05-cenas/plano_12_13.py`).

Trecho 12 (P06 + P09, ref V04-A15 e V01-A45): corte seco para o cartão vertical da conversa; o cartão do roteiro cai por
cima em "roteiro" (i112) com estalo de 2 degraus.
Trecho 13 (P10 + P08, ref V04-A16 e V03-A22), variante B: o cartão 1 do carrossel empurra o conjunto antigo para
baixo-esquerda em "transformar" (i117) e assenta em "carrosséis"; o cartão 2 pipoca em maço em "Instagram" (i121).

Câmera por fases (taxa em %/s, `base.zoom_fases`; a câmera medida na Ref manda, ver auditoria-r2-plano_12_13.md):
  1 · q619 → queda do roteiro: zoom +7,7 → +8,7 %/s (V04-A15, leve aceleração) em torno do centro da tela, com o conteúdo
      descendo 3,45 → 4,1 px/q e 0,5 px/q para a esquerda (V04-A15: 2,3 → 2,75 px/q em 720).
  2 · queda do roteiro: freia de +8,7 para +0,9 %/s em 8 q (a deriva para nos 4 q do estalo); âncora no centro do roteiro.
  3 · roteiro assentado → empurrão: quase parada, +0,9 %/s (V01-A45: o cartão que caiu anda ≈ +0,9 %/s).
  4 · empurrão (15 q): a taxa sobe de +0,9 para +3,5 %/s; as peças do empurrão estão em posições de TELA.
  5 · cartão 1 assentado → corte: +3,5 %/s (V04-A16: +3,4 a +3,6 %/s), pivô em (900, 703) (quadro seguro); corta andando.
Sem desfoque de movimento (V04: nenhum empurrão borra).
"""
import math
import e3, pecas, perfis, base

Q = e3.QUADRO_MS
CX, CY = e3.W / 2, e3.H / 2

# empurrão (trecho 13 §2, medido em V04-A16): fração do caminho do cartão novo, k = 0…15
P_EMPURRAO = [0.0, 0.13, 0.25, 0.38, 0.48, 0.59, 0.67, 0.74, 0.81, 0.87, 0.92, 0.94, 0.96, 0.98, 0.99, 1.00]
# deslocamento acumulado em x do conjunto antigo (px de tela), k = 0…13; y = +0,27·|x|
DX_ANTIGO = [0, -15, -45, -95, -161, -229, -334, -439, -554, -691, -835, -979, -1123, -1267]


def cartao_k(img, largura, altura, K):
    """Cartão do perfil feito num raster K× maior que a tela (a câmera aproxima). Borda, fio e sombra do perfil vão ×K
    no raster para que, na escala 1/K, fiquem na tela com a medida do perfil (borda 12 px, sombra dy 12 px)."""
    P = perfis.ativo()
    if P.get('antigo'): return pecas.cartao(img, largura, altura, borda=int(round(12 * K)))
    B, S = P['borda'], P['sombra_cartao']
    P['borda'] = dict(B, px=int(round(B['px'] * K)))
    try:
        rgba = pecas.cartao_do_perfil(img, largura, altura, sombra=False)
    finally:
        P['borda'] = B
    return pecas.com_sombra(rgba, 'cartao', sombra=dict(dy=S['dy'] * K, sigma=S['sigma'] * K, op=S['op']))


def _integra(chaves, t0, t):
    """∫ de t0 até t de uma grandeza que varia em linha reta entre chaves [(t_ms, valor)] (constante fora), em valor·ms."""
    def v(x):
        if x <= chaves[0][0]: return chaves[0][1]
        if x >= chaves[-1][0]: return chaves[-1][1]
        for (ta, va), (tb, vb) in zip(chaves, chaves[1:]):
            if ta <= x <= tb: return va if tb == ta else va + (vb - va) * (x - ta) / (tb - ta)
    pts = sorted({t0, t} | {tk for tk, _ in chaves if min(t0, t) < tk < max(t0, t)})
    s = sum((b - a) * (v(a) + v(b)) / 2 for a, b in zip(pts, pts[1:]))
    return s if t >= t0 else -s


def plano(ctx):
    f0, f1 = base.CORTES['plano_12_13']
    t = ctx.t
    t0 = t(f0)

    # ── gatilhos (iguais ao corte 03), recalculados nos ataques reconferidos ──
    qR = ctx.q_palavra(112, -40)          # roteiro cai: 40 ms antes de "roteiro" (spec 12, passo 3)
    qRa = qR + 4                          # roteiro assentado
    qK1 = ctx.q_palavra(117, -42)         # 1º quadro visível do empurrão: 1 q antes de "transformar"
    qK0 = qK1 - 1                         # k = 0 (cartão 1 ainda fora, encostado na borda direita)
    qK15 = qK0 + 15                       # cartão 1 assentado
    qC2 = ctx.q_palavra(121, 0)           # cartão 2 pipoca no início de "Instagram" (spec 13, variante B)
    tR, tRa, tK0, tK15 = t(qR), t(qRa), t(qK0), t(qK15)
    gatilhos = {'corte_entrada': f0, 'roteiro_cai': qR, 'roteiro_assenta': qRa, 'empurrao_k0': qK0, 'empurrao_k1': qK1,
                'carrossel1_assenta': qK15, 'carrossel2': qC2, 'corte_saida': f1}

    # ── câmera por fases ──
    tF = tR + 8 * Q                       # fim do freio da queda do roteiro
    CHAVES = [(t0, 7.7), (tR, 8.7), (tF, 0.9), (tK0, 0.9), (tK15, 3.5)]
    zoom = base.zoom_fases(t0, CHAVES)
    # deriva do conteúdo (px de tela por quadro): V04-A15 desce 2,3 → 2,75 px/q em 720 (×1,5), 0,5 px/q para a esquerda;
    # para nos 4 q do estalo do roteiro
    DRIFT_X = [(t0, -0.5), (tR, -0.5), (tRa, 0.0)]
    DRIFT_Y = [(t0, 3.45), (tR, 4.1), (tRa, 0.0)]

    def deriva(tt):
        return _integra(DRIFT_X, t0, tt) / Q, _integra(DRIFT_Y, t0, tt) / Q

    # âncoras: até tRa o centro da tela (com a deriva); de tRa a tK15 o centro do roteiro assentado; depois o cartão 1
    def cam0(tt):
        z = zoom(tt); dx, dy = deriva(tt)
        return z, -dx / z, -dy / z

    A2 = (530.0, 632.0)                   # centro do roteiro assentado (tela)
    zA, cxA, cyA = cam0(tRa)
    m2 = (cxA + (A2[0] - CX) / zA, cyA + (A2[1] - CY) / zA)   # ponto do mundo sob o roteiro: fica parado na fase 3

    def cam2(tt):
        z = zoom(tt)
        return z, m2[0] - (A2[0] - CX) / z, m2[1] - (A2[1] - CY) / z

    z15, cx15, cy15 = cam2(tK15)
    A4 = (535.0, 703.0)                   # centro do cartão 1 assentado (tela)
    m4 = (cx15 + (A4[0] - CX) / z15, cy15 + (A4[1] - CY) / z15)

    # pivô da fase 5 à direita do cartão 1, na altura do centro dele: o maço cresce para a esquerda e o canto de cima à
    # direita do cartão 2 (+1,8°) não sai do quadro no corte (quadro seguro). Efeito colateral: o conteúdo anda ≈ 0,5 px/q
    # para a esquerda, no sentido do pan medido no V04-A16 (−6 px/q em 1080), bem mais fraco que ele.
    AP = (900.0, A4[1])
    mp = (cx15 + (AP[0] - CX) / z15, cy15 + (AP[1] - CY) / z15)

    def cam4(tt):
        z = zoom(tt)
        return z, mp[0] - (AP[0] - CX) / z, mp[1] - (AP[1] - CY) / z

    memo = {}
    def cam(tt):
        if tt not in memo:
            memo[tt] = cam0(tt) if tt < tRa else (cam2(tt) if tt < tK15 else cam4(tt))
        return memo[tt]

    camera = e3.Camera(zoom=lambda tt: cam(tt)[0], cx=lambda tt: cam(tt)[1], cy=lambda tt: cam(tt)[2])
    c = base.cena(camera, semente=1213)

    def k_de(tt, k0, kmax):
        return max(0, min(kmax, math.floor((tt - k0) / Q + 1e-6)))

    # ── peça 1 · cartão da conversa (P06): 912 × 1134 no corte, centro (535, 703), −0,7° ──
    KC = 1.5                              # raster 1,5× (a câmera leva o cartão a ≈ ×1,27 antes do empurrão)
    img = ctx.img('print-conversa-roteiro', int(888 * KC), int(1110 * KC), 'conversa\n+ pedido\n(4:5)')
    conv = cartao_k(img, 912 * KC, 1134 * KC, KC)
    # o conjunto antigo é empurrado a partir de k = 1 (deslocamento de tela convertido para o mundo)
    def empurra(tt):
        k = k_de(tt, tK0, 13)
        if k == 0: return 0.0, 0.0
        z = cam(tt)[0]
        dx = DX_ANTIGO[k]
        return dx / z, 0.27 * abs(dx) / z
    wx, wy = base.mundo(535, 703)
    c.poe(e3.Peca(conv, x=lambda tt: wx + empurra(tt)[0], y=lambda tt: wy + empurra(tt)[1], escala=1 / KC, giro=-0.7,
                  z=1, ate=t(qK0 + 13), nome='cartão da conversa'))

    # ── peça 2 · cartão do roteiro (P09): 867 × 424 assentado em qRa, centro (530, 632), +1,2° ──
    KR = 1.25
    img = ctx.img('print-roteiro', int(round(843 * KR)), int(400 * KR), 'roteiro (2,1:1)')
    rot = cartao_k(img, round(867 * KR), 424 * KR, KR)
    sR = 1 / KR / cam(tRa)[0]             # escala no mundo que dá 867 px na tela no quadro assentado
    esc_r = e3.Trilha([(tR, 1.09), (tR + 2 * Q, 1.02), (tR + 4 * Q, 1.0)], degrau=2 * Q, t0=tR)
    gir_r = e3.Trilha([(tR, -1.3), (tR + 2 * Q, 0.5), (tR + 4 * Q, 1.2)], degrau=2 * Q, t0=tR)
    c.poe(e3.Peca(rot, x=lambda tt: m2[0] + empurra(tt)[0], y=lambda tt: m2[1] + empurra(tt)[1],
                  escala=lambda tt: sR * esc_r(tt), giro=gir_r, z=2, de=tR, ate=t(qK0 + 13), nome='cartão do roteiro'))

    # ── cartões do carrossel (4:5): 912 × 1134 na tela ──
    KK = 14 / 12                          # raster 1,167× (chega a ×1,18 no estalo do cartão 2)
    S0, S1 = (1536.0, 424.0), (535.0, 703.0)   # centro do cartão 1 em k = 0 (fora, borda esquerda em x 1080) e assentado

    img = ctx.img('carrossel-1', int(888 * KK), int(1110 * KK), 'carrossel 1\n(4:5)')
    car1 = cartao_k(img, round(912 * KK), round(1134 * KK), KK)
    def pos1(tt):
        k = k_de(tt, tK0, 15)
        if k >= 15: return m4[0], m4[1], 1 / KK / z15
        p = P_EMPURRAO[k]
        sx, sy = S0[0] + (S1[0] - S0[0]) * p, S0[1] + (S1[1] - S0[1]) * p
        z, cx_, cy_ = cam(tt)
        return cx_ + (sx - CX) / z, cy_ + (sy - CY) / z, 1 / KK / z
    c.poe(e3.Peca(car1, x=lambda tt: pos1(tt)[0], y=lambda tt: pos1(tt)[1], escala=lambda tt: pos1(tt)[2], giro=-0.8,
                  z=3, de=t(qK1), nome='carrossel 1 (empurra)'))

    # cartão 2: maço por cima do 1º, +54 px →, +38 px ↓ (na escala do cartão 1 assentado), +1,8°, estalo do P08
    img = ctx.img('carrossel-2', int(888 * KK), int(1110 * KK), 'carrossel 2\n(4:5)')
    car2 = cartao_k(img, round(912 * KK), round(1134 * KK), KK)
    tC2 = t(qC2)
    esc2, gir2 = base.estalo(tC2, escala=1 / KK / z15, giro=1.8, fatores=(1.10, 1.03), giros=(3.5, 1.0))
    c.poe(e3.Peca(car2, x=m4[0] + 54 / z15, y=m4[1] + 38 / z15, escala=esc2, giro=gir2, z=4, de=tC2,
                  nome='carrossel 2 (maço)'))

    return {'nome': 'plano_12_13 · conversa + roteiro → carrossel', 'f0': f0, 'f1': f1, 'cena': c, 'gatilhos': gatilhos}
