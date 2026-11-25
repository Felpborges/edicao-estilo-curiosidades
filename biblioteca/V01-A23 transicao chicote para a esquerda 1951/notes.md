# V01-A23 · transição em chicote para a esquerda (3ª data da linha do tempo)
- Categoria: P11 · Viagem de câmera entre peças (provisória do analista: (provisória) transição: deslize horizontal com borrão de movimento (chicote), trocando de foto)
- Fonte: V01 quadros f1532–f1546 (63,83–64,42 s; 15 quadros ≈ 625 ms) · 24 fps
- Fala: "By 1951,"
- Tipo de fala: data (última data da sequência)
- Gatilho: começa em f1532 = 63833 ms, +33 ms depois do início da palavra nº 202 "By" (63800 ms).
- Quadro-chave: f1538
- Camadas ativas: transição | cena de tela cheia | grafismo (linha do tempo, ponto anda) | legenda
- Leitura dos strips: strip.jpg = quadros f1529 a f1549, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 21 células; cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-borrao-chicote.jpg = quadro f1538, região x0 y150 720x560 px, ampliada 1× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: 3ª e última data; o mesmo chicote fecha a série e leva à estação final antes de voltar ao rosto.
- Por que este design: nenhum elemento próprio; o ponto da régua faz o salto mais longo (270 px, 6 anos).
- Por que estas cores: as das fotos.
- Por que estes efeitos: borrão horizontal nas imagens rápidas (detalhe f1538: bordas verticais com rastro de ≈ 20–25 px).
- Por que este movimento: começa mais suave que os anteriores (diferença 13 na 1ª imagem contra 40–51) e tem o pico no meio, acompanhando o ponto que precisa correr 3× mais.
- Sensação do movimento: "e anos depois…": o salto mais longo se sente mais longo; produzido por 7 imagens de chicote (583 ms) com diferença 13 → 29 → 36 → 31 → 21 → 18 → 17 → 11 a 12/s.

## FORMA (fixa: reproduzir igual)
- Igual a V01-A19/A21 (conferido: saída para a esquerda com borrão, chegada pela direita freando, linha do tempo parada, ponto anda). Medidas próprias:
- Movimento (med.py, região acima da linha do tempo):
  - Saída: f1534–f1538 conteúdo cobre a tela toda com rastro (caixa x0–719). (medido)
  - Entrada: borda esquerda da foto nova f1542 x77 → f1544 x52 → f1546 x44 (passos 25 e 8 px: ease-out). (medido)
  - Duração f1532 → f1546 ≈ 14 q (583 ms), 12 imagens/s. (medido)
  - Ponto da linha do tempo da 2ª para a 3ª data: diferença na faixa da linha de f1532 a f1546 (o último passo, de ≈ 20 px, cai em f1546 junto do assentar da foto) = 14 q (583 ms) (remedido, f1546); anda uma distância 3× maior que o salto anterior (3× mais anos, a 45 px/ano), no mesmo tempo. (medido)
- Ritmo: 3,9 s depois do chicote anterior (V01-A21). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11): sem superfície própria; mesa parada; fotos com borda off-white e grão de arquivo.
- Efeitos (reestudo 20/11): desfoque de movimento horizontal nas imagens do meio (f1534–f1540; detalhe f1538: rastro de ≈ 20–25 px nas bordas verticais e no conteúdo); nítido nas 2 últimas imagens. Vinheta, brilho, grão global, aberração: nenhum.
- Câmera (reestudo 20/11): deslize horizontal puro para a esquerda; mesa e régua paradas. Chegada: x77 (f1542) → x52 (f1544) → x44 (f1546) (medida antiga). Diferente dos 2 chicotes anteriores, a curva é ease-in-out (arranque mais suave) e não só ease-out, acompanhando o ponto da régua (passos 10/54/86/58/37/15/8/2 px, ver V01-A25).
- Cadência (reestudo 20/11): 12 imagens/s: `perfil` f1531–f1547: 0,02 / 13,0 / 0,06 / 29,0 / 0,01 / 36,5 / 0,06 / 31,3 / 0,03 / 20,8 / 0,07 / 18,0 / 0,03 / 16,9 / 0,05 / 11,4 / 0,24.
- Legenda nesta cena (reestudo 20/11): o bloco da data (2 palavras) entra em f1531, 1 quadro ANTES do chicote, até f1544; o bloco seguinte (a data repetida + o cargo, 6 palavras) entra em f1545, no penúltimo quadro do chicote (a legenda não espera a foto assentar aqui). Atrás da tarja: a mesa → tarja preta pura lida como preta (74 % no vídeo, medida direta da conferência).

## CONSTRUÇÃO
1. igual a V01-A19/A21, com curva ease-in-out: fotos saem para a esquerda de 0 ms (f1532) com arranque suave, pico de 167–250 ms, foto nova chega freando (x77 em 417 ms, x52 em 500 ms, x44 em 583 ms).
2. régua: o ponto corre 270 px (ano 2 → ano 3) nos mesmos quadros (V01-A25).
- Linha do tempo (ms a partir de f1532): −42 legenda da data · 0 chicote + ponto · 167–250 pico · 542 legenda seguinte · 583 foto e ponto assentados.
- Parâmetros que dependem do conteúdo: fotos; a distância do ponto (anos × 45 px).
- O que NÃO fazer: o mesmo arranque brusco dos outros chicotes num salto longo (aqui arranca suave); borrão nas imagens de chegada.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: nenhuma imagem própria.
- Nesta referência as lacunas foram preenchidas com: (não se aplica; o ponto anda de 1945 para 1951, 6 anos)
- Receita de tratamento de cada imagem: não se aplica.
- Regra de escolha: última data da sequência = último chicote; depois dela o vídeo volta ao rosto.
- Teste de generalização: (1) Claude Code: "e em 2025," → chicote final para o print atual. (2) café: "e hoje," → chicote final para a foto atual.

- Confiança: posições e tempos medido; borrão observado.
