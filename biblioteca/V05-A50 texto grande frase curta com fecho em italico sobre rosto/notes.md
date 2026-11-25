# V05-A50 · texto grande sobre o rosto: frase curta de resultado ("The experiment / failed.")
- Categoria: P03 · Texto grande palavra a palavra sobre o rosto (provisória do analista: (provisória) texto grande palavra a palavra sobre o rosto (sans branca + fecho em serifada itálica))
- Fonte: V05 quadros f3446–f3479 (143,81–145,19 s; 34 quadros ≈ 1418 ms) · 23,976 fps · plano de rosto f3445–f3479
- Fala: "The experiment failed."
- Tipo de fala: virada
- Gatilho: "The" começa a aparecer em f3446 (143 726 ms), 16 ms depois do início da palavra nº 466 "The" (143 710 ms), 1 quadro depois do corte. Conferido pelo brilho (75 → 132 → 203 → 247 de f3445 a f3448).
- Quadro-chave: f3466
- Camadas ativas: A-roll (rosto) | grafismo de texto | sem som de efeito
- Leitura dos strips: strip.jpg = quadros f3443 a f3480, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 38 células. detalhe-texto-grande-curto.jpg = quadro f3470 (bloco completo), região x150 y690 380x135 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: "o experimento falhou" é o fundo do poço antes da virada feliz; frase curta, volta ao rosto e escreve.
- Por que este design: 2 palavras sans na linha 1 e o verbo do resultado sozinho em serifada itálica na linha 2: o resultado vira manchete.
- Por que estas cores: branco e creme (#eae8de), como nos outros textos grandes.
- Por que estes efeitos: nenhum; fundo escuro do peito.
- Por que este movimento: acende palavra a palavra e sai inteiro com fade de 5 q antes do corte (corrigido na conferência: era 4 q); a cena seguinte começa no "But" da virada.
- Sensação do movimento: pausa seca e curta (1,4 s), como prender a respiração antes da reviravolta.

## FORMA (fixa: reproduzir igual)
- Design: igual a V05-A41/A47, conferido: linha 1 (2 palavras) sans semibold branca x160–512 (centro 336 = 46,7 %), linha 2 (o verbo do resultado) sozinha em serifada itálica bold (medido com `med.py big`).
- Movimento: cada palavra acende no lugar: opacidade 0–4 → 32–34 → 74–76 → 98–99 → 100 % (fade de 3 q) com desfoque que só some no 5º quadro (miolo 22–27 → 59–63 → 88–91 → 96–97 → 99–100 %) (medido na correção nas 3 palavras, miolo × fundo do quadro anterior; corrigido na conferência: era "fade de 3 quadros" pelo pico de luminância). Saída: fade-out do bloco inteiro, sem desfoque, f3475–f3479: 100 → 91 → 65 → 35 → 10 → 0 % (5 quadros ≈ 209 ms; medido na correção, fundo f3479), corte seco em f3480.
- Passos internos:

| palavra (pelo papel) | 1º quadro a ≈ 33 % | opacidade cheia (≥ 98 %) | offset do 1º quadro |
|---|---|---|---|
| palavra 1 | f3446 | f3448 | +16 ms (#466) |
| palavra 2, o sujeito | f3448 | f3450 | −70 ms (#467, 143 880 ms; f3448 = 143 810 ms) (corrigido na conferência: era f3449, −28 ms) |
| verbo do resultado (serif itál.) | f3457 | f3459 | −275 ms (#468, 144 460 ms) — ver nota (corrigido na conferência: a coluna trazia as palavras citadas) |
| saída | f3475 | f3479 | fade 5 q |

- Nota de sincronia: pela transcrição, o verbo do resultado começa em 144 460 ms; no envelope (`audio` f3448–f3472) há um vale em f3452–f3456 e energia nova em f3457, o que sugere que a palavra começa antes do que o whisper marcou (desvio de até ≈ 270 ms). Não corrigido no JSON; o texto provavelmente entra junto da palavra.
- Ritmo: bloco completo parado f3459–f3474 = 16 quadros ≈ 667 ms.
- Som: nenhum efeito detectado (lateral −120 dB).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

- Textura (reestudo 20/11): texto vetorial liso; fundo = A-roll do rosto.
- Efeitos (reestudo 20/11): sombra, caixa, escurecimento: nenhum (como em V05-A35); leve desfoque até o 5º quadro de cada palavra (medido na correção: o miolo fica 8 a 15 pontos abaixo da opacidade do 1º ao 3º quadro, palavra 1 32/22, 74/59, 99/88) (corrigido na conferência: era só nos 2 primeiros quadros); vinheta, aberração, grão: nenhum adicionado.
- Câmera (reestudo 20/11): A-roll fixo; texto parado.
- Cadência (reestudo 20/11): 24 imagens/s.
- Legenda nesta cena (reestudo 20/11): a legenda amarela some no corte para o rosto (f3445) e volta no corte para a cena (f3480): 35 q sem legenda (censo); 1º quadro de texto grande em f3446 (1 q depois do corte).
- Entrada do texto (reestudo 20/11; remedida na correção palavra por palavra, cada uma na sua região e com o fundo do quadro anterior, linha 1 até y752 e linha 2 a partir de y755, o que separa as palavras que se tocam pelo descendente), opacidade integrada / miolo:
  - palavra 1 f3445 0/0 → f3446 32/22 → 74/59 → 99/88 → 100/96 → 100/99 %; palavra 2 f3448 32/23 → 75/61 → 99/90 → 100/97 → 100/99 %; verbo do resultado (serif) f3456 4/3 → f3457 34/27 → 76/63 → 98/91 → 100/97 → 100/99 %. Mesma receita de V05-A35: opacidade em 3 q, nitidez no 5º–6º (corrigido na conferência: era 14 → 40 → 71 → 87 → 96 → 98 → 100 %, ease-out de ≈ 6 q, com as palavras 2 e 3 lidas juntas).
  - 1º quadro × início da palavra: palavra 1 f3446 × f3445,6 (junto), palavra 2 f3448 × f3449,7 (−2 q), verbo do resultado f3457 × f3463,6 pela transcrição (−7 q) (corrigido na conferência: eram as palavras citadas), mas o envelope indica que a palavra começa ≈ f3457 (ver nota de sincronia): então o texto entra junto da voz.
  - saída: bloco inteiro, sem desfoque, 100 → 91 → 65 → 35 → 10 → 0 % (f3475–f3479; medido na correção), o 0 no último quadro do plano e corte seco em f3480 (corrigido na conferência: era 92 → 60 → 28 → 7 → 3 %).
  - letra (f3470, limiar 200): linha 1 sans x160–512 × y705–751 (com o descendente da 2ª palavra), maiúscula 37 px, haste 7 px, #f9f8fa; linha 2 serifada itálica bold x248–414 × y757–812, haste 8 px, #eae8de; centros x 46,7 % e 46,0 %.

## CONSTRUÇÃO
1. fundo: A-roll do rosto, sem alteração.
2. linha 1: sans semibold, maiúscula 37 px (2,9 %), #f9f8fa, centrada em x 46,7 %, topo y 55,1 %.
3. linha 2: o verbo do resultado sozinho, serifada itálica bold, corpo ≈ 1,15× a sans, #eae8de, centrada em x ≈ 46,5 %, topo y 59,1 %.
4. cada palavra: opacidade 0,04 → 0,33 → 0,75 → 0,99 → 1 (fade de 3 q depois de 1 quadro quase invisível) com desfoque leve que zera no 5º quadro; posição fixa (corrigido na conferência: era 0,14 → 0,4 → 0,71 → 0,87 → 0,96 → 1 em ≈ 6 q).
5. saída: bloco inteiro, sem desfoque, 1 → 0,91 → 0,65 → 0,35 → 0,10 → 0 em 5 q, o 0 no último quadro do plano e corte seco no seguinte (corrigido na conferência: era 1 → 0,92 → 0,6 → 0,28 → 0,07 → 0 em 4–5 q).
6. legenda amarela desligada no plano de rosto.
- Linha do tempo (ms a partir do corte para o rosto, f3445): +42 palavra 1 · +125 palavra 2 · +501 verbo do resultado (serif) · +667 bloco completo e nítido (corrigido na conferência: era +709) · +1251 fade-out · +1418 texto em 0 · +1460 corte seco para a cena (na conjunção da virada) (corrigido na conferência: eram as palavras citadas).
- Parâmetros que dependem do conteúdo: a frase de resultado (2–3 palavras); o verbo final em serif.
- O que NÃO fazer: fade longo de 6 q (a opacidade sobe em 3; o desfoque dura até o 5º quadro); saída de 4 q (são 5); manter a legenda amarela; pôr o verbo na linha 1; animar com escala; esticar o plano (é curto, 1,4 s).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "frase curta de resultado/virada" ; "o verbo do resultado" (serif itálica, sozinho na linha 2).
- Nesta referência as lacunas foram preenchidas com: "The experiment / failed."
- Receita de tratamento de cada imagem: sem imagem.
- Regra de escolha: virada curta (o fracasso que precede a descoberta) → rosto + texto grande.
- Receita de tratamento (reestudo 20/11): sem imagem.
- Teste de generalização: reel sobre Claude Code → "O deploy / *quebrou.*" antes da virada em que o erro vira descoberta; reel sobre café → "A safra / *perdeu-se.*" antes da virada da nova variedade.

- Confiança: tempos e posição medidos; início de "failed." incerto (transcrição × envelope).
