# V04-A26 · afastamento com nuvens (2ª vez) + nuvens somem em fade + manchas se espalham pelo mapa inteiro
- Categoria: P13 · Afastamento que revela a quantidade (provisória do analista: (provisória) movimento de câmera de afastamento com recortes de profundidade (nuvens) + multiplicação)
- Fonte: V04 quadros f2061–f2172 (85,97–90,59 s; 112 quadros ≈ 4671 ms) · 23,976 fps
- Fala: "run right across its edges, your eye stops seeing one shape. It sees pieces."
- Tipo de fala: mecanismo (a consequência visível do mecanismo: "o olho para de ver uma forma, vê pedaços")
- Gatilho: o afastamento começa em f2061 (85961 ms), 79 ms antes da palavra nº 293 "run" (86040 ms). Conferido no `perfil` (dif 5,6 → 6,3 em f2060→f2061, subindo até 16,6 em f2086).
- Quadro-chave: f2170
- Camadas ativas: legenda | cena de tela cheia | grafismo (nuvens, manchas) | som (voz)
- Leitura dos strips: strip.jpg = quadros f2059 a f2106, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha (afastamento); strip-saida.jpg = quadros f2130 a f2172, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha (fade das nuvens e manchas se espalhando); strip-geral.jpg = quadros f2059 a f2174, de 3 em 3, 8 colunas, da esquerda para a direita, linha a linha. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-borda-cartao.jpg = quadro f2150, região x540 y150 160x160 px, ampliada 3× sem suavizar (canto superior direito do cartão, borda e fundo); detalhe-manchas-espalhadas.jpg = quadro f2170, região x60 y380 600x260 px, ampliada 1× sem suavizar (as formas espalhadas na faixa do objeto).

## LEITURA DE EDITOR
- Por que esta cena aqui: é a conclusão do mecanismo; depois de mostrar as formas em cima do objeto (A25), a fala diz o efeito no conjunto e a câmera recua para o espectador ver "pedaços" em vez de um objeto.
- Por que este design: o mesmo cartão de A24/A25 (continuidade sem corte); as nuvens recortadas dizem "visto do alto, de longe" sem texto; as formas se multiplicam na mesma faixa do objeto para o olho perder o contorno.
- Por que estas cores: o cartão é a foto aérea verde-oliva de arquivo e as formas usam as 3 cores de A25 (ferrugem, ocre, oliva) que pertencem à paleta da própria foto; por isso elas "somem" no chão, que é exatamente o argumento.
- Por que estes efeitos: a vinheta da cena escurece a borda do cartão e o fundo, o que concentra o olho no miolo onde as formas se espalham; nuvens brancas são o único branco da cena e marcam a altitude (alinhado ao reestudo).
- Por que este movimento: afastamento acelera-cruzeiro-freia (≈ −28 a −35 %/s no pico) = "subir de avião"; depois a câmera volta a se aproximar devagar (+7,6 %/s) enquanto as formas pipocam, para a cena não parar.
- Sensação do movimento: de decolagem e de distância (o chão encolhe e as nuvens passam por cima em paralaxe), seguida de um respiro que se reaproxima; o que produz é o recuo rápido com freio longo e os recortes de nuvem num plano mais perto da câmera.

## FORMA (fixa: reproduzir igual)
- Design: igual a V04-A24 (cartão com borda que encolhe, elementos de distância recortados no alto e na base). Medido aqui: em f2112 o cartão = x0–641 × y203–1152 = larg 89 %, alt ≈ 74 %, centro (44,5 %, 53,1 %), −1,3° (remedido, f2112: topo em x360/x600, base em x100/x600; a caixa antiga pegava os elementos de distância da base); em f2140 y215–1131, alt 71,6 %, −1,2° (remedido, f2140); em f2170 alt 78,1 %, centro (46,8 %, 52,1 %), −1,1° (medido). Elementos do mecanismo: as mesmas formas nas 3 cores de A25, agora espalhadas por boa parte da imagem de fundo (observado).
- Movimento:
  - Afastamento f2061–f2110: dif 6,3 (f2061) → 8,1 (f2063) → 10,5 (f2065) → 12,5 (f2068) → 13,1 (f2072) → 12,6 (f2076) → 13,8 (f2081) → 16,1 (f2083) → 16,6 (pico f2086) → 14,9 (f2090) → 12,5 (f2094) → 11,3 (f2098) → 13,7 (f2101) → 12,6 (f2106) → 9,8 (f2109) → 7,5 (f2112) → 6,2 (f2115) (medido): acelera ≈8 quadros, cruzeiro, freia ≈10 quadros. Sem giro de câmera: o cartão fica em ≈ −1,2° o tempo todo (remedido: registro de pontos f2061→f2085→f2112→f2140→f2170 gira menos de 0,2° em cada trecho).
  - Elementos de distância: entram em paralaxe junto com o afastamento (≈f2088 no alto, ≈f2100 na base) e somem em fade f2132–f2142 (≈11 quadros ≈ 460 ms) (remedido no perfil das faixas do alto e da base).
  - As formas se espalham: novas formas pipocam por toda a imagem de fundo f2144–f2172, e a câmera volta a se aproximar devagar (alt 71,6 % em f2140 → 77,3 % em f2170, ×1,115 no registro de pontos) (remedido).
  - Saída: corte seco f2172→f2173 (dif 72,4) para o A-roll (medido).
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| afastamento + elementos de distância | f2061 | ≈50 quadros (≈2085 ms) | movimento de câmera + paralaxe | acelera, cruzeiro, freia | nº 293, o verbo que abre a frase (86040 ms) | −79 ms |
| elementos de distância somem | ≈f2132 | ≈11 quadros (460 ms) (remedido) | fade | linear (observado) | nº 303, a palavra que fecha a frase (88860 ms) | f2132 = 88906 ms → +46 ms |
| formas se espalham pela imagem de fundo | ≈f2144 | ≈28 quadros até o fim | pops sucessivos | — | nº 304, 1ª palavra da conclusão (89460 ms) / nº 305 | f2144 = 89422 ms → −38 ms |

- Ritmo: 4,7 s sempre em movimento; não há trecho parado: as formas seguem crescendo e a câmera seguindo até o corte f2172 (remedido, perfil e folha f2156–f2172).
- Som: pausas f2098,9–f2102,0 (−64,5 dB) e f2142,0–f2144,9 (−67,9 dB) sem efeito (medido).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Fundo atrás do cartão: liso (ruído fino de compressão), #25211b, luma 33, grão 0,45 níveis, manchas 1,62, ac1 +0,47 (horizontal +0,72 × vertical +0,22 = só bloco de compressão), grão cinza (B/G/R 0,49/0,45/0,46); não é mesa nem papel. Cor em 9 pontos de #1b1813 (alto) a #302b25 (perto do cartão): o fundo clareia em direção ao centro do quadro (f2150, x200 y60 300x110). PARADO na tela: correlação do grão no lugar +0,92 entre f2150 e f2151 (medido, x200 y60 300x110) (corrigido na conferência: era "com --q2 f2160 sai viva").
  - Foto do cartão (foto aérea de arquivo): grão de filme/impressão, #5f5637, grão 8,18 níveis, manchas 9,15, ac1 +0,69 (grão de 2 a 3 px, igual nas duas direções), grão cinza (8,19/8,18/8,19); anda com a câmera (f2150×f2156: correlação +0,71 depois de alinhar −0,6/+6,6 px) (f2150, x250 y950 250x150).
  - Borda do cartão: faixa creme-rosada de 8 a 10 px, lisa, sem fibra visível no detalhe; luma 201 no topo (y≈205), 149 na lateral direita, 97 na base (f2150): a MESMA tinta muda de luma com a posição, prova de que a vinheta é aplicada por cima de tudo. Entre a borda e a foto há uma linha irregular mais escura (o limite da foto impressa), sem fio desenhado.
- Efeitos (reestudo 20/11):
  - Vinheta da cena (quadro inteiro, f2150): luma 100 % → 87 % → 68 % → 25 % → 10 % do centro para a borda; nitidez 100 → 113 → 62 → 24 → 6 % (a nitidez cai junto com a luma, então é vinheta escura e não desfoque de borda). Na área do cartão (x90 y205 550x930): 100 → 86 → 80 → 73 → 67 % com nitidez 77 % na borda: vinheta forte, fora do cartão quase preto (alinhado ao reestudo).
  - O fundo não é preto uniforme: 43 de luma logo acima do cartão (y≈170) contra 9 logo abaixo (y≈1150): o centro da vinheta fica acima do meio do quadro.
  - Luz da cena (correção 20/11, medido): em f2067 (cartão grande, começo do afastamento) o centro da poça fica em (48 %, 31 %) (ajuste sobre o cartão, σ 0,19, e na mesa, σ 0,16: concordam); luma 133 no centro, a 100 px das bordas 66 % (esq) e 56 % (dir) do centro. Em f2150 o ajuste fica instável (σ 0,38: centro entre x 43 e 54 %, y ≈ 41 %); mesa 7 em (360,1180) (em (360,1060) ainda é o cartão, 92). A luz é desta cena, por cima de fundo, cartão e nuvens; os anéis acima valem só aqui (não é um multiplicador fixo do vídeo).
  - Sombra do cartão: nenhuma sombra escura medível. Perfis (f2150): topo = borda (pico 201) e fundo plano 42–43; base = borda (97) e fundo plano 9; lado direito = borda (149) e fundo que desce suave de 22 a 15 em 30 px (é a própria vinheta, não sombra).
  - Fio escuro ou claro na borda: nenhum fio desenhado; só a borda clara.
  - Aberração de cor: nenhuma (0,00 px, f2150 na borda direita).
  - Desfoque de movimento: nenhum nas formas (pops); nuvens recortadas ficam nítidas mesmo no pico do afastamento (observado na strip-geral).
  - Grão global: não há grão sobre o fundo liso (0,45 níveis): o grão vem só da foto.
- Câmera (reestudo 20/11): afastamento f2061→f2069 escala ×0,897 (−27,8 %/s, deriva −0,5/−1,3 px/q, giro −0,3°); pico f2084→f2090 ×0,897 em 6 q (−35,2 %/s); freio f2112→f2124 ×0,960 (−7,7 %/s); reaproximação f2150→f2162 ×1,037 (+7,6 %/s, 0,1 px/q, giro 0) (região do cartão sem legenda). Paralaxe: as nuvens andam em direção oposta e mais rápido que o cartão (observado na strip-geral; não medido com camera porque somem em fade).
- Câmera em 3 pares (correção 20/11, medido, `camera` com região x12 y200 629x616: começo f2062→f2070 −30,6 %/s, −0,03/−1,2 px/q; meio f2112→f2120 −7,6 %/s, +0,6/0 px/q; fim f2163→f2171 +6,7 %/s, −0,2/0 px/q; giro ≤ 0,03°/q. Fases: afastamento forte até ≈ f2110 · freio de ≈ f2112 a ≈ f2150 · reaproximação de ≈ f2150 ao corte (confere a nota).
- Cadência (reestudo 20/11): 24 imagens/s em todas as camadas (perfil f2086–f2096: 24,9 → 13,3 sem nenhum quadro ≈ 0; f2150–f2160: 8,7–9,2 em todos os quadros, a câmera anda a cada quadro).
- Legenda nesta cena (reestudo 20/11): amarela #ece71c em 100 % dos 112 quadros, altura 33 px; tarja preta a 59 % fixa no vídeo (medida direta aqui: 57–60 % em f2091, f2096 e f2101, fundo 115–153) (corrigido na conferência: era "mediana 54 % (46–62 %)", leitura do censo); atrás dela o miolo médio da foto aérea (luma 90–132, mediana 105). 7 blocos de 1 · 3 · 1 · 2 · 3 · 2 · 2 palavras; o 6º junta o fim de uma frase e a 1ª palavra da conclusão. O 1º bloco (o verbo que abre a frase) começa 1 quadro antes (f2060), dentro de A25, porque não há corte. Nenhum sumiço, nenhum outro texto na tela.
- Correção (reestudo 20/11): as formas NÃO se espalham "por boa parte da imagem": em f2170 elas ocupam uma faixa horizontal x≈80–700 × y≈390–600 (30–47 % da altura), a faixa do objeto de A25 alongada para os dois lados (corrigido no reestudo, f2170, detalhe-manchas-espalhadas.jpg).

## CONSTRUÇÃO
1. fundo: retângulo liso #1b1813 no alto clareando a #302b25 perto do cartão, preto (#0e0d08 a #000) nas bordas; nenhuma textura.
2. cartão: foto aérea com borda creme de 8–10 px (cor de papel ≈ #e8ddd0 antes da vinheta), larg 89 % × alt 72–78 % do quadro, centro (44,5–46,8 %, 52–53 %), girado −1,2°; vem de A25 já na tela.
3. formas do mecanismo: chapadas nas 3 cores de A25 com contorno marrom-escuro de 1–2 px e furos internos; novas formas pipocam secas (1 quadro, sem escala) a partir de 3361 ms (f2144), uma ou duas a cada 2–4 quadros, até o corte, só na faixa y 30–47 %.
4. nuvens recortadas: 2 grupos brancos (alto-esquerda e base) num plano mais próximo da câmera; entram com o afastamento em 1125 ms (alto, f2088) e 1625 ms (base, f2100), andam mais rápido que o cartão (paralaxe) e somem em fade linear de 460 ms a partir de 2958 ms (f2132).
5. câmera (escala do conjunto 2 + 3; as nuvens em plano próprio): 0 → 2085 ms afastamento ×≈0,62 no total com curva acelera 8 q, cruzeiro, freia 10 q (pico −35 %/s em ≈1050 ms); 2085 → 3500 ms quase parada (−7,7 → 0 %/s); 3500 ms → corte reaproxima a +7,6 %/s linear; giro do cartão fixo em −1,2°.
6. luz da cena por cima de tudo (fundo, borda do cartão, foto e nuvens; não é vinheta fixa do vídeo): poça centrada em (48 %, 31 %) no começo (f2067) e em ≈ (48 %, 41 %) no fim do afastamento (f2150); luma 133 no centro, a 100 px das bordas 56–66 % do centro; anéis medidos com `borda` em f2150: 100/87/68/25/10 % nos anéis 0–0,3/0,3–0,55/0,55–0,75/0,75–0,9/0,9–1 (corrigido na conferência: era "vinheta da cena por cima de tudo, centro ≈ 45 % da altura", lida como fixa do vídeo) (alinhado ao reestudo).
7. legenda (sistema L01) por cima da vinheta.
- Linha do tempo (ms a partir do corte de entrada f2061, que é contínuo com A25): 0 afastamento começa (−79 ms do verbo que abre a frase) · 1050 pico de velocidade · 1125 nuvens do alto entram · 1625 nuvens da base · 2085 afastamento freado · 2958 nuvens começam a sumir (fade 460 ms, na palavra que fecha a frase) · 3420 1ª forma nova (−38 ms da 1ª palavra da conclusão) · 3420–4630 formas pipocam e câmera reaproxima · 4630 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: quantas formas novas e onde (ficam sempre na faixa do objeto); a altura do recuo (até o cartão caber inteiro); os recortes de "distância" (nuvens aqui).
- O que NÃO fazer: espalhar as formas pelo cartão todo (elas ficam na faixa do objeto); dar sombra preta ou contorno ao cartão; deixar a vinheta só no fundo (ela escurece também a borda e a foto); afastar com velocidade constante (precisa do acelera-freia); parar a câmera no fim (ela volta a se aproximar). Pôr uma vinheta fixa igual em todas as cenas: a luz é desta cena, com centro e força próprios, por cima de fundo e peças (correção 20/11).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "ponto de vista distante" (nuvens);
  - "elementos do mecanismo multiplicados" (as mesmas formas de A25 cobrindo o todo).
- Nesta referência as lacunas foram preenchidas com: nuvens recortadas; manchas de camuflagem.
- Receita de tratamento de cada imagem: igual a A24 (nuvens) e A25 (manchas).
- Regra de escolha: a conclusão do mecanismo ("o olho para de ver UMA forma, vê PEDAÇOS") → afasta para mostrar o efeito no conjunto e multiplica as formas. Teste em 2 temas: Claude Code → afasta do bloco de código e as caixinhas se espalham pelo projeto inteiro; café → afasta da xícara e os pontos de sabor se espalham pela mesa.

- Receita de tratamento (reestudo 20/11): foto aérea de arquivo sem retoque de cor (oliva/ocre), grão de filme de 2–3 px (8 níveis), contraste médio; a vinheta é a global, não da foto. Formas: chapadas, cores tiradas da própria foto, contorno escuro fino, furos.
- Receita de ILUSTRAÇÃO (reestudo 20/11): formas orgânicas chapadas (blob com furos) em 3 cores da paleta da imagem, contorno marrom-escuro 1–2 px, sem sombra nem textura, sem anti-alias suave; reveladas por pop de 1 quadro, nunca por fade ou escala; o traço não "ferve".
- Teste de generalização: Claude Code → recuo de um mapa de arquivos do projeto; as caixinhas de "tarefa" pipocam ao longo de uma faixa e o projeto vira mosaico; café → recuo de uma foto aérea de fazenda, manchas de cor dos lotes de colheita pipocam ao longo do vale.

- Confiança: curva, cartão, cortes = medido; tempos das nuvens e das manchas = observado.
