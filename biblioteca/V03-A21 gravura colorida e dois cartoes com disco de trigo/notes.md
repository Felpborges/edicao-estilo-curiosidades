# V03-A21 · gravura colorida da ação + dois cartões da lista + disco com recorte (callback do trigo)
- Categoria: P08 · Pilha de cartões (provisória do analista: (provisória) cartões em pilha por item de lista + disco com recorte)
- Fonte: V03 quadros f2680–f2814 (111,78–117,40 s; 135 quadros ≈ 5631 ms) · 23,976 fps
- Fala: "while a servant turned your hair white. White hair said you had the time, the servants, and the wheat to spare."
- Tipo de fala: ação narrada → lista de 3 (consequência / status)
- Gatilho: o cartão pipoca em f2680 (111786 ms), 134 ms ANTES do início da palavra nº 382 "while" (111920 ms). Entra por cima da V03-A20, sem corte.
- Quadro-chave: f2800
- Camadas ativas: cena de corte (cartões) | grafismo (disco + recorte) | legenda
- Leitura dos strips: strip.jpg = f2678 a f2688, de 1 em 1, 8 colunas, linha a linha (pop da gravura colorida); strip-saida.jpg = f2749 a f2796, de 1 em 1 (cartão "tempo", cartão "criados", disco do trigo); strip-geral.jpg = f2678 a f2816, de 3 em 3. Detalhes do reestudo: detalhe-disco-trigo.jpg = quadro f2800, região x50 y500 250x240 px, ampliada 2× sem suavizar (disco creme, recorte com contorno solto e sombra curta, o recorte transbordando o disco); detalhe-estalo-f2680.jpg = quadro f2680, região x0 y80 360x300 px, ampliada 1× sem suavizar (1º quadro do estalo: cartão maior e girado, sem borrão).

## LEITURA DE EDITOR
- Por que esta cena aqui: fecha o bloco do pó com a ação (o criado empoando) e logo vira lista de 3 ("the time, the servants, and the wheat"); a lista pede uma imagem por item, na palavra.
- Por que este design: a gravura colorida da ação pipoca por cima da cena anterior (continuidade); os itens 1 e 2 são cartões que cobrem a ação, o item 3 já foi mostrado e volta no MESMO disco creme com o mesmo recorte (callback visual = "lembra do trigo?").
- Por que estas cores: a gravura colorida à mão (azul, verde e creme pastel) é a cena mais clara e alegre do trecho, combinando com "status"; os cartões da lista são pinturas escuras e quentes, então a pilha escurece quando a frase vira "custo".
- Por que estes efeitos: sopro de pó animado sobre a gravura (o "turned your hair white" acontecendo), grão vivo nos claros, borda de papel e sombra caída para baixo na pilha.
- Por que este movimento: estalo forte de 3 degraus no pop da gravura (marca a nova frase), avanço curto e recuo lento enquanto o criado age; depois 3 entradas em 1,7 s, uma por item, com a câmera quase parada para o olho contar.
- Sensação do movimento: de "lista batida na mesa", item por item; produzida pelo ritmo regular dos pops (≈ 0,55 s) e pela câmera que desacelera até quase parar (−1,4 %/s) no fim.

## FORMA (fixa: reproduzir igual)
- Design: fundo escuro #0f100b (f2720, x360 y1240) (medido). Cartão 1: gravura colorida à mão (tons pastel, papel creme; #403e31 na área escura, f2720 x300 y600) ≈ 95 % da largura, girado (observado). Cartão 2 (imagem do 1º item da lista, horizontal) no alto: x114–599 × y84–433 em f2800 (485 × 349 px = 67,4 % × 27,3 %); cartão 3 (imagem do 2º item da lista) embaixo: x≈212–619 × y426–762 em f2800 (≈ 407 × 336 px = 56,5 % × 26,3 %), ambos com borda branca de 7 px e girados alternadamente (remedido, f2800, saltos de borda; antes: os dois "≈ 2/3 da largura", observado). No f_chave o cartão 1 vai de x34 a x705 (93 %). Disco creme embaixo-esquerda, Ø 214 px (29,7 % da largura), x67–282 na linha y615, por cima dos cartões 1 e 3 e por baixo de nada (remedido, f2800; antes: Ø ≈ 1/3 da largura) com o recorte do 3º item da lista, o MESMO recorte da V03-A19 (callback) (observado).
- Movimento: cartão 1 pipoca com estalo (f2680 55,3 · f2682 26,2 · f2684 19,0) e push-in que desacelera (dif 16,5 → 10) (medido). Cartão 2 pipoca em f2751 (29,6 / 16,1 / 13,0) (medido); cartão 3 em f2764 (22,5 / 14,5 / 11,3) (medido). Disco nasce ≈ f2786 (±2) e o recorte do 3º item pipoca ≈ f2792 (observado na folha; o blob da cor do disco se confunde com o cartão claro). Parado/deriva leve (dif < 10) até o corte em f2815 (medido) (corrigido no reestudo, f2688–f2814: depois do push-in curto (+6,6 %/s até f2705) há um RECUO de −7,5 %/s (f2708–f2745) e −5,6 %/s (f2770–f2785); só no último 0,75 s a câmera quase para, −1,4 %/s).
- Passos internos:

| passo | quadro início | duração | tipo | palavra-gatilho (nº) | deslocamento |
|---|---|---|---|---|---|
| gravura colorida (ação) | f2680 | 4 q de estalo + push-in | pop por cima | 1ª palavra da frase (382) | −134 ms |
| cartão do 1º item | f2751 | 4 q | pop | o artigo do 1º item (394, 114700 ms) | +42 ms |
| cartão do 2º item | f2764 | 4 q | pop | o artigo do 2º item (396, 115280 ms) | +2 ms |
| disco | ≈ f2786 | ≈ 5 q | escala ease-out | o artigo do 3º item (399, 116220 ms) | ≈ −20 ms |
| recorte do 3º item | ≈ f2792 | ≈ 3 q | pop | o 3º item (400, 116460 ms) | ≈ −10 ms |

- Ritmo: a ação (a frase que a descreve) fica 3,0 s; depois a lista de 3 itens em 1,7 s (um a cada ≈ 0,55 s), cada item com sua imagem; a pilha completa fica ≈ 0,9 s até o corte.
- Som: nenhum efeito detectado (áudio mono, só voz) (medido).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- (correção da conferência, 2026-11-20: falas, nomes e objetos usados como âncora de tempo ou como descrição na FORMA e na CONSTRUÇÃO trocados pelo PAPEL; a fala literal fica só em Fala, Gatilho e CONTEÚDO)
- Textura (reestudo 20/11):
  - mesa: lisa com luz central (coluna x690 em f2800: 21,7 em y100, 21,3 em y900, 17,4 em y1100, 15,4 em y1250; o meio está coberto pelos cartões), fixa na tela.
  - gravura colorida: papel creme impresso, #ab9882 (f2720, x470 y240 70x70), luma 154, grão 7,71 níveis, ac1 +0,42, cinza (7,72/7,71/7,71), VIVO (+0,35 depois de alinhar com f2721: é o grão do grupo por cima do papel da gravura, que tem fibra própria). Teste da conferência: f2805×f2806 com a câmera parada (afim identidade, 584 pontos, sem interpolar), resíduo do grão fino 7,4 níveis nos claros (|dif| 9,1) × 1,8 nos escuros (piso sem grão: A-roll f2150×f2151, 0,57 nos claros) (medido).
  - pinturas da lista: óleo escuro e quente, textura original.
  - disco creme e recorte: como V03-A19 (papel pontilhado vivo; contorno branco ≈ 8–10 px em volta do corpo do objeto, as partes finas, como as pontas, saem do contorno sem papel; detalhe-disco-trigo).
  - sopro de partículas: nuvem branca semitransparente de borda macia saindo da mão de quem age até o ponto da ação (f2705–f2730), forma muda quadro a quadro (folha f2710–f2721, observado).
- Efeitos (reestudo 20/11):
  - vinheta global: nenhuma aplicada (só a luz central da mesa). Vinheta da imagem: nenhuma.
  - sombra: cai para BAIXO (corrigido na conferência: era "difusa e fraca nos cartões"). f2800, perfil alinhado na borda real nos 4 lados: cartão 2 (caixa 114,84,485,349) embaixo, sobre os cartões de trás, −96 % colado e volta em 27 px; à esquerda, sobre a mesa, −69 %, 12 px; à direita, sobre o cartão 1, −27 %, 12 px; em cima, sobre a mesa, −26 % só em 2 px. Cartão 3 (caixa 212,426,407,336) embaixo, sobre a mesa, −59 %, 12 px. Disco (caixa 67,508,215,214): à direita, sobre o cartão 3, −53 %, 25 px; à esquerda, sobre o cartão 1, −36 %, 15 px; em cima −7 %. Recorte sobre o disco (perfis y590–610 e y640–660): à direita do contorno −17 a −24 %, volta em 15–20 px; à esquerda nada (±3 %) (medido; corrigido na conferência: era "sombra cinza curta"; detalhe-disco-trigo).
  - desfoque de movimento: nenhum no estalo (detalhe-estalo-f2680: o cartão grande e girado está nítido).
  - grão vivo nos claros; brilho, halo, profundidade, aberração: nenhum.
- Câmera (reestudo 20/11): f2688→f2705 push-in +6,6 %/s, a cena anda para direita/baixo (+3,2; +2,5 px/q) logo depois do estalo; f2708→f2745 RECUO −7,5 %/s quase sem deslize; f2770→f2785 recuo −5,6 %/s subindo 1,5 px/q; f2796→f2814 quase parada (−1,4 %/s, −0,5 px/q); remedido sem a faixa da legenda (região 0,0,720,820): f2802→f2814 −1,3 %/s e f2808→f2814 −1,4 %/s, −0,4 px/q (mesmo valor). Giro 0 (±0,04°). Cartões e disco andam juntos; a mesa fica.
- Cadência (reestudo 20/11): câmera e pops a 24 imagens/s; o ESTALO da entrada anda em degraus de 2 q (posição e giro iguais em f2680/f2681 e em f2682/f2683, ver Entrada); perfil f2712–f2722 (com o sopro) 6,9–8,6 sem quadros iguais.
- Legenda nesta cena (reestudo 20/11): 9 blocos (#148–#156), 1–3 palavras; cada item da lista abre um bloco; o #148 atravessa a ENTRADA (f2674–f2685, vem da V03-A20; o pop é em f2680), o #156 termina no corte (f2814). Tarja 73,5 %, altura 46 px (y846–892) (medido na conferência: 73,0–75,1 em 10 quadros do V03; remedido aqui em 7 quadros do lote, 73,0–74,2 onde o fundo é limpo) (corrigido na conferência: era ≈ 74 %, mediana do censo). Atrás da tarja: a parte de baixo da gravura clara (f2680–f2750, luma ≈ 90: tarja bem visível) e depois a mesa escura sob a pilha (luma ≈ 26–28: tarja some). Cada item da lista tem bloco próprio que começa na palavra do item (bloco do 2º item em f2762, cartão em f2764; bloco do 3º item em f2779, disco em f2786). "Texto branco grande" (52 q) = falso positivo.
- Entrada do texto (reestudo 20/11): sem texto do editor. Estalo do cartão-gravura medido pela borda de cima (eti, f2679–f2686): f2680–f2681 borda em y ≈ 110 e giro −4,4° (≈ ×1,13); f2682–f2683 y ≈ 153, −2,0° (≈ ×1,03); f2684 y 163, ≈ 0° (assentado). São 3 degraus segurados 2 q cada (6 q no total), sem borrão e sem fade. O recorte do 3º item entra como na V03-A19 (grande → assenta).

## CONSTRUÇÃO
1. fundo: mesa fixa na tela com luz central (V03-A20).
2. (por baixo) a cena anterior continua lá e é coberta.
3. cartão 1, gravura colorida da ação: 93–95 % da largura, giro final ≈ 0 a −1°, borda de papel ≈ 7 px + fio + sombra preta caída para baixo. Pop por cima em 0 ms: degrau 1 (0–83 ms) ×1,13 e −4,4°; degrau 2 (83–167 ms) ×1,03 e −2,0°; degrau 3 (167 ms) ×1,0 e giro final. Sem borrão.
4. sopro de partículas: nuvem branca semitransparente, borda macia, saindo do instrumento para o ponto da ação, de ≈ +1043 a +2100 ms, forma animada quadro a quadro.
5. grão vivo (como V03-A19): sorteado a cada quadro nos claros, nunca congela.
6. cartão 2 (item 1 da lista): 485 × 349 px (67,4 % × 27,3 %) no alto (x114–599, y84–433 em f2800), giro ≈ +1,5°, sombra preta caída para baixo (−60 a −95 % colada embaixo e 12–27 px; −27 a −69 % e 12 px dos lados; quase nada em cima; corrigido na conferência: era "difusa e fraca"); pop com estalo em +2961 ms.
7. cartão 3 (item 2): ≈ 407 × 336 px (56,5 % × 26,3 %) embaixo-direita (x212–619, y426–762), giro ≈ −1,5°, por cima do cartão 2; pop em +3504 ms.
8. disco creme (item 3, callback): Ø 214 px (29,7 %), embaixo-esquerda (x67–282), por cima dos cartões 1 e 3; nasce em +4421 ms em ≈ 5 q (ease-out); recorte já visto antes entra em +4671 ms grande → assenta, transbordando o disco; sombra do recorte sobre o disco −17 a −24 % e 15–20 px; sombra do disco sobre os cartões −36 a −53 % e 15–25 px.
9. câmera do grupo: push-in +6,6 %/s até +1043 ms; recuo −7,5 %/s até +2711 ms; recuo −5,6 %/s; quase parada (−1,4 %/s) no último segundo.
10. legenda fixa por cima.
- Linha do tempo (ms a partir do pop): 0 / 83 / 167 degraus do estalo · 167–1043 push-in · ≈ 1043–2100 sopro de partículas · 1168–2711 recuo · 2961 cartão do item 1 · 3504 cartão do item 2 · 4421 disco do item 3 · 4671 recorte · 5631 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: imagem da ação (cena clara e colorida, se houver), nº de itens da lista (3), qual item é callback (volta como o mesmo recorte no disco), tamanhos dos cartões pelo formato das imagens.
- O que NÃO fazer: estalo suave contínuo (são 3 degraus segurados 2 q cada, ×1,13 → ×1,03 → ×1); apresentar o item já visto com imagem nova (volta o MESMO recorte); câmera correndo na hora da lista (ela quase para); legenda que espera o pop (a legenda segue a fala); sombra simétrica ou curta nos cartões e no recorte (ela cai para baixo, 12–27 px).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: (1) imagem da ação descrita; (2) uma imagem por item da LISTA falada (aqui 3 itens: tempo, criados, trigo); o item que já apareceu antes volta como o MESMO recorte (callback).
- Nesta referência as lacunas foram preenchidas com: gravura colorida de um criado empoando uma dama; pintura de um homem ocioso deitado na paisagem ("tempo"); painel de retratos de criados ("criados"); a espiga de trigo já mostrada.
- Receita de tratamento de cada imagem: pinturas/gravuras em cor natural, cartões de borda branca girados; o item já visto reaparece com o mesmo recorte no disco creme.
- Regra de escolha: LISTA de 3 itens no fim de uma explicação ("you had the time, the servants, and the wheat") → um cartão/disco por item, na palavra do item, empilhando; item metafórico ("the time") vira uma imagem que o encarna (alguém ocioso). Em outros temas: reel sobre Claude Code, "isso mostrava que você tinha tempo, equipe e GPU sobrando" → foto de alguém relaxando, foto de um time, recorte da GPU (callback); reel sobre café, "mostrava que você tinha tempo, criados e açúcar" → pintura ociosa, retrato de criados, recorte do açúcar.
- Receita de tratamento de cada imagem (reestudo 20/11): gravura colorida à mão com o papel creme original (fibra + o grão vivo do grupo, σ ≈ 7,7), pinturas da lista com cor e craquelado originais, nenhuma vinheta, nenhum filtro; recorte callback idêntico ao da 1ª aparição.
- Receita de ILUSTRAÇÃO (reestudo 20/11): recorte de objeto (planta, ferramenta) em ilustração botânica/gravura clara, fundo removido, contorno de papel branco 8–10 px só em volta do corpo do objeto (partes finas saem do papel), sombra cinza curta para o lado; traço parado; revelado dentro do disco creme com o estalo grande → assentado.
- Teste de generalização: reel sobre Claude Code → "enquanto o agente rodava os testes sozinho; isso dizia que você tinha tempo, equipe e orçamento sobrando": print do agente trabalhando (com um efeito de linhas passando no terminal) + cartão de uma agenda vazia + cartão de foto de equipe + disco com o recorte de moeda já usado antes. Reel sobre café → "enquanto o barista tirava o espresso; isso dizia que você tinha tempo, dinheiro e grão importado": foto do barista com vapor animado + cartão de relógio + cartão de cédulas + disco com o grão (callback).

- Confiança: estalos e perfil = medido; quadros do disco e do trigo = observado (±2 q); layout, tamanhos e conteúdo = observado.
