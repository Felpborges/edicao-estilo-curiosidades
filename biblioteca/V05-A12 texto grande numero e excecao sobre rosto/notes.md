# V05-A12 · texto grande sobre o rosto: número + "a exceção"
- Categoria: P03 · Texto grande palavra a palavra sobre o rosto (provisória do analista: (provisória) texto grande palavra a palavra sobre o rosto (sans branca + fecho em serifada itálica))
- Fonte: V05 quadros f837–f924 (34,91–38,54 s; 88 quadros ≈ 3670 ms) · 23,976 fps
- Fala: "Nearly 4,000 years ago, dyers on Crete found the one exception."
- Tipo de fala: virada (número + "a única exceção")
- Gatilho: "4,000" começa a aparecer em f837 (34 910 ms), 50 ms antes do início da palavra nº 127 "4,000" (34 960 ms). Conferido pelo brilho do texto quadro a quadro (pico de luminância na região do número: 126 em f837 → 205 em f838 → 253 em f839).
- Quadro-chave: f912
- Camadas ativas: A-roll (rosto; corte de entrada em f831) | grafismo de texto (no lugar da legenda amarela) | som estéreo no fim do plano
- Leitura dos strips: strip.jpg = quadros f835 a f860, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 26 células. strip-saida.jpg = quadros f900 a f926, de 1 em 1, 8 colunas; 27 células. strip-geral.jpg = quadros f835 a f923, de 2 em 2 (aprox.), 8 colunas. detalhe-palavra-conceito-f902.jpg = quadro f902, região x290 y750 280x70 px, ampliada 2× sem suavizar (a palavra em serifada a ≈ 70 % da entrada, ainda borrada). detalhe-bloco-f912.jpg = quadro f912, região x100 y695 470x125 px, ampliada 1× sem suavizar (bloco completo: sans branca nas duas linhas e só a última palavra em serifada creme).

## LEITURA DE EDITOR
- Por que esta cena aqui: depois do problema (11 s de cena), a virada da história ("a única exceção") volta ao rosto: a frase de virada é dita olho no olho e reforçada por escrito.
- Por que este design: só o número e a palavra-conceito ganham peso; as palavras de ligação da linha 2 ficam em sans e SÓ a palavra final em serifada itálica: o olho termina a leitura no conceito.
- Por que estas cores: sans branco neutro (#f7f8f9) e serifada creme quente (#ece6db): a palavra-conceito parece "impressa", diferente do resto.
- Por que estes efeitos: nenhum além do desfoque de entrada; A-roll sem vinheta, fundo escuro da roupa dá o contraste.
- Por que este movimento: cada palavra acende junto da voz; o meio da frase (quem e onde) fica só na voz, sem texto, e a linha 1 espera 1,3 s sozinha: cria expectativa para a palavra final.
- Sensação do movimento: suspense que fecha numa batida; produzida pela pausa longa entre as linhas, pelo fade de 3 q em cada palavra (com desfoque até o 5º–6º quadro) e pela saída em fade de 5 q logo antes do corte (corrigido na conferência: era saída de 4 q), com um som grave estéreo crescendo por baixo.

## FORMA (fixa: reproduzir igual)
- Design: igual a V05-A08, conferido: 2 linhas brancas sem caixa sobre o rosto/peito; linha 1 sans semibold em y705–751, linha 2 em y758–812 (com descendentes); linhas centradas no eixo x ≈ 335 px (linha 1 x146–526, centro 46,7 %; linha 2 x113–556, centro 46,5 %) (medido com `med.py big`, limiar 215). Diferença em relação a A08: a linha 2 MISTURA as duas fontes: as palavras de ligação em sans semibold e só a última palavra (a palavra-conceito) em serifada itálica bold. Número escrito com algarismos e separador de milhar (número de 4 algarismos com vírgula).
- Movimento: cada palavra entra já na posição final com fade de 3 quadros (126 → 205 → 253 no número; 124 → 207 → 248 na 1ª palavra da linha 2; 127 → 195 → 234 na palavra-conceito; medido); opacidade 3 → 35 → 77 → 98 → 100 % nas 6 palavras e letra nítida só no 5º–6º quadro (medido na correção: opacidade pelo excesso de luz integrado na caixa dilatada da palavra e miolo pelos pixels da letra erodida, fundo do quadro anterior à entrada). Saída: fade-out do bloco inteiro f920–f924 (254 → 245 → 180 → 128 …), 5 quadros ≈ 209 ms, terminando no corte seco f925 (f920–f924: opacidade 91 → 63–65 → 30–36 → 9–11 → 0–2 %, medida na correção no miolo da letra com fundo local nas 2 linhas, sem desfoque; o último traço visível é f923; corrigido na conferência: era 90 → 51 → 18 → 3 → 0 %).
- Passos internos:

| passo | 1º quadro | completo | tipo | gatilho |
|---|---|---|---|---|
| número (linha 1) | f837 | f839 (100 % em f840) | fade-in no lugar (3 → 35 → 77 → 99 → 100 %, f836–f840) | o número (#127) −50 ms |
| palavra 2 (linha 1) | f853 (corrigido na correção: era f854) | f855 (100 % em f857) | idem (33 → 76 → 98 → 99 → 100 %, f853–f857) | a unidade do número (#128) −61 ms (corrigido: era +19 ms) |
| palavra 3 (linha 1, com vírgula) | f856 (corrigido na correção: era f857) | f858 (100 % em f859) | idem (5 → 35 → 76 → 99 → 100 %, f855–f859) | a 3ª palavra da linha 1 (#129) −47 ms (corrigido: era +5 ms) |
| palavra 4 (linha 2) | f891 | f893 (100 % em f894) | idem (3 → 35 → 76 → 98 → 100 %, f890–f894) | a 1ª palavra da linha 2 (#134) −17 ms |
| palavra 5 (linha 2) | f895 (corrigido na correção: era f896) | f897 (100 % em f898) | idem (3 → 34 → 77 → 98 → 100 %, f894–f898) | a 2ª palavra da linha 2 (#135) −70 ms (corrigido: era −28 ms) |
| palavra-conceito (serif itál.) | f901 | f903 (100 % em f906) | idem (3 → 33 → 73 → 97 → 99 → 100 %, f900–f906) | a palavra-conceito (#136) −40 ms |
| saída | f920 | f924 | fade-out do bloco (5 q: 91 → 64 → 33 → 10 → 0 %) | 300 ms depois do fim da palavra-conceito |

- Ritmo: a 1ª palavra da frase e o trecho do meio (sujeito, lugar e verbo, 4 palavras) NÃO aparecem: entre f859 e f891 (32 quadros ≈ 1335 ms) a linha 1 fica sozinha na tela enquanto ele fala o meio da frase. Bloco completo parado f903–f919 = 17 quadros ≈ 709 ms.
- Som: o canal lateral (efeito estéreo) está ativo de ≈ 36,9 s a 38,6 s (f885–f925): começa no fim da linha 1 e cresce até o corte para o mapa (A13). Lido como efeito de transição que antecipa o corte (ver análise, seção Som).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11): A-roll liso (igual a A08: parede grão 2,4, sem grão de filme); letras chapadas.
- Efeitos (reestudo 20/11): nenhuma vinheta (A-roll, ver A08); nenhuma sombra ou caixa no texto; desfoque só durante a entrada de cada palavra (mediana de luma na caixa da palavra sobe acima do valor final durante a entrada: número 90–94 × 84 final; 1ª palavra da linha 2 84–86 × 76; no miolo da letra o desfoque dura até o 5º–6º quadro, medido na correção). Sem brilho, sem aberração.
- Câmera (reestudo 20/11): parada (A-roll fixo; medido em A08: ×1,000 e 0 px na parede).
- Cadência (reestudo 20/11): 24 imagens/s (fade muda em 3 quadros seguidos).
- Legenda nesta cena (reestudo 20/11): sem legenda amarela em todo o plano (f831–f924 = 94 q, 3921 ms; some no corte de entrada e volta no corte de saída f925). O único texto é o branco grande (f837–f923). As palavras do meio da frase (sujeito, lugar, verbo) não aparecem em lugar nenhum.
- Entrada do texto (reestudo 20/11):
  - Número (linha 1): f836 3 % · f837 35 % · f838 77 % · f839 99 % · f840 100 %; miolo da haste 2 · 26 · 64 · 91 · 98 · 100 (nítido em f841) (medido na correção: opacidade pelo excesso de luz integrado na caixa dilatada da palavra e miolo pelos pixels da letra erodida, fundo do quadro anterior à entrada); corrigido na conferência: era 2 · 29 · 73 · 100. Palavra 2 da linha 1: f853 33 · f854 76 · f855 98 · f856 99 · f857 100 %; palavra 3: f855 5 · f856 35 · f857 76 · f858 99 · f859 100 %; palavra 5 (linha 2): f894 3 · f895 34 · f896 77 · f897 98 · f898 100 % (as três começam 1 q antes do que dizia a tabela).
  - 1ª palavra da linha 2 (sans): f890 3 % · f891 35 % · f892 76 % · f893 98 % · f894 100 %; miolo 2 · 28 · 64 · 90 · 99 · 100 (nítida em f895) (corrigido na conferência: era 1 · 31 · 75 · 97 · 100).
  - Palavra-conceito (serifada itálica): f900 3 % · f901 33 % · f902 73 % · f903 97 % · f904 99 % · f906 100 %; miolo 2 · 27 · 63 · 91 · 98 · 100 (nítida em f905) (corrigido na conferência: era 1 · 22 · 70 · 98 · 99, "começa mais devagar"; é a mesma curva das outras palavras).
  - Saída do bloco: f919 100 % · f920 91 % · f921 63–65 % · f922 34–36 % · f923 9–11 % · f924 0–2 % (miolo × fundo local nas 2 linhas, sem desfoque: o miolo acompanha a opacidade); corte seco em f925 (corrigido na conferência: era 90 · 51 · 18 · 3 · 0, medido contra um fundo de luma ≈ 93 que não é o fundo da letra).
  - Palavras: linha 1 [x146–283] [x299–419] [x435–526], espaços 16 px; linha 2 [x113–184] [x200–281] [x302–556], espaços 16 e 21 px; eixos 336 e 334,5 px (46,7 e 46,5 %): centragem confirmada (linhas de larguras 380 e 443 px no mesmo eixo).
  - Letra (f912): sans das duas linhas com haste 7 px (mesma da A08: 0,25 da altura-x 28 px); serifada: altura-x 29 px (y771–799), haste 8 px (0,28); a palavra-conceito 255 px ÷ 10 caracteres ÷ 29 = 0,88 (serifada um pouco mais estreita que a sans). Cor: sans #f7f8f9 / #faf7f7, serifada #ece6db.

## CONSTRUÇÃO
1. fundo: A-roll em close, câmera fixa, sem vinheta; legenda amarela desligada no plano todo.
2. bloco de texto (diagramado completo antes de animar), eixo de centragem x 335 px (46,6 %):
   - linha 1: sans semibold/bold, altura-x 28 px, cor #f8f8f8, topo da maiúscula y705: número com separador de milhar + as 2 palavras seguintes;
   - linha 2: topo y758; palavras de ligação em sans igual à linha 1 e a palavra-conceito final em serifada itálica bold, altura-x 29 px, cor #ece6db; espaço entre palavras 16–21 px.
3. animação por palavra: opacidade 0,04 → 0,35 → 0,77 → 0,98 → 1 (o fade sobe em 3 q, 125 ms) com desfoque ≈ 3 px que só zera no 5º quadro, no lugar, começando 17 a 70 ms antes da palavra falada; a serifada segue a mesma curva (corrigido na conferência: era 0 → 30 → 73 → 100 % com desfoque nos mesmos 3 q e serifada começando a 22 %).
4. saída: o bloco inteiro 100 → 91 → 64 → 35 → 10 → 0 % em 5 q (209 ms), sem desfoque nem movimento, terminando no quadro anterior ao corte seco (corrigido na conferência: era 100 → 90 → 51 → 18 → 3 → 0).
5. som: efeito grave estéreo de ≈ 1,7 s crescendo do fim da linha 1 até o corte (nota antiga).
- Linha do tempo (ms a partir do corte para o rosto, f831): 0 corte · 250 número · 918 palavra 2 · 1043 palavra 3 (corrigido na correção: eram 959 e 1084) · 1043–2419 linha 1 sozinha (a voz diz o meio da frase) · 2502 1ª palavra da linha 2 · 2669 palavra 5 (corrigido na correção: era 2711) · 2919 palavra-conceito · 3044–3711 bloco parado · 3753 fade-out · 3920 corte seco para o mapa.
- Parâmetros que dependem do conteúdo: quais palavras viram texto (número + núcleo da frase final); qual é a palavra-conceito (só a última vai para a serifada); a largura de cada linha.
- O que NÃO fazer: não pôr a linha 2 inteira em serifada (aqui só a última palavra); não mostrar as palavras do meio da frase; não centrar no meio do quadro; não sincronizar a linha 2 com a linha 1 (ela espera a voz); não manter a legenda amarela.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "número/data de abertura do fato" (linha 1); "a palavra-conceito que fecha a frase" (última palavra, serif itálica).
- Nesta referência as lacunas foram preenchidas com: "4,000 years ago," / "the one exception."
- Receita de tratamento de cada imagem: sem imagem; tipografia branca sobre o A-roll.
- Regra de escolha: ênfase de virada. Frase que introduz a resposta ("found the one exception") puxa o texto grande; o número abre e a palavra-conceito fecha em serifada itálica. As palavras de ligação ficam fora.

- Teste de generalização: reel sobre Claude Code: "Há 2 anos, um laboratório achou a única saída" → linha 1 "2 anos atrás,", linha 2 "a única saída" com "saída" em serifada. Reel sobre café: "Há 1.000 anos, pastores acharam o único grão" → linha 1 "1.000 anos atrás,", linha 2 "o único grão" com "grão" em serifada.

- Confiança: posições, brilho e tempos medidos (±1 quadro nas palavras do meio, tiradas da contagem de pixels); fontes por comparação, iguais às de A08.
