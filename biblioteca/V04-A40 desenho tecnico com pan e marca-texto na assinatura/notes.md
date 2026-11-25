# V04-A40 · desenho técnico em papel (tela cheia) + pan lateral ao longo dele + marca-texto amarelo na assinatura do autor
- Categoria: P20 · Documento com marca-texto (provisória do analista: (provisória) documento com pan e marca-texto (nome do autor))
- Fonte: V04 quadros f3064–f3149 (127,83–131,38 s; 86 quadros ≈ 3587 ms) · 23,976 fps
- Fala: "So in 1917, a British painter named Norman Wilkinson"
- Tipo de fala: data + pessoa (ano e nome de quem fez, ilustrados pelo documento de autoria dele)
- Gatilho: corte seco em f3064 (127794 ms), 36 ms antes da palavra nº 433 "So" (127830 ms). Conferido: dif 108,8 em f3064 (o maior pico do vídeo) e pausa f3062,0–f3064,9.
- Quadro-chave: f3145
- Camadas ativas: legenda | cena de tela cheia | grafismo (marca-texto) | som (voz)
- Leitura dos strips: strip.jpg = quadros f3062 a f3070, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; strip-saida.jpg = quadros f3116 a f3140, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha (marca-texto); strip-geral.jpg = quadros f3062 a f3151, de 2 em 2, 8 colunas, da esquerda para a direita, linha a linha. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-papel-tinta.jpg = quadro f3100, região x40 y500 220x160 px, ampliada 2× sem suavizar (pico do pan: papel creme com pintinhas, tinta rosa e preta; leve arrasto horizontal nas letras pequenas); detalhe-marca-texto-assinatura.jpg = quadro f3145, região x190 y800 240x80 px, ampliada 3× sem suavizar (marca-texto sobre a assinatura, encostado na tarja da legenda).

## LEITURA DE EDITOR
- Por que esta cena aqui: a frase dá ano, nacionalidade, profissão e nome; o documento original assinado pela pessoa prova quem ela é, e o marca-texto acha a assinatura na hora em que o nome é dito.
- Por que este design: o desenho técnico em tela cheia (sem cartão), percorrido por um pan, e o marca-texto na assinatura, logo acima da legenda: nome dito, nome escrito e nome marcado no mesmo ponto da tela.
- Por que estas cores: papel creme claro (a cena mais clara do trecho, luma 210 no centro), traços preto, rosa e verde do próprio documento; o amarelo do marca-texto repete o da legenda.
- Por que estes efeitos: vinheta da cena forte sobre papel claro (borda a 15 %) dá luz de mesa; nenhum arrasto no pico do pan (corrigido na conferência: era "leve arrasto no pico do pan") (alinhado ao reestudo).
- Por que este movimento: aproximação lenta, depois um pan rápido para a direita (pico ≈ 68 px/q) com leve recuo no meio, freando até o marca-texto correr linear sobre a assinatura.
- Sensação do movimento: de alguém percorrendo a prancha com os olhos até achar a assinatura; produz isso o pan acelera-freia e o marca-texto linear no fim.

## FORMA (fixa: reproduzir igual)
- Design:
  - Documento original de autoria da pessoa citada: desenho técnico colorido (preto, rosa, verde) em papel creme envelhecido, com anotações manuscritas; em f3070: x14 y89 706x799 = larg 98,1 %, alt 62,4 %, centro (51,0 %, 38,2 %), −0,9° (medido). Fundo escuro com vinheta (cantos #040303–#0b0a06) (medido).
  - Marca-texto: faixa amarela #eec236 (f3145, mediana dos amarelos em x200 y790 300x60), altura ≈ 25 px (2,0 %), sobre a assinatura manuscrita no canto inferior do desenho, logo acima da legenda; em f3145: x210 y826 179x25 = x 29,2 %, y 64,5 %, larg 24,9 % (medido).
- Movimento:
  - Entrada: corte seco (medido).
  - A câmera nunca para: desde f3065 há aproximação contínua (≈ +6 %/s: ×1,022 de f3066 a f3074, ×1,046 de f3125 a f3145) com deriva lenta para a esquerda (≈2 px/q) (remedido, registro de pontos). O pan lateral para a direita acelera a partir de f3076, fica em cruzeiro ≈f3086–f3108 e freia até ≈f3122 (≈47 quadros ≈ 1,96 s) (remedido, perfil da região x0 y100 720x700: 6,9 (f3075) → 7,8 (f3076) → 17,7 (f3087) → 17,0 (f3108) → 9,5 (f3120) → 5,8 (f3123)). Valores da nota original, em outra região: dif 8,3 (f3082) → 9,8 (f3085) → 10,2 (f3087) → 10,9 (f3092) → 9,5 (f3095) → 8,9 (f3100) → 10,0 (f3104) → 10,9 (f3108) → 8,8 (f3110) → 8,3 (f3112) (medido). Ao fim do pan o desenho ocupa larg 100 %, alt 52,0 %, centro (50,0 %, 42,9 %) (f3115) (medido).
  - Marca-texto: cresce da esquerda para a direita sobre a assinatura de f3120 a f3130 (11 quadros ≈ 460 ms), linear: largura 12 px (f3120) → 41 (f3122) → 71 (f3124) → 117 (f3126) → 147 (f3128) → 174 px (f3130) → estável (remedido por `caixa` quadro a quadro; a nota dizia ≈17 q até ≈f3136; contagem antiga: a contagem de pixels amarelos na faixa da legenda sobe de 2387 em f3120 até ≈4300 em f3135, medido por script).
  - Saída: corte seco f3149→f3150 (dif 96,8) para o A-roll (medido).
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| pan lateral para a direita | f3076 (remedido) | ≈47 quadros (1960 ms) até ≈f3122 | movimento de câmera | acelera 10 q, cruzeiro, freia ≈14 q | nº 435, o ano (128100 ms) | f3076 = 128295 ms → +195 ms (durante a palavra longa) |
| marca-texto na assinatura | f3120 | 11 quadros (460 ms) (remedido) | wipe da esquerda para a direita | linear | nº 440, o prenome da pessoa (130160 ms) | f3120 = 130130 ms → −30 ms |

- Ritmo: antes do pan f3064–f3075 ≈ 0,5 s só com aproximação lenta e deriva (não fica parado); assinatura marcada f3131–f3149 ≈ 0,79 s, com a câmera ainda se aproximando (remedido).
- Som: nenhum efeito destacável (áudio mono) (observado no envelope).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Papel do documento: creme claro (#e2d2a6 no centro sob a luz, #fae0b2 no mais claro), com pintinhas e manchas de envelhecimento; na área de traços, grão 20,5 níveis, manchas 34,7, ac1 +0,47, direção horizontal +0,78 × vertical +0,16 (as linhas do desenho), grão cinza (f3100, x60 y600 120x60; o "viva" do --q2 é o pan de 53 px entre quadros).
  - Tinta: traço preto chapado (casco), rosa e verde de lápis/aquarela com bordas levemente irregulares, letreiros manuscritos e carimbados (detalhe-papel-tinta.jpg).
  - Marca-texto: amarelo #eec236 em modo multiplicar (a assinatura em tinta escura aparece por cima), alt ≈ 25 px, bordas de cima e de baixo levemente irregulares (detalhe-marca-texto-assinatura.jpg).
  - Fundo: liso (tela fixa) acima e abaixo do papel, luma 23–31 perto da borda (f3070). Correlação f3100×f3101 +0,84 com o pan a −67 px/q (sem grão real, 0,36 níveis): construir parado (medido).
- Efeitos (reestudo 20/11):
  - Vinheta da cena (f3100): luma 100/79/57/25/15 %, nitidez 100/64/52/39/19 % (alinhado ao reestudo).
  - Luz da cena (correção 20/11, f3100, medido): centro da poça em (49 %, 40 %) (ajuste sobre o papel, σ 0,09, igual em f3070; a mesa dá (51 %, 48 %)); luma 239 no centro (40 px), a 100 px das bordas 74 % (esq) e 73 % (dir) do centro; mesa 35 em (360,1060) e 23 em (360,1180) (razão 1,5). A luz é desta cena, por cima de fundo e peças; os anéis acima valem só aqui (não é um multiplicador fixo do vídeo).
  - Borda do papel: sem borda de cartão (o papel termina direto no fundo: topo 145–160 → 30 em 3 px, f3070); sem sombra (fundo plano 30 → 23 = vinheta).
  - Desfoque de movimento: nenhum; a −61 px/q (f3091) o traço de 2–3 px continua nítido (medido na conferência) (corrigido na conferência: era "leve arrasto horizontal de 2–4 px no pico do pan, baixa confiança").
  - Fio, brilho, aberração, profundidade, grão global: nenhum.
- Câmera (reestudo 20/11): f3066→f3074 aproximação ×1,022 (+6,8 %/s), −2,2/−0,2 px/q; pan para a direita (conteúdo para a esquerda), medido de 2 em 2 quadros: f3076 −8,6 px/q (+3,3 %/s) · f3082 −31,9 (−5,1 %/s) · f3090 −62,0 (−17,4 %/s) · f3100 −67,9 (−20,8 %/s, pico) · f3110 −40,3 (−11,1 %/s) · f3118 −12,1 (0 %/s) · f3122 −3,1 (+4,2 %/s); depois f3130→f3145 ×1,035 (+5,6 %/s), −1,8 px/q. O pan leva junto um pequeno recuo (até −21 %/s no pico) e uma leve descida (+3 px/q): é um movimento de "respirar para trás" enquanto atravessa.
- Câmera em 3 pares (correção 20/11, medido, `camera` com região x12 y173 696x643: começo f3065→f3073 +6,8 %/s, −2,1 px/q; meio, no pan, f3100→f3102 −68 px/q (−21 %/s) e f3110→f3114 −37 px/q (−10 %/s) (o par de 8 q f3102→f3110 não mede: 15 pontos); fim f3140→f3148 +5,5 %/s, −1,8 px/q. Fases: aproximação lenta até f3075 · pan para a direita f3076–f3122 · aproximação até o corte (confere a nota).
- Cadência (reestudo 20/11): 24 imagens/s (perfil f3084–f3094: 14,9–16,9 em todos os quadros; o marca-texto cresce a cada quadro).
- Legenda nesta cena (reestudo 20/11): amarela #f1e718, altura 32 px; atrás da tarja o papel claro na maior parte (luma 55–231): a tarja aparece bem; opacidade do censo não serve aqui (o detector confunde o amarelo do marca-texto e da pintura com a legenda); vale a tarja fixa de 59 % do vídeo. Blocos REAIS (folha da faixa e XOR quadro a quadro): 4 palavras com o ano (f3064–f3098, 1460 ms) · 1 (nacionalidade, f3099–f3107) · 2 (profissão + a palavra que apresenta o nome, f3108–f3123) · 1 (prenome, f3124–f3134) · 1 (sobrenome, f3135–até o corte). O nome é dividido em 2 blocos de 1 palavra; o marca-texto começa em f3120, 4 quadros antes do bloco do prenome.
- Entrada do texto (reestudo 20/11): o marca-texto é o texto do editor: cresce da esquerda para a direita, linear, ≈ 15–23 px/q (12 → 41 → 71 → 117 → 147 → 174 px em f3120–f3130), cor cheia desde o 1º quadro, frente macia, sem fade nem escala.
- Correção (reestudo 20/11): a tabela de blocos de `analises/V04.md` junta a apresentação do nome (profissão + nome completo) num bloco só (nº 211, f3108–f3152) porque o detector leu o marca-texto como legenda; na tela são 3 blocos: profissão f3108–f3123, prenome f3124–f3134, sobrenome f3135– (corrigido no reestudo, folha x150 y840 f3064–f3148 e XOR da máscara amarela y855–888).

## CONSTRUÇÃO
1. fundo: tela fixa marrom-escura lisa (só aparece acima e abaixo do papel).
2. documento: scan/foto do desenho original em papel creme envelhecido, sem borda e sem sombra; em f3070 x14–720 × y89–888 (98 % × 62 %, centro (51 %, 38 %)), giro −0,9°; corte seco em 0 ms.
3. marca-texto: retângulo amarelo #eec236 em multiplicar, alt 25 px (2 %), sobre a assinatura em x210–389 × y826–851 (f3145); cresce da esquerda para a direita de 2335 a 2794 ms (11 quadros), linear.
4. câmera sobre 2 + 3: 0–500 ms aproximação +6,8 %/s e deriva −2 px/q; 500–2420 ms pan para a direita com curva acelera-cruzeiro-freia (pico −68 px/q ≈ 1630 px/s em ≈ 1500 ms) e recuo de até −21 %/s junto com o pico; 2420 ms ao fim aproximação +5,6 %/s.
5. luz da cena por cima de tudo (fundo e peças; não é vinheta fixa do vídeo): poça centrada em (49 %, 40 %), luma 239 no centro, a 100 px das bordas 74 % e 73 % do centro, mesa 35 em (360,1060) e 23 em (360,1180); anéis medidos com `borda` 100/79/57/25/15 % (f3100) (corrigido na conferência: era "vinheta da cena 100/79/57/25/15 %, centro ≈ 40 % da altura", lida como vinheta fixa do vídeo) (alinhado ao reestudo).
6. legenda L01 (tarja bem visível sobre o papel claro), logo abaixo do marca-texto.
- Linha do tempo (ms a partir de f3064): 0 corte seco (−36 ms da 1ª palavra) e legenda com o ano · 500 pan começa (+195 ms do ano) · 1460 nacionalidade · 1500 pico do pan · 1835 profissão · 2335 marca-texto começa (−30 ms do prenome) · 2420 pan termina · 2502 prenome · 2794 assinatura toda marcada · 2961 sobrenome · 3587 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: o documento (de autoria da pessoa citada), onde está a assinatura (o pan termina com ela logo acima da legenda), a largura do pan (a do documento).
- O que NÃO fazer: pan linear; marcar o nome antes da fala; pôr o documento em cartão; deixar a assinatura longe da legenda; confiar no censo de legenda numa cena com amarelo próprio. Pôr uma vinheta fixa igual em todas as cenas: a luz é desta cena, com centro e força próprios, por cima de fundo e peças (correção 20/11).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "documento original de autoria da pessoa citada" (desenho, projeto, manuscrito);
  - "assinatura/nome no documento" (marcado na hora em que o nome é dito).
- Nesta referência as lacunas foram preenchidas com: projeto de camuflagem dazzle de um navio; assinatura de Norman Wilkinson.
- Receita de tratamento de cada imagem: scan real do documento, papel envelhecido, cores originais, tela cheia com vinheta; marca-texto amarelo-ouro sobre a assinatura.
- Regra de escolha: apresentação de pessoa pela OBRA dela ("um pintor britânico chamado X") → mostra o documento que ele fez e marca o nome dele no próprio documento. Teste em 2 temas: Claude Code → print do primeiro commit do autor com o nome dele marcado; café → rótulo original de uma marca com a assinatura do fundador marcada.

- Receita de tratamento (reestudo 20/11): documento original escaneado (papel creme envelhecido com pintinhas, cores de tinta originais), sem correção de cor, nitidez alta; marca-texto amarelo-ouro em multiplicar, alt 2 % do quadro.
- Teste de generalização: Claude Code → print do primeiro commit do autor; pan até a linha com o nome dele, marcado quando o nome é dito; café → a patente original do coador, pan até a assinatura do inventor, marcada no nome.

- Confiança: corte, caixas, cores, pan = medido; início/fim exato do wipe = medido por contagem de pixels (±1 quadro).
