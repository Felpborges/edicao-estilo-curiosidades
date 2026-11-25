# V05-A47 · texto grande sobre o rosto: o trocadilho ("Died with the / Empire.")
- Categoria: P03 · Texto grande palavra a palavra sobre o rosto (provisória do analista: (provisória) texto grande palavra a palavra sobre o rosto (sans branca + fecho em serifada itálica))
- Fonte: V05 quadros f3288–f3315 (137,14–138,26 s; 28 quadros ≈ 1168 ms) · 23,976 fps · plano de rosto f3287–f3315
- Fala: "(And a 3,000-year-old craft) dyed with the empire."
- Tipo de fala: piada
- Gatilho: "Died" começa a aparecer em f3288 (137 137 ms), 177 ms depois do início da palavra nº 445 "dyed" (136 960 ms), 1 quadro depois do corte. Conferido pelo brilho (71 → 128 → 205 → 252 de f3287 a f3290).
- Quadro-chave: f3310
- Camadas ativas: A-roll (rosto) | grafismo de texto | sem som de efeito
- Leitura dos strips: strip.jpg = quadros f3285 a f3316, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 32 células. detalhe-texto-grande-trocadilho.jpg = quadro f3312 (bloco completo), região x180 y690 320x135 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a frase termina num trocadilho que só funciona escrito (a fala soa igual para as duas palavras); o editor corta para o rosto só para escrever a grafia que vira a piada.
- Por que este design: linha 1 com o verbo do trocadilho em sans, linha 2 com a última palavra sozinha em serifada itálica com maiúscula: leitura de "epitáfio".
- Por que estas cores: branco e creme, como nos outros textos grandes.
- Por que estes efeitos: nenhum; o rosto escuro atrás basta.
- Por que este movimento: as palavras acendem na fala; não há saída animada: o texto corta seco junto com o plano, e a cena seguinte entra em cima da última sílaba.
- Sensação do movimento: um "ponto final" seco; o corte duro reforça o tom de lápide da frase.

## FORMA (fixa: reproduzir igual)
- Design: igual a V05-A41, conferido: linha 1 (3 palavras) sans semibold branca x190–485 (centro 337,5 = 46,9 %), y705–751; linha 2 (a palavra final) sozinha em serifada itálica bold, com maiúscula, y758–812 (medido com `med.py big`). A tela ESCREVE a grafia de um homófono (a leitura que o roteiro quer destacar) onde a fala soa ambígua: o texto grande resolve o trocadilho que só o som não mostra.
- Movimento: cada palavra acende no lugar: opacidade 0–4 → 32–36 → 73–77 → 98–100 → 100 % (fade de 3 q; a 1ª palavra entra no 1º quadro depois do corte, sem o quadro quase invisível) e desfoque que só some no 5º quadro (miolo 23–27 → 60–66 → 90–93 → 97–98 → 99–100 %) (medido na correção nas 4 palavras, miolo × fundo do quadro anterior; corrigido na conferência: era "fade de 3 quadros" pelo pico de luminância). SEM fade de saída: 100 % em f3315 e corte seco em f3316 (6153 px → 0).
- Passos internos:

| palavra (pelo papel) | 1º quadro a ≈ 33 % (o de ≈ 4 % é o anterior) | opacidade cheia (≥ 98 %) | offset do 1º quadro |
|---|---|---|---|
| palavra 1, o homófono escrito | f3288 (o anterior é o corte) | f3290 | +177 ms (#445) |
| palavra 2 | f3296 | f3298 | +151 ms (#446) |
| palavra 3 | f3300 | f3302 | −111 ms (#447) |
| palavra final (serif itál.) | f3304 | f3306 | +48 ms (#448) (corrigido na conferência: a coluna trazia as palavras citadas) |
| saída | f3316 | — | corte seco, 0 q |

- Ritmo: bloco completo parado f3306–f3315 = 10 quadros ≈ 417 ms; plano de rosto de 1,2 s só para o trocadilho.
- Som: nenhum efeito detectado (lateral −120 dB).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

- Textura (reestudo 20/11): texto vetorial liso; fundo = A-roll do rosto.
- Efeitos (reestudo 20/11): sombra, caixa, escurecimento atrás do texto: nenhum (como em V05-A35); leve desfoque até o 5º quadro de cada palavra (medido na correção: o miolo fica 7 a 11 pontos abaixo da opacidade do 2º ao 4º quadro, palavra 2 36/27, 77/66, 100/93) (corrigido na conferência: era só nos 2 primeiros quadros); vinheta, aberração, grão: nenhum adicionado.
- Câmera (reestudo 20/11): A-roll fixo; texto parado.
- Cadência (reestudo 20/11): 24 imagens/s.
- Legenda nesta cena (reestudo 20/11): a legenda amarela some no corte para o rosto (f3287) e volta no corte para a cena (f3316): 29 q sem legenda (censo); o último bloco amarelo antes do corte (5 palavras, f3245–f3286) já tinha a palavra do trocadilho escrita do jeito da fala (corrigido na conferência: eram a fala e a palavra citadas): o texto grande reescreve a mesma palavra com a grafia do trocadilho.
- Entrada do texto (reestudo 20/11), opacidade por quadro (f3286–f3317):
  - remedida na correção (região de cada palavra, fundo do quadro anterior à entrada), opacidade integrada / miolo: palavra 1 f3287 0/0 → f3288 32/23 → 75/60 → 99/90 → 100/97 → 100/99 %; palavra 2 f3295 4/3 → 36/27 → 77/66 → 100/93 → 100/98 → 100/100 %; palavra 3 f3299 4/3 → 35/26 → 76/62 → 99/90 → 100/97 %; palavra final (serif) f3303 4/3 → 33/26 → 73/62 → 98/90 → 100/97 → 100/99 %. Mesma receita de V05-A35: opacidade em 3 q depois de 1 quadro quase invisível, nitidez no 5º–6º, sem deslocamento nem escala (corrigido na conferência: era 11 → 39 → 71 → 88 → 97 → 99 → 100 %, ease-out de ≈ 6 q).
  - 1º quadro × início da palavra: palavra 1 f3288 × f3283,8 (+4 q: a 1ª palavra espera o corte), palavra 2 f3296 × f3292,4 (+4 q), palavra 3 f3300 × f3302,7 (−3 q), palavra final f3304 × f3304,9 (−1 q) (corrigido na conferência: eram as palavras citadas). Cascata de 8, 4, 4 q.
  - saída: nenhuma: tudo a 100 % em f3315 e 0 em f3316 (corte seco).
  - letra (f3312, limiar 200): linha 1 sans x190–485 × y705–742 (maiúscula 38 px), haste 7 px (semibold), #f9f9fb; linha 2 serifada itálica bold x237–434 × y758–812 (55 px com maiúscula e descendente), haste 8 px, #ece8de; centros x 46,9 % e 46,8 %.

## CONSTRUÇÃO
1. fundo: A-roll do rosto, sem alteração.
2. linha 1: sans semibold, maiúscula 37–38 px (2,9 %), #f9f9fb, centrada em x 46,9 %, topo y 55,1 %.
3. linha 2: a última palavra sozinha, serifada itálica bold com maiúscula, corpo ≈ 1,15× a sans, #ece8de, centrada em x 46,8 %, topo y 59,2 %.
4. cada palavra: opacidade 0,04 → 0,33 → 0,75 → 0,99 → 1 (fade de 3 q depois de 1 quadro quase invisível; a 1ª palavra começa direto em 0,33 no 1º quadro depois do corte) com desfoque leve que zera no 5º quadro; posição fixa (corrigido na conferência: era 0,11 → 0,39 → 0,71 → 0,88 → 0,97 → 1 em ≈ 6 q e desfoque em 2 q).
5. sem saída: corta seco com o plano.
6. legenda amarela desligada no plano de rosto.
- Linha do tempo (ms a partir do corte para o rosto, f3287): 0 corte · +42 1ª palavra · +375 2ª · +542 3ª · +709 palavra final (serif) · +876 bloco completo e nítido (corrigido na conferência: era +959) · +1210 corte seco (sem fade).
- Parâmetros que dependem do conteúdo: o trocadilho (a grafia escrita é a que a fala esconde); a palavra final em serif.
- O que NÃO fazer: fade longo de 6 q (a opacidade sobe em 3; o desfoque dura até o 5º quadro); escrever a grafia literal da fala (perde a piada); pôr fade-out (aqui corta seco); manter a legenda amarela.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "frase de efeito/trocadilho que fecha um capítulo"; "a palavra final" (serif itálica, sozinha na linha 2).
- Nesta referência as lacunas foram preenchidas com: "Died with the / Empire."
- Receita de tratamento de cada imagem: sem imagem.
- Regra de escolha: fecho de capítulo + jogo de palavras. Quando a frase tem um duplo sentido sonoro, o texto grande escreve a leitura que o roteiro quer destacar.
- Receita de tratamento (reestudo 20/11): sem imagem.
- Teste de generalização: reel sobre Claude Code → num app de música, a fala diz "e o app precisava de um conserto" e a tela escreve "e o app precisava de um / *Concerto.*"; reel sobre café → num reel sobre a contagem de cafeterias, a fala diz "e a cidade perdeu o senso" e a tela escreve "e a cidade perdeu o / *Censo.*".

- Confiança: tempos, brilho e posição medidos; fontes por comparação.
