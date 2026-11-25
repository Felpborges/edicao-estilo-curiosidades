# V04-A49 · pan lateral: peça de tecido estampado (com ilhós) entra pela direita e cobre; contorno creme desenhado em volta de uma mancha
- Categoria: P19 · Marcação e desenho à mão (provisória do analista: (provisória) objeto recortado com contorno desenhado (nome do padrão))
- Fonte: V04 quadros f3736–f3799 (155,82–158,45 s; 64 quadros ≈ 2669 ms) · 23,976 fps
- Fala: "was called the Splinter Camo. It looks like"
- Tipo de fala: nome (o padrão ganha nome: "foi chamado de Splinter")
- Gatilho: o novo tecido entra pela direita em f3736 (155822 ms), DURANTE a palavra nº 521 "1931," (começa 155200 ms → +622 ms; a voz dessa palavra vai até ≈ f3744 no envelope), 378 ms antes da nº 522 "was" (156200 ms) (conferido: a palavra dita em f3736 é "1931,", não "was"; o JSON passou a apontar a nº 521). Conferido no `perfil` (dif 7,5 → 9,5 → 11,2 em f3736–f3738; pico 15,9 em f3741).
- Quadro-chave: f3790
- Camadas ativas: legenda | cena de tela cheia | grafismo (contorno) | som (voz)
- Leitura dos strips: strip.jpg = quadros f3734 a f3781, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha (entrada + contorno); strip-geral.jpg = quadros f3734 a f3801, de 2 em 2, 8 colunas, da esquerda para a direita, linha a linha. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-contorno-desenhando.jpg = quadro f3770, região x260 y520 300x140 px, ampliada 2× sem suavizar (traço creme de 6–7 px, cantos arredondados, irregular como marcador); detalhe-contorno.jpg = quadro f3784, região x200 y520 360x150 px, ampliada 2× sem suavizar (contorno fechado em volta da mancha).

## LEITURA DE EDITOR
- Por que esta cena aqui: o padrão impresso ganha nome; o objeto real que levou o padrão (a peça de tecido com ilhós) aparece, e um contorno desenhado isola UMA mancha, a forma que dá nome ao padrão ("lasca").
- Por que este design: o objeto recortado ocupa a metade de baixo e o centro, sem cartão; o contorno é a única marca do editor e fica no terço de cima, longe da legenda.
- Por que estas cores: o tecido em bege, marrom e verde-oliva de arquivo; o traço creme quase branco é o único elemento claro e limpo.
- Por que estes efeitos: vinheta da cena (borda a 12 %); o traço é chapado, sem brilho nem sombra: parece riscado à mão com marcador (alinhado ao reestudo).
- Por que este movimento: um chicote de câmera rápido com giro leva da peça anterior para a nova (≈ 100 px/q, −0,8°/q); depois a câmera quase para e o traço se desenha em passos de 2 quadros enquanto o nome é dito.
- Sensação do movimento: de virar o olhar de uma peça para outra numa mesa e circular com a caneta "esta forma aqui"; produz isso o chicote com giro seguido do traço manual em passos.

## FORMA (fixa: reproduzir igual)
- Design: foto recortada do objeto final real (que leva o padrão), sem cartão, ocupando a metade de baixo e o centro; em f3760: x0 y256 654x821 = larg 90,8 %, alt 64,1 %, centro (45,4 %, 52,1 %) (medido). Contorno: traço creme #fff4d2 de ≈ 6–7 px de espessura (meia altura de 630,3 a 637,8 px no perfil vertical em x400, f3784; corrigido no reestudo: não é ≈ 3 px), cantos arredondados, bordas levemente irregulares (mesma forma de V04-A02) em volta do detalhe que dá nome, no alto do objeto (≈ x 25–65 %, y 28–36 %) (observado). Fundo quase preto com vinheta (medido, cantos #020202–#090804).
- Movimento:
  - Entrada por chicote de câmera com giro (corrigido no reestudo: não é empurrão; a peça anterior e o novo objeto andam juntos na mesma "mesa"): `camera` f3738→f3742 −102 px/q e −3,1° em 4 quadros; f3746→f3750 −54 px/q e −1,6°; f3756→f3760 parada (+0,5/+2,2 px/q); ≈15 quadros f3736–f3750: dif 7,5 → 9,5 → 11,2 → 12,7 → 15,0 → 15,9 (pico f3741) → 15,5 → 14,6 → 15,0 → 14,9 → 14,8 → 13,6 → 12,3 → 10,8 → 10,1 (f3750) → 7,9 (f3751) (medido).
  - Contorno: desenha-se em ≈20 quadros f3764–f3784 (≈830 ms), traço da direita para a esquerda (observado); some em fade f3797–f3800 (observado em A50) (reestudo 20/11: o 1º pixel do traço é f3765 e ele avança em passos de 2 quadros, não contínuo; o sumiço parece encurtar antes de sumir, não confirmado como fade).
  - Câmera quase parada (−1 a −4 %/s), subindo no fim para A50; alt 64,1 % (f3760) → 67,7 % (f3790) (medido) (alinhado ao reestudo).
  - Saída: a obra de V04-A50 desce do topo a partir de f3799–f3800.
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| chicote de câmera: objeto entra pela direita (corrigido no reestudo: não é empurrão) | f3736 | ≈15 quadros (625 ms) | chicote com giro | pico f3741, freia | nº 522, 1ª palavra do anúncio do nome (156200 ms) | −378 ms |
| contorno desenhado em volta do detalhe que dá nome | f3764 | ≈20 quadros (830 ms) | traço que se desenha | em passos de 2 quadros (alinhado ao reestudo) | nº 525, a palavra que dá nome (157020 ms) | f3764 = 156990 ms → −30 ms |

- Ritmo: objeto parado f3751–f3763 ≈ 0,5 s; contorno completo parado f3785–f3797 ≈ 0,5 s.
- Som: legenda some em f3746–f3749 (pausa da fala); nenhum efeito destacável (áudio mono) (observado no envelope).
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Fundo: liso (tela fixa), visível no alto (luma 30–40 sob a vinheta). PARADO: f3790×f3791 +0,97 (medido, x60 y40 600x150).
  - Tecido estampado (foto recortada): #7a6144 médio, grão 8,1 níveis, manchas 11,8, ac1 +0,64 (trama de 2 px + o pontilhado do próprio padrão), grão cinza; anda com a câmera (f3790×f3791 +0,89 depois de alinhar +2,1/+4,2 px) (f3790, x120 y700 200x80). No detalhe: o padrão tem traços verticais finos (chuva) sobre as manchas.
  - Traço do contorno: creme #fff4d2 chapado (f3784, x398 y632), sem textura, com pequenas irregularidades de espessura (marcador).
- Efeitos (reestudo 20/11):
  - Vinheta da cena (f3790): luma 100/85/57/28/12 %, nitidez 100/110/45/25/9 % (alinhado ao reestudo).
  - Luz da cena (correção 20/11, f3790, medido): centro da poça em (46 %, 44 %) (ajuste na mesa, σ 0,21); luma 102 no centro (40 px), a 100 px das bordas 75 % (esq) e 72 % (dir) do centro (sobre o tecido); mesa 61 em (360,1060) e 15 em (360,1180) (razão 4,0); (360,1060) cai no tecido. A luz é desta cena, por cima de fundo e peças; os anéis acima valem só aqui (não é um multiplicador fixo do vídeo).
  - Sombra do recorte e do traço: nenhuma (o traço passa de 85–93 do tecido para 250 em 2–3 px e volta, sem halo escuro; detalhe).
  - Brilho/halo do traço: nenhum.
  - Desfoque de movimento: nenhum visível no chicote (strip-geral f3738–f3742 nítidos).
  - Fio, aberração, profundidade, grão global: nenhum.
- Câmera (reestudo 20/11): chicote f3738→f3742 −102,4/+1,9 px/q, giro −0,78°/q, escala −2,5 %/s; f3746→f3750 −53,6/−2,1 px/q, −0,41°/q; parada f3756→f3760 (−1,2 %/s, +2,2 px/q para baixo); f3786→f3790 −3,8 %/s, +3,3 px/q para baixo (a câmera começa a subir para a entrada de A50).
- Câmera em 3 pares (correção 20/11, medido, `camera` com regiões x0 y100 720x720 e x0 y250 720x570: começo f3738→f3742 −102 px/q, giro −0,93°/q (26 de 358 pontos; confere a nota); f3746→f3750 −54 px/q, −0,47°/q; meio f3764→f3770 −1,3 %/s, +2,5 px/q; fim f3786→f3790 −4,2 %/s, +3,2 px/q. Fases: chicote f3736–≈ f3751 · quase parada · subida no fim para A50.
- Cadência (reestudo 20/11): câmera a 24 imagens/s; o TRAÇO avança em passos de 2 quadros (folha f3764–f3771: f3765 = f3766; perfil x150 y480 520x200 alterna 7,1/6,3/8,0/7,6/8,7/8,0/9,7/9,0: quadro sim, quadro não o traço cresce).
- Legenda nesta cena (reestudo 20/11): amarela #ede81a, altura 32 px; SOME 4 quadros f3746–f3749 no meio do chicote; atrás da tarja o tecido (luma 39–132, mediana 92): tarja preta a 59 % fixa no vídeo (medida direta aqui: 52–60 %, mediana 59 %, em f3744, f3754 e f3758, fundo 79–141) (corrigido na conferência: era "58 % (48–63 %)", leitura do censo). Blocos na tela (folha geral; a tabela do V04.md atribui as palavras com 1 de deslocamento aqui): o bloco do ano (vem de A48) · some · 2 (o anúncio do nome, f3750) · 3 (f3762, 1210 ms, o nome inteiro num bloco só) · 3 (a comparação, f3791, atravessa para A50).
- Entrada do texto (reestudo 20/11): o contorno é o "texto" do editor: começa em f3765 no canto superior direito da mancha (1 quadro depois do bloco do nome, f3762 + 3) e corre da direita para a esquerda em passos de 2 quadros, ≈ 60–80 px por passo, fechando a forma em ≈ f3784 (≈ 20 quadros); fica parado ≈ 0,3 s e some entre f3792 e f3800 (na folha geral parece encurtar antes de sumir; não confirmado quadro a quadro).

## CONSTRUÇÃO
1. fundo: tela fixa marrom-escura lisa.
2. peça anterior (de A48) e objeto novo (foto recortada do objeto real com o padrão, x0–654 × y256–1077 em f3760, 91 % × 64 %) deitados lado a lado na mesma superfície; sem contorno, sem sombra.
3. câmera sobre 2: 0 → 625 ms chicote para a direita com giro: até ≈ 100 px/q e −0,8°/q no pico (≈ 170 ms), freando até parar em ≈ 625 ms; 625 → 2200 ms quase parada; 2200 ms → fim começa a subir (+3 px/q no conteúdo).
4. contorno: polilinha creme #fff4d2, 6–7 px, cantos arredondados, em volta da mancha que dá nome (≈ x 25–65 %, y 28–36 % do quadro); desenha-se da direita para a esquerda de 1210 ms a ≈ 2000 ms em passos de 2 quadros; some de ≈ 2340 a 2670 ms.
5. luz da cena por cima de tudo (fundo e peças; não é vinheta fixa do vídeo): poça centrada em (46 %, 44 %), força dada pelos anéis e pela mesa (os números sobre a foto misturam luz e conteúdo), mesa 61 em (360,1060) e 15 em (360,1180); anéis medidos com `borda` 100/85/57/28/12 % (f3790) (corrigido na conferência: era "vinheta da cena 100/85/57/28/12 %", lida como vinheta fixa do vídeo) (alinhado ao reestudo).
6. legenda L01, que some de 417 a 584 ms.
- Linha do tempo (ms a partir de f3736): 0 objeto novo aponta na direita (durante o ano) · 170 pico do chicote · 417–584 legenda some · 584 anúncio do nome · 1085 o nome · 1210 traço começa (≈ +0 ms da palavra que dá nome) · 2000 contorno fechado · 2294 a comparação · ≈ 2340 contorno começa a sumir · 2669 A50 (obra desce do topo).
- Parâmetros que dependem do conteúdo: o objeto real que leva o padrão; qual forma contornar (a que explica o nome); onde começa o traço.
- O que NÃO fazer: traço fino de 2–3 px ou com brilho; desenhar o traço liso a 24 q/s (é em passos de 2); usar empurrão que tira a peça anterior (é a câmera que corre); deixar a legenda durante o chicote (ela some). Pôr uma vinheta fixa igual em todas as cenas: a luz é desta cena, com centro e força próprios, por cima de fundo e peças (correção 20/11).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o produto final real" (objeto feito com o padrão);
  - "detalhe que dá nome" (a forma marcada pelo contorno na hora do nome).
- Nesta referência as lacunas foram preenchidas com: lona alemã com padrão splinter; uma "lasca" do padrão.
- Receita de tratamento de cada imagem: foto real recortada do objeto, sem cartão, sem sombra (alinhado ao reestudo); contorno creme fino à mão.
- Regra de escolha: frase de batismo ("se chamava X") → contorno na forma que justifica o nome, na palavra do nome. Teste em 2 temas: Claude Code → contorno no ícone de "agente" ao dizer "isso se chama agente"; café → contorno numa bolha da crema ao dizer "crema".

- Receita de tratamento (reestudo 20/11): foto recortada do objeto real (peça com ferragens, trama visível), cor de arquivo, sem contorno nem sombra.
- Receita de ILUSTRAÇÃO (reestudo 20/11): traço à mão creme quase branco de 6–7 px, chapado, cantos arredondados, contorno fechado em volta de UMA forma; revelado por "desenho" progressivo em passos de 2 quadros; não ferve depois de pronto.
- Teste de generalização: Claude Code → chicote da tela anterior para o print do produto real e um traço creme circula o botão que dá nome ao recurso; café → chicote para a foto da saca e o traço circula o selo que dá nome à variedade.

- Confiança: entrada e cortes = medido; posição do contorno, direção do traço e fade = observado.
