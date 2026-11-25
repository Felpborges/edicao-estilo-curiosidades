# V01-A46 · disco creme + recorte do objeto do início; água translúcida sobe pela base (fecho visual)
- Categoria: P14 · Disco creme com recorte (provisória do analista: (provisória) palco de círculo creme + recorte-adesivo, com agente animado (callback do hook))
- Fonte: V01 quadros f3713–f3748 (154,71–156,17 s; 36 quadros ≈ 1500 ms) · 24 fps · por cima de V01-A44/A45
- Fala: "warm by keeping the water out."
- Tipo de fala: conclusão (tese em callback do gancho)
- Gatilho: cai em f3713 = 154708 ms, +108 ms depois da palavra nº 521 "warm" (154600 ms). Água começa em f3719 = 154958 ms, +98 ms depois da nº 522 "by" (154860 ms).
- Quadro-chave: f3744
- Camadas ativas: cena de tela cheia | grafismo animado (água) | legenda
- Leitura dos strips: strip.jpg = quadros f3711 a f3722, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 12 células. strip-saida.jpg = quadros f3730 a f3750 (água sobe e corte para o rosto), mesma regra, 21 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-agua-translucida.jpg = quadro f3744, região x420 y560 200x140 px, ampliada 2× sem suavizar · detalhe-disco-amassado-realce.jpg = quadro f3744, região x40 y200 220x200 px, ampliada 2× sem suavizar, contraste ×6 em volta da média.


## LEITURA DE EDITOR
- Por que esta cena aqui: a tese final repete o objeto do gancho; o editor fecha o círculo com a MESMA imagem do início, agora com a água subindo por ela, na palavra "água": o espectador vê a resposta à pergunta do começo.
- Por que este design: o palco do início (disco creme + recorte-adesivo do objeto), maior (89 % da largura), por cima de tudo que veio antes; uma faixa de água translúcida sobe e cobre metade do objeto.
- Por que estas cores: creme e a cor real do objeto (o único recorte colorido de produto), e o teal claro da água: as duas cores que contam a história inteira.
- Por que estes efeitos: água translúcida (≈ 83 %) com borda de cima clara: o objeto continua visível por baixo (a água entra, e tudo bem); disco de papel amassado e vivo, adesivo com sombra.
- Por que este movimento: pop com sobra (o disco passa do tamanho e volta) e água que sobe rápido e freia (ease-out), parando pouco antes do corte para o rosto.
- Sensação do movimento: "chegamos": um gesto único, calmo e conclusivo; a água assentando dá o ponto final.

## FORMA (fixa: reproduzir igual)
- Igual a V01-A01/A11 na forma (disco creme + recorte-adesivo do mesmo objeto do hook, pop desencontrado). Medidas próprias (disco.py, quadro cheio):
  - Disco: linha mais larga assentada f3719 640 px (88,9 % da largura), centro x 50,5 %, linha y476 (37,2 %); maior que nos palcos do começo (76–80 %). O anúncio de trás aparece nas pontas.
  - Recorte: o objeto-tema do hook (a mesma imagem), de frente, contorno de adesivo off-white; passa do disco embaixo. (observado)
  - Agente que a conclusão menciona: faixa azul-teal CLARA e translúcida #6a9fa3 (f3740, 360,640) que sobe da base do disco, com borda de cima reta/ondulada, por cima do disco E da parte de baixo do recorte (que aparece através dela). (cor medido; transparência ≈ 83 % calculada pelos dois fundos (alinhado ao reestudo))
- Movimento:
  - Entrada: disco f3713 618 px (96,6 %) → f3715 660 (103 %) → f3717 639 → f3719 640 (100 %). Pop com sobra; já assentado em f3717 (639 → 640 é deriva): 4 q da entrada ao assentado (remedido; o eventos.json dizia 6). (medido)
  - O agente sobe de f3719 a ≈ f3741 (≈ 22 q, 917 ms) desacelerando: diferença por imagem na faixa 21,8 → 22,8 → 17,4 → 13,6 → 10,6 → 8,9 → 7,7 → 6,4 → 5,5 → 5,0 (ease-out). (medido no perfil, região x100 y550 520x250)
  - Saída: corte seco para o A-roll final em f3749. Cadência 12 imagens/s (fase ímpar). (medido)
- Ritmo: 1500 ms; agente parado só nos últimos ≈ 0,3 s. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Disco: papel creme amassado. f3744 região 540,250,100,80: #b9b1a0, luma 177, grão 4,07 níveis, manchas 8,50 (vincos), ac1 +0,60, cinza (4,04/4,07/4,09); VIVO (+0,01 no lugar, +0,13 depois de alinhar 2,6 px; teste novo f3744×f3746, afim da cena, claros lisos: resíduo/σ 1,22–1,24, correlação +0,27/+0,30; escuros 0,38–0,43, +0,90 = VIVO, mesmo veredito). No realce: fibras mosqueadas, vincos claros horizontais e borda do disco mais acinzentada.
  - Recorte do objeto: foto colorida real do objeto do gancho, recortada, adesivo off-white ≈ 8 px (linha y400: x218–225, L214–222).
  - Agente da conclusão (teal claro translúcido). f3744 região 520,640,100,60: #6fa1a2, luma 150, grão 1,55, manchas 7,99; VIVA (+0,26 / +0,39). Borda de cima: faixa clara de ≈ 8 px (#b4c0b6 → #b7d2cb, y586–594) e depois o corpo teal (#6a9da1). Opacidade calculada pelos dois fundos: disco L208 → 148 e objeto L37–46 → 120 ⇒ ≈ 83 % de teal com cor de luma ≈ 137 (#5a96a0 aprox.).
- Efeitos (reestudo 20/11):
  - Sombra do recorte no disco: ≈ 8 px, −15 % (x210–217 em y400: 154–171 contra 183–189).
  - Sombra do disco na mesa (medido, f3744, perfil alinhado embaixo e em cima, linhas y420–460 nos lados): embaixo −45 % no contato, volta em 14 px; à esquerda −34 % (23 contra 35), volta em ≈ 12 px; à direita −30 %, ≈ 10 px; em cima −10 %, 4 px. Caída para baixo, como a das fotos (corrigido na conferência: a nota não media a sombra do disco).
  - Transparência: sim, o teal deixa ver ≈ 17 % do que está atrás.
  - Vinheta, desfoque de movimento, aberração, brilho: nenhum (medido em f3744). O anúncio de trás aparece nas pontas, nítido.
- Câmera (reestudo 20/11): o disco sobe e aproxima, quase constante: f3719 → f3733 escala ×1,0173 (+3,0 %/s), centro (+0,10, −1,16 px/q), giro −0,11°; f3735 → f3747 ×1,0142 (+2,9 %/s), centro (+0,09, −0,89 px/q). Fim da cena (medido, f3736 → f3746, região 0,0,720,830): ×1,0127 (+3,1 %/s), centro (+0,11, −0,85 px/q): o mesmo ritmo até o corte, sem recuo. Mesa parada.
- Cadência (reestudo 20/11): 12 imagens/s (perfil f3714–f3748: 0,01 / 49,4 / 0,01 / 21,9 / 0,00 / 16,9 / 3,6 / 15,7 / 0,06 / 11,8 / 0,02 / 9,5 … / 3,4 / 0,63; fase ímpar), o teal freando de 16,9 para ≈ 4 por imagem.
- Legenda nesta cena (reestudo 20/11): o 1º bloco (3 palavras) entra em f3712, 1 quadro ANTES do disco; o 2º (3 palavras, o agente da conclusão; f3728–f3748) termina no corte seco para o rosto final. Texto #ebdf53, 68 %. Atrás da tarja: a mesa (o disco termina em y≈790). Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #181516, parada.
2. cena de baixo: o anúncio de V01-A44/A45, visível nas pontas.
3. disco: papel creme amassado #b9b1a0–#d7cfbc com grão vivo ≈ 4 níveis, Ø ≈ 640 px (88,9 % da largura), centro (50,5 %, 37,2 %); sombra caída para baixo na mesa (embaixo −45 %, some em 14 px; lados −30 a −34 %, 10–12 px; em cima −10 %, 4 px).
4. recorte do objeto do gancho (a mesma imagem), foto colorida com adesivo off-white ≈ 8 px e sombra ≈ 8 px (−15 %), passando um pouco do disco embaixo.
5. agente da conclusão: retângulo teal claro a ≈ 83 % de opacidade, recortado pelo círculo do disco E cobrindo o objeto, borda de cima reta/levemente ondulada com faixa clara de ≈ 8 px, grão vivo ≈ 1,5.
6. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Animação: disco 0 ms (f3713) a 96,6 % → 83 ms 103 % → 167 ms 100 % (pop com sobra); o teal sobe da base a partir de 250 ms (f3719) até ≈ 1167 ms, ease-out (diferença por imagem 16,9 → 4); disco sobe ≈ 1 px/q e aproxima +3 %/s. Passos de 2 quadros.
- Linha do tempo (ms a partir da queda do disco, f3713 = 154708 ms): −42 ms 1º bloco de legenda · 0 disco · 167 ms assentado · 250 ms o teal começa a subir · 625 ms 2º bloco · ≈ 1167 ms o teal para · 1500 ms corte seco para o rosto final.
- Parâmetros que dependem do conteúdo: o objeto (o MESMO do gancho), o agente da conclusão (aqui, faixa teal clara) e até onde ele sobe.
- O que NÃO fazer: usar uma imagem diferente da do gancho, teal opaco (tem de deixar ver o objeto), teal subindo linear, disco liso e parado.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "objeto-tema" (o MESMO recorte usado no hook).
  - "o agente que a conclusão menciona": forma de cor translúcida animada.
- Nesta referência as lacunas foram preenchidas com: a roupa de mergulho sem capuz; água subindo pelas pernas.
- Receita de tratamento de cada imagem: recorte idêntico ao do começo (callback); agente vetorial chapado translúcido em versão clara da cor do sistema.
- Regra de escolha: a frase-tese final repete a imagem do começo com o agente agindo nela (fecha o círculo do hook).
- Teste de generalização: (1) Claude Code: "então ele não funciona por lembrar de tudo" → o mesmo recorte do notebook do hook, com uma faixa translúcida de "esquecimento" subindo. (2) café: "então ele não é forte por causa da cafeína" → o mesmo recorte da xícara do hook, com o café subindo translúcido.
- Receita de tratamento (reestudo 20/11): foto colorida real do objeto do gancho, recortada, adesivo off-white ≈ 8 px e sombra curta, sobre disco de papel creme amassado com grão vivo.
- Receita de ILUSTRAÇÃO (reestudo 20/11): agente como faixa chapada translúcida (≈ 83 %) na cor de sistema (teal claro), recortada pelo disco, com borda de cima clara de ≈ 8 px e grão vivo; revelada subindo da base com ease-out.
- Teste de generalização (reestudo 20/11): (1) Claude Code: "então o agente não é bom por esconder o contexto, é bom por usá-lo" → o mesmo recorte do robô do gancho no disco, faixa teal translúcida subindo por ele no fim. (2) café: "então a garrafa não funciona isolando o ar" → a mesma garrafa do gancho no disco, faixa translúcida de ar subindo.

- Confiança: disco, cor, tempos e curva da água medido; transparência calculada (≈ 83 %) (alinhado ao reestudo); recorte observado.
