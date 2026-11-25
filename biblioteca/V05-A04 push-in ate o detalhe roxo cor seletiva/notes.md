# V05-A04 · push-in até o detalhe roxo (cor seletiva)
- Categoria: P23 · B-roll 3D com cor seletiva (provisória do analista: (provisória) zoom de câmera contínuo até um detalhe em cor seletiva)
- Fonte: V05 quadros f256–f340 (10,68–14,18 s; 85 quadros ≈ 3545 ms) · 23,976 fps
- Fala: "(Only a handful have) even a tiny speck. Hidden in a parrot's feathers,"
- Tipo de fala: exemplo (exceção mínima: "só um pontinho")
- Gatilho: o mergulho rápido começa em f304 (12680 ms), 60 ms antes do início da palavra nº 45 "Hidden" (12740 ms). Conferido no `perfil` (dif salta de 3,1 em f303 para 7,7 em f304 e 13,7 em f306) e na legenda, que troca para "hidden in" em f304.
- Quadro-chave: f335
- Camadas ativas: b-roll em sépia (mesmo mundo de A01–A03) | legenda | (sem grafismo)
- Leitura dos strips: strip.jpg = quadros f296 a f342, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 47 células. strip-geral.jpg = quadros f254 a f342, de 2 em 2, 8 colunas; 45 células. detalhe-cor-seletiva.jpg = quadro f335, região x260 y420 160x160 px, ampliada 2× sem suavizar (trama do tecido, traço do desenho e a fronteira cor × sépia). detalhe-ponto-f300.jpg = quadro f300, região x300 y440 100x100 px, ampliada 3× sem suavizar (o ponto de cor ainda minúsculo, no fim do creep).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala admite a exceção ("só um pontinho"); a câmera sai do objeto que procurou, recua, acha o único ponto colorido e mergulha nele: a exceção vira prova visual.
- Por que este design: tudo em sépia e um só detalhe em cor no centro exato do quadro (x ≈ 49 %); a ampliação de ≈ 25× faz o "minúsculo" virar meia tela, sem trocar de plano.
- Por que estas cores: o roxo-lilás (#a371b8) é a primeira aparição da cor-tema e a única saturada; o resto fica em sépia, então o olho vai sozinho para ela.
- Por que estes efeitos: a trama do tecido aparece no close (o detalhe é bordado/estampado num pano real) e prova que é um objeto físico; a vinheta de tela (borda a 34 %) segura o olho no centro.
- Por que este movimento: recuo → quase parado → mergulho → aproximação constante: dá ao espectador ≈ 1,2 s para achar o ponto antes de a câmera "confirmar" mergulhando na palavra do 1º exemplo.
- Sensação do movimento: "achei!": a pausa dá suspense e o mergulho dá recompensa; produzida pelo creep de +0,39 %/q seguido de mergulho a +7 a +20 %/q que começa 60 ms antes da palavra.

## FORMA (fixa: reproduzir igual)
- Design: tela cheia em sépia (saturação ≈ 0,19) com UM detalhe em cor: lilás #a371b8 (f335, x290 y450, medido, 1 pixel); média de área #a06cb4 (x230–290 × y500–560) e #775086 no topo, escurecido pela vinheta (x280 y120) (remedido, f335). Em f300 o detalhe é um ponto de 13x28 px no centro (x342 y492; 1,8 % × 2,2 % do quadro, centro 48 %, 40 %); em f335 ele ocupa x171–548 y107–809 (52,4 % × 54,8 % do quadro, centro 49,9 %, 35,8 %) (remedido, f335: a caixa antiga com `#a77bd0` perdia o topo do detalhe, mais escuro pela vinheta; medido com `caixa --cor #8a5c9a --tol 45`). Ampliação ≈ 25× entre f300 e f335. O alvo fica sempre centrado em x ≈ 49 %, y ≈ 37–40 %. Textura de tecido/papel visível no close (observado). Vinheta oval mantida.
- Movimento (dif global por quadro, `perfil` f256–f342, medido), 4 fases:
  1. f256–f275 recuo (zoom-out ≈ −0,9 %/q com descida; corrigido no reestudo, f256–f278; antes "aproximação média"): 5,5 → 9,4 (pico f270) → 5,9; 20 quadros ≈ 834 ms, lento-rápido-lento.
  2. f276–f303 quase parado (creep): 1,35 a 3,1; 28 quadros ≈ 1168 ms. É quando a fala diz que o detalhe é minúsculo e o ponto em cor fica visível no centro.
  3. f304–f318 mergulho rápido: 7,7 → 16,4 (f309) → 18,0 (f315) → 12,9; 15 quadros ≈ 626 ms.
  4. f319–f340 continua aproximando em velocidade constante (dif 8,7 a 11,0) até o corte.
- Saída: corte seco em f341 para A05 (dif 42,8). Não freia antes do corte.
- Cadência: fps cheio (nenhum quadro com dif ≈ 0).
- Ritmo: começa 1 quadro depois de a lupa sair (A03, f255); o detalhe fica legível ≈ 1,2 s (fase 2) antes do mergulho.
- Som: nenhum efeito detectado (canal lateral em −120 dB).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Pano do exemplar em close: família tecido (trama de linho/lona). `textura` f335 região 250,480,160,160 (miolo em cor): cor #7f6080, grão 10,7, manchas 8,4 (fundo uniforme), ac1 +0,60 / ac2 +0,13 / ac4 +0,17, direção: vertical +0,83 × horizontal +0,37 (fios verticais dominantes), grão B/G/R 10,9/10,7/10,7 (cinza). Detalhe f335: trama de fios bem visível na cor e na sépia, com a mesma escala dos dois lados da fronteira; traço do desenho marrom-escuro, ≈ 3–4 px, contínuo, por cima da trama. A textura é do objeto (cresce com o zoom).
  - Ponto em cor no plano aberto (f300): no detalhe, mancha lilás de ≈ 13x28 px sem contorno próprio, sobre os cartões em sépia.
- Efeitos (reestudo 20/11): vinheta de tela: `borda` f335 (fundo uniforme) 100 · 101 · 91 · 59 · 34 % (só começa a cair depois de 55 % do raio); nitidez 100 · 106 · 70 · 28 · 11 % (cai mais que a luma na borda: leve desfoque de borda/profundidade no close). Comparando planos, a borda do quadro fica a 9–22 % da luma do centro nos planos abertos da mesa (f36–f300) e a 34–44 % nos closes (f335, f360, f395): há uma vinheta de tela fixa (≈ 35–45 % na borda) somada a uma queda de luz da própria cena nos planos abertos. Cor seletiva: fronteira nítida entre lilás e sépia (segue o desenho, sem degradê). Sem grão de filme, sem brilho, sem aberração (medido em f335).
- Câmera (reestudo 20/11): fase 1 é RECUO, não aproximação: f256→f262 ×0,947, f266→f272 ×0,943, f272→f278 ×0,951 (−0,9 %/q, ≈ −20 %/s), com descida de +2,4 px/q; continua o recuo que começou no fim de A03 (f236). Fase 2 (f290→f300): +0,39 %/q, parada lateral. Fase 3 (f304→f308): ≈ +6,8 %/q (confiança baixa: 89 de 340 pontos); f310→f320: +10 a +20 %/q (confiança baixa, o casamento falha com a ampliação rápida). Fase 4 (f325→f335): ×1,437 em 10 q = +3,7 %/q, centro sobe −10 px/q. Corrigido no reestudo: "f256–f275 aproximação média" → "f256–f278 recuo de ≈ −0,9 %/q (zoom-out) com descida" (medido por `camera`). Remedido na correção em 3 pares (0,0,720,790): começo f258→f266 −19,0 %/s (−0,8 %/q), desce +2,2 px/q; meio f292→f300 +10,8 %/s (+0,43 %/q); fim f328→f336 +82,8 %/s (+2,55 %/q), sobe −6 px/q: mesmas fases da nota.
- Cadência (reestudo 20/11): 24 imagens/s (dif da nota sem nenhum ≈ 0 alternado; zoom muda em todos os quadros).
- Legenda nesta cena (reestudo 20/11): 4 blocos (2 a 3 palavras). O bloco do 1º exemplo da lista (3 palavras, f319–f343) atravessa o corte de saída (f341). Tarja mediana 68 % (f256–f340), f335: luma dentro 30 × fora 95 → 69 %; texto #eee817. Atrás da tarja: tecido em sépia/cor (luma 50–95). Sem outro texto.

## CONSTRUÇÃO
1. fundo: a mesma superfície de A01–A03 em sépia (saturação 0,19), com um único exemplar que tem uma área em cor (a cor-tema, saturada, sem tinta sépia); a imagem tem que ter resolução para ampliar ≈ 25× e mostrar a trama do tecido no close.
2. cor seletiva: máscara exata da área do desenho (segue o contorno do desenho, sem borda suave), saturação original dentro, sépia fora.
3. vinheta de tela fixa: radial, 100 % até 55 % do raio, 91 % a 55–75 %, 59 % a 75–90 %, 34 % na borda; nos planos abertos a própria cena escurece mais a borda (9–22 %).
4. câmera (na camada 1+2): 0–920 ms recuo −0,9 %/q e descida 2,4 px/q (ease-out); 920–2000 ms quase parada (+0,4 %/q), alvo centrado em x 49 %, y 40 %; 2000–2630 ms mergulho com ease-in-out (pico ≈ +15 %/q em ≈ 2300 ms); 2630–3540 ms aproximação constante +3,7 %/q até o corte, centrada em x 50 %, y 36 %.
5. legenda por cima; troca 3 q depois do corte de saída.
- Linha do tempo (ms a partir de f256): 0 começa (o objeto de A03 acabou de sair) · 834 fim do recuo · 834–2000 creep, o ponto em cor visível no centro · 2000 mergulho (60 ms antes da palavra do 1º exemplo) · 2630 fase constante · 3545 corte seco para A05.
- Parâmetros que dependem do conteúdo: onde está o exemplar (o alvo do zoom); o tamanho final do detalhe (aqui 52 % × 55 % do quadro); a palavra do 1º exemplo, que dispara o mergulho.
- O que NÃO fazer: não começar com aproximação (é recuo); não parar a câmera no fim (corta em movimento); não suavizar a máscara de cor; não usar textura lisa no close (o close precisa da trama); não deixar o alvo fora do centro.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "a exceção rara dentro da coleção" (o único exemplar que tem a qualidade procurada); "o detalhe exato onde a qualidade aparece".
- Nesta referência as lacunas foram preenchidas com: a única bandeira com roxo (Dominica) e o papagaio roxo do brasão dela.
- Receita de tratamento de cada imagem: mesma cena da coleção, em sépia; só o detalhe tem cor natural saturada; aproximação a partir do plano geral até o detalhe ocupar metade da tela; textura de material (tecido/papel) visível no close; vinheta forte.
- Regra de escolha: literal. A fala cita o exemplo ("hidden in a parrot's feathers") e a câmera mergulha no objeto citado; a pausa do zoom (fase 2) cai na frase "a tiny speck", para mostrar o tamanho do detalhe antes de ampliá-lo.

- Receita de tratamento de cada imagem (reestudo 20/11): imagem em sépia com saturação 0,19; só o detalhe-alvo em cor cheia, recortado pelo contorno do desenho; material com trama de tecido visível no close (ac1 vertical 0,83); vinheta de tela 34 % na borda.
- Receita de ILUSTRAÇÃO (reestudo 20/11): desenho plano tipo estampa/bordado: preenchimento chapado, contorno marrom-escuro de 3–4 px contínuo, sem sombreado; impresso sobre tecido com trama; destaca-se só pela cor seletiva; revelado pelo zoom.
- Teste de generalização: reel sobre Claude Code: "só um ou outro tem isso: escondido num cantinho do menu" → recuo, pausa e mergulho num botão em cor dentro de uma tela em sépia. Reel sobre café: "só um pontinho de dourado, escondido no rótulo" → recuo e mergulho num detalhe dourado de um rótulo em sépia.

- Confiança: tempos, dif, caixas e cor medidos; ampliação 25× calculada a partir das caixas; "Dominica" é identificação visual (observado).
