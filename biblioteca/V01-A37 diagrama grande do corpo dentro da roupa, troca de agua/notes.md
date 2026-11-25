# V01-A37 · diagrama grande: corpo dentro do contorno da roupa num disco teal; camada de água entra, esquenta, é trocada por água fria
- Categoria: P18 · Diagrama chapado com estados (provisória do analista: (provisória) diagrama-silhueta sobre disco de cor (estados + setas), cena longa que volta entre interrupções)
- Fonte: V01 quadros f2594–f2903 (108,08–121,00 s; 310 quadros ≈ 12917 ms) · 24 fps · coberto por V01-A38 (f2714–f2785) e V01-A39 (f2828–f2866)
- Fala: "Let in as little water as possible. And stop it from being swapped out for new cold water. (…) A little water against your skin is fine. (…) move is what freezes you."
- Tipo de fala: mecanismo + consequência (a única função da roupa, em 3 trechos)
- Gatilho: corte seco em f2594 = 108083 ms, −167 ms antes da palavra nº 351 "Let" (108250 ms).
- Quadro-chave: f2650
- Camadas ativas: cena de tela cheia | grafismo animado (camadas, setas, círculo à mão) | legenda
- Leitura dos strips: strip.jpg = quadros f2592 a f2606, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 15 células. strip-saida.jpg = quadros f2655 a f2675 (setas de troca), mesma regra, 21 células. strip-geral.jpg = quadros f2592 a f2900, de 7 em 7, 45 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-contorno-aspero.jpg = quadro f2650, região x190 y380 130x140 px, ampliada 3× sem suavizar · detalhe-disco-teal-realce.jpg = quadro f2650, região x20 y450 200x200 px, ampliada 2× sem suavizar, contraste ×6 em volta da média.


## LEITURA DE EDITOR
- Por que esta cena aqui: é o coração do vídeo (a regra "pouca água, sem troca"); o editor dá ao mecanismo a cena mais longa e volta a ela três vezes, entre provas reais, sempre já no estado seguinte.
- Por que este design: o corpo inteiro dentro do contorno da roupa, num disco teal maior que a tela (o corpo está DENTRO da água); a folga entre corpo e roupa é a camada que muda de cor.
- Por que estas cores: teal = água fria por fora e na camada; laranja = a mesma água já aquecida e o calor do corpo; preto áspero = o material. A troca teal ↔ laranja na camada É a explicação.
- Por que estes efeitos: papel amassado no disco (vinco visível), contorno preto com pontinhos (textura de espuma), corpo creme arenoso: tudo parece recortado e colado, não vetorial.
- Por que este movimento: estados mudam por cor (preenchimento contínuo de baixo para cima, troca de cor gradual) e setas que "estalam"; as fotos que cobrem a cena funcionam como cortinas que escondem a mudança de estado.
- Sensação do movimento: lenta e explicativa (cada mudança dura 0,5–0,8 s), com respiração de câmera quase nula (+1,2 a +2,7 %/s) e um leve giro; o grão meio vivo (parado nas pernas) mantém tudo tremendo de leve (alinhado ao reestudo).

## FORMA (fixa: reproduzir igual)
- Design (quadro cheio):
  - Disco teal #347f8a (mesmo de V01-A09) MAIOR que a tela: ocupa os 720 px na linha mais larga (corta nas duas laterais); topo do disco em f2650 y≈93 (7,3 % da altura), base ≈ y875 (remedido, f2650; antes y≈165 / 13 %, que não vale para nenhum quadro da cena: f2594 y141 na entrada, f2600 y108, f2790 e f2880 y91, a câmera aproxima); linhas finas onduladas claras = o meio de fora. (medido com disco.py)
  - Sujeito: silhueta creme #dfc6a3 aprox. (miolo; f2650, 360,500) com degradê laranja (o benefício) #cd8f64 no centro (f2700, 360,400); caixa do miolo claro f2620 x206–516, y212–868 = 310x656 px (43,1 % da largura, 51,2 % da altura), centro (50,1 %, 42,2 %); a parte de cima do sujeito, que fica fora do objeto e é mais cinza (#a19f93), começa em y≈122 (f2620), então a silhueta inteira vai de y≈122 a y≈870 (remedido, f2620, coluna x360). (medido)
  - Objeto que envolve o sujeito: contorno preto grosso em volta dele com uma folga entre os dois (a camada entre os dois), e borda de adesivo off-white por fora. (observado)
  - Camada fina entre sujeito e objeto: teal no estado inicial, laranja no estado ativado. (observado)
  - Setas: brancas curvas finas entrando pela abertura de cima (o fluxo que entra, na cor do estado inicial) e laranja grossas saindo pelas aberturas de baixo (o fluxo que sai, na cor do estado ativado). (observado)
  - Círculo à mão amarelo-mostarda (laço comprido) em volta da camada fina numa extremidade de baixo (à esquerda). (observado; traço de V01-A15)
- Movimento:
  - Entrada: corte seco; o disco ainda cresce e assenta em f2600, 6 q (perfil na região do sujeito x190 y110 340x760: f2594 89,8 → f2596 38,0 → f2598 19,7 → f2600 6,1 → f2602 4,0 = tremor) (remedido; antes 4 q / 2 imagens). (medido)
  - Cadência 12 imagens/s (fase par). (medido)
  - Quando volta de debaixo das fotos (f2784, f2866), o diagrama JÁ está no estado seguinte (o estado muda enquanto está coberto). (observado no strip-geral)
  - Saída: corte seco para o A-roll em f2904. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | sujeito + objeto no disco | f2594 | 6 q (250 ms) (remedido) | assenta | estalo | nº 351 | −167 ms |
  | camada fina entra (teal) | f2606 (remedido) | ≈ 16 q (667 ms) | cor preenche a folga de baixo para cima | contínua | nº 352 (108400) | +183 ms |
  | camada troca para o laranja | f2640 | ≈ 12 q (500 ms) | troca de cor | contínua | nº 358 (110320) | −320 ms |
  | setas brancas entrando pela abertura de cima | f2658 | ≈ 6 q (250 ms) | setas se desenham | estalo | nº 361 (110840) | −90 ms |
  | setas laranja saindo pelas aberturas de baixo | f2666 | ≈ 6 q (250 ms) | setas crescem | estalo | nº 363 (111160) | −77 ms |
  | camada volta a teal, o sujeito perde o laranja | f2692 | ≈ 20 q (833 ms) | troca de cor gradual | contínua | nº 367 (112180) | −13 ms |
  | (coberto por V01-A38) | f2714–f2785 | — | — | — | — | — |
  | volta laranja, camada parada; laço à mão numa extremidade de baixo | f2794 (remedido) | 6 q (250 ms), laço fechado em f2800 (remedido, folha f2786–f2828) | traço se revela | desacelera | nº 383 (116540) | −123 ms |
  | (coberto por V01-A39) | f2828–f2866 | — | — | — | — | — |
  | volta com setas de troca; o sujeito perde o laranja | f2880 | ≈ 16 q (667 ms) | laranja apaga | contínua | nº 398 (120140) | −140 ms |
  (quadros dos passos observado no strip-geral/strip-saida; durações aproximadas. Remedição: 1º passo, camada teal e laço conferidos por perfil e folha; camada laranja f2640 e passo final f2880 batem no perfil)
- Ritmo: 12,9 s no total (a cena mais longa do vídeo), visível em 3 trechos: f2594–f2713 (5,0 s), f2784–f2827 (1,8 s), f2866–f2903 (1,5 s). Nenhum trecho parado > ≈ 1 s. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Disco teal: papel amassado. f2650 região 40,560,120,80: #35818b, luma 113, grão 1,00 nível, manchas 0,80, ac1 +0,60, grão cinza (1,00/1,00/1,03); VIVO pela correlação simples (+0,25 / +0,39); pelo teste novo (f2650×f2652, afim da cena, região 15,440,170,300, pixels lisos de luma 60–150): resíduo/σ 1,17, correlação +0,37 → MEIO VIVO (parte do grão troca a cada imagem). No realce: vinco diagonal escuro e relevo largo de papel amassado; linhas onduladas claras de ≈ 3 px atravessam o disco.
  - Sujeito: creme arenoso. f2650 região 330,520,60,60: #ded0bc, luma 210, grão 4,58 níveis, ac1 +0,45 (≈ 1–2 px), cinza; VIVO pela correlação simples (+0,02). Teste novo (afim da cena, pares de 2 em 2, claros lisos da região 200,100,320,400): resíduo/σ 0,89–1,39 e correlação +0,24…+0,54 em 22 pares seguidos (f2620–f2634 e f2870–f2898), sem pares congelados → MEIO VIVO em toda a cena: bem acima do diagrama parado da V01-A34 (0,74 / +0,69) e abaixo do papel das fotos (1,2–1,5 / ≤ +0,2). Debaixo da foto da V01-A39 (f2845, região 0,600,720,235: pernas e borda do disco) mede PARADO (0,65 / +0,78; a conferência deu +0,77). (corrigido na conferência: era VIVO; a conferência pôs este diagrama entre os sem grão vivo; a minha medida dá meio vivo no tronco do sujeito, parado nas pernas: baixa confiança).
  - Estado quente: laranja #da783b (f2650 região 330,330,60,60), grão 1,48, manchas 3,82, VIVO pela correlação simples (+0,18 / +0,24; não remedido com o teste novo: região pequena, conta junto com o sujeito = meio vivo); degradê radial com pontilhado.
  - Contorno do envoltório: preto com pontinhos claros (textura porosa) e borda levemente irregular, adesivo off-white fino (≈ 3–4 px) por fora; a camada (teal ou laranja) é lisa e limpa (detalhe-contorno-aspero).
- Efeitos (reestudo 20/11):
  - Sombra: a silhueta projeta sombra escura difusa sobre o disco (halo escuro de ≈ 10–15 px em volta do adesivo, visível no realce); medido em f2650 (linhas y300–330, lado direito): o disco cai de 101 para 85 logo depois do adesivo (−16 %) e volta em ≈ 15 px. Disco sobre a mesa (medido, f2650, colunas x140–170 e x560–590, borda de cima): rampa de ≈ 20 px de L88 a L27 sem fio escuro e sem sombra separável fora dela (a borda do disco teal é macia, diferente do disco creme de V01-A29, que é nítido com fio de 1 px); nos lados o disco sai do quadro.
  - Vinheta, borda borrada, desfoque de movimento, aberração, brilho: nenhum (medido em f2650). Degradê: só o radial do estado quente.
- Câmera (reestudo 20/11): quase parada, com giro: f2600 → f2614 escala ×1,0070 (+1,2 %/s), centro (−0,01, −0,26 px/q), giro −0,44° (−0,03°/q); f2880 → f2894 ×1,0159 (+2,7 %/s), centro (+0,02, −0,49 px/q), giro +0,10°. O disco sobe devagar e gira um pouco. Fim da cena (medido, f2889 → f2901, região 0,0,720,830): ×1,0111 (+2,2 %/s), centro (+0,03, −0,42 px/q), giro −0,03°: o mesmo ritmo lento até o corte, sem recuo. Mesa parada.
- Cadência (reestudo 20/11): 12 imagens/s (perfil do sujeito f2595–f2616: 0,00 / 31,9 / 0,01 / 16,7 / 0,18 / 5,2 / 0,27 / 3,2 / 0,11 / 3,3 / 0,00 / 3,9 / 0,14 / 5,4 …; quadros pares mudam; o 3–5 por imagem é o grão vivo + a camada enchendo).
- Legenda nesta cena (reestudo 20/11): 17 blocos ao longo de 12,9 s (incluindo os trechos cobertos por V01-A38 e V01-A39); o 1º (4 palavras; f2594) entra no quadro do corte; o último (2 palavras, a consequência; f2884–f2903) termina no corte. Texto #ebde53, 68 %. A tarja fica sobre a borda de baixo do disco: em cima teal (L95–114 → L23–33 dentro), embaixo mesa (L20 → L4–6): a mesma tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %). O censo dá "luma dentro 27 × fora 26" porque mede o "fora" na mesa e o "dentro" no teal. Nenhum sumiço.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #181516, parada.
2. disco teal #35818b de papel amassado (vinco visível), maior que a tela (corta nas laterais), topo em y≈93 e base em y≈875 (f2650); linhas onduladas claras horizontais de ≈ 3 px; grão ≈ 1 nível meio vivo (só parte dele troca a cada imagem); borda de cima macia, rampa de ≈ 20 px, sem fio escuro.
3. sombra do sujeito: halo escuro difuso sobre o disco, −16 % junto do adesivo, some em ≈ 15 px.
4. contorno do envoltório: faixa preta com pontinhos claros (poroso), borda irregular, adesivo off-white 3–4 px por fora.
5. camada entre o envoltório e o sujeito: faixa lisa de ≈ 12 px, teal ou laranja conforme o estado.
6. sujeito: silhueta creme arenosa #ded0bc com grão ≈ 4,6 níveis meio vivo (parte do ruído sorteada de novo a cada imagem); miolo x206–516, y212–868 (43,1 % × 51,2 %); cabeça acima do envoltório, mais cinza (#a19f93).
7. estado quente: degradê radial laranja #da783b no centro do sujeito, com pontilhado.
8. setas: brancas finas curvas entrando por cima; laranja grossas saindo por baixo.
9. laço à mão amarelo translúcido numa extremidade de baixo.
10. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Animação: entrada 0 ms (f2594) corte com o disco a ≈ 110 % → 83 ms → 167 ms → 250 ms assentado (3 imagens). Camada teal enche de baixo para cima 500–1167 ms. Camada troca para laranja 1917–2417 ms. Setas brancas estalam 2667 ms (250 ms); setas laranja 3000 ms (250 ms). Camada volta a teal e o sujeito perde a cor quente 4083–4917 ms. [coberta por V01-A38 de 5000 a 7958 ms; o estado muda escondido]. Laço à mão 8333–8583 ms. [coberta por V01-A39 de 9750 a 11375 ms]. A cor quente apaga de novo 11833–12500 ms. Câmera: +1,2 → +2,7 %/s, sobe ≈ 0,3–0,5 px/q, giro até −0,44° em 0,6 s. Passos de 2 quadros.
- Linha do tempo (ms a partir do corte f2594 = 108083 ms): 0 corte · 250 assenta · 500 camada teal · 1917 laranja · 2667 setas entrando · 3000 setas saindo · 4083 volta a teal · 5000–7958 fotos por cima · 8333 laço · 9750–11375 foto por cima · 11833 cor quente apaga · 12917 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: o sujeito, o envoltório (contorno), a camada e seus 2 estados de cor, o que entra e o que sai (setas).
- O que NÃO fazer: disco liso (precisa do vinco e do grão meio vivo), grão tão forte e tão vivo quanto o do papel das fotos (aqui ele é mais fraco e só em parte re-sorteado), contorno vetorial limpo (aqui é áspero com pontinhos), mudar o estado com a cena visível quando ela está coberta pelas fotos (a troca acontece escondida), setas animadas suaves (estalam), girar mais de ≈ 0,5°.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o sujeito dentro do objeto": silhueta + contorno do objeto em volta.
  - "a camada entre os dois": cor que muda de estado (frio/quente).
  - "o fluxo de troca": setas de entrada e saída.
  - "o ponto bom": o que circular à mão.
- Nesta referência as lacunas foram preenchidas com: corpo dentro da roupa (cabeça para fora, mais cinza); água fina, fria (teal) e aquecida (laranja); calor no tronco; água fria entrando no pescoço e quente saindo pelas pernas; a camada fina na perna esquerda; ondas = água.
- Receita de tratamento de cada imagem: ilustração chapada de papel recortado, não vetorial (alinhado ao reestudo), sobre disco teal gigante; silhueta com degradê de calor; contorno preto grosso + adesivo; setas finas brancas e grossas laranja; círculo amarelo à mão.
- Regra de escolha: o "trabalho" do objeto explicado em etapas (deixar entrar pouco → não deixar trocar) vira um único diagrama que fica na tela e muda de estado a cada frase; fotos reais interrompem para dar prova e o diagrama volta no estado seguinte.
- Teste de generalização: (1) Claude Code: robô dentro de uma "caixa de contexto"; camada fina de texto entra (azul), fica útil (verde); setas de "lixo" entrando e saindo; laço na camada boa. (2) café: grão dentro do filtro; camada de água fina, esquenta; setas de água nova entrando e café saindo.
- Receita de ILUSTRAÇÃO (reestudo 20/11): silhueta frontal inteira em papel creme arenoso com grão meio vivo no tronco e parado nas pernas (alinhado ao reestudo), dentro de um contorno preto de textura porosa com borda irregular e adesivo off-white fino; folga lisa entre os dois que troca de cor (teal frio ↔ laranja quente); calor radial pontilhado; disco de fundo em papel teal amassado maior que a tela, com ondas claras finas; setas finas brancas e grossas laranja; destaca-se pelo contraste creme × teal e por uma sombra escura curta.
- Teste de generalização (reestudo 20/11): (1) Claude Code: "deixe entrar o mínimo de contexto e não troque ele a toda hora" → silhueta de robô dentro de um contorno de "janela", a folga troca de cor quando entra contexto novo, setas finas entrando e grossas saindo. (2) café: "a garrafa deixa entrar pouco ar e não deixa ele circular" → silhueta da garrafa com a folga entre as paredes trocando de teal para laranja, setas de ar entrando e saindo.

- Confiança: cores, caixa do corpo, entrada e tempos de saída medido; ordem dos estados e setas observado; durações dos passos observado.
