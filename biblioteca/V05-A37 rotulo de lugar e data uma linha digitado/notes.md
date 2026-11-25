# V05-A37 · rótulo de lugar e data (1 linha) digitado e apagado
- Categoria: P04 · Rótulo e número digitados sobre a cena (provisória do analista: (provisória) rótulo de documentário digitado e apagado letra a letra (variante de 1 linha))
- Fonte: V05 quadros f2499–f2551 (104,23–106,40 s; 53 quadros ≈ 2211 ms; f_in remedido de f2503 para f2499; f_out corrigido no reestudo de f2548 para f2551) · 23,976 fps
- Fala: "(In) Rome, Emperor Nero made wearing full purple (a crime)."
- Tipo de fala: lugar
- Gatilho: a 1ª letra aparece FRACA em f2499 (104 229 ms), 11 ms antes do início da palavra nº 352 "Rome," (104 240 ms), 4 quadros depois do corte (remedido: dif com limiar 15 contra f2498 já marca a letra "R" em f2499, x77–99; o branco pleno só chega em f2503). Medida antiga, só do branco pleno, com `med.py big` (pixels brancos > 200: 0 em f2502 → 44 em f2503 → 1302 em f2510).
- Quadro-chave: f2525
- Camadas ativas: b-roll 3D (A36) | grafismo (rótulo) | legenda
- Leitura dos strips: strip.jpg = quadros f2501 a f2512, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 12 células. strip-saida.jpg = quadros f2538 a f2550, de 1 em 1, 8 colunas; 13 células. detalhe-rotulo-letras.jpg = quadro f2525, região x70 y120 250x45 px, ampliada 3× sem suavizar. Folhas de entrada (f2497–f2512) e saída (f2539–f2549), de 1 em 1, recorte x70 y125 250x40, no scratchpad do reestudo, descritas em "Entrada do texto".

## LEITURA DE EDITOR
- Por que esta cena aqui: a anedota precisa de "onde e quando" sem gastar fala; o rótulo de documentário dá o contexto enquanto o narrador já conta a ação.
- Por que este design: 1 linha só (lugar + intervalo de anos), pequena, no canto de cima à esquerda, longe da legenda e do protagonista: informação de rodapé de documentário, não manchete.
- Por que estas cores: branco puro sem caixa sobre o fundo escuro do cenário.
- Por que estes efeitos: cada letra nasce desfocada e foca (e sai do mesmo jeito): "máquina de escrever macia".
- Por que este movimento: escrito da esquerda para a direita na palavra do lugar e apagado na mesma direção quase 1 s antes do corte, limpando a tela para o gesto final.
- Sensação do movimento: digitação rápida e suave; aparece e some como um carimbo de tempo, sem chamar mais atenção que a cena.

## FORMA (fixa: reproduzir igual)
- Design: UMA linha em sans branca (peso médio/semibold, menor que o nome de A10), sem linha cinza, sem caixa, alinhada à esquerda em x78 (10,8 %), y133–158 (10,4–12,3 % da altura), x78–307 (31,9 % da largura) (medido com `med.py white`). Diferença em relação a A10/A16: só lugar + data, numa linha, mais perto do canto (x 11 %, y 10 %).
- Movimento: digitação da esquerda para a direita, cada letra com fade + foco: 1ª letra fraca em f2499, 12 caracteres visíveis iniciados em 8 q (f2499–f2506, ≈ 1,5 por quadro), cada caractere levando 6 q de 0 a 100 % (opacidade integrada 12 → 31 → 51 → 68 → 84 → 99 %; miolo 6 → 15 → 29 → 52 → 79 → 99 %), último caractere nítido em f2511: 13 quadros ≈ 542 ms do 1º quadro ao assentado (medido na correção, miolo de cada letra × fundo de f2498, região x72 y126 245x38; o fim em f2511 confirma a remedição; corrigido na conferência: a cadência era ≈ 1,1 caractere por quadro e 3–4 q por caractere). Parado f2512–f2539. Apagamento da esquerda para a direita f2540–f2551 (borda esquerda do branco pleno anda x79 → 114 → 152 → 168 → 190 → 217 → 255 → 273 de f2540 a f2547, mas os últimos caracteres ainda ficam visíveis, fracos e desfocados, até f2550–f2551: 12 quadros ≈ 500 ms; medido na correção, por caractere: 100 → 73 → 42 → 8 → 0 % em 4 q, 12 caracteres iniciados em 8 q, f2540–f2547) (corrigido no reestudo, folha f2539–f2549 de 1 em 1 e `perfil` x200 y128 120x35 ativo até f2553; antes "f2540–f2548, 9 quadros", contado só no branco pleno).
- Ritmo: completo e parado 29 quadros ≈ 1,21 s (f2511–f2539; corrigido na conferência: era 28 q, f2512–f2539); sai antes do corte (19 quadros antes).
- Som: nenhum efeito detectado.

- Textura (reestudo 20/11): texto vetorial liso; fundo = foto desfocada da colunata (ver V05-A36), escura atrás do rótulo.
- Efeitos (reestudo 20/11): desfoque por letra na entrada, que dura até o 6º quadro da letra (medido na correção: o miolo da letra fica 13 a 22 pontos abaixo da opacidade integrada do 2º ao 4º quadro, 15/31, 29/51, 52/68; numa haste de 4 px o desfoque pesa mais que nos algarismos grandes), e leve na saída (miolo 5 a 17 pontos abaixo no fim de cada letra) (corrigido na conferência: era ≈ 3 px só no 1º/último quadro); sombra, caixa, contorno, brilho: nenhum (medido em f2525: a letra passa direto do branco para o fundo escuro).
- Câmera (reestudo 20/11): o rótulo é fixo na tela (não acompanha o push-in de +1,5 %/s da cena: `perfil` x70 y128 250x35 = 0,03–0,25 com o rótulo parado, f2537–f2543).
- Cadência (reestudo 20/11): 24 imagens/s (um estado novo por quadro na entrada e na saída).
- Legenda nesta cena (reestudo 20/11): a legenda amarela continua normal embaixo (tarja de 51 px, y 809–859, 68 %); o rótulo fica no topo (y 10,4–12,3 %), a 53 pontos de distância; não se tocam e não se alinham (rótulo à esquerda em x 10,8 %, legenda centrada).
- Entrada do texto (reestudo 20/11), folha f2497–f2512 de 1 em 1:
  - remedida na correção, caractere a caractere (12 caracteres visíveis; a 1ª palavra tem 4 letras e uma vírgula, depois 2 letras e 5 caracteres do intervalo de anos), opacidade integrada / miolo por quadro: 1º caractere f2499 12/6 → f2500 31/15 → f2501 51/29 → f2502 68/52 → f2503 84/79 → f2504 99/99 %; começos (≥ 10 %): 1 caractere em f2499, 2 em f2500, 2 em f2501, 1 em f2502, 1 em f2503, 2 em f2504, 3 em f2505–f2506; último nítido em f2511.
  - receita: cascata de ≈ 1,5 caractere visível por quadro (12 em 8 q; ≈ 1,75 contando os espaços), cada caractere leva 6 q de 0 a 100 % em rampa linear de ≈ +17 %/q, com desfoque que só some no 6º quadro; sem deslocamento, sem escala, sem cursor (corrigido na conferência: era ≈ 1,1 caractere por quadro e 3–4 q por caractere).
  - saída (folha f2539–f2549 e medida na correção com o fundo de f2555): espelho da entrada, da esquerda para a direita: o 1º caractere começa a apagar em f2540, a 1ª palavra some em f2543–f2544, o intervalo de anos fica sozinho de f2545 a f2547, o último caractere ainda tem 10 % em f2550, vazio em f2551; cada caractere perde opacidade em 4 q (100 → 73 → 42 → 8 → 0 %), com desfoque leve (corrigido na conferência: era ≈ 3 q e eram os caracteres citados).
  - cola na voz: 1ª letra 11 ms antes do nome do lugar; sai 1,0 s antes do corte (19 q de cena limpa no fim) (corrigido na conferência: era a palavra citada).
  - letra (f2525, limiar 200): caixa 26 px com vírgula (≈ 1,5 % de maiúscula ≈ 19–20 px), haste 4 px → ≈ 0,20 da maiúscula (semibold), 0,59 da caixa por caractere; cor #fefcf9; sans grotesca neo (SF Pro Display Semibold; alt. Inter SemiBold).

## CONSTRUÇÃO
1. rótulo: 1 linha, sans semibold, maiúscula ≈ 20 px (1,5 % da altura), branco #fefcf9, alinhado à esquerda em x 10,8 %, topo y 10,4 %; sem caixa, sem sombra; fixo na tela (não acompanha a câmera da cena).
2. entrada: cascata da esquerda para a direita, ≈ 1,5 caractere visível por quadro (≈ 28 ms por caractere); cada caractere opacidade 0,12 → 0,31 → 0,51 → 0,68 → 0,84 → 1 (6 q, linear) com desfoque ≈ 3 px que some no 6º quadro (corrigido na conferência: era 1 caractere a cada ≈ 0,9 q e 0 → 1 em 3–4 q).
3. saída: mesma cascata invertida, também da esquerda para a direita, cada caractere 1 → 0,73 → 0,42 → 0,08 → 0 em 4 q, com desfoque leve; 12 q no total.
4. legenda amarela V05-L01 embaixo, independente.
- Linha do tempo (ms a partir do corte de A36, f2495): +167 1ª letra (11 ms antes do nome do lugar; corrigido na conferência: era a palavra citada) · +667 rótulo completo e nítido (corrigido na conferência: era +709) · +1876 saída começa · +2336 vazio · +3003 corte.
- Parâmetros que dependem do conteúdo: o texto (lugar, intervalo de anos); o nº de caracteres define a duração (≈ 0,67 q por caractere visível + 5 q de foco; aqui 8 + 5 = 13 q) (corrigido na conferência: era ≈ 0,9 q por caractere + 3 q de foco); o lado (aqui à esquerda porque o protagonista está no centro e a cabeça dele sobe até y 8 %).
- O que NÃO fazer: digitação seca sem desfoque; caractere que acende em 3 quadros (leva 6); cascata lenta de 1 por quadro (aqui ≈ 1,5); cursor piscando; caixa ou tarja atrás; manter até o corte (sai antes); apagar da direita para a esquerda.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "lugar e período" (texto único).
- Nesta referência as lacunas foram preenchidas com: "Rome, AD 54–68" (o reinado de Nero).
- Receita de tratamento de cada imagem: sem imagem.
- Regra de escolha: localização no tempo. Ao citar um governante, o rótulo dá o lugar e os anos do reinado (dado que a fala não diz).
- Receita de tratamento (reestudo 20/11): sem imagem; o canto precisa ser escuro (fundo da cena desfocado) para o branco ler sem caixa.
- Teste de generalização: reel sobre Claude Code → "São Francisco, 2023–2025" no canto enquanto a cena mostra o escritório; reel sobre café → "Etiópia, séc. IX" no canto sobre a cena do pastor.

- Confiança: tempos e geometria medidos; peso da fonte observado.
