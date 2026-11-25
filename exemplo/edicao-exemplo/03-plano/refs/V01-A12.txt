# V01-A12 · pilha de 3 fotos de arquivo em P&B (contexto histórico)
- Categoria: P08 · Pilha de cartões (provisória do analista: (provisória) pilha de fotos impressas (montagem por empilhamento))
- Fonte: V01 quadros f550–f651 (22,92–27,13 s; 102 quadros ≈ 4250 ms) · 24 fps (continua por baixo de V01-A13/A14 até f777)
- Fala: "In the early 1950s, a diver in cold water wore a rubberized suit with thick"
- Tipo de fala: data (abre o capítulo histórico: época + quem + o quê)
- Gatilho: foto 1 em f550 = 22917 ms, +7 ms depois do início da palavra nº 76 "In" (22910 ms). Foto 2 em f576 = 24000 ms, −280 ms antes da nº 80 "a" (24280 ms; entra no fim de "1950s,"). Foto 3 em f610 = 25417 ms, −143 ms antes da nº 85 "wore" (25560 ms).
- Quadro-chave: f630
- Camadas ativas: cena de tela cheia | legenda | b-roll (fotos e vídeo de arquivo)
- Leitura dos strips: strip.jpg = quadros f548 a f557, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 10 células. strip-saida.jpg = quadros f574 a f583 (entrada da foto 2), mesma regra, 10 células. strip-geral.jpg = quadros f548 a f653, de 3 em 3, 36 células. Cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-grao-arquivo.jpg = quadro f630, região x360 y130 170x130 px, ampliada 3× sem suavizar, contraste ×6 em volta da média.

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala abre o passado ("no começo dos anos 1950"); toda data falada no vídeo puxa arquivo, e aqui cada meia-frase (época → quem → o que vestia) empilha uma prova.
- Por que este design: pilha de 3 fotos impressas, do geral para o detalhe, cada uma deslocada para deixar a anterior aparecer: "dossiê" de época que vai engrossando.
- Por que estas cores: preto e branco neutro de arquivo (#666467, grão cinza puro): o P&B sozinho já diz "antigamente", contra a cor das cenas do presente.
- Por que estes efeitos: borda de papel off-white com sombra curta entre as camadas; o grão é o da própria cópia de arquivo, com uma parte viva nos claros, re-sorteada a 12/s (alinhado ao reestudo).
- Por que este movimento: cada foto cai com estalo de 3 imagens em giro alternado (anti-horário, horário, anti-horário), como mãos jogando fotos numa mesa; a pilha deriva devagar.
- Sensação do movimento: ritmo de "e mais… e mais…" a cada ≈ 1,2 s; produzida por 3 entradas de 167 ms (112 → 103 → 100 %) a 12/s, intervalos de 1083–1417 ms e deriva de ±1 a 3 %/s.

## FORMA (fixa: reproduzir igual)
- Design (medido com med.py e inc.py, quadro cheio):
  - Foto 1 horizontal P&B com borda de papel off-white ≈ 8 px: assentada f556 x46–657, y177–675 = 612x499 px (85,0 % da largura, 39,0 % da altura), centro (50,4 %, 33,7 %), inclinada ≈ 1,4° anti-horário.
  - Foto 2 horizontal (vídeo P&B de arquivo), do mesmo tamanho, cai DESLOCADA PARA BAIXO (cobre os 2/3 de baixo da foto 1; a foto 1 fica visível só na faixa de cima): caixa do conjunto f581 x34–675, y160–779.
  - Foto 3 quase quadrada P&B, cai um pouco à esquerda e mais alta, com as duas anteriores aparecendo pela direita: conjunto f617 x28–697, y98–804 (93 % x 55 % do quadro); inclinação ≈ 2,2° anti-horário.
  - Giro ALTERNADO: foto 1 ≈ 1,4° anti-horário (f556: borda de cima y192 em x80 → y179 em x600), foto 2 ≈ 2,0° HORÁRIO (f600: y336 em x400 → y346 em x690), foto 3 ≈ 2,2° anti-horário (f630: y114 em x60 → y96 em x530). Fotos 1 e 3 giram para o mesmo lado; a 2 para o outro (remedido). Pilha sempre centrada horizontalmente. (medido)
- Movimento:
  - Foto 1: corte seco, maior, assenta em 3 imagens: largura f550 685 px (112 %) → f552 633 (103 %) → f554 610 (100 %) = 4 q de animação até o 1º quadro assentado (f554; perfil f556 já na deriva, 3,7) (remedido). Estalo. (medido)
  - Foto 2: entra em f576 maior e assenta em 3 imagens, 4 q (f576 → f580; perfil 26,3 · 9,6 · 6,7 · depois 3,5 só o vídeo) (remedido): base do conjunto f577 y785 → f579 y779. (medido)
  - Foto 3: entra em f610: topo do conjunto f611 y69 → f613 y89 → f615 y98 (assenta em 3 imagens = 4 q, f610 → f614; perfil 29,9 · 18,9 · 13,5 · depois 3,5) (remedido). (medido)
  - Pilha deriva devagar e o vídeo da foto 2 anda (diferença contínua). Cadência 12 imagens/s. (medido)
  - Saída: não sai; vira fundo das cenas V01-A13 e V01-A14 (disco e diagrama caem por cima) até o corte para o A-roll em f778. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | foto 1 | f550 | 4 q (167 ms) (remedido) | escala 112 → 100 % | estalo | nº 76, 1ª palavra da abertura da época | +7 ms |
  | foto 2 (mais baixa) | f576 | 4 q (167 ms) (remedido) | escala + cai por cima | estalo | nº 80, o personagem | −280 ms |
  | foto 3 (quadrada, à esq.) | f610 | 4 q (167 ms) (remedido) | escala | estalo | nº 85, o verbo que leva ao objeto | −143 ms |
- Ritmo: foto 1 sozinha 26 q (1083 ms); foto 2 no topo 34 q (1417 ms); foto 3 no topo até o disco cair (f652) 42 q (1750 ms). Intervalo entre fotos ≈ 1,1–1,4 s. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- Textura (reestudo 20/11):
  - Fundo: a mesa de V01-A01.
  - Bordas de papel: off-white #e5e3dd–#e7e3dc, luma 225–228, 6 px (`sombra` f630 x300–340, +13…+18), canto vivo; a borda de baixo da foto de trás aparece mais escura (luma 186–206, na sombra da de cima).
  - Imagens: família impressão de arquivo P&B com grão de filme: `textura` f630 em 330,140,180,90 (foto 3): #666467, grão 2,1, manchas 3,0, ac1 +0,50 (grão de 1–2 px), grão por canal 2,12/2,12/2,12 (cinza puro, sem sépia). No detalhe com realce: grão fino de filme + estrias horizontais claras (riscos/linhas de varredura da cópia). O grão anda com a foto (f630×f632 +0,25 → +0,70 alinhada), mas nos CLAROS há uma parte que muda a cada imagem. Teste novo na foto 1, parada (alinhado pela afim da foto, região 80,210,540,430, pixels lisos): f560×f561 (mesma imagem) resíduo 0,00–0,44; f560×f562 resíduo ÷ σ 0,84 nos claros (3,9 níveis) × 0,37 nos escuros e 0,32 nos médios (1,3 e 2,6 níveis); f566×f568 0,89 × 0,36 / 0,30. Nos escuros o resíduo é só interpolação; nos claros é 2,4 vezes maior → grão VIVO parcial nos claros, re-sorteado a 12/s (medido; corrigido na conferência: era "não é grão animado por cima").
- Efeitos (reestudo 20/11):
  - Sombra entre fotos (borda de baixo da foto 3 sobre a foto de trás, f630): logo depois da borda a foto de trás está a luma 59 e sobe para 89 em 9 px (−35 % no contato, ≈ 9 px). Sombra da pilha sobre a mesa: CAI PARA BAIXO (`sombra` alinhada, foto 1 sozinha, f560, caixa 46,177,612,499): embaixo −50 % no 1º px fora e volta em 14 px; direita −33 %, volta em 11 px; esquerda (perfil y380–480) 28 × 35 = −20 %, volta em ≈ 11 px; em cima −12 % só no 1º px (medido; corrigido na conferência: era "1–2 px a luma 17 (−45 %) junto à borda").
  - Vinheta da imagem (`borda` f630 na foto 3): luma 100 / 110 / 97 / 106 / 119 %, nitidez 100 → 56 %: sem vinheta; a queda de nitidez é da própria foto antiga (foco suave nas bordas).
  - Brilho, desfoque de movimento (entradas nítidas no strip), profundidade, grão global sobre a tela, aberração: nenhum.
- Câmera (reestudo 20/11): pilha com deriva lenta: `camera` f556→f574 (foto 1) ×1,0252 (+3,4 %/s), sobe 0,5 px/q; f616→f650 (foto 3) ×0,9856 (−1,0 %/s), vai 0,5 px/q para a esquerda e 0,4 para cima; fim, antes do disco cair, f640→f651 (0,0,720,820): ×0,9956 (−1,0 %/s), (−0,42; −0,26) px/q → o mesmo ritmo até a próxima peça (medido). A cada foto nova a deriva muda de sentido (aproxima, depois afasta). Fundo parado.
- Cadência (reestudo 20/11): 12 imagens/s nas entradas e na deriva; a foto 3 também tem movimento interno (filmagem de arquivo: `perfil` f620–f627 8,1 / 0,00 / 9,7 / 0,00 / 10,1 / 0,00 / 10,8 / 0,00), também a 12/s.
- Legenda nesta cena (reestudo 20/11): 6 blocos: a abertura da época (f550–f559, 3 palavras, troca no MESMO quadro do corte), a data sozinha (f560–f573, 1 palavra), o personagem (f574–f590, 2 palavras; a foto 2 entra 2 quadros depois, em f576), onde ele está + o verbo (f591–f616, 4 palavras), o verbo repetido + o adjetivo do objeto (f617–f639, 3 palavras; foto 3 entrou 7 quadros antes), o objeto + o começo da característica (f640–f664, 3 palavras, atravessa a queda do disco de V01-A13 em f652). Atrás da tarja: só a mesa (a pilha termina em y≈779–804) → tarja preta pura lida como preta (7 × 28; 74 % no vídeo, medida direta da conferência). Cor #ecdd50. Nenhum outro texto.

## CONSTRUÇÃO
1. fundo: mesa fixa.
2. foto 1 (horizontal P&B): x46–657 y177–675 (85 % × 39 %), centro 50,4 % × 33,7 %, −1,4° (anti-horário), borda off-white 6–8 px, sombra caída para baixo (embaixo −50 %, some em 14 px; dos lados −20/−33 %, 11 px; em cima só 1 px; corrigido na conferência: era "sombra de contato 1–2 px −45 %"); grão de filme da foto com uma parte viva nos claros (re-sorteada a 12/s, resíduo ≈ 3,9 níveis nos claros). Entrada 0 ms (f550): 112 % → 83 ms 103 % → 167 ms 100 %.
3. foto 2 (vídeo P&B, mesmo tamanho): entra em 1083 ms (f576) deslocada para baixo, cobrindo os 2/3 de baixo da foto 1; +2,0° (horário); 3 imagens de estalo (f576–f580).
4. foto 3 (quase quadrada P&B, com movimento interno): entra em 2500 ms (f610), um pouco à esquerda e mais alta, as de trás aparecendo pela direita; −2,2°; topo do conjunto y69 → y89 → y98 em 3 imagens. Sombra sobre a de trás ≈ 9 px −35 %.
5. deriva do conjunto: +3,4 %/s depois da foto 1; −1 %/s depois da foto 3; fundo parado.
6. a pilha fica por baixo das cenas seguintes (V01-A13, V01-A14) até o corte f778.
- Linha do tempo (ms a partir de f550): 0 foto 1 + legenda da abertura da época · 417 a data sozinha · 1000 o personagem · 1083 foto 2 · 1708 onde + verbo · 2500 foto 3 · 2792 verbo + adjetivo · 3750 objeto + característica · 4250 disco de V01-A13 cai por cima.
- Parâmetros que dependem do conteúdo: número de fotos (uma por meia-frase), proporção de cada uma, se é foto ou filmagem.
- O que NÃO fazer: sépia ou tom quente (é P&B neutro); grão de filme todo parado (nos claros das fotos uma parte do grão muda a cada imagem; corrigido na conferência: era "não fazer grão animado por cima da tela"); sombra igual em volta (cai para baixo); girar todas para o mesmo lado (alterna); fotos centradas uma exatamente sobre a outra (cada uma desloca para deixar a anterior aparecer).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "foto de época 1: o grupo/contexto" (abre o capítulo histórico).
  - "foto/vídeo de época 2: a ação".
  - "foto/filmagem de época 3, com movimento interno: o detalhe do equipamento/objeto antigo" (alinhado ao reestudo).
- Nesta referência as lacunas foram preenchidas com: mergulhadores dos anos 1950 numa mesa; mergulhadores entrando no mar (vídeo); dois homens com a roupa de borracha.
- Receita de tratamento de cada imagem: fotos e filmes de arquivo reais, preto e branco com grão, impressos com borda de papel ≈ 8 px e sombra caída para baixo (14 px embaixo, 11 nos lados, 1 em cima), giro de 1–2° alternando o lado, tamanho ≈ 85 % da largura. (reestudo 20/11) Medido: P&B neutro (#666467, grão por canal idêntico, sem sépia), grão de filme 2,1 níveis de 1–2 px com estrias horizontais da cópia, parte dele viva nos claros (resíduo ÷ σ 0,84–0,89 × 0,36 nos escuros), contraste médio-alto, foco suave nas bordas, sem vinheta aplicada; borda off-white 6 px luma ≈ 226; sombra entre fotos ≈ 9 px −35 %.
- Regra de escolha: a data/época na fala ("in the early 1950s") abre uma sequência de fotos de arquivo; cada nova meia-frase (quem → onde → o quê) empilha uma foto nova, do geral para o detalhe.
- Teste de generalização: (1) Claude Code: "nos anos 1970, programar era cartão perfurado" → foto P&B de uma sala de computadores, vídeo de alguém perfurando cartões, foto do cartão. (2) café: "no século 17, o café chegou à Europa" → gravura de uma casa de café, pintura do porto, foto antiga de um moinho.

- Confiança: tamanhos, inclinações e tempos medido; deslocamento relativo das fotos observado.
