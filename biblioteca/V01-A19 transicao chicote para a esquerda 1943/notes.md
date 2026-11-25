# V01-A19 · transição em chicote para a esquerda (entrada na 1ª data da linha do tempo)
- Categoria: P11 · Viagem de câmera entre peças (provisória do analista: (provisória) transição: deslize horizontal com borrão de movimento (chicote), trocando de foto)
- Fonte: V01 quadros f1339–f1353 (55,79–56,38 s; 15 quadros ≈ 625 ms) · 24 fps
- Fala: "In 1943,"
- Tipo de fala: data (1ª data de uma sequência cronológica)
- Gatilho: começa em f1339 = 55792 ms, +12 ms depois do início da palavra nº 177 "In" (55780 ms). A data falada dispara o deslize.
- Quadro-chave: f1343
- Camadas ativas: transição | cena de tela cheia | grafismo (linha do tempo, V01-A25) | legenda
- Leitura dos strips: strip.jpg = quadros f1336 a f1356, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 21 células; cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-borrao-chicote.jpg = quadro f1343, região x200 y60 520x330 px, ampliada 1× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala abre a 1ª data de uma sequência ("em 1943"); o editor troca de foto deslizando a mesa para a esquerda, como se o tempo andasse para a direita na régua.
- Por que este design: nenhum elemento novo; o movimento É o design: as fotos correm, a régua fica.
- Por que estas cores: as das fotos; nada se acrescenta.
- Por que estes efeitos: borrão horizontal proporcional à velocidade (≈ 26–30 px no meio, ≈ 8 px na chegada): é o que vende a "câmera chicoteando".
- Por que este movimento: saída rápida e entrada que freia forte (ease-out), em 7 imagens a 12/s; a régua parada embaixo dá a referência do deslocamento.
- Sensação do movimento: "pulo no tempo" enérgico mas controlado; produzida por passos de 93 → 54 → 24 → 7 px na chegada da foto nova, borrão só nas imagens rápidas.

## FORMA (fixa: reproduzir igual)
- Design: não tem elemento próprio; move a cena inteira de cima (fotos) para a esquerda, como uma câmera que corre para a direita sobre uma mesa. A linha do tempo de baixo (y770–811) NÃO se move. (medido: perfil da faixa da linha do tempo ≈ 0 durante o deslize)
- Movimento (med.py, região acima da linha do tempo):
  - Saída da cena antiga: f1339 começa a andar para a esquerda com borrão horizontal forte; f1341–f1343 o conteúdo cobre a tela toda com rastro; some pela esquerda até ≈ f1345. (medido: caixa vira x0–719 de f1341 a f1345; borrão observado)
  - Entrada da foto nova pela direita, freando: borda esquerda da foto f1347 x110 → f1349 x77 → f1351 x53 → f1353 x46 (passos de 33, 24 e 7 px por imagem: desaceleração forte, ease-out). (medido)
  - Duração total f1339 → f1353 ≈ 14 q (583 ms), em 12 imagens/s. (medido)
  - Borrão de movimento horizontal nas imagens rápidas (f1341–f1349, ainda ≈ 8 px em f1349), nenhum nas 2 de chegada (f1351–f1353) (alinhado ao reestudo). (observado)
- Ritmo: acontece 60 ms depois de a linha do tempo surgir (f1337); a foto nova chega assentada 0,6 s depois do início da palavra da data. (medido)
- Som: nenhum efeito detectado (áudio mono; nenhum ruído largo no meio fora da voz em f1339–f1353). (medido)
- Textura (reestudo 20/11): sem superfície própria; mesa de V01-A01 por trás (parada: a poça de luz não anda com o chicote), fotos com as texturas da receita de fotos impressas (borda off-white, grão de arquivo).
- Efeitos (reestudo 20/11): desfoque de movimento horizontal, só nas imagens rápidas: borda esquerda da foto nova em f1343 com rampa de ≈ 26–30 px (linha y260: luma 47 em x384 → 168 em x410), em f1349 rampa de ≈ 8 px (x76–84); nas imagens de chegada (f1351–f1353) nítida. Sem borrão vertical, sem fade, sem escala. Vinheta, brilho, grão, aberração: nenhum.
- Câmera (reestudo 20/11): é um deslize horizontal puro das fotos para a esquerda (escala ×1,000, giro 0); a régua e a mesa ficam paradas. Borda esquerda da foto nova: f1345 x224 → f1347 x131 → f1349 x77 → f1351 x53 → f1353 x46 (passos −93 / −54 / −24 / −7 px por imagem: ease-out forte). A foto antiga sai pela esquerda entre f1339 e f1345 com a mesma velocidade alta.
- Cadência (reestudo 20/11): 12 imagens/s: `perfil` f1338–f1356 (0,15 / 40,1 / 0,08 / 58,6 / 0,05 / 64,9 / 0,02 / 55,9 / 0,01 / 42,8 / 0,12 / 49,1 / 0,07 / 46,5 / 0,18 / 32,5 / 0,06 / 22,0 / 0,07): troca só nos ímpares, mesmo no chicote.
- Legenda nesta cena (reestudo 20/11): 1 bloco, a data com a preposição (f1338–f1358, 2 palavras), que entra 1 quadro ANTES do chicote começar (f1339) e 1 depois da régua (f1337); o próximo, o verbo da estação (3 palavras), entra em f1359, quando a foto nova já assentou. A legenda não se move com o chicote. Atrás da tarja: a mesa → tarja preta pura lida como preta (74 % no vídeo, medida direta da conferência).

## CONSTRUÇÃO
1. fundo: mesa fixa.
2. régua de anos (V01-A25): na faixa y771–811, abaixo das fotos, sem sobreposição; não se move.
3. grupo de fotos da cena anterior: de 0 ms (f1339) desliza para a esquerda, acelerando, com borrão horizontal ≈ 26–30 px; some pela esquerda até ≈ 250 ms (f1345).
4. foto nova: entra pela direita junto (já visível em f1343), atravessa com borrão e freia: em 250 ms está com a borda esquerda em x224, 333 ms x131, 417 ms x77, 500 ms x53, 583 ms x46 (assenta). Borrão proporcional ao passo (0 nas 2 últimas imagens).
- Linha do tempo (ms a partir de f1339): −42 legenda da data · 0 saída começa · 167–333 pico (diferença 58–65) · 583 foto nova assentada · 833 legenda seguinte.
- Parâmetros que dependem do conteúdo: nenhum além das fotos de saída e chegada; a direção é sempre para a esquerda (tempo anda para a direita).
- O que NÃO fazer: mover a régua junto; chicote com curva linear ou suave dos dois lados (é rápido e freia forte); borrão igual em todas as imagens (é proporcional à velocidade); chicote a 24/s.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: nenhuma imagem própria; liga a cena anterior à 1ª foto da data.
- Nesta referência as lacunas foram preenchidas com: (não se aplica)
- Receita de tratamento de cada imagem: não se aplica (as fotos de saída e de chegada seguem a receita das fotos impressas).
- Regra de escolha: cada data nova falada numa sequência cronológica = um chicote para a esquerda (o tempo "anda para a direita" na linha do tempo).
- Teste de generalização: (1) Claude Code: "em 2021… em 2023… em 2025" → um chicote a cada ano, trocando prints de cada época. (2) café: "em 1600… em 1900… hoje" → um chicote a cada data, trocando gravura, foto antiga, foto atual.

- Confiança: posições e tempos medido; borrão observado.
