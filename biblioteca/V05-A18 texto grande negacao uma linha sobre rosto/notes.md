# V05-A18 · texto grande sobre o rosto: a negação ("Not at all.")
- Categoria: P03 · Texto grande palavra a palavra sobre o rosto (provisória do analista: (provisória) texto grande palavra a palavra sobre o rosto (1 linha, fecho em serifada itálica))
- Fonte: V05 quadros f1123–f1142 (46,84–47,63 s; 20 quadros ≈ 834 ms) · 23,976 fps · plano de rosto f1122–f1142
- Fala: "Not at all."
- Tipo de fala: virada (negação curta que responde à pergunta retórica)
- Gatilho: "Not" começa a aparecer em f1123 (46 834 ms), 16 ms antes do início da palavra nº 169 "Not" (46 850 ms), 1 quadro depois do corte para o rosto (f1122). Conferido pelo brilho (pico de luminância na região da palavra: 50 em f1122 → 120 → 205 → 249 em f1125).
- Quadro-chave: f1140
- Camadas ativas: A-roll (rosto) | grafismo de texto (no lugar da legenda) | sem som de efeito
- Leitura dos strips: strip.jpg = quadros f1120 a f1145, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 26 células. detalhe-linha-unica.jpg = quadro f1140, região x210 y745 250x65 px, ampliada 2× sem suavizar (linha única: 2 palavras em sans branca e a última em serifada creme).

## LEITURA DE EDITOR
- Por que esta cena aqui: a cena anterior termina numa pergunta retórica ("então é roxo por dentro, né?"); a negação seca volta ao rosto por menos de 1 s: o "não" é dito olhando para o espectador.
- Por que este design: só 3 palavras, uma linha, na altura da linha 2 dos outros blocos (y758–800), mais perto do queixo que do peito: curta e central; a última palavra em serifada fecha a frase como uma batida.
- Por que estas cores: sans #f9f8fa e serifada #ebe6dd (creme), as mesmas de A08/A12.
- Por que estes efeitos: nenhum (A-roll sem vinheta, texto sem caixa nem sombra).
- Por que este movimento: as 3 palavras acendem com a voz e o bloco NÃO faz fade de saída: some no corte, porque o plano é curto demais para um fade.
- Sensação do movimento: resposta rápida e seca, "corta!"; produzida pelo plano de 876 ms, palavras a cada ≈ 300 ms e saída em 0 q no corte.

## FORMA (fixa: reproduzir igual)
- Design: igual a V05-A08/A12, conferido, com uma diferença de posição: UMA linha só, e ela fica na altura da LINHA 2 dos outros blocos (y758–801, 59,2–62,6 % da altura), não na linha 1. Linha centrada no eixo x ≈ 336 px (x222–450, centro 46,7 %) (medido com `med.py big`, limiar 215). As 2 primeiras palavras em sans semibold branca; a última palavra em serifada itálica bold branca.
- Movimento: palavras com fade de 3 quadros no lugar (palavra 1 120 → 205 → 249; palavra 2 103 → 199 → 250; palavra 3 105 → 185 → 234; medido); opacidade 4 → 34 → 76 → 99 → 100 % e letra nítida só no 5º–6º quadro (medido na correção: opacidade pelo excesso de luz integrado na caixa dilatada da palavra e miolo pelos pixels da letra erodida, fundo do quadro anterior à entrada). SEM fade de saída: o texto completo fica até f1142 e some no corte seco f1143 (pixels 2749 → 0).
- Passos internos:

| passo | 1º quadro | completo | gatilho |
|---|---|---|---|
| palavra 1 | f1123 | f1125 (100 % em f1126) | a 1ª palavra (#169) −16 ms |
| palavra 2 | f1130 | f1132 (100 % em f1133) | a 2ª palavra (#170) +30 ms |
| palavra 3 (serif itál.) | f1134 | f1136 (100 % em f1137) | a palavra final (#171) +17 ms |
| saída | f1143 | — | corte seco junto com a troca de plano (0 q) |

- Ritmo: plano de rosto curto (21 quadros ≈ 876 ms) só para a negação; bloco completo parado f1136–f1142 = 7 quadros ≈ 292 ms.
- Som: nenhum efeito detectado (lateral −120 dB de 46,5 a 47,8 s).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11): A-roll liso (como A08); letras chapadas.
- Efeitos (reestudo 20/11): nenhum (A-roll sem vinheta; sem sombra/caixa no texto; desfoque só na entrada de cada palavra: mediana de luma na caixa 100–109 durante a entrada × 95 no fim).
- Câmera (reestudo 20/11): parada (A-roll fixo, ver A08).
- Cadência (reestudo 20/11): 24 imagens/s.
- Legenda nesta cena (reestudo 20/11): sem legenda amarela no plano todo (f1122–f1142, 21 q; `legenda` f1130: nenhuma); some no corte de entrada e volta no corte de saída (f1143). Único texto: as 3 palavras grandes.
- Entrada do texto (reestudo 20/11): palavra 1: f1123 33 % · f1124 76 % · f1125 98 % · f1126 100 % (fundo f1122), miolo 26 · 66 · 92 · 99 · 100 (nítida em f1127); palavra 2: f1129 4 · f1130 34 · f1131 76 · f1132 99 · f1133 100 %, miolo nítido em f1134; palavra 3 (serifada): f1133 4 % · f1134 35 % · f1135 75 % · f1136 99 % · f1137 100 %, miolo 4 · 29 · 67 · 94 · 98 · 100 (nítida em f1138) (medido na correção: opacidade pelo excesso de luz integrado na caixa dilatada da palavra e miolo pelos pixels da letra erodida, fundo do quadro anterior à entrada); corrigido na conferência: palavra 3 era 2 · 34 · 75 · 100 pelo p98. Mesma curva de A08/A12: 4 → 35 → 77 → 98 → 100 %, com desfoque até o 5º–6º quadro. Saída: nenhuma animação; p98 252,6 em f1142 e 86 em f1143 (corte seco); remedido na correção: opacidade 100 % de f1138 a f1142, nenhum fade. Letra (f1140): sans haste 7 px (altura-x 28 px → 0,25), #f9f8fa; serifada #ebe6dd. Palavras [x222–298] [x315–355] [x375–450], espaços 17 e 20 px; eixo 336 px (46,7 %).

## CONSTRUÇÃO
1. fundo: A-roll em close, câmera fixa, sem vinheta; legenda amarela desligada no plano.
2. texto: 1 linha centrada no eixo x 336 px (46,7 %), topo da maiúscula em y758 (59,2 %: a posição da linha 2 dos blocos de 2 linhas, não a da linha 1); palavras de ligação em sans semibold/bold, altura-x 28 px, #f9f8fa; última palavra em serifada itálica bold, #ebe6dd; espaço 17–20 px.
3. animação por palavra: opacidade 0,04 → 0,35 → 0,77 → 0,98 → 1 (o fade sobe em 3 q, 125 ms) com desfoque ≈ 3 px que só zera no 5º quadro, no lugar, começando −16 a +30 ms em relação à palavra falada (corrigido na conferência: era 0 → 34 → 75 → 100 % com desfoque nos mesmos 3 q).
4. saída: nenhuma; o texto some no corte seco (plano < 1 s).
- Linha do tempo (ms a partir do corte para o rosto, f1122): 0 corte · 42 palavra 1 · 334 palavra 2 · 501 palavra 3 (serifada) · 584–876 parado · 876 corte seco para a cena.
- Parâmetros que dependem do conteúdo: as palavras (frase de negação/resposta curta); qual vai para a serifada (a última).
- O que NÃO fazer: não pôr a linha única na altura da linha 1 (ela fica na altura da linha 2); não fazer fade-out num plano tão curto; não manter a legenda amarela.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "a resposta curta que desmente a suposição anterior"; a última palavra (a de maior força) vai em serifada itálica.
- Nesta referência as lacunas foram preenchidas com: "Not at all." (com "all." em itálico).
- Receita de tratamento de cada imagem: sem imagem; tipografia branca sobre o A-roll.
- Regra de escolha: negação/virada. Depois de uma pergunta retórica feita sobre b-roll ("So the snail is purple inside, right?"), corta para o rosto e a resposta curta vira texto grande.

- Teste de generalização: reel sobre Claude Code: "Então ele entende tudo, né?" → rosto, "Nem *perto*." Reel sobre café: "Então o grão já nasce marrom?" → rosto, "Nada *disso*."

- Confiança: tempos, brilho e posição medidos; fontes iguais às de A08 (por comparação).
