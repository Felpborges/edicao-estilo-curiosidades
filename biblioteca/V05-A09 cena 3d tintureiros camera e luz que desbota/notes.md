# V05-A09 · cena 3D dos tintureiros (câmera que passeia e luz que desbota o pano)
- Categoria: P24 · Cena 3D narrativa (provisória do analista: (provisória) cena 3D de personagens (low-poly) em tela cheia, câmera virtual em movimento, fundo dessaturado e objetos-chave em cor)
- Fonte: V05 quadros f555–f830 (23,15–34,62 s; 276 quadros ≈ 11 512 ms) · 23,976 fps
- Fala: "In the ancient world, making purple was a nightmare. Mixing red and blue plant dyes made a muddy brown. And cheap purples from berries or lichen had a flaw. The sun killed them. If you wore a tunic in the heat, the color would fade away."
- Tipo de fala: contexto (problema histórico + mecanismo: "a luz mata a cor")
- Gatilho: entra por corte seco em f555 (23149 ms), 91 ms antes do início da palavra nº 80 "In" (23240 ms). Conferido: dif 55 em f555 (`perfil`); a legenda "In the ancient world," aparece no mesmo quadro.
- Quadro-chave: f770
- Camadas ativas: b-roll 3D | grafismo (V05-A10 rótulo de lugar, V05-A11 card de foto) | legenda
- Leitura dos strips: strip.jpg = quadros f738 a f760, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 23 células (a luz que desbota o pano). strip-geral.jpg = quadros f553 a f829, de 6 em 6, 8 colunas; 47 células (a cena inteira). detalhe-personagem.jpg = quadro f770, região x440 y180 240x240 px, ampliada 2× sem suavizar (rosto com textura de pintura antiga sobre corpo de blocos, roupa com fibra, fundo desfocado). detalhe-fundo-realce.jpg = quadro f770, região x0 y60 240x240 px, ampliada 2× sem suavizar, contraste ×6 em volta da média (a parede de pedra cinza desfocada). detalhe-travelling-f690.jpg = quadro f690, região x200 y250 240x240 px, ampliada 2× sem suavizar (meio do deslize lateral: o personagem fica nítido, o fundo já era borrado). detalhe-luz-desbota-f746.jpg = quadro f746, região x60 y300 240x240 px, ampliada 2× sem suavizar (a varredura do desbotamento: metade esquerda já clara, metade direita ainda na cor-tema, fronteira vertical nítida).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala abre o "problema" (fazer a cor era um pesadelo); uma cena encenada com gente da época dá corpo ao passado, e cada coisa citada aparece na mão de alguém.
- Por que este design: bonecos 3D simples (corpo de blocos) com rosto de retrato antigo pintado, num cenário real de pedra em preto e branco: lê como "reconstituição de museu", barata de fazer e coerente com o tema histórico.
- Por que estas cores: cenário em cinza neutro (B = G = R), personagens em bege/pele quente e SÓ os objetos citados em cor saturada (o objeto-tema na cor-tema): o olho vai para o que a fala nomeia.
- Por que estes efeitos: profundidade de campo (parede do fundo borrada, peças da frente nítidas) dá escala de maquete; vinheta forte (borda 18 %) fecha o palco; um feixe de luz diagonal claro é o "sol" que desbota o pano.
- Por que este movimento: a câmera fica parada enquanto a frase se desenvolve e anda (travelling, push, recuo) exatamente na palavra que muda o assunto: o movimento pontua a fala como uma vírgula visual.
- Sensação do movimento: documentário encenado, calmo com "solavancos" de atenção; produzida pela alternância parado (dif ≈ 1) → movimento lento-rápido-lento de 14 a 33 q → parado, e pela varredura de 6 q que desbota o pano.

## FORMA (fixa: reproduzir igual)
- Design: cena 3D de tela cheia, personagens humanos estilizados low-poly (corpo de blocos, roupa lisa, rosto com textura de retrato antigo pintado, não foto; alinhado ao reestudo), no cenário do lugar (textura real, com um recipiente central e parede ao fundo) totalmente DESSATURADO em cinza; só os objetos que a fala cita têm cor, cada um na sua cor natural saturada (4 objetos nesta cena, o objeto-tema na cor-tema roxo-magenta). Pele e roupa dos personagens em marrom/bege quente. Vinheta escura nas bordas: base #202020 (f600, x360 y1150, medido); pele clara #dcaa90 (f770, x200 y300, medido, 1 pixel; média de 14x14 px no mesmo ponto #d2a68e, remedição). Iluminação de estúdio de cima, sombras suaves.
- Movimento (dif global por quadro, `perfil` f553–f780, medido): a câmera alterna "parado → movimento lento-rápido-lento → parado", sempre começando na palavra que muda o assunto.
- Passos internos:

| passo | quadros | duração | tipo | curva (dif) | gatilho |
|---|---|---|---|---|---|
| plano parado + rótulo (A10) | f555–f599 | 45 q ≈ 1877 ms | câmera fixa, personagens quase parados | 1 | corte, 1ª palavra da frase (#80) −91 ms |
| reenquadra no personagem 2 | f600–f613 | 14 q ≈ 584 ms | travelling curto | 6 → 14 (patamar f603–f609) → 6 | a palavra que fecha a frase do problema (#88) +0 ms (f600 = 25 025 ms; palavra 25 040 ms) |
| personagem age com os 2 primeiros objetos citados (cada um na sua cor) | f614–f639 | 26 q ≈ 1084 ms | câmera fixa, animação do personagem | 1 a 4 | o verbo da ação (#89) |
| push-in no recipiente central do cenário | f640–f672 | 33 q ≈ 1376 ms | aproximação lenta que acelera e freia | 3 → 8 → 18 (pico f664) → 5 | o nome dos materiais (#94) / o resultado ruim |
| travelling lateral até o personagem 2 | f681–f713 | 33 q ≈ 1376 ms | deslize rápido para a direita | 8 → 32 (pico f690) → 14 → 6 | a versão barata do objeto-tema (#100–101): f681 = 28 404 ms, 1ª palavra 28 260 ms (+144) |
| abre para os 2 personagens | f727–f758 | 32 q ≈ 1335 ms | recuo/pan | 8 → 16 (f732–f736) → 6 | o anúncio do defeito / o agente que causa o defeito |
| luz desbota o objeto-tema | f744–f749 | 6 q ≈ 250 ms (remedido; antes f744–f746, 3 q) | feixe de luz clara cai sobre o personagem 1 e o objeto-tema troca da cor-tema para a versão desbotada dela (rosa-claro) numa VARREDURA da esquerda para a direita: borda esquerda desbota em f744–f745, o meio em f746, a borda direita só em f748–f749 (remedido: saturação por faixa vertical do objeto-tema e strip; antes "troca" sem direção) | cor média do objeto-tema: #7d3f4e (f744) → #a87570 (f745) → #c7a790 (f746), depois estável | o nome do agente (#110, 30 960 ms) +71 ms |
| plano parado | f759–f778 | 20 q ≈ 834 ms | câmera fixa | 1 a 4 | a hipótese com a peça de roupa |
| card de foto (A11) | f779–f794 | 16 q | ver A11 | | o nome da peça |

- Saída: corte seco em f831 para o rosto (dif 59,7).
- Cadência: fps cheio nos movimentos (sem dif ≈ 0 alternado); nos trechos "parados" a dif fica em 1 (personagens se mexem pouco).
- Ritmo: cena longa (11,5 s) mas com algo mudando a cada 1,1 a 1,9 s (média de 1,4 s entre passos).
- Som: nenhum efeito detectado (canal lateral em −120 dB de 23 a 34,6 s).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Parede do fundo (cenário): família foto real de pedra em P&B, desfocada. `textura` f770 região 50,90,120,170: #474843 (cinza neutro), grão 1,49, manchas 5,3, ac1 +0,81 / ac2 +0,57 (borrão largo), grão B/G/R 1,51/1,50/1,49 (cinza). f770 × f778: correlação no lugar e alinhada medida na nota de câmera (anda com a câmera). Detalhe realçado: manchas de pedra macias, sem nenhum detalhe fino: está fora de foco.
  - Recipiente de pedra na frente: família foto real de pedra em P&B, nítida. `textura` f770 região 520,880,150,150: #363636, grão 7,65, manchas 9,9, ac1 +0,71 / ac2 +0,18 / ac4 −0,15, B/G/R 7,65 iguais (cinza puro).
  - Roupa dos personagens: família tecido (textura de pano mapeada em bloco liso). `textura` f770 região 430,420,60,90: #b59176, grão 5,65, manchas 14,3, direção vertical +0,83 × horizontal +0,47 (fios verticais), grão cinza. Detalhe: fibra fina vertical, sem dobra nem sombra de pano (o "pano" é plano).
  - Pano na cor-tema: liso. `textura` f770 região 500,470,80,110: #944459, grão 2,4, manchas 7,8, ac1 +0,42 (quase sem textura).
  - Rosto: família pintura antiga (retrato pintado sobre madeira, com rachaduras e veios), colado como textura plana na cabeça; não é foto de pessoa real moderna (detalhe f770).
  - Pano desbotado sob a luz: #f6d1b3, grão 1,49 (estourado, sem detalhe).
- Efeitos (reestudo 20/11): vinheta forte (`borda` f770: luma 100 · 94 · 66 · 34 · 18 %; borda #191919 neutra). Profundidade de campo: parede do fundo com grão 1,5 × recipiente da frente 7,65 (5× menos detalhe atrás). Feixe de luz: faixa diagonal clara sobre o fundo e o personagem 1 (observado no still). Sombras dos personagens: suaves, sem sombra projetada nítida (observado). Sem grão de filme global (fundo 1,5), sem aberração, sem brilho/halo, sem desfoque de movimento visível no travelling (detalhe f690: o personagem fica nítido).
- Câmera (reestudo 20/11): parada no 1º plano (f560→f595: ×1,021 em 35 q, +0,06 %/q, 0,16 px/q = deriva quase nula). Reenquadramento f604→f606: +3,0 %/q e deslize −17,5 px/q (pico). Push no recipiente f650→f652: +1,26 %/q e subida −4,5 px/q; no pico (f662) o casamento falha (confiança baixa). Travelling lateral f688: não medível (a imagem muda demais entre quadros; o detalhe mostra que não há borrão de movimento forte). Recuo f733→f735: −3,8 %/q e deslize +14,9 px/q. Paralaxe: não medida (casamento falha no travelling); observado no strip-geral: o recipiente da frente corre mais que a parede do fundo (cena 3D com profundidade real). Remedido na correção em 3 pares: começo f560→f572 +1,4 %/s, −0,2 px/q (parada; região 0,250,720,540, 584 de 600 pontos); meio f760→f770 +3,7 %/s (+0,15 %/q), sobe −0,6 px/q (quase parada, antes do card; região 0,0,720,790); fim f800→f812 na região de baixo 0,870,720,330 (fora do card) +0,3 %/s, 0 px: parada. Acima de y795 o card A11 sobe −0,67 px/q e engana a medida.
- Cadência (reestudo 20/11): 24 imagens/s na câmera (dif sem alternância nos movimentos); animação dos personagens f617–f628 com dif 1,75 a 2,54 em todos os quadros (sem passos de 12 imagens/s).
- Legenda nesta cena (reestudo 20/11): volta NO QUADRO do corte de entrada (f555, depois de 75 q sem amarelo) e sai NO QUADRO do corte de saída (f831, para o rosto com texto grande). 16 blocos, 1 a 6 palavras (mediana 2–3). Tarja mediana 67 % (37 a 81); em f580 66 %, f770 65 %, f800 72 %; texto #f0e715. Altura da caixa do texto 35 px com descendentes e 28 px sem: o topo fica fixo em y821 (o centro "muda" 65,2 ↔ 65,5 % só por causa dos descendentes). Atrás da tarja: pernas dos personagens e pedra cinza (luma 62–107). Junto: o rótulo A10 (topo, f564–f613) e o card A11 (f779–f830).

## CONSTRUÇÃO
1. cenário: foto real do lugar (pedra, parede, chão) convertida para cinza neutro (B = G = R), em 2 planos: parede do fundo borrada (desfoque ≈ σ 4–6 px; grão final ≈ 1,5) e peças da frente nítidas (grão ≈ 7–8). Um feixe de luz diagonal claro (faixa de +40 a +60 de luma, borda macia) atravessando o fundo.
2. personagens: bonecos 3D low-poly (cabeça, tronco-bloco, braços e pernas cilíndricos), roupa com textura de pano plana em bege/pele quente (#b59176), rosto = retrato antigo pintado aplicado como textura plana; luz de cima, sombra suave de contato no chão.
3. objetos citados: modelos 3D/fotos recortadas em cor natural saturada (cada um na sua cor); o objeto-tema na cor-tema (#944459). Únicos elementos coloridos.
4. vinheta forte: 100 % até 30 % do raio, 94 % a 55 %, 66 % a 75 %, 34 % a 90 %, 18 % na borda.
5. câmera 3D: parada 0–1877 ms (f555–f599); reenquadramento lento-rápido-lento 1877–2460 ms (pico +3 %/q, −17 px/q); parada 2460–3540; push no recipiente 3540–4920 (ease-in-out); travelling lateral rápido 5300–6680 (pico em ≈ 5670 ms); recuo 7200–8540 (pico −3,8 %/q); parada até o corte.
6. efeito "a luz desbota": em 7445 ms (f744, 71 ms depois do nome do agente) o feixe cai sobre o personagem 1 e a cor do pano varre da esquerda para a direita para a versão clara (#7d3f4e → #a87570 → #c7a790) em 6 q (250 ms), fronteira vertical nítida.
7. legenda: entra e sai nos quadros dos cortes; grafismos A10 e A11 por cima.
- Linha do tempo (ms a partir do corte f555): 0 corte, legenda volta · 375 rótulo A10 · 1877 reenquadra (fim da frase do problema) · 2460 personagem age com os 2 objetos citados · 3540 push (nome dos materiais) · 5300 travelling (a versão barata) · 7200 recuo (anúncio do defeito) · 7445 varredura do desbotamento (nome do agente) · 8590 card A11 (nome da peça) · 11512 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: o lugar (foto do cenário), quantos personagens e o que fazem, quais objetos têm cor, qual palavra dispara cada movimento.
- O que NÃO fazer: não colorir o cenário; não usar rostos de pessoas modernas ou de banco de imagem; não deixar a câmera sempre em movimento (os trechos parados são parte do ritmo); não deixar o fundo nítido; não fazer o desbotamento por fade global (é varredura com fronteira).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "personagens da época/ofício de que se fala"; "cenário do lugar"; "objetos que a fala cita, cada um na sua cor" (os únicos coloridos); "objeto-tema, o único na cor-tema, vestido por um personagem"; "o que acontece com o objeto quando a fala descreve a mudança" (aqui: perder a cor).
- Nesta referência as lacunas foram preenchidas com: tintureiros antigos em uma oficina de pedra; jarro vermelho, frasco azul, cesto de frutas, túnica roxa; a túnica desbota sob o sol.
- Receita de tratamento de cada imagem: render 3D low-poly estilo "boneco" (corpos de formas simples, rostos de retrato antigo pintado; alinhado ao reestudo), cenário com textura real dessaturada para cinza, objetos citados em cor saturada natural, luz de cima com vinheta; câmera virtual que faz movimentos curtos lento-rápido-lento.
- Regra de escolha: ilustração literal da narrativa. Cada frase descritiva vira uma ação dos personagens ou um movimento de câmera até o objeto citado; a cor é reservada ao objeto de que a frase fala.

- Receita de ILUSTRAÇÃO (reestudo 20/11): reconstituição 3D "de museu": bonecos low-poly de blocos com textura de tecido plana e rosto de retrato pintado da época; cenário = foto real do lugar em cinza neutro com profundidade de campo; objetos citados em cor natural saturada; vinheta forte e feixe de luz como elemento dramático. Revela-se por corte seco e por movimentos de câmera nas palavras.
- Teste de generalização: reel sobre Claude Code: "antes, automatizar era um pesadelo" → bonecos de escritório numa foto real de escritório antigo em P&B, só o disquete/planilha citado em cor; a câmera anda nas palavras-chave. Reel sobre café: "secar café era um pesadelo" → bonecos de agricultores numa foto real de terreiro em P&B, só os grãos em cor; a luz do sol queima o grão numa varredura.

- Confiança: tempos e curvas medidos; cores medidas; "low-poly/rosto de retrato pintado" observado (alinhado ao reestudo); correspondência palavra × passo medida pelos tempos da transcrição (±40–100 ms).
