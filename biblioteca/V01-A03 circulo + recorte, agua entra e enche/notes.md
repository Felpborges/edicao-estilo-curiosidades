# V01-A03 · disco creme + recorte do objeto; o "problema" entra e enche o objeto (cena com passos)
- Categoria: P14 · Disco creme com recorte (provisória do analista: (provisória) palco de círculo creme + recorte-adesivo, com animação de preenchimento desenhada por cima (diagrama sobre foto))
- Fonte: V01 quadros f83–f200 (3,46–8,33 s; 118 quadros ≈ 4917 ms) · 24 fps (remedido: último quadro visível f200, um pedaço do disco no canto inferior esquerdo; antes f198)
- Fala: "cold water pours inside. Down your neck, up your sleeves, right against your skin."
- Tipo de fala: mecanismo (com lista: os pontos por onde entra)
- Gatilho: entra em f83 = 3458 ms, +58 ms depois do início da palavra nº 13 "cold" (3400 ms) (legenda "cold water" troca em f80, a cena 3 quadros depois).
- Quadro-chave: f99
- Camadas ativas: cena de tela cheia | legenda | grafismo animado (água) | transição (saída)
- Leitura dos strips: strip.jpg = quadros f81 a f92, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 12 células. strip-saida.jpg = quadros f193 a f200, de 1 em 1, 8 colunas; 8 células. strip-geral.jpg = quadros f81 a f198, de 3 em 3, 8 colunas, 40 células. Cada célula traz o nº do quadro e o tempo. Detalhes do reestudo: detalhe-agua-borda.jpg = quadro f99, região x290 y130 140x140 px, ampliada 3× sem suavizar · detalhe-gota.jpg = quadro f99, região x480 y420 90x90 px, ampliada 3× sem suavizar · detalhe-whoosh-borrao.jpg = quadro f197, região x60 y250 300x300 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala descreve o que acontece DENTRO do objeto, que não se vê numa foto; o editor volta ao mesmo objeto do gancho (o espectador já o conhece) e desenha o invisível por cima dele.
- Por que este design: foto real + desenho chapado por cima = "raio-X de livro didático"; a água fica presa à silhueta do objeto, e as gotas entram pelos pontos que a fala cita, na ordem em que são ditos (pescoço, punhos, pés).
- Por que estas cores: teal (#2a5e6b → #357f8c) é a cor-código da água no vídeo inteiro; frio contra o creme do disco e contra o navy do objeto, legível sem branco.
- Por que estes efeitos: borda da água esfumada (10–12 px) para parecer líquido e não adesivo; as gotas, ao contrário, têm forma dura de bastão com brilho no eixo, como "ícone" de gota; o borrão forte na saída cola esta cena na seguinte.
- Por que este movimento: o enchimento cresce a cada imagem em degraus (12/s), acompanhando a lista falada; a câmera para enquanto a água entra, depois aproxima (V01-A04) para a parte que a fala nomeia, e uma lupa abre (V01-A05) quando a fala chega à pele.
- Sensação do movimento: a água "invade" aos poucos, inevitável, e a câmera chega perto como quem aponta; produzida pelo preenchimento em degraus de 83 ms, gotas em queda linear e câmera parada (f89–f101, ×0,9996) seguida de zoom +5,6 %/s.

## FORMA (fixa: reproduzir igual)
- Design (f89–f99, quadro cheio):
  - Fundo escuro igual ao de V01-A01. Disco creme com grão de papel, linha mais larga 588 px = 81,7 % da largura (f89 e f91, linha y448–457, x66–653), centro x 49,9 %; centro vertical y457 = 35,7 % (remedido, f99: ponto mais largo do disco em y405–510), topo ≈ y164 (12,8 %, escondido atrás do recorte, inferido de centro + raio) e base y749 (58,5 %) (remedido, f99; o y235 antigo não era o topo do disco). (medido com disco.py)
  - Recorte do objeto-tema (outra vista do mesmo objeto de V01-A01, de frente) com o mesmo contorno de adesivo off-white ≈ 10 px de V01-A01; navy #1d202c (f99, 300,400). Objeto mais alto que o disco: passa do disco embaixo. (medido / observado)
  - Grafismo do agente que invade o objeto (cor medida nesta cena no reestudo: #2a5e6b em f99 na parte de cima e #317584–#357f8c em f165 com o objeto cheio; corrigido no reestudo, f99/f165: era "#3a8d99 aprox." tirado de outra cena): gotas e preenchimento teal chapado #3a8d99 aprox. (cor do preenchimento depois de cheio: #ded6cc é o adesivo; teal amostrado na cena de corte #347f8a em f2620, mesmo tom) desenhados DENTRO da silhueta do objeto, com bordas arredondadas e leve translucidez; gotas como bastões curtos arredondados que caem de fora para dentro pelas aberturas do objeto (os pontos de entrada citados) e escorrem pelas extremidades de baixo. Linhas tracejadas finas claras indicam o fluxo dentro da parte central do objeto (observado em f155–f161). (observado; cor teal medido em outra cena, ver V01-A31)
  - Ordem: fundo → disco → recorte → agente (por cima do recorte, recortada pela silhueta) → legenda. (observado)
- Movimento:
  - Entrada: cai por cima da foto anterior (V01-A02), que desliza para a esquerda por baixo. Disco entra maior e assenta em 2 imagens (4 quadros, 167 ms): linha mais larga f83 644 px (109,5 %) → f85 606 (103,1 %) → f87 588 (100 %), igual em f89 (remedido, f87; antes 3 imagens, 6 q, 250 ms). Curva de estalo (salto grande na 1ª imagem). (medido)
  - Cadência: 12 imagens/s (diferença só nos quadros ímpares, f89–f119). (medido)
  - Permanência: animação contínua do agente de f85 a f165; punch-in f119–f151 (pasta V01-A04); lupa a partir de f167 (pasta V01-A05).
  - Saída: 6 q, f195–f200 (remedido) · "whoosh" em 2 imagens: f195 e f197 com borrão de movimento forte no recorte e no disco (o disco encolhe e vai para a esquerda), depois em f199 a foto seguinte cobre tudo e um pedaço do disco ainda escapa pelo canto inferior esquerdo até f200. Diferença por imagem: f195 23,5 · f197 48,5 · f199 107. (medido no perfil; direção observado no strip-saida)
- Passos internos:
  | passo | quadro de início | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | 1 disco + recorte assentam | f83 | 4 q (167 ms) (remedido) | escala 109,5 → 100 % | estalo | nº 13, 1ª palavra do bloco (3400 ms) | +58 ms |
  | 2 1ª gota teal do agente desce do topo até o 1º ponto de entrada | f85 | ≈ 6 q (250 ms) | translação vertical para baixo | linear (observado) | nº 14, o agente nomeado (3620 ms) | −162 ms |
  | 3 gotas entram pelo 2º ponto de entrada; enche a parte de cima do objeto | f89 | ≈ 12 q (500 ms) | gotas em diagonal para dentro + preenchimento que "cresce" | contínua | nº 15, o verbo (4000 ms) | −292 ms |
  | 4 enche as extremidades; gotas pingam das extremidades de baixo | f101 | ≈ 18 q (750 ms) | preenchimento subindo das extremidades | contínua, acelera (diferença 3 → 8 por imagem f101–f117) | nº 16, fim da frase (4620 ms) | −412 ms |
  | 5 parte central do objeto enche, linhas tracejadas de fluxo | f129 | ≈ 32 q (1333 ms) | preenchimento da parte central de cima para baixo durante o punch-in | contínua | nº 17, 1º item da lista (5380 ms) | −5 ms |
  | 6 objeto todo teal (cheio) | f161 | até f198 | parado, só tremor | — | nº 22, fim do 2º item | — |
  (quadros de início medido no perfil e no strip-geral; durações observado)
- Ritmo: 4917 ms na tela (remedido, até f200), a mais longa do hook, porque a fala é uma lista de 3 pontos de entrada e cada um ganha um passo visual. Nenhum momento parado por mais de ≈ 1,5 s (f161–f195 tem a lupa entrando). (medido)
- Som: nenhum efeito detectado (áudio mono; o meio só mostra a voz). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Fundo (mesa): o mesmo de V01-A01 (papel escuro quase liso, parado, poça de luz fixa).
  - Disco creme: papel com fibra, `textura` f99 em 160,600,50,50: grão 5,2, manchas 1,6, ac1 +0,46 (grão de 1–2 px). VIVA de novo: f99×f101 +0,04 e f89×f91 +0,04 → o papel ferve a 12/s em toda cena com disco. Teste novo (f91×f93, alinhado pela cena, claros lisos da região 80,350,120,200): resíduo ÷ σ 1,39 = VIVO; no par f157×f159, claros da cena inteira 1,27. (medido)
  - Contorno de adesivo: o mesmo de V01-A01 (off-white ≈ 10 px com grão).
  - Água (desenho): família tinta chapada sem grão próprio (σ 0,6–1,1 dentro da mancha, f99 e f165); não ferve: muda só porque cresce. Teste novo de grão (f157×f159, alinhado pela cena 0,0,720,820, pixels lisos de luma 60–150): σ 0,69 e resíduo 1,05 níveis, no piso da compressão (o disco no mesmo par dá 3,44) → PARADA. (medido)
  - Foto do objeto: textura da foto, anda com a câmera. Teste novo (f89×f91, região 270,300,180,300, câmera parada): escuros lisos resíduo ÷ σ 0,55 (0,23 níveis) = PARADA. (medido)
- Efeitos (reestudo 20/11):
  - Borda da água esfumada: rampa de 12 px na lateral (linha y200 em f99: luma 29 em x300 → 83 em x312) e de 10 px embaixo (coluna x360: 88 em y233 → 36 em y245) → desfoque de borda ≈ 4–5 px de raio; sem contorno.
  - Gota: bastão de pontas redondas, teal mais escuro na borda e fio de brilho claro de 2–3 px no eixo (detalhe-gota; luma 141 com σ 33 na gota de x515 y462); borda dura, sem esfumado.
  - Sombra do disco: CAI PARA BAIXO (`sombra` 4 lados alinhada, f91, caixa 66,164,588,585): embaixo −55 % no 1º px fora e volta ao fundo em 22 px; esquerda −25 % e direita −26 %, voltam em 11–13 px; em cima −8 % só no 1º px (medido; corrigido na conferência: era "as mesmas de V01-A01, contato 6–8 px"). Sombra do adesivo sobre o disco: a de V01-A01 (dos lados 12–15 px, −25 a −30 %; nenhuma em cima). A água e as gotas não têm sombra.
  - Desfoque de movimento na saída: f195 e f197 com borrão forte e uniforme em tudo (detalhe-whoosh-borrao: raio ≈ 8–12 px, sem rastro direcional nítido), diferença 22,3 → 39,9 → 46,7 em f195/f197/f199.
  - Vinheta, brilho, profundidade, grão global, aberração: nenhum (medido em f99: água σ ≈ 1, borda do disco nítida).
- Câmera (reestudo 20/11): parada enquanto a água entra (`camera` f89→f101: ×0,9996, 0 px); zoom in a partir de f101 (f101→f117: ×1,0368, +5,6 %/s, desce 1,9 px/q), que emenda no punch-in de V01-A04 (f119–f151); depois recua (f155→f165: ×0,983, −4,1 %/s) e segue recuando com a lupa aberta (f177→f193 na metade esquerda: −7 %/s; fim f185→f193 na região 0,0,720,820: −6,8 %/s e o conjunto sobe 2,7 px/q e vai 2,1 px/q à direita, sem frear antes do borrão de saída; medido). O fundo não anda.
- Cadência (reestudo 20/11): 12 imagens/s na câmera, no disco (textura) e no enchimento (diferença só nos ímpares, f89–f119, medida antiga confirmada); a saída também troca nos ímpares (f195, f197, f199; f194/f196/f198/f200 ≈ 0).
- Legenda nesta cena (reestudo 20/11): 7 blocos, 1 por item da lista: o sujeito da frase (f80–f96, 2 palavras, entra 3 q ANTES do corte e atravessa a chegada da cena), o verbo (f97–f127, 2 palavras), o 1º item da lista (f128–f146, 3 palavras), o 2º item (f147–f165, 3 palavras), o 3º item partido em dois (f166–f184 e f185–f197, 2 + 2 palavras) e a virada que abre a cena seguinte (f198–f208, 2 palavras, atravessa a saída borrada f199). Cor #ecde55. Atrás da tarja: as pernas do objeto e as gotas que pingam (a foto e o adesivo descem até y≈830 e, no punch-in, passam por trás da tarja): censo f90–f198 dá luma fora 107 e tarja 29 → aqui a tarja preta pura a 74 % (medida direta da conferência no vídeo; o 0,71 do censo subestima: corrigido na conferência: era "opacidade 0,71") fica visivelmente cinza-escura, não preta. Gotas caem até y≈890, por trás e por baixo da tarja. Nenhum outro texto (o "texto branco grande" do censo é o contorno do adesivo).

## CONSTRUÇÃO
1. fundo: mesa fixa de V01-A01.
2. disco: creme Ø 81,7 % da largura (588 px), centro 49,9 % × 35,7 %, papel com fibra que ferve a cada imagem; sombra caída para baixo (22 px embaixo a −55 %, 11–13 px nos lados a −25 %, nada em cima); entra com 109,5 % (0 ms), 103,1 % (83 ms), 100 % (167 ms).
3. recorte do objeto: foto recortada de frente (sem grão vivo), adesivo off-white 10 px + sombra dos lados 12–15 px e nenhuma em cima (corrigido na conferência: era "sombra em volta"), mais alto que o disco (sai embaixo até y≈830). Entra junto com o disco.
4. água (máscara = silhueta da FOTO, sem o contorno de adesivo): mancha teal #2a5e6b (sobre a parte escura) a #357f8c (cheia), opacidade ≈ 80–100 %, borda esfumada de 10–12 px, sem contorno nem sombra; cresce em degraus de 1 imagem (83 ms) a partir de cada ponto de entrada: 1º ponto em 83 ms, 2º em 250 ms, extremidades a partir de 750 ms, parte central de 1917 ms a 3250 ms (de cima para baixo); linhas tracejadas finas claras (2 px) no sentido do fluxo dentro da parte central.
5. gotas: bastões teal de pontas redondas (≈ 12–15 px de espessura, 40–60 px de comprimento), borda mais escura e fio de brilho claro no eixo; caem em linha reta e velocidade constante de fora até o ponto de entrada; ficam POR CIMA do adesivo e do disco; também pingam das extremidades de baixo até a faixa da legenda.
6. câmera: parada até 750 ms; zoom in +5,6 %/s de 750 ms até ≈ 1500 ms, emendando no punch-in de V01-A04 (até 2833 ms); recuo de −4 a −7 %/s até a saída, sem frear (−6,8 %/s nos últimos 8 quadros).
7. lupa (V01-A05) a partir de 3500 ms.
8. saída: em 4667 ms (f195) e 4750 ms (f197) tudo leva borrão forte (raio 8–12 px) e o conjunto encolhe e vai para a esquerda; em 4833 ms (f199) a cena seguinte cobre tudo; um pedaço do disco escapa no canto inferior esquerdo até 4917 ms.
- Linha do tempo (ms a partir da entrada f83): 0 disco + recorte 109,5 % · 83 1ª gota (topo) · 167 assentado · 250 gotas no 2º ponto, enche em cima · 583 legenda do verbo · 750 enche extremidades, gotas pingam embaixo; zoom in começa · 1500 legenda do 1º item da lista · 1500–2833 punch-in (V01-A04) e enchimento da parte central · 2667 legenda do 2º item · 3250 objeto todo cheio · 3458 legenda do 3º item (1ª metade) · 3500 lupa abre (V01-A05) · 4250 legenda do 3º item (2ª metade) · 4667–4750 borrão de saída · 4833 cena seguinte.
- Parâmetros que dependem do conteúdo: o número e a ordem dos pontos de entrada (seguem a fala), a forma da máscara (silhueta do objeto), a cor do agente (água = teal; calor = laranja, ver V01-A09), a duração (um passo por item falado).
- O que NÃO fazer: água com borda dura de vetor (é esfumada 10–12 px); água pintando por cima do contorno de adesivo (fica dentro da foto); gotas esfumadas (são duras, com brilho); enchimento suave a 24/s (cresce em degraus de 83 ms); câmera andando enquanto a água entra (fica parada nesse trecho); sombra na água.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "objeto do tema": foto recortada do objeto (mesmo recorte de V01-A01 ou outra vista).
  - "o agente que invade o objeto": forma chapada de cor (aqui água) animada entrando pelas aberturas.
  - "pontos de entrada": as aberturas citadas na fala, na ordem em que são ditas.
- Nesta referência as lacunas foram preenchidas com: roupa de mergulho sem capuz; água teal; pescoço, punhos e tornozelos.
- Receita de tratamento de cada imagem: foto real recortada com adesivo off-white de 10 px; o agente é ilustração vetorial chapada, sem contorno, cor viva do sistema (teal), um pouco translúcida, recortada pela silhueta da foto; gotas em bastão arredondado.
- Receita de ILUSTRAÇÃO (reestudo 20/11): o agente é tinta chapada digital (sem grão, σ ≈ 1), uma cor só do sistema (teal #2a5e6b–#357f8c), opacidade 80–100 %, borda esfumada de 10–12 px, sem contorno e sem sombra, recortada pela máscara da foto (não invade o adesivo); destaca-se do fundo por ser a única cor fria saturada sobre o navy e o creme; não ferve (só cresce, em degraus de 1 imagem); revelada por crescimento a partir dos pontos de entrada. Os "ícones" de movimento (gotas) são o oposto: bastão de borda dura, teal com borda mais escura e fio de brilho no eixo, caindo em linha reta. Linhas tracejadas finas claras marcam o fluxo dentro da mancha.
- Regra de escolha: diagrama do mecanismo desenhado SOBRE a foto real do objeto. A fala descreve o que acontece dentro do objeto → anima-se isso por cima do próprio objeto, na ordem da fala.
- Teste de generalização: (1) Claude Code: "o contexto entra pelo prompt, pelos arquivos, pelas ferramentas" → recorte de um notebook; blocos de cor entram pela tela e enchem a "memória" desenhada por cima. (2) café: "a água entra pelo topo, passa pelo pó e desce" → recorte de um coador; água chapada desce por dentro dele.

- Confiança: tamanhos, tempos e cadência medido; cores do agente medido em cena equivalente; durações dos passos internos observado no strip-geral; direção da saída observado.
