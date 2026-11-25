# V01-A04 · punch-in animado dentro da cena de recorte
- Categoria: P11 · Viagem de câmera entre peças (provisória do analista: (provisória) zoom de câmera animado (punch-in suave) dentro de uma cena de tela cheia)
- Fonte: V01 quadros f119–f153 (4,96–6,38 s; 35 quadros ≈ 1458 ms) · 24 fps · acontece dentro de V01-A03
- Fala: "(pours inside.) Down your neck, up your"
- Tipo de fala: lista (os pontos do corpo por onde a água entra)
- Gatilho: começa em f119 = 4958 ms, −422 ms antes da palavra nº 17 "Down" (5380 ms) (remedido, f119: 1ª imagem nitidamente acima da deriva, linha do disco 607 → 615 px; o arranque lento já se insinua em f115–f117): o zoom começa no fim da palavra "inside." e chega ao ápice da velocidade em "neck" (f139–f141).
- Quadro-chave: f151
- Camadas ativas: cena de tela cheia | legenda | grafismo animado
- Leitura dos strips: strip.jpg = quadros f117 a f154, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 38 células; cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-meio-punch-in.jpg = quadro f143, região x0 y200 330x330 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala vira lista de lugares do corpo ("pescoço, mangas"); em vez de cortar, o editor aproxima a câmera do lugar falado e prepara a lupa que vem a seguir.
- Por que este design: nenhum elemento novo; só muda o enquadramento, para o objeto ganhar a tela (de ≈ 60 % para ≈ 80 % da altura) e o disco sair pela esquerda.
- Por que estas cores: as mesmas da cena (teal sobre navy, creme, mesa escura); nada se acrescenta.
- Por que estes efeitos: nenhum; o movimento é limpo, sem borrão, para não competir com a água que continua enchendo.
- Por que este movimento: em duas fases (primeiro aproxima, depois desliza), ease-in-out, como um cinegrafista que dá zoom e depois corrige o quadro.
- Sensação do movimento: "chegar perto para ver" sem pressa; produzida pelo zoom de +21 %/s na 1ª metade (f119–f135) seguido de deslize de ≈ 6,7 px/q para cima e para a esquerda na 2ª (f135–f151), pico de velocidade no meio, sem borrão, em passos de 12/s.

## FORMA (fixa: reproduzir igual)
- Design: não cria elemento novo; aproxima as peças da cena (disco, recorte e agente juntos; o fundo NÃO aproxima, ver Câmera do reestudo) e desloca o enquadramento para a esquerda e para baixo, de modo que o objeto passa a ocupar quase toda a altura e o disco sai pela esquerda. Centro do disco: x 50 % (f121) → ≈ 42 % (f151). (medido com disco.py, linha mais larga; o disco sai do quadro à esquerda a partir de f135)
  - Escala: linha mais larga do disco 588 px (f91) → 630 (f121) → 694 (f131, último quadro com as duas bordas visíveis) = +18 % só até a metade do movimento; escala final ×1,14, medida pela câmera do reestudo (o objeto passa de ≈ 60 % para ≈ 80 % da altura do quadro) (alinhado ao reestudo). Não deu para medir a escala final em px: o disco sai do quadro e o agente animado muda o recorte.
- Movimento:
  - Duração: f119 → f151 = 32 quadros (1333 ms), na grade de 12 imagens/s (16 imagens) (remedido, f119; antes f121 → f151 = 30 q). (medido)
  - Curva (diferença média por imagem no perfil, quadro cheio): f117 6,3 · f119 8,6 · f121 11,0 · f125 12,1 · f129 11,9 · f133 13,2 · f137 17,4 · f139 18,1 · f141 18,1 · f145 17,3 · f147 15,2 · f149 11,0 · f151 7,2 · f153 5,1 (o resto é o agente animando). Leitura: lenta-rápida-lenta (ease-in-out), pico no meio. (medido)
  - Depois do punch-in a cena fica no novo enquadramento até a saída (não volta). (observado)
- Ritmo: começa 1,5 s depois da entrada da cena (f83) e termina 0,6 s antes da lupa (f167). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11): as superfícies de V01-A03 (mesa parada com poça de luz; disco de papel com fibra que ferve; adesivo off-white; água em tinta chapada). No detalhe-meio-punch-in (f143) a borda do adesivo e o grão do disco ficam nítidos mesmo no meio do movimento; a frente da água que desce pelo tronco tem borda RETA e dura (frente de enchimento), enquanto as manchas das extremidades são esfumadas.
- Efeitos (reestudo 20/11): desfoque de movimento: nenhum (f143, no pico de velocidade, 6,7 px/q, tudo nítido no detalhe). Vinheta, brilho, profundidade, grão global: nenhum (os de V01-A03). Sombras: as das peças, que crescem com a escala (caídas para baixo: a do disco 22 px embaixo, 11–13 nos lados, nada em cima, medidas em V01-A03 f91; corrigido na conferência: a referência antiga era "contato 6–8 px em volta").
- Câmera (reestudo 20/11): só as peças se movem; o fundo fica: coluna x700 em f119 e f151 com o mesmo perfil de luz (17 / 28 / 35–36 em y400–480 / 28 / 14) → a mesa não aproxima (corrigido no reestudo, f119/f151: a nota dizia "aproxima a cena inteira (fundo, …)"). `camera` (0,0,720,830): f119→f135 ×1,1375 (+21,3 %/s), conjunto desce 6,5 px/q e vai 1,4 px/q para a esquerda (âncora no alto); f135→f151 ×1,003 (escala parada) e deslize (−86, −64) px = 5,4 px/q para a esquerda e 4,0 px/q para cima; f141→f143 −6,7 / −5,5 px/q (pico). Escala total f119→f151 ×1,14 (corrigido no reestudo: a nota estimava ≈ 1,3× a olho; somando o empurrão anterior f101→f117 ×1,037 dá ×1,18 desde o assentamento). Giro 0°.
- Cadência (reestudo 20/11): 12 imagens/s (16 imagens em 32 quadros; perfil antigo com diferença só nos ímpares), zoom e deslize nos mesmos passos.
- Legenda nesta cena (reestudo 20/11): 3 blocos atravessam o movimento sem relação com ele: o verbo (até f127), o 1º item da lista (f128–f146, entra no meio do zoom), o 2º item (f147–f165). Atrás da tarja: as pernas do objeto, agora maiores, com água teal e contorno off-white (censo/`legenda` f140: fora 162, tarja 47; opacidade real da tarja preta pura 74 %, medida direta da conferência; corrigido na conferência: era "≈ 71 %"): a tarja aparece cinza-escura translúcida. Nenhum outro texto (o "branco grande" é o contorno do adesivo).

## CONSTRUÇÃO
1. fundo: mesa fixa (não participa do zoom).
2. grupo de peças (disco + recorte + água + gotas, como um só grupo): a partir de 0 ms (f119), escala 1,00 → 1,1375 em 667 ms com âncora perto do topo do grupo (o grupo desce ≈ 104 px e vai 22 px à esquerda), curva ease-in; de 667 a 1333 ms, escala parada e translação de (−86, −64) px, curva ease-out; pico de velocidade em ≈ 917 ms (f141). Tudo em passos de 2 quadros.
3. a água continua enchendo durante o movimento (ver V01-A03).
- Linha do tempo (ms a partir de f119): 0 começa o zoom · 375 legenda do 1º item da lista · 667 fim do zoom, começa o deslize · 917 pico · 1167 legenda do 2º item · 1333 assenta no novo quadro (não volta).
- Parâmetros que dependem do conteúdo: o ponto de chegada (a região que a fala nomeia), quanto aproximar (até o objeto ocupar ≈ 80 % da altura), a direção do deslize.
- O que NÃO fazer: dar zoom no fundo junto (a mesa fica parada); usar borrão de movimento; voltar ao enquadramento anterior; movimento a 24/s ou numa curva única linear.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "região que a fala está descrevendo": o ponto do objeto para onde o zoom vai.
- Nesta referência as lacunas foram preenchidas com: o tronco e o lado esquerdo da roupa, onde a água está enchendo.
- Receita de tratamento de cada imagem: nenhuma imagem nova; é o mesmo plano aproximado. (reestudo 20/11) Ao aproximar ×1,14 nada é refeito em resolução maior: o grão do disco e a foto ampliam junto, sem borrão.
- Regra de escolha: o zoom vai na direção do detalhe que a fala passa a descrever ("down your neck, up your sleeves") e prepara o detalhe seguinte (lupa na pele, V01-A05).
- Teste de generalização: (1) Claude Code: depois de mostrar o notebook inteiro, aproxima devagar a área do terminal quando a fala diz "aqui no terminal…". (2) café: aproxima a xícara quando a fala passa de "a cafeteira" para "a espuma por cima".

- Confiança: duração, curva e deslocamento do centro medido; escala final medido pela câmera (×1,14), não pelo disco, que sai do quadro (alinhado ao reestudo).
