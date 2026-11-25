# V05-A11 · card de foto com moldura branca sobe da borda de baixo
- Categoria: P09 · Cartão que cai por cima da cena (provisória do analista: (provisória) card de foto real com moldura branca que entra sobre a cena e escurece o fundo)
- Fonte: V05 quadros f779–f830 (32,49–34,62 s; 52 quadros ≈ 2169 ms) · 23,976 fps
- Fala: "(If you wore a) tunic in the heat, the color would fade away."
- Tipo de fala: consequência (prova do efeito: "a cor desbotava")
- Gatilho: o card aparece em f779 (32 491 ms), 71 ms depois do início da palavra nº 117 "tunic" (32 420 ms). Conferido: `perfil` sobe de 1,3 (f778) para 2,8 (f779) e 6,6 (f780); no strip, a borda branca surge no pé do quadro em f779–f780.
- Quadro-chave: f810
- Camadas ativas: b-roll 3D (A09) escurecido | grafismo (card de foto) | legenda
- Leitura dos strips: strip.jpg = quadros f777 a f800, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 24 células. strip-geral.jpg = quadros f777 a f831, de 2 em 2, 8 colunas; 28 células. detalhe-moldura-sombra.jpg = quadro f810, região x60 y740 240x100 px, ampliada 3× sem suavizar (canto inferior esquerdo do card: moldura branca, fio escuro e sombra por baixo, tarja da legenda logo abaixo). detalhe-meio-da-subida-f785.jpg = quadro f785, região x0 y500 720x300 px, ampliada 1× sem suavizar (meio da subida: o card nítido, sem borrão de movimento).

## LEITURA DE EDITOR
- Por que esta cena aqui: depois da encenação 3D do desbotamento, entra a PROVA real (foto de amostras lado a lado) na palavra do objeto: a reconstituição vira evidência.
- Por que este design: foto real dentro de moldura branca de papel fotográfico, grande (88 % da largura), por cima da cena que continua atrás escurecida: "olha a prova" sem tirar o espectador do lugar.
- Por que estas cores: moldura branca quase pura (#fcfcfc) e foto com fundo escuro: o card salta sobre a cena cinza escurecida; a cor-tema da foto conversa com o pano da cena.
- Por que estes efeitos: fio escuro de 1 px e sombra curta embaixo descolam o card do fundo como um papel apoiado; o fundo cai 28 % para o card virar o foco; a moldura tem um leve degradê de luz (mais escura à direita) que a integra à luz da cena.
- Por que este movimento: sobe do canto inferior crescendo, lento-rápido-lento, como uma foto que alguém levanta para a câmera; depois flutua para cima bem devagar.
- Sensação do movimento: "deixa eu te mostrar", suave e firme; produzida pela subida de 16 q com pico no meio (dif 35) e assentamento sem quique, e pela deriva de −0,67 px/q depois de parado.

## FORMA (fixa: reproduzir igual)
- Design: foto retangular horizontal-quadrada com MOLDURA BRANCA de ≈ 7 px (x88–95 à esquerda, y129–135 no topo, y788–795 embaixo; ≈ 1 % da largura) e um fio escuro de 1 px por fora só na borda de baixo (luma 17); à esquerda não há fio, o fundo (luma 73) encosta na moldura (alinhado ao reestudo; a 1ª passada dava fio também em x87 e y128, o topo não foi remedido), medido com `med.py row/col` em f810. Posição final: x88 até além da borda direita (o card sangra pela direita), y129–795 → 12,2 %–100 % da largura × 10,1–62,1 % da altura (medido). Cor da moldura #fefcfa (cor dominante de `geometria` f810). Dentro, a foto ocupa o card todo; os rótulos pequenos da foto fazem parte da imagem. Sem cantos arredondados, sem inclinação no fim. O fundo (cena 3D) escurece atrás do card: luminância média de x300 y1100 100x100 cai de 62,4 (f770, #3f403c) para 45,0 (f810, #2d2e2b), ≈ −28 % (medido).
- Movimento: entra pela borda de BAIXO, do lado direito, subindo e crescendo até a posição final; 16 quadros (f779–f794) ≈ 667 ms; curva lento-rápido-lento: dif 2,8 (f779) → 10,7 (f781) → 22,1 (f784) → 35,0 (pico f786) → 26,5 (f789) → 13,9 (f792) → 6,8 (f793) → 2,2 (f794) (medido). Nada de quique. Assentado de f794 até o corte, com leve deriva (dif 2,2 a 3,0).
- Saída: não sai sozinho; some no corte seco para o rosto em f831.
- Ritmo: design completo parado f794–f830 = 37 quadros ≈ 1543 ms. Entra 20 quadros depois de a câmera da cena parar (f759).
- Som: nenhum efeito detectado (lateral −120 dB de 32 a 35 s).
- Textura (reestudo 20/11):
  - Moldura: família papel fotográfico (branco liso, sem fibra): #fdfdfd (x91 y300), #fcfcfc (x300 y131), #fdf9f6 (x300 y791); à direita mais escura e esverdeada: #e1e3d4 (x600 y131), #e5e2d5 (x710 y131), #e8e4d5 (x600 y791) (medido em f810, 3x3 px). Degradê de luz de ≈ −11 % da esquerda para a direita.
  - Foto: família foto real (tecido fotografado sobre fundo escuro). `textura` f810 região 380,200,180,220: #a84885, grão 11,9 (trama do tecido da foto), manchas 4,3, ac1 +0,68, direção vertical +0,75 × horizontal +0,60, grão cinza. Sem vinheta própria (`borda` na região do card: o miolo é mais escuro só porque o fundo da foto é preto).
  - Fundo escurecido da cena (30,950,150,150): #232321, grão 1,25 (cena A09 atrás, mais escura); PARADO na tela (correlação +0,99 com f811 e +0,96 com f812, medido na correção).
- Efeitos (reestudo 20/11):
  - Sombra embaixo: `sombra` f810 x300 lado baixo: moldura 7 px (y789–795, luma 224–245) → fio escuro de 1 px (luma 17) → sombra macia de ≈ 10 px que clareia de 33 a 52 de luma → fundo; a tarja da legenda começa 14 px abaixo da moldura (y809).
  - Lado esquerdo: moldura 7 px (x86–92) sem fio escuro por fora (luma do fundo 73 até encostar): a sombra é só para baixo (luz de cima).
  - Escurecimento do fundo: −28 % (nota antiga), sem desfoque do fundo.
  - O card fica ACIMA da vinheta global (a moldura no canto x710 y131 tem luma 229; a vinheta ali levaria a < 35 %).
  - Desfoque de movimento: nenhum visível na subida (detalhe f785). Brilho: nenhum. Cantos: retos.
- Câmera (reestudo 20/11): cena de fundo parada (f796→f828, região y880–1180: ×1,003, 0 px). O card, depois de assentar, sobe sozinho −0,67 px/q (21 px em 32 q), sem escala (f796→f828 na região do card: ×1,000).
- Cadência (reestudo 20/11): 24 imagens/s (dif da subida muda em todos os quadros f779–f794).
- Legenda nesta cena (reestudo 20/11): segue ligada (3 blocos de 2, 3 e 2 palavras: f785–f795, f796–f807, f808–f830) e sai no corte para o rosto (f831). Com o fundo escurecido, a tarja fica quase invisível (f800: luma dentro 27 × fora 99 → 72 %, mas o "fora" inclui pernas claras). O card foi posto para terminar 14 px ACIMA da tarja: a legenda não é coberta.

## CONSTRUÇÃO
1. cena A09 por baixo (parada).
2. escurecimento: camada preta sobre a cena, 0 → ≈ 28 % de opacidade junto da subida do card (f779–f794, mesma curva), sem desfoque.
3. card: foto real (horizontal, quase quadrada) dentro de moldura branca de 7 px (≈ 1 % da largura), cantos retos; posição final x88 até sangrar a direita, y129–795 (10,1–62,1 % da altura; base 14 px acima do topo da tarja da legenda); por cima da vinheta global.
4. luz do card: degradê horizontal multiplicativo de 100 % (esquerda) a ≈ 89 % (direita), levemente esverdeado.
5. sombra do card: fio escuro de 1 px colado na borda inferior + sombra macia de ≈ 10 px para baixo (opacidade ≈ 40 % no início, some até o fim); sem sombra nas laterais.
6. animação: entra pela borda de baixo, lado direito, subindo e crescendo até a posição final em 16 q (667 ms), ease-in-out com pico no q 7 (≈ 290 ms); depois sobe −0,67 px/q até o corte.
7. legenda por cima, sem mudança.
- Linha do tempo (ms a partir da entrada, f779, 71 ms depois da palavra do objeto): 0 borda da moldura aparece no pé do quadro · 290 pico de velocidade · 667 assentado · 667–2169 parado com deriva para cima · 2169 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: a foto (prova real do que a fala diz); a proporção do card (segue a foto, mantendo base acima da legenda); a palavra que dispara.
- O que NÃO fazer: não arredondar cantos; não pôr sombra em volta toda (só embaixo); não deixar a vinheta da cena escurecer o card; não fazer quique; não cobrir a legenda; não usar moldura grossa (> 1 % da largura).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "foto real que prova o que a frase afirma" (a evidência do mundo real dentro da cena ilustrada).
- Nesta referência as lacunas foram preenchidas com: foto de 2 amostras de lã tingida lado a lado, "in the sun" (desbotada) × "in the shade" (roxa).
- Receita de tratamento de cada imagem: fotografia real (documental/experimento), recorte retangular, cores naturais, moldura branca fina de ≈ 1 % da largura + fio escuro e sombra macia de ≈ 10 px só embaixo (alinhado ao reestudo), sem inclinação; tamanho grande (≈ 88 % da largura, metade de cima da tela).
- Regra de escolha: prova. Depois da ilustração 3D de um fenômeno, entra a foto real do fenômeno (comparação antes × depois) no momento em que a fala descreve o efeito.

- Receita de tratamento de cada imagem (reestudo 20/11): foto real sem filtro de cor (mantém a cor natural), dentro de moldura branca de 7 px, com degradê de luz de −11 % para um lado; sem vinheta própria, sem grão adicionado.
- Teste de generalização: reel sobre Claude Code: "e o código quebrava toda vez" → card com print real de um log de erro, moldura branca, sobe do canto inferior sobre a cena 3D escurecida. Reel sobre café: "o grão perdia o aroma" → card com foto real de grãos frescos × velhos lado a lado.

- Confiança: geometria, cores, curva e tempos medidos; "sangra pela direita" medido (a moldura direita não aparece até x720); fio escuro medido por luminância (só embaixo, alinhado ao reestudo).
