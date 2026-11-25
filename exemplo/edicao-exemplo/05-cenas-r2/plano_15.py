#!/usr/bin/env python3
"""plano_15 · fecho · "você tem tudo em uma única conversa." · a interface do Claude em cartão com câmera viva (P06).

Versão 2 (20/11/2026), pedida pelo Felipe na revisão do corte 01: "no final, eu acho que ficaria legal mostrar de novo
a interface do Claude para falar que você tem tudo numa mesma conversa". A versão 1 (callback dos discos do gancho com
o cartão do chat subindo) está guardada em `_plano_15_callback_v1.py.txt`.

Forma: a mesma do trecho 12 (Ref V04-A15, P06: cartão que entra já assentado no corte seco, zoom linear de +8 %/s e
conteúdo descendo 4,8 px por quadro; medidas em `04-specs/trecho-12.md`). Aqui o cartão é quadrado (o P06 da referência
tem cartão quadrado no V01-A26, 72 % da largura; aqui 96 %, dentro da faixa do molde, para a interface ficar legível) e o giro vai para o
lado contrário do cartão do trecho 12 (o molde alterna o sentido).
Conteúdo: captura real da conversa "Apresentação comercial Grão Vizinho", com o pedido do carrossel à esquerda e o
carrossel aberto no Claude Design à direita (`05-imagens/tratadas/print-interface.png`).

2ª rodada (corte 04), perfil V03: cartão do perfil (borda de papel pontilhada, fios escuros, sombra caída do perfil já
incluída), mesa do perfil, grão vivo (semente 15). Câmera por taxa (`base.zoom_fases`), medida na V04-A15 (reestudo
20/11): +7,7 %/s em f1232–f1244 e +8,7 %/s em f1262–f1274 (centros 9 q e 39 q depois do corte), isto é, aproximação
contínua com leve aceleração, sem pico; corta andando. O `zoom_linear` antigo era linear no zoom (a taxa em %/s caía
ao longo da cena). O cartão continua descendo 4,8 px/q (medido em V04-A15, `04-specs/trecho-12.md`).
Auditoria: `auditoria-r2-plano_15.md`.
"""
import e3, pecas, base

Q = e3.QUADRO_MS
LADO = 1040                     # 96 % da largura (faixa do molde: 64 a 99 %), para a interface ficar legível no celular
CENTRO = (540, 700)             # no corte; o cartão desce 4,8 px/q (V04-A15) e a base passa por baixo da legenda
GIRO = 0.7                      # horário (o cartão do trecho 12 está a −0,7°)
TAXAS = ((9, 7.7), (39, 8.7))  # (quadros depois do corte, %/s) · V04-A15 medido: +7,7 → +8,7 %/s, sem pico
DESCE_Q = 4.8                   # px por quadro
# âncora do zoom (ponto que fica parado na tela): 40 px à esquerda do centro do cartão. Com a taxa da Ref o zoom chega a
# ×1,153 no último quadro (×1,140 no corte 03) e a âncora no centro cortaria mais 7 px do começo das linhas da conversa,
# à esquerda (a parte que a fala cita); aqui a esquerda corta igual ao corte 03 e a direita (a 3ª miniatura do
# carrossel, já cortada no corte 03) corta 13 px a mais. Quadro seguro conferido em q887.
ANCORA = (500, 700)


def plano(ctx):
    f0, f1 = base.CORTES['plano_15']
    t0 = ctx.t(f0)
    zoom = base.zoom_fases(t0, [(t0 + q * Q, taxa) for q, taxa in TAXAS])
    cx, cy = base.ancora(zoom, *ANCORA)
    c = base.cena(e3.Camera(zoom=zoom, cx=cx, cy=cy), semente=15)
    img = ctx.img('print-interface', 1016, 1016, 'print-interface\n(conversa + Claude Design)')
    x, y = base.mundo(*CENTRO)
    # perfil V03: pecas.cartao devolve o cartão do perfil, com a sombra dele (o RGBA cresce igual dos 4 lados)
    c.poe(e3.Peca(pecas.cartao(img, LADO, LADO), x=x, y=lambda t: y + DESCE_Q * (t - t0) / Q, giro=GIRO, z=1, de=t0,
                  nome='cartão da interface'))
    return {'nome': 'plano_15 · fecho: a interface do Claude (conversa + Claude Design)', 'f0': f0, 'f1': f1, 'cena': c,
            'gatilhos': {'corte_entrada': f0}}
