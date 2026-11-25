# Trecho 04 · Pilha: um cartão por nome, com etiqueta · P08 + P05 · Ref V03-A21, V03-A10
Fala: "Elas se chamam Slides, Docs e Design"   ·   Janela no clipe: 6050 a 8218 ms (plano); a cena real vai de
q145 (6047,7 ms) até ser coberta pelo print do trecho 05 em q212–q219 (8842–9134 ms)   ·   Entra por: corte seco

*Spec escrita em 20/11/2026. Convenções do `00-globais.md` (1080x1920; 1 q = 41,708 ms; giro + = horário; (M)
medido · (O) observado · (I) inferido · (NM) não medido). Onde este arquivo diverge dos globais, vale este.
Tempos das palavras = `palavras-corte.json` (whisper aparado): reconferir no envelope "Elas", "Slides", "Docs"
(aparado 70 ms) e "Design" antes de travar os quadros. A regra é o deslocamento; o quadro é a consequência.*

## 1 · Linha do tempo da cena (relativa às palavras)

| passo | o que acontece | gatilho (palavra, índice, deslocamento em ms) | duração (ms · quadros) | curva |
|---|---|---|---|---|
| 1 | Corte seco do trecho 03 para a mesa escura com o **cartão 1 (SLIDES)** já no lugar, com estalo | **68 ms antes** de "Elas" (21) → **q145** (6047,7). Molde P08: −100 ms (mediana −105; p10 −163, p90 +7) (M). Se a reconferência mover "Elas", manter entre −63 e −105 ms, dentro da pausa | estalo 167 ms (4 q): q145–146 · q147–148 · assentado q149 | degraus secos de 2 q |
| 2 | Câmera começa a andar (zoom + descida, ver §2) e não para mais | q145 | contínua até o fim da cena | zoom linear; descida lento-rápido-lento |
| 3 | **Etiqueta SLIDES** pipoca no topo do cartão 1 | **+51 ms** depois de "Slides" (24) → **q162** (6756,8). Molde +43 ms (V03 +23 a +137) (M) | 167 ms (4 q): q162–163 · q164–165 · assentada q166 | degraus de 2 q |
| 4 | **Cartão 2 (DOCS)** pipoca por cima, deslocado para baixo-direita, giro oposto | **29 ms antes** de "Docs" (25) → **q175** (7299,0). Molde 0 ms (faixa −143 a +63) (M) | 167 ms: q175–176 · q177–178 · assentado q179 | degraus de 2 q |
| 5 | **Etiqueta DOCS** pipoca no topo do cartão 2 | **+54 ms** depois de "Docs" (25) → **q177** (7382,4) = 2 q depois do cartão, no 2º degrau dele | 167 ms: q177–178 · q179–180 · assentada q181 | degraus de 2 q |
| 6 | **Cartão 3 (DESIGN)** pipoca por cima de todos, mais embaixo e no centro, giro oposto ao 2 | **19 ms antes** de "Design" (27) → **q187** (7799,5) | 167 ms: q187–188 · q189–190 · assentado q191 | degraus de 2 q |
| 7 | **Etiqueta DESIGN** pipoca no topo do cartão 3 | **+65 ms** depois de "Design" (27) → **q189** (7882,9) = 2 q depois do cartão | 167 ms: q189–190 · q191–192 · assentada q193 | degraus de 2 q |
| 8 | Pilha completa; só a câmera anda | q193 → q212 | 792 ms (19 q) | — |
| 9 | Saída: **sem corte**. O print do trecho 05 desliza da esquerda e cobre a pilha; a pilha continua com a mesma câmera por baixo até sumir | início **+84 ms** depois de "dentro" (30) → **q212** (8842,2); pilha totalmente coberta em q219 (9134,0), salvo as faixas de mesa em cima e embaixo (ver trecho 05) | 7 q até cobrir; deslize total 9 q (375 ms), assenta em q221 | ver trecho 05 |

Regra de sincronia usada nos itens 4–7: o cartão entra na palavra do item (molde 0 ms) e a etiqueta entra **2 q
depois do cartão**, no 2º degrau do estalo dele, para que dois elementos nunca nasçam no mesmo quadro (P08: "nunca
mais de um cartão entrando no mesmo quadro", M) e a etiqueta caia na faixa medida do V03 (+23 a +137 ms) (I).

## 2 · FORMA (copiar igual) — px de 1080x1920

**Fundo / mesa:** a mesa global (`00-globais.md` §1): luz central #22211d, topo #171612, base #10110c, vinheta
até #0a0905 nos cantos (M as cores; forma I). Reconferido em V03-A21: fundo #0f100b embaixo (nota, M).

**Coordenadas:** "mundo" = posição na tela no quadro q145 (câmera ×1,00, deslocamento 0). A câmera (abaixo)
transforma tudo; as etiquetas são filhas do seu cartão (herdam posição, giro, estalo e câmera).

**Cartões** (borda 12 px #e8e6e0, cantos retos; imagem preenche o miolo; sombra: 1 px escuro colado à borda e,
cartão sobre cartão, sombra curta (0, +3 px), desfoque 4 px, preto 35 %, como nos globais §2 (V03 "sem sombra
visível", O; números I)):

| cartão | externo (L × A) | miolo da imagem | centro no mundo | caixa sem giro | giro assentado | empilhamento |
|---|---|---|---|---|---|---|
| 1 SLIDES | 820 × 472 (75,9 % × 24,6 %) | 796 × 448 (16:9) | (480, 470) | x 70–890 · y 234–706 | **−1,8°** | atrás |
| 2 DOCS | 780 × 500 (72,2 % × 26,0 %) | 756 × 476 (≈ 3:2) | (610, 790) | x 220–1000 · y 540–1040 | **+2,0°** | meio |
| 3 DESIGN | 800 × 460 (74,1 % × 24,0 %) | 776 × 436 (16:9) | (540, 1100) | x 140–940 · y 870–1330 | **−1,5°** | frente |

- Arranjo "cascata" (I, montado a partir de V03-A21 e V03-A11): cada cartão novo cai **≈ 320 px mais baixo** e
  alternando o lado, cobrindo só a parte de baixo do anterior: o cartão 1 fica com 65 % da altura à mostra (mais
  a faixa esquerda x 70–220 inteira); o cartão 2 com 66 % (mais a faixa direita x 940–1000). Assim **as três
  etiquetas ficam legíveis juntas** até a cobertura. Medidas que sustentam: V03-A21 cartões da lista 67,4 % ×
  27,3 % e 56,5 % × 26,3 %, o de baixo encostando na base do de cima (M, reconferido no still: x 114–599 · y
  84–433 e x ≈ 212–619 · y 426–762 em 720 — bateu); P08 maço 70–96 % da largura, deslocado para baixo/lado, o
  último por cima e perto do centro (M); P08 "cobre a metade/os 2/3 de baixo do anterior" (V01-A07/A12/A16, M).
- Giros alternados −/+/− (P08: o 1º e o 3º para o mesmo lado, o 2º para o outro, M; mediana 1,8°, faixa 0,8–5°).
- O cartão 3 passa por baixo da legenda (base no mundo y 1330 = 69,3 %; na tela chega a ≈ y 1407 = 73 % com o
  zoom): permitido (P08: base até 76 % em V03-A08, M). Nada importante no 1/5 de baixo da imagem 3.
- Nada sangra a borda no início; com o zoom, o canto esquerdo do cartão 1 e o direito do cartão 2 encostam ou
  passam poucos px da borda perto de q212 (permitido, P08/G4).

**Estalo de cada cartão** (globais §8; V03-A08 medido ×1,11–1,12 / ×1,03–1,035, registro de pontos): escala
relativa ao centro do próprio cartão, giro a mais **no sentido do giro do cartão**:
- q1–q2: ×1,12 e giro +3,5° a mais → cartão 1 −5,3° · cartão 2 +5,5° · cartão 3 −5,0°
- q3–q4: ×1,04 e +1,0° a mais → −2,8° · +3,0° · −2,5°
- q5 em diante: ×1,00 no giro assentado. Sem quadros intermediários, sem borrão, sem fade.
- Reconferido (perfil `ferr.py`, V03-A21): cartão do 1º item pipoca em f2751 (71,1) com degraus em f2753 (20,9)
  e f2755 (18,2), assentado f2755; cartão do 2º item f2764 (81,0) · f2766 (43,9) · f2768 (29,2). **Bateu**: 3
  imagens, 4 q, degraus de 2 q. Intervalo entre os dois pops: 13 q = 542 ms (aqui: 12 q = 500 ms).

**Etiquetas** (P05 variante A; globais §5; Ref V03-A10):
- Tira de papel **#b5b1a8** com grão fino (M, V03; V03-A10 #b2afa5, M; minha amostra em f955 deu #aaa89c com
  desvio alto por causa da textura), cantos retos, sem sombra, sem contorno. Altura **84 px** (V03-A10 tem 52 px
  = 78 px; molde 56 = 84) (M).
- Texto **caixa-alta, Inter Bold corpo 58 px** (maiúscula 42 px; provável Helvetica Neue Bold), **#111111**,
  alinhado à esquerda com **33 px** de margem; tira = largura do texto + 33 px de cada lado (≈ 280 px "SLIDES",
  ≈ 235 px "DOCS", ≈ 295 px "DESIGN", estimativa I: medir o texto no motor). Uma palavra por tira, já completa
  no 1º quadro.
- Posição (no referencial do cartão): **centro x = centro do cartão + 63 px** (5,8 % do quadro à direita, como
  nas pilhas do V03: V03-A11 tira a 55,9 % com o cartão a 50,1 %, M; V03-A27 54,5 %, M), **centro y na borda de
  cima** (metade da tira fora do cartão, M). No mundo: SLIDES (543, 234) · DOCS (673, 540) · DESIGN (603, 870).
  Nenhuma etiqueta é coberta por outro cartão (a de DOCS e a de DESIGN ficam por cima do cartão anterior).
- Giro absoluto: **SLIDES −2,0° · DOCS +1,2° · DESIGN −2,0°** (−2° M/O no V03; a de DOCS acompanha o cartão de giro
  oposto: em V03-A10 a tira gira 0,8° a mais que o cartão no sentido anti-horário, cartão −1,2° e tira −2°, O → I).
- Estalo (globais §5; V03-A10): q1–q2 ×1,10 e +2,4° a mais (no sentido do giro da tira) · q3–q4 ×1,03 · q5
  assentada. Escala em torno do centro da tira. Reconferido: perfil V03 f921 (60,9) · f923 (28,5) · f925 (13,1),
  assentada f925; folha f911–f926 mostra a tira maior e mais girada em f921–922, menor em f923–924, assentada em
  f925 — **bateu** (4 q). As larguras da nota (374 → 350 → 343 px) dão ×1,09 → ×1,02; os globais arredondam para
  ×1,10 → ×1,03 (diferença de 3 px a 1080; usar os globais).
- Saída: nenhuma animação; ficam até serem cobertas pelo print (P05 saída "fica até o corte", M).

**Câmera** (P08 "nunca parada", M):
- Tela = A + s(t)·(mundo − A) + (0, d(t)), com **A = (540, 780)**, t em s desde q145.
- **Zoom-in linear +5 %/s**: s(t) = 1 + 0,05·t (molde P08 5 %/s, faixa 2–16 %/s, M). Em q212 s = 1,140; em q219
  s = 1,154. Segue a mesma taxa por baixo do print até a pilha sumir (P10: a anterior continua por baixo; V04-A08
  "o zoom de A07 continua por baixo", M).
- **Descida (a câmera viaja até o cartão novo):** d(t) vai de **+240 px em q145 a 0 em q191** (46 q, 1919 ms),
  lento-rápido-lento `cubic-bezier(0.45, 0, 0.55, 1)`; pico ≈ 8 px/q (5,5 em 720), dentro dos 3,4–8,5 px/q dos
  pans/tilts do V03 (M). Efeito: no corte o cartão 1 aparece com centro em y 710 (37 %, molde P08, M) e a pilha
  sobe até ficar centrada quando o cartão 3 assenta. Depois de q191, d = 0. (Regra "a câmera viaja até o cartão
  de que se fala" = V03, 8 de 8 pilhas, M; a combinação com o zoom é I. Em V03-A21 a câmera faz deriva leve
  durante a lista, M: se a descida pesar no render, trocar por d = 0 e mundo deslocado +240 px, ficando só o zoom.)
- Corta em movimento (não há corte: é coberta em movimento).

**Taxa de imagem:** 23,976 imagens/s; estalos de cartão e etiqueta em degraus de 2 q; câmera a cada quadro (M).

**Confiança:** tamanhos e posições dos cartões = I (dentro das faixas M de P08/V03-A21); estalos, cores, borda,
etiqueta (altura, cor, fonte provável, margem, posição relativa) = M; giro das etiquetas = O/I; câmera = taxa M,
combinação I.

## 3 · CONTEÚDO (deste vídeo)

| lacuna (papel) | preenchida com | receita de tratamento |
|---|---|---|
| imagem do item 1 da lista ("Slides") | print real de um deck feito no Claude Slides (capa ou slide de título) | print 16:9 inteiro dentro da borda, cor original, sem filtro, sem moldura de navegador; título grande legível em ≈ 1 s; nada recortado do fundo |
| imagem do item 2 ("Docs") | print real de um documento feito no Claude Docs | recorte horizontal ≈ 3:2 do **topo da página** (título + 1º bloco de texto), cor original; o que identifica "documento" nos 2/3 de cima (o terço de baixo fica coberto pelo cartão 3) |
| imagem do item 3 ("Design") | print real de um design feito no Claude Design (post, banner ou tela) | recorte 16:9, cor original; o ponto forte do design nos 4/5 de cima (o 1/5 de baixo passa sob a legenda); é o último item: a imagem mais forte das três |
| nome do item 1 / 2 / 3 | etiquetas "SLIDES", "DOCS", "DESIGN" | só o nome, caixa-alta, sem "Claude", sem enfeite (P05: o texto é o que é falado) |

Regra de escolha (P08 + P05): literal, um por item, na ordem da fala; o nome próprio vira etiqueta na palavra.

## 4 · IMAGENS NECESSÁRIAS

| # | o que é, exatamente | papel | de onde pode vir | formato e tamanho mínimo | tratamento a aplicar |
|---|---|---|---|---|---|
| 1 | Tela de um deck gerado no Claude Slides (slide de capa/título) | item 1 | print do próprio Felipe (gerar dentro do Claude e capturar); alternativa: imagem do anúncio oficial da Anthropic (baixar só com o "sim" dele) | PNG 16:9, ≥ 1280 × 720 (miolo 796 px × estalo 1,12 × zoom 1,15 ≈ 1030 px); ideal 1920 × 1080 | nenhum além do cartão; sem cor, grão ou nitidez extra |
| 2 | Página de um documento gerado no Claude Docs (topo, com título) | item 2 | print do próprio Felipe; alternativa: anúncio oficial (com "sim") | PNG recortado 3:2, ≥ 1000 × 630; ideal 1500 × 945 | idem; recorte só retangular |
| 3 | Um design gerado no Claude Design | item 3 | print do próprio Felipe; alternativa: anúncio oficial (com "sim") | PNG 16:9, ≥ 1280 × 720; ideal 1920 × 1080 | idem |

## 5 · Piso de leitura e ritmo

| peça | no topo (até o próximo entrar ou a cobertura) | visível no total | piso | situação |
|---|---|---|---|---|
| cartão 1 SLIDES | q145–q175 = **1251 ms** | q145–q213 ≈ 2,8 s (65 % à mostra) | série ≥ 1,2 s | ok |
| cartão 2 DOCS | q175–q187 = **500 ms** | q175–q213 ≈ 1,6 s (66 % à mostra) | série ≥ 1,2 s | **abaixo no topo**; a fala dá 490 ms entre "Docs" e "Design". Solução (preserva a sincronia): o cartão não sai nem é coberto inteiro; fica 66 % visível com a etiqueta até q213 |
| cartão 3 DESIGN (último) | q187–q211 inteiro = **1043 ms** (+ 2 q parcialmente coberto) | até q214 | último item ≥ 700 ms | ok |
| etiqueta SLIDES | parada q166–q212 ≈ **1,9 s** | — | texto ≥ 700 ms após a palavra | ok |
| etiqueta DOCS | parada q181–q213 ≈ **1,38 s**; 1,25 s depois do fim de "Docs" | — | idem | ok |
| etiqueta DESIGN | parada q193–q213 ≈ **876 ms**; inteira até o fim de q213 (8925,6) = **708 ms depois do fim de "Design"** (8218) | — | idem | **no limite**; por isso a etiqueta fica 63 px à direita do centro (a borda do print só a alcança em q214). Se a reconferência adiantar o fim de "Design" ou atrasar "dentro", conferir de novo |
| cena inteira | q145 → coberta em q212–q219 = **2,8–3,1 s** | — | tela cheia ≥ 1,5 s | ok |

Ritmo: cartões a cada 30 q e 12 q (1251 e 500 ms); referência de enumeração: mediana 709 ms, V03-A21 13 q = 542 ms
(M). A diferença vem da fala do Felipe (3,95 palavras/s) e do 1º cartão entrar no corte, antes do 1º nome (P08:
"o 1º entra por corte ≈ 100 ms antes da 1ª palavra da frase; cada seguinte na palavra do item", M).

## 6 · Dúvidas e o que não foi possível medir

- **Nenhuma referência tem três etiquetas visíveis ao mesmo tempo** numa pilha (V03-A11 e A17/A27 têm uma por
  vez; nas outras a tira sai em fade). A cascata que deixa as três à mostra é I: cumpre o pedido ("cada um com
  etiqueta") e o piso. Alternativa mais fiel ao V03: maço com cada cartão cobrindo ≈ 2/3 do anterior e a etiqueta
  anterior saindo em fade de 250 ms (6 q) quando o cartão seguinte entra (P05 saída (a), M) — mas a de DOCS ficaria
  só ≈ 500 ms.
- **O 1º cartão entra no corte, antes de "Slides"** (regra P08); a etiqueta é que entra na palavra. Se o Felipe
  quiser o cartão literalmente na palavra, o que preenche q145–q161 fica sem imagem (não existe tela vazia no
  estilo): manter assim.
- **Cor da etiqueta:** P05 e os globais adotam #b5b1a8 (V03); a tabela G2 do guia dá #ede8dd. Mantido #b5b1a8
  (Ref V03-A10). Sobre prints claros a tira cinza contrasta pouco: conferir no render.
- **Giro da etiqueta DOCS (+1,2°)** = I. Grão do papel da tira = NM (globais: ±4 níveis).
- **Câmera:** taxa M; a descida de 240 px com ease-in-out é I (inspirada na viagem do V03, cuja velocidade em %/s
  nunca foi medida). Âncora do zoom = I. **Conflito com `00-globais.md` §8** ("na vertical o conteúdo desce"):
  aqui o conteúdo SOBE, como no tilt medido de V03-A17 (P08, M). Se o principal preferir seguir os globais, usar
  d = 0 (só o zoom) com o mundo da tabela como está: o cartão 1 fica alto no corte (centro y 24,5 %), o resto não
  muda.
- Medidas dos cartões 2 e 3 de V03-A21 vêm da nota remedida e bateram no still a olho (±10 px em 720); não
  remedi com `caixa`.
- Coordenar com o trecho 03: o corte de entrada é q145 (fim da janela do trecho 03 = 6050 ms). Coordenar com o
  trecho 05: a mesa e a pilha continuam renderizadas por baixo do print (zoom +5 %/s, d = 0) **até ≈ q252**,
  porque o print só sangra as bordas de cima e de baixo aos poucos e as faixas mostram o que está por baixo (lá
  só aparece mesa escura: a pilha não chega a y < 100 nem a y > 1420 na tela). Ver trecho 05.
