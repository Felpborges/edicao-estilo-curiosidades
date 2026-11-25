#!/usr/bin/env python3
"""plano_04_05 · "Elas se chamam Slides, Docs e Design / e ficam dentro do chat que você já utiliza."

Um plano só (sem corte entre os trechos 4 e 5). Specs: `04-specs/trecho-04.md` e `trecho-05.md`.
Refs: V03-A21 + V03-A10 (pilha com etiquetas) e V04-A08 (print que entra deslizando + elipse à mão).

- Trecho 4: três cartões em cascata (um por nome, estalo de 4 q em degraus de 2 q), cada um com a etiqueta de papel
  2 q depois (filha do cartão: herda posição, giro, estalo e câmera). Câmera da pilha: zoom +5 %/s, âncora (540, 780),
  e descida de 240 px → 0 (lento-rápido-lento) até o cartão 3 assentar; o zoom segue por baixo do print.
- Trecho 5: o print do chat desliza da esquerda (9 q, ease-out quadrático, −1° → 0°) e cobre a pilha; depois zoom
  +4,3 %/s, âncora (648, 864). A pilha e o print têm câmeras diferentes, por isso o print e a elipse são peças
  `fixa=True` com a transformação de tela calculada aqui (a câmera da cena é a da pilha).
- Elipse amarela (pecas.MARCA_MAO) em 5 degraus de 2 q (25/45/65/85/100 %), começando na esquerda-baixo, horária.

Todos os quadros saem das palavras (ctx.q_palavra); só o corte (145, 262) é fixo (base.CORTES).
Nenhum hex escrito à mão: cores = constantes do pecas.py (já convertidas por do_guia).

2ª rodada (corte 04, perfil V03): mesmos gatilhos, peças, posições e tamanhos. Muda o acabamento (cartões e print com
a borda e a sombra do perfil, etiquetas com a sombra do perfil, elipse sem grão) e a câmera, agora por FASES em %/s
(auditoria: `auditoria-r2-plano_04_05.md`):
- pilha (V03-A21 + V03-A10): push-in +6,6 %/s depois do 1º estalo → lista quase parada (−4 → −1,4 %/s, valores da
  A21) → pico +14 %/s 135 ms depois de "Design" (sobe a partir da palavra), freio longo de 900 ms até +8 %/s (painel);
  a descida de 240 px do corte 03 continua (enquadra cada cartão quando entra).
- print (V04-A08): desliza lento-rápido-lento (painel); a câmera desacelera sem parar (+15 → +12 → +4,5 → +2 %/s),
  como a Ref mede (o painel pedia parar durante o traço: vale a Ref). Âncora no centro da elipse para ela caber até o fim.
"""
import math
import e3, pecas, base

Q = e3.QUADRO_MS

# Alvo da elipse no print: posição de TELA (px 1080x1920) no quadro em que o print assenta (zoom 1).
# Conteúdo variável: quando o print real chegar, recortá-lo para o menu das ferramentas cair aqui
# (= 36 % da largura e 52 % da altura do miolo da imagem, ver auditoria) ou mudar este ponto dentro das
# restrições da spec (centro y 770–1100, x 25–75 %, base da elipse ≤ y 1200 quando fecha).
ALVO_CHAT = (530, 860)        # 20/11: centro da caixa de mensagem no print real (medido na captura)


def _pos_filho(cx, cy, esc, gir, dx, dy):
    """Posição (mundo do e3) de um ponto preso ao cartão: offset (dx, dy) no referencial do cartão sem giro."""
    def x(t):
        g = math.radians(gir(t)); k = esc(t)
        return cx + k * (dx * math.cos(g) - dy * math.sin(g))
    def y(t):
        g = math.radians(gir(t)); k = esc(t)
        return cy + k * (dx * math.sin(g) + dy * math.cos(g))
    return x, y


def plano(ctx):
    f0, f1 = base.CORTES['plano_04_05']

    # ───────── quadros pelas palavras (recalculados com os ataques reconferidos) ─────────
    q_c1 = f0                                   # cartão 1 entra no corte (62 ms antes de "Elas", i21)
    q_e1 = ctx.q_palavra(24, 43)                # etiqueta SLIDES: +43 ms de "Slides" (molde P05)
    q_c2 = ctx.q_palavra(25, 0)                 # cartão DOCS: na palavra (molde P08 0 ms)
    q_e2 = q_c2 + 2                             # etiqueta 2 q depois do cartão (spec §1, regra 4–7)
    q_c3 = ctx.q_palavra(27, 0)                 # cartão DESIGN
    q_e3 = q_c3 + 2
    q_assenta3 = q_c3 + 4                       # fim da descida da câmera
    q_elipse = ctx.q_palavra(32, 41)            # 1º pixel do traço: +41 ms de "chat" (P19, metade central −98…+44)
    q_print = q_elipse - 10                     # deslize de 9 q + 1 q parado antes do traço (estrutura da spec)
    q_assenta_p = q_print + 9

    # trava do piso: etiqueta DESIGN inteira até ≥ 700 ms depois do fim de "Design" (o print a alcança no 2º quadro)
    assert (q_print + 2) * Q - ctx.fim(27) >= 700, 'etiqueta DESIGN abaixo do piso'
    assert f0 <= q_print and q_elipse + 8 < f1

    # ───────── câmera da pilha, por fases (V03-A21 + V03-A10; painel do trecho 4) ─────────
    t_c = ctx.t(q_c1)
    t_design = ctx.ataque(27)
    CAM_PILHA = ([(t_c, 6.6), (ctx.t(q_c1 + 12), 6.6),          # A21: push-in +6,6 %/s logo depois do 1º estalo
                  (ctx.t(q_e1 + 1), -4.0),                        # vira na etiqueta SLIDES: começa a lista
                  (ctx.t(q_c2), -1.4)]                            # A21: na lista −5,6 → −1,4 %/s ("quase para")
                 + e3.fases_pico(ctx.t(q_c2), t_design, repouso=-1.4, pico=14.0, atraso_ms=135.0, subida_ms=135.0,
                                 freio_ms=900.0, depois=8.0)[1:])  # pico depois de "Design", freio longo até +8 (painel)
    s = base.zoom_fases(t_c, CAM_PILHA)
    d = e3.Trilha([(t_c, 240.0), (ctx.t(q_assenta3), 0.0, e3.viagem)])          # descida 240 → 0 (corte 03)
    # tela = A + s·(m − A) + (0, d), A = (540, 780)  →  centro de câmera do e3:
    cam = e3.Camera(zoom=s, cx=0, cy=lambda t: -180 * (1 - 1 / s(t)) - d(t) / s(t))
    c = base.cena(cam, semente=405)

    # ───────── trecho 4: cartões e etiquetas ─────────
    cartoes = [  # nome, imagem, rótulo, externo (L, A), miolo, centro no mundo, giro, etiqueta, giro da etiqueta, quadros
        ('SLIDES', 'card-slides', 'card-slides\nprint do deck (16:9)', (820, 472), (796, 448), (480, 470), -1.8, -2.0, q_c1, q_e1),
        ('DOCS', 'card-docs', 'card-docs\nprint do documento (3:2)', (780, 500), (756, 476), (610, 790), 2.0, 1.2, q_c2, q_e2),
        ('DESIGN', 'card-design', 'card-design\nprint do design (16:9)', (800, 460), (776, 436), (540, 1100), -1.5, -2.0, q_c3, q_e3),
    ]
    for n, (rot, nome, rotulo, (L, A), (mw, mh), (wx, wy), giro, giro_et, qc, qe) in enumerate(cartoes):
        img = ctx.img(nome, mw, mh, rotulo)
        rgba = pecas.cartao(img, L, A, borda=12)       # perfil V03: borda de papel + sombra caída (cartão sobre cartão)
        tc = ctx.t(qc)
        esc, gir = base.estalo(tc, 1.0, giro)                                     # ×1,12 +3,5° · ×1,04 +1° · assentado
        mx, my = base.mundo(wx, wy)
        c.poe(e3.Peca(rgba, x=mx, y=my, escala=esc, giro=gir, z=1 + 2 * n, de=tc, nome=f'cartão {rot}'))

        et = pecas.com_sombra(pecas.etiqueta(rot), 'etiqueta')   # tira de papel: ferve (grão vivo) e tem sombra
        te = ctx.t(qe)
        esc_e, gir_e = base.estalo(te, 1.0, giro_et, fatores=(1.10, 1.03), giros=(2.4, 0.0))   # estalo leve P05
        ex, ey = _pos_filho(mx, my, esc, gir, 63.0, -A / 2.0)                     # +63 px do centro, na borda de cima
        c.poe(e3.Peca(et, x=ex, y=ey,
                      escala=(lambda t, a=esc, b=esc_e: a(t) * b(t)),
                      giro=(lambda t, a=gir, g0=giro, b=gir_e: b(t) + (a(t) - g0)),
                      z=2 + 2 * n, de=te, nome=f'etiqueta {rot}'))

    # ───────── trecho 5: print do chat (transformação de tela própria) ─────────
    PW, PH, PB = 1180, 1824, 13
    img = ctx.img('print-chat', 1300, 2010, 'print-chat\ntela do chat (0,647:1)\nalvo: menu das ferramentas')
    prt = pecas.cartao(img, PW, PH, borda=PB)                                     # perfil V03: borda 12 px + sombra
    tp, ta = ctx.t(q_print), ctx.t(q_assenta_p)
    # âncora do zoom do print = centro da elipse: a elipse (1000 px de 1080 ao fechar) cresce igual dos dois lados
    AZ = (float(ALVO_CHAT[0]), 864.0)
    # câmera do print (V04-A08): +15 %/s no fim do deslize → +12 ao assentar → desacelera durante o traço, sem parar →
    # +4,5 ao fechar → +2 no corte. O zoom vale 1 no quadro em que o print assenta (antes, um pouco menor).
    CAM_PRINT = [(tp, 15.0), (ta, 12.0), (ctx.t(q_elipse + 8), 4.5), (ctx.t(f1 - 1), 2.0)]
    sp = base.zoom_fases(ta, CAM_PRINT)

    def k_desl(t): return max(0, min(9, int(math.floor((t - tp) / Q + 1e-6))))

    def tela_print(t):
        """Centro do print em px de tela, giro e escala no tempo t (deslize em 9 q, lento-rápido-lento, + câmera)."""
        u = e3.lento_rapido_lento(k_desl(t) / 9.0)
        cx_d = (240 + 890 * u) - PW / 2                                           # borda direita 240 → 1130
        z = sp(t)
        return AZ[0] + z * (cx_d - AZ[0]), AZ[1] + z * (950 - AZ[1]), -1.0 + u, z

    c.poe(e3.Peca(prt, x=lambda t: tela_print(t)[0] - e3.W / 2, y=lambda t: tela_print(t)[1] - e3.H / 2,
                  giro=lambda t: tela_print(t)[2], escala=lambda t: tela_print(t)[3],
                  z=20, de=tp, fixa=True, nome='print do chat'))

    # ───────── elipse à mão (presa ao print; já assentado quando começa) ─────────
    # caixa na hora em que fecha: 347 × 335 px; eixo maior 35–40° subindo da esquerda-baixo para a direita-cima.
    # Eixos equivalentes a essa caixa com 37,5°: 364 × 317 px. Desenhada com o eixo maior na vertical e girada
    # −127,5° para o traço começar na ponta de baixo-esquerda (≈ 8 h) e correr no sentido horário.
    t_fecha = ctx.t(q_elipse + 8)
    k0 = sp(t_fecha)
    # 20/11 (principal): o alvo real é a caixa de mensagem inteira (1062 × 306 px na tela), então a elipse fica larga
    # (1000 × 380 px ao fechar; proporção 2,6:1, dentro da faixa do P19 para linha de texto: até 4,5:1), quase sem giro.
    larg, alt = 1000.0 / k0, 380.0 / k0
    passos = [0.25, 0.45, 0.65, 0.85, 1.0]
    mk = lambda fr: pecas.elipse_mao(larg, alt, espessura=12.0 / k0, fracao=fr, inclinacao=-3.0, semente=5, sobra=0.05)
    te0 = ctx.t(q_elipse)
    var = [(te0 + 2 * i * Q, mk(fr)) for i, fr in enumerate(passos) if i > 0]

    def tela_alvo(t):
        z = sp(t)
        return AZ[0] + z * (ALVO_CHAT[0] - AZ[0]), AZ[1] + z * (ALVO_CHAT[1] - AZ[1]), z

    c.poe(e3.Peca(mk(passos[0]), x=lambda t: tela_alvo(t)[0] - e3.W / 2, y=lambda t: tela_alvo(t)[1] - e3.H / 2,
                  escala=lambda t: tela_alvo(t)[2], z=21, de=te0, fixa=True, variantes=var, sem_grao=True,
                  nome='elipse do chat'))

    return {'nome': 'plano_04_05 · pilha Slides/Docs/Design + print do chat com elipse', 'f0': f0, 'f1': f1, 'cena': c,
            'quadros': dict(c1=q_c1, e1=q_e1, c2=q_c2, e2=q_e2, c3=q_c3, e3=q_e3, print=q_print, assenta_print=q_assenta_p,
                            elipse=q_elipse, elipse_fecha=q_elipse + 8)}
