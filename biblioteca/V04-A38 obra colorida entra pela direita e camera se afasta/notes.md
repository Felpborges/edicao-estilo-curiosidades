# V04-A38 · obra colorida em cartão entra pela direita grande e a câmera se afasta até ela ficar pequena no centro
- Categoria: P10 · Troca de cartão por empurrão ou cobertura (provisória do analista: (provisória) troca de cartão por cobertura lateral + afastamento)
- Fonte: V04 quadros f2890–f2958 (120,54–123,37 s; 69 quadros ≈ 2878 ms) · 23,976 fps
- Fala: "the same methods the cubists used to paint."
- Tipo de fala: comparação ("os mesmos métodos que os cubistas usavam para pintar")
- Gatilho: a obra começa a entrar em f2890 (120537 ms), 23 ms antes da palavra nº 410 "the" (120560 ms). Conferido no `perfil` (dif 6,5 → 14,8 em f2889→f2890).
- Quadro-chave: f2940
- Camadas ativas: legenda | cena de tela cheia | som (voz)
- Leitura dos strips: strip.jpg = quadros f2888 a f2928, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; strip-geral.jpg = quadros f2888 a f2960, de 2 em 2, 8 colunas, da esquerda para a direita, linha a linha. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-papel-aquarela.jpg = quadro f2940, região x420 y250 200x150 px, ampliada 3× sem suavizar (papel de aquarela com pintinhas, tinta granulada, traço de nanquim); detalhe-entrada-pico.jpg = quadro f2894, região x0 y100 720x900 px, ampliada 1× sem suavizar (pico do deslize: obra maior que o quadro, nítida).

## LEITURA DE EDITOR
- Por que esta cena aqui: a frase liga o método ao estilo de arte; a obra do estilo cobre a foto do resultado, e o recuo mostra a obra inteira como "o modelo".
- Por que este design: entra gigante (passa da altura do quadro) e a câmera recua até a obra caber a 88 % da largura, centro a 39 %, deixando a faixa da legenda livre.
- Por que estas cores: aquarela de verdes, ocres e laranjas sobre papel bege: a primeira imagem colorida e "de arte" depois de várias fotos sépia.
- Por que estes efeitos: vinheta da cena fortíssima (borda a 4 %); sem sombra; a textura do papel e da tinta fica visível porque a obra termina grande e parada (alinhado ao reestudo).
- Por que este movimento: deslize rápido (pico no 5º quadro) e, sem pausa, um recuo que acelera até −44 %/s e freia em ≈ 31 quadros; depois só −2 %/s.
- Sensação do movimento: de "dar um passo para trás" diante de um quadro num museu; produz isso o recuo grande ease-in-out logo depois da chegada.

## FORMA (fixa: reproduzir igual)
- Design: pintura colorida (obra do método citado; verdes, ocres, laranjas) em papel/cartão com borda clara, horizontal; ao fim do afastamento, em f2930: x40 y242 635x511 = x 5,6 %, y 18,9 %, larg 88,2 %, alt 39,9 %, centro (49,7 %, 38,9 %), −0,7° (medido). Fundo quase preto com vinheta (medido).
- Movimento:
  - Entrada: desliza da direita, grande (já maior que o quadro), em ≈12 quadros f2890–f2901: dif 14,8 → 21,5 → 28,1 → 31,7 → 32,8 (pico f2894) → 29,9 → 28,8 → 27,1 → 24,3 → 20,6 → 16,2 → 9,9 (f2901) (medido).
  - Afastamento (zoom-out) logo em seguida, f2902–f2926: dif 9,4 → 10,3 → 11,8 → 12,4 → 13,3 (f2909) → 13,2 → 12,5 → 11,8 → 11,5 → 10,8 → 10,3 → 9,5 → 8,9 → 8,1 → 7,1 → 6,2 (f2926) → 5,2 → 4,2 → 3,4 → 2,7 → 3,1 (f2932) → 1,8 (f2933) (remedido: a frenagem vai até f2932, 31 quadros): a altura do bloco cai de 66,0 % (f2903) para 39,9 % (f2930) = ×0,60 em 27 quadros (1,1 s) (medido).
  - Depois quase parado a partir de f2933, ainda se afastando devagar: ×0,977 de f2933 a f2957 (≈ −2,3 %/s, registro de pontos) (remedido).
  - Saída: troca seca f2958→f2959 (dif 31,6) para A39 (medido).
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| obra entra pela direita, grande | f2890 | 12 quadros (500 ms) | deslize | pico no 5º quadro | nº 410, o artigo antes da palavra do método (120560 ms) | −23 ms |
| câmera se afasta até a obra caber | f2902 | 31 quadros (≈1290 ms, até f2932) (remedido) | zoom-out | ease-in-out, pico f2909 | nº 412, a palavra do método (120920 ms) | f2902 = 121038 ms → +118 ms |

- Ritmo: obra inteira parada f2933–f2958 ≈ 1,08 s (26 quadros), com afastamento residual de −2,3 %/s (remedido, perfil quadro a quadro).
- Som: pausas f2943,3–f2947,4 (−69,3 dB) e f2956,0–f2959,6 (−68,3 dB), sem efeito (medido).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Fundo: liso (tela fixa), luma 34–40 logo fora do cartão no alto e embaixo, 6–12 do lado direito (f2940). PARADO: f2940×f2941 +0,96 (medido, x80 y960 560x200).
  - Papel da obra (aquarela): bege #cdad8e, luma 177, grão 2,8 níveis, manchas 3,7, ac1 +0,53 (pintinhas finas de 1–2 px), grão cinza; com a câmera quase parada, f2940×f2941 +0,75 (parada); f2948 já muda pelo recuo residual (f2940, x400 y280 90x60). No detalhe: papel com pintinhas escuras espalhadas, tinta verde granulada (deixa o papel aparecer), contornos de nanquim marrom-escuro de 2–3 px irregulares.
  - Borda do cartão: creme, ≈ 6–8 px, pico 198–200 (topo e base), 108 no lado direito (f2940).
- Efeitos (reestudo 20/11):
  - Vinheta da cena (f2940): luma 100/82/51/22/4 %, nitidez 100/68/33/14/2 %. No lado direito a obra cai de 104 para 81 em 22 px antes da borda (alinhado ao reestudo).
  - Luz da cena (correção 20/11, f2940, medido): centro da poça em (49 %, 38 %) (ajuste sobre o papel da obra, σ 0,09; a mesa dá (49 %, 40 %)); luma 144 no centro (40 px), a 100 px das bordas 84 % (esq) e 88 % (dir) do centro; mesa 10 em (360,1060) e 4 em (360,1180) (razão 2,6). A luz é desta cena, por cima de fundo e peças; os anéis acima valem só aqui (não é um multiplicador fixo do vídeo).
  - Sombra: nenhuma (topo: borda 200 → fundo 41 em 2 px; base: 200 → 34; direita: 108 → 12 e depois 12 → 6 = vinheta).
  - Desfoque de movimento: nenhum no pico da entrada (f2894).
  - Fio, brilho, aberração, profundidade, grão global: nenhum.
- Câmera (reestudo 20/11): recuo f2903→f2909 ×0,902 (−33,9 %/s), +1,6/−3,3 px/q; f2915→f2921 ×0,866 (−43,7 %/s), +1,7/−2,4 px/q; resíduo f2935→f2955 ×0,981 (−2,3 %/s), 0 px/q; giro 0. Nota: o recuo também sobe (conteúdo vai para cima) e para a direita ≈ 1,7 px/q.
- Câmera em 3 pares (correção 20/11, medido, `camera`; refeita com região, porque a conferência achou câmera "zero" falsa medindo o quadro inteiro; regiões x40 y200 660x600 e x59 y253 599x488: f2891→f2897 não mede (a obra entra, 5 pontos); f2900→f2906 −25,6 %/s, +0,4/−2,4 px/q; f2905→f2911 −38,5 %/s, +1,7/−3,6; meio f2921→f2927 −31,3 %/s, +1,0/−1,1; fim f2951→f2957 −1,2 %/s, 0 px/q. Fases: entrada da obra f2890–f2901 · recuo forte que sobe e vai para a direita f2902–f2932 · resíduo quase parado até o corte (não é zero).
- Cadência (reestudo 20/11): 24 imagens/s em entrada e recuo (perfis da nota antiga sem quadro parado).
- Legenda nesta cena (reestudo 20/11): amarela #ece81a, altura 27 px; enquanto a obra é grande (f2890–f2913) a tarja fica sobre ela (tarja preta a 59 % fixa no vídeo; medida direta aqui: 58–61 % em f2891, f2905 e f2910, fundo 106–155) (corrigido na conferência: era "opacidade até 85 % sobre área clara"); depois do recuo fica sobre o fundo escuro (luma 25–30, não medível). 5 blocos: o bloco de A37 · 3 · 1 (751 ms: a palavra-chave sozinha) · 2 · 1; o 1º bloco da frase seguinte começa no quadro do corte f2958 (1 quadro antes da cena nova).

## CONSTRUÇÃO
1. fundo: tela fixa marrom-escura lisa.
2. foto anterior (A37) coberta.
3. cartão da obra: aquarela sobre papel bege com pintinhas, borda creme 6–8 px, horizontal; tamanho final x40–675 × y242–753 em f2930 (88,2 % × 39,9 %, centro (49,7 %, 38,9 %)), giro −0,7°. Entra da direita já grande (alt ≈ 66 % do quadro): 0 → 500 ms (12 quadros), pico em 167 ms.
4. câmera sobre 3: 500 → 1790 ms recuo ×0,60 (alt 66 % → 40 %), ease-in-out com pico −44 %/s em ≈ 800 ms, subindo e indo para a direita ≈ 2–3 px/q; depois −2,3 %/s até o corte.
5. luz da cena por cima de tudo (fundo e peças; não é vinheta fixa do vídeo): poça centrada em (49 %, 38 %), luma 144 no centro, a 100 px das bordas 84 % e 88 % do centro, mesa 10 em (360,1060) e 4 em (360,1180); anéis medidos com `borda` 100/82/51/22/4 % (f2940) (corrigido na conferência: era "vinheta da cena 100/82/51/22/4 %", lida como vinheta fixa do vídeo) (alinhado ao reestudo).
6. legenda L01.
- Linha do tempo (ms a partir de f2890): 0 obra entra pela direita (−23 ms do artigo) · 167 pico · 167 legenda do 2º bloco · 500 assentada, recuo começa (+118 ms da palavra do método) · 1001 a palavra-chave · 1293 freio · 1752 4º bloco · 1790 recuo termina · 2502 último bloco · 2878 troca seca para A39.
- Parâmetros que dependem do conteúdo: o formato da obra (horizontal: termina com alt ≈ 40 %), o quanto ela entra maior (até o lado curto encher o quadro).
- O que NÃO fazer: entrar já no tamanho final; recuar linear; parar o recuo com estalo; pôr sombra ou moldura grossa. Pôr uma vinheta fixa igual em todas as cenas: a luz é desta cena, com centro e força próprios, por cima de fundo e peças (correção 20/11).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "obra/exemplo do método citado".
- Nesta referência as lacunas foram preenchidas com: pintura cubista colorida.
- Receita de tratamento de cada imagem: reprodução real da obra, cores originais vivas, cartão/papel com borda clara.
- Regra de escolha: "os mesmos métodos que os cubistas usavam" → uma obra real do método, que entra grande (detalhe) e se afasta para ser vista inteira. Teste em 2 temas: Claude Code → print de um código bem estruturado de um projeto famoso, entra em detalhe e afasta; café → foto de uma pintura de latte art, entra em detalhe e afasta.

- Receita de tratamento (reestudo 20/11): reprodução fotográfica de obra em papel (aquarela/guache), cores originais sem saturar, papel com textura e pintinhas visíveis, borda creme fina (6–8 px), sem vinheta própria.
- Teste de generalização: Claude Code → um diagrama desenhado à mão do método de arquitetura entra grande e a câmera recua até ele caber; café → uma ilustração botânica antiga do cafeeiro entra grande e recua.

- Confiança: tudo medido, exceto o conteúdo (observado).
