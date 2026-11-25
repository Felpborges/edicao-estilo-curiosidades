# V01-A34 · disco de células fechadas: células "se selam", água encosta por cima, uma célula circulada à mão
- Categoria: P18 · Diagrama chapado com estados (provisória do analista: (provisória) diagrama de estrutura (padrão de células) dentro de disco com aro, com estados e marcação à mão)
- Fonte: V01 quadros f2366–f2490 (98,58–103,75 s; 125 quadros ≈ 5208 ms) · 24 fps
- Fala: "bubbles of gas. Each one sealed off from the next. Water can't get into a sealed bubble."
- Tipo de fala: mecanismo
- Gatilho: assenta em f2366 = 98583 ms, +83 ms depois do início da palavra nº 320 "bubbles" (98500 ms) (chega pela lupa de V01-A33).
- Quadro-chave: f2460
- Camadas ativas: cena de tela cheia (foto atrás) | grafismo animado | legenda
- Leitura dos strips: strip.jpg = quadros f2392 a f2410 (as células se selam), de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 19 células. strip-saida.jpg = quadros f2464 a f2480 (círculo à mão), mesma regra, 17 células. strip-geral.jpg = quadros f2364 a f2490, de 3 em 3, 43 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-agua-gotas-circulo.jpg = quadro f2488, região x200 y180 320x220 px, ampliada 2× sem suavizar.


## LEITURA DE EDITOR
- Por que esta cena aqui: a fala explica a propriedade-chave ("cada uma selada") e a consequência ("a água não entra"); o diagrama mostra as duas coisas no mesmo palco, uma depois da outra.
- Por que este design: o disco que a lupa acabou de abrir vira o palco; as células ganham parede dupla (selada) e a água encosta por cima sem entrar: a regra vira imagem.
- Por que estas cores: escuro/creme do material e teal da água, o código do vídeo; o amarelo à mão é a única cor de "atenção" e aponta UMA célula.
- Por que estes efeitos: gotas com reflexo e traços claros de ondulação dizem "água" sem texto; o círculo amarelo translúcido e torto é a anotação do professor.
- Por que este movimento: cada estado chega na sua palavra (parede dupla em "each", água em "water", círculo em "sealed"); entre eles o palco só aproxima devagar.
- Sensação do movimento: lição em três toques, cada um um pequeno "clique" de mudança; a aproximação acelera (+1,6 → +5,9 %/s) até perto do círculo e, no fim, o palco recua (−5,0 → −7,6 %/s) e sobe ≈ 30 px (alinhado ao reestudo).

## FORMA (fixa: reproduzir igual)
- Design (quadro cheio):
  - Disco ≈ 90 % da largura com aro creme fino, cheio das unidades da estrutura: polígonos arredondados de miolo escuro #2e2a24 (f2420, 340,500) com paredes creme claras; a foto do material continua atrás pelas bordas (caixa do conjunto f2380 x17–703, y178–765 = 687x588 px). (cor medido; caixa medido com med.py) Disco em f2460: borda externa x≈39–675, y≈203–839 = diâmetro ≈ 636 px (88 % da largura, 50 % da altura), centro ≈ (357, 521) px = (49,6 %, 40,7 %) (medido, remedição f2460, varredura na linha y520 e na coluna x360; em f2366, fim da lupa A33, ≈ 583 px / 81 %: o disco ainda cresce com a câmera).
  - Propriedade de cada unidade: cada unidade ganha um 2º contorno interno (parede dupla). (observado)
  - Agente de fora que não entra: faixa teal escura #284c54 (f2440, 360,230) no topo do disco, com bolinhas claras, encostando nas unidades sem entrar. (cor medido; forma observado)
  - Círculo à mão amarelo-mostarda (traço de V01-A15) em volta de UMA unidade da borda de cima. (observado)
- Movimento (perfil, região x60 y170 600x620; cadência 12 imagens/s fase par):
  - A região muda o tempo todo (diferença 5–14 por imagem), pela câmera: o padrão das unidades é rígido (alinhado ao reestudo). f2396–f2414: ganham a parede dupla (diferença sobe 8 → 14 → 9). (medido)
  - f2418–f2442: grande mudança contínua (diferença 13 → 32,6 no pico f2430 → 26): as unidades se reorganizam e a faixa do agente entra por cima (f2438–f2444). (medido; o que muda observado)
  - f2466–f2480: círculo à mão + o palco começa a recuar e subir (diferença 11 → 38) (alinhado ao reestudo). (medido)
  - Saída: a foto de V01-A35 cai por cima em f2491. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | disco da estrutura assenta | f2366 | — | (fim da lupa A33) | — | nº 320 | +83 ms |
  | unidades ganham parede dupla (a propriedade) | f2396 | ≈ 18 q (750 ms) | contorno interno cresce | acelera e desacelera | nº 323 (99840) | −7 ms |
  | o agente de fora entra no topo | f2438 | ≈ 6 q (250 ms) | faixa desce do topo | estalo | nº 330 (101790) | −207 ms |
  | círculo à mão numa unidade | f2470 | ≈ 6 q (250 ms) | traço se revela | desacelera | nº 335 (102980) | −63 ms |
- Ritmo: 5208 ms. Parado final = 0 (o último passo, círculo à mão + unidades, ainda anda na saída: diferença 29,6 em f2490). Mas há um trecho quase parado logo depois da entrada, f2370–f2394 ≈ 1000 ms, com diferença 3,2–5,0 por imagem (é a aproximação lenta da câmera, +1,6 %/s; o padrão de células fica rígido, correlação +0,99 entre f2380 e f2382: corrigido no reestudo; antes "só o tremor de stop-motion") (remedido, perfil f2366–f2492). A tabela de tempo em tela da análise dá 583 ms, que não bate com nenhum dos dois. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Células: miolo escuro #2e2a24, paredes creme com grão; padrão RÍGIDO (f2380 × f2382: correlação +0,99, região 300,500,80,80): as células não fervem; a "respiração" de 3–5 por imagem da nota antiga é a aproximação lenta da câmera. Teste novo (f2460×f2462, afim do disco, pixels lisos): claros resíduo/σ 0,74, correlação +0,69; escuros 0,88, +0,57; par idêntico f2460×f2461: 0,05 → PARADO, sem grão vivo (mesmo veredito; a conferência mediu +0,83…+0,90 e 0,69). É um dos diagramas chapados do vídeo SEM grão vivo.
  - Agente de fora (faixa teal escura) com grão, #224b51–#29545b (L68–76, f2460); na região 120,225,120,40 grão 14,2 (inclui os traços claros), grão cinza (13,95/14,20/14,48); anda com a peça (+0,94 depois de alinhar). Traços horizontais claros curtos (ondulação) e gotas semitransparentes mais claras com reflexo curvo branco, pousadas na linha das células (detalhe).
  - Círculo à mão: amarelo translúcido, ≈ 7–8 px (linha y330, f2488: x376–383), sobre a célula escura lê #8f8b28–#958c15 (≈ 55 % de opacidade), forma torta com as pontas sobrepostas.
- Efeitos (reestudo 20/11):
  - Brilho: reflexos curvos nas gotas.
  - Sombra do disco (medido, f2460, perfil alinhado e linhas y500–540): à esquerda −39 % no contato (22 contra 36), volta ao fundo em ≈ 14 px; em cima −18 %, volta em 13 px (= conferência); embaixo a borda do disco (y≈839) encosta na faixa da legenda e não se mede; à direita fica a foto de trás. É a sombra herdada da lupa de V01-A33, mais forte dos lados que em cima (corrigido na conferência: era "nenhuma nova", sem número).
  - Vinheta, borda borrada, desfoque de movimento, aberração: nenhum (medido em f2460). Grão global: nenhum; e aqui o diagrama também não tem grão vivo (ver Textura).
- Câmera (reestudo 20/11): o disco aproxima e acelera, para e RECUA no fim: f2370 → f2384 escala ×1,0095 (+1,6 %/s), centro (−0,04, −0,07 px/q), giro 0,00°; f2446 → f2460 ×1,0337 (+5,9 %/s), centro (−0,18, +0,86 px/q), giro 0,00°; f2458 → f2470 +2,3 %/s (medido na conferência); f2464 → f2470 ×1,0001 (parado, sobe 0,84 px/q); f2470 → f2476 −5,0 %/s, sobe 2,13 px/q; f2476 → f2488 ×0,9614 (−7,6 %/s), centro (+0,15, −2,49 px/q) = sobe 30 px; f2482 → f2488 −7,5 %/s (medido, região 0,0,720,830, sem a faixa da legenda) (corrigido na conferência: era "aproxima e acelera" até o fim; a conferência mediu −7,5 %/s e 34 px em f2476 → f2488). O recuo começa em ≈ f2470, junto do círculo à mão. A foto de trás (V01-A32) continua aparecendo nas laterais. Mesa parada.
- Cadência (reestudo 20/11): 12 imagens/s (perfil do topo do disco f2463–f2490: 0,07 / 5,6 / 0,03 / 6,2 / 0,17 / 5,6 / 0,04 / 7,0 … / 0,22 / 10,0; quadros pares mudam).
- Legenda nesta cena (reestudo 20/11): 6 blocos: o 1º (3 palavras, o nome da unidade da estrutura) entra no quadro em que a lupa assenta (f2366); o último (1 palavra; f2479–f2489) termina 1 quadro antes de a foto de V01-A35 cair; o bloco que entra em f2490 já é da cena seguinte. Texto #e7dd53, 68 %. Atrás da tarja: a mesa (a borda de baixo do disco fica em y≈835–839, 8–12 px acima da tarja). Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %, estimativa grosseira). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #181516, parada.
2. foto de trás (V01-A32) visível nas laterais, parada atrás do disco.
3. disco/palco: herdado da lupa (aro creme fino + sombra: −39 % no contato dos lados, some em ≈ 14 px; −18 % em cima, 13 px), Ø ≈ 583 px em f2366 crescendo para ≈ 636 px (88 %) em f2460, centro ≈ (49,6 %, 40,7 %).
4. unidades da estrutura: polígonos arredondados escuros #2e2a24 em paredes creme granuladas, SEM grão vivo (padrão parado, anda só com a câmera); em 1250–2000 ms cada unidade ganha um contorno interno creme fino (parede dupla), crescendo de dentro com aceleração e freada.
5. agente de fora: faixa teal escura #224b51–#29545b no topo do disco, com traços claros horizontais e 3 gotas semitransparentes com reflexo; desce do topo com estalo em ≈ 250 ms e pousa na linha das unidades sem entrar.
6. círculo à mão: amarelo translúcido ≈ 55 %, traço ≈ 7–8 px, torto, Ø ≈ 90–110 px, em volta de uma unidade da 1ª fileira; revelado como traço em ≈ 250 ms, desacelerando.
7. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Linha do tempo (ms a partir do assentamento da lupa, f2366 = 98583 ms): 0 palco pronto + 1º bloco de legenda · 0–1000 ms quase parado (só aproximação +1,6 %/s) · 1250 ms paredes duplas · 2167–2667 ms reorganização (pico em 2667 ms) · 3000 ms o agente de fora desce · 3333–3917 ms aproximação acelera (+5,9 %/s) · 3833–4333 ms freia (+2,3 %/s) e para · 4167 ms círculo à mão · 4333–5083 ms RECUA, acelerando de −5,0 a −7,6 %/s, e sobe ≈ 2,1–2,5 px/q (≈ 30 px) (corrigido na conferência: era "4167–5208 ms aproximação acelera") · 5208 ms foto de V01-A35 cai por cima.
- Parâmetros que dependem do conteúdo: a propriedade que as unidades ganham (parede dupla aqui), o agente de fora (aqui, faixa com gotas), qual unidade é circulada.
- O que NÃO fazer: fazer as unidades ferverem ou pôr grão vivo no diagrama (aqui ele é parado), pôr o agente de fora entrando entre as unidades, terminar aproximando (o fim recua −7,5 %/s e sobe ≈ 30 px), círculo amarelo opaco ou perfeito, mudar estados sem palavra-gatilho, câmera parada.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "a estrutura microscópica": padrão repetido de unidades.
  - "a propriedade de cada unidade": um detalhe gráfico que aparece em todas (aqui parede dupla).
  - "o agente de fora que não entra": faixa de cor que encosta.
  - "a unidade-exemplo": a que se circula.
- Nesta referência as lacunas foram preenchidas com: células de espuma; selada; água; uma bolha.
- Receita de tratamento de cada imagem: padrão vetorial chapado (creme + quase preto), parado, sem respiração nem grão vivo, anda só com a câmera (alinhado ao reestudo), faixa teal escura com bolhas, círculo amarelo à mão.
- Regra de escolha: a fala explica a microestrutura em 3 frases (o que é → propriedade → consequência) e cada uma acende um estado no mesmo disco.
- Teste de generalização: (1) Claude Code: disco cheio de "blocos de memória"; cada um ganha um cadeado (isolado); uma faixa vermelha "ruído" encosta e não entra; círculo num bloco. (2) café: disco cheio de células do grão; cada uma ganha óleo dentro; a água encosta; círculo numa célula.
- Receita de ILUSTRAÇÃO (reestudo 20/11): padrão de unidades escuras com contorno interno claro (parede dupla) em paredes de papel creme granulado; agente de fora como faixa teal escura com traços curtos claros e gotas translúcidas com reflexo; anotação à mão em amarelo translúcido ≈ 55 %, ≈ 7–8 px, torta; tudo dentro do disco herdado da lupa; estados revelados por crescimento do contorno, descida da faixa e traço à mão.
- Teste de generalização (reestudo 20/11): (1) Claude Code: "cada sessão fica isolada; um pedido de fora não entra numa sessão fechada" → disco de blocos escuros que ganham contorno duplo, faixa teal de "pedidos" encosta por cima sem entrar, círculo amarelo num bloco. (2) café: "cada célula do grão é fechada; a água não entra numa célula selada" → disco de células do grão com parede dupla, faixa de água com gotas por cima, círculo numa célula.

- Confiança: cores, tempos e intensidade de movimento medido; formas e conteúdo de cada passo observado.
