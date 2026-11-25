# V05-A41 · texto grande sobre o rosto: a virada ("Then their monopoly / backfired.")
- Categoria: P03 · Texto grande palavra a palavra sobre o rosto (provisória do analista: (provisória) texto grande palavra a palavra sobre o rosto (sans branca + fecho em serifada itálica))
- Fonte: V05 quadros f2965–f3011 (123,66–125,59 s; 47 quadros ≈ 1960 ms) · 23,976 fps · plano de rosto f2963–f3011
- Fala: "Then, their monopoly backfired."
- Tipo de fala: virada
- Gatilho: "Then" começa a aparecer em f2965 (123 665 ms), 55 ms antes do início da palavra nº 412 "Then," (123 720 ms), 2 quadros depois do corte. Conferido pelo brilho (76 → 128 → 206 → 252 de f2964 a f2967).
- Quadro-chave: f3002
- Camadas ativas: A-roll (rosto) | grafismo de texto | som estéreo (efeito começa durante o texto)
- Leitura dos strips: strip.jpg = quadros f2963 a f2998, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 36 células. strip-saida.jpg = quadros f3004 a f3013, de 1 em 1, 8 colunas; 10 células. detalhe-texto-grande-virada.jpg = quadro f3002 (bloco completo), região x95 y690 490x135 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: "o monopólio saiu pela culatra" é a virada da história (do auge para a queda); volta ao rosto com texto grande para marcar o capítulo.
- Por que este design: a palavra da virada fica SOZINHA na linha 2, em serifada itálica maior: o conceito vira manchete; a linha 1 (sans) é só o sujeito.
- Por que estas cores: branco na sans e creme (#ede8dd) na serif: a mudança é de família e de corpo, não de cor.
- Por que estes efeitos: nenhum efeito sobre o texto; o peito escuro do apresentador basta de fundo.
- Por que este movimento: cada palavra acende no lugar; aqui as 2 palavras do meio aparecem 120–220 ms ANTES de serem ditas (o texto puxa a fala) e a palavra da virada chega 1 q depois de dita, com um efeito sonoro estéreo começando por baixo.
- Sensação do movimento: "anúncio" sério; a linha 1 se monta rápida e a palavra-virada demora meio segundo a mais, criando expectativa antes do corte.

## FORMA (fixa: reproduzir igual)
- Design: igual a V05-A12/A35, conferido: linha 1 (3 palavras) sans semibold branca x104–570 (centro 337 = 46,8 %), y705–752; linha 2 (a palavra da virada) sozinha em serifada itálica bold, y758–813 (medido com `med.py big`). A palavra-conceito ocupa a linha 2 inteira.
- Movimento: cada palavra acende no lugar: opacidade 4 → 34–35 → 74–78 → 97–100 → 100 % (fade de 3 q depois de 1 quadro quase invisível), com desfoque que só some no 5º ou 6º quadro (miolo 2–3 → 25–27 → 62–64 → 89–92 → 96–98 → 99–100 %) (medido na correção nas 4 palavras, miolo × fundo do quadro anterior; corrigido na conferência: era "fade de 3 quadros" lido pelo pico de luminância). Saída: fade-out do bloco inteiro, sem desfoque, f3007–f3011: 100 → 91 → 65 → 35 → 9 → 0 % (5 quadros ≈ 209 ms; medido na correção, fundo f3011), corte seco em f3012.
- Passos internos:

| palavra (pelo papel) | 1º quadro a ≈ 35 % (o de ≈ 4 % é o anterior) | opacidade cheia (≥ 97 %) | offset do 1º quadro |
|---|---|---|---|
| palavra 1 | f2965 | f2967 | −55 ms (#412) |
| palavra 2 | f2971 | f2973 | −224 ms (#413) (corrigido na conferência: era f2972, −183 ms) |
| palavra 3 | f2976 | f2978 | −116 ms (#414) |
| palavra da virada (serif itál., linha 2) | f2994 | f2996 | +95 ms (#415) |
| saída | f3007 | f3011 | fade 5 q, 100 ms depois do fim da palavra da virada |

- Ritmo: bloco completo parado f2996–f3006 = 11 quadros ≈ 459 ms.
- Som: o canal lateral (efeito estéreo) fica ativo de ≈ 124,4 s a 126,1 s (f2983–f3023): começa ≈ 15 quadros antes da palavra da virada e atravessa o corte para a cena seguinte (A42). Lido como efeito de transição/impacto ligado à virada (ver análise, Som).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

- Textura (reestudo 20/11): texto vetorial liso; fundo = A-roll do rosto (peito escuro atrás do texto).
- Efeitos (reestudo 20/11): sombra, caixa, escurecimento atrás do texto: nenhum (como em V05-A35, medido em f3002 pelo perfil das letras contra o entorno); leve desfoque só na entrada, até o 5º quadro de cada palavra (medido na correção: o miolo fica 8 a 14 pontos abaixo da opacidade do 2º ao 4º quadro, 34/26, 75/63, 98/90) (corrigido na conferência: era 15–30 pontos nos 2–3 primeiros quadros); vinheta, aberração, grão: nenhum adicionado.
- Câmera (reestudo 20/11): A-roll fixo; texto parado (a máscara do quadro final casa em 100 %).
- Cadência (reestudo 20/11): 24 imagens/s (cada quadro de entrada e de saída é um estado diferente).
- Legenda nesta cena (reestudo 20/11): a legenda amarela some no corte para o rosto (f2963) e volta no corte para a cena (f3012): 49 q sem legenda (censo); 1º quadro de texto grande em f2965 (2 q depois do corte).
- Entrada do texto (reestudo 20/11), opacidade de cada palavra por quadro (f2963–f3013):
  - remedida na correção (região de cada palavra, fundo do quadro anterior à entrada), opacidade integrada / miolo: palavra 1 f2964 3/2 → f2965 35/26 → f2966 78/62 → f2967 101/90 → 101/96 → 102/99 %; palavra 2 f2970 4/3 → 35/27 → 76/64 → 97/89 → 99/98 → 99/100 %; palavra 3 f2975 4/2 → 34/25 → 75/63 → 98/92 → 100/98 → 100/100 %; palavra da virada (serif) f2993 4/2 → 34/26 → 74/63 → 98/90 → 100/97 → 100/99 %. Receita igual à de V05-A35: opacidade em 3 q depois de 1 quadro quase invisível, nitidez no 5º–6º, sem deslocamento nem escala (corrigido na conferência: era 13 → 39 → 71 → 85 → 93 → 95 %, ease-out de ≈ 6 q, que misturava fade e nitidez).
  - 1º quadro a ≈ 35 % × início da palavra: palavra 1 f2965 × f2966,3 (−1 q), palavra 2 f2971 × f2976,4 (−5 q), palavra 3 f2976 × f2978,8 (−3 q), palavra da virada f2994 × f2991,7 (+2 q) (corrigido na conferência: eram as palavras citadas). A cascata é 6, 5, 18 q: segue o texto, não um intervalo fixo, e pode adiantar a fala em até 220 ms.
  - saída: bloco inteiro, sem desfoque, 100 → 91 → 65 → 35 → 9 → 0 % (f3007–f3011, 5 q; medido na correção), começando 1 q antes do fim da palavra da virada (f3008) e chegando a 0 no último quadro do plano, com corte seco em f3012 (corrigido na conferência: era 92 → 58 → 27 → 5 → 0 em 4–5 q).
  - letra (f3002, limiar 200): linha 1 sans x104–570 × y705–751 (com o descendente da 3ª palavra), maiúscula 37 px, haste 7 px (semibold), cor #f9f9fa; linha 2 serifada itálica bold x210–464 × y757–812 (56 px com ascendentes e o descendente do "f"), haste 8 px, cor #ede8dd, 0,46 da caixa por letra; corpo da serif ≈ 1,15× o da sans.
  - geometria: linha 1 centrada em x 46,8 %, linha 2 centrada em x 47,0 %; entrelinha topo a topo 52 px (igual a A35).

## CONSTRUÇÃO
1. fundo: A-roll do rosto, sem alteração.
2. linha 1: sans semibold (SF Pro Display Semibold; alt. Inter SemiBold), maiúscula 37 px (2,9 %), #f9f9fa, centrada em x 46,8 %, topo y 55,1 %.
3. linha 2: só a palavra da virada, serifada itálica bold (Playfair Display Bold Italic; alt. Source Serif Bold Italic), corpo ≈ 1,15× a sans, #ede8dd, centrada em x 47,0 %, topo y 59,1 %.
4. animação de cada palavra: aparece quando a palavra começa (de −5 a +2 q), opacidade 0,04 → 0,35 → 0,76 → 0,98 → 1 (fade de 3 q depois de 1 quadro quase invisível) com desfoque leve que zera no 5º quadro; posição e escala fixas (corrigido na conferência: era 0,12 → 0,4 → 0,72 → 0,88 → 0,95 → 1 com desfoque em 3 q).
5. saída: bloco inteiro, sem desfoque, em 5 q (1 → 0,91 → 0,65 → 0,35 → 0,09 → 0), o 0 no último quadro do plano e corte seco no seguinte (corrigido na conferência: era 1 → 0,92 → 0,58 → 0,27 → 0,05 → 0 em 4–5 q).
6. legenda amarela desligada no plano de rosto.
7. som: efeito estéreo de impacto/transição começando ≈ 0,4 s antes da palavra da virada e atravessando o corte (ver Som).
- Linha do tempo (ms a partir do corte para o rosto, f2963): 0 corte, legenda some · +83 palavra 1 · +334 palavra 2 · +542 palavra 3 · +834 som estéreo começa · +1293 palavra da virada · +1460 bloco completo e nítido (corrigido na conferência: era +1543 e eram as palavras citadas) · +1835 fade-out · +2002 texto sumiu · +2044 corte seco.
- Parâmetros que dependem do conteúdo: a frase; se a palavra da virada for 1 só, ela fica sozinha na linha 2; o corpo da serif sobe para ocupar a linha.
- O que NÃO fazer: fade longo de 6 q (a opacidade sobe em 3; o desfoque é que dura até o 5º quadro); saída de 4 q (são 5); pôr a palavra da virada na mesma linha da sans; usar cor diferente (é creme quase branco); animar com pulo/escala; manter a legenda amarela.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "frase de virada da história"; "o verbo/palavra da virada" (serif itálica, sozinha na linha 2).
- Nesta referência as lacunas foram preenchidas com: "Then their monopoly / backfired."
- Receita de tratamento de cada imagem: sem imagem.
- Regra de escolha: virada (anúncio de que tudo vai mudar). Volta ao rosto, texto grande; a palavra que vira a história fica em itálico.
- Receita de tratamento (reestudo 20/11): sem imagem.
- Teste de generalização: reel sobre Claude Code → "Aí, a vantagem deles / *virou contra.*" na virada para os problemas; reel sobre café → "Então, o monopólio / *desabou.*" antes da queda dos preços.

- Confiança: tempos, brilho e posição medidos; fontes por comparação.
