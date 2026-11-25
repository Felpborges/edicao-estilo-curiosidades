# V01-A20 · estação "1943" da linha do tempo: foto-documento com elipse num rosto + 2ª foto por cima
- Categoria: P21 · Linha do tempo e dado em papel (provisória do analista: (provisória) estação de linha do tempo: foto(s) impressa(s) acima da régua de anos)
- Fonte: V01 quadros f1341–f1440 (55,88–60,00 s; 100 quadros ≈ 4167 ms) (remedido: a borda da foto já aparece na direita em f1341; antes f1345) · 24 fps
- Fala: "1943, he was recruited to Los Alamos for the Manhattan Project."
- Tipo de fala: data (biografia: onde a pessoa estava naquele ano)
- Gatilho: a foto entra pela direita em f1341 = 55875 ms, −5 ms antes do início da palavra nº 178 "1943," (55880 ms) (remedido, folha f1337–f1344; antes f1345, +162 ms; é a chegada do chicote V01-A19, que começa em f1339). Elipse em f1353 = 56375 ms, −365 ms antes da nº 179 "he" (56740 ms). 2ª foto em f1399 = 58292 ms, +132 ms depois da nº 185 "for" (58160 ms).
- Quadro-chave: f1420
- Camadas ativas: cena de tela cheia | grafismo (linha do tempo + elipse à mão) | legenda | b-roll (fotos)
- Leitura dos strips: strip.jpg = quadros f1349 a f1366 (chegada e elipse), de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 18 células. strip-saida.jpg = quadros f1396 a f1406 (entrada da 2ª foto), mesma regra, 11 células. strip-geral.jpg = quadros f1343 a f1442, de 3 em 3, 34 células. Cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-elipse-documento.jpg = quadro f1380, região x270 y340 190x240 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: 1ª estação da biografia ("em 1943, foi recrutado…"); o editor prova o fato com um documento da época e aponta a pessoa nele, depois mostra o lugar/projeto nomeado.
- Por que este design: documento grande acima da régua; elipse no rosto da pessoa entre muitos rostos (agulha no palheiro); a 2ª foto, menor e vertical, cai no centro deixando o documento aparecer dos lados.
- Por que estas cores: tudo P&B de arquivo; o único acento é o amarelo translúcido da elipse; o ano aceso em branco na régua.
- Por que estes efeitos: elipse de marcador com textura de traço seco (estrias), sombras caídas para baixo (≈ 18 px embaixo) entre as fotos (alinhado ao reestudo); nada de vinheta.
- Por que este movimento: a foto chega pelo chicote (ease-out), a elipse se desenha logo em seguida (250 ms, desacelerando), a 2ª foto estala na palavra do projeto; deriva quase nula para ler os rostos.
- Sensação do movimento: investigação ("achamos ele aqui"); produzida pela elipse revelada em 6 quadros com diferença 47 → 21 por imagem, entrada de 3 imagens da 2ª foto (base y740 → 727 → 722) e deriva de ±1,5 %/s.

## FORMA (fixa: reproduzir igual)
- Design (quadro cheio, med.py restrito acima da régua y<765):
  - Foto 1 horizontal (o documento que prova o fato da data, em P&B) com borda de papel: assentada f1355 x46–676, y195–701 = 631x507 px (87,6 % da largura, 39,6 % da altura), centro (50,0 %, 35,1 %). Fica ACIMA da régua (base da foto y≈701–707, régua y770–811).
  - Elipse à mão amarelo-mostarda translúcida em volta da pessoa citada dentro do documento: caixa x284–439, y356–558 = 155x202 px (21,5 % da largura, 15,8 % da altura), centro (361, 457) = (50,2 %, 35,7 %) (remedido, f1380; antes ≈ 70x90 px observado). Fica TODA coberta pela foto 2 a partir de f1399: não aparece no still f1420. (medido; mesmo traço de V01-A15)
  - Foto 2 vertical (P&B, o lugar/projeto citado), cai por cima no centro, BEM MENOR que a foto 1 e um pouco mais baixa, com a foto 1 aparecendo pelos lados: a foto 2 sozinha vai de x146 a x580 e de y≈210 a y712 = 434x502 px (60,3 % da largura, 39,2 % da altura), centro (50,4 %, 36,0 %), contra a foto 1 em y≈193–696 no mesmo quadro (remedido, f1420; antes "um pouco menor e mais alta"). Conjunto f1405 x37–683, y183–721. (medido)
  - Régua de anos embaixo (V01-A25), com o ano da estação aceso. (medido em A25)
- Movimento:
  - Foto 1: aparece na borda direita em f1341, chega pela direita no chicote (V01-A19) e assenta em f1353 (12 q, 500 ms) (remedido). (medido)
  - Elipse: desenha-se de f1353 a f1359 (6 q, 250 ms; fechada em f1359, folha ampliada f1351–f1361; um traço tênue talvez já em f1351) (remedido; antes até ≈ f1361, ≈ 8 q); diferença na região f1351 62,9 (chegada da foto) · f1353 47,3 · f1355 33,8 · f1357 28,2 · f1359 21,4 · f1361 17,2 · f1363 13,1 · f1365 9,1 (desacelera). (medido no perfil, região x150 y200 420x500)
  - Foto 2: entra em f1399, assenta em 3 imagens = 4 q até o 1º quadro assentado (f1399 → f1403; perfil 56,0 · 25,8 · 17,6 · depois 7,4) (remedido) (base do conjunto f1399 y740 → f1401 y727 → f1403 y722). (medido)
  - Saída: chicote para a esquerda em f1439 (V01-A21). (medido)
  - Cadência 12 imagens/s. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | foto-documento chega (chicote) | f1341 (remedido) | 12 q (500 ms) | deslize da direita | ease-out | nº 178, a data | −5 ms |
  | elipse na pessoa citada | f1353 | 6 q (250 ms) (remedido) | traço se revela | desacelera | nº 179, o sujeito (1ª palavra depois da data) | −365 ms |
  | 2ª foto por cima | f1399 | 4 q (167 ms) (remedido) | escala + cai | estalo | nº 185, a preposição antes do nome do projeto | +132 ms |
- Ritmo: foto 1 no topo 58 q (2417 ms, de f1341; remedido) com a elipse completa e parada ≈ 1,7 s (f1359–f1398); foto 2 no topo 40 q (1667 ms). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Mesa: a de V01-A01 (parada).
  - Foto 1 (documento P&B): `textura` f1380 em 80,230,100,90: #999497, grão 16 (conteúdo: grade de retratos), ac1 +0,75, cinza puro; a imagem é fixa, sem vídeo (f1380×f1382 +0,81 → +0,97 alinhada), mas o grão dos CLAROS é VIVO: teste novo (f1380×f1382, alinhado pela afim da foto, região 80,225,560,440, pixels lisos) resíduo ÷ σ 1,09 nos claros (3,0 níveis) × 0,47 nos escuros e 0,62 nos médios (medido; corrigido na conferência: era "PARADA").
  - Foto 2 (P&B): `textura` f1420 em 200,250,200,80: #bdbbbe (céu claro), grão 12,8, ac1 +0,62; a imagem é fixa (+0,90, a região mede figuras), mas o grão dos claros é vivo em parte: teste novo (f1420×f1422, região 170,230,390,460) resíduo ÷ σ 0,77 nos claros (4,4 níveis) × 0,33 nos escuros; a conferência mediu no céu liso correlação alinhada +0,52 estável (medido; corrigido na conferência: era "PARADA (+0,90)").
  - Bordas: off-white #dbd8cf, luma 213–219, 7 px (`sombra` dir f1420 x574–580), canto vivo.
  - Elipse: marcador amarelo translúcido com textura de traço seco (estrias finas ao longo do traço, bordas irregulares; detalhe-elipse-documento), ≈ 6 px.
- Efeitos (reestudo 20/11):
  - Sombras CAEM PARA BAIXO (`sombra` alinhada): foto 1 sozinha (f1380, caixa 46,195,631,507): embaixo −55 % no 1º px fora, volta em 18 px; em cima −17 %, volta em 5 px (quase só o 1º px); lados encostam na borda do quadro. Foto 2 (f1420, caixa 146,210,434,502): embaixo, sobre a mesa, −49 %, volta em 18 px; à direita, sobre a foto 1, −58 % no 1º px e faixa escura de ≈ 12 px; em cima, sobre a faixa clara da foto 1, −21 %, 7 px (medido na conferência). Na borda direita, linhas y450–490, a foto 1 começa a luma 42 e sobe para 55 em ≈ 8 px. (medido; corrigido na conferência: era "≈ −25 %, curta, sem deslocamento")
  - Vinheta, brilho, desfoque de movimento (fora do chicote), profundidade, grão global, aberração: nenhum (f1380, f1420).
- Câmera (reestudo 20/11): deriva mínima: `camera` foto 1 f1365→f1395 ×1,0182 (+1,4 %/s), sobe 0,44 px/q; foto 2 f1405→f1435 ×0,9818 (−1,5 %/s), sobe 0,1 px/q (a deriva troca de sentido com a foto nova, como nas pilhas). Régua e mesa paradas. Chegada e saída pelos chicotes (V01-A19, V01-A21).
- Cadência (reestudo 20/11): 12 imagens/s (perfil da elipse só nos ímpares f1353–f1365; foto 2 em f1399/f1401/f1403).
- Legenda nesta cena (reestudo 20/11): 6 blocos: a data (f1338–f1358, 2 palavras), o verbo (f1359–f1374, 3 palavras, a elipse fechou em f1359: mesmo quadro), o lugar citado (f1375–f1398, 4 palavras), o nome do projeto (f1399–f1419, 4 palavras, MESMO quadro da foto 2), a última palavra do nome repetida sozinha (f1420–f1434; troca entre blocos de mesma largura que o censo não vê, achada pela conferência), a data seguinte (f1435–f1453, 2 palavras, atravessa o chicote de saída f1439). Atrás da tarja: a mesa → tarja preta pura lida como preta (74 % no vídeo, medida direta da conferência); acima dela a régua (42 px de folga). Outro texto junto: os anos da régua. Cor #e8de52.

## CONSTRUÇÃO
1. fundo: mesa fixa; régua de anos (V01-A25) fixa embaixo, com o 1º ano aceso.
2. foto 1 (documento P&B, imagem fixa com grão vivo nos claros, re-sorteado a 12/s): chega pelo chicote (V01-A19), assentada em 500 ms (f1353) com caixa x46–676 y195–701 (87,6 % × 39,6 %), centro 50 % × 35,1 %, base acima da régua; borda off-white 7 px; sombra caída para baixo (18 px embaixo a −55 %, nada em cima).
3. elipse: marcador amarelo translúcido com textura de traço seco, ≈ 6 px, 155 × 202 px, centro 50,2 % × 35,7 %, em volta da pessoa no documento; revelada de 500 ms (f1353) a 750 ms (f1359), desacelerando.
4. foto 2 (vertical P&B, imagem fixa com grão vivo parcial nos claros): cai em 2417 ms (f1399), x146–580 y210–712 (60,3 % × 39,2 %), no centro, cobrindo a elipse e deixando a foto 1 aparecer dos lados; 3 imagens de estalo (base y740 → 727 → 722); sombra caída para baixo: 18 px a −49 % embaixo sobre a mesa, ≈ 8–12 px dos lados sobre a foto 1, 7 px a −21 % em cima (corrigido na conferência: era "≈ 8 px −25 %").
5. deriva: +1,4 %/s com a foto 1, −1,5 %/s com a foto 2.
6. saída pelo chicote em 4083 ms (f1439, V01-A21).
- Linha do tempo (ms a partir de f1341): 0 foto 1 entrando · 500 assentada + elipse começa · 750 elipse fechada + legenda do verbo · 1417 legenda do lugar · 2417 foto 2 + legenda do nome do projeto · 3250 legenda da última palavra repetida · 3917 legenda da data seguinte · 4083 chicote de saída.
- Parâmetros que dependem do conteúdo: o documento e a pessoa a circular; a 2ª foto (lugar/projeto); proporções (documento horizontal, 2ª foto vertical).
- O que NÃO fazer: elipse limpa de vetor (tem textura de traço seco); 2ª foto do mesmo tamanho da 1ª (é bem menor, deixa a 1ª aparecer); foto passando por trás da régua (fica acima dela); fotos com grão parado ou sombra igual em volta.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "documento que prova o fato da data": foto de documento/registro de época.
  - "a pessoa no documento": o que circular à mão.
  - "foto do lugar/projeto citado".
- Nesta referência as lacunas foram preenchidas com: grade 3x5 de fotos de crachá de Los Alamos (elipse no rosto de Bradner); foto de dois homens no campo de testes do Projeto Manhattan; ano aceso "1943".
- Receita de tratamento de cada imagem: fotos/documentos reais P&B, borda de papel 7 px (alinhado ao reestudo), 85–90 % da largura, acima da régua de anos; elipse amarela translúcida à mão. (reestudo 20/11) Medido: P&B neutro (grão por canal idêntico), fotos fixas (sem vídeo) com grão vivo nos claros (resíduo ÷ σ 0,77–1,09 × 0,33–0,47 nos escuros), sombra caída para baixo, contraste médio, sem vinheta; borda off-white 7 px luma ≈ 216; elipse com textura de traço seco.
- Regra de escolha: em cada data, um documento que prova onde a pessoa estava (com ela circulada) e depois a foto do lugar/projeto nomeado.
- Teste de generalização: (1) Claude Code: "em 2021, ele entrou na Anthropic" → print da página de equipe com o rosto circulado; foto do escritório. (2) café: "em 1901, Bezzera registrou a patente" → página da patente com o nome circulado; foto da oficina.

- Confiança: caixas e tempos medido; tamanho da elipse observado.
