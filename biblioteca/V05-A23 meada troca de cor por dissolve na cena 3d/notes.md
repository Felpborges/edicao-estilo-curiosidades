# V05-A23 · meada de lã troca de cor por varredura (cena 3D) (alinhado ao reestudo)
- Categoria: P24 · Cena 3D narrativa (provisória do analista: (provisória) cena 3D low-poly, câmera fixa, um objeto muda de cor a cada cor dita (sequência de estados))
- Fonte: V05 quadros f1420–f1618 (59,23–67,51 s; 199 quadros ≈ 8300 ms) · 23,976 fps
- Fala: "Within minutes, it turns lemon yellow, then pale green, then deep ocean blue. Until finally, it locks into a shade so dark that it looks almost black."
- Tipo de fala: lista (sequência de estados: "fica X, depois Y, depois Z")
- Gatilho: entra por corte seco em f1420 (59 225 ms), 95 ms antes do início da palavra nº 207 "Within" (59 320 ms). Conferido: dif 50 em f1420 (`perfil`), legenda "Within minutes," no mesmo quadro.
- Quadro-chave: f1460
- Camadas ativas: b-roll 3D | legenda (sem grafismo)
- Leitura dos strips: strip.jpg = quadros f1436 a f1452, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 17 células (1ª troca). strip-saida.jpg = quadros f1504 a f1520, de 1 em 1, 8 colunas; 17 células (3ª troca). strip-geral.jpg = quadros f1420 a f1618 (amostrado), 8 colunas. detalhe-material.jpg = quadro f1460, região x110 y330 160x200 px, ampliada 2× sem suavizar (material de fios torcidos em cor, fibra visível). detalhe-dissolve-f1477.jpg = quadro f1477, região x110 y330 160x200 px, ampliada 2× sem suavizar (meio da 2ª troca: a cor nova avança da esquerda com frente irregular, a antiga ainda à direita). detalhe-troca-f1443.jpg e detalhe-troca-f1512.jpg = quadros f1443 e f1512, mesma região, ampliada 1× sem suavizar (meio da 1ª e da 3ª troca). detalhe-feixe-poeira-realce.jpg = quadro f1460, região x120 y40 220x220 px, ampliada 2× sem suavizar, contraste ×6 em volta da média (feixe de luz com borda macia e pontos claros de poeira).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala lista as cores pelas quais o material passa; a cena volta ao mundo do personagem e mostra cada estado na hora em que é dito, sem cortar: a transformação é contínua.
- Por que este design: personagem ao lado do material pendurado num suporte, câmera fixa: o material é o único elemento que muda, então o olho fica nele.
- Por que estas cores: cenário e personagem em sépia/marrom; o material é o único com cor e passa por amarelo, verde, azul-acinzentado e quase preto (#f7e177 → #a5b582 → #565065 → #4a2d2a): a sequência é o conteúdo.
- Por que estes efeitos: feixe de luz diagonal claro com partículas de poeira e vinheta (borda 31 %): luz de "laboratório antigo"; o feixe também justifica a mudança de cor (a fala liga a mudança ao ar e à luz).
- Por que este movimento: câmera parada e cada troca como uma onda de tinta que atravessa o material da esquerda para a direita em 3 a 10 q, um pouco antes de a cor ser dita.
- Sensação do movimento: química acontecendo diante dos olhos, calma e precisa; produzida pela câmera fixa (×0,997 em 7 s), varreduras curtas e o intervalo de 1,4 a 2,4 s entre estados; a última troca é a mais lenta (o "trava").

## FORMA (fixa: reproduzir igual)
- Design: mesmo mundo de A15 (personagem 3D low-poly, cenário em sépia/marrom, vinheta), com feixe de luz diagonal claro vindo do alto à esquerda (observado). O objeto que muda: o material que passa por estados, pendurado num suporte à esquerda do personagem, caixa x111–267 y312–694 (21,8 % × 29,9 % do quadro), centro (189, 503) = (26,3 %, 39,3 %) (remedido, f1460, máscara por matiz 40–70° com brilho ≥ 0,4, que separa o material do suporte; antes "x115–≈260 y294–855, 20 % × 44 %, centro 42 %": a caixa de cor pegava o suporte, que desce até y ≈ 925). Cores do material (média 20x20 px no centro, medido): f1430 estado inicial #ebb881 · f1460 estado 1 #f7e177 · f1495 estado 2 #a5b582 · f1540 estado 3 #565065 · f1600 estado 4, o final, quase preto #4a2d2a.
- Movimento: câmera FIXA (dif médio 1,35 em todo o plano, medido); o personagem gesticula. As trocas de cor são curtas, no lugar, sem flash nem escala, e acontecem como VARREDURA da esquerda para a direita com frente irregular (corrigido no reestudo, f1475–f1479 e f1510–f1513: 4 faixas verticais mudam em sequência; antes "dissolves"):

| passo | quadros | duração | de → para (medido) | gatilho |
|---|---|---|---|---|
| inicial → estado 1 | f1442–f1444 | 3 q ≈ 125 ms | #faf2ac → #f8e284 → #f6dd74 | o nome do estado 1 (#211, 60 280 ms): f1442 = 60 147 ms, −133 ms |
| estado 1 → estado 2 | f1476–f1479 | 4 q ≈ 167 ms (remedido, cor média de 80x220 px no material quadro a quadro: #d4bb62 → #aca966 → #8d9b69 → #84966a; antes 2 q) | #efd676 → #abb780 | o nome do estado 2 (#214, 61 380 ms): f1476 = 61 564 ms, +184 ms (−156 ms da 2ª palavra do estado) |
| estado 2 → estado 3 | f1511–f1513 | 3 q ≈ 125 ms | #a0b07e → #5f6667 → #565064 | o nome do estado 3 (#219, 63 220 ms): f1511 = 63 022 ms, −198 ms |
| estado 3 → estado 4 (final) | f1569–f1578 | 10 q ≈ 417 ms (remedido: o vermelho sobe até f1578, #373347 → #3e2827; antes f1569–f1576, 8 q) | #50495c → #4e4653 → #563e3f → #583c37 (mais lento) | o nome do estado final (#228, 65 680 ms): f1569 = 65 443 ms, −237 ms |

- Saída: corte seco em f1619 (dif 48) para a foto do material (A24).
- Ritmo: uma troca a cada 34 a 58 quadros (1,4 a 2,4 s), sempre 130 a 240 ms ANTES da palavra do estado (o estado muda um pouco antes de ser dito); a última troca é mais lenta (o "trava" final).
- Som: nenhum efeito detectado (lateral −120 dB de 59 a 67,5 s).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Material: família tecido/fio (meada de fios torcidos). `textura` f1460 região 140,400,90,180: #e4c462, grão 12,3, manchas 17,1, ac1 +0,64 / ac2 +0,06, direção vertical +0,72 × horizontal +0,55 (fios). Detalhe f1460: fios torcidos com sombra entre as voltas, sem contorno.
  - Feixe de luz: `textura` f1460 região 150,60,110,200: #8e7557, grão 3,0, manchas 9,0; f1460 × f1462 PARADO na tela (correlação +0,83 no lugar): o feixe é fixo. Detalhe realçado: borda macia (≈ 20–30 px de degradê) e pontos claros pequenos (poeira) dentro do feixe.
  - Cenário (praia/rochas em sépia desfocada, como A15) e chão escuro (`textura` 560,120,140,120: #140f0a, grão 0,78; cantos quase pretos).
  - Personagem e suporte de madeira: como A15 (roupa lisa em sépia, rosto pintado em cor).
- Efeitos (reestudo 20/11): vinheta (`borda` f1460: luma 100 · 114 · 75 · 47 · 31 %; o anel 2 é mais claro porque o feixe passa ali). Feixe de luz diagonal do alto à esquerda, borda macia, com partículas de poeira. Profundidade de campo no fundo (como A15). Sem grão de filme, sem aberração, sem halo no material.
  - Corrigido no reestudo: as trocas de cor NÃO são dissolves no lugar: são VARREDURAS da esquerda para a direita com frente irregular (como tinta se espalhando). Medido em 4 faixas verticais do material (x120–260, y400–620): 2ª troca f1475 #a08440 · #e5c161 · #f0d36c · #e5cf6f → f1477 #586745 · #a0a367 · #e3cb6c · #e5ce6f → f1479 #546445 · #83956a · #95a675 · #b2b276 (a faixa da esquerda muda 2 q antes da da direita); 3ª troca f1511 #414b3d · … · #9ba273 → f1513 #201e2c · #3d3c4e · #6b7467 · #959b70 (mesmo sentido). Detalhe f1477: frente verde irregular avançando sobre o amarelo.
- Câmera (reestudo 20/11): parada (medido: f1430→f1600 na região de baixo, escala ×0,997, −0,25 px/q, 19 de 351 pontos: cena escura, confiança média; a dif média 1,35 da nota confirma). Remedido na correção em 3 pares (0,0,720,790, 404 a 554 de 600 pontos): f1425→f1437 +0,7 %/s, f1515→f1527 +1,1 %/s, f1600→f1612 +1,0 %/s, deslize ≤ 0,1 px/q: parada (mesmo valor da nota).
- Cadência (reestudo 20/11): 24 imagens/s (as faixas mudam em quadros seguidos durante cada troca; personagem anima continuamente).
- Legenda nesta cena (reestudo 20/11): troca NO quadro do corte de entrada (f1420, o bloco que abre a frase); 10 blocos de 1 a 5 palavras; cada cor dita tem o seu bloco (estado 1 em f1446, estado 2 em f1466, estado 3 em f1491, o estado final sozinho em f1598); o último sai no corte (f1619). A cor do material e a legenda não são sincronizadas entre si: o estado 1 muda 4 q ANTES do bloco dele; o estado 2 muda 10 q DEPOIS do bloco dele; o estado 3, 20 q depois do bloco; ambos seguem a fala por caminhos próprios. Tarja 66 % (f1460: luma dentro 27 × fora 78).

## CONSTRUÇÃO
1. cenário: foto real do lugar em sépia, desfocada, como A15; chão quase preto embaixo.
2. feixe de luz: faixa diagonal clara do alto à esquerda (≈ +40 de luma), borda macia de 20–30 px, fixa na tela, com 10–20 pontos claros de 1–2 px (poeira) flutuando devagar dentro dele.
3. vinheta (borda ≈ 31 %).
4. personagem low-poly (como A15) à direita, com gestos pequenos contínuos; suporte de madeira à esquerda.
5. material pendurado no suporte (x 15–37 %, y 24–54 %), com textura de fio, cor inicial do estado 0.
6. trocas de estado (ms a partir do corte f1420): cada troca é uma varredura da esquerda para a direita com frente irregular (máscara de ruído), duração 3–4 q (125–167 ms), a última 10 q (417 ms): 917 ms → estado 1; 2336 ms → estado 2; 3795 ms → estado 3; 6214 ms → estado 4 (lento). Cada uma começa 130–240 ms antes de a cor ser dita.
7. câmera fixa; legenda por cima.
- Linha do tempo (ms a partir de f1420): 0 corte (95 ms antes da 1ª palavra) · 917 amarelo · 2336 verde · 3795 azul · 6214–6631 quase preto · 8300 corte seco para a foto (A24).
- Parâmetros que dependem do conteúdo: o material e a sequência de estados (cores, nº de trocas), as palavras de cada estado.
- O que NÃO fazer: não trocar a cor por dissolve global nem por corte (é varredura esq → dir com frente irregular); não mover a câmera; não colorir o cenário; não fazer todas as trocas com a mesma duração (a última é mais lenta).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "o material que passa por estados"; "cada estado dito na fala" (aqui, cores; em outro tema: tamanhos, fases, números).
- Nesta referência as lacunas foram preenchidas com: meada de lã que vira amarela, verde, azul e quase preta.
- Receita de tratamento de cada imagem: objeto 3D único destacado à esquerda do personagem, com luz própria (feixe), cores dos estados saturadas sobre um mundo sépia; troca por varredura da esquerda para a direita com frente irregular, de 3 a 4 quadros (o último estado, mais lento, 10 q) (alinhado ao reestudo).
- Regra de escolha: sequência literal de estados. Cada estado nomeado na fala ganha um corte de estado no mesmo objeto, sem mudar o plano.

- Receita de ILUSTRAÇÃO (reestudo 20/11): material 3D/foto realista com textura própria (fio), único elemento colorido; a mudança de estado é uma onda de cor com borda de ruído que atravessa o objeto; luz de feixe com poeira.
- Teste de generalização: reel sobre Claude Code: "o código passa por rascunho, teste, revisão e produção" → um bloco 3D de código pendurado ao lado do boneco muda de cor por varredura a cada etapa dita. Reel sobre café: "o grão fica verde, amarelo, canela e marrom" → um punhado de grãos ao lado do torrador muda de cor por varredura a cada palavra.

- Confiança: tempos e cores medidos no centro da meada (quadros com o braço passando, como f1440, descartados); caixa da meada parcialmente misturada com a pele.
