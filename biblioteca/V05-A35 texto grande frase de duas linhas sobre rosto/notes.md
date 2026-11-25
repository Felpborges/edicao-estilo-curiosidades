# V05-A35 · texto grande sobre o rosto: frase de transição ("And rulers wanted it / for themselves.")
- Categoria: P03 · Texto grande palavra a palavra sobre o rosto (provisória do analista: (provisória) texto grande palavra a palavra sobre o rosto (sans branca + fecho em serifada itálica))
- Fonte: V05 quadros f2443–f2494 (101,90–104,06 s; 52 quadros ≈ 2169 ms) · 23,976 fps · plano de rosto f2441–f2494
- Fala: "And rulers wanted it for themselves."
- Tipo de fala: virada
- Gatilho: "And" aparece com brilho cheio em f2444 (101 935 ms), 75 ms depois do início da palavra nº 345 "And" (101 860 ms), 3 quadros depois do corte para o rosto. Conferido com `med.py big` (pixels brancos > 215: 0 em f2443 → 1181 em f2444).
- Quadro-chave: f2485
- Camadas ativas: A-roll (rosto) | grafismo de texto (no lugar da legenda) | sem som de efeito
- Leitura dos strips: strip.jpg = quadros f2441 a f2480, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 40 células. strip-saida.jpg = quadros f2486 a f2496, de 1 em 1, 8 colunas; 11 células. detalhe-texto-grande-letras.jpg = quadro f2485 (bloco completo), região x100 y690 470x120 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a frase muda o capítulo (do "o que é" para "quem quis o poder"); o editor volta ao rosto e escreve a frase inteira em grande, para marcar a virada como um título falado.
- Por que este design: 2 linhas centradas logo acima de onde a legenda mora, sobre o peito do apresentador; a legenda amarela sai para não haver dois textos; a última palavra em serifada itálica é o "fecho" que dá o tom (a palavra que carrega a ironia ou o peso).
- Por que estas cores: branco quase puro na sans e branco levemente creme (#ede8de) na serifada itálica: a troca de família já destaca, a cor quase não muda.
- Por que estes efeitos: nenhum efeito sobre o texto (sem sombra, sem caixa): o fundo do A-roll é escuro o bastante (luma 20–30 no peito) para o branco ler sozinho.
- Por que este movimento: cada palavra acende no lugar, no instante em que é dita, e o bloco inteiro apaga junto em 5 q antes do corte (corrigido na conferência: era 4 q): leitura sincronizada com a voz, sem coreografia.
- Sensação do movimento: legenda "de cinema", calma e editorial; as palavras parecem surgir da fala, sem pulo, e a saída é um sopro.

## FORMA (fixa: reproduzir igual)
- Design: igual a V05-A12, conferido: linha 1 sans semibold branca x110–562 (centro 336 px = 46,7 %), linha 2 com a 1ª palavra em sans e a última em serifada itálica bold; faixa y705–812 (medido com `med.py big`). A linha 1 é longa (4 palavras, 62,8 % da largura).
- Movimento: cada palavra acende no lugar, sem deslize nem escala: opacidade 4 → 33 → 75 → 99 → 100 % (fade de 3 q depois de 1 quadro quase invisível) e desfoque que só some no 5º quadro (miolo da letra 3 → 25 → 62 → 90 → 97 → 100 %) (medido na correção nas 6 palavras, miolo × fundo local do quadro anterior; corrigido na conferência: era fade de 2–3 q até o brilho cheio). Saída: fade-out do bloco inteiro, sem desfoque, f2490–f2494: 100 → 91 → 63 → 35 → 10 → 0 % (5 quadros ≈ 209 ms; medido na correção, região x106 y700 462x106, fundo f2494), corte seco em f2495.
- Passos internos (quadro em que a palavra fica com brilho cheio, `med.py big`; medido na correção: a palavra tem ≈ 33 % 2 quadros antes e ≈ 4 % 3 quadros antes; palavras pelo papel, a fala fica no cabeçalho e no CONTEÚDO):

| palavra | quadro | offset do início da palavra |
|---|---|---|
| palavra 1 | f2444 | +75 ms (#345) |
| palavra 2 | f2449 | +163 ms (#346) |
| palavra 3 | f2459 | +200 ms (#347) |
| palavra 4 | f2467 | +94 ms (#348) |
| palavra 5 (linha 2) | f2473 | +84 ms (#349) |
| palavra 6, o fecho (serif itál.) | f2476 (nítida em f2478) | +109 ms (#350) |
| saída | f2490–f2494 | fade 5 q, 290 ms depois do fim do fecho |

- Ritmo: bloco completo parado f2478–f2489 = 12 quadros ≈ 500 ms. Aqui as palavras chegam com brilho cheio 80 a 200 ms DEPOIS de ditas (nos outros blocos, junto ou um pouco antes): a sincronia é "na palavra", com tolerância de ± 200 ms.
- Som: nenhum efeito detectado (lateral −120 dB de 101,8 a 104,1 s).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

- Textura (reestudo 20/11): texto vetorial liso (sem textura, sem grão); fundo = A-roll do rosto (peito com a roupa escura, luma 18–30 atrás do texto).
- Efeitos (reestudo 20/11): sombra, caixa, tarja ou escurecimento atrás do texto: nenhum (a faixa entre as linhas tem luma 24,8 sem texto em f2441 e 31,0 com texto em f2485: não escurece; sobe 6 níveis, lido como halo claro fraquíssimo de antisserrilhado/compressão, ≈ 4–6 px, `sombra` f2485 abaixo da linha 2: 156 → 68 → 44 → 33 → 25 → 22); desfoque leve só na entrada, que dura até o 5º quadro da palavra (medido na correção: o miolo da letra fica 8 a 12 pontos abaixo da opacidade do 2º ao 4º quadro, 33/25, 75/62, 99/90, e só empata no 5º ou 6º) (corrigido na conferência: era 15–25 pontos nos 2–3 primeiros quadros); vinheta, aberração, grão: nenhum adicionado.
- Câmera (reestudo 20/11): A-roll fixo (close frontal, sem punch-in); o texto não anda (a máscara das letras do quadro final casa em 100 % desde o 3º quadro de cada palavra: sem deslocamento nem escala).
- Cadência (reestudo 20/11): 24 imagens/s (cada quadro da entrada e da saída é um estado diferente de opacidade).
- Legenda nesta cena (reestudo 20/11): a legenda amarela some no próprio corte para o rosto (f2441) e volta só no corte seguinte (f2495): 54 q sem legenda (censo); o texto grande ocupa o lugar dela; o 1º quadro de texto é f2442 (1 q depois do corte).
- Entrada do texto (reestudo 20/11), opacidade de cada palavra por quadro (luma das letras do quadro final contra o entorno, f2441–f2496):
  - receita de cada palavra (remedida na correção nas 6 palavras, região de cada palavra, fundo do quadro anterior à entrada): opacidade integrada 4 → 32–33 → 74–76 → 97–99 → 100 % (o fade leva 3 q depois de 1 quadro quase invisível); miolo da letra 3 → 23–26 → 60–64 → 87–93 → 97–98 → 99–100 % (a letra só fica nítida no 5º ou 6º quadro); sem deslocamento, sem escala (corrigido na conferência: era 13 → 45 → 75 → 89 → 96 → 98 → 100 % em 6 q, que misturava o fade com a nitidez).
  - 1º quadro com ≈ 33 % de cada palavra × início da palavra na fala: palavra 1 f2442 (início f2442,2: junto), palavra 2 f2447 (f2445,1: +2 q), palavra 3 f2457 (f2454,2: +3 q), palavra 4 f2465 (f2464,7: junto), palavra 5 f2471 (f2471,0: junto), fecho f2474 (f2473,4: +1 q) (corrigido na conferência: eram as palavras citadas). Cascata = ritmo da fala (não há intervalo fixo): 5, 10, 8, 6, 3 q entre palavras.
  - saída: o bloco inteiro junto, sem desfoque (miolo = opacidade), 100 → 91 → 63 → 35 → 10 → 0 % (f2490–f2494, 5 q ≈ 209 ms; medido na correção), começando ≈ 260 ms depois do fim do fecho e terminando no último quadro do plano, com corte seco em f2495 (corrigido na conferência: era 93 → 58 → 25 → 5 → 0 em 4 q).
  - letra (f2485, limiar 200): linha 1 sans, altura de maiúscula/ascendente 37 px (2,9 % da altura), altura-x ≈ 29 px, haste 7 px → peso 0,19 da maiúscula (semibold), palavra 1 0,81 e palavra 2 0,56 da altura por letra; serifada itálica: caixa 42 px (ascendentes mais altos), haste 8 px (0,19: bold), 0,63 da altura por letra, cor #ede8de (creme) contra #fbf7f7 da sans.
  - geometria (f2485): linha 1 x111–563 × y706–742, centro x 46,8 %; linha 2 x151–519 × y758–799, centro x 46,6 %; entrelinha (topo a topo) 52 px; palavra em serif começa na linha 2 depois de 1 palavra sans.

## CONSTRUÇÃO
1. fundo: o A-roll do rosto, sem alteração (sem escurecer, sem desfocar).
2. texto linha 1: sans semibold (SF Pro Display Semibold; alt. Inter SemiBold), maiúscula 37 px (2,9 % da altura), branco #fbf7f7, centrado no eixo x 46,7 % (não 50 %), topo y 55,2 %.
3. texto linha 2: mesmas regras; a última palavra (o fecho) em serifada itálica bold (Playfair Display Bold Italic; alt. Source Serif Bold Italic) em corpo ≈ 1,13× a sans, cor #ede8de; topo y 59,2 %; mesma linha de base da sans.
4. animação de cada palavra: aparece no quadro em que a palavra começa a ser dita (0 a +3 q), opacidade 0,04 → 0,33 → 0,75 → 0,98 → 1 (fade de 3 q depois de 1 quadro quase invisível) com desfoque leve que diminui até zerar no 5º quadro; posição e escala fixas (corrigido na conferência: era 0,13 → 0,45 → 0,75 → 0,89 → 0,96 → 0,98 → 1 e desfoque 2 → 1 → 0 px em 3 q).
5. saída: bloco inteiro, sem desfoque, opacidade 1 → 0,91 → 0,64 → 0,35 → 0,10 → 0 em 5 q, o 0 no último quadro do plano e corte seco no seguinte (corrigido na conferência: era 1 → 0,93 → 0,58 → 0,25 → 0,05 → 0 em 4–5 q).
6. legenda amarela: desligada do corte de entrada ao corte de saída do plano de rosto.
- Linha do tempo (ms a partir do corte para o rosto, f2441): 0 corte, legenda some · +42 palavra 1 · +250 palavra 2 · +667 palavra 3 · +1001 palavra 4 · +1251 palavra 5 · +1376 fecho (serif) · +1543 bloco completo e nítido · +2044 fade-out começa · +2210 texto em 0 · +2252 corte seco para a cena (corrigido na conferência: eram as palavras citadas; bloco completo era +1626).
- Parâmetros que dependem do conteúdo: a frase (2 linhas, quebra antes do fecho ou com 1–2 palavras sans na linha 2), qual palavra vai em serif itálica (sempre a última), a largura de cada linha (centrada em 46,7 %).
- O que NÃO fazer: manter a legenda amarela junto; fade longo de 6 q (a opacidade sobe em 3; o que dura até o 5º quadro é o desfoque); saída de 4 q (são 5); animar com deslocamento ou pulo; usar caixa ou sombra escura; centralizar em 50 % (o eixo do texto é o do rosto, 46,7 %); pôr a serif em outra palavra que não a última; apagar palavra por palavra (a saída é do bloco inteiro).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "frase-ponte que muda o capítulo" (inteira); a última palavra vai em serifada itálica.
- Nesta referência as lacunas foram preenchidas com: "And rulers wanted it / for themselves."
- Receita de tratamento de cada imagem: sem imagem.
- Regra de escolha: virada de capítulo. A frase que muda a história de "o que é" para "quem quis" (poder) volta ao rosto com texto grande, inteira.
- Receita de tratamento (reestudo 20/11): sem imagem; o A-roll precisa ter região escura (roupa) atrás de y 55–63 % para o branco ler sem caixa.
- Teste de generalização: reel sobre Claude Code → "E as empresas quiseram / só para *elas.*" na virada para o capítulo de quem controla a IA; reel sobre café → "E os reis quiseram / tudo para *si.*" antes do capítulo do monopólio.

- Confiança: tempos e posição medidos (±2 quadros por causa do fade); fontes por comparação (iguais a A08).
