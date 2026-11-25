# V05-A31 · etiqueta de preço com número digitado (comparação em 2 linhas)
- Categoria: P04 · Rótulo e número digitados sobre a cena (provisória do analista: (provisória) etiqueta de dado sobre a cena: linha pequena (o quê) + número grande digitado, empilhada para comparar)
- Fonte: V05 quadros f2180–f2322 (90,92–96,89 s; 143 quadros ≈ 5964 ms) · 23,976 fps
- Fala: "(could) afford to fly a dye pricier than gold."
- Tipo de fala: comparação
- Gatilho: a 1ª linha pequena aparece em f2180 (90 924 ms), 116 ms antes do início da palavra nº 311 "afford" (91 040 ms). A 2ª etiqueta (ouro) começa ≈ f2230 (93 015 ms), 65 ms antes de "gold." (#318, 93 080 ms). Conferido no strip (f2180 linha pequena fraca; f2181 1º algarismo) e com `med.py big` (pixels do número a partir de f2184; 2º número a partir de f2234).
- Quadro-chave: f2260
- Camadas ativas: b-roll 3D (A30) | grafismo (etiqueta) | legenda
- Leitura dos strips: strip.jpg = quadros f2178 a f2193, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 16 células (1ª etiqueta). strip-saida.jpg = quadros f2228 a f2244, de 1 em 1, 8 colunas; 17 células (2ª etiqueta). strip-geral.jpg = quadros f2178 a f2322 (amostrado), 8 colunas. detalhe-etiqueta-letras.jpg = quadro f2260, região x85 y570 210x175 px, ampliada 3× sem suavizar. Folha de entrada quadro a quadro (f2178–f2189, recorte x80 y560 230x190) gerada no scratchpad do reestudo e descrita em "Entrada do texto".

## LEITURA DE EDITOR
- Por que esta cena aqui: "mais caro que o ouro" só convence com os dois números lado a lado; a etiqueta transforma a frase em prova.
- Por que este design: texto branco sem caixa escrito sobre o próprio produto, alinhado à direita na borda do tecido; o número do produto em corpo maior que o da referência, a diferença de tamanho já conta a comparação.
- Por que estas cores: branco quase puro (#fcf8f9) no número e branco levemente translúcido (#f3eaed) na linha do "o quê": hierarquia sem usar outra cor.
- Por que estes efeitos: cada algarismo nasce desfocado e transparente e foca em 5 quadros (corrigido na conferência: era 3): parece escrito na hora, mas suave, sem "máquina de escrever" seca.
- Por que este movimento: a 1ª etiqueta entra na palavra do verbo de valor ("afford") e a 2ª na palavra da referência ("gold"): o dado acompanha a fala.
- Sensação do movimento: contagem rápida e limpa, como um preço que vai aparecendo no visor; o foco que chega em cada dígito dá uma leve "batida" por caractere.

## FORMA (fixa: reproduzir igual)
- Design: texto branco sem caixa, sobre o objeto-tema na cor-tema, que acabou de se desenrolar na frente do móvel (x ≈ 40–300 × y ≈ 505–790 em f2260, observado; desenrola em f2174–f2181, o texto nasce sobre ele ainda no fim do movimento; remedido), ALINHADO À DIREITA em x284 (39,4 % da largura); bloco total x93–284 y576–739 (26,5 % × 12,7 % do quadro) em f2260 (medido com `med.py white`, limiar 215). 4 linhas:
  1. "o quê" 1: sans semibold pequena (alinhado ao reestudo), branca levemente translúcida, y576–598 (altura de linha 23 px ≈ 1,8 %);
  2. número 1: sans semibold GRANDE, y612–654 (≈ 43 px com vírgula; ≈ 3,3 %), largura x93–284;
  3. "o quê" 2: sans semibold ainda menor (alinhado ao reestudo), y682–699 (≈ 1,3 %);
  4. número 2: sans semibold médio, y712–739 (≈ 2,1 %), menor que o número 1.
  O número maior tem corpo maior: a diferença de tamanho mostra a comparação (o valor maior em corpo maior). Fonte por comparação: SF Pro Display (confiança média); alternativa: Inter.
- Movimento: linha pequena inteira com fade + foco de 5 q (f2180–f2184; medido na correção, miolo da letra × fundo local de f2178: 20 → 41 → 60 → 79 → 98 %) (corrigido na conferência: era ≈ 3 q, f2180–f2183); número DIGITADO da esquerda para a direita, 1 caractere novo por quadro (o 1º a 7 % em f2181 e a 21 % em f2182; o último começa em f2188) e cada caractere leva 5 q até 100 %, então o número só fica completo e nítido em f2192: 12 q ≈ 500 ms para 7 caracteres (corrigido na conferência: era f2181–f2189, ≈ 9 q, que contava os pixels > 215). 2ª etiqueta igual: linha pequena f2229–f2234 (10 → 20 → 42 → 64 → 81 → 99 %, medido na correção), número f2231–f2241 (11 q ≈ 459 ms; 1 caractere novo por quadro de f2232 a f2237, o último 100 % em f2241, medido na correção; corrigido no reestudo, `perfil` x85 y670 210x75: dif sobe de 0,05 em f2228 para 1,1 em f2229 e volta a 0,4 em f2242; antes "número f2232–f2240, observado"). Não há contagem animada de valor (os algarismos aparecem na ordem de escrita). Sem saída: fica até o corte f2323.
- Ritmo: etiqueta 1 completa e sozinha f2192–f2228 = 37 quadros ≈ 1,5 s; as duas completas juntas f2241–f2322 = 82 quadros ≈ 3,4 s (alinhado ao reestudo).
- Som: nenhum efeito detectado (lateral −120 dB de 90 a 96,9 s).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

- Textura (reestudo 20/11): texto vetorial liso, sem textura; suporte = tecido liso na cor-tema (#33262a na região medida, grão 0,76, parado) com variação vertical suave (ver V05-A30).
- Efeitos (reestudo 20/11): desfoque de entrada por caractere, que dura até o 5º quadro do caractere (medido na correção: no miolo da letra o 1º caractere fica 7 a 9 pontos abaixo da opacidade integrada nos 2 primeiros quadros, 21 × 30 % e 43 × 49 %, e empata a partir do 4º; nítido no 5º) (corrigido na conferência: era ≈ 3 px → 1 px → nítido no 3º quadro); nenhuma sombra, contorno, caixa ou brilho em volta do texto (medido em f2260: a letra passa direto do branco para o violeta do tecido); a linha pequena tem leve transparência (miolo #f3eaed contra #fcf8f9 do número).
- Câmera (reestudo 20/11): a etiqueta acompanha o recuo lento da cena (V05-A30); na janela f2226–f2228 a região do texto fica parada (dif 0,05), então não há movimento próprio da etiqueta.
- Cadência (reestudo 20/11): 24 imagens/s: um estado novo por quadro durante a digitação (`perfil` f2179–f2192 sem quadro repetido).
- Legenda nesta cena (reestudo 20/11): a legenda amarela continua normal embaixo (os blocos do plano de A30), tarja invisível sobre o preto (corrigido na conferência: eram as falas entre aspas); o texto da etiqueta fica 6 pontos acima (base da etiqueta y 57,9 %, topo da legenda y 64,1 %), alinhado à direita em x 39,4 %, enquanto a legenda é centrada: os dois textos não se alinham nem se tocam; a legenda NÃO some quando a etiqueta entra.
- Entrada do texto (reestudo 20/11; remedida na correção quadro a quadro no miolo de cada letra, com o fundo local tirado do quadro anterior à entrada, regiões x88 y572 202x30, x88 y605 202x55, x88 y676 202x28 e x120 y705 172x40):
  - linha pequena "o quê" 1: aparece inteira de uma vez, sem cascata: f2180 20 % → f2181 41 → f2182 60 → f2183 79 → f2184 98 → 100 % (5 q ≈ 208 ms, linear, ≈ +20 %/q); não é digitada (corrigido na conferência: era ≈ 50 → 75 → 75 → 100 %).
  - número 1 (7 caracteres): cascata de 1 caractere novo por quadro (≈ 42 ms), cada caractere leva 5 q: miolo 21 → 43 → 65 → 82 → 100 % (1º caractere, f2182–f2186), precedido de 1 quadro fraco (≈ 7 %); opacidade integrada 30 → 49 → 67 → 83 → 100 %; o desfoque só some no 5º quadro; sem deslocamento e sem escala (cada caractere nasce no lugar final); 1º caractere f2181 (fraco), último começa em f2188 e fica nítido em f2192 → 12 q ≈ 500 ms = 7 caracteres + 4 q de foco + 1 fraco (corrigido na conferência: era 30 → 70 → 100 % em 3 q e f2181–f2189).
  - 2ª etiqueta: a mesma receita, linha pequena f2229–f2234 (10 → 20 → 42 → 64 → 81 → 99 %), número f2231–f2241 (6 caracteres, 1 por quadro de f2232 a f2237, cada um 16 → 40 → 62 → 81 → 100 %; 11 q).
  - Não há cursor. Não há saída: tudo some no corte seco.
  - Cola na voz: 1ª linha 116 ms antes do verbo de valor; 2ª etiqueta 65 ms antes da palavra da referência (corrigido na conferência: eram as palavras citadas).
  - Letra (medida em f2260 com limiar de luma 170): número 1 = altura dos algarismos 34 px (2,7 % da altura), haste 7 px → peso 0,21 da altura (semibold/bold), largura 0,81 da altura por caractere (algarismos tabulares largos); número 2 = 30 px, haste 6 px (0,20), 0,75 por caractere; linha pequena 1 = caixa 24 px com ascendente e descendente, haste 3 px (≈ 0,23 da altura-x de ≈ 13 px: semibold), 0,46 da caixa por caractere; linha pequena 2 = 19 px, haste 3 px. Família: sans grotesca neo (SF Pro Display Semibold; alternativa Inter SemiBold).

## CONSTRUÇÃO
1. suporte: o objeto na cor-tema da cena (aqui um tecido liso desenrolado), região x 6–42 %, y 40–62 %.
2. linha pequena 1: sans semibold, caixa 24 px (1,8 %), cor #f3eaed (branco ≈ 92 %), alinhada à direita em x 39,4 %, topo em y 45,0 %; a linha inteira de uma vez, opacidade 0,20 → 0,41 → 0,60 → 0,79 → 0,98 → 1 (linear) com desfoque leve que some no 5º quadro.
3. número 1: sans semibold, algarismos 34 px (2,7 %), #fcf8f9, alinhado à direita em x 39,4 %, topo y 47,8 %; caracteres entram em cascata de 1 por quadro (42 ms), cada um com opacidade ≈ 0,07 (1 q fraco) → 0,30 → 0,49 → 0,67 → 0,83 → 1 e desfoque ≈ 3 px que some no 5º quadro (corrigido na conferência: era 0,3 → 0,7 → 1 e 3 → 1 → 0 px em 3 quadros).
4. linha pequena 2: 19 px, mesma cor e alinhamento, topo y 53,3 %.
5. número 2: 30 px, topo y 55,6 %, mesma cascata e mesma curva por caractere.
6. legenda amarela V05-L01 embaixo, centrada, independente.
- Linha do tempo (ms a partir do corte de A30, f2144): +1501 linha 1 (cheia em +1668) · +1543 1º caractere do número 1 (fraco) · +2002 número 1 nítido (corrigido na conferência: era +1877) · +3546 linha 2 (cheia em +3754) · +3629 1º caractere do número 2 (corrigido na conferência: era +3587) · +4046 número 2 nítido · +7466 corte seco (sem saída animada).
- Parâmetros que dependem do conteúdo: o texto das 2 linhas pequenas e dos 2 números; o número de caracteres (a duração da digitação é 1 q por caractere + 4 q de foco, mais 1 q fraco no começo) (corrigido na conferência: era + 2 q de foco); qual número fica em corpo maior (o de maior valor, que é o do sujeito da frase).
- O que NÃO fazer: digitação seca sem o desfoque por caractere; caractere que acende em 3 quadros (cada um leva 5, em rampa linear de ≈ +20 %/q); linha pequena com fade rápido de 3 q (são 5); contador animado (0 → 150 000); caixa ou sombra atrás do texto; centralizar (é alinhado à direita na borda do suporte); tirar a legenda amarela enquanto a etiqueta está na tela.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "item 1 e unidade" (linha pequena); "valor 1" (número grande); "item de comparação e unidade"; "valor de comparação" (número menor).
- Nesta referência as lacunas foram preenchidas com: "Purple silk, 1 lb" / "150,000" / "Gold, 1 lb" / "72,000".
- Receita de tratamento de cada imagem: sem imagem; tipografia branca sobre a cena, ancorada no objeto de que se fala.
- Regra de escolha: número + comparação. Quando a fala compara preço/medida com uma referência conhecida ("pricier than gold"), mostram-se os 2 números empilhados, o maior em corpo maior; a 2ª etiqueta entra na palavra da referência.
- Receita de tratamento (reestudo 20/11): sem imagem; o texto é escrito sobre a superfície do objeto citado, que precisa ser escura ou média e lisa (aqui violeta escuro, luma ≈ 41) para o branco ler sem caixa.
- Teste de generalização: reel sobre Claude Code → sobre a tela escura de um notebook em cena: "Equipe humana, 1 mês / 20.000" e embaixo, menor, "Assinatura, 1 mês / 1.000"; reel sobre café → sobre a saca escura: "Café raro, 1 kg / 1.200" e "Café comum, 1 kg / 40".

- Confiança: geometria e tempos da etiqueta 1 medidos; tempos da etiqueta 2 medidos na correção (eram observados, ±2 quadros); valores lidos no quadro.
