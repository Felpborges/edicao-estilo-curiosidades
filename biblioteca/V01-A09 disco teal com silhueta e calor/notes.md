# V01-A09 · disco teal (água) com silhueta humana creme; calor laranja nasce no peito
- Categoria: P18 · Diagrama chapado com estados (provisória do analista: (provisória) diagrama em disco: silhueta + estado (calor) sobre fundo de cor)
- Fonte: V01 quadros f333–f375 (13,88–15,63 s; 43 quadros ≈ 1792 ms) · 24 fps · por cima de V01-A08
- Fala: "the water in keep you warm?"
- Tipo de fala: pergunta (2ª metade da pergunta central: o resultado que parece impossível)
- Gatilho: entra em f333 = 13875 ms, −125 ms antes da palavra nº 48 "water" (14000 ms). Calor começa em f359 = 14958 ms, +298 ms depois da palavra nº 50 "keep" (14660 ms) e −222 ms antes da nº 52 "warm?" (15180 ms).
- Quadro-chave: f370
- Camadas ativas: cena de tela cheia | grafismo (diagrama) | legenda
- Leitura dos strips: strip.jpg = quadros f331 a f340, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 10 células. strip-saida.jpg = quadros f355 a f370 (o calor crescendo), mesma regra, 16 células. Cada célula traz o nº do quadro e o tempo. Detalhes do reestudo: detalhe-calor-aneis.jpg = quadro f370, região x260 y250 200x320 px, ampliada 2× sem suavizar · detalhe-borda-silhueta.jpg = quadro f370, região x190 y370 90x110 px, ampliada 3× sem suavizar · detalhe-teal-ondas.jpg = quadro f370, região x30 y330 200x100 px, ampliada 3× sem suavizar, contraste ×6 em volta da média.

## LEITURA DE EDITOR
- Por que esta cena aqui: na 2ª metade da pergunta ("…mantém você quente?") o editor joga por cima da foto um diagrama-síntese: corpo dentro da água e o calor acendendo, a pergunta desenhada.
- Por que este design: disco maior que a tela (sangra dos lados) com silhueta chapada no meio: símbolo, não foto; o sujeito genérico vale para qualquer pessoa.
- Por que estas cores: teal = água (código fixo do vídeo), creme = corpo/papel, laranja = calor; o laranja é a cor mais quente e saturada do trecho e cai exatamente no peito.
- Por que estes efeitos: o calor é um degradê granulado (pontilhado) com anéis concêntricos na borda, como onda de calor; o halo escuro em volta da silhueta a descola do teal; as ondas finas claras dizem "água" sem desenhar água.
- Por que este movimento: o disco bate em 2 imagens (estalo) sobre a foto; o calor nasce de um ponto e cresce em ≈ 6 imagens, acelerando e assentando; a câmera avança devagar.
- Sensação do movimento: "acendeu", um calor que se espalha de dentro para fora; produzida pela mancha radial crescendo de ≈ 10 px a ≈ 200 px em 417 ms (diferença 7,5 → 11,8 → 7 por imagem) a 12/s, sobre zoom +5 %/s.

## FORMA (fixa: reproduzir igual)
- Design:
  - Disco teal #388690 (f345, 120,700) com linhas finas claras onduladas horizontais (marcas que caracterizam o meio, observado), maior que a largura: a linha mais larga ocupa os 720 px (corta nas laterais) e a cor vai de y≈115 a y≈840 (9,0–65,6 % da altura) em f339–f357 (remedido, f345: y115–846; o topo estava como y≈130) e de y107 a y865 (8,4–67,6 %) em f370 (remedido, f370). A foto de trás (V01-A08) continua aparecendo nas pontas de cima e de baixo. (medido com disco.py)
  - Silhueta do sujeito chapada creme #e5dccb (f345, 360,450) com grão de papel, de frente, centrada; sem contorno. (medido / observado)
  - Estado prometido: mancha laranja em degradê radial suave no centro da parte de cima do sujeito, núcleo saturado e borda que se dissolve no creme (#e8c38e em f370, 360,500 é a zona média). Sem contorno. (medido / observado)
- Movimento:
  - Entrada: pop em 2 imagens: linha mais larga f333 646 px (89,7 %) → f335 720 (passa da tela). Curva de estalo. (medido)
  - Deriva: o disco desce/cresce devagar (linha mais larga desce de y425 para y350 entre f345 e f375). (medido)
  - Estado prometido: cresce de f357 a f367 (5–6 imagens ≈ 417–500 ms), diferença por imagem na região central do sujeito 7,5 → 11,8 (pico f361–f367) → 7; depois pulsa leve (≈ 6–7). (medido no perfil, região x250 y350 220x400)
  - Saída: corte seco para o A-roll em f376. (medido)
  - Cadência: 12 imagens/s. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | disco + silhueta | f333 | 4 q (167 ms) | escala 90 → 100 % | estalo | nº 48, o meio nomeado | −125 ms |
  | estado prometido (mancha) no centro do sujeito | f357 | ≈ 10 q (417 ms) | mancha radial cresce do centro | acelera e desacelera | nº 50, o verbo do estado prometido | +298 ms (no quadro f359) |
- Ritmo: 1792 ms na tela; o estado fica completo e parado de f367 a f375 (≈ 375 ms) antes do corte. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Disco teal: família tinta chapada com papel leve: `textura` f370 em 60,520,140,80: #35828c, grão 0,74, manchas 0,85, ac1 +0,62, grão cinza; quase liso, com manchas largas fracas (detalhe-teal-ondas com realce: mosqueado de 10–30 px). f370×f371 +0,68 (mesma imagem), f370×f373 +0,40 → muda pouco de imagem para imagem (fervura fraca, muito menor que a do disco creme). Teste novo (f365×f367, região 40,450,160,250, pixels lisos de luma 60–150): σ 0,83 e resíduo 0,72 níveis, resíduo ÷ σ 0,87 → no piso da compressão: PARADO na prática. (medido)
  - Ondas do meio: linhas claras de ≈ 4 px (coluna x130: luma 105 → 130 → 105, y361–365), branco translúcido ≈ 20 % sobre o teal, levemente onduladas, horizontais, espaçadas ≈ 120 px.
  - Silhueta: família papel com fibra (creme), `textura` f370 em 295,660,40,90: #e3daca, grão 7,0, manchas 7,7, ac1 +0,75, grão quente (B/G/R 6,2/6,7/8,3), VIVA nos claros (corrigido na conferência: era "PARADA (f370×f371 +0,79; f370×f373 +0,72): o papel da silhueta não ferve"; a correlação simples misturava a borda). Teste novo (alinhado pela cena 0,0,720,820, pixels lisos do tronco 300,450,120,250): f345×f346, mesma imagem, resíduo 0,00; f345×f347, imagem seguinte, resíduo 4,59 com σ 2,83 (resíduo ÷ σ 1,62); f345×f351 1,51; pés f371×f373 1,37. O teal no mesmo par fica em 0,72 níveis (piso). O papel creme da silhueta ferve a 12/s como o disco creme; o teal não. (medido)
  - Calor: degradê granulado, `textura` f370 em 320,300,80,80: #d97028, grão 1,1, manchas 4,6; no detalhe-calor-aneis o degradê é pontilhado (grãos laranja espalhados no creme, como spray), com anéis concêntricos finos na borda de baixo (ondas de calor).
- Efeitos (reestudo 20/11):
  - Halo escuro em volta da silhueta: é halo de verdade, igual em cima e dos lados (f345): acima da cabeça (colunas x350–370) o teal desce de 102 para 77 nos 15 px junto à borda (−24 %); à esquerda (linhas y400–420) 113 → 91 em ≈ 14 px (−19 %); à direita 112 → 86 em ≈ 15 px (−23 %); embaixo não medível (os pés encostam na tarja). Sem deslocamento (medido em 3 lados; antes só na linha y400). Borda da silhueta: 1 px claro (216) e logo dentro 197–209; transição em 2–3 px (detalhe-borda-silhueta: borda limpa, levemente macia).
  - Degradê radial do calor: núcleo #d96826 (luma 124, y360) → #e88b34 (y440) → #d5a564 (borda, x300 y420) → creme #e4cfae (y520). Sem contorno.
  - Disco teal sem sombra própria medível: na borda de cima (colunas x120–180, f345) o teal encosta numa faixa clara de 8 px e logo acima vem a parte escura da foto de baixo (luma 21–22), onde uma sombra não apareceria; a foto de baixo aparece em cima e embaixo. (medido)
  - Vinheta, brilho, desfoque de movimento, profundidade, grão global, aberração: nenhum (f370).
- Câmera (reestudo 20/11): zoom in contínuo do disco + silhueta: `camera` f339→f351 ×1,0236 (+4,8 %/s), desce 0,5 px/q; f361→f373 ×1,0271 (+5,5 %/s), desce 0,4 px/q; fim f363→f375 (0,0,720,820): ×1,0252 (+5,1 %/s), desce 0,23 px/q → não freia antes do corte (medido). A foto de baixo (V01-A08) continua recuando: as duas camadas andam em sentidos opostos (paralaxe de camadas: uma aproxima, a de baixo afasta). Fundo parado.
- Cadência (reestudo 20/11): 12 imagens/s: `perfil` f337–f344: 12,6 / 0,01 / 7,2 / 0,3 / 3,7 / 0,4 / 3,8 / 0,4. O calor cresce nos mesmos passos.
- Legenda nesta cena (reestudo 20/11): 2 blocos: o meio da pergunta (f333–f361, 4 palavras, troca no MESMO quadro em que o disco cai: troca = entrada de peça) e o estado prometido (f362–f375, 2 palavras; o estado já nasceu em f357, 5 quadros antes). Atrás da tarja: a borda de baixo do disco teal e os pés da silhueta (y846–865) e, nos lados, a foto de baixo → censo 0,78, tarja luma 13 × 26; opacidade real 74 %, preta pura, medida direta da conferência (corrigido na conferência: era "opacidade 0,78"). Cor #e8de53. Nenhum outro texto.

## CONSTRUÇÃO
1. fundo: mesa fixa.
2. foto de baixo (V01-A08): continua por baixo, recuando.
3. disco teal: círculo #35828c maior que a largura (corda máxima > 720 px; cor de y≈115 a y≈846 em f345, 9 → 66 % da altura), quase liso com manchas fracas de 10–30 px, ondas claras horizontais de 4 px (branco 20 %) a cada ≈ 120 px. Entrada em 0 ms (f333) com a corda a 89,7 % → 83 ms já passa da tela (100 %); estalo.
4. silhueta do sujeito: forma humana de frente, braços levemente abertos, creme #e3daca com grão de papel quente TROCADO a cada imagem (12/s, como o disco creme; corrigido na conferência: era "PARADO"), sem contorno, halo escuro de 14–15 px (−19 a −24 %) igual em volta sobre o teal; centrada em x 50 %, da cabeça em y≈125 aos pés em y≈845. Entra junto com o disco.
5. calor: mancha radial granulada (pontilhado) no peito, núcleo #d96826 → #e88b34 → #d5a564 → creme, com 2–3 anéis concêntricos finos na borda; nasce em 1000 ms (f357) como ponto de ≈ 10 px e cresce até ≈ 200 × 260 px em 417 ms (f367), ease-in-out; depois pulsa leve (diferença 6–7 por imagem).
6. câmera: disco + silhueta + calor fazem zoom in +5 %/s do assentamento ao corte.
- Linha do tempo (ms a partir de f333): 0 disco 89,7 % + legenda do meio da pergunta · 83 disco na largura cheia · 1000 calor nasce · 1208 legenda do estado prometido · 1417 calor completo, pulsa · 1792 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: a cor do meio (aqui água = teal), a forma da silhueta (o sujeito), a cor e o lugar do estado que nasce (aqui calor = laranja no peito).
- O que NÃO fazer: degradê liso de vetor no calor (é granulado, com anéis); silhueta com contorno ou com sombra deslocada (halo em volta, sem direção); teal com textura forte (é quase liso); disco inteiro dentro da tela (sangra dos lados); papel da silhueta parado (ele ferve a 12/s como o disco creme; parado fica só o teal; corrigido na conferência: era "não fazer o papel da silhueta fervendo").

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o meio onde o sujeito está": cor de fundo do disco (aqui água = teal).
  - "o sujeito": silhueta simples chapada.
  - "o estado que a pergunta promete": mancha de cor que cresce (aqui calor = laranja).
- Nesta referência as lacunas foram preenchidas com: água (com ondas finas de superfície), corpo humano de frente com os braços levemente abertos, calor no peito.
- Receita de tratamento de cada imagem: tudo vetorial chapado com grão de papel; silhueta creme sem contorno, com grão vivo; meio em cor sólida do sistema com detalhes em linha fina clara; estado em degradê radial suave, cor quente.
- Receita de ILUSTRAÇÃO (reestudo 20/11): diagrama chapado em 3 camadas de "papel": (a) meio = disco de cor sólida do sistema, quase liso (grão < 1), com 3–6 linhas claras finas (4 px, branco ≈ 20 %) que dizem o que é o meio; (b) sujeito = silhueta recortada em papel creme com fibra (grão 7, quente, trocado a cada imagem), sem contorno, com halo escuro de 14–15 px em volta, parada na posição; (c) estado = degradê radial granulado em cor quente (laranja #d96826 no núcleo), com anéis concêntricos finos na borda, que nasce de um ponto e cresce. Destaca-se do fundo pelo contraste teal × creme × laranja; nada tem traço preto. A silhueta ferve (grão vivo nos claros); o teal fica parado (corrigido na conferência: era "a silhueta não ferve").
- Regra de escolha: a pergunta do vídeo vira um diagrama-síntese de 1 frase (sujeito no meio hostil + o resultado que parece impossível).
- Teste de generalização: (1) Claude Code: "como ele lembra do projeto?" → silhueta de um chip/robô num disco escuro (o "vazio"), e uma mancha de cor "memória" acendendo na cabeça. (2) café: "como ele fica doce sem açúcar?" → silhueta de xícara num disco marrom, mancha dourada "doçura" nascendo no centro.

- Confiança: cores, escala e tempos medido; ondas e forma da silhueta observado.
