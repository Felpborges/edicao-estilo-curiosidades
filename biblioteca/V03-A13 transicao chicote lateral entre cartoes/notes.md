# V03-A13 · transição "chicote" lateral: a câmera corre para o cartão vizinho com desfoque de movimento
- Categoria: P11 · Viagem de câmera entre peças (provisória do analista: (provisória) transição animada: pan rápido com motion blur entre dois cartões lado a lado)
- Fonte: V03 quadros f1480–f1513 (61,73–63,11 s; 34 quadros ≈ 1418 ms) (conferido: o freio do pan segue em f1511–f1513 a −9,8 · −6,9 · −4,3 px/q e assenta em f1514, −1,5 px/q; antes: f1480–f1510, 31 quadros) · 23,976 fps
- Fala: "crossed to England with King"
- Tipo de fala: lugar (deslocamento no espaço: "crossed to England")
- Gatilho: começa em f1480 (61728 ms), 132 ms ANTES do início da palavra nº 210 "crossed" (61860 ms); o pico de velocidade (f1489–f1490) cai em "to" (nº 211, 62160 ms) e o assentamento em "King" (nº 214, 62860 ms).
- Quadro-chave: f1495 (meio do chicote: os dois cartões borrados lado a lado)
- Camadas ativas: transição | legenda
- Leitura dos strips: strip.jpg = f1478 a f1512, de 1 em 1, 8 colunas, linha a linha (a transição inteira, do quadro antes ao quadro depois). Reestudo: detalhe-desfoque-movimento.jpg = quadro f1493, região x240 y380 260x200 px, ampliada 2× sem suavizar · detalhe-borda-sombra-destino.jpg = quadro f1500, região x0 y960 320x120 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a frase descreve um deslocamento geográfico ("crossed to England"); em vez de cortar, o editor faz a câmera viajar de um retrato para o outro, no meio da frase, e assenta no novo personagem em "King".
- Por que este design: os dois cartões estão na mesma mesa, o de destino à direita e por cima da borda do de origem: a viagem é física, não um efeito de transição genérico.
- Por que estas cores: as das duas pinturas (dourado/branco → vermelho/arminho); nada acrescentado.
- Por que estes efeitos: desfoque de movimento horizontal do tamanho do deslocamento de um quadro (≈ 40 px no pico): é o que faz o chicote parecer uma câmera de verdade correndo.
- Por que este movimento: ease-in-out simétrico de 34 q, pico de 42 px/q no meio da palavra "to", com leve recuo (−12 a −28 %/s) que mostra a borda do cartão novo antes de enchê-lo.
- Sensação do movimento: viagem rápida e física, "atravessar o mar". Produzida pela aceleração 14 → 42 px/q e freio 42 → 4 px/q, pelo desfoque proporcional à velocidade e pela ausência de corte.

## FORMA (fixa: reproduzir igual)
- Design: dois cartões-pintura colocados lado a lado na mesma "mesa" escura, o de destino à DIREITA do de origem, com uma faixa do fundo escuro entre eles; o cartão de destino é maior que o quadro (quase tela cheia), levemente girado, borda clara (observado na folha). Reestudo (folha f1490–f1497): o cartão de destino fica POR CIMA da borda direita do de origem, sobrepostos, sem faixa de fundo entre eles nesse trecho (corrigido no reestudo; antes "com uma faixa do fundo escuro entre eles"); o fundo só aparece embaixo, a partir de f1502. A legenda continua fixa por cima.
- Movimento: pan horizontal da câmera para a direita (conteúdo anda para a ESQUERDA) com desfoque de movimento horizontal forte no meio. Velocidade medida por correlação de fase (dx por quadro): f1481 −14,2 · f1484 −26,7 · f1487 −38,7 · f1493 −42,3 · f1499 −34,3 · f1502 −30,9 · f1505 −23,8 · f1508 −15,2 px/quadro (nos quadros de blur máximo, f1490 e f1496, a medida falha) (medido). Curva lento-rápido-lento (ease-in-out), pico ≈ 42 px/q ≈ 5,8 % da largura por quadro; deslocamento total ≈ 900 px (inferido pela soma). Diferença por quadro 18 → 35,9 (f1489) → 19,6 (f1510) → 15,2 (f1514) → 1,7 (f1515, parado) (medido; conferido, f1515). Também uma pequena subida vertical no começo (dy −7,4 → 0) (medido). Não há corte: a cena de destino (V03-A14) continua do último quadro.
- Ritmo: 1,42 s (conferido; antes 1,29 s); liga duas imagens de dois personagens no meio da frase que descreve a passagem de um lugar a outro (a frase descreve deslocamento → a câmera se desloca).
- Som: nenhum whoosh detectado (áudio mono; envelope só com a voz; nenhum pico de agudos isolado em f1480–f1510) (medido, ferr audio).
- Textura (reestudo 20/11):
  - fundo (embaixo, a partir de f1502): liso #10110c, luma 16 (f1512).
  - borda do cartão de destino: papel pontilhado claro 7–8 px (luma 153–174 no centro do rastro). No detalhe f1493 o salpicado da borda continua nítido dentro da faixa borrada (observado): a textura do papel não aparece arrastada como a pintura.
  - pinturas: as reproduções de sempre (cor natural, craquelado), arrastadas na horizontal no meio do chicote (a textura do fundo da imagem vira riscos horizontais no detalhe). Grão vivo: NÃO DECIDIDO pelo teste de resíduo (pan de 15–42 px/q com desfoque: não há dois quadros alinháveis sem interpolação). O salpicado nítido dentro do rastro borrado (detalhe f1493) indica que a camada de grão do vídeo é aplicada DEPOIS do desfoque, por cima de tudo (observado).
- Efeitos (reestudo 20/11): desfoque de movimento horizontal: a borda de 7–8 px vira uma rampa de ≈ 22 px de subida + 6–8 px de topo + ≈ 20 px de descida em f1493 (≈ 42 px/q) e ≈ 22 + 8 + 20 px em f1500 (≈ 30 px/q) → comprimento do rastro ≈ deslocamento de 1 quadro (obturador de 360°); some no assentamento (f1512 nítido); vertical sem desfoque. Vinheta global nenhuma; sombra do cartão de destino sobre o de origem: não separável do conteúdo (baixa confiança); sombra do cartão de destino sobre o fundo, embaixo: 18 → 12–13 no 1º px (−33 %) e volta em ≈ 25–30 px (f1512 e f1514, x100–300) (medido); lados e topo fora do quadro ou sobre o outro cartão; brilho nenhum; profundidade nenhuma; grão global: não decidido pelo teste (ver Textura); o salpicado nítido sobre o rastro indica grão aplicado depois do desfoque (corrigido na conferência: era "nenhum"); aberração não medida.
- Câmera (reestudo 20/11): f1480→f1484 conteúdo (−16,7, −5,1) px/q, escala −28 %/s, giro +0,21°; meio f1487–f1499 −34 a −42 px/q (medido na 1ª passada); f1500→f1505 (−29,5, −1,3) px/q, −17,9 %/s, giro −0,15°; f1505→f1512 (−14,9, −0,4) px/q, −12,4 %/s, giro −0,24° (medido, região 0,0,720,820, poucos pontos por causa do desfoque: 134–191 de 600). Últimos quadros f1509→f1513: (−8,25, −0,11) px/q, −11,0 %/s, giro −0,05° (medido, região 0,60,720,770, sem a faixa da legenda, 418 de 600 pontos): o freio continua até o fim, como na nota. Durante a chegada o destino recua levemente e gira ≈ −0,4° (endireita).
- Cadência (reestudo 20/11): 24 imagens/s (todas as velocidades mudam a cada quadro; nenhum degrau).
- Legenda nesta cena (reestudo 20/11): o bloco de 2 palavras que abre a frase (f1471–f1483) vem da A12 e atravessa o começo do chicote; o verbo de deslocamento + destino (3 palavras) f1484–f1502; 2 palavras (preposição + título do novo personagem) f1503–f1512; o nome do novo personagem começa em f1513, no fim do freio (A14). A legenda fica fixa e nítida, sem desfoque, por cima do chicote. Cor #ece352–#ede251. Tarja preta a 73,5 % (73,0–75,1), altura 46 px (y847–892) (medido na conferência, 10 quadros do V03) (corrigido na conferência: era 53 % em f1493, sobre fundo borrado misto, a 69 % em f1505). Nenhum outro texto.
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)

## CONSTRUÇÃO
1. fundo: camada fixa lisa #10110c.
2. cartão de origem: o da cena anterior (continua do recuo da A12).
3. cartão de destino: pintura maior que o quadro, borda de papel 7–8 px, à direita do de origem e por cima da borda dele (sobreposição de ≈ 50–100 px), giro inicial ≈ +3° que endireita até ≈ +1° no fim.
3b. sombra do cartão de destino: embaixo, sobre o fundo, −33 % no contato e ≈ 25–30 px (sobre o cartão de origem não separável).
4. câmera (2 + 3 juntos): pan para a direita de ≈ 900 px em 34 q (ms 0–1418), ease-in-out simétrico: 14 → 27 → 39 → 42 px/q (pico em ms 375–540) → 34 → 31 → 24 → 15 → 10 → 7 → 4 → 1,5 px/q; junto, recuo leve (−28 %/s no começo, −12 %/s no fim), subida de 5 px/q no começo, e giro de ≈ −0,4° na chegada.
5. desfoque de movimento horizontal em cada quadro, com comprimento = deslocamento daquele quadro (≈ 15 px no começo, 40 px no pico); a legenda não é borrada.
5b. grão: a camada viva dos claros (24/s) vai por cima do quadro já borrado, nítida.
6. legenda: V03-L01 (tarja preta 73,5 %, 46 px), fixa por cima.
- Linha do tempo (ms a partir do início do chicote, f1480): 0 começa a correr (−132 ms do verbo de deslocamento) · 167 legenda troca para o verbo + destino · ≈ 375–540 pico (na palavra seguinte ao verbo) · 959 legenda troca para o título do novo personagem · 1376 legenda mostra o nome dele · 1418 assentado (A14 continua).
- Parâmetros que dependem do conteúdo: a direção (destino à direita, no sentido de leitura, salvo se o deslocamento da fala for para o outro lado), a distância entre os cartões (define os ≈ 900 px), a duração (≈ 1,4 s, presa à frase de deslocamento).
- O que NÃO fazer: usar corte ou dissolve; velocidade constante; desfoque fixo ou de 1 direção que não acompanha a velocidade; borrar a legenda; borrar o grão junto com a imagem (ele fica nítido por cima); whoosh (não há som); deixar os cartões separados por uma faixa de fundo.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: (1) imagem de origem (a que estava na tela); (2) imagem de destino (o novo lugar/personagem para onde a história "viaja").
- Nesta referência as lacunas foram preenchidas com: o retrato do rei francês → o retrato do rei inglês.
- Receita de tratamento de cada imagem: as duas como cartões grandes de cor natural, borda clara, lado a lado sobre o fundo escuro; destino à direita (sentido de leitura). Reestudo 20/11: destino por cima do de origem, sem tratamento extra de cor; o desfoque de movimento é aplicado na composição, não nas imagens.
- Teste de generalização: reel sobre Claude Code, "a moda passou do Vale do Silício para o Brasil" → chicote do print de uma empresa americana para o print de uma brasileira, com desfoque proporcional à velocidade · reel sobre café, "o café atravessou o mar até Veneza" → chicote da pintura de um porto árabe para a pintura de Veneza.
- Regra de escolha: frase de MOVIMENTO/DIFUSÃO no espaço ("crossed to England", "spread to", "moved to") → a câmera literalmente atravessa de um cartão para o outro. Em outros temas: reel sobre Claude Code, "a moda passou do Vale do Silício para o Brasil" → chicote de um print de São Francisco para um print brasileiro; reel sobre café, "o café atravessou o mar até Veneza" → chicote da pintura de um porto árabe para Veneza.

- Confiança: velocidades, perfil e quadros = medido; layout lado a lado e destino à direita = observado; deslocamento total = inferido.
