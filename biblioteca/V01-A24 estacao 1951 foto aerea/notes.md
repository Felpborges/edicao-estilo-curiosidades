# V01-A24 · estação "1951" da linha do tempo: foto do lugar
- Categoria: P21 · Linha do tempo e dado em papel (provisória do analista: (provisória) estação de linha do tempo: foto impressa acima da régua de anos)
- Fonte: V01 quadros f1540–f1596 (64,17–66,54 s; 57 quadros ≈ 2375 ms) · 24 fps (remedido: a foto já aparece nítida em f1540, borda esquerda em x144)
- Fala: "1951, he was a physicist at Berkeley."
- Tipo de fala: data (+ lugar)
- Gatilho: a foto chega pela direita em f1540 = 64167 ms (remedido), +267 ms depois do início da palavra nº 203 "1951," (63900 ms) (chegada do chicote V01-A23).
- Quadro-chave: f1570
- Camadas ativas: cena de tela cheia | grafismo (linha do tempo) | legenda | b-roll
- Leitura dos strips: strip.jpg = quadros f1540 a f1550, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 11 células. strip-geral.jpg = quadros f1540 a f1598, de 2 em 2, 30 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-canto-borda.jpg = quadro f1570, região x20 y640 140x110 px, ampliada 4× sem suavizar · detalhe-fundo-realce.jpg = quadro f1570, região x0 y1000 240x160 px, ampliada 2× sem suavizar, contraste ×6 em volta da média · detalhe-chicote-f1542.jpg = quadro f1542, região x60 y300 300x200 px, ampliada 2× sem suavizar (meio da chegada).


## LEITURA DE EDITOR
- Por que esta cena aqui: é a 3ª e última estação da régua de anos; a fala dá data + lugar, e o lugar pede uma foto que mostre o lugar inteiro de uma vez.
- Por que este design: uma foto só, grande (88 % da largura), igual às estações anteriores: a repetição da forma faz a régua ser lida como "capítulos" e o olho só procura o que mudou (o ano aceso e a foto).
- Por que estas cores: foto de arquivo P&B neutra sobre o fundo quase preto; a única cor da tela é o amarelo da legenda, então nada compete com a leitura.
- Por que estes efeitos: borda de papel off-white e sombra caída para baixo (19 px embaixo, quase nada em cima) (alinhado ao reestudo) fazem a foto parecer um objeto físico pousado na mesa; sem vinheta própria e sem brilho, para não parecer "filtro".
- Por que este movimento: o chicote da estação anterior traz a foto já andando (sensação de virar a página do tempo) e a aproximação lenta e que desacelera mantém a imagem viva enquanto a frase termina.
- Sensação do movimento: "chegou e parou" com assentamento firme (ease-out forte em 3 imagens, 55 → 28 → 17 px) e depois respiração lenta (zoom que perde velocidade, +3,9 %/s → +2,2 %/s); a cadência de 12 imagens/s dá o leve "tranco" de animação feita à mão.

## FORMA (fixa: reproduzir igual)
- Igual à estação de V01-A20/A22 (conferido: foto ≈ 88 % da largura com borda de papel acima da régua, chegada por chicote). Só uma imagem nesta estação.
- Design (med.py, região acima da régua): assentada f1546 x44–677, y222–722 = 634x501 px (88,1 % · 39,1 %), centro (49,9 %, 36,8 %); foto aérea P&B do lugar. Aproxima/cresce devagar (alinhado ao reestudo): f1594 x26–698, y212–741 = 673x530 (+6 % em 2 s). (medido)
- Movimento: chegada por chicote (V01-A23): borda esquerda f1540 x144 → f1542 x89 → f1544 x61 → f1546 assentada, 6 q (remedido, f1540–f1546); deriva lenta de aproximação ≈ 3 %/s; saída por corte seco para o A-roll em f1597 (a régua some junto). Cadência 12 imagens/s. (medido)
- Ritmo: 2375 ms (remedido); parada (só deriva) de f1546 a f1596 = 2083 ms. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- Textura (reestudo 20/11):
  - Fundo (mesa): liso com manchas suaves de nuvem. f1570 região 20,960,680,300: cor #131112, luma 17,1, grão 0,44 níveis, manchas 0,46, ac1 +0,52 (sem grão de 1 px), grão cinza (B/G/R 0,44/0,45/0,50). PARADO: diferença entre quadros 0,00–0,09 em toda a cena (o "VIVA" da ferramenta é ruído de compressão, grão abaixo de 0,5 nível). No detalhe com realce: nuvens largas e blocos de compressão de 8 px com leve tinta vermelha; nenhuma fibra, nenhum pontilhado.
  - Foto: papel fotográfico P&B neutro. f1570 região do céu 120,240,480,70: #b8b5b8, grão 3,32 níveis, manchas 2,69, ac1 +0,49 (grão de ≈ 2 px), grão por canal 3,33/3,33/3,33 (cinza puro, sem tinta sépia). Grão VIVO nos claros (medido, teste novo: f1570×f1572 e f1570×f1574 alinhados pela afim da foto, pixels lisos: claros resíduo/σ 1,23 e 1,06, correlação +0,36 e +0,41; escuros 0,82 e 0,40, correlação +0,70 e +0,92; par idêntico f1570×f1571: 0,01): o céu e as áreas claras da foto ganham grão novo a cada imagem, as massas escuras andam rígidas com a foto (corrigido na conferência: era "o grão é da própria foto e anda com ela").
  - Borda de papel: off-white quente, mais clara embaixo (#e7e2d8, ≈ 7–8 px) que nos lados (#ccc7bf, 5–6 px); no detalhe, fibra fina mosqueada e cantos retos (sem arredondar).
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: o fundo é mais claro atrás da foto e escurece para cima e para baixo: luma do fundo f1570 (mediana por faixa) 22–24 no topo, 32–36 em y320–640, 28–32 em y640–800, 18–20 em y960–1120, 14,5–15,5 no rodapé; os lados ficam 1–4 níveis abaixo do centro. É um foco de luz largo centrado em ≈ (50 %, 35 %), não uma vinheta de canto.
  - Vinheta da imagem: nenhuma (borda na região da foto: a luma SOBE para a borda, 68 → 117, por conteúdo; nitidez estável 88–122 %).
  - Borda borrada: nenhuma (medido em f1570).
  - Sombra da foto (medido, f1570, perfil alinhado na borda real, terço central de cada lado): embaixo −54 % no contato (luma 16 contra 34) e volta ao fundo em 19 px; à esquerda −20 % e à direita −23 % no contato, volta em 13–15 px; em cima −22 % só no 1º px, volta em 8 px. Leitura: sombra CAÍDA para baixo (longa e forte embaixo, média dos lados, quase nada em cima) (corrigido na conferência: era "deslocada ≈ 3–4 px para baixo, desfoque ≈ 15 px, força ≈ 30 %"). Sem fio escuro: o papel cai para a sombra em 2 px de antisserrilhado.
  - Desfoque de movimento: sim, só na chegada: f1542 (meio do chicote) mostra arrasto horizontal leve (≈ 4–8 px) nas bordas dos objetos da foto; some em f1546.
  - Profundidade: nenhuma camada desfocada. Grão global: nenhum aplicado no quadro inteiro (a mesa é parada); o grão vivo mora nos claros da foto (ver Textura) (corrigido na conferência: era só "nenhum"). Aberração de cor: +0,50 px (f1570, região da foto; no limite da subamostragem de cor do vídeo, não é efeito). Brilho/halo: nenhum. Degradê: só o do fundo.
- Câmera (reestudo 20/11): a câmera não anda; só a FOTO aproxima sobre o próprio centro. Foto: f1546 → f1560 escala ×1,0228 (+3,9 %/s), centro (+0,05, +0,10 px/q), giro 0,00°; f1580 → f1594 ×1,0125 (+2,2 %/s), giro +0,01° → desacelera. Fim da cena (medido, f1582 → f1594, região 0,0,720,830, sem a faixa da legenda): ×1,0108 (+2,2 %/s), centro (+0,01, +0,02 px/q): continua no ritmo freado até o corte, sem recuo. Fundo e régua parados (diferença ≤ 0,1 por quadro depois de f1548). Paralaxe: sim, de camada (foto se aproxima, régua e mesa paradas).
- Cadência (reestudo 20/11): foto a 12 imagens/s na chegada e na deriva (perfil da região da foto f1537–f1562: 42,6 / 0,02 / 25,9 / 0,02 / 24,2 / 0,01 / 22,0 / 0,02 / 17,1 / 0,35 / 7,1 / 0,02 / 7,0 …, ≈ 0 nos quadros pares); a régua troca o ano aceso também em passos de 2 quadros (f1538–f1546); fundo parado.
- Legenda nesta cena (reestudo 20/11): 3 blocos: o 1º (2 palavras, a data; f1531–f1544) atravessa a chegada (começa no chicote, 9 quadros antes da foto entrar); o 2º (6 palavras, f1545–f1578, o bloco mais longo do vídeo) entra 1 quadro antes da foto assentar; o 3º (2 palavras, o lugar citado; f1579–f1596) termina junto do corte seco para o rosto (f1597). Texto #e8dd51–#eadf55, caixa do texto 194–308 x 30 px, centro 68,2 %. Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px de altura (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %, estimativa grosseira sobre fundo escuro). Atrás da tarja: só a mesa (a foto termina em y733, a régua em y811). Outro texto junto: os anos da régua (V01-A25), 50 px acima da tarja. Nenhum sumiço.
- Entrada do texto (reestudo 20/11): nenhum texto novo entra nesta pasta; o ano da estação já acende durante o chicote (f1538–f1546, ver V01-A25 e V01-A23).

## CONSTRUÇÃO
1. fundo: retângulo 720x1280 #131112 com foco de luz largo (elipse centrada em 50 % × 35 %, luma 34 no centro → 22 no topo e 15 no rodapé; lados 1–4 níveis mais escuros); liso, sem grão animado; parado.
2. sombra da foto: retângulo do tamanho da foto com borda, preto, caída para baixo: embaixo escurece 54 % no contato e some em 19 px; dos lados 20–23 % e some em 13–15 px; em cima só 1–2 px (corrigido na conferência: era preto 30 %, deslocado 3–4 px, desfoque 15 px). Anda e escala junto com a foto.
3. foto de estação: imagem P&B neutra (dessaturar 100 %, sem tinta), horizontal ≈ 4:3, com borda de papel off-white (#e7e2d8 embaixo, #ccc7bf nos lados; 7–8 px embaixo, 5–6 px nos lados e em cima), cantos retos, sem giro; assentada em x44–677, y222–722 (88,1 % × 39,1 %, centro 49,9 % × 36,8 %). Grão próprio da foto ≈ 3 níveis + grão VIVO nos claros: ruído cinza de 1–2 px, ≈ 3 níveis, sorteado de novo a cada imagem (12/s) só onde a foto é clara (luma > 150); nas sombras da foto o grão anda rígido com ela (corrigido na conferência: era só o grão parado da foto). Chega pela direita no fim do chicote: 0 ms borda esq. em x144 → 83 ms x89 → 167 ms x61 → 250 ms x44 (ease-out forte, borrão horizontal leve nas 2 primeiras imagens); depois escala 100 → 106 % sobre o próprio centro até 2375 ms, com ease-out (≈ 3,9 %/s no começo, 2,2 %/s no fim). Tudo em passos de 2 quadros (12 imagens/s).
4. régua de anos (V01-A25): fixa em y771–811, entre a foto e a legenda; o ano da estação já aceso.
5. legenda: tarja preta pura a 74 %, 46 px de altura, texto amarelo #eade53, centro em 68 % da altura; troca seca por bloco (ver V01-L01).
- Linha do tempo (ms a partir da 1ª imagem da foto, f1540 = 64167 ms): −375 ms 1º bloco de legenda (a data) já na tela (chicote começou) · 0 foto entra pela direita · 208 ms troca de legenda · 250 ms foto assenta · 250–2375 ms aproximação lenta · 1625 ms último bloco de legenda (o lugar) · 2375 ms corte seco para o rosto (régua some junto).
- Parâmetros que dependem do conteúdo: proporção da foto (horizontal aqui); o enquadramento (plano aberto do lugar); o ano aceso.
- O que NÃO fazer: congelar o grão dos claros da foto (ele troca a cada imagem), fazer a sombra simétrica em volta (ela cai para baixo, quase nada em cima), arredondar os cantos, pôr vinheta ou moldura escura na foto, deixar a foto parada (sem a aproximação ela morre), animar a 24 imagens/s com curva suave (perde o tranco), mover o fundo junto com a foto, girar a foto (nesta estação ela entra reta).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o lugar citado na data": foto real, plano aéreo/aberto.
- Nesta referência as lacunas foram preenchidas com: vista aérea P&B do laboratório de Berkeley.
- Receita de tratamento de cada imagem: foto de época P&B, plano aberto, horizontal, borda de papel de 5–8 px (7–8 embaixo, 5–6 nos lados) (alinhado ao reestudo), ≈ 88 % da largura, acima da régua.
- Regra de escolha: data + lugar → foto literal do lugar na época, de cima.
- Teste de generalização: (1) Claude Code: "em 2025, ele estava em São Francisco" → foto aérea de SF. (2) café: "em 1900, a fábrica ficava em Milão" → foto aérea antiga de Milão.
- Receita de tratamento (reestudo 20/11): foto de arquivo P&B neutra (grão ≈ 3 níveis de 2 px, sem tinta), plano aberto/aéreo do lugar, céu claro em cima e massa escura embaixo (contraste natural da foto, sem curva extra), sem vinheta, borda de papel off-white de 5–8 px com cantos retos e sombra caída para baixo (embaixo −54 % em 19 px, lados 13–15 px, quase nada em cima) (alinhado ao reestudo).

- Confiança: caixas e tempos medido.
