# V05-A03 · lupa 3D entra, passeia e sai
- Categoria: P23 · B-roll 3D com cor seletiva (provisória do analista: (provisória) objeto 3D em cor que atravessa uma cena dessaturada)
- Fonte: V05 quadros f174–f255 (7,26–10,64 s; 82 quadros ≈ 3420 ms) · 23,976 fps
- Fala: "No nation uses purple as a main stripe or background. Only a handful have"
- Tipo de fala: crença (negação: "ninguém usa")
- Gatilho: entra 57 ms depois do início da palavra nº 27 "No" (7200 ms; f174 = 7257 ms). Conferido: borda do aro aparece na borda direita em f174 (strip de entrada) e a legenda troca para "No nation" em f172.
- Quadro-chave: f210
- Camadas ativas: b-roll em sépia (continua A01/A02) | grafismo 3D (lupa) | legenda
- Leitura dos strips: strip.jpg = quadros f172 a f195, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 24 células. strip-saida.jpg = quadros f240 a f257, de 1 em 1, 8 colunas; 18 células. strip-geral.jpg = quadros f172 a f256, de 2 em 2, 8 colunas; 43 células. detalhe-aro.jpg = quadro f210, região x170 y330 150x150 px, ampliada 3× sem suavizar (aro, reflexo e lente sobre o fundo). detalhe-cabo.jpg = quadro f210, região x480 y600 160x200 px, ampliada 2× sem suavizar (madeira entalhada, luz e borda contra o fundo).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala diz que ninguém usa a cor; o instrumento de procurar varre a coleção e não acha nada, transformando a negação em ação que o espectador acompanha.
- Por que este design: um único objeto realista e grande (60 % da largura), em cor natural, sobre o mundo em sépia: o olho segue o objeto e confere sob a lente.
- Por que estas cores: o objeto é o único colorido (madeira avermelhada #6d4c3d no cabo) e é quente como a sépia, sem roubar o lugar do roxo, que ainda não apareceu.
- Por que estes efeitos: a lente amplia o que está embaixo (prova física do "procurar"); a luz de cima à esquerda no aro e nos entalhes faz o objeto parecer real dentro da mesma luz da mesa; a vinheta segue.
- Por que este movimento: trajetória curva, contínua, que acelera e freia como uma mão que procura e para em cima de um exemplar antes de ir embora.
- Sensação do movimento: busca manual, orgânica e sem pressa; produzida pela curva sem quadro parado, velocidade 4 → 8 → 4,8 → 13 (dif) e pela câmera do fundo que quase para (2,6 px/q) para não competir com o objeto.

## FORMA (fixa: reproduzir igual)
- Design: o objeto da ação, em COR natural do material (aqui cobre/marrom avermelhado) sobre o fundo em sépia; é o único elemento com cor da tela (o fundo segue com saturação 0,19). Tamanho: o objeto inteiro (parte principal + cabo) ocupa x179–611 y338–795 em f210 = 60 % da largura × 36 % da altura (medido com `caixa --cor #a0522d --tol 50`); parte principal ≈ 1/3 da largura (observado). O objeto age sobre a cena (o que está sob ele aparece maior em f178–f181, observado). Sem sombra projetada visível (corrigido no reestudo, f210: perfil e detalhe sem faixa escura junto à borda; antes "sombra suave do objeto sobre a coleção (observado)").
- Movimento: entra pela borda DIREITA (f174 só a borda da parte principal; f181 a parte principal toda dentro), desliza para a esquerda e para cima até ≈ x 35–65 %, y 30–45 % (f192–f214), depois desce em diagonal para a esquerda (f216–f236) e sai pelo canto inferior DIREITO (f246–f255; último quadro visível f255, só a borda). Velocidade (dif na metade direita, `perfil` f168–f262): sobe de 4,3 (f178) para 7,7–8,1 (f192–f212), cai para 4,8 (f232–f236, momento de "pausa" sobre um exemplar da coleção) e acelera na saída até 13,4 (f248). Trajetória curva e contínua, como mão que procura (observado). Não há quadro parado.
- Saída: sai pela borda, sem fade, 7 quadros da 1ª entrada no canto até sumir (f249–f255).
- Ritmo: entra 16 quadros (667 ms) depois do fim da transição de cor (A02); sai 1 quadro antes do início do push-in de A04 (f256).
- Som: nenhum efeito detectado (canal lateral em −120 dB de 7 a 11 s).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Objeto (madeira entalhada do cabo e do aro): família madeira (render realista). `textura` f210 região 500,640,60,90: cor #6d4c3d, grão 9,2, manchas 19,0, ac1 +0,59 / ac2 +0,07 / ac4 −0,14 (detalhe fino de entalhe e veio), grão B/G/R 9,2/9,2/9,6. Detalhe: veio de madeira visível no aro, folhas entalhadas em relevo no cabo, realces claros nas arestas viradas para cima e para a esquerda (luz-chave de cima à esquerda), sem contorno.
  - Lente: `textura` f210 região 240,420,140,110 (dentro da lente): #968678, grão 4,6, manchas 16,7; fora da lente na mesma altura (40,420,140,110): #584e46, luma 80. A lente é mais clara (luma 137 × 80) e amplia o fundo; no detalhe a área ampliada fica um pouco lavada (menos contraste), como vidro.
  - Fundo: os cartões em sépia de A02 (impressão lisa).
- Efeitos (reestudo 20/11): vinheta global de A01/A02 (parada). Lente: ampliação e clareamento local (+57 de luma). Sombra do objeto: nenhuma sombra projetada mensurável (perfil `sombra` f210 lado dir no cabo: a borda cai direto para o fundo, sem faixa escura; no detalhe não há halo); corrigido no reestudo: "sombra suave do objeto sobre a coleção (observado)" → "sem sombra projetada visível (f210)". Brilho: só os realces de material (nenhum halo). Desfoque de movimento: não visível (observado no strip). Aberração: não medida (borda do objeto em cor sobre sépia; o detalhe não mostra franja).
- Câmera (reestudo 20/11): o fundo quase para enquanto o objeto passeia: f196→f208 região do topo (sem objeto) deslize −2,6 px/q, escala ×0,996; no fim, f236→f248, recuo −0,385 %/q (×0,955 em 12 q) e descida +1,9 px/q, preparando o zoom de A04. O objeto anda sozinho (não preso à câmera). Remedido na correção em 3 pares (região do topo 0,0,720,300, sem o objeto): começo f176→f186 −0,1 %/s, deslize −3,3 px/q; meio f210→f222 −1,5 %/s, −2,5 px/q; fim f240→f252 −14,7 %/s (−0,66 %/q), desce +3,2 px/q (97 de 135 pontos): o recuo do fim acelera (era −0,39 %/q em f236→f248).
- Cadência (reestudo 20/11): 24 imagens/s no objeto e no fundo (sem dif ≈ 0 alternado no `perfil` da nota).
- Legenda nesta cena (reestudo 20/11): 5 blocos de 1 a 5 palavras (f174–f255); o 1º (3 palavras, f171–f187) entra 3 q antes do objeto. Tarja 68 %, o valor do vídeo (o censo dava ≈ 60–64 %, mediana 64 %, f174–f255) (alinhado ao reestudo), texto #f0e917. O cabo passa por trás da tarja (f210: tarja sobre o fundo; o objeto fica acima de y 795, a 26 px da tarja). Sem outro texto.

## CONSTRUÇÃO
1. fundo: plano de A01/A02 em sépia, deriva lenta (2,5–3,3 px/q) e no fim recuo que acelera de −0,4 a −0,7 %/q (corrigido na correção: era recuo de −0,4 %/q).
2. vinheta global parada (A01).
3. objeto 3D realista em cor natural, 60 % da largura × 36 % da altura com o cabo (corpo principal ≈ 1/3 da largura), luz-chave de cima à esquerda, sem sombra projetada, sem contorno; a área sob a lente é a camada 1 ampliada ≈ ×1,3 e clareada (luma +57) dentro de um círculo. A lente fica mais clara que o entorno mesmo sob a vinheta.
4. animação do objeto: entra pela borda direita em f174 (0 ms) e fica inteiro em f181 (292 ms); sobe e vai à esquerda até x 35–65 %, y 30–45 % (f192–f214, 750–1670 ms, velocidade constante); desce em diagonal à esquerda e quase para sobre um exemplar (f232–f236, 2420–2590 ms); acelera e sai pelo canto inferior direito (f246–f255, 3000–3380 ms). Curva contínua tipo spline, ease-in no fim.
5. legenda por cima.
- Linha do tempo (ms a partir da entrada, f174): 0 borda do objeto entra · 292 objeto inteiro · 750–1670 passeio alto · 2420–2590 pausa sobre um exemplar · 2590 começa o recuo da câmera de fundo · 3380 último quadro com objeto · 3420 começa o zoom de A04.
- Parâmetros que dependem do conteúdo: qual objeto (o instrumento da ação pedida); por onde ele para (um exemplar que NÃO tem o que se procura).
- O que NÃO fazer: não dessaturar o objeto; não dar sombra projetada (alinhado ao reestudo); não mover em linha reta nem com velocidade constante; não deixar o objeto parar de verdade; não usar ícone plano.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "objeto que simboliza a ação que a fala pede ao espectador" (procurar, contar, medir…).
- Nesta referência as lacunas foram preenchidas com: uma lupa antiga ("now try to find…" → procurar).
- Receita de tratamento de cada imagem: objeto 3D realista (ou foto recortada), material com cor natural mantida enquanto o fundo está dessaturado; tamanho ≈ 1/3 da largura; sem sombra projetada (alinhado ao reestudo); sem contorno; detalhe alto.
- Regra de escolha: metáfora da ação. A fala manda o espectador procurar → aparece o instrumento de procurar varrendo a cena, sem achar nada (o roxo não aparece sob a lente).

- Receita de ILUSTRAÇÃO (reestudo 20/11): objeto 3D realista (render ou foto recortada), material com textura real (veio, entalhe, metal), luz-chave de cima à esquerda igual à da cena, sem contorno nem sombra projetada; destaca-se do fundo só pela cor (é o único elemento saturado sobre a sépia) e pelo tamanho; revelado entrando pela borda.
- Teste de generalização: reel sobre Claude Code: "nenhum app faz isso" → um cursor de mouse 3D grande e realista passeia sobre a mesa de apps em sépia sem parar em nenhum. Reel sobre café: "nenhuma marca usa esse grão" → uma colher de café de metal realista passeia sobre os pacotes em sépia.

- Confiança: quadros de entrada/saída medidos nos strips; tamanho medido (inclui cabo); trajetória observada; "3D" inferido.
