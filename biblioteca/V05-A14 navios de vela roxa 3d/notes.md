# V05-A14 · navios de vela roxa (3D) no mar
- Categoria: P24 · Cena 3D narrativa (provisória do analista: (provisória) plano 3D de tela cheia que herda o movimento da transição anterior)
- Fonte: V05 quadros f974–f1009 (40,62–42,10 s; 36 quadros ≈ 1502 ms) · 23,976 fps
- Fala: "made it into an empire."
- Tipo de fala: consequência ("virou um império")
- Gatilho: a imagem vira tela cheia em f974 (40 624 ms), 56 ms antes do início da palavra nº 147 "made" (40 680 ms). Não há corte: é o fim do zoom-portal de V05-A13 (a borda do círculo sai do quadro em ≈ f972). Conferido no `perfil` (dif cai de 21,7 em f973 para 14,6 em f974).
- Quadro-chave: f990
- Camadas ativas: b-roll 3D | legenda
- Leitura dos strips: strip.jpg = quadros f970 a f990, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 21 células. detalhe-vela-mastro.jpg = quadro f990, região x400 y360 200x200 px, ampliada 2× sem suavizar (pano da vela na cor-tema, cordas, mastro). detalhe-barcos-ao-fundo.jpg = quadro f990, região x0 y450 240x200 px, ampliada 2× sem suavizar (objetos ao fundo um pouco mais macios, névoa no horizonte).

## LEITURA DE EDITOR
- Por que esta cena aqui: "virou um império" pede escala e poder; a frota inteira com velas na cor-tema mostra a riqueza saindo do lugar recém-mostrado no mapa.
- Por que este design: o portal do mapa desemboca numa paisagem realista ampla; o objeto principal grande no centro e cópias menores atrás dão "muitos" em 1 imagem.
- Por que estas cores: é a 1ª cena em cor natural plena (mar azul, madeira, céu de névoa), e a cor-tema ocupa a maior área saturada (velas #723560 a #8b4474): a cor agora é poder, não raridade.
- Por que estes efeitos: névoa no céu e no horizonte (céu liso com degradê) e leve perda de detalhe ao fundo dão profundidade; quase sem vinheta (borda 83 %), porque é "ar livre", não estúdio.
- Por que este movimento: herda a velocidade do mergulho e freia em ease-out de ≈ 12 q, depois deriva lenta: o espectador "chega" na cena.
- Sensação do movimento: aterrissagem suave depois da queda; produzida pela escala que cai de +0,92 %/q (f976–f984) para +0,2 %/q (f995–f1007) com deslize lateral de ≈ 3 px/q.

## FORMA (fixa: reproduzir igual)
- Design: cena 3D realista de tela cheia: paisagem com plano de baixo azul #304d63 (f990, x360 y1000), céu cinza-azulado claro #92a7b5 (f990, x400 y330) com névoa, grupo de objetos-símbolo repetidos com a parte maior na COR-TEMA (#8b4474, f990, x470 y470, medido); a cor-tema ocupa x0–≈692 y389–605 em f990 (sangra pela esquerda; 96 % × 17 % do quadro); a parte na cor-tema do objeto principal sozinha x≈250–673 y389–605 (59 % × 17 %, centro ≈ 64 %, 39 %) (remedido, f990, máscara por matiz 290–350° e olhando o still; a caixa antiga perdia as partes na cor-tema dos objetos da esquerda e a do fundo à direita). Médias de área (remedição, f990): cor-tema #823c6b (20x20 em x460 y460), plano de baixo #375166 (60x40 em x330 y980), céu #92a7b5 (60x40 em x370 y310). Objeto principal no centro, outros menores atrás à esquerda (perspectiva de grupo, dá a escala). Horizonte em y ≈ 563–564, ≈ 44 % da altura (remedido: degrau de luminância na coluna x696–716 em f974 e still f990; antes "≈ 30 %"). Sem vinheta forte (diferente das cenas de estúdio).
- Movimento: aproximação que desacelera (herança do portal): dif 14,6 (f974) → 10,4 (f976) → 7,0 (f978) → 5,4 (f981) → 4,4 (f984) → 3,4 a 3,7 constante até o corte (medido). Ou seja, ease-out de ≈ 12 quadros e depois deriva lenta; paisagem animada (ondulação contínua).
- Saída: corte seco em f1010 (dif 84,5) para A15.
- Ritmo: 1,5 s de plano; nenhum texto além da legenda.
- Som: nenhum efeito detectado (lateral −120 dB).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Mar: família render realista de água. `textura` f990 região 100,950,200,150: #354e60, grão 4,7, manchas 11,0, ac1 +0,69 / ac2 +0,30 / ac4 +0,30, direção horizontal +0,98 × vertical +0,40 (ondulação horizontal); f990 × f992 anda com a câmera (correlação alinhada +0,96: a água mexe pouco em 2 q).
  - Céu: família liso (degradê de névoa). `textura` f990 região 200,100,300,200: #7a92a5, grão 0,44, manchas 1,3.
  - Vela na cor-tema: família tecido (pano liso com costuras). `textura` f990 região 330,420,150,110: #723560, grão 2,85, manchas 2,9, direção vertical +0,74 (costuras/dobras verticais). Detalhe: pano com painéis costurados e leve dobra, sem textura de trama.
  - Casco: família madeira realista. `textura` f990 região 250,650,120,50: #93724e, grão 21,4 (tábuas), direção horizontal +0,80 (veio e tábuas horizontais), grão levemente mais forte no vermelho (B/G/R 21,0/21,3/22,1).
  - Objetos ao fundo (0,480,200,120): grão 6,7 contra 21,4 do casco da frente: menos detalhe à distância (névoa + leve desfoque).
- Efeitos (reestudo 20/11): vinheta quase nenhuma (`borda` f990: luma 100 · 115 · 105 · 91 · 83 %; a nitidez cai para 13 % na borda porque céu e mar distante são lisos). Névoa atmosférica no horizonte (céu claro e liso, barcos distantes mais claros e macios). Sem grão de filme global (céu 0,44), sem aberração, sem halo.
- Câmera (reestudo 20/11): f976→f984 ×1,076 (+0,92 %/q, +24,7 %/s), centro sobe −3,1 px/q; f995→f1007 ×1,024 (+0,20 %/q), deslize −2,9 px/q e giro −0,04°/q. Ease-out confirmado (fim do portal de A13) e depois deriva lenta lateral.
- Cadência (reestudo 20/11): 24 imagens/s (dif da nota sem alternância).
- Legenda nesta cena (reestudo 20/11): o bloco com o nome do lugar (5 palavras) atravessa o portal (f952–f975) e troca 2 q depois de a cena encher a tela; 2 blocos na cena (2 palavras f976–f989; o resultado, 2 palavras, f990–f1009); o último termina no corte seco f1010 (a troca e o corte coincidem). Tarja mediana 71 % (f990: luma dentro 29 × fora 99); atrás: mar escuro azul. Sem outro texto.

## CONSTRUÇÃO
1. céu: degradê liso cinza-azulado (#92a7b5 no alto a mais claro no horizonte), névoa; horizonte em y ≈ 563 (44 % da altura).
2. mar: render de água azul (#354e60) com ondulação horizontal fina, animada devagar.
3. objetos: o objeto-símbolo principal no centro (casco de madeira realista, vela/peça grande na cor-tema), 3 a 4 cópias menores atrás à esquerda e uma à direita, mais claras e macias pela névoa; luz natural difusa, sombras suaves.
4. vinheta: quase nenhuma (borda ≈ 83 %).
5. câmera: entra em movimento vindo do portal (+0,9 %/q no início), ease-out em ≈ 12 q até ≈ +0,2 %/q, depois deriva lateral de ≈ 3 px/q até o corte.
6. legenda por cima.
- Linha do tempo (ms a partir de f974, quando a imagem enche a tela): 0 fim do portal (56 ms antes da palavra) · 0–500 freio · 83 troca a legenda · 500–1502 deriva lenta · 1502 corte seco para a cena seguinte.
- Parâmetros que dependem do conteúdo: o objeto-símbolo do "império/sucesso" e quantas cópias; qual parte dele leva a cor-tema.
- O que NÃO fazer: não dessaturar esta cena (é a cena de cor plena); não pôr vinheta forte; não parar a câmera de repente (o freio é longo); não cortar para entrar (a entrada é o fim do portal).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "imagem do poder/escala do lugar citado" (a consequência da frase).
- Nesta referência as lacunas foram preenchidas com: frota de navios com velas roxas ("made it into an empire").
- Receita de tratamento de cada imagem: render 3D realista (ou vídeo de banco) com o objeto-símbolo na cor do tema; luz natural difusa; paleta fria e dessaturada no fundo para o roxo saltar; câmera em aproximação lenta.
- Regra de escolha: consequência/metáfora visual. "Fez disso um império" → muitos navios com a cor do produto (a cor como bandeira do poder comercial).

- Receita de ILUSTRAÇÃO (reestudo 20/11): render 3D realista de paisagem aberta em cor natural, luz difusa de dia nublado, névoa atmosférica, o objeto-símbolo repetido em grupo com a cor-tema na maior superfície; revelado como destino do zoom-portal.
- Teste de generalização: reel sobre Claude Code: "e isso virou um império" → uma cidade de servidores realista em cor natural com as luzes na cor-tema, câmera chegando do portal. Reel sobre café: "o porto virou um império" → navios cargueiros antigos com sacas na cor-tema saindo de um porto com névoa.

- Confiança: tempos e dif medidos; cores e caixa medidas; horizonte observado.
