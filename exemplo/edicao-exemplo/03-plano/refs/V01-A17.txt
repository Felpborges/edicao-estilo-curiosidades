# V01-A17 · pilha de 3 fotos de época (1 colorizada + 2 vídeos P&B)
- Categoria: P08 · Pilha de cartões (provisória do analista: (provisória) pilha de fotos impressas (montagem por empilhamento))
- Fonte: V01 quadros f1096–f1223 (45,67–50,96 s; 128 quadros ≈ 5333 ms) · 24 fps
- Fala: "Its frogmen had to stay in cold water for long stretches. And staying dry wasn't working."
- Tipo de fala: contexto (o grupo que sofria o problema e por que a solução falhava)
- Gatilho: corte seco em f1096 = 45667 ms, −103 ms antes da palavra nº 146 "Its" (45770 ms). Foto 2 em f1114 = 46417 ms, −3 ms da nº 148 "had" (46420 ms). Foto 3 em f1176 = 49000 ms, −20 ms da nº 157 "And" (49020 ms).
- Quadro-chave: f1150
- Camadas ativas: cena de tela cheia | legenda | b-roll (fotos/vídeos de época)
- Leitura dos strips: strip.jpg = quadros f1094 a f1103, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 10 células. strip-saida.jpg = quadros f1174 a f1183 (entrada da foto 3), mesma regra, 10 células. strip-geral.jpg = quadros f1094 a f1223, de 3 em 3, 44 células. Cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-colorizada.jpg = quadro f1105, região x90 y200 160x130 px, ampliada 3× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: depois do rosto dizer "a Marinha estava pior", a fala descreve o grupo e o problema; o editor responde com arquivo, uma imagem por meia-frase, do retrato do grupo para a ação.
- Por que este design: a mesma pilha de V01-A12 (fotos impressas caindo uma sobre a outra, mais baixas, giro alternado): repetir a forma diz "isto também é passado".
- Por que estas cores: a 1ª foto é colorizada em tons quentes desbotados (#998f7a), as 2 seguintes P&B: vai do retrato "humano" para o documento frio da falha.
- Por que estes efeitos: borda de papel e sombra caída para baixo (14–16 px embaixo); grão vivo parcial nos claros da foto 1 (alinhado ao reestudo).
- Por que este movimento: estalo de 3 imagens colado à 1ª palavra de cada meia-frase (−3 a −103 ms); a pilha quase não deriva até a foto 3, para não competir com os vídeos de dentro, e depois avança +4,1 → +3,4 %/s (alinhado ao reestudo).
- Sensação do movimento: relato documental, firme; produzida pelas entradas de 167 ms (113 → 104 → 100 %), intervalos longos (750–2583 ms) e deriva de −0,4 %/s até a foto 3, depois avanço de +4,1 → +3,4 %/s (alinhado ao reestudo).

## FORMA (fixa: reproduzir igual)
- Igual a V01-A12 na forma (conferido: borda de papel, entrada por escala de 3 imagens, cada foto nova cai por cima e mais baixa). Diferenças medidas abaixo.
- Design (quadro cheio, med.py/inc.py):
  - Foto 1 (colorizada, tons quentes desbotados): assentada f1101 x77–641, y192–735 = 565x544 px (78,5 % · 42,5 %), centro (49,5 %, 36,2 %), giro ≈ 1,2° horário.
  - Foto 2 (vídeo P&B), cai DESLOCADA PARA BAIXO, cobrindo os 2/3 de baixo da foto 1: conjunto f1119 x61–652, y130–786 (82 % · 51 %); giro ≈ 2,1° ANTI-horário (f1150: borda de cima y315 em x360 → y306 em x600), oposto ao da foto 1 (remedido, f1150).
  - Foto 3 (vídeo P&B), maior: conjunto f1181 x26–707, y80–764 (94,6 % da largura); giro leve anti-horário (observado em f1200). Giro alternado como em V01-A12: horário → anti-horário → anti-horário leve.
- Movimento:
  - Foto 1: largura f1097 636 (112,6 %) → f1099 587 (103,9 %) → f1101 565 (100 %) = 4 q até o 1º quadro assentado (f1096 → f1100; perfil 60,2 · 20,0 · 12,2 · depois ≈ 10 do vídeo) (remedido). Estalo. (medido)
  - Foto 2: entra em f1114; conjunto f1115 631x675 → f1117 599 → f1119 592 (3 imagens = 4 q, f1114 → f1118) (remedido). (medido)
  - Foto 3: entra em f1176; conjunto f1177 720 (sangra) → f1179 706 → f1181 682 (3 imagens = 4 q, f1176 → f1180; perfil 33,9 · 15,3 · 10,4 · depois 2,6) (remedido). (medido)
  - Vídeos dentro das fotos 2 e 3 correm (diferença contínua); deriva lenta da pilha até a foto 3, depois avanço de +4,1 → +3,4 %/s (alinhado ao reestudo). Cadência 12 imagens/s. (medido)
  - Saída: corte seco para o A-roll em f1224. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | foto 1 colorizada | f1096 | 4 q (167 ms) (remedido) | escala 113 → 100 % | estalo | nº 146, 1ª palavra da frase | −103 ms |
  | foto 2 vídeo, mais baixa | f1114 | 4 q (167 ms) (remedido) | escala + cai | estalo | nº 148, o verbo | −3 ms |
  | foto 3 vídeo, maior | f1176 | 4 q (167 ms) (remedido) | escala 106 → 100 % | estalo | nº 157, 1ª palavra da virada | −20 ms |
- Ritmo: foto 1 no topo 18 q (750 ms); foto 2 no topo 62 q (2583 ms); foto 3 no topo 48 q (2000 ms). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- Textura (reestudo 20/11):
  - Mesa: a de V01-A01.
  - Foto 1 (colorizada): família foto de arquivo colorizada, `textura` f1105 em 120,230,200,90: #998f7a (bege-oliva quente desbotado), grão 10,2, manchas 36 (conteúdo: rochas), ac1 +0,80, grão levemente azulado no canal B (10,7 × 10,2): cor pintada por cima de P&B, saturação baixa (detalhe-colorizada: tons chapados de colorização, sem grão de cor). Anda (+0,92 alinhada, com 6,5 px de deslocamento entre imagens: tem movimento interno). Teste novo (f1105×f1107, alinhado pela afim da foto, região 110,220,500,480, pixels lisos): claros resíduo ÷ σ 0,96 (3,4 níveis) × escuros 0,44 e médios 0,41 → grão VIVO parcial nos claros. (medido)
  - Fotos 2 e 3 (filmagens P&B): `textura` f1150 em 150,450,350,120: #605e61, grão 5,3 cinza puro, ac1 +0,81 (grão de filme grosso, comprimido). Teste novo: foto 3 f1200×f1202 (região 80,120,570,600): claros 0,68 × escuros 0,51 e médios 0,42 → sinal fraco de grão vivo nos claros; foto 2 f1150×f1152 inconclusivo (só 130 pontos de alinhamento, o vídeo de dentro mexe). (medido)
  - Bordas: off-white ≈ 7–8 px de canto vivo (como V01-A12).
- Efeitos (reestudo 20/11):
  - Vinheta da foto 1 (`borda` f1105): 100 / 91 / 89 / 88 / 93 %, nitidez 100 / 92 / 85 / 85 / 162 % → leve queda de 10 % para a borda, provavelmente da própria foto antiga (o anel externo inclui a borda de papel, por isso sobe); vinheta aplicada: nenhuma medida.
  - Sombras: CAEM PARA BAIXO (`sombra` 4 lados alinhada): foto 1 sozinha (f1105, caixa 77,192,565,544): embaixo −39 % no 1º px fora, volta em 14 px; esquerda −34 % e direita −31 %, voltam em 10–11 px; em cima −8 % só no 1º px. Foto 3 (f1200, caixa 26,80,681,684): embaixo −51 %, volta em 16 px; em cima −16 %, volta em 4 px; lados encostam na borda do quadro (não medidos). (medido; corrigido na conferência: era "sombras de contato curtas, como V01-A12")
  - Brilho, desfoque de movimento, profundidade, grão global, aberração: nenhum.
- Câmera (reestudo 20/11): deriva quase parada: `camera` na faixa visível da foto 1 f1124→f1170: ×0,9921 (−0,4 %/s), sobe 0,8 px/q. Depois da foto 3 a câmera muda de fase e AVANÇA: f1190→f1202 (0,0,720,820) ×1,0202 (+4,1 %/s), desce 0,28 px/q; fim f1211→f1223 ×1,0166 (+3,4 %/s), desce 0,22 px/q (medido; a nota antiga só tinha a 1ª fase). Fundo parado.
- Cadência (reestudo 20/11): 12 imagens/s (entradas em f1096/f1114/f1176 com 3 imagens cada; vídeos de dentro reamostrados a 12/s, como em V01-A12).
- Legenda nesta cena (reestudo 20/11): 6 blocos: o grupo + verbo (f1096–f1118, 3 palavras, MESMO quadro do corte; a foto 2 entra em f1114, dentro do bloco), a ação + lugar (f1119–f1135, 3 palavras), a continuação (f1136–f1157, 3 palavras), a palavra-chave da duração sozinha (f1158–f1175, 1 palavra), a virada (f1176–f1198, 3 palavras, MESMO quadro da foto 3), o fracasso (f1199–f1223, 2 palavras). Atrás da tarja: a mesa (a pilha termina em y≈764–786) → tarja preta pura lida como preta (74 % no vídeo, medida direta da conferência). Nenhum outro texto.

## CONSTRUÇÃO
1. fundo: mesa fixa.
2. foto 1 (colorizada, com movimento interno): x77–641 y192–735 (78,5 % × 42,5 %), +1,2° (horário), borda off-white 7–8 px, sombra caída para baixo (14 px embaixo a −39 %, 10–11 px dos lados a −31/−34 %, nada em cima), grão vivo parcial nos claros. Entrada 0 ms (f1096): 112,6 % → 83 ms 103,9 % → 167 ms 100 %.
3. foto 2 (filmagem P&B): cai em 750 ms (f1114) deslocada para baixo, cobrindo os 2/3 de baixo da foto 1, −2,1° (anti-horário); 3 imagens de estalo.
4. foto 3 (filmagem P&B), maior (94,6 % da largura, sangra na entrada): cai em 3333 ms (f1176), giro leve anti-horário; 720 → 706 → 682 px em 3 imagens.
5. câmera em 2 fases: até a foto 3, deriva ≈ −0,4 %/s subindo 0,8 px/q; da foto 3 (3333 ms) ao corte, avança +4,1 → +3,4 %/s descendo ≈ 0,25 px/q; fundo parado.
- Linha do tempo (ms a partir de f1096): 0 foto 1 + legenda (grupo + verbo) · 750 foto 2 · 958 legenda (ação + lugar) · 1667 legenda (continuação) · 2583 legenda (palavra da duração sozinha) · 3333 foto 3 + legenda (virada) · 4292 legenda (o fracasso) · 5333 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: quantas fotos, se a 1ª é colorida/colorizada, quais são filmagens.
- O que NÃO fazer: saturar a foto colorizada (é desbotada); deixar as filmagens a 24/s; pilha com deriva forte antes da última foto (é quase parada; depois dela avança ≈ +4 %/s); sombra igual em volta.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "quem sofria o problema": foto de época do grupo.
  - "o problema em ação": vídeo de época.
  - "a solução atual falhando": vídeo de época.
- Nesta referência as lacunas foram preenchidas com: homens-rã da Marinha nas pedras (colorizada); nadador na água gelada (vídeo); bote com homens-rã (vídeo).
- Receita de tratamento de cada imagem: arquivo real (foto colorizada ou filme P&B com grão), impresso com borda de papel ≈ 8 px, giro de 1–2°, 78–95 % da largura. (reestudo 20/11) Medido: colorizada em tons quentes desbotados (#998f7a, saturação baixa, cor chapada de colorização); filmagens P&B neutro com grão grosso de filme (5,3 níveis, ac1 +0,81); sem vinheta aplicada.
- Regra de escolha: frase sobre um grupo/instituição ("the navy had it worse") → fotos de época desse grupo, uma por meia-frase, do retrato para a ação.
- Teste de generalização: (1) Claude Code: "e as agências sofriam mais: equipes inteiras revisando código à mão" → foto de escritório antigo, vídeo de gente digitando, vídeo de tela cheia de erros. (2) café: "e os navios sofriam mais: meses no mar" → gravura de marinheiros, vídeo de um porão, vídeo do mar agitado.

- Confiança: tamanhos, giro e tempos medido; tons de cor observado.
