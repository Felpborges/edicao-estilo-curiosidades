# 00 · Globais do motor (Estilo 03, edição "reellls")
*Spec escrita em 20/11/2026 a partir de `GUIA-DE-ESTILO.md` (G2–G6, famílias Legenda, Cartão, Câmera, Recorte,
Apresentador, P01/P05/P14/P19/P20) e das notas V01-L01, V03-L01, V04-L01, V05-L01, V04-C00. Vale para todas as
cenas; o `trecho-NN.md` de cada cena manda quando divergir.*

**Convenções.** Quadro 1080x1920. Px do guia (720x1280) × 1,5. Tempo em ms com quadros de 23,976 fps entre
parênteses (1 q = 41,708 ms). (M) medido · (O) observado · (I) inferido · (NM) não medido. Giro: **+ = horário
(topo desce para a direita), − = anti-horário**. Escala "×1,12" = relativa ao tamanho assentado.
Ordem de camadas (de trás para a frente): mesa → peças (com a câmera) → vinheta → legenda.

---

## 1 · Mesa / fundo
- Cores (molde do V03, medido em 8 cenas): centro (luz) **#22211d** (M) · topo **#171612** (M) · base
  **#10110c** (M) · cantos **#0a0905** (M, molde G2; faixa #000000 a #14130f). Faixa do centro vista nos 5:
  #16130e–#3c3932 (M).
- Luz central: mancha radial difusa, sem borda. Forma e tamanho (NM); adotar elipse com centro em (540, 768)
  = (50 %, 40 %) (I, guia G5 "centro a ≈ 40 %"), raio 0,75 × largura na horizontal (810 px) e 0,45 × altura na
  vertical (864 px), queda suave (smoothstep) do centro até a cor de topo/base (I).
- Gradiente vertical por baixo da luz: topo #171612 → base #10110c, linear (I a partir das cores M).
- Vinheta média (molde G2; V01/V02 leve, V04/V05 forte): escurece até #0a0905 nos cantos; começa a ≈ 55 % do
  raio da diagonal (I). Aplicada **por cima das peças também** (I: a borda do cartão do V04 lê #94846f sob a
  vinheta, M), abaixo da legenda.
- Textura/grão: **nenhum** no molde (V04 e V05 lisos, M; V03 "textura sutil", O). Para evitar faixas de
  gradiente, ruído de ±1 nível de 8 bits (I, técnico, invisível).
- Com a câmera em movimento: luz, gradiente e vinheta ficam **presos à tela** (I); o que anda são as peças. O
  vão escuro entre peças aparece quando a câmera viaja (O, V03-A13, V04-A11, V05-A32): por isso a mesa nunca
  pode ter borda: tem que cobrir o quadro todo em qualquer posição de câmera.

## 2 · Cartão (imagem real)
- Forma: retângulo de **cantos retos** (M, 4 vídeos), sem arredondamento.
- Borda de papel: **12 px** (8 px em 720; faixa 10,5–13,5 px; V05 17–27 px creme) (M). Cor **#e8e6e0** (M,
  molde G2/P08; na área iluminada lê #d5d0c8, que é a mesma borda sob a luz/vinheta, M).
- Sombra: **1 px escuro colado à borda**, #000000 a 40 % (V01 M o 1 px; opacidade I). Nada de sombra
  projetada larga (M, 0 casos). Em pilha (cartão sobre cartão): sombra curta deslocada (0, +3 px), desfoque
  4 px, preto 35 % (O "curta e suave" V04-A18/A28; números I).
- Giro: **1,5°, alternando o sentido de um cartão para o seguinte** (M; faixa dos soltos 0,65–1,9°; pilhas até
  ±5°, M).
- Tamanho: largura mediana **87 % = 940 px** (faixa 63,7–98,9 % = 688–1068 px, M em 16 cartões); altura
  mediana 58,9 % = 1131 px (horizontal 37–42 %, vertical 49–75 %, M). Centro **(540, 749) = (50 %, 39 %)**
  (faixa y 31,4–49,5 % = 603–950, M).
- Imagem dentro: **cor original, nada adicionado** (sem gradação, contraste ou grão extra, O nos 5; V01
  levemente dessaturado, O). Textura da própria imagem preservada. Corte da imagem: preenche o cartão (cover).
- Sangria: a base do cartão passa por baixo da legenda (M, V04-A34/A47, V05-A24/A25); com o zoom da câmera o
  cartão pode passar das bordas do quadro (M, V03-A01 83,4 % da altura; V04-A47 topo; V05-A25 laterais). O
  quadro simplesmente corta; nenhum tratamento na borda.

## 3 · Recorte-adesivo
- Um tratamento por vídeo (O, nunca misturado). **Molde: adesivo com contorno** (3 de 5 vídeos):
  contorno off-white **15 px** (10 px em 720, V01 M; V03 9–15 px irregular "de tesoura", O), cor ≈ #e6e2da
  (I a partir da luminância 202–233 medida no V01), uniforme (V01) ou levemente irregular ±3 px (V03, O).
  Sombra fina escura em volta: deslocamento (0, 2 px), desfoque 3 px, preto 45 % (O "fina", números I).
- Alternativa (V04/V05): recorte limpo sem contorno, sombra suave (0, 6 px), desfoque 18 px, 40 % (O, números I).
- Tamanho: solto na mesa **50–85 % da largura = 540–918 px** (M, V04; V05 30–45 %); sobre disco, **altura
  55 % = 1056 px** (M, V01-A01 54,8 %, A11 55,8 %), topo ≈ 68 px acima do disco e base ≈ 156 px abaixo (M).
- Giro: 0° no recorte em pé; leve giro de chegada só no deslize do V04-A02 (O, não medido em graus). Cor da
  fonte sem filtro (O); P&B alto contraste para foto de pessoa só quando a fonte já pede (O).

## 4 · Disco creme
- Cor **#d9d3c7** (M, V03; faixa #c6bdac–#dfd7c9), sem aro. Grão de papel fino (O em V01/V03, amplitude NM;
  adotar ruído monocromático ±4 níveis, I).
- Sombra: escura e curta na borda, opcional (O só no V01): (0, 3 px), desfoque 6 px, preto 35 % (I).
- Diâmetro: **80 % = 864 px** (faixa 70–89 % = 756–961 px, M; V03 44–51 % = 475–551 px; disco menor sobre
  imagem 67 % = 724 px). Centro **(540, 691) = (50 %, 36 %)** (faixa y 34–37 %, M).
- Nasce: **pop ease-out em 3 q (125 ms)**: 49 % → 81 % → 100 % do diâmetro, 1 valor por quadro (M, V03-A07 246 →
  408 → 504 px). O recorte entra no quadro em que o disco assenta: 108 % → 102,5 % → 100 % em degraus de 2 q
  (167 ms, 4 q) (M, V01-A01/A11). Disco cresce, recorte encolhe.
- Sai: encolhendo até 0 em 6 q (250 ms), ease-in (M, V03-A19), ou com o corte.
- Depois de assentado: parallax leve: o disco acompanha a câmera; o recorte anda ≈ 15 % disso e desce 2 % da
  altura em 1,33 s (M, V01-A01: disco +6,8 %, recorte +1 %).

## 5 · Etiqueta de papel (P05)
- Papel **#b5b1a8 com grão fino** (M, V03, 11 de 21 tiras; alternativa clara #ede8dd, V02/V04). Grão NM
  (adotar ±4 níveis, I).
- Tira: altura **84 px** (56 em 720; faixa 78–93 px, M); comprimento = texto **completo** + 33 px de cada lado
  (M à esquerda, I à direita). Nasce no comprimento final; cantos retos (O).
- Texto: **Inter Bold** (fonte provável Helvetica Neue Bold, confiança média; alternativas livres e
  multiplataforma: Arimo Bold (Apache 2.0, Google Fonts) e Liberation Sans Bold; de sistema: Arial Bold).
  **Caixa alta**, cor **#111111**, altura de maiúscula **42 px** (28 em 720, faixa 25–45 px) → Inter Bold em
  corpo **58 px** (I: maiúscula do Inter = 0,727 do corpo). Alinhado à esquerda, centrado na vertical da tira.
- Giro: **−2°** (M). Sombra: nenhuma (variante A) ou (0, 3–4,5 px) curta (variante B, O).
- Posição: centrada no cartão, encavalada na borda de cima (metade da tira fora do cartão) (M); presa ao
  cartão (herda câmera e zoom).
- Entrada: **+43 ms (1 q) depois do início da palavra**; estalo de 167 ms (4 q): q1–q2 a ×1,10 e +2,4° a mais,
  q3–q4 a ×1,03, assentada no q5 (M). A 1ª palavra entra à esquerda com o resto da tira vazio; cada palavra
  seguinte aparece seca (1 q) no início dela, sem a tira mudar (M, V03-A03/A10/A11/A25).
- Saída: fade linear 100 → 0 % em 250 ms (6 q) no início da frase seguinte, ou fica até o corte (M).
  Variante B: deslize da borda lateral em 250 ms (6 q), ease-out, giro −15° → −3° (M).
- Permanência mínima vista 540 ms parada (M); mediana 1330 ms.

## 6 · Marcação à mão e marca-texto
- **Traço à mão (P19):** cor **#e8d840** (M, V03, 3 pastas; faixa amarelo #e0b830–#f0d830; alternativa creme
  #fdefd7 só se a cena já tiver marca-texto amarelo). Opaco, mistura normal, sem preenchimento, sem sombra (M).
  Espessura **4,5 px** (3 em 720; faixa 3–12 px), borda irregular (O: variação ±1 px, I). Forma: elipse/círculo
  à mão em volta do alvo, proporção 1,1:1 (faixa 0,77–1,55; até 4,5:1 em linha de texto), folga visível, largura
  ≈ 25 % = 270 px (faixa 6–58 %), sentido horário a partir do alto, pontas que se cruzam (M).
  Desenho: **292 ms (7 q)**, trim path, **ease-out cúbico** (1º quadro já com um arco curto: ≈ ¼ do traço no 1º
  q do V04-A08, M; curva I = 1 − (1 − t)³). Início: 1º pixel **35 ms antes** da palavra que nomeia o alvo
  (mediana −36 ms, M). Vários alvos: 1 traço por alvo, na sua palavra, ou um a cada 417 ms (10 q) (M). Preso à
  imagem; fica até o corte; sem saída (M).
- **Marca-texto (P20):** cor **#efcb3b** em **multiplicar**, opacidade 100 % (M a cor; modo I a partir do tom
  #d7be5a medido sobre papel creme). Faixa reta da altura da linha marcada (19–25 px em 720 → **29–38 px**;
  até 77 px com documento ampliado, M), borda levemente irregular (O), largura = só o trecho lido.
  Varredura esquerda → direita, **lento-rápido-lento** (molde P20; o V04 é quase constante, o V03 ease-out
  forte: baixa confiança): linha curta **334 ms (8 q)**, linha longa 460–540 ms (11–13 q); várias linhas: cada
  uma começa 1 q depois que a anterior acaba. Início na 1ª palavra do trecho, 0 ms (mediana −2 ms, M).

## 7 · Legenda (P01) — molde completo
Molde = **V04** (259 blocos, a medida mais robusta), salvo onde dito.
- Fonte: **Inter Bold** (OFL, Google Fonts; embutir o .ttf no motor). Fonte provável da referência: Helvetica
  Neue Bold / Arial Bold (confiança média). Alternativas: Arimo Bold, Liberation Sans Bold (livres); Arial Bold
  (Windows/macOS). Inter tem terminais horizontais como a Helvetica (O no still V04-L01).
- Peso: Bold (700). Caixa da fala (maiúscula só no início de frase e nomes), pontuação mantida, **números em
  algarismos** ("três ferramentas" → "3 ferramentas") (M/O). Nomes: "Claude", "Slides", "Docs", "Design".
- Tamanho: altura de maiúscula **37,5 px** (25 px em 720; faixa 33–39 px nos 4 vídeos de curiosidade, M;
  reconferido: V04 still 25–26 px, V01 24 px) → **Inter Bold corpo 52 px** (I). Sem contorno, sem sombra.
- Cor do texto: **#f0eb32** (M, V04, mediana de 259 blocos; faixa #e9e061–#f5eb1d). Ver dúvida D1 (cor).
- Tarja: preto **#000000 a 75 %** (faixa 50–85 %; vem do V01 = 77 % reconferido no still e V03 75–80 %, I; o
  V04 mede ≈ 58–60 %, reconferido: lum. 100–105 → 42–45). Raio **12 px** (8 em 720; reconferido no canto do
  V04: curva de x257,y853 a x265,y844; faixa 0–15 px). Altura **fixa 70 px** (47 em 720, M V03/V04; faixa
  63–71 px). Folga lateral **9 px** (6 em 720, reconferido no V04: 5 à esquerda, 6 à direita; faixa 6–18 px).
  Largura = largura do texto + 2 × 9 px. Desenhada sempre, sobre qualquer fundo.
- Posição: **tarja de y 1266 a 1336**, centro y 1301 = 67,8 % (M; reconferido V04 y844–891 em 720), centro x
  540. Linha de base do texto em **y 1322** (881 em 720, reconferido), topo das maiúsculas em ≈ y 1284.
  (V05 fica 34 px acima em 720; não usar.)
- Agrupamento (regra lida em V03/V04/V05; números M): 1 linha, nunca 2.
  1. Quebra obrigatória depois de pontuação (. , ? ! :) e em toda pausa que ficou no corte (91–128 ms).
  2. Palavras curtas (o, a, os, as, um, uma, de, do, da, em, no, na, e, que, pra, com, por, se, é) grudam na
     seguinte.
  3. Alvo **2 palavras** (V04 média 2,07, mediana 2); 3 quando a 3ª é curta grudada; **máximo 4**.
  4. Limite **21 caracteres** com espaços (= 560 px de texto, maior bloco do V04: 373 px em 720, M → I);
     teto absoluto 28 (V05, 494 px em 720).
  5. Número, nome próprio ou palavra de impacto podem ficar sozinhos; a última palavra da frase pode ficar
     sozinha com o ponto.
  6. Duração mínima **292 ms (7 q)** (mínimo do V04, M); bloco mais curto se junta ao vizinho. Máximo
     visto 1877 ms (45 q). Mediana esperada aqui ≈ 500 ms (Felipe a 3,95 palavras/s; V04 584 ms a 3,2).
  7. Texto literal; não resume.
- Sincronia: o bloco entra no quadro **round(ini_ms / 41,708)** da 1ª palavra (início **reconferido** no
  envelope), deslocamento **0 ms** (V04 mediana +8 ms, V03 0 ms; aceitar −100 a +50 ms, M). Troca **seca**:
  o bloco seguinte substitui no mesmo quadro, 0 q de transição, a tarja muda de largura a seco (M).
- Pausas: **sem vão** (V03: 0 quadros sem legenda em 171 s, M): o bloco fica até a entrada do seguinte. (V04
  some 2–4 q só em pausas longas; as pausas deste corte são de 91–128 ms.) A última legenda do vídeo fica até o
  fim da última palavra + 292 ms ou até o fim do clipe, o que vier antes (I).
- Sobre rosto × cena clara × cena escura: **mesma posição, mesmo desenho** (M nos 5). Sobre escuro a tarja quase
  some (vira sombra); sobre print claro vira retângulo cinza-escuro (#404040 sobre branco a 75 %) e é ela que
  segura a leitura. Nunca muda de lugar para fugir de área clara ou do rosto.
- Câmera: a legenda **não acompanha** corte, pan nem zoom; é desenhada em coordenadas de tela, por cima de
  tudo, a 24 imagens/s mesmo em cena a 12 (M).

## 8 · Movimento — regras gerais
**Taxa de imagem:** tudo a **23,976 imagens/s** (adotado; 4 de 5 vídeos, M). Estalos, pops e assentamentos em
**degraus de 2 q** (cada valor dura 2 quadros, sem interpolar, M). 12 imagens/s de cena inteira = opção
"stop-motion" do V01, não usar sem pedido.

**Entradas**
| nome | onde | valores quadro a quadro | duração |
|---|---|---|---|
| estalo (cartão, documento) | P06/P08/P09/P20 | q1–q2 ×1,12 e giro +3,5° a mais (no sentido do giro do cartão) · q3–q4 ×1,04 e +1° · q5 ×1,00 | 167 ms (4 q) (M) |
| estalo leve (etiqueta) | P05 | ×1,10 +2,4° · ×1,03 · ×1,00 | 167 ms (4 q) (M) |
| estalo de recorte | P14 | ×1,087 · ×1,025 · ×1,00 (2 q cada) | 167 ms (4 q) (M) |
| estalo de peça quase tela cheia | P06/P20 | igual ao estalo + resíduo ×1,003 até o q6 | 250 ms (6 q) (M) |
| pop de disco | P14 | 49 % · 81 % · 100 % (1 q cada), ease-out | 125 ms (3 q) (M) |
| corte seco já assentado | V04/V05 | entra no tamanho final | 0 q (M) |
| deslize / empurrão / cobertura | P10 | translação **+ escala juntas**, lento-rápido-lento, pico no 5º–8º q; a peça empurrada sai na mesma duração; cobertura chega grande e encolhe ×0,81 enquanto assenta | 584–626 ms (14–15 q); cobertura com assentamento 917 ms (22 q) (M) |
| queda de cartão por cima | P09 | estalo 109 → 102 → 100 % | 167 ms (4 q) (M) |

**Saídas:** corte seco (padrão, M) · saída deslizante ease-in com borrão, 167–833 ms (4–20 q), velocidade
24 → 45 → 225 px/q (16 → 30 → 150 em 720, M, V03-A15) · disco encolhe até 0 em 250 ms (6 q) ease-in (M) ·
etiqueta fade 250 ms (6 q) (M). Nunca fade de plano inteiro.

**Curvas (fórmulas I, ajustadas aos pontos M):**
- Lento-rápido-lento (viagem, empurrão, marca-texto, push-in forte): `cubic-bezier(0.45, 0, 0.55, 1)`; pico
  de velocidade perto do meio (V04-A11 a 42 % da duração, M).
- Ease-out forte (quem chega: chicote, cobertura, pan do V02): decaimento geométrico, cada passo ≈ 0,55 do
  anterior (chicote V01: 147 → 84 → 42 → 14 px a cada 2 q, M) ≈ `cubic-bezier(0.16, 1, 0.3, 1)`.
- Ease-in (quem sai): `cubic-bezier(0.55, 0, 1, 0.45)` (I; V03-A15 acelera 16 → 30 → 150 px/q).
- Ease-out cúbico (traço à mão): `1 − (1 − t)³`.
- Linear (deriva/zoom lento de câmera e afastamento até o corte).

**Câmera virtual (translação + escala de toda a mesa; a legenda fica fora):**
- Nunca parada. Depois de assentar: **zoom-in linear +7 %/s** (molde G6; escala(t) = 1 + 0,07·t, ≈ +0,29 %
  por quadro; faixa M −5,4 a +16 %/s). Por tipo: cartão +8 %/s (P06, M) · documento +3 %/s (P20, M) ·
  imagem de tela cheia: pan 5–10 px/q (3,4–6,8 em 720, V03 P07, M).
- Pan de deriva: 3–6 px/q (2–4 em 720, V04, M). Conteúdo anda para a **esquerda** em todo movimento horizontal
  (câmera para a direita, M); na vertical o conteúdo desce (câmera sobe, M).
- Viagem entre peças: **1290 ms (31 q)**, lento-rápido-lento, com recuo junto (no pico ×0,95 a cada 2 q; total
  até ×0,76) (M; faixa 960–1418 ms).
- Chicote lateral: curto 500–583 ms (12–14 q) ease-out forte, a imagem nova chega borrada por 2–4 imagens; longo
  1418 ms (34 q) ease-in-out, pico 63 px/q (42 em 720) (M).
- Afastamento que revela: ×0,60–×0,72 em 30–31 q, constante ou acelera e corta andando (M).
- Acelera: só nas viagens/chicotes e nos push/pan de fim de plano que aceleram até o corte (V05, M).
- **Pode cortar em movimento:** zoom, afastamento e pan seguem até o corte; nada precisa assentar (M).

**Borrão de movimento:** só no **chicote** e na **saída que deixa a mesa** (M, por ocorrência). Quantidade NM;
adotar borrão direcional de comprimento = 0,5 × deslocamento do quadro (obturador 180°, I): chicote longo ≈
32 px no pico; saída rápida ≈ 110 px no pico. Pan, deslize de série, empurrão e zoom: **sem borrão** (O).

**Sincronia geral das peças:** imagem entra junto ou um pouco antes da palavra que ilustra: **−42 ms (1 q
antes) do início da palavra** (mediana −38 ms; p10 −137, p90 +106, M). Lista: 1 peça por item falado.
Etiqueta +43 ms; traço −35 ms; marca-texto 0 ms (M).

## 9 · A-roll (apresentador)
- Nunca: zoom, punch-in, reenquadramento, troca de ângulo, PiP, tela dividida, moldura (0 em 5 vídeos, M).
  Enquadramento do clipe limpo já fixo (rosto 55,6 % da largura, centro y 30,4 %, M no clipe). O rosto entra
  cheio e sai cheio.
- Cor: **sem tratamento** (sem vinheta, grão, gradação ou máscara, O nos 5). O cenário (neon, microfone) é
  conteúdo, não se mexe.
- Corte rosto ↔ cena: **seco, 0 q**, sem flash, preto ou dissolve (M, 126 de 126). Cai **1 q (42 ms) antes da
  1ª palavra da frase**, dentro da pausa (mediana V01 −46, V02 −5, V05 −55 ms; V04 93 % dentro de pausa ≥ 60
  ms, M). Na abertura: o corte do rosto para o objeto cai na palavra do objeto ou logo depois (−62 a +208 ms, M).
- Legenda sobre o rosto: a mesma, mesmo lugar (y 1266–1336). Neste clipe ela cai sobre o corpo do microfone e
  o moletom escuro (O na folha do clipe): legível; não mover.
- Nada além da legenda sobre o rosto (sem ícone, seta, print ou logo, M).

## 10 · Zonas do quadro (1080x1920)
- **Faixa da legenda y 1266–1336 (66–70 %):** reservada; nenhuma informação de cena dentro dela. Imagem pode
  passar por baixo (a tarja garante a leitura) (M).
- **Abaixo de y 1382 (72 %):** nada para ler (zona da interface do Instagram); peças grandes podem passar e
  sangrar a borda (M).
- Imagem principal: centro entre **y 653 e 864 (34–45 %)**, molde y 749 (39 %) (M).
- Rótulos/etiquetas do editor: topo da imagem, **y 192–384 (10–20 %)**, ou na borda do cartão (M).
- Margem lateral: imagem a 22–130 px da borda (2–12 %) ou sangrando; **texto do editor a ≥ 108 px (10 %)** (M).
- Acima da legenda entra no máximo **1 texto do editor por vez** (O nos 5).
- Rosto: nunca coberto (M).

## 11 · Nunca acontece neste estilo
Dissolve, fade, flash, wipe ou quadro preto entre planos (0 em 170 cortes) · zoom/punch-in no rosto · legenda
em 2 linhas, com palavra destacada, karaokê, pop, fade, contorno ou sombra no texto · legenda que se move ou
muda de lugar · ícone, emoji, seta gráfica ou logo decorativo · glow, brilho, degradê colorido · cantos
arredondados no cartão · sombra projetada larga · ilustração genérica ou metáfora solta · imagem com filtro de
cor que não é o da fonte · pan com o conteúdo andando para a direita · câmera parada por mais de ≈ 0,8 s (exceção: 1 cena 3D do V05) ·
música ou efeito sonoro (adotado: só a voz).

## 12 · Dúvidas e não medido
- **D1 · Cor depende do caminho de decodificação (achado nesta passada).** O mesmo amarelo lê **#f1eb30** no
  quadro JPG extraído pelo `prepara.py` (V04 f400) e **#f8e017** no `still.png` (ffmpeg → PNG); V05: #f7eb2a ×
  #fde014. Todo hex do guia veio do caminho JPG. Antes de travar cores, o principal deve renderizar 1 quadro de
  teste (mesa + legenda), codificar como no vídeo final (yuv420p, BT.709 marcado) e extrair pelo **mesmo**
  caminho JPG do `prepara.py`: o hex lido tem que bater com o do guia (±4 por canal). Vale para mesa, borda,
  disco e marcações.
- D2 · Opacidade da tarja: 75 % (V01/V03) adotado; V04 mede 58–60 %. Com muitos prints claros (Slides/Docs),
  75 % lê melhor; confirmar com o Felipe.
- D3 · Luz central da mesa: forma e tamanho NM (adotei elipse 810 × 864 px em y 40 %). Grão do disco e da
  etiqueta NM.
- D4 · Quantidade de borrão NM (adotado 0,5 × deslocamento). Sombra do recorte e da pilha: números I.
- D5 · Tratamento do recorte: adotado "com contorno" (V01/V03); um só por vídeo. Se as specs de trecho
  escolherem refs do V04/V05 (recorte limpo), unificar antes de construir.
- D6 · Cor da marcação à mão: P19 dá #e8d840 (adotado), G2 dá #e0b830; ambos amarelo-ouro (decisão adotada).
- D7 · Curva do marca-texto varia por vídeo (V02 lento-rápido-lento, V03 ease-out, V04 constante). Adotado o
  molde P20 (lento-rápido-lento).
- D8 · Legenda: tamanho 37,5 px em PT-BR no celular não foi validado pelo Felipe (dúvida 8 do contexto). O
  Felipe fala 3,95 palavras/s: blocos de 2 palavras duram ≈ 500 ms (V04: 584). Se ficar frenético, subir o
  alvo para 3 palavras (V03/V05) mantendo o limite de 21 caracteres.
- D9 · Prints de interface com fundo branco (tema do vídeo) serão bem mais claros que as imagens de época da
  referência. A forma manda não alterar a imagem; a vinheta sobre as peças escurece as bordas. Não reconferido
  em nenhum caso real.
- Não reconferido por mim nesta passada: medidas de cartão, disco, etiqueta e movimento (vêm do guia/notas
  remedidas, sem nova amostragem). Reconferido: legenda (posição, altura da tarja, raio, folga, opacidade,
  altura de maiúscula) nos stills de V04-L01, V03-L01, V01-L01 e V05-L01.
