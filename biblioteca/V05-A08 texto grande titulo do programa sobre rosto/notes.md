# V05-A08 · texto grande sobre o rosto: título do programa
- Categoria: P03 · Texto grande palavra a palavra sobre o rosto (provisória do analista: (provisória) texto grande palavra a palavra sobre o rosto (sans branca + fecho em serifada itálica))
- Fonte: V05 quadros f487–f554 (20,31–23,11 s; 68 quadros ≈ 2836 ms) · 23,976 fps
- Fala: "(This is) Chasing Beauty, (and today we're looking at) Tyrian purple."
- Tipo de fala: anúncio (título do programa e do tema)
- Gatilho: "Chasing" começa a aparecer em f487 (20312 ms), 8 ms antes do início da palavra nº 71 "Chasing" (20320 ms). Conferido pelo brilho do texto quadro a quadro (pico de luminância na região da palavra: 72 em f486 → 123 em f487 → 205 → 248 em f489).
- Quadro-chave: f548
- Camadas ativas: A-roll (rosto) | grafismo de texto (substitui a legenda amarela) | som estéreo no início do plano
- Leitura dos strips: strip.jpg = quadros f484 a f531, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 48 células (recorte x0 y650 720x180 do quadro, só a faixa do texto). strip-saida.jpg = quadros f538 a f556, de 1 em 1, 8 colunas; 19 células. strip-geral.jpg = quadros f485 a f555, de 2 em 2, 8 colunas; 36 células. detalhe-entrada-f488.jpg = quadro f488, região x150 y695 200x65 px, ampliada 3× sem suavizar (1ª palavra a ≈ 72 % da entrada: ainda borrada). detalhe-letras-f548.jpg = quadro f548, região x150 y695 200x125 px, ampliada 3× sem suavizar (as duas famílias de letra completas, nítidas, sem halo).

## LEITURA DE EDITOR
- Por que esta cena aqui: fim do gancho de 20 s; a volta ao rosto com o nome do programa e o nome do tema funciona como "cartela de abertura" sem sair do apresentador.
- Por que este design: só as palavras-chave da frase, grandes, no peito do apresentador, abaixo do queixo; a sans diz o nome da série e a serifada itálica diz o tema (a parte "bonita", nobre).
- Por que estas cores: branco puro #f9f8fa na sans e branco-creme quente #ede5db na serifada: a diferença é sutil e faz a palavra-tema parecer impressa, de livro.
- Por que estes efeitos: nenhum (sem caixa, sem sombra mensurável, sem vinheta: o A-roll não tem vinheta); o texto pousa direto sobre a roupa escura, que dá o contraste.
- Por que este movimento: cada palavra acende no lugar, junto da voz, com um leve desfoque que limpa: o texto parece "falado", não digitado; sai inteiro num fade curto antes do corte.
- Sensação do movimento: calma, editorial, de abertura de documentário; produzida pelo fade-in de 3 q (35 → 77 → 98 %) com um desfoque que só limpa no 5º–6º quadro, sem deslize nem escala, e pelo fade-out de 5 q sem movimento (corrigido na conferência: era 30 → 73 → 97 % e fade-out de 4 q).

## FORMA (fixa: reproduzir igual)
- Design: 2 linhas de texto branco #f2f1f2 (mediana dos pixels do texto, f548) sem caixa, sem contorno visível, sem sombra mensurável (corrigido no reestudo, f548: luma em volta igual antes e com texto; antes "sombra suave escura difusa (observado)") direto sobre o rosto/peito, na faixa y705–812 (55,1–63,4 % da altura). Linhas CENTRADAS num eixo deslocado para a esquerda, x ≈ 337 px (46,8 % da largura), não no centro do quadro (medido com `med.py white`, limiar 215: linha 1 x159–515, centro 337; linha 2 x158–518, centro 338; o mesmo eixo de 46,5–46,7 % aparece em V05-A12, onde as linhas têm larguras diferentes, o que confirma centralização e não alinhamento à esquerda). Cada palavra já entra na posição final da linha completa (o texto não se recentra quando a linha cresce).
  - Linha 1: sans-serif, peso semibold/bold, caixa alta e baixa; altura de maiúscula 36–38 px (2,8–3,0 % da altura; 1ª maiúscula y705–742, 2ª maiúscula y706–741, medido); caixa da linha y705–751. Fonte por comparação: SF Pro Display Semibold (confiança média); alternativa: Inter SemiBold.
  - Linha 2: serifada ITÁLICA bold, mesmo corpo aparente, caixa y758–812 (com descendentes). Fonte por comparação: Playfair Display Bold Italic (confiança baixa); alternativa: Source Serif 4 Bold Italic.
  - Entrelinha: 53 px de topo a topo (705 → 758).
- Movimento: cada palavra entra sozinha, NO LUGAR FINAL (sem deslize, sem escala), por fade de cinza para branco em 3 quadros ≈ 125 ms (pico de brilho: palavra 1 123 → 205 → 248; palavra 3 116 → 188 → 232; medido); opacidade por quadro 4 → 35 → 77 → 98 → 100 % nas 4 palavras e letra nítida só no 5º–6º quadro (medido na correção: opacidade pelo excesso de luz integrado na caixa dilatada da palavra e miolo pelos pixels da letra erodida, fundo do quadro anterior à entrada). O bloco cresce para a direita e para baixo; nada se reposiciona.
- Passos internos:

| passo | 1º quadro | completo | duração | tipo | gatilho |
|---|---|---|---|---|---|
| palavra 1 (linha 1) | f487 | f489 (100 % em f490) | 3 q ≈ 125 ms | fade-in no lugar (4 → 35 → 77 → 98 → 100 %, f486–f490) | 1ª palavra do nome da série (#71) −8 ms |
| palavra 2 (linha 1) | f494 | f496 (100 % em f497) | 3 q ≈ 125 ms | fade-in no lugar (4 → 35 → 76 → 99 → 100 %, f493–f497) | 2ª palavra do nome da série (#72) −36 ms |
| palavra 3 (linha 2, serif itál.) | f530 | f532 (100 % em f533) | 3 q ≈ 125 ms | fade-in no lugar (3 → 33 → 74 → 98 → 100 %, f529–f533) | 1ª palavra do tema (#78) −45 ms |
| palavra 4 (linha 2, serif itál.) | f541 (corrigido no reestudo, f541; antes f542) | f543 (100 % em f544) | 3 q ≈ 125 ms | fade-in no lugar (3 → 34 → 75 → 99 → 100 %, f540–f544) | 2ª palavra do tema (#79) −14 ms |
| saída do bloco | f550 | f554 | 5 q ≈ 209 ms | fade-out de tudo junto: opacidade 100 → 91 → 63 → 34 → 9 → 0 % (f549–f554, sem desfoque; corrigido na conferência: era 254 → 245 → 178 → 125 → 82 → 63 de pico, que dava 92 · 59 · 28 · 6) | logo após o fim da última palavra do tema (22910 ms); corte seco em f555 |

- Ritmo: só as palavras-chave da frase aparecem (as palavras de ligação, 2 antes do nome da série e 5 entre a série e o tema, ficam sem texto nenhum na tela: nem a legenda amarela). A linha 1 fica sozinha 34 quadros (f496–f529, ≈ 1418 ms); o bloco completo fica parado f543–f549 = 7 quadros ≈ 292 ms antes do fade-out.
- Som: o canal lateral (efeito estéreo) está ativo de ≈ 18,8 s a 20,4 s, terminando no começo deste plano (corte para o rosto em f480 = 20,02 s); nenhum som novo na entrada das palavras (lateral −120 dB de 20,5 a 23,2 s).
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - A-roll (parede do fundo, região 560,100,140,200 em f520): família liso (vídeo digital limpo, fundo desfocado). Cor #285846, grão 2,4, manchas 6,4, ac1 +0,72 / ac2 +0,28 / ac4 −0,04. Sem grão de filme.
  - Letras: chapadas, sem textura (detalhe f548: borda limpa, antisserrilhado de 1–2 px).
- Efeitos (reestudo 20/11): vinheta NENHUMA no rosto (`borda` f520: luma 100 · 96 · 96 · 94 · 105 %); a nitidez cai para a borda (100 · 60 · 35 · 27 · 19 %) porque o fundo está desfocado (profundidade de campo da lente, não efeito). Sombra/halo do texto: nenhum mensurável (mediana de luma em volta das linhas igual antes e com texto: acima 22,8 → 23,0; direita 23,3 → 23,1; abaixo 23,3 → 24,3); corrigido no reestudo: "sombra suave escura difusa (observado)" → "sem sombra mensurável; o fundo atrás já é escuro (luma ≈ 23)". Desfoque na entrada: sim, a palavra entra borrada e fica nítida; o miolo da haste fica 9 a 15 pontos abaixo da opacidade do 2º ao 4º quadro (25 · 62 · 88 contra 35 · 77 · 98) e só fica nítido no 5º–6º quadro (medido na correção, f486–f491; corrigido na conferência: era "limpa nos mesmos 3 q") (detalhe f488; a mediana de luma na caixa da palavra sobe acima do valor final durante a entrada: 92,9 em f488 × 82,9 no fim). Sem aberração, sem grão.
- Câmera (reestudo 20/11): parada (medido: escala ×1,000 e 0 px entre f490 e f545 na parede, região 0,0,220,600). O apresentador se mexe, a câmera não.
- Cadência (reestudo 20/11): 24 imagens/s (a opacidade de cada palavra muda em 3 quadros seguidos, sem quadro repetido).
- Legenda nesta cena (reestudo 20/11): a legenda amarela SOME no corte para o rosto (f479 → f480) e só volta no corte seguinte (f555), 75 quadros = 3128 ms sem amarelo; nesse tempo o único texto é o branco grande (f487–f553). As palavras de ligação não exibidas ficam sem texto nenhum. Tarja: nenhuma.
- Entrada do texto (reestudo 20/11): medida quadro a quadro (p98 de luma na caixa de cada palavra, opacidade relativa ao fundo):
  - palavra 1 (linha 1) f486 4 % · f487 35 % · f488 77 % · f489 98 % · f490 100 %; miolo da haste 3 · 25 · 62 · 88 · 98 · 100 % (nítida em f491) (medido na correção: opacidade pelo excesso de luz integrado na caixa dilatada da palavra e miolo pelos pixels da letra erodida, fundo do quadro anterior à entrada); corrigido na conferência: era 1 · 26 · 72 · 95 · 100 pelo p98;
  - palavra 2 (linha 1) f493 4 % · f494 35 % · f495 76 % · f496 99 % · f497 100 %; miolo 3 · 25 · 61 · 89 · 97 · 99 · 100 (nítida em f499) (corrigido na conferência: era 3 · 31 · 73 · 97 · 98);
  - palavra 3 (linha 2) f529 3 % · f530 33 % · f531 74 % · f532 98 % · f533 100 %; miolo 2 · 26 · 65 · 92 · 98 · 100 (nítida em f534) (corrigido na conferência: era 2 · 30 · 73 · 97 · 98);
  - palavra 4 (linha 2) f540 3 % · f541 34 % · f542 75 % · f543 99 % · f544 100 %; miolo 2 · 28 · 66 · 93 · 98 · 100 (nítida em f545) (corrigido no reestudo, f541: começa em f541, não em f542; corrigido na conferência: era 0 · 30 · 74 · 99).
  - Curva padrão: opacidade 4 → 35 → 77 → 98 → 100 % (o fade sobe em 3 quadros, 125 ms, +31 a +42 %/q); a palavra entra borrada e o desfoque dura mais que o fade: o miolo da letra (25 → 62 → 89 → 98 → 100) só fica nítido no 5º ou 6º quadro (≈ 210–250 ms); no lugar final, sem deslize e sem escala (corrigido na conferência: era 30 → 73 → 97 % com desfoque que limpa nos mesmos 3 q). Cola na voz: −8, −36, −45, −14 ms do início da palavra.
  - Saída: o bloco inteiro f549 100 % · f550 91 % · f551 63–64 % · f552 34–36 % · f553 9–11 % · f554 0–1 %, medido nas 2 linhas com fundo local, sem movimento e sem desfoque (miolo igual à opacidade); corte seco em f555 (corrigido na conferência: era 92 · 59 · 28 · 6 · 0).
  - Letra (medido em f548 no quadro cheio): linha 1 sans: maiúscula 37 px (y705–742), altura-x 28 px (y715–742), descendente até y751; haste 7 px (mediana das corridas horizontais) → peso haste ÷ altura-x = 0,25 (semibold a bold); largura 184 px ÷ 7 letras ÷ 28 = 0,94 (largura normal). Linha 2 serifada itálica: maiúscula 41 px (y758–799), altura-x 28–29 px (y771–799), descendente até y812; haste 8 px → 0,28 (bold); largura 166 ÷ 6 ÷ 28,5 = 0,97. Espaço entre palavras: 18 px (linha 1) e 13 px (linha 2). Entrelinha 53 px. Eixo de centragem x 337–338 (46,8–47,0 %).
  - Cor: sans #f9f8fa (branco neutro); serifada #ede5db (branco-creme quente, B 31 níveis abaixo do R) (medido, mediana do miolo das letras em f548).

## CONSTRUÇÃO
1. fundo: A-roll em close, câmera parada, sem vinheta, sem filtro; a legenda amarela desligada em todo o plano.
2. texto linha 1: sans semibold/bold (SF Pro Display Semibold ou Inter SemiBold/Bold), altura-x 28 px (2,2 % da altura), maiúscula 37 px, cor #f9f8fa, sem caixa, sem sombra, sem contorno; centrada no eixo x 337 px (46,8 % da largura), topo da maiúscula em y705 (55,1 %).
3. texto linha 2: serifada itálica bold (Playfair Display Bold Italic ou Source Serif 4 Bold Italic), mesma altura-x (28–29 px), cor #ede5db, mesmo eixo, topo da maiúscula em y758 (53 px abaixo do topo da linha 1).
4. layout: diagramar o bloco COMPLETO primeiro (posição final de cada palavra com a linha inteira centrada) e só então animar palavra por palavra; nada se recentra.
5. animação de cada palavra: começa 8 a 45 ms antes do início da palavra falada; opacidade 0,04 → 0,35 → 0,77 → 0,98 → 1 em quadros seguidos (o fade leva 3 q, 125 ms), com desfoque gaussiano que começa em ≈ 3 px e só zera no 5º quadro (≈ 210 ms); sem deslize, sem escala (corrigido na conferência: era 0 → 30 → 73 → 97 → 100 % com o desfoque zerando nos mesmos 3 q).
6. saída: o bloco inteiro faz fade 100 → 91 → 64 → 35 → 10 → 0 % (5 q ≈ 209 ms, ease-in-out, sem desfoque, sem movimento) e o corte seco vem no quadro seguinte (corrigido na conferência: era 100 → 92 → 59 → 28 → 6 → 0, ease-in).
- Linha do tempo (ms a partir do corte para o rosto, f480): 0 corte; nada na tela durante as palavras de ligação · 292 palavra 1 · 584 palavra 2 · 584–2084 linha 1 sozinha · 2085 palavra 3 (1ª da linha 2) · 2544 palavra 4 · 2627–2836 bloco completo parado · 2919 começa o fade-out · 3128 corte seco para a cena seguinte.
- Parâmetros que dependem do conteúdo: quais palavras da frase viram texto (só as de conteúdo: nome da série + nome do tema); quais vão para a serifada (a linha do tema, aqui as 2 palavras da linha 2); a largura de cada linha (o eixo fica em 46,8 %).
- O que NÃO fazer: não centrar no meio do quadro (eixo 46,8 %); não manter a legenda amarela junto; não mostrar as palavras de ligação; não deslizar nem escalar as palavras; não pôr caixa, sombra preta ou contorno; não usar o mesmo branco nas duas famílias; não fazer o fade-out depois do corte; não deixar a letra nítida já no 3º quadro (o desfoque dura até o 5º).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "nome do programa/série" (linha 1, sans); "tema do episódio" (linha 2, serif itálica).
- Nesta referência as lacunas foram preenchidas com: "Chasing Beauty" / "Tyrian purple."
- Receita de tratamento de cada imagem: não há imagem; só tipografia branca sobre o A-roll.
- Regra de escolha: apresentação/anúncio. A frase em que o apresentador diz o nome do programa e o tema puxa o texto grande; só os nomes próprios viram texto; o tema (o assunto-âncora) vai na serifada itálica.

- Teste de generalização: reel sobre Claude Code: "Este é o [nome da série], e hoje: agentes que trabalham sozinhos" → linha 1 sans "Nome da Série", linha 2 serifada itálica "agentes sozinhos." Reel sobre café: "Este é o [nome da série], e hoje: o café mais caro do mundo" → linha 1 "Nome da Série", linha 2 serifada "o café mais caro."

- Confiança: posições, alturas, cor e tempos medidos; fontes por comparação (média/baixa); sombra medida: nenhuma mensurável (alinhado ao reestudo).
