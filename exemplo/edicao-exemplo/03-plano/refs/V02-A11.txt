# V02-A11 · linha do tempo com contador regressivo
- Categoria: P21 · Linha do tempo e dado em papel (provisória do analista: (provisória) cartão de interface (linha do tempo de vídeo) com etiqueta de duração que conta para trás enquanto trechos são cortados; marca-texto no valor final)
- Fonte: V02 quadros f1146–f1212 (47,80–50,55 s; 67 quadros ≈ 2795 ms) · 23,976 qps
- Fala: "Editors, send your best edit under a minute."
- Tipo de fala: número
- Gatilho: entra por corte seco em f1146 (47810 ms), +10 ms depois do início da palavra nº 154 "Editors," (47800 ms); o corte vem direto da cena anterior (sem rosto). A contagem para em f1189, +92 ms depois de nº 159 "under" (49500 ms). Marca-texto no número em f1206, -5 ms antes de nº 161 "minute." (50320 ms). Conferido no perfil (f1206 dif 3,22, isolado).
- Quadro-chave: f1210
- Camadas ativas: legenda | grafismo (cena de tela cheia) | som
- Leitura dos strips:
  - strip.jpg: quadros f1145 a f1192, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 48 células; cada célula traz o nº do quadro e o tempo.
  - strip-saida.jpg: quadros f1193 a f1214, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 22 células; cada célula traz o nº do quadro e o tempo.
  - strip-geral.jpg: quadros f1144 a f1214, de 2 em 2, 8 colunas, da esquerda para a direita, linha a linha; 36 células; cada célula traz o nº do quadro e o tempo.
  - detalhe-etiqueta-marca-texto.jpg: quadro f1210, região x80 y255 220x110 px, ampliada 3× sem suavizar (etiqueta branca de cantos arredondados, marca-texto e algarismos).
  - detalhe-canto-cartao-sombra.jpg: quadro f1210, região x480 y560 130x160 px, ampliada 3× sem suavizar (canto da moldura de papel e a sombra).
  - detalhe-fundo-aneis-realce.jpg: quadro f1210, região x0 y880 720x400 px, ampliada 1× sem suavizar, contraste ×6 em volta da média (o fundo desta cena: degradê radial com anéis de quantização).
  - detalhe-contagem-f1165.jpg: quadro f1165 (meio da contagem), região x0 y150 720x700 px, ampliada 1× sem suavizar (DESFOQUE DE MOVIMENTO horizontal nos trechos que deslizam e nos pedaços que caem).

## LEITURA DE EDITOR
- Por que esta cena aqui: a instrução para o 2º público tem um LIMITE numérico; a cena mostra o limite sendo cumprido: a duração desce enquanto a linha do tempo é cortada, e o valor final é marcado quando a unidade do limite é dita.
- Por que este design: a mesma interface impressa em papel da V02-A04 (callback da função 2), agora numa moldura de cartão, com a etiqueta do valor no canto como num painel; a régua com o início e o alvo mostra o limite sem precisar dizer.
- Por que estas cores: moldura creme e etiqueta branca sobre um fundo escuro com luz alta (atrás do cartão); o único amarelo é o ponteiro e o marca-texto do número final.
- Por que estes efeitos: os trechos que deslizam e os pedaços que caem levam desfoque de movimento horizontal forte (a única cena do vídeo com isso), o que dá a sensação de "corte rápido de editor"; o cartão tem sombra embaixo e, curta, dos lados.
- Por que este movimento: o cartão entra grande e recua devagar enquanto o conteúdo se comprime; o contador desce em saltos que encolhem (grande → pequeno), desacelerando até parar exatamente na palavra do limite; o marca-texto carimba o valor na unidade do limite.
- Sensação do movimento: compressão e urgência controlada: muita coisa sendo cortada rápido, e depois um "pronto, coube". Produzida por contagem desacelerando (≈ 42 q) + desfoque de movimento nos cortes + número parado ≈ 1 s antes do carimbo de 4 q, com o cartão ainda recuando devagar (alinhado ao reestudo).

## FORMA (fixa: reproduzir igual)
- Design:
  - Fundo: tampo escuro #1f1f1b (78,5 % da área em f1210) / #22231f (f1210, x600 y700). Medido.
  - Cartão: moldura de papel creme #dfd8ca, com cantos vivos e sombra curta, levemente inclinado (≈ 2°); dentro, a interface da tarefa recriada em plano, em 2 andares (faixa de imagens reais repetidas em cima, painel branco com traço gráfico preto embaixo) e régua com marcas em sans pequena cinza. f1210: cartão x87 y313 489x386 (12,1 % · 24,5 %; 67,9 % x 30,2 %), centro (46,0 %, 39,5 %). Medido.
  - Etiqueta do valor: tira de papel creme/branca no canto superior esquerdo do cartão, x89 y268 107x57 (14,9 % x 4,5 %), algarismos pretos bold no formato da grandeza contada. No fim, marca-texto amarelo #f0d050 dentro da etiqueta, x97 y277 90x41 (12,5 % x 3,2 %). Medido.
  - Pedaços removidos: retângulos cinza (pedaços da faixa da interface) que se soltam e caem sob o cartão, com sombra. Observado.
  - Ponteiro: linha vertical amarela fina que corre pela faixa da interface. Observado.
- Movimento:
  - Entrada: corte seco em f1146 (dif 62,3); o cartão aparece grande (a faixa passa das bordas) e a câmera anda/afasta: dif 3,2 (f1148) → 10,5 (f1155, pico) → ≈ 6,5 constante (f1160–f1181) → 3,3–4,2 (f1189–f1200) → 1,3–0,6 (f1201–f1212). Medido.
  - Contagem regressiva: a etiqueta troca de valor a vários quadros (17 valores; os saltos encolhem: no início ≈ 20–30 unidades por troca (≈ 7–11 % do valor inicial) a cada 2–4 quadros, no fim poucas unidades por troca a CADA quadro, f1180–f1188) (conferido; os valores desta referência estão no bloco CONTEÚDO), de f1148 a f1188 (valor final já em f1188) (≈ 42 quadros ≈ 1752 ms), desacelerando (passos grandes no início, pequenos no fim). Troca seca, sem rolagem. Observado (valores lidos nas folhas).
  - Cortes: enquanto a contagem desce, o ponteiro amarelo atravessa a faixa e pedaços cinza caem por baixo (f1151–f1187); a faixa de imagens se comprime (a interface "encolhe" junto com o valor). Observado.
  - Assentamento: f1189–f1200 o cartão freia perto do tamanho final (≈ 68 % da largura) e segue recuando ≈ −0,13 %/q até o corte (corrigido na conferência: era "termina de recuar"; medido f1204 → f1212 na correção). Observado + perfil + câmera.
  - Marca-texto: VARRE o número da esquerda para a direita em ≈ 4 quadros (f1206 → f1209, ≈ 167 ms), não estala (conferido, f1206–f1209, folha recortada na etiqueta; antes: "estala em f1206, completo em f1206–f1207").
  - Permanência: completo f1207–f1212 = 6 quadros ≈ 250 ms (o número final, sem marca, já estava parado desde f1189 ≈ 1 s). Medido.
  - Saída: corte seco para o rosto em f1213 (dif 67,8). Medido.
- Passos internos:

| passo | quadro de início | duração | tipo de movimento | curva | palavra-gatilho e deslocamento |
|---|---|---|---|---|---|
| cartão em cena (corte) + câmera afastando | f1146 | ≈ 55 q | corte + zoom out/pan | ataque em 8 q, depois constante e freio | nº 154, o público chamado (47800 ms): +10 ms |
| contagem regressiva + trechos caindo | f1148 | ≈ 42 q ≈ 1752 ms | troca seca de número + quedas | desacelera | nº 155, o verbo da tarefa (48380 ms): -499 ms |
| contagem para no valor final | f1189 | — | — | — | nº 159, a palavra do limite (49500 ms): +92 ms |
| marca-texto no número | f1206 | ≈ 4 q (conferido; antes ≈ 2 q) | varredura esquerda → direita | — | nº 161, a unidade do limite (50320 ms): -5 ms |

- Ritmo: entra 0 ms depois da V02-A10 (corte direto). Número final parado ≈ 1 s (f1189–f1212), marcado só nos últimos 250 ms. Medido.
- Som: efeito estéreo f1200–f1204 (lateral pico -29,4 dB), 2 a 6 quadros ANTES do marca-texto (f1206): um "tique"/estalo que anuncia o número final. Nada no corte de entrada nem durante os cortes da faixa (lateral -120 dB em f1146–f1199). Medido (envelope); natureza inferida.
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Fundo desta cena: NÃO é a mesma luz da mesa das V02-A02 a A09. Também parado na tela (f1210 × f1212: +0,98; mapa de luz igual em f1150 e f1210), mas com o centro da luz ALTO: luma 35,9–36,3 em x 50 % y 13 %, 33–34 nas laterais até y ≈ 50 %, caindo para 29–30 a y 75 %, 24 a y 87 % e 23,2 no pé (f1210, região x40 y950 640x300: #1a1a16, luma 25,5, grão 0,18, manchas 0,43). É um degradê radial centrado atrás do cartão, com anéis de quantização coloridos visíveis no realce (verde, roxo, vermelho; #1f1816 e #191718 na parte de baixo) (detalhe-fundo-aneis-realce). Família: liso.
  - Moldura do cartão: papel/cartão creme #dfd8ca com grão forte (f1210 região x530 y360 25x220, perto da borda interna: grão 8,9 níveis, manchas 4,8; a medida pega a borda do painel, valor alto por isso). Família: cartão.
  - Interface: tiras de papel impressas (imagens coloridas em cima, traço gráfico preto sobre creme embaixo) e régua de marcas em sans pequena cinza, como na V02-A04.
  - Etiqueta: papel branco (luma ≈ 237) com cantos arredondados (raio ≈ 4 px), sombra curta; marca-texto #f0d050 dentro, retângulo com cantos arredondados; algarismos pretos bold (detalhe-etiqueta-marca-texto).
- Efeitos (reestudo 20/11):
  - Sombra do cartão (sombra4 f1210, caixa x95 y318 480x378): embaixo −10 níveis (24,5 contra 34,5) em ≈ 18 px; laterais −4 a −5 em ≈ 10 px; em cima nenhuma. Remedida na correção 20/11 com perfil alinhado na borda real (o cartão está girado 2°): embaixo fio 14 (−58 %) e 23 contra 35 (−12 níveis, −34 %) até ≈ 14 px; à esquerda fio 24 e 31 contra 35 (−4 níveis) até ≈ 8 px; à direita fio 23 e 31 contra 38 (−7 níveis) até ≈ 12 px; em cima nada (1 px). Mesmo desenho da nota (baixo forte, lados fracos, nada em cima), com o lado direito mais forte que o esquerdo.
  - Sombra da etiqueta (caixa x89 y268 107x57): fio escuro de 1 a 2 px nas laterais (−7 a −8); remedida na correção (perfil alinhado, f1210): à esquerda fio 20 (−43 %) e 30 contra 34 (−4 níveis) até ≈ 9 px; à direita fio 21 (−44 %) e volta a 35–38 em ≈ 4 px; embaixo ela encosta no cartão (sombra de −69 sobre o creme da moldura, 19 px); em cima nenhuma.
  - DESFOQUE DE MOVIMENTO: sim, só aqui no V02: em f1165 os trechos da faixa que deslizam para a esquerda estão borrados na horizontal (rastro de ≈ 100 a 150 px, com transparência) e os pedaços que caem também (detalhe-contagem-f1165). As peças paradas (etiqueta, moldura) ficam nítidas.
  - Vinheta: o degradê radial do fundo (centro alto, pé a ≈ 64 % do centro). Brilho, halo, aberração, profundidade de campo, grão global: nenhum (medido em f1210).
- Câmera (reestudo 20/11): o fundo fica parado; a camada do cartão recua. `camera` na região x0 y200 720x560: f1150 → f1158 −0,18 %/q, −0,6/+0,3 px/q; f1170 → f1180 −0,39 %/q, −0,9/+0,4 px/q; f1192 → f1202 −0,57 %/q, −0,5/+0,8 px/q, giro ≈ +0,01 °/q. Ressalva: a região inclui a faixa que se comprime sozinha; o perfil (dif caindo de ≈ 6,5 para 0,6 em f1201–f1212) indica que o cartão assenta no fim, então os valores de f1192–f1202 misturam o recuo com a compressão da faixa. Fim f1204 → f1212 (região x0 y0 720x820, 593 de 600 pontos, faixa já parada; medido na correção 20/11): −0,135 %/q (−3,2 %/s), −0,15/+0,26 px/q: o cartão NÃO assenta, continua recuando devagar até o corte (corrigido na conferência: era "o cartão assenta no fim").
- Cadência (reestudo 20/11): 24 imagens/s (`perfil` f1160–f1176: 13,2 a 15,5 constante, sem quadros parados alternados); o contador troca a cada 2 a 4 q no começo e a cada quadro no fim.
- Legenda nesta cena (reestudo 20/11): tarja 50 % (luma dentro 16 × fora 30, f1170 e f1210; direta 49,6–50,9 % na conferência; altura 76 px; o fundo aqui é um pouco mais escuro na faixa da legenda que na mesa, 30 × 35); cor #f4ea14 a #f6e913; centro 67,9–68,2 %. Blocos: público + verbo f1145–f1169 entrou 1 q ANTES do corte de entrada (ainda sobre a folha da V02-A10) e atravessa o corte; possessivo + adjetivo f1170–f1181; substantivo + limite + artigo (3 pal.) f1182–f1205; a unidade do limite com ponto f1206–f1212 entra NO MESMO QUADRO do marca-texto do número (f1206) e termina no corte; o bloco do rosto entra junto do corte (f1213). Atrás da tarja: só o fundo escuro (o cartão termina em y ≈ 700). Outro texto: a etiqueta do contador (algarismos de 34 a 40 px de altura no censo; o detector marca "texto branco grande" em f1145–f1212 por causa da moldura e da etiqueta claras) e a régua com o início e o alvo.
- Entrada do texto (reestudo 20/11): o número da etiqueta não entra: já está em cena no corte e troca seco (sem rolagem, sem fade); 17 valores de f1148 a f1188, com o passo encolhendo; o marca-texto varre em 4 q (f1206–f1209). Peso por comparação (detalhe-etiqueta-marca-texto, 3×): haste ≈ 6 px ÷ altura do algarismo ≈ 30 px = 0,20 (bold pesado); largura ≈ 0,62 da altura por algarismo.

## CONSTRUÇÃO
1. fundo: degradê radial escuro PARADO na tela, centro alto (x 50 %, y ≈ 15–35 %, luma ≈ 36) caindo para 23 no pé; liso, sem grão.
2. camada do cartão (recua devagar): moldura de cartão creme #dfd8ca, 68 % × 30 % do quadro no fim, centro (46 %, 39,5 %), inclinada ≈ 2°, cantos vivos; sombra para baixo (fio −58 %, depois −12 níveis, some em ≈ 14 px) e dos lados (−4 a −7 níveis, some em 8–12 px, mais forte à direita), nada em cima (corrigido na conferência: era "para baixo −10 níveis em 18 px", sem os lados).
3. interface dentro da moldura: faixa da interface (imagens reais + traço gráfico) em tiras de papel, régua com o início e o alvo do limite; ponteiro amarelo vertical que atravessa a faixa; trechos que deslizam para a esquerda com DESFOQUE DE MOVIMENTO horizontal (rastro ≈ 100–150 px) e pedaços que se soltam e caem por baixo do cartão, também borrados (83 a 1708 ms, f1148–f1187).
4. etiqueta do valor: papel branco de cantos arredondados (≈ 15 % × 4,5 %) no canto superior esquerdo do cartão, algarismos pretos bold; troca seca de valor de 83 a 1752 ms (f1148–f1188), passo grande no início (a cada 2–4 q) e pequeno no fim (a cada quadro), parando no valor final em ≈ 1752 ms.
5. marca-texto #f0d050 atrás do número, varrendo da esquerda para a direita de 2500 a 2667 ms (f1206–f1209), com um tique 2 a 6 q antes.
6. movimento da camada 2–5: entra grande no corte e recua (−0,2 → −0,4 %/q), freando para ≈ −0,13 %/q a partir de ≈ 2250 ms (f1200) e sem parar até o corte (corrigido na conferência: era "até assentar por volta de 2250 ms").
7. legenda (camada fixa, tarja preta 50 %, altura 76 px; ver V02-L02).
- Linha do tempo (ms a partir do corte f1146): 0 corte (cartão grande) · 83 contagem + cortes começam · 1752 valor final, cartão assentando · 2250 quase parado (−0,13 %/q até o corte) · 2500 marca-texto (167 ms) · 2795 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: a interface da tarefa, a grandeza e o formato do contador, o valor inicial e final, o alvo da régua.
- O que NÃO fazer: usar a luz da mesa das outras cenas (aqui o centro da luz é alto); contador com rolagem; contagem linear (os passos encolhem); marca-texto antes da palavra do limite; esquecer o desfoque de movimento nos trechos que deslizam (é a assinatura desta cena).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - interface/objeto da tarefa pedida ao 2º público (aqui uma linha do tempo de edição)
  - grandeza que precisa caber num limite (aqui a duração) e o valor final dentro do limite
- Nesta referência as lacunas foram preenchidas com: linha do tempo de editor de vídeo (miniaturas com o próprio rosto do criador em cima, forma de onda do áudio embaixo, régua de tempo, cabeça de leitura amarela, trechos cortados caindo); duração no formato m:ss, de 4:40 descendo até 0:56 (abaixo de 1 minuto), em saltos de ≈ 20–30 s no início e de poucos segundos no fim.
- Receita de tratamento de cada imagem: interface recriada em estilo plano dentro de uma moldura de papel creme, com cores reais nas miniaturas; números em etiqueta de papel, bold preto; nada de janela de sistema operacional.
- Regra de escolha: uma RESTRIÇÃO numérica ("menos de um minuto", "até 5 páginas") vira um contador que desce até caber, com o valor final marcado em amarelo no instante em que o limite é dito. Teste de generalização: (1) Claude Code: "mande um app que carregue em menos de 2 segundos" → cartão de painel de desempenho com o tempo de carga descendo de 9,4 s a 1,8 s, marca-texto no 1,8. (2) Café: "extração em menos de 30 segundos" → cartão com cronômetro da máquina descendo até 0:28, marca-texto no número.

- Receita de tratamento (reestudo 20/11): interface recriada como objeto de papel (tiras impressas com frestas) dentro de moldura de cartão creme com grão; miniaturas em cor real sem tratamento; etiqueta de papel branco com cantos arredondados e sombra curta.
- Receita de ILUSTRAÇÃO (reestudo 20/11): não há desenho à mão; a interface é ilustração plana impressa em papel; os trechos cortados ganham desfoque de movimento quando deslizam.
- Teste de generalização: (1) Claude Code: "mande um app que carregue em menos de 2 segundos" → cartão de papel com o painel de desempenho, etiqueta com o tempo de carga descendo de 9,4 s para 1,8 s enquanto barras são cortadas com rastro de movimento, marca-texto no 1,8 em "segundos". (2) café: "extração em menos de 30 segundos" → cartão com o cronômetro da máquina, etiqueta descendo até 0:28, marca-texto no número.

- Confiança: caixas, cores, cortes, curvas de câmera, efeito sonoro = medido · valores da contagem, quedas dos trechos, cabeça amarela = observado (folha 2 em 2 e strips 1 em 1) · natureza do som = inferido.
