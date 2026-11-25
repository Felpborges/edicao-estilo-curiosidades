# V03-A20 · gravura (o lugar) + dois discos com recortes dos objetos do ritual
- Categoria: P14 · Disco creme com recorte (provisória do analista: (provisória) cartão-gravura + discos creme com recortes (objetos citados))
- Fonte: V03 quadros f2576–f2679 (107,44–111,74 s; 104 quadros ≈ 4338 ms) · 23,976 fps
- Fala: "houses had a room just for it. You'd poke your head through a curtain. With a mask over your face"
- Tipo de fala: descrição (lugar + objetos de um ritual)
- Gatilho: o cartão pipoca em f2576 (107441 ms), 39 ms ANTES do início da palavra nº 362 "houses" (107480 ms). Entra por cima da V03-A19, sem corte.
- Quadro-chave: f2670
- Camadas ativas: cena de corte (cartão) | grafismo (discos, recortes) | legenda
- Leitura dos strips: strip.jpg = f2574 a f2584, de 1 em 1, 8 colunas, linha a linha (pop da gravura); strip-saida.jpg = f2625 a f2662, de 1 em 1 (os dois discos crescem e recebem os recortes); strip-geral.jpg = f2574 a f2679, de 3 em 3. Detalhes do reestudo: detalhe-discos-sobrepostos.jpg = quadro f2670, região x200 y400 200x300 px, ampliada 2× sem suavizar (disco 2 por cima do disco 1, contorno do recorte da máscara e a sombra dele); detalhe-mesa-luz-realce.jpg = quadro f2676, região x0 y0 720x1280 px, ampliada 1×, contraste ×6 em volta da média (a luz central da mesa à direita do cartão).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala descreve um lugar e um ritual com objetos ("a room… a curtain… a mask"); a gravura de época mostra o lugar inteiro e cada objeto nomeado ganha um disco no instante do nome.
- Por que este design: o cartão novo pipoca POR CIMA do anterior, sem corte, porque é a continuação da mesma explicação (o pó → a sala do pó); os discos repetem o molde da V03-A19, então o público já sabe ler "disco = objeto da etapa".
- Por que estas cores: a gravura tem viragem amarelo-esverdeada (#605a41 nos meios-tons) e os discos creme ficam como o ponto mais claro da tela; nenhuma cor gráfica nova.
- Por que estes efeitos: contorno branco largo e sombra de 15–20 px caída para baixo nos recortes (relevo de papel colado), grão vivo nos claros, luz central da mesa à direita do cartão (o fundo não é preto chapado).
- Por que este movimento: o cartão assenta com estalo e a câmera avança (+16 a +18 %/s) enquanto a frase descreve a sala; quando chegam os objetos, ela recua (−23 %/s) e escorrega para baixo/esquerda para caber os dois discos.
- Sensação do movimento: de folhear um álbum e apontar detalhes; produzida pelo pop por cima sem corte, pelo avanço lento na gravura e pelos discos que nascem com ease-out e recebem o recorte grande que assenta.

## FORMA (fixa: reproduzir igual)
- Design: fundo escuro (#0f100b embaixo, #181713 em cima; f2600 x360 y1240 / y60) (medido). Cartão-gravura monocromática esverdeada/sépia (#605a41, f2600 x300 y700) com borda clara, ≈ 89 % da largura ao assentar (x≈60–700 em f2582); depois a câmera avança e anda, e o cartão passa a sangrar pela direita (f2600: borda esquerda x19–38) e, no fim, pela esquerda (f2670: borda direita x≈480) (remedido, folha f2582–f2658 e saltos de borda), girado (observado). Disco 1 (embaixo-esquerda): Ø final ≈ 357 px (≈ 50 % da largura), centro (34 %, 58–60 %) em f2634 (medido, blob); recorte do 1º objeto citado, em gravura clara, com contorno de papel. Disco 2 (meio-direita): Ø ≈ 343 px (47,6 %) em f2658, com a borda direita em x684 e centro x ≈ 71 %; no f_chave f2670, com a câmera recuando e indo para a esquerda, Ø ≈ 351 px (48,8 %), x≈259–610 × y367–718, centro (60,4 %, 42,4 %) (remedido, f2658 e f2670, coluna do centro e linha mais larga do disco; antes: Ø ≈ 300 px, ≈ 42 %, centro x ≈ 73 %, blob parcial); recorte do 2º objeto citado, em gravura (observado). Os dois discos se sobrepõem um pouco ao centro (observado).
- Movimento: cartão pipoca com estalo (f2576 47,7 · f2578 23,1 · f2580 18,3) (medido). Câmera em deriva crescente (dif 10 → 15) (medido) (corrigido no reestudo, f2582–f2679: pela `camera` é push-in +16 a +18 %/s até ≈ f2624, depois RECUO −22,9 %/s (f2638–f2650) quando os discos entram e deriva para baixo-esquerda no fim). Disco 1 cresce de Ø 119 (f2627) → 206 → 264 → 302 → 336 → 346 → 357 (f2634): 7 q, incrementos 87/58/38/34/10/11 = ease-out (medido). Recorte pipoca dentro dele ≈ f2632 (observado). Disco 2 cresce a partir de f2652 (Ø 225 → 259 → …) em ≈ 5 q e o recorte do 2º objeto pipoca em ≈ f2660 (medido parcialmente + observado). Saída: a V03-A21 pipoca por cima em f2680, sem corte.
- Passos internos:

| passo | quadro início | duração | tipo | palavra-gatilho (nº) | deslocamento |
|---|---|---|---|---|---|
| cartão-gravura | f2576 | 4 q de estalo | pop por cima | o lugar, sujeito da frase (362) | −39 ms |
| disco 1 + recorte | f2627 | 7 q | escala ease-out + pop | o verbo da ação (370, 109500 ms) | +73 ms |
| disco 2 | f2652 | ≈ 5 q | escala ease-out | a preposição que introduz o 2º objeto (376, 110740 ms) | −121 ms |
| recorte do 2º objeto | ≈ f2660 | ≈ 3 q | pop | o nome do 2º objeto (378, 110940 ms) | ≈ +3 ms |

- Ritmo: gravura sozinha 2,1 s (a frase que descreve o lugar); um disco por objeto citado, ≈ 1 s entre eles; cena 4,3 s.
- Som: nenhum efeito detectado (áudio mono, só voz) (medido).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- (correção da conferência, 2026-11-20: falas, nomes e objetos usados como âncora de tempo ou como descrição na FORMA e na CONSTRUÇÃO trocados pelo PAPEL; a fala literal fica só em Fala, Gatilho e CONTEÚDO)
- Textura (reestudo 20/11):
  - mesa: lisa, com LUZ CENTRAL: na coluna da direita (x690) a luma vai 22 (y100) → 29 → 35,5 (y400) → 35 (y550) → 29 → 20 → 17 → 15 (y1250); na linha de baixo (y1000) 19 → 22 no meio → 19 nas pontas (f2676). Cor #11120d–#252420, desvio por ponto 0,0–0,9 (sem textura). No realce (detalhe-mesa-luz-realce) aparece como mancha clara levemente fria à direita do cartão, centrada na altura dos discos.
  - gravura: impressão antiga com retícula/hachura, viragem amarelo-esverdeada; fundo escuro f2600 (x90 y320 90x90): #1f1d13, grão 11,43 níveis, ac1 +0,37 (traço fino de 1 px), manchas 3,66; ANDA com a câmera (+0,83 depois de alinhar −2,3/+0,5 px).
  - disco creme: papel com pontilhado, #e1dacc (f2670, x265 y500 30x80), luma 219, grão 7,97 níveis, ac1 +0,49, cinza (8,06/7,99/7,93); VIVO (−0,09 com f2671). Teste da conferência (alinhar pela peça e comparar o resíduo): f2670×f2671 (×1,0019, 374 pontos) 9,9 níveis nos claros × 3,8 nos escuros da gravura (piso sem grão: A-roll f2150×f2151, 0,57 nos claros) (medido).
  - recortes: um em gravura P&B de hachura vertical, outro em objeto claro de papel, contorno de papel branco ≈ 14 px (detalhe-discos-sobrepostos).
- Efeitos (reestudo 20/11):
  - vinheta global: nenhuma aplicada sobre a imagem; o que escurece para as bordas é a luz central da mesa (luma 35 no meio da altura → 15 no canto de baixo, f2676).
  - vinheta da imagem: nenhuma.
  - sombra: o recorte do disco 2 projeta sombra preta sobre o disco, caída para BAIXO (f2670, perfis de luma atravessando o contorno): embaixo (x380–420) o papel cai de ≈ 226 para 151 (−33 %) logo depois do contorno e volta em ≈ 18 px; à direita (y540–560) −19 %, ≈ 20 px; à esquerda −17 %, ≈ 15 px; em cima −11 %, ≈ 12 px (medido; corrigido na conferência: era "sombra cinza curta ≈ 3–4 px para baixo-esquerda"). Disco 2 (caixa 259,367,351,351, perfil alinhado na borda real): à direita, sobre a mesa, −31 %, volta em 16 px; em cima e embaixo só 1–2 px; sobre o disco 1, à esquerda, −8 % (quase nada). Cartão: borda de papel ≈ 7 px; em cima, sobre a mesa, −31 % e 10 px (caixa 7,122,466,705) (medido).
  - grão vivo nos claros (disco σ 8,0); desfoque de movimento, brilho, halo, profundidade, aberração: nenhum (folha geral de 3 em 3 sem borrão nos pops).
- Câmera (reestudo 20/11): f2582→f2600 PUSH-IN +16,3 %/s (a cena desce 1,4 px/q); f2604→f2624 +18,1 %/s (vai para a esquerda 1,6 px/q); f2638→f2650 RECUO −22,9 %/s, a cena sobe/esquerda (−2,0; −3,4 px/q) quando os discos entram; f2664→f2679 quase parada em escala (−2,5 %/s) mas descendo 3,4 px/q e indo para a esquerda (o cartão sangra pela esquerda no fim). Remedido sem a faixa da legenda (região 0,0,720,820): f2667→f2679 escala ×1,000 (+0,1 %/s) e a cena desce 3,3 px/q; f2673→f2679 +5,0 %/s, (+1,9; +3,3) px/q: a descida continua até o fim e um push-in leve começa nos últimos 6 q (medido; corrigido na conferência: era −2,5 %/s). Giro 0 (±0,05°). Discos andam com o cartão; a mesa fica.
- Cadência (reestudo 20/11): 24 imagens/s (câmera e crescimento dos discos, incrementos diferentes a cada quadro: 87/58/38/34/10/11 px); grão troca a cada quadro.
- Legenda nesta cena (reestudo 20/11): 7 blocos (#142–#148), 2–4 palavras, quebrando nas orações; o #142 entrou em f2571, 5 q ANTES do pop do cartão (f2576): sem corte, a troca não espera a imagem; o #148 atravessa a saída (f2674–f2685; a V03-A21 pipoca em f2680). Tarja 73,5 %, altura 46 px (y846–892) (medido na conferência: 73,0–75,1 em 10 quadros do V03; remedido aqui em 7 quadros do lote, 73,0–74,2 onde o fundo é limpo) (corrigido na conferência: era ≈ 72 %, mediana do censo; f2700 remedido: 74,0 %). Atrás da tarja: a parte de baixo da gravura (f2576–f2645, luma 60–90: tarja visível) e depois a mesa escura (f2646–f2679, luma ≈ 25–35: tarja some), porque a câmera sobe o cartão. "Texto branco grande" (48 q) = falso positivo (discos e pano claro da gravura).
- Entrada do texto (reestudo 20/11): sem texto do editor; os recortes entram como na V03-A19: grandes e girados no 1º quadro (o recorte 1 em f2631 transborda o disco), assentando em 2–3 q.

## CONSTRUÇÃO
1. fundo: mesa fixa na tela com luz central suave: preto quente #0f100b nos cantos de baixo (luma 15), #252420 (luma ≈ 35) no meio da altura atrás das peças, #161712 (luma 22) no alto; degradê radial muito largo, sem textura.
2. cartão-gravura do lugar: ≈ 89 % da largura ao assentar (x ≈ 60–700 em f2582), giro ≈ −1°, borda de papel ≈ 7 px + fio + sombra preta caída para baixo (em cima, sobre a mesa, −31 % e 10 px); pipoca POR CIMA da cena anterior em +0 ms com estalo de degraus de 2 q (picos 47,7 / 23,1 / 18,3).
3. grão vivo nos claros (como V03-A19), sorteado a cada quadro, nunca congela.
4. disco 1: papel creme, Ø ≈ 357 px (50 %), centro (34 %, 58–60 %) em f2634; nasce em +2127 ms: Ø 119 → 206 → 264 → 302 → 336 → 346 → 357 em 7 q (ease-out).
5. recorte 1: objeto citado, contorno branco ≈ 14 px, sombra preta sobre o disco caída para baixo: ≈ −33 % e 18 px embaixo, −17 a −19 % e 15–20 px dos lados, ≈ −11 % em cima (corrigido na conferência: era 3–4 px para baixo-esquerda); entra ≈ +2294 ms GRANDE e girado, transbordando o disco, e assenta em 2–3 q.
6. disco 2: Ø ≈ 343–351 px (48 %), meio-direita, encostando/sobrepondo o disco 1; nasce em +3170 ms em ≈ 5 q.
7. recorte 2: idem, entra ≈ +3420 ms.
8. câmera do grupo: push-in +16 a +18 %/s de +250 a +2000 ms; recuo −23 %/s com subida/esquerda de ≈ +2600 a +3100 ms; depois deriva descendo ≈ 3,3 px/q até o fim, com push-in leve (+5 %/s) nos últimos 6 q.
9. legenda fixa por cima.
- Linha do tempo (ms a partir do pop): 0 cartão pipoca por cima · 250–2000 push-in · 2127 disco 1 · ≈ 2294 recorte 1 · ≈ 2600 câmera inverte (recuo) · 3170 disco 2 · ≈ 3420 recorte 2 · 4338 a cena seguinte pipoca por cima.
- Parâmetros que dependem do conteúdo: imagem do lugar (cena larga com gente fazendo a ação), nº de objetos nomeados (= discos), em que palavra cada um entra (o nome do objeto), tamanho do recorte (pode transbordar o disco).
- O que NÃO fazer: cortar seco para a gravura (ela pipoca por cima da anterior); pintar a mesa de preto chapado (tem luz central); discos com sombra projetada forte (o disco tem −31 % e 16 px só sobre a mesa); recorte com sombra curta de 3–4 px (ela tem 15–20 px e é mais forte embaixo); recorte entrando pequeno e crescendo (entra grande e assenta).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: (1) imagem do LUGAR/situação descrita; (2) recorte de cada objeto citado na descrição (um por disco).
- Nesta referência as lacunas foram preenchidas com: gravura de um criado empoando um senhor numa sala; um cone de papel; uma máscara.
- Receita de tratamento de cada imagem: gravura de época monocromática; objetos como gravura/ilustração clara recortada com contorno branco, dentro de discos creme de ≈ 40–50 % da largura.
- Regra de escolha: DESCRIÇÃO de um ritual com objetos ("poke your head through a curtain, with a mask over your face") → a imagem do lugar + um disco por objeto nomeado, no instante do nome. Em outros temas: reel sobre Claude Code, "tinha uma sala só pra isso: você abria o terminal, colava a chave de API" → foto da sala/print + discos com ícone do terminal e da chave; reel sobre café, "você entrava na torrefação, punha o avental e as luvas" → gravura da torrefação + discos com avental e luvas.
- Receita de tratamento de cada imagem (reestudo 20/11): gravura de época com a viragem original (amarelo-esverdeada/sépia), retícula e hachura nítidas, sem dessaturar, sem vinheta própria; recortes de gravura P&B com fundo removido, contorno branco ≈ 14 px e sombra de 15–20 px caída para baixo; grão vivo do grupo nas partes claras.
- Receita de ILUSTRAÇÃO (reestudo 20/11): objeto tirado de gravura (hachura preta, sem cor) ou objeto claro desenhado; fundo removido; contorno de papel branco largo cortado com folga; sombra preta de 15–20 px caída para baixo (−33 % embaixo); o traço não ferve; revelado grande e girado dentro de um disco creme que nasceu 3–4 q antes, assentando em 2–3 q.
- Teste de generalização: reel sobre Claude Code → "as empresas tinham uma sala só pra isso: você entrava, sentava no terminal, colocava o crachá": foto de uma sala de servidores (lugar) + disco com recorte de um terminal + disco com recorte de um crachá. Reel sobre café → "toda torrefação tinha uma sala de prova: você punha o avental e pegava a colher de prova": gravura da sala + disco com avental + disco com colher.

- Confiança: estalo, crescimento do disco 1, cores = medido; disco 2 e recortes = medido parcialmente/observado; tamanho do cartão e giro = observado.
