#!/usr/bin/env python3
"""perfis.py · perfis de ACABAMENTO do Estilo 03 (guia, seção G12.2; reestudo de 2026-11-20).

Cada reel de referência é coerente por dentro e diferente dos outros: luz da mesa, grão, sombra, borda, cadência e
tarja da legenda vêm do MESMO vídeo. Uma edição escolhe UM perfil e segue ele inteiro. Nunca a média, nunca a
vinheta de um com o grão de outro.

- `V03` é o padrão (decisão do autor do método, 2026-11-20): é o que vem marcado no plano de edição; o usuário troca por vídeo.
- `V01` e `V04` são alternativas inteiras.
- `corte03` é o acabamento antigo do motor (o do corte 03 do reel de teste), guardado para reproduzir aquele corte.

Os valores das referências foram medidos em 720x1280; o motor trabalha em 1080x1920, então todo tamanho é ×1,5.
Todo hex vem do treino pelo caminho JPG e passa por `pecas.do_guia` antes de virar pixel.
Só dados e contas simples: roda igual em Windows, macOS e Linux.
"""
import os, json

E = 1.5        # 720 → 1080

PERFIS = {
    # ───────── V03 · mundo de papel, luz central, grão vivo, sombra caída (PADRÃO) ─────────
    'V03': dict(
        nome='V03 · mundo de papel',
        resumo='Luz central na mesa, papel que ferve (grão vivo nos claros), sombra caída para baixo, 24 imagens/s com '
               'estalos em degraus de 2 quadros.',
        pontos=['Mesa com luz central (mais clara no terço de cima), parada na tela.',
                'Papel que "ferve": grão sorteado a cada quadro, só nas partes claras das peças.',
                'Sombra caída para baixo (longa embaixo, média dos lados), que some sobre a mesa escura.',
                'Cartão com borda de papel de 8 px e estalo de entrada; recorte com contorno branco ondulado.',
                'Legenda em tarja preta a 73,5 %, 46 px de altura.'],
        refs=['V03-A10', 'V03-A07'],
        # mesa: medida em V03 f3820 (mesa quase vazia): pico de luma 48 em y ≈ 36 % da altura; 45 a ±160 px e 38 a ±320 px
        # na horizontal; topo 23, base 16. Parada na tela (só as peças andam).
        mesa=dict(centro='#32312c', topo='#181713', base='#10110c', cx=540, cy=690, rx=1200, ry_cima=720, ry_baixo=975),
        luz_por_cima=None,                 # nenhuma vinheta sobre as peças
        # grão vivo: camada sorteada a cada quadro, proporcional à luma, só sobre as peças (nunca na mesa nem no rosto).
        # Alvo medido na referência (720 px, depois da compressão): desvio do grão vivo ≈ 0,045 × luma
        # (disco luma 207 → ≈ 8,5; borda 161 → ≈ 7; tira 217 → ≈ 11), ac1 ≈ 0,45–0,5.
        grao_vivo=dict(k=0.045, ganho=1.0, desfoque=0.9, passo_q=1),
        papel_fixo=8.0,                    # pontilhado fixo do papel (disco 7,7; tira 7,6; borda 5,5), em níveis a 720 px
        ganho_papel=1.0,
        borda=dict(px=round(8 * E), cor='#d2ccc0', fio_fora=0.45, fio_dentro=0.55),   # 8 px off-white + fio escuro de 1 px
        # sombra preta multiplicada, caída para baixo. Cartão: embaixo −40 a −77 % em 15–28 px; lados −18 a −55 % em 8–20 px;
        # em cima de nada a −20 % em 1–11 px. Como deslocamento + desfoque: (dy, sigma, opacidade) em px de 1080.
        sombra_cartao=dict(dy=12, sigma=8, op=0.56),
        sombra_recorte=dict(dy=8, sigma=11, op=0.43),     # recorte sobre disco: embaixo −33 % em 18–25 px; lados −17 a −30 %
        sombra_disco=dict(dy=6, sigma=8, op=0.40),        # some sobre a mesa escura; aparece onde a mesa está iluminada
        sombra_etiqueta=dict(dy=10, sigma=9, op=0.45),    # −33 a −41 % em 17 px
        contorno=dict(px=round(11 * E), var=round(3 * E), cor='#e9e6df'),   # 7–14 px, ondulado, branco de papel
        disco=dict(cor='#ded8cb'),
        etiqueta=dict(cor='#a8a79c'),
        papel=dict(cor='#dcd5c3'),
        cadencia_q=1, degrau_estalo_q=2, estalo=True,
        desfoque_mov='só em chicotes e em saídas que deixam a mesa',
        # tarja: preta pura a 73,5 %, 46 px (y 847–892), raio ≈ 5 px, folga 4–5 px dos lados, 11 px em cima; maiúscula ≈ 23 px
        # (topo y 858, linha de base y 881); cor do miolo #ede350.
        tarja=dict(y0=round(847 * E), y1=round(847 * E) + round(46 * E), base_y=round(881.3 * E), raio=round(5 * E), folga=round(4.5 * E),
                   op=0.735, maiuscula=round(23 * E), cor='#ede350'),
    ),
    # ───────── V01 · papel que ferve a 12 imagens por segundo ─────────
    'V01': dict(
        nome='V01 · stop-motion de papel',
        resumo='Poça de luz fixa, papel que ferve, sombra caída para baixo e TUDO na cena a 12 imagens/s (rosto e legenda a 24).',
        pontos=['Cara de stop-motion: tudo na cena anda a 12 imagens por segundo (o rosto e a legenda a 24).',
                'Papel que "ferve" no mesmo passo, nos claros de fotos, documentos e discos.',
                'Sombra caída para baixo; discos e lupas com fio escuro de 1 a 2 px.',
                'Recorte com contorno de tesoura de 8 a 10 px; diagramas chapados combinam com este perfil.',
                'Legenda em tarja preta a 74 %, 46 px de altura.'],
        refs=['V01-A12', 'V01-A28'],
        mesa=dict(centro='#242020', topo='#151112', base='#100e0f', cx=540, cy=720, rx=1100, ry_cima=700, ry_baixo=900),
        luz_por_cima=None,
        grao_vivo=dict(k=0.040, ganho=1.0, desfoque=0.9, passo_q=2),          # o grão também troca a 12 por segundo
        papel_fixo=7.0, ganho_papel=1.0,
        borda=dict(px=round(7.5 * E), cor='#e2ddd3', fio_fora=0.40, fio_dentro=0.0),
        sombra_cartao=dict(dy=11, sigma=7, op=0.60),      # embaixo −45 a −61 % em 14–23 px; lados −20 a −44 % em 7–17 px; em cima 1 px
        sombra_recorte=dict(dy=7, sigma=9, op=0.40),
        sombra_disco=dict(dy=10, sigma=9, op=0.50),       # −47/−49 % embaixo, nada em cima, com fio escuro de 1–2 px
        sombra_etiqueta=dict(dy=8, sigma=7, op=0.45),
        contorno=dict(px=round(9 * E), var=round(1 * E), cor='#ebe6dd'),     # 8–10 px, de tesoura
        disco=dict(cor='#cac3b1'), etiqueta=dict(cor='#ede8dd'), papel=dict(cor='#d8cdbb'),
        cadencia_q=2, degrau_estalo_q=2, estalo=True,
        desfoque_mov='whoosh de 2 imagens e chicote',
        tarja=dict(y0=round(847 * E), y1=round(847 * E) + round(46 * E), base_y=round(882 * E), raio=round(4 * E), folga=round(4.5 * E),
                   op=0.74, maiuscula=round(24.5 * E), cor='#eade53'),
    ),
    # ───────── V04 · luz da cena por cima de tudo, nenhuma sombra ─────────
    'V04': dict(
        nome='V04 · luz de cena, sem sombra',
        resumo='Mesa lisa, uma poça de luz por cena que escurece também as peças, nenhuma sombra, nenhum desfoque de '
               'movimento, 24 imagens/s com pops em degraus de 2 quadros.',
        pontos=['Mesa lisa e escura; uma poça de luz por cena, por cima da mesa e das peças (as pontas dos cartões escurecem).',
                'Nenhuma sombra em cartões, recortes e etiquetas.',
                'Nenhum desfoque de movimento, mesmo nas entradas rápidas.',
                'Cartão de borda creme de 10 px, sem estalo; recorte limpo, sem contorno.',
                'Legenda em tarja preta a 59 %, 48 px de altura (mais transparente).'],
        refs=['V04-A15', 'V04-A02'],
        mesa=dict(centro='#12100b', topo='#0a0906', base='#060503', cx=540, cy=800, rx=1100, ry_cima=900, ry_baixo=900),
        # luz da cena: fator multiplicativo preso à tela, por cima da mesa E das peças; centro perto do meio; a força muda a
        # cada cena (a 100 px da borda sobra de 25 a 88 % do centro). `sobra` = quanto sobra na borda (padrão do meio da faixa).
        luz_por_cima=dict(cx=0.50, cy=0.42, sobra=0.55, inicio=0.20),
        grao_vivo=None, papel_fixo=3.0, ganho_papel=1.0,
        borda=dict(px=round(10 * E), cor='#e3d6c2', fio_fora=0.0, fio_dentro=0.0),
        sombra_cartao=None, sombra_recorte=None, sombra_disco=None, sombra_etiqueta=None,
        contorno=None,
        disco=dict(cor='#d9d3c7'), etiqueta=dict(cor='#ddc5b1'), papel=dict(cor='#fceac6'),
        cadencia_q=1, degrau_estalo_q=2, estalo=False,
        desfoque_mov='nenhum (medido até 107 px por quadro)',
        tarja=dict(y0=round(844 * E), y1=round(844 * E) + round(48 * E), base_y=round(881 * E), raio=round(7.5 * E), folga=round(4 * E),
                   op=0.59, maiuscula=round(26.5 * E), cor='#eee818'),
    ),
    # ───────── acabamento antigo do motor (corte 03 do reel de teste) ─────────
    'corte03': dict(
        nome='acabamento antigo (corte 03)', resumo='O que o motor fazia antes do reestudo. Só para reproduzir o corte 03.',
        antigo=True,
    ),
}
PADRAO = 'V03'
ORDEM = ['V03', 'V01', 'V04']          # como aparecem no plano de edição (o padrão primeiro)

_ativo = 'corte03'


def usa(nome):
    """Escolhe o perfil da edição (vale para pecas, e3.Cena e legenda criados depois da chamada)."""
    global _ativo
    if nome not in PERFIS: raise SystemExit(f'perfil desconhecido: {nome} (existem: {", ".join(PERFIS)})')
    _ativo = nome
    return PERFIS[nome]


def ativo(): return PERFIS[_ativo]
def nome_ativo(): return _ativo
def antigo(): return bool(PERFIS[_ativo].get('antigo'))


def da_edicao(edicao):
    """Perfil escolhido no plano de edição: `<edição>/03-plano/perfil.json` = {"perfil": "V03"}.
    Sem o arquivo, vale o acabamento antigo (edição feita antes do reestudo)."""
    p = os.path.join(edicao, '03-plano', 'perfil.json')
    if os.path.exists(p):
        return json.load(open(p, encoding='utf-8')).get('perfil', PADRAO)
    return 'corte03'


# ───────── texto que entra animado (guia G12.5; medido no miolo da letra, com fundo local) ─────────
# opacidade por quadro a partir do 1º quadro visível, e desfoque (sigma em px de 1080) que só limpa no 5º ou 6º quadro
TEXTO_GRANDE_ENTRA = [0.04, 0.35, 0.77, 0.98, 1.0]
TEXTO_GRANDE_DESFOQUE = [6.0, 4.5, 3.0, 1.5, 0.7, 0.0]
TEXTO_GRANDE_SAI = [0.91, 0.64, 0.35, 0.10, 0.0]             # bloco inteiro, sem desfoque; depois corte seco
CARACTERE_ENTRA = [0.12, 0.31, 0.50, 0.67, 0.84, 1.0]        # rótulo digitado: 5 a 6 quadros por caractere
CARACTERES_POR_QUADRO = 1.25                                  # cascata de 1 a 1,5 caractere novo por quadro
