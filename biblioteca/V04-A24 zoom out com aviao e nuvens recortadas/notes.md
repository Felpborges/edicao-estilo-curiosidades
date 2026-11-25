# V04-A24 · zoom-out da câmera revelando o cartão inteiro + avião recortado subindo + nuvens recortadas passando (vista "do alto")
- Categoria: P13 · Afastamento que revela a quantidade (provisória do analista: (provisória) movimento de câmera de afastamento com recortes de profundidade (nuvens))
- Fonte: V04 quadros f1940–f1991 (80,91–83,05 s; 52 quadros ≈ 2169 ms) · 23,976 fps
- Fala: "from the air, it's still a cannon."
- Tipo de fala: consequência ("visto do alto, continua sendo X")
- Gatilho: o afastamento e o avião começam em f1940 (80914 ms), 286 ms antes da palavra nº 273 "from" (81200 ms), logo após "green," (termina 80800 ms). Conferido no `perfil` (dif 8,9 em f1939 → 10,6 em f1940 → 13–14 até f1982).
- Quadro-chave: f1985
- Camadas ativas: legenda | cena de tela cheia | grafismo (recortes) | som (voz)
- Leitura dos strips: strip.jpg = quadros f1938 a f1985, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; strip-geral.jpg = quadros f1938 a f1993, de 2 em 2, 8 colunas, da esquerda para a direita, linha a linha. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-quadro.jpg = quadro f1985, região x0 y0 720x1280 px, ampliada 1× sem suavizar (o quadro inteiro: cartão, observador, nuvens e o contorno no objeto); detalhe-contorno-objeto.jpg = f1985, x240 y380 300x140, 3× (o contorno creme que aparece no objeto); detalhe-inicio.jpg = f1950, x0 y250 720x500, 1× (o objeto ainda sem contorno); detalhe-nuvens.jpg = f1985, x0 y1080 520x170, 2× (nuvens recortadas por cima da borda do cartão).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala volta ao ponto de vista aéreo de A06/A07; a câmera literalmente sobe (zoom out) e mostra que, mesmo pintado, o objeto ainda se destaca.
- Por que este design: o mapa vira de novo um cartão na mesa, o observador (o mesmo recorte creme de A06) entra por baixo, nuvens recortadas passam por cima e um contorno creme se desenha em volta do objeto: o "contorno que o olho acha" fica visível.
- Por que estas cores: tudo da cena anterior + o creme do contorno (o creme é sempre a cor do "editor apontando") e o branco das nuvens.
- Por que estes efeitos: vinheta forte volta a cair sobre a mesa (12 % na borda); as nuvens são fotos recortadas brancas que saem do cartão e ficam sobre a mesa preta: profundidade por camadas.
- Por que este movimento: afastamento rápido que freia (−36 → −9 %/s) com giro leve, nuvens em paralaxe e o contorno desenhado na palavra "still".
- Sensação do movimento: subida de avião; o freio no fim pousa a conclusão "continua sendo X".

## FORMA (fixa: reproduzir igual)
- Design:
  - O fundo vira de novo um cartão com borda clara: em f1970 bloco x0 y158 669x1082 = larg 92,9 %, alt 84,5 %, centro (46,5 %, 54,6 %), −0,9°; em f1988 larg 90,6 %, alt 80,9 %, centro (45,3 %, 54,5 %), −3,0° (medido). Fundo escuro aparece em volta (cantos #000100–#080703) (medido).
  - Observador (recorte): o mesmo recorte de papel creme de V04-A06, ≈ 20 % da largura, sobe da borda inferior direita na diagonal (observado).
  - Elementos de distância: fotos recortadas claras e leves, em 2 camadas — uma no alto à esquerda, outra na base — passando por cima do cartão, ≈ 30–40 % da largura cada (observado).
- Movimento:
  - Afastamento da câmera (zoom-out) contínuo f1940–f1991, com leve rotação (−0,9° → −3,0°) (medido); dif do quadro quase constante: 10,6 (f1940) → 13,2 → 13,8 → 14,4 (f1946) → 13,5 → 13,8 → 14,1 → 14,5 (f1960) → 15,0 (f1965) → 13,0 → 11,5 (f1972) → 13,7 (f1977) → 13,1 (f1981) → 10,9 → 9,3 → 7,6 → 6,9 → 6,1 (f1991) (medido em `perfil`), alto porque as nuvens entram; a escala da câmera freia desde o começo (alinhado ao reestudo). (Corrigido no reestudo, `camera` na região do cartão sem nuvens: a escala já freia desde ≈ f1965, −36,5 %/s em f1942–f1950 → −16,7 %/s em f1975–f1983 → −8,8 %/s em f1983–f1991; o `perfil` fica alto porque as nuvens entram.)
  - O observador entra f1940–f1944 pela borda inferior direita e sobe devagar (observado).
  - Os elementos de distância entram pelo canto superior esquerdo a partir de ≈f1960 e pela base ≈f1976, passando em paralaxe (mais rápidas que o cartão) (observado).
  - Saída: corte seco f1991→f1992 (dif 74,1) para o A-roll (medido).
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| zoom-out + observador entra | f1940 | 52 quadros (2169 ms) | movimento de câmera + deslize | freia do começo ao fim (−36 → −9 %/s) (alinhado ao reestudo) | nº 273, a palavra que abre o novo ponto de vista (81200 ms) | −286 ms |
| elementos de distância de cima entram | ≈f1960 | até o fim | paralaxe | constante | nº 275, o lugar do novo ponto de vista (81480 ms) | f1960 = 81748 ms → +268 ms |
| elementos de distância de baixo entram | ≈f1976 | até o fim | paralaxe | constante | nº 277, a palavra que reafirma o objeto (82140 ms) | f1976 = 82416 ms → +276 ms |
| contorno creme se desenha em volta do objeto (passo acrescentado no reestudo 20/11) | f1968 | ≈ 10 quadros f1968–f1978 (≈ 420 ms) | traço que se desenha (trim path), a partir da parte de baixo | constante (observado em folha de 3 em 3) | nº 277, a palavra que reafirma o objeto (82140 ms) | f1968 = 82083 ms → −57 ms |

- Ritmo: 2,17 s sempre em movimento (nenhum quadro parado).
- Som: nenhum efeito destacável (áudio mono; voz contínua) (observado no envelope).
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)
- Textura (reestudo 20/11):
  - Foto aérea e mesa: as mesmas de A23 e das cenas de cartão (mesa preta lisa).
  - Nuvens: fotos reais de nuvem recortadas (família outra: foto recortada), brancas fofas, bordas macias de algodão (detalhe-nuvens); na região x300 y1150 200x100 (nuvem + mesa) luma 75, grão 10,7, manchas 55,3 (o contraste branco/preto).
  - Contorno do objeto: creme claro (luma 198–243), ≈ 6–8 px cheios em f1985 já afastado (f1985 `vscan` x440 y394–403), com borda macia de 2–3 px (detalhe-contorno-objeto); segue a silhueta com folga de ≈ 4–6 px.
  - Observador: o recorte creme de gravura de A06.
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: forte, luma 100/86/68/37/12 % (f1985); nitidez 100/88/52/35/9 %.
  - Luz da cena (correção 20/11, medido f1985, perfis p75 no cartão, a superfície clara mais larga): centro da poça em x ≈ 46–52 % (platô e ajuste parabólico) e em y ≈ 31 % (platô; o ajuste em y não fecha porque as nuvens claras entram embaixo), luma de pico 161 (p75); a 100 px da borda esquerda 46–49 % e em x620 54–70 % do centro. Mesa à vista (grade de 80 px): 8–16 na faixa de cima e 5–15 na coluna da direita. Mesa nos pontos fixos: (360,1060) 90,8 cai numa nuvem; (360,1180) 10,8 é mesa. Centro e força próprios desta cena, não um multiplicador fixo do vídeo.
  - Desfoque de movimento: sem desfoque de movimento (medido na conferência: borda de 2 a 9 px a 56–107 px por quadro); aqui também nenhum no afastamento de −36 %/s nem nas nuvens.
  - Sombra: nenhuma nas nuvens, no observador ou no cartão.
  - Aberração: 0,57 px (f1985, confiança 0,89), provavelmente das bordas brancas das nuvens sobre preto (borda de alto contraste na compressão); baixa confiança.
  - Profundidade: as nuvens andam mais rápido que o cartão (paralaxe, nota antiga); nenhuma camada desfocada.
- Câmera (reestudo 20/11): zoom OUT que freia: f1942→f1950 −36,5 %/s, conteúdo sobe −4,8 px/q, giro +0,06°/q; f1955→f1963 −33,8 %/s; f1975→f1983 −16,7 %/s; f1983→f1991 −8,8 %/s, −0,9 px/q. (Medido na região do cartão, sem nuvens.)
- Cadência (reestudo 20/11): 24 imagens/s (dif 6–15 em todo quadro, nota antiga).
- Passo novo (reestudo 20/11; ausente na nota antiga): o CONTORNO creme se desenha em volta do objeto entre f1968 e ≈ f1978 (≈ 10 q, 420 ms; trim path, começando pela parte de baixo), na palavra que reafirma o objeto (82140 ms = f1969,4 → f1968 = 82083 ms, −57 ms); folha f1956–f1980 de 3 em 3: sem contorno até f1965, parcial em f1971–f1974, completo em f1980.
- Legenda nesta cena (reestudo 20/11): a legenda SOME 4 quadros no começo (f1942–f1945, ainda sobre o fim da pintura de A23); depois 2 blocos de 4 palavras (f1946–f1964 e f1965–f1981; o 2º reafirma o objeto) e o bloco seguinte entra em f1982, atravessando o corte para o rosto. Tarja 59 % (medido direto, colunas do meio: f1950 59/59 %, f1970 60/59 %, f1985 58/56 %, fundo 100–134; altura 48 px y844–891, folga 2–4 px dos lados e 11 px em cima) (corrigido na conferência: era "58 % (mediana, 52–62 %)" do censo; vale para o vídeo 59 %, 56 a 64) sobre a foto clara (luma 106–130). Nenhum outro texto.

## CONSTRUÇÃO
1. mesa preta lisa (aparece à medida que a câmera se afasta).
2. cartão: a foto aérea de A23 vira cartão com borda clara (≈ 93 % × 85 % em f1970), girando de −0,9° a −3,0° com o afastamento.
3. objeto: o recorte já recolorido de A23; recebe um contorno creme de ≈ 6–8 px (folga de 4–6 px da silhueta, borda macia), desenhado por trim path em ≈ 10 q a partir de 1170 ms.
4. observador: recorte creme de gravura (o de A06), ≈ 20 % da largura, sobe da borda inferior direita na diagonal desde 0 ms.
5. nuvens: fotos recortadas de nuvem branca, 2 grupos (cima-esquerda a partir de ≈ 830 ms; base a partir de ≈ 1500 ms), por cima do cartão e da mesa, andando mais rápido que o cartão (paralaxe); sem sombra.
6. câmera: zoom out −36 %/s no começo, freando para −9 %/s no fim, giro leve; conteúdo sobe ≈ 5 → 1 px/q.
7. efeito de quadro: luz desta cena, poça com centro em ≈ (49 %, 31 %) (37 % a 0,75–0,90 do raio, 12 % na borda; a 100 px da borda ≈ 48 % à esquerda e 54–70 % à direita) + borda mole. Sem desfoque de movimento no afastamento nem nas nuvens.
8. legenda V04-L01 (some 167 ms no começo).
- Linha do tempo (ms a partir de f1940): 0 ms afastamento começa (sem corte) e o observador entra; 83–250 ms legenda ausente; ≈ 830 ms nuvens de cima; 1170–1590 ms contorno se desenha (na palavra que reafirma o objeto); ≈ 1500 ms nuvens de baixo; 2169 ms corte seco para o rosto.
- Parâmetros que dependem do conteúdo: o objeto contornado; o observador; os elementos de distância (nuvens).
- O que NÃO fazer: contornar o objeto desde o início (o contorno nasce na palavra); nuvens desenhadas (são fotos recortadas); afastamento linear; borrar as nuvens ou o cartão no afastamento; copiar a vinheta de outra cena.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "ponto de vista distante" (o que dá a sensação de olhar de longe: nuvens, vidro, distância);
  - "observador" (quem olha: avião, pessoa, satélite).
- Nesta referência as lacunas foram preenchidas com: nuvens recortadas; avião de papel creme.
- Receita de tratamento de cada imagem: fotos reais recortadas (nuvens brancas, avião em gravura creme) passando por cima do cartão com paralaxe; o cartão encolhe e mostra a borda.
- Regra de escolha: "visto de longe/do ar, ainda é X" → a câmera se afasta literalmente e os elementos de distância passam pela frente. Teste em 2 temas: Claude Code → afasta do print do código até ver a tela inteira do monitor, com reflexos/vidro passando ("de longe ainda é só um terminal"); café → afasta da xícara até ver a mesa do café, com vapor passando.
- Receita de tratamento (reestudo 20/11): nuvens = fotos reais de nuvem branca recortadas com borda macia; o contorno creme é o mesmo tom dos traços do editor (A02 #fdefd7, A08 #fff7de).
- Receita de ILUSTRAÇÃO (reestudo 20/11): contorno de silhueta creme, 6–8 px, com folga da peça e borda macia, revelado por trim path; não ferve.
- Teste de generalização: Claude Code → o print da página com o botão já disfarçado se afasta, um cursor recortado sobe, e um contorno creme se desenha em volta do botão na frase "de longe, ainda é um botão"; café → a xícara pintada da cor da mesa se afasta, fumaça recortada passa por cima e um contorno creme se desenha na xícara na frase "de longe, ainda é uma xícara".

- Confiança: zoom, rotação, curva e cortes = medido; avião e nuvens (tamanhos, entradas) = observado.
