# V05-A15 · tintureiro na praia (3D, sépia)
- Categoria: P24 · Cena 3D narrativa (provisória do analista: (provisória) cena 3D low-poly de personagem, câmera fixa, tom sépia)
- Fonte: V05 quadros f1010–f1121 (42,13–46,76 s; 112 quadros ≈ 4671 ms) · 23,976 fps
- Fala: "It came from a spiny sea snail called the murex. So the snail is purple inside, right?"
- Tipo de fala: mecanismo (definição: de onde vinha + pergunta retórica)
- Gatilho: entra por corte seco em f1010 (42 128 ms), 2 ms antes do início da palavra nº 152 "It" (42 130 ms). Conferido: dif 84,5 em f1010 e legenda "It came from" no mesmo quadro.
- Quadro-chave: f1030
- Camadas ativas: b-roll 3D | grafismo (V05-A16 rótulo, V05-A17 objeto que salta + rótulo) | legenda
- Leitura dos strips: strip.jpg = quadros f1008 a f1030, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 23 células. strip-geral.jpg = quadros f1008 a f1121 (amostrado), 8 colunas. detalhe-personagem-objeto.jpg = quadro f1030, região x180 y110 320x420 px, ampliada 1× sem suavizar (rosto pintado em cor quente, roupa lisa em sépia escura, objeto na mão em cor natural com detalhe alto). detalhe-fundo-realce.jpg = quadro f1030, região x0 y250 240x240 px, ampliada 2× sem suavizar, contraste ×6 em volta da média (foto real de pedras desfocada em sépia).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala define a origem ("vinha de um bicho do mar"); um personagem da época apresenta o objeto como um guia de museu, de frente para a câmera.
- Por que este design: personagem de corpo inteiro, quase centrado, câmera fixa; o objeto citado pequeno na mão (13,5 % × 6 % do quadro) e com rótulo de personagem no topo: retrato de "quem e o quê".
- Por que estas cores: cenário e roupa em sépia escura (#3c2f24, #4f3926); rosto em cor quente de pintura e o objeto na cor natural (#865f3e): a cena inteira em tons de marrom e só o objeto com detalhe e cor próprios.
- Por que estes efeitos: fundo fotográfico desfocado (praia/pedras, grão 2,9) e vinheta forte embaixo e nos lados (borda 21 %) isolam o personagem como num palco escuro.
- Por que este movimento: câmera parada: o movimento fica no personagem (levanta, gira o objeto) e no objeto que salta para a câmera (A17); a imobilidade faz o salto ser o evento.
- Sensação do movimento: apresentação calma, "deixa eu te mostrar isto"; produzida pela câmera fixa (×1,002 em f1100–f1118), gestos lentos do boneco (dif 2 a 4) e pausas com dif 0.

## FORMA (fixa: reproduzir igual)
- Design: personagem 3D low-poly (mesmo estilo de V05-A09: corpo de blocos, rosto de retrato antigo pintado; alinhado ao reestudo), de corpo inteiro, um pouco à direita do centro: roupa x ≈ 300–555 (42–77 %, centro ≈ 59 %), com a mão e o objeto citado x ≈ 186–575 (26–80 %), topo do cabelo y ≈ 118 (9 %), barra da roupa y ≈ 730 (57 %), pernas somem no escuro em y ≈ 820 (remedido, observado no still f1030; antes "centrado, x ≈ 30–70 %"), de frente para a câmera, segurando o objeto citado; fundo: o cenário onde o objeto é encontrado, em sépia/marrom escuro: #46382c (f1030, x100 y300), roupa #4c3724 (f1030, x330 y600), chão #261f18 (f1030, x360 y1100) (medido, 1 pixel); médias de área (remedição, f1030): fundo #42362b (40x40 em x80 y280), roupa #503a27 (50x50 em x400 y600), chão #251e18 (60x60 em x330 y1080). Vinheta forte embaixo e nos lados. O objeto na mão tem cor natural (aqui bege, #c8965a ± 60): em f1030 o objeto ocupa x186–283 y424–502 (13,5 % × 6,1 % do quadro, centro 32,6 %, 36,2 %) (remedido, f1030, `caixa --cor #e0b888 --tol 50 --regiao 150,380,200,160`; antes "f1040, x128–559 y163–856 incluindo pele").
- Movimento: câmera FIXA o tempo todo (dif 1 a 3 fora do salto do objeto, medido). Só o personagem se mexe: levanta o objeto (f1040–f1053, dif 2), o objeto salta para a câmera (A17, f1054–f1072), gira o objeto na mão (f1080–f1093, dif 3) e para (f1098–f1103 e f1118–f1121 com dif 0: personagem imóvel).
- Saída: corte seco em f1122 (dif 52) para o rosto (a negação curta, A18).
- Ritmo: 4,7 s de plano com 3 elementos entrando por cima (rótulo, objeto, rótulo do objeto).
- Som: nenhum efeito detectado (lateral −120 dB de 42 a 46,8 s).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Cenário (praia com pedras): família foto real em sépia, desfocada. `textura` f1030 região 30,300,170,150: #3c2f24, grão 2,86, manchas 11,8, ac1 +0,83 / ac2 +0,56 (borrão largo), grão B/G/R 2,85/2,86/2,98; f1030 × f1040 anda com a câmera (correlação alinhada +0,78; deslocamento −3,4 px = a câmera mexe muito pouco). Detalhe realçado: pedras e areia reconhecíveis mas sem detalhe fino.
  - Chão escuro da frente (300,980,150,150): #2d241c, grão 0,47 (liso, quase preto pela vinheta).
  - Roupa do personagem: família liso (sem a fibra vista em A09). `textura` f1030 região 380,580,80,90: #4f3926, grão 0,42, manchas 1,6.
  - Objeto na mão: família render realista (concha). `textura` f1030 região 200,425,70,70: #865f3e, grão 15,5, manchas 28,3, grão levemente colorido (B/G/R 14,5/15,4/16,2): é a peça mais detalhada da cena.
  - Rosto: pintura antiga em cor quente (como A09), cabelo com textura de pintura.
- Efeitos (reestudo 20/11): vinheta forte (`borda` f1030: luma 100 · 109 · 84 · 42 · 21 %; mais pesada embaixo, observado); profundidade de campo: fundo grão 2,9 × objeto 15,5; sépia no cenário e na roupa, cor natural só no rosto e no objeto (cor seletiva por objeto, não por máscara de tela). Sem grão de filme global (chão 0,47), sem aberração, sem halo.
- Câmera (reestudo 20/11): parada (medido: f1100→f1118 escala ×1,0015 e 0,06 px/q; f1012→f1048 ×1,017 com só 88 de 244 pontos, confiança baixa, cena escura). Confirma "câmera fixa". Remedido na correção em 3 pares (0,0,720,790): começo f1012→f1024 +1,6 %/s, −0,4 px/q; meio f1030→f1042 +1,5 %/s; fim f1104→f1116 +0,1 %/s, 0 px: parada (≤ +0,07 %/q). Em f1080→f1092 a medida dá +8 %/s porque o personagem se mexe depois que o objeto volta: não é câmera.
- Cadência (reestudo 20/11): 24 imagens/s no personagem (`perfil` f1078–f1094 na região do personagem: dif 4,0 a 4,4 contínua no giro do objeto, sem alternância de ≈ 0).
- Legenda nesta cena (reestudo 20/11): troca NO QUADRO do corte de entrada (f1010: o último bloco de A14 sai e o 1º desta cena, 4 palavras, entra junto do corte) e some no corte de saída (f1122, rosto com texto grande). 5 blocos (2 a 4 palavras). Tarja 66–70 % (mediana 67 %); f1030: luma dentro 21 × fora 61. Atrás da tarja: pernas e chão escuros (luma ≈ 60). Junto: rótulo A16 (topo direito, f1016–f1053) e nome do objeto A17 (f1054–f1095).

## CONSTRUÇÃO
1. cenário: foto real do lugar (aqui praia rochosa) em sépia escura (#3c2f24 médio), desfocada (borrão de ≈ 4–6 px), ocupando a tela toda.
2. vinheta pesada: 100 % no centro, 84 % a 55–75 % do raio, 42 % a 75–90 %, 21 % na borda; mais forte na metade de baixo (o chão vira quase preto, #2d241c).
3. personagem 3D low-poly de corpo inteiro, de frente, centro em x ≈ 59 % (topo do cabelo em 9 %, barra da roupa em 57 % da altura): roupa lisa em sépia/marrom (#4f3926), rosto = retrato pintado em cor quente; luz frontal suave.
4. objeto citado na mão, em cor natural e detalhe alto (13,5 % × 6,1 % do quadro em f1030, à esquerda do corpo, x ≈ 33 %, y ≈ 36 %).
5. animação do personagem: levanta o objeto (f1040–f1053), o objeto salta (A17), gira o objeto na mão (f1080–f1093, ≈ 580 ms), fica imóvel.
6. câmera fixa.
7. rótulo A16 e nome A17 por cima; legenda embaixo.
- Linha do tempo (ms a partir do corte f1010): 0 corte (2 ms antes da 1ª palavra), troca a legenda · 250 rótulo do personagem (A16) · 1251–1793 levanta o objeto · 1835 objeto salta para a câmera (A17) · 2920–3500 gira o objeto · 3670–4671 parado · 4671 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: o lugar (foto do cenário), o personagem (quem lida com o objeto), o objeto citado.
- O que NÃO fazer: não colorir cenário e roupa; não mover a câmera; não deixar o fundo nítido; não aliviar a vinheta de baixo (a legenda e o nome do objeto ficam sobre o escuro).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "personagem do ofício/época" ; "o objeto-fonte citado, na mão dele"; "cenário onde o objeto é encontrado".
- Nesta referência as lacunas foram preenchidas com: tintureiro de Tiro, na praia, segurando um búzio murex.
- Receita de tratamento de cada imagem: igual a A09 (3D low-poly, rosto de retrato pintado, cenário real dessaturado; alinhado ao reestudo), aqui com tinta sépia/marrom em tudo menos no objeto, que fica na cor natural.
- Regra de escolha: literal. "Came from a sea snail" → o personagem mostra o animal, no lugar onde ele é achado.

- Receita de tratamento de cada imagem (reestudo 20/11): foto real do cenário em sépia escura, desfocada, vinheta pesada (21 % na borda).
- Receita de ILUSTRAÇÃO (reestudo 20/11): boneco 3D low-poly com roupa lisa em sépia e rosto de retrato pintado em cor quente; objeto 3D realista em cor natural na mão; luz frontal suave; destaca-se do fundo pela profundidade de campo e pelo detalhe do objeto.
- Teste de generalização: reel sobre Claude Code: "tudo começou com um engenheiro" → boneco de engenheiro numa foto de escritório desfocada em sépia, segurando um chip em cor natural. Reel sobre café: "vinha de uma fruta vermelha" → boneco de pastor numa foto de montanha desfocada em sépia, segurando o fruto vermelho em cor.

- Confiança: tempos, dif e cores medidos; posição do personagem observada.
