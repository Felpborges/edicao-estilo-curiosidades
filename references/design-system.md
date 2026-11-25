# Design system: G1 estilo em uma página, G2 paleta, G3 tipografia, G4 composição, G5 tratamento de imagem

> Extraído do GUIA-DE-ESTILO do Estilo 03 (treino com 5 reels de referência). Onde o texto cita `still.png`, `strip.jpg` ou `clip.mp4` de uma Ref (ex.: V01-A28), nesta skill só existem `biblioteca/<ID> …/notes.md` (a medida) e `thumb.jpg` (miniatura). Onde cita "o Felipe", é o autor do método: veja `references/decisoes-do-autor.md`.

## G1 · O estilo em uma página

**Reestudo de 2026-11-20.** Depois desta página ter sido escrita, as 204 notas ganharam medida de material, luz, sombra,
câmera por fase e legenda sobre a cena, com nova conferência independente (355 itens) e correção das notas. O que mudou está
na seção 12, que manda sobre as seções 2, 5 e 6. Os quatro pontos que mais pesam: a mesa fica parada na tela e só as peças
andam; a câmera de cada cena tem fases amarradas à fala; luz, grão, sombra, borda e tarja são de cada vídeo (perfis, sem
média); a legenda é translúcida e muda de cara conforme o fundo.

**Como este guia foi conferido.** As 209 pastas da biblioteca (204 de animação e legenda, mais os 5 planos de rosto)
passaram por três filtros depois da 1ª passada dos analistas. (1) Um conferente independente refez 25 animações (5 por
vídeo) contra os quadros: achou 8 com erro de 2 quadros ou mais, 4 gatilhos apontando a palavra seguinte, 5 geometrias
fora da tolerância e nenhuma cor fora. (2) A remedição em massa refez as outras 179 pastas A e L em 8 lotes, quadro a
quadro, por borda, matiz e registro de pontos: **144 tinham correção (80 %)**, só 35 bateram. (3) Uma passada de
vazamento leu as 209 notas e reescreveu pelo papel o conteúdo que tinha ficado na FORMA (160 notas, 784 trechos). O
que isso quer dizer para a confiança: o que os analistas mediram com ferramenta (cor, texto, cortes, legenda) bateu; o
que foi lido a olho errou sempre para o mesmo lado. Tamanhos de recortes, discos, lupas e marcas estavam 10 a 33
pontos abaixo do real, estalos contados com 2 quadros a mais, traços à mão contados do 1º quadro legível (o fim lento ficava de
fora) e câmeras chamadas de fixas. Os números deste guia vêm agora das notas e dos `eventos.json` corrigidos. A margem que sobra é de ±1 quadro
nos tempos, de ±12 px na geometria e de 1 a 3 quadros nos gatilhos de início de frase, porque a transcrição adianta
(seção 11.2).

Documentário de curiosidade de 2,5 a 3 min (158,8 · 171,8 · 160,5 · 165,5 s; o V02 tem 55,8 s) em que um apresentador
fixo pergunta "por que X é assim?" e a resposta é contada como uma colagem de imagens reais sobre uma mesa escura.

1. **Proporção.** 79–86 % do tempo é cena de tela cheia; o rosto fica com 14–21 % (medido nos 5).
2. **Apresentador.** Um único enquadramento frontal fixo, parede verde ao fundo, sem punch-in, zoom ou troca de ângulo
   (5 de 5). Rosto e cena se alternam por corte seco: 170 cortes nos 5 vídeos, nenhum dissolve entre planos (medido).
3. **Quando o rosto volta.** Nas viradas curtas ("It isn't his.", "It's not.", "Not exactly."), nas perguntas, na
   assinatura da série e na conclusão. Todo dado concreto (data, nome, número, lista, lugar, citação) vira imagem.
4. **O mundo.** Fundo quase preto quente (#100e0c nas bordas, #221f1d na luz central). Sobre ele, imagens reais em
   cartão de borda clara (7–9 px, giro de ±1° a ±5°), recortes grandes (50–85 % da largura, muitas vezes sangrando a
   borda) sobre discos creme e documentos com marca-texto amarelo. A câmera quase nunca para: deriva ou zoom lento
   (V01 −5 a +7 %/s; V04 ±2 a ±12 %/s ou pan de 2–4 px/q; V03 push-ins contínuos; V05 2 a 6 %/s), inclusive nos
   trechos que a 1ª passada chamou de "parados" (seção 6).
5. **Ritmo.** 3,2–3,4 palavras/s, pausas medianas de 80–110 ms e máxima de 190–320 ms (`SOM.md`), uma imagem nova a
   cada ≈ 1,1 s (intervalo mediano entre eventos: 1,08 · 0,77 · 1,08 · 1,13 · 0,75 s), 2,1–2,6 cortes secos por 10 s.
6. **Sincronia.** A imagem entra junto ou um pouco antes da palavra que ilustra: mediana −38 ms nas 192 entradas de
   pasta dos 5 vídeos, p10 −137 ms, p90 +106 ms (por vídeo: −48 · 0 · −62 · −29 · −25 ms; recalculado em 2026-11-20).
7. **Legenda.** Uma só, amarela (a cor muda um pouco por vídeo), sans bold de ≈ 25 px, numa tarja preta translúcida (50 a
   74 % conforme o vídeo, seção 12.2) fixa a ≈ 68 % da altura.
   De 1 a 3 palavras por bloco (até 6 no V05), troca seca, sem palavra destacada (958 blocos medidos nos 5, com o V05
   recontado).
8. **Som.** Só a voz. Nenhum vídeo tem música; efeitos raros e baixos só foram detectados em 2 vídeos (V02, V05), e
   ninguém ouviu o áudio.
9. **Abertura e fecho.** Os 4 reels de curiosidade abrem com "Look at this/these X" no rosto por 0,7–1,3 s e cortam
   para o objeto. Fazem a pergunta-tema entre 11 e 17 s e assinam a série ("This is Chasing Beauty episode N, and
   today we're looking at X") entre 14,7 e 20 s. Terminam sem CTA e sem cartela.

**Os dois desvios da amostra:**
- **V02 é um anúncio de vagas do criador, não uma curiosidade** (1ª pessoa, CTA "link na bio", 55,8 s). O sistema
  visual é o mesmo, mas costurado por movimento de câmera num tampo contínuo: 13 cortes; um plano de 16,4 s com 4 pans e
  1 zoom (medido). **Peso:** cheio para design, movimento, legenda e A-roll; baixo para roteiro, abertura/fecho e
  proporção rosto × cena.
- **V05 é o único com cenas 3D e com texto grande sobre o rosto.** As cenas 3D são low-poly, sépia com o objeto-tema
  em cor: 23 pastas P23/P24, 95,5 s = 57,7 % do vídeo, pela união dos intervalos. O texto grande branco
  aparece palavra a palavra 7 vezes, 14,1 s = 8,5 % (as duas contas recalculadas em 2026-11-20 sobre o `eventos.json`
  corrigido: não mudaram, porque nenhum `f_in` ou `f_out` dessas pastas mudou). **Peso:** cheio para ritmo, legenda, roteiro, abertura e fecho.
  O 3D e o texto grande entram só como opção, até o Felipe decidir (seção 11).
- **Núcleo do estilo:** V01, V03 e V04 (curiosidades sem 3D) pesam cheio em tudo. O V01 tem uma peculiaridade própria,
  as cenas a 12 imagens/s e os diagramas chapados (8 ocorrências, todas no V01): conta como "regra dentro de 1 vídeo".

---

## G2 · Paleta

Cores amostradas pelos analistas (quadro citado quando a análise o diz). Molde = UM valor por papel; quando há faixa, o
molde é a mediana por canal dos valores medidos (recalculado) ou o valor do vídeo que fica no meio da faixa.

| papel | V01 | V02 | V03 | V04 | V05 | faixa vista | **molde** |
|---|---|---|---|---|---|---|---|
| fundo, luz central | #221e1f (meio) | tampo #24231e (#1e1d19–#24231e) | #22211d–#3c3932 (varia por cena) | #16130e (centro-baixo, f165/f2330) | #221f1a (A33/A48/A52), #2a2926 (A24) | #16130e–#3c3932 | **#221f1d** (mediana por canal) |
| fundo, base/rodapé | #100e0f (rodapé), #151112 (topo) | (tampo liso) | #10110c (base), #171612 (topo) | #0e0c08 / #13100b | #1e1b16 | #0e0c08–#151112 | **#100e0c** |
| luz e vinheta | poça fixa, sem vinheta por cima | sem vinheta por cima | luz central elíptica, sem vinheta por cima | poça de luz **por cena**, por cima das peças | vinheta só nas cenas | muda por vídeo e, no V04, por cena | **a do perfil escolhido (seção 12.2)**; não existe valor médio |
| fundo chapado de faixa | — | — | — | #181713 (f250, f470) | — | — | #181713 (só V04) |
| borda do cartão | off-white 7–8 px | (objetos, sem cartão) | #e8e6e0 grossa / #aca8a4–#c8c4bf fina, 7–8 px (remedido) | ≈ 9 px, #94846f sob a vinheta (f155) | moldura creme 11–18 px (#d8ccbc A24, #bfa98e A20; remedido) | 7–9 px; V05 11–18 px | **#e8e6e0**, 8 px |
| disco creme | #c6bdac–#dbd3c0 | interior #dfd7c9, aro #e9e2d7–#ede5d8 | #d9d3c7 (sombra #bcb5a7–#c6c2b7) | aro creme (hex não medido) | — | #c6bdac–#dfd7c9 | **#d9d3c7** |
| aro de lupa/medalhão | claro fino + preto grosso | #e9e2d7–#ede5d8 | — | creme (não medido) | — | — | **#ebe3d7** |
| legenda (texto) | #e9e061 | #f5eb1d | #f0ec4d | #f0eb32 | #f4eb2b (f10) / #f2ec2f | #e9e061–#f5eb1d | **#f0eb32** (mediana por canal = V04) |
| tarja da legenda (medida direto no reestudo) | preta a 74 %, 46 px | preta a 50 %, 76 px, raio 8–10 px | preta a 73,5 %, 46 px | preta a 59 %, 48 px, raio 7–8 px | preta a 68 %, 51 px, raio 8–9 px | 50–74 % | **a do perfil escolhido (seção 12.2)**; preta pura |
| etiqueta de papel | — | branca #ede8dd | cinza-claro #b5b1a8 (#b2afa5–#b7b3a8) | #ddc5b1 / #fff1da / #f4f2ee | — | — | **#ede8dd**, texto #111111 |
| marcação à mão | amarelo-mostarda translúcido #b9b04d (A15) | #e0b830 (elipse), #d4b82a (traço) | ≈ #e8d840–#f0d830 | **creme** #fdefd7 (contorno), #fff7de (elipse) | **creme-claro** de 3 px (#e8dcd0 em A07, #e3d7c9 em A53, com o quadro em sépia; a 1ª passada dizia "branco"); preto no mapa; elipse roxa #815685 | amarelo (3 vídeos), creme (2) | **#e0b830** (amarelo-ouro) |
| marca-texto | #d0b83a (A42) | #efcb3b / #f0d050 / #f0d84a / #e8cf5a | #d7be5a | #ecc039 (f2700) / #eec236 (f3145) | (não usa) | #d0b83a–#f0d84a | **#ecc039**, translúcido |
| texto branco (título, texto grande, rótulo) | #ffffff | — | #ffffff | creme #f9f6e9 (título serifado) | #f2f1f2 (A08), #f6f6f6 (A10); cinza de apoio #8a8a8a | — | **#ffffff**; apoio #8a8a8a |
| papel de documento | carta #d0c4bb–#ddd6c3, folha #d4c5a6 | #f2eee4 / #f0ede3, antigo #e8e1b7 | página antiga (não medida) | livro #fceac6, creme #bca488 | página antiga (não medida) | — | vem da imagem (conteúdo) |
| cores de diagrama | teal #347f8a (#317d8b–#3a8a96), laranja-calor #e48750 (#cd8f64–#e8c38e), creme #e5dccb, lã #9c9287 | gráfico creme #e2dacd | — | cores explicativas #e8a835 / #50834a / #465983 / #f1decc | — | — | teal **#347f8a**, laranja **#e48750** (só V01) |
| cor-tema saturada | teal + laranja (diagramas) | só o amarelo | só o amarelo | amostras de cor do tema (camuflagem) | roxo #812463 (#a371b8–#532665), único saturado | — | lacuna: a cor do tema |
| A-roll (cenário) | verde-azulado escuro | parede #538176 / #4a746b, mesa #603f1b | parede #304b38 / #3a5745, mesa #5f3b22 | parede #385a42, moletom #43644e | verde-água (observado) | verde em 5 de 5 | não é edição: cenário do criador |

**Regra de uso (inferido das 5 análises):**
- A família do amarelo (legenda, marcação à mão, marca-texto) é a única cor gráfica fixa do estilo. Ela aparece nos
  5 vídeos na legenda e em 4 na marcação ou no marca-texto.
- Fora do amarelo, a saturação vem do **tema** e nunca de enfeite: cores explicativas de diagrama (V01), amostras do
  objeto (V04), a cor-tema em cor seletiva sobre sépia (V05). Na prática, 1 cor saturada por ideia, e as imagens de
  arquivo ficam em P&B, sépia ou cor desbotada.
- "Uma única cor saturada por vídeo" só vale estritamente para o V05 (o roxo). O V01 usa duas (teal = água, laranja =
  calor) e o V04 várias, porque o tema é cor. Regra proposta: **uma cor saturada por conceito**, nunca decorativa.
- Nenhum brilho, glow ou degradê colorido (V01, V02, V04 afirmam; V03 e V05 não registram nenhum).

---

## G3 · Tipografia

| papel | fonte provável (confiança) · alternativa livre | peso / caixa | corpo por vídeo (px em 1280 e % da altura) | **molde** |
|---|---|---|---|---|
| **legenda** (5 vídeos) | Helvetica Neue Bold (média, os 5 concordam) · alt. Inter Bold | bold, caixa de frase com pontuação | V01 25 px (2,0 %) · V02 **42 px (3,3 %)** · V03 24 px (1,9 %, recalculado em f130; o analista deu 30 px com descendente) · V04 23–31 px (1,8–2,4 %; ≈ 25 sem descendente, recalculado em f400) · V05 ≈ 25 px (1,95 %; caixa com descendente 33–35 px, recalculado; tarja de 42 px, remedido) | **25 px de ascendente a base (2,0 %)**, Inter Bold |
| **título da série sobre o rosto** (V01, V03) | Open Sans (média) · alt. Noto Sans | V01 regular, V03 seminegrito; caixa de frase | V01 67 px por linha · V03 ≈ 5,2 % por linha (≈ 67 px) | **Open Sans SemiBold, 2 linhas, ≈ 67 px por linha (5,2 %)**, branco |
| título-pergunta do gancho (V04-A01) | Tiempos Headline / Georgia Bold (média) | serifada semibold, creme, caixa escura por linha | 2 linhas a 11,0–18,6 % da altura | ocorrência (1 vídeo) |
| texto grande sobre o rosto (V05, 7×) | SF Pro Display Semibold (média) · alt. Inter SemiBold; última palavra Playfair Display Bold Italic (baixa) · alt. Source Serif Bold Italic | semibold + 1 palavra em serifada itálica | maiúscula 36–38 px (2,8–3,0 %), entrelinha 53 px | regra dentro de 1 vídeo |
| rótulo e número digitados (V05, 8×) | a mesma sans do texto grande | linha de apoio regular cinza + linha bold branca | apoio: maiúscula 10–12 px (0,9 %); nome: maiúscula ≈ 23 px (1,8 %); número 33 px | regra dentro de 1 vídeo |
| etiqueta de papel (V02, V03, V04) | V02 Helvetica Neue Bold (média) · V04 Franklin Gothic / Helvetica Condensed Bold (baixa) | bold preta; V02 caixa mista, V03 e V04 **caixa alta** | V02 28–30 px com descendente (2,2–2,3 %); V03 tira de 52–62 px (4,3–4,8 % da altura, 34–66 % da largura; remedido em A03, A10, A11, A25), letra não medida; V04 tira de data de 40 px (3,1 %) com letras de 21 px (1,6 %, A13), tiras de nome de 61–69 px (A10) (remedido) | **sans bold preta em caixa alta, ≈ 28 px (2,2 %)**, alt. Inter Bold |
| rótulo de diagrama e régua (V01) | sans bold (observado) | caixa alta | 19–26 px (1,5–2,0 %) | regra dentro de 1 vídeo |
| texto de documento | tipografia da própria imagem (datilografada, serifada de época, jornal) | — | — | é conteúdo, não forma |

Observações:
- A legenda usa a mesma família nos 5 vídeos, mas **o tamanho não é igual em todos**. O V02 tem a legenda 1,7× maior,
  com tarja de 76 px (y830–905), contra 42–47 px nos outros (V05: 42 px, remedido em f2110). Recalculei com `caixa` em 2
  quadros por vídeo e conferi numa folha de 1 quadro (V02 f100). O molde segue V01, V03, V04 e V05.
- **V05 recontado (remedição V05-a, `remedicao/V05-legenda-blocos-recontagem.json`):** 178 blocos, não 167; no máximo
  6 palavras por bloco (média 2,80), não 9. Os blocos de 7 a 9 palavras eram trocas que o detector juntou. Duração
  mediana 792 ms (19 q), mínima 334 ms, máxima 1752 ms; troca seca. Entrada × 1ª palavra recalculada sobre a
  recontagem: mediana −58 ms (p10 −168, p90 +70), não −96 ms.
- Não há serifada gráfica no núcleo do estilo. Ela só aparece no título-pergunta do V04 e na palavra final do texto
  grande do V05; as outras serifas que aparecem são das imagens de época (observado nos 5).

---

## G4 · Composição e zonas do quadro

Quadro 720x1280. Todas as posições em % da altura (y) ou da largura (x), medidas pelos analistas salvo indicação.

| zona | V01 | V02 | V03 | V04 | V05 | **molde** |
|---|---|---|---|---|---|---|
| topo do texto da legenda | y858 (67,0 %) | y848 (66,2 %) | y858 (67,0 %) | y855–858 (66,8–67,0 %) | **y821 (64,1 %)** (recalculado; o analista deu centro a 65,2 %) | **y858 (67,0 %)**, centro x 50 % |
| tarja da legenda | y849–893 | y830–905 | y846–892 | y844–891 (3,7 %) | y813–855 (42 px), folga ≈ 6 px lateral e 7–8 px vertical (remedido, f2110) | **y846–892** (≈ 3,6 %), folga lateral 8–10 px |
| rosto (A-roll) | largura 50–57 %, topo 14–18 %, centro y 29–32 % | largura 45–51 % (Haar 50,6 %), centro (48 %, 31–32 %), olhos a 27–29 % | altura 24,8–28,4 % (Haar: largura 43,8 %), centro x 39,6–51,5 %, y 29–33 % | largura 45,8–54 %, centro y 28–32 % | largura 47–52 %, centro (44–52 %, 28–32 %) | **rosto com ≈ 50 % da largura, centro a ≈ 30 % da altura, olhos a ≈ 27–29 %** |
| conteúdo das cenas | y ≈ 7–66 %; discos Ø 63–102 % da largura, centro do disco creme a y 34–37 %; fotos em cartão 65–92 % (remedido) | centro dos objetos y 31–39 %, base acima de 50–55 %; medalhões 45 % cada, sobrepostos 20 % do diâmetro (remedido) | cartões com 70–98 % da largura, vários sangram a borda; discos Ø 44–51 % (até 70 %) (remedido) | conteúdo 5–63 %, centro y 34–48 %; recortes e objetos 50–85 % da largura (até ≥ 86 %), muitos sangram (remedido) | texto grande y 55–63 %; objetos recortados 30–45 % da largura; objetos em cor do 3D sangram até as 4 bordas (remedido) | **centro da imagem principal a 34–45 % da altura**; cartão com 70–98 % da largura; recorte ou objeto com 50–85 %, podendo sangrar |
| textos auxiliares | régua de anos y771–811 (60–63 %); rótulo de diagrama a y 56–58 % (V01-A31, remedido) | etiquetas presas no topo do aro | etiquetas a 10–17 % (topo do cartão) | título a 11 % do topo; etiquetas na borda do cartão (nome a y 55–65 %, A10 remedido) | rótulos a 10–23 % e x ≥ 10,8 %, ou a partir de x 73 %; números a 9–14 % | **rótulos e etiquetas no topo da imagem (10–20 %)** |
| margem lateral | fotos a 1–5 % da borda; discos e silhuetas sangram (disco de 102 % no A29; teal sangra a base no A31) | 5–12 % de cada lado; folha de tela cheia sangra por um lado (A10) | cartões que sangram depois do zoom (A09, A16, A20, A22) | cartões sangram com frequência: topo (A30, A47), as 2 laterais (A31), esquerda (A32), as 4 (A45) | texto a ≥ 10,8 %; cartões sangram depois do push-in (A25) | **imagem a 2–12 % da borda ou sangrando; texto a ≥ 10 %** |

**Zona livre e o que nunca é coberto (medido/observado):**
- **Abaixo de ≈ 70–72 %** não fica informação para ler: zona da interface do Instagram (V04 medido: "y > 72 % quase
  sempre vazio"; V05: "nada abaixo de 67 % além da legenda"; V01: nada importante abaixo da legenda). Mas a remedição
  mostrou que **peças grandes passam por ali** com frequência: discos, silhuetas, tecidos e cartões que sangram a borda
  de baixo (V01-A29 até y995, V01-A31, V04-A21, V04-A48 até y1200, V05-A17). A zona fica livre de texto e de detalhe, não
  de imagem.
- **O rosto nunca é coberto.** A tarja cai no peito (V02: rosto y231–595, tarja y830–905); o título e o texto grande
  ficam a 55–67 % (no peito), nunca no rosto.
- **A faixa da legenda (≈ 66–70 %) nunca leva informação de cena.** O papel em tela cheia pode passar por baixo dela, e a
  tarja garante a leitura (V02, V04 L03). Exceção medida: com o zoom, a elipse do V04-A08 cresce até 35 × 18 % e encosta
  na tarja em f794 (ocorrência).
- Grafismo sobre o rosto: só título da série (V01, V03), título-pergunta (V04) e texto grande (V05). Nada de ícone, seta
  ou print sobre o rosto (5 de 5).

---

## G5 · Tratamento de imagem (a receita global)

É a receita que faz uma imagem nova, de qualquer tema, ficar com a mesma cara. Em ordem, de trás para frente:

1. **A mesa.** Fundo quase preto quente, #100e0c nas bordas e #221f1d no centro. **A mesa fica parada na tela; só as
   peças andam** (reestudo). A luz é própria de cada vídeo e não tem valor médio: poça fixa no V01, luz central elíptica
   no V03, poça que troca de centro e de força a cada cena e escurece também as peças no V04, vinheta só nas cenas no
   V05. Mesa lisa no V04 e no V05. Os números de cada perfil estão na seção 12.2; uma edição segue um perfil inteiro.
2. **A imagem real em cartão** (P06, P08, P09). Foto, pintura, gravura ou documento impresso com borda clara de 7–9 px
   (#e8e6e0; 7–8 px em 11 cartões do V03, ≈ 10 px na pintura larga; no V05 moldura creme de 11–18 px), sombra com a regra de cada vídeo
   (reestudo, seção 12.2: no V01 difusa e caída, 19–20 px embaixo e 11–13 px nos lados; no V03 multiplicativa de 10–25 px;
   no V04 nenhuma), largura de 70 a 98 % do quadro (V01 65–92 %; V03 retratos de pilha
   70–98 %; V04 75–96 %), e muitos sangram a borda depois do zoom. **Giro de ±1° a ±5°** (remedido). Convenção deste
   guia: **negativo = topo sobe para a direita (anti-horário)**; positivo = topo desce para a direita (horário). V01:
   1–2°, com o sentido alternando a cada foto da pilha (A12: −1,4°, +2,0°, −2,2°; A17: +1,2°, −2,1°). V03: +0,8° a
   +2°, quase sempre horário. V04: −5° a +3,2° (−1,2 a −1,9° os mais comuns). V05: inclinação residual de 0,5 a 1°, nos
   dois sentidos. A 1ª passada tinha giros de −10° e sentidos trocados (V01-A08, V04-A34, V04-A44).
   **Etiqueta de papel** (P05, V03): tira presa no topo do cartão, 4,3–4,8 % da altura, que **nasce já no comprimento
   do texto completo**; a 1ª palavra entra **alinhada à esquerda** (margem ≈ 22 px) com o resto da tira vazio, e as
   palavras seguintes preenchem sem a tira mudar (medido em A03, A10, A11, A25). Entra com o estalo leve (seção 6) e sai
   em fade de 6 q.
3. **O recorte-adesivo** (P14, P16). Objeto ou pessoa recortado da foto, **grande**: 50 a 85 % da largura do quadro no
   V04 (até ≥ 86 %, sangrando), 30 a 45 % no V05, silhueta de 47 % × 69 % no V01-A29. A 1ª passada dava 20 a 35 %; o
   real é 7 a 33 pontos maior. Contorno off-white de 10–12 px no V01, 3–4 px no V02, 6–10 px irregular no V03; recorte
   limpo, sem contorno, sem sombra no V04 e com sombra de contato de 4–5 px no V05 (reestudo). Fica sobre um disco de papel creme #d9d3c7 com grão ou solto
   na mesa (V02, V04, V05). **Disco creme:** Ø 63–89 % da largura no V01 (até 102 % nos discos de diagrama), Ø 44–51 %
   no V03 (até 70 % no anúncio do tema, A07), 86 % no V04-A06; no V01 o **centro do disco fica a y 34–37 %** da altura e
   o recorte passa por cima dele ≈ 35–45 px em cima e ≈ 100 px embaixo. Os discos "observados" estavam 10 a 25 % menores
   que o real.
4. **A janela circular** (P15). Disco com aro claro que mostra outra imagem dentro (lupa, ponto de vista) e pelo qual a
   câmera pode mergulhar (V01, V02, V04). Lupas do V01 nascem com ≈ 50 % da largura (48,6 % no A05, 50 % no A30, 53 % no
   A33, que depois cresce até 81 %); medalhões do V02 com 45 % cada, sobrepostos em 20 % do diâmetro; aro do V04-A06 de
   17–18 px (remedido). A 1ª passada dava 38–40 %.
5. **A anotação** (P19, P20). Traço à mão (círculo, elipse, laço) de 3 a 8 px: 6–7 px no V01, faixa de ≈ 7 px no V02,
   contorno de 3–4 px e elipse de 8 px no V04, 3 px no V05. As marcas são grandes: **90 a 235 px** no V01 (13 a 33 % da
   largura: A15 90×95, A20 155×202, A16 182×218, A18 235×228), elipse de 32–35 % × 17–18 % no V04-A08, círculo de
   escala de 157 × 182 px no V05-A29. Marca-texto amarelo translúcido de 19 a 25 px de altura (2 a 4 % do quadro) que
   varre exatamente o trecho lido; a linha longa do V04-A35 tem 265 px (36,8 % da largura).
6. **A legenda** por cima de tudo, na mesma posição.

**Cor × P&B × sépia:** a imagem fica na cor em que existe (cor original, P&B de arquivo, sépia, autocromo). Nenhum
analista viu gradação aplicada nas fotos. A exceção é o V05, que dessatura o mundo para sépia (7–10 q, 292–417 ms) e
deixa só a cor-tema.

**Tipos de imagem e proporção** (tempo das pastas por princípio; há sobreposição entre pastas, recalculado sobre os
`eventos.json`):

| vídeo | o que domina | proporção (tempo das pastas) |
|---|---|---|
| V01 | fotos e vídeos de arquivo impressos (cor ou P&B) + recortes em disco + **diagramas vetoriais chapados com grão** | diagramas P18 24 % (37,4 s = 23,5 % do vídeo); pilhas e cartões P06/P08/P09 28 %; disco + recorte P14 12 %; régua de anos P21 14 %; documentos P20 8 % |
| V02 | objetos recortados, medalhões, papéis, mapa (fotos do próprio canal) | documentos P20 33 %; lupa/medalhão P15 26 %; colagem P16 18 %; dado em papel P21 12 %; mapa P22 8 % |
| V03 | **100 % imagens de época** (pintura, gravura, caricatura, documento, objeto de museu) | pilhas P08 41 %; etiquetas P05 17 %; tela cheia P07 15 %; disco + recorte P14 15 % |
| V04 | **100 % fotos, obras e filmes reais de época** (P&B, sépia, autocromo, colorizadas) + recortes de objetos; nenhuma ilustração gerada, ícone ou 3D | objeto que se transforma P17 18 %; colagem P16 15 %; empurrão P10 9 %; faixa de b-roll P12 9 %; afastamento P13 9 % |
| V05 | **3D low-poly** dessaturado com cor seletiva + fotos reais recortadas ou emolduradas + mapa plano | 3D P23/P24 = 95,5 s, **57,7 % do vídeo**; rótulos P04 11 %; texto grande P03 8 %; colagem P16 8 % |

**Regra de escolha da imagem (inferido, 4 vídeos de curiosidade):** sempre uma imagem **real e fotográfica** do que é
dito. Pode ser o objeto, a pessoa (retrato), o lugar (foto aérea ou mapa), o documento (a fonte citada) ou a época
(arquivo P&B). A única imagem desenhada é o diagrama do mecanismo (V01) ou o 3D (V05). A imagem não é ilustração
genérica nem metáfora visual solta.

**Teste de generalização da receita:**
- **Reel sobre Claude Code:** print real da tela do terminal impresso em cartão de borda clara, girado 1°, sobre a mesa
  escura. O recorte do notebook vai sobre um disco creme; a linha de código citada leva marca-texto amarelo; o retrato
  P&B do criador da ferramenta, recortado, entra na palavra do nome.
- **Reel sobre café:** foto de arquivo P&B de uma fazenda de café em cartão; grão de café recortado como adesivo sobre o
  disco creme; anúncio de época de uma marca de café com marca-texto no slogan; diagrama chapado do grão em corte, com o
  calor em laranja, se a frase descrever um mecanismo.

---
