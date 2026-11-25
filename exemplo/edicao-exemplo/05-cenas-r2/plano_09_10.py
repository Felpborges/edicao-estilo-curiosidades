#!/usr/bin/env python3
"""plano_09_10 · Afastamento que revela a parede de slides (trecho 9, P13, ref V04-A45) e, sem corte, dois cartões
que caem por cima da parede (trecho 10, P09, ref V01-A38). Specs: `04-specs/trecho-09.md` e `trecho-10.md`, mais
os "Ajustes ao plano" da `LISTA-DE-IMAGENS.md` (valem por cima da spec do trecho 10):
  · cartão do PowerPoint entra em "apresentação" (i84), 42 ms antes;
  · cartão do Google Slides entra 132 ms antes de "Google" (i90);
  · sem cascata de saída: o plano acaba no corte seco para o rosto.

Custo: a parede (5 colunas × 12 linhas = 60 cartões) é UMA placa rígida para a câmera; os 60 cartões são peças
que compartilham a pirâmide de imagem dos 12 slides (12 conversões em vez de 60, ≈ 110 MB em vez de ≈ 540 MB), e
cartão fora da tela não custa nada por quadro (o motor recorta pela caixa).

2ª rodada (corte 04): acabamento do perfil V03 (mesa do perfil parada, sem a "luz de museu" por cima, grão vivo,
cartões e recortes do perfil com a sombra caída) e câmera por fases. Parede: a câmera medida na V04-A45 (reestudo
20/11: −7,6 %/s → acelera até −34 %/s → freia a −13,6 %/s); depois, onde a Ref já cortou, a linha do painel (retoma
+3 %/s em "prontos"; quase para enquanto os adesivos caem). O menu e os adesivos formam a pilha da V01-A38, que
sobe e recua devagar (−1,3 %/s, depois −2,4 %/s). O véu do trecho 10 (pedido do Felipe) fica. Auditoria:
`auditoria-r2-plano_09_10.md`.
"""
import copy, math
import numpy as np
import e3, pecas, base

Q = e3.QUADRO_MS

# ───────── a parede (px do mundo; escala 1 = quadro f428, em "todos") ─────────
CARTAO_W = 858                              # largura do cartão de referência em f428 (tabela §2)
BORDA = int(round(0.013 * CARTAO_W))        # borda de papel 1,3 % da largura do cartão = 11 px
SLIDE_W = CARTAO_W - 2 * BORDA
SLIDE_H = int(round(SLIDE_W * 9 / 16))
CARTAO_H = SLIDE_H + 2 * BORDA
PASSO_X = CARTAO_W * 1.086                  # vão entre colunas 8,6 % da largura do cartão (M)
PASSO_Y = CARTAO_H + 0.045 * CARTAO_W       # vão vertical 4,5 % da largura do cartão (M)
PONTO_FIXO = (540, 864)                     # ponto fixo do afastamento, px de tela (M: 50 %, 45 %)
COLUNAS = (-2, -1, 0, 1, 2)                 # 3 visíveis + 1 de folga de cada lado
LINHAS = range(-6, 6)                       # 12 linhas; k = 0 é o slide 3 da coluna central
DESLOC_COL = {0: 0.0, 1: 0.37, -1: -0.29, 2: -0.21, -2: 0.13}   # deslocamento vertical (fração do passo; ±2 = I)
GIRA_SLIDE = {0: 0, 1: 4, -1: 8, 2: 8, -2: 4}                     # rodízio dos 12 slides por coluna (sem vizinho igual)
N_SLIDES = 12

# câmera: largura do cartão central (px) por quadro, relativa ao quadro de "todos" (tabela da spec §2)
TABELA_W = [(-16, 904), (-8, 881), (0, 858), (4, 823), (8, 777), (12, 733), (16, 686), (20, 640), (24, 597),
            (28, 556), (32, 516), (36, 483), (40, 459), (44, 440), (48, 426), (52, 413), (56, 403), (62, 393),
            (68, 389)]
RECUO_LENTO = 0.023                         # −2,3 %/s depois do freio (V04-A38, M), até o corte
PRE_RECUO = 0.076                           # −7,6 %/s (só para estender a tabela para trás se o gatilho mudar)
# (corte 03: TABELA_W e zoom_parede eram a câmera; ficam só como registro. 2ª rodada: CAMERA_A45 abaixo.)

# câmera da parede, 2ª rodada: taxas em %/s medidas na V04-A45 (reestudo 20/11, de 4 em 4 quadros), em ms a partir
# do início do afastamento acelerado (ref f3386 = nosso "todos" + 5 ms): f3381 −7,6 · f3392 −31,5 · f3404 −33,3 ·
# f3416 −34,0 (pico) · f3428 −21,7 · f3436 −13,6 (a ref corta a −13 %/s).
CAMERA_A45 = [(0, -7.6), (250, -31.5), (750, -33.3), (1300, -34.0), (1750, -21.7), (2085, -13.6)]
Z_CORTE = 904 / CARTAO_W                    # zoom no corte de entrada (f412): o mesmo enquadramento do corte 03
# pilha da V01-A38 (reestudo 20/11, M): a pilha recua −1,3 %/s e sobe 0,41 px/q (720) com a 1ª foto; com a 2ª,
# −2,4 %/s e 1,86 px/q. Em 1080: 0,6 e 2,8 px/q.
PILHA = dict(taxa1=-1.3, sobe1=0.41 * 1.5, taxa2=-2.4, sobe2=1.86 * 1.5)

# ───────── trecho 10: os dois cartões (px de tela; presos à tela, não acompanham o recuo) ─────────
CARTAO_PPT = dict(largura=991, centro=(546, 580), giro=1.4)      # 91,8 %; (50,5 %, 30,2 %); horário
CARTAO_GS = dict(largura=822, centro=(531, 781), giro=-1.6)      # 76 %; (49,2 %, 40,7 %); anti-horário
ESTALO_QUEDA = dict(fatores=(1.12, 1.04), giros=(2.4, 0.7))      # V01: ×1,12 +2,4° · ×1,04 +0,7° · ×1,00


def _pchip(xs, ys):
    """Interpolação monotônica (Fritsch–Carlson) — a mesma família usada para montar a tabela da spec."""
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    h = np.diff(xs); d = np.diff(ys) / h
    m = np.zeros_like(ys)
    for i in range(1, len(xs) - 1):
        if d[i - 1] * d[i] > 0:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
    m[0], m[-1] = d[0], d[-1]

    def f(x):
        if x <= xs[0]: return ys[0] + m[0] * (x - xs[0])
        if x >= xs[-1]: return ys[-1] + m[-1] * (x - xs[-1])
        i = int(np.searchsorted(xs, x) - 1); i = max(0, min(i, len(h) - 1))
        u = (x - xs[i]) / h[i]
        h00, h10, h01, h11 = 2*u**3 - 3*u**2 + 1, u**3 - 2*u**2 + u, -2*u**3 + 3*u**2, u**3 - u**2
        return h00 * ys[i] + h10 * h[i] * m[i] + h01 * ys[i + 1] + h11 * h[i] * m[i + 1]
    return f


def zoom_parede(t_todos):
    """Zoom da câmera (1 = cartão de 858 px) em função do tempo: tabela da spec em ln(W), interpolada quadro a
    quadro; antes da tabela, pré-recuo −7,6 %/s; depois do último ponto (+68 q), recuo lento −2,3 %/s linear."""
    ult_q, ult_w = TABELA_W[-1]
    t_ult = t_todos + ult_q * Q
    z_ult = ult_w / CARTAO_W
    fant = [(ult_q + k, ult_w * (1 - RECUO_LENTO * k * Q / 1000)) for k in (6, 12)]   # pontos-fantasma: PCHIP chega
    pts = TABELA_W + fant                                                               # no recuo lento sem tranco
    f = _pchip([t_todos + q * Q for q, _ in pts], [math.log(w / CARTAO_W) for _, w in pts])
    t_pri, z_pri = t_todos + TABELA_W[0][0] * Q, TABELA_W[0][1] / CARTAO_W

    def z(t):
        if t >= t_ult: return z_ult * (1 - RECUO_LENTO * (t - t_ult) / 1000)
        if t < t_pri: return z_pri * (1 + PRE_RECUO * (t_pri - t) / 1000)
        return math.exp(f(t))
    return z


def pilha(t_1, t_2, ancora):
    """Movimento próprio da pilha (menu + adesivos), presa à tela: devolve (s(t), dy(t)) = escala em torno da âncora e
    subida em px. Fase 1 desde t_1 (1ª peça), fase 2 desde t_2 (2ª peça assentada). Antes de t_1: parada."""
    def s(t):
        if t <= t_1: return 1.0
        a = min(t, t_2) - t_1; b = max(0.0, t - t_2)
        return math.exp((PILHA['taxa1'] * a + PILHA['taxa2'] * b) / 100000.0)
    def dy(t):
        if t <= t_1: return 0.0
        a = min(t, t_2) - t_1; b = max(0.0, t - t_2)
        return -(PILHA['sobe1'] * a + PILHA['sobe2'] * b) / Q
    return s, dy


def na_pilha(x_tela, y_tela, escala, s, dy, ancora):
    """x, y (mundo, peça fixa) e escala de uma peça que anda com a pilha."""
    ax, ay = ancora
    esc = e3.como_funcao(escala)
    return ((lambda t: base.mundo(ax + (x_tela - ax) * s(t), 0)[0]),
            (lambda t: base.mundo(0, ay + (y_tela - ay) * s(t) + dy(t))[1]),
            (lambda t: esc(t) * s(t)))


def _slide_de(c, k):
    return (k + 2 + GIRA_SLIDE[c]) % N_SLIDES + 1          # coluna central: k = −2..1 → slides 1, 2, 3, 4


def plano(ctx):
    f0, f1 = base.CORTES['plano_09_10']
    t_todos = ctx.t(ctx.q_palavra(70, 5))                   # a aceleração começa em "todos" (i70), +5 ms
    q_ppt = ctx.q_palavra(84, -42); t_ppt = ctx.t(q_ppt)    # (gatilhos do trecho 10, iguais ao corte 03)
    q_pp = ctx.q_palavra(87, -42); q_gs = ctx.q_palavra(90, -132)
    t_pp, t_gs = ctx.t(q_pp), ctx.t(q_gs)

    # câmera por fases (G12.3). Trecho 9 = V04-A45 medida (o painel pedia −30 %/s no pico; vale a Ref, −34 %/s).
    # Depois do −13,6 %/s em que a Ref corta, a nossa cena segue (sem corte): freio na mesma desaceleração da Ref
    # (≈ 30 %/s²) até parar em "prontos" + 135 ms e retomar +3 %/s (linha do painel). Trecho 10 = painel: repouso
    # +3 %/s, quase para (+0,3 %/s) do 1º adesivo até o 2º assentar, retoma +3 %/s e corta andando.
    t_prontos = ctx.ataque(79) + 135
    chaves = [(ctx.t(f0), -7.6)] + [(t_todos + d, r) for d, r in CAMERA_A45]
    chaves += [(t_prontos, 0.0), (t_prontos + 250, 3.0)]
    chaves += e3.pausa(t_pp, t_gs + 4 * Q, antes=3.0, durante=0.3, depois=3.0, rampa_ms=250)
    zoom = base.zoom_fases(ctx.t(f0), chaves, Z_CORTE)
    cx, cy = base.ancora(zoom, *PONTO_FIXO)
    c = base.cena(e3.Camera(zoom=zoom, cx=cx, cy=cy), semente=910)

    # 12 cartões-modelo (um por slide), cada um convertido uma vez só
    modelos = {}
    for n in range(1, N_SLIDES + 1):
        nome = f'slide-{n:02d}'
        img = ctx.img(nome, 1280, 720, f'{nome}\n(16:9)')
        # perfil V03: borda de papel de 12 px pontilhada + fio + sombra caída (o RGBA cresce, o centro fica)
        modelos[n] = e3.Peca(pecas.cartao(img, CARTAO_W, CARTAO_H), z=1, nome=nome)

    # a placa: cada cartão é cópia rasa do modelo (mesma pirâmide), com posição, giro e desalinhamento próprios
    fx, fy = base.mundo(*PONTO_FIXO)                        # com zoom 1 o ponto fixo cai em (0, −96) do mundo
    y_slide3 = fy + PASSO_Y / 2                             # o vão entre o slide 2 e o 3 passa no ponto fixo
    rng = np.random.default_rng(909)
    parede = []
    for col in COLUNAS:
        for k in LINHAS:
            p = copy.copy(modelos[_slide_de(col, k)])
            x = fx + col * PASSO_X + rng.uniform(-0.01, 0.01) * CARTAO_W           # ±1 % da largura (O)
            y = y_slide3 + (k + DESLOC_COL[col]) * PASSO_Y
            g = (1 if (col + k) % 2 == 0 else -1) * rng.uniform(0.25, 0.5)        # ≤ 0,5°, sentido alternado (O)
            p.x, p.y, p.giro = e3.const(x), e3.const(y), e3.const(g)
            p.de, p.nome = ctx.t(f0), f'{p.nome} c{col:+d} k{k:+d}'
            c.poe(p); parede.append((col, k, _slide_de(col, k), x, y, g))

    # trecho 10 · cartão 1 (PowerPoint): estalo de queda, 42 ms antes de "apresentação" (i84) — ajuste adotado.
    # Cartão do perfil (sombra já incluída). Anda com a pilha da V01-A38 (recua e sobe devagar), âncora no centro dele.
    s_p, dy_p = pilha(t_ppt + 4 * Q, t_gs + 4 * Q, CARTAO_PPT['centro'])
    img = ctx.img('print-powerpoint', 1600, 1000, 'print-powerpoint\n(menu de download, 16:10)')
    esc, gir = base.estalo(t_ppt, 1.0, CARTAO_PPT['giro'], **ESTALO_QUEDA)
    x_, y_, e_ = na_pilha(*CARTAO_PPT['centro'], esc, s_p, dy_p, CARTAO_PPT['centro'])
    c.poe(e3.Peca(pecas.cartao(img, CARTAO_PPT['largura']), x=x_, y=y_, escala=e_, giro=gir, z=5, de=t_ppt,
                  fixa=True, nome='cartão PowerPoint'))

    # trecho 10 · 20/11 (principal): não há print real do deck aberto no PowerPoint nem no Google Slides (o Claude Slides
    # baixa em PDF, PNG ou .pptx; não exporta para o Google Slides). O cartão 1 passa a ser o print real do menu de
    # download, e os dois destinos falados entram como adesivos com o logo oficial, um por palavra (P16: recorte que
    # pipoca na palavra), no lugar do 2º cartão. Estalo de recorte do molde: ×1,087 · ×1,025 · ×1,00, 2 q cada.
    # "PowerPoint" (i87, −42 ms) · "Google" (i90, −132 ms, piso de 700 ms): q_pp e q_gs, definidos no alto
    # 20/11, revisão do Felipe ("na hora que aparecer a logo do PowerPoint ou Google Slides, eu gostaria que o fundo
    # tivesse escurecido, para não ficar muita informação na tela"): véu preto preso à tela entre a cena (parede + menu)
    # e os adesivos, junto do 1º logo. A referência escurece o fundo atrás de um cartão em −28 % (V05-A11, medido);
    # aqui vai a −62 %, a pedido, porque atrás há uma parede de slides e um print. Entra em 2 degraus de 2 q, como o estalo.
    VEU = 0.62
    tv = ctx.t(q_pp)
    preto = np.zeros((e3.H, e3.W, 4), np.uint8); preto[..., 3] = 255
    c.poe(e3.Peca(preto, alfa=e3.Trilha([(tv, VEU * 0.55), (tv + 2 * Q, VEU)], degrau=2 * Q, t0=tv), z=6, de=tv, fixa=True, nome='véu escuro'))
    for nome, q, (cx_, cy_), alt, giro in (('logo-powerpoint', q_pp, (330, 905), 300, -6.0), ('logo-google-slides', q_gs, (735, 930), 300, 5.0)):
        fig = pecas.recorte_do_perfil(ctx.rgba(nome, 330, 300, nome), altura=alt)     # contorno ondulado + sombra V03
        tq = ctx.t(q)
        esc = e3.Trilha([(tq, 1.087), (tq + 2 * Q, 1.025), (tq + 4 * Q, 1.0)], degrau=2 * Q, t0=tq)
        x_, y_, e_ = na_pilha(cx_, cy_, esc, s_p, dy_p, CARTAO_PPT['centro'])
        c.poe(e3.Peca(fig, x=x_, y=y_, escala=e_, giro=giro, z=7, de=tq, fixa=True, nome=nome))

    return {'nome': 'plano_09_10 · parede de slides + PowerPoint e Google Slides', 'f0': f0, 'f1': f1, 'cena': c,
            'eventos': {'corte_entrada': f0, 'acelera': ctx.q_palavra(70, 5), 'cartao_ppt': q_ppt,
                        'logo_powerpoint': q_pp, 'logo_google_slides': q_gs, 'corte_saida': f1},
            'parede': parede, 'zoom': zoom, 'pilha': (s_p, dy_p)}
