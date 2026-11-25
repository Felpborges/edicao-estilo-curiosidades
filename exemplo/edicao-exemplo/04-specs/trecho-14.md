# Trecho 14 · Recortes dos dois logos, um por palavra · P16 · Ref V04-A02
Fala: "Então, ao invés de você pagar pelo Gamma ou pelo Canva,"   ·   Janela no clipe: 32 960 a 35 282 ms   ·   Entra por: corte seco (vindo do maço do carrossel, trecho 13)

Clipe: 1080x1920, 23,976 fps, 1 q = 41,708 ms. Quadros do clipe entre parênteses.

## 0 · O que está na tela antes do 1º logo (≈ 1,1 s de "Então, ao invés de você pagar pelo")

**Na referência:** o V04-A02 entra por corte seco com a composição **já montada**: o objeto do tema recortado,
grande, deitado no centro-esquerda (57,9 % da largura, −5°), e um cartão de papel creme à direita (o apoio onde
os itens comparados vão pousar), com a câmera aproximando devagar desde o 1º quadro (medido: dif 66,6 no corte e
≈ 1,7 nos quadros seguintes; nada mais entra no corte). As entradas que vêm depois (3 amostras em pop seco e um
contorno desenhado) são da enumeração "verde, marrom e preto" e do detalhe "bordas duras": esta fala não tem
enumeração nem detalhe, então essas lacunas ficam vazias (não é forma nova, é lacuna sem conteúdo).

**Conteúdo equivalente neste tema:** o objeto do tema da frase é **o dinheiro que se paga**. P16, regra de
escolha: "o abstrato vira um objeto que o represente: um valor vira o objeto que o simboliza". E o P16 tem a
variação "recorte reaproveitado de cena anterior, para o público reconhecer" (regra, 3 vídeos). Então: **o maço
de notas do trecho 3** ("economizar centenas de dólares"), os mesmos recortes no mesmo arranjo, como objeto
principal; o cartão de papel creme à direita, vazio, esperando os logos. Descartado: o recorte do chat do Claude
(é a resposta do trecho 15, "tudo em uma única conversa"; mostrar aqui gasta o fecho).

## 1 · Linha do tempo da cena (relativa às palavras)

| passo | o que acontece | gatilho (palavra, índice, deslocamento em ms) | duração (ms · quadros) | curva |
|---|---|---|---|---|
| 1 | Corte seco para a mesa já montada: maço de notas (objeto) + cartão de papel creme | 40 ms antes de "Então," (126) → f790 (32 950 ms; −42 ms) | 0 q | — |
| 2 | Câmera, fase A: aproximação | f790 → f812 | 23 q ≈ 959 ms | linear |
| 3 | Logo do Gamma desliza da direita e pousa na palavra (k = 0 em f812, fora do quadro) | 1º quadro visível 213 ms antes de "Gamma" (133) → f813 (33 909 ms); assenta f819 (34 159 ms; +37 ms) | 7 q = 292 ms (f813–f819) | freia (frações medidas, seção 2) |
| 4 | Câmera, fase B: a aproximação vira recuo | f813 → f824 | 12 q = 500 ms | velocidade varia linear (ease-in-out na escala) |
| 5 | Logo do Canva desliza de baixo-direita e pousa na palavra (k = 0 em f825) | 1º quadro visível 291 ms antes de "Canva," (136) → f826 (34 451 ms); assenta f833 (34 743 ms; +1 ms) | 8 q = 334 ms (f826–f833) | freia (frações medidas) |
| 6 | Câmera, fase C: recuo com deriva para a esquerda até o corte (corta em movimento) | f825 → f844 | 20 q ≈ 834 ms | linear |
| 7 | Saída: corte seco para o trecho 15 | 1 a 2 q antes de "você" (137): último quadro f844, corte em f845 (35 244 ms; −38 ms). O quadro exato é do trecho 15 | 0 q | — |

## 2 · FORMA (copiar igual) — px de 1080x1920

- **Fundo / mesa:** a mesa global do motor. No V04-A02 o fundo é liso, sem textura, vinheta forte: centro-baixo
  #0e0c08, borda #0b0a06, cantos #010101 a #070602 (nota, medido); reconferi #080703 em (600, 1150) e #030303
  no canto de cima (f31): bateu.
- **Objeto principal (maço de notas do trecho 3):** caixa de **625 px de largura** (57,9 %), centro **(511, 922)**
  = (47,3 %, 48,0 %), giro **−5,0°** (nota, medido em f31: pants 417 × 766 px em 720). A altura sai do próprio
  arranjo do maço (no V01-A43 o maço final é 550 × 379 em 720 = 1,45:1 → ≈ 431 px). Tratamento: igual ao do
  trecho 3 (os mesmos recortes). Sombra curta e macia sobre a mesa.
- **Cartão de apoio (papel creme):** **267 × 642 px** (24,7 % × 33,4 %), centro **(938, 789)** = (86,8 %, 41,1 %),
  giro **+4°** (horário), sem borda de cartão, papel texturizado #bca488 na luz e #7e6d5d na parte que cai na
  vinheta. Medido agora em f31 (folha ampliada e `ferr.py caixa/cor`): x 536–714, y 312–740 em 720; a borda
  esquerda vai de x 565 no topo a x 534 na base (4,1°). Fica por cima do maço onde se tocam (ordem da nota:
  objeto → cartão → recortes que entram).
- **Câmera (medida agora por registro de pontos em V04-A02; a nota só tinha "+10 % em 1,2 s"):**
  - Fase A (f790–f812): zoom **+9 %/s** (×1,0036 por quadro) em torno do centro do quadro. Medido f31–f55:
    ×1,0133 a ×1,0190 a cada 4 q (a nota dizia ≈ +8 %/s: bateu).
  - Fase B (f813–f824): a taxa vai de +9 %/s a **−11 %/s** em 12 q, linear na velocidade. Medido f103–f115:
    ×1,0185 → ×0,9965 → ×0,9835 → ×0,9776 a cada 4 q (12 q de virada).
  - Fase C (f825–f844): **−11 %/s** (×0,99515 por quadro), conteúdo deslizando **2,7 px/q para a esquerda**.
    Medido f117–f153: ×0,954 a ×0,966 a cada 8 a 10 q; o centro do quadro anda 1,3 a 2,9 px/q (720) para a
    esquerda. Corta ainda andando (P16 permite).
  - **O que a referência faz e aqui não entra:** entre f55 e f107 a câmera do V04-A02 dá um push-in forte
    (acelera até ×1,07 a cada 4 q, ≈ +50 %/s no pico, total ×2,04) para dentro do detalhe que recebe o contorno
    desenhado ("bordas duras"), e só então recua. Esta fala não tem detalhe nomeado, então o push não tem lacuna;
    ficam a aproximação de antes e o recuo durante a entrada dos itens comparados, na ordem da referência.
- **Recorte 1 · logo do Gamma (1º item comparado):**
  - Assentado (f819): **370 px de largura** (34,3 %; nota f145: 247 × 365 em 720), centro **(850, 706)**, giro
    **−4°**. Posição: pousado sobre a metade de cima do cartão de apoio, avançando sobre a ponta do maço, como a
    folha do V04-A02 (centro a 37 % da altura do cartão e ≈ 15 % para dentro da borda esquerda dele, medido em
    f145). O valor no quadro da referência, (72,5 %, 38,4 %), não serve direto porque lá a cena já estava ×1,74
    maior pelo push (inferido).
  - Entrada: desliza **da direita**, começando com a borda esquerda em x = 1080 (fora do quadro), quase na
    horizontal (desce ≈ 24 px no caminho, observado). Fração do caminho por quadro, k = 1…7 (medido agora na
    folha f116–f125, borda esquerda da peça, ±12 px em 720): **0,18 · 0,53 · 0,70 · 0,81 · 0,95 · 0,99 · 1,00**.
    Pico de velocidade no 2º quadro e chegada freando; nenhum quique. Giro extra de +6° no 1º quadro que some na
    mesma fração (o "leve giro" é observado; o valor é inferido).
- **Recorte 2 · logo do Canva (2º item comparado):**
  - Assentado (f833): **336 px de largura** (31,1 %; nota f145: 224 × 300 em 720), centro **(798, 962)**, giro
    **+5°**. Posição: sobre o canto de baixo-esquerdo do cartão de apoio, encostando na borda dele e na ponta do
    maço, cobrindo um pouco a base do logo do Gamma (por cima dele), como a casca sobre a folha no V04-A02 (centro
    a 77 % da altura do cartão, logo à esquerda da borda dele, medido em f145). Inferido pela mesma razão.
  - Entrada: desliza **de baixo-direita**: começa com a borda esquerda em x = 1080 e ≈ 135 px mais baixo que o
    ponto final (observado: sobe ≈ 90 px em 720 enquanto anda para a esquerda). Fração por quadro, k = 1…8 (medido
    agora na folha f134–f145): **0,23 · 0,40 · 0,60 · 0,73 · 0,83 · 0,90 · 0,97 · 1,00**. Chega mais girado:
    giro extra de +10° no 1º quadro que some na mesma fração (observado, valor aproximado).
- **Contorno dos logos:** **contorno de adesivo off-white ≈ 15 px** (10 px em 720, luminância 202 a 233, ≈
  #cac5bb a #e9e4da), com textura de papel e sombra fina escura em volta. **É o mesmo tratamento dos ícones das
  ferramentas no trecho 2** (P14, V01-A28): use exatamente o que o principal aplicar lá. O V04-A02 não tem
  contorno (V04 usa recorte limpo com sombra macia), mas o guia registra que cada vídeo usa um tratamento só, e
  neste vídeo os ícones oficiais já aparecem como adesivo; o plano também pede "contorno claro de adesivo".
- **Texto:** nenhum além da legenda global (tarja a 67 % = y ≈ 1286). Ela fica abaixo dos dois logos.
- **Taxa de imagem:** 24 (23,976), deslizes quadro a quadro (o V04-A02 anda em todos os quadros, medido).
- **Som:** nenhum (P16: 11 de 12 sem efeito; o V04-A02 sem efeito, medido).
- **Confiança:** composição do corte, tamanhos dos itens, durações e gatilhos = medido (nota, reconferidos na
  folha); curvas de entrada e câmera = medido agora; posições dos logos em relação ao cartão = inferido da relação
  medida em f145; giros finais dos logos = inferido (P16: 0 a 10°); contorno = decisão de coerência com o trecho 2.

## 3 · CONTEÚDO (deste vídeo)

| lacuna (papel) | preenchida com | receita de tratamento |
|---|---|---|
| objeto do tema (inteiro, grande) | o maço de notas de dólar do trecho 3 (o "que você paga"), reaproveitado | igual ao trecho 3 |
| apoio dos itens comparados | papel creme texturizado | foto real de papel, cor quente, textura visível, sem borda |
| 1º item comparado ("Gamma") | ícone oficial do Gamma | arquivo oficial com transparência, recortado pela silhueta do próprio ícone, cor original, contorno de adesivo |
| 2º item comparado ("Canva") | ícone oficial do Canva | idem |
| amostras / detalhe com contorno | vazias (a fala não tem enumeração nem detalhe) | — |

Regra de escolha: literal. Cada coisa nomeada (Gamma, Canva) vira o objeto real dela, na ordem da fala, pousando
na própria palavra; o valor abstrato ("pagar") vira o objeto que o simboliza, já visto no vídeo.

## 4 · IMAGENS NECESSÁRIAS

| # | o que é, exatamente | papel | de onde pode vir | formato e tamanho mínimo | tratamento a aplicar |
|---|---|---|---|---|---|
| 14-1 | Ícone/logo oficial do Gamma (gamma.app) | 1º item comparado | página de marca / press kit oficial do Gamma | PNG com transparência ou SVG, ≥ 740 px de lado | recorte pela silhueta, contorno de adesivo igual ao trecho 2 |
| 14-2 | Ícone/logo oficial do Canva | 2º item comparado | página de marca oficial do Canva | PNG com transparência ou SVG, ≥ 680 px de lado | idem |
| 14-3 | Papel creme texturizado (folha real fotografada) | apoio | foto do próprio Felipe ou acervo público de textura (licença livre) | ≥ 540 × 1300 px | sem borda, cor quente, recorte retangular |
| — | Maço de notas | objeto do tema | **os recortes já preparados para o trecho 3** | — | nada novo |

Baixar os logos e a textura exige o "sim" do Felipe (regra do projeto).

## 5 · Piso de leitura e ritmo

- Cena de tela cheia: f790–f844 = 2 294 ms (≥ 1,5 s). OK.
- Logo do Gamma: na tela f813–f844 = 1 335 ms; assentado 1 084 ms. OK.
- **Logo do Canva (o pedido de verificação):** na tela f826–f844 = **792 ms**; assentado f833–f844 = **500 ms**;
  da palavra "Canva" até o corte = **502 ms**.
  - Piso "último item de lista ≥ 700 ms": **passa** se contado do 1º quadro visível (792 ms); **não passa** se
    contado da palavra ou do assentamento (≈ 500 ms).
  - A referência faz o mesmo: a composição completa do V04-A02 fica parada **459 ms** (f143–f153) antes do corte.
  - Não há como estender sem quebrar a sincronia: o corte para o trecho 15 tem de cair 1 a 2 q antes de "você"
    (137); alongar a cena 200 ms poria o corte no meio de "você tem". Começar o deslize mais cedo (14 q, como o
    V05-A48) só aumenta o tempo "na tela", não o assentado. **Proposta: manter**, registrando que o 2º logo fica
    ≈ 0,5 s parado, igual à referência.

## 6 · Dúvidas e o que não foi possível medir

- **Câmera:** usei a sequência medida (aproxima → vira → recua) sem o push forte do detalhe. A alternativa mais
  simples é o molde do P16: aproximação contínua +7 %/s do corte ao corte. O principal escolhe.
- **Contorno de adesivo × recorte limpo:** a Ref não tem contorno; segui o tratamento dos ícones do trecho 2 para o
  vídeo ter um tratamento só. Se o trecho 2 sair sem contorno, aqui também sai.
- **Posição dos logos:** a nota mede a posição em f145, com a cena ×1,74 maior por causa do push. Mantive a relação
  com o cartão de apoio (pousar sobre ele e avançar sobre o objeto), não o valor no quadro.
- **Giros:** o giro de entrada dos recortes (≈ +6° e +10° a mais) e os giros finais (−4°, +5°) são observados ou
  escolhidos dentro da faixa do P16; não medidos.
- **O maço como objeto:** é o mesmo objeto do trecho 3 a 30 s de distância. Se o Felipe preferir outro objeto para
  "pagar", a lacuna pede um objeto real que simbolize o pagamento (nunca uma fatura inventada).
- Não medido: a sombra dos recortes no V04-A02 em px (nota: "sombra curta e macia", observado).
