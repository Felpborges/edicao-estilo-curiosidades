# Família · Apresentador e corte (regras comuns aos princípios dela)

> Extraído do GUIA-DE-ESTILO do Estilo 03 (treino com 5 reels de referência). Onde o texto cita `still.png`, `strip.jpg` ou `clip.mp4` de uma Ref (ex.: V01-A28), nesta skill só existem `biblioteca/<ID> …/notes.md` (a medida) e `thumb.jpg` (miniatura). Onde cita "o Felipe", é o autor do método: veja `references/decisoes-do-autor.md`.

# Família · Apresentador e corte

> **Nota do redator (10-apresentador-corte.md).** *Fontes: as 5 pastas `V0X-C00` (notes.md), as seções (a), (b), (c) e (e) de `analises/V01.md` a `V05.md` e as
> transcrições `transcricoes/V0X.json`. Os deslocamentos de TODOS os 170 cortes foram recalculados nesta
> redação com o mesmo método do V01-C00 e do V02-C00 (tempo do quadro de corte menos o início da palavra mais
> próxima no JSON); nos 47 cortes em que a nota já trazia o número (V01, V02), o recálculo bate ao ms. Isso é
> marcado "medido (recálculo)". Unidades: ms; entre parênteses, quadros de 24 q/s (q24) ou quadros da fonte.*

## O apresentador

A camada A-roll é a mesma nos 5 vídeos: uma câmera, um enquadramento, nenhum movimento de câmera. O
apresentador aparece pouco (14 a 21 % do tempo), em trechos curtos de uma frase, e sempre entra e sai por
corte seco.

### Enquadramento, posição e tamanho do rosto (medido, detector Haar, caixa testa-queixo)

| vídeo | plano | largura do rosto (% da largura) | altura do rosto (% da altura) | centro x | centro y | medições |
|---|---|---|---|---|---|---|
| V01 | frontal, do peito para cima | 49,9–56,9 (mediana ≈ 54) | não medido | 43–57 % | 29–32 % | 16 (1 por plano) |
| V02 | meio primeiro plano (cabeça à cintura, mãos embaixo) | 45,1–51,4 (mediana ≈ 48) | 25,4–28,9 | 43,2–50,0 % (med. ≈ 48) | 28,3–32,6 % (med. ≈ 30,7) | 21 |
| V03 | plano médio frontal | 43,8–47,2 (só 3 quadros, em volta do jump cut: f3865, f3872 e o still da C00) | 24,6–28,4 | 39,6–51,5 % | 29,0–32,8 % | 40 (2 por trecho) + 1 (still) |
| V04 | plano médio-próximo (rosto, ombros, mãos) | 46,9–54,0 (média ≈ 49,8); 1º plano 45,8 | não medido | 39,9–49,2 % | 28,0–32,2 % | 13 (1 por trecho) |
| V05 | "close" frontal (mesma escala dos outros) | 47–52 | não medido | 44–52 % | 28–32 % | 27 |

- **Pontos de referência do corpo (só V02, observado em f0):** topo do cabelo y ≈ 8,6 %, olhos y ≈ 26,6 %,
  queixo y ≈ 44,5 %, ombros ocupando a largura toda, mãos gesticulando em y ≈ 55–86 %. A legenda (centro
  y 68,0–68,2 %, V05 65,5 %; tarja y847–892 no V01 e no V03, y830–905 no V02) cai no peito, abaixo do queixo
  (rosto em y ≈ 190–550 no V01, caixa y231–595 no V02 f100) (reestudo, censo). V04 confirma mãos gesticulando na
  parte de baixo (observado).
- **Olhos: faixa 27–29 %.** Nos stills das pastas C00 os anotadores do quadro viram os olhos a y ≈ 29 %, com
  o rosto mais baixo que no f0 do V02: V02-C00 caixa 50,6 % × 28,4 % com centro y 32,3 %; V03-C00 43,8 % ×
  24,6 % com centro y 31,9 % (medido, Haar; olhos observado). Os dois centros caem dentro das faixas da tabela;
  o olho sobe e desce com o centro do rosto (≈ 3 pontos abaixo dele).
- **Câmera à altura dos olhos, frontal, apresentador centrado** nos 5 (observado). A variação de posição
  vem só do corpo se mexendo: no V02 a transformação do fundo contra f0 deu escala 0,999–1,001 e
  deslocamento < 1,5 px em 17 quadros de todos os trechos (medido, pontos ORB).
- **Os nomes de plano divergem** ("do peito para cima", "meio primeiro plano", "plano médio", "close"), mas
  os números se sobrepõem: rosto com ≈ 48–50 % da largura e centro em y ≈ 30 % em todos. É o mesmo
  enquadramento, descrito com palavras diferentes por cada analista (inferido dos números).

### Fundo, cor e luz

| vídeo | fundo (hex amostrado) | roupa | outros |
|---|---|---|---|
| V01 | parede #1a2325 (V01-A10 f400, x600 y150), verde-azulado escuro desfocado, placa iluminada atrás à esquerda (reestudo) | escura e saturada, gola clara (observado no detalhe da tarja) | luz quente no rosto |
| V02 | parede verde-petróleo #538176 / #53837a, canto #4a746b (f0) | suéter azul-marinho quase preto | borda de mesa de madeira #603f1b em y ≈ 98,6–100 %; sacola desfocada na parede |
| V03 | parede verde listrada #304b38 / #3a5745 (f5) | jaqueta preta, camiseta verde-água #214b49 | sacola escura #090e12 à esquerda; mesa de madeira #5f3b22 na base |
| V04 | parede verde-água #385a42 (f405, f15) | moletom verde-água #43644e (sombra) | sacola preta com texto à esquerda |
| V05 | parede #285846 (V05-A08 f520, x560 y100), verde-água desfocado (reestudo) | cachecol e suéter vermelhos | bolsa escura atrás; luz quente lateral |

- **Constantes (observado nos 5):** parede lisa de uma cor fria (verde, verde-água, petróleo), desfocada por
  profundidade de campo curta; um objeto escuro pendurado atrás, à esquerda; pele quente; luz suave
  frontal-lateral, sem sombra dura; nenhuma vinheta, grão, luz de cena ou gradação acrescentados pela edição
  (medido em V01, V03, V04 e V05; tabela abaixo) (reestudo).
- **O que muda entre vídeos:** a roupa e o tom exato da parede (são gravações em dias diferentes). Isso é
  conteúdo do cenário do apresentador, não forma da edição. Mas a roupa muda a cara da legenda (tabela abaixo).
- **Taxa de imagem:** o rosto roda sempre a 24 imagens/s, cada quadro diferente, mesmo no V01, em que TODAS as
  camadas da cena andam a 12 (medido; conferência V01 f2078–f2090: diferença 2,0–4,8 em todo quadro; V01-A10
  f380–f387 3,0–4,2; V04-A01 f0–f12 3,1–6,0). A legenda também anda na grade de 24 no V01: troca em qualquer
  quadro, não segue a grade de 12 da cena (V01-L02) (reestudo).

### Acabamento do rosto por vídeo (reestudo de 20/11; vale para P25 inteiro)

O A-roll é o único plano do estilo que a edição não trata. As cenas têm luz, vinheta, grão e sombra por vídeo
(globais §12.2); nada disso passa para o rosto. O que muda de vídeo para vídeo sobre o rosto é só a legenda.

| vídeo | luma do centro para a borda (5 anéis) | nitidez na borda | parede: grão e estado | tarja sobre a roupa (luma dentro × fora) | legenda no rosto |
|---|---|---|---|---|---|
| V01 | 100 → 72 → 50 → 45 → 42 % (A10 f400): é a luz da filmagem, não circular (inferido) | 13 % (lente) | 0,32, liso (A10 f400) | 74 %; 15–20 × 73 (f10, coluna 300); gola 5–6 × 26–30 (f2080): caixa escura tingida pela roupa | 100 % dos quadros; troca no quadro do corte em 31 de 34 cortes (18 de 18 cortes rosto ↔ cena do lote b) |
| V02 | não medido (observado: sem vinheta) | não medido | não medido | 50 %; 12 × 24 sobre o suéter escuro (#041b2c → #020e16): a caixa quase some | troca no corte em 7 de 13 cortes; 5 atravessam 1–7 q; f134 some 2 q |
| V03 | 100/88/81/80/78 % (A06 f480): acompanha a roupa escura; nenhuma aplicada | 18 % (lente) | 0,26, parado (+0,96 em f480 × f481); resíduo nos claros 0,47, o piso de quadro sem grão | 73,5 %; camiseta clara, fora 79–142: caixa visível | 100 %; 22 de 22 cortes do lote b no quadro do corte; f654 (rosto → cena) atravessa 5 q |
| V04 | 100/117/100/103/104 % (A01 f20); 100/116–120/96–104/100–111/102–111 (conferência f360, f1400, f3160); cantos com luma 76–103 | sem queda (A01 f20) | 0,26, parado (+0,94, A01 f20) | 57 % sobre o rosto (56/58; fundo 102–118, blusa clara): caixa visível | no corte, 1 q antes ou 1 q depois (f354, f459, f1230, f2014); sumiços de 2–3 q colados no corte (f351–f353, f1374–f1376) |
| V05 | 100/96/96/94/105 % (A08 f520); borda 94–105 % nos rostos do lote a | 19 % (lente) | 2,4 (A08, outra escala da ferramenta; liso) | 68 %; 10 × 26 sobre a roupa vermelha escura: a caixa quase some | desligada nos 7 rostos com texto grande, do quadro do corte de entrada ao de saída; nos outros, troca no corte |

- **Sem grão vivo no rosto:** o grão vivo do V01 e do V03 é uma camada só das cenas. No V03 o A-roll dá resíduo
  0,47 nos claros (f480 × f481) e 0,57 (f2150 × f2151), contra 4,2–11,3 nas imagens; o título branco sobre o rosto,
  0,25 (medido; conferência e correção V03-a/b).
- **Sem luz de cena no rosto:** a poça de luz por cena do V04 fica nas cenas e não toca o rosto nem as faixas de
  filme; a vinheta do V05 existe só nas cenas (medido).
- **A nitidez que cai na borda** (13–19 %) é o fundo desfocado da lente, não efeito (V01, V03, V05).

### O que NÃO acontece no A-roll (contado)

| evento | V01 | V02 | V03 | V04 | V05 | total |
|---|---|---|---|---|---|---|
| zoom, punch-in ou reenquadramento | 0 | 0 | 0 | 0 | 0 | 0 |
| troca de ângulo ou de câmera | 0 | 0 | 0 | 0 | 0 | 0 |
| jump cut visível dentro de um trecho de rosto | 0 | 0 | 1 (f3868) | 0 | 0 | 1 |
| transição que não seja corte seco entre rosto e cena | 0 | 0 | 0 | 0 | 0 | 0 de 126 |
| ícone, seta, print, emoji, logo ou PiP sobre o rosto | 0 | 0 | 0 | 0 | 0 | 0 |

- O único jump cut (V03 f3868, "Almost all were servants. / Why?") mantém o enquadramento: o rosto passa de
  47,2 % × 26,6 % para 44,2 % × 24,8 % por mudança de pose, sem zoom (medido). É ocorrência.
- No V04 o 1º plano (f0–f29) tem o rosto ≈ 8 % menor (45,8 % contra ≈ 49,8 % nos outros 12 trechos) e
  traz o título por cima (medido). É ocorrência; não há punch-in animado.

### Quanto do tempo é rosto e quantos trechos

| vídeo | duração | trechos de rosto | rosto total | rosto puro | rosto + texto por cima | trecho mín. | mediana | máx. | cena entre dois rostos (mediana · máx.) |
|---|---|---|---|---|---|---|---|---|---|
| V01 | 158,75 s | 16 | 32,7 s (20,6 %) | 19,6 % | 1,0 % (título) | 0,71 s | 2,06 s | 3,46 s | 6,88 · 16,04 s |
| V02 | 55,76 s | 6 | 9,30 s (16,7 %) | 16,7 % | 0 % | 0,79 s | 1,69 s | 2,04 s | 9,18 · 16,39 s |
| V03 | 171,76 s | 20 | 33,8 s (19,7 %) | 18,7 % | 1,0 % (título) | 0,50 s | 1,65 s | 3,42 s | 5,63 · 17,48 s |
| V04 | 160,54 s | 13 | 22,6 s (14,1 %) | 13,3 % | 0,8 % (título) | 0,63 s | 1,63 s | 4,38 s | 9,86 · 19,56 s |
| V05 | 165,46 s | 12 | 27,9 s (16,8 %) | 8,3 % | 8,5 % (texto grande) | 0,88 s | 2,31 s | 3,92 s | 11,47 · 19,52 s |
| **5 vídeos** | | **67** | | | | **0,50 s** | **1,84 s** | **4,38 s** | **8,38 · 19,56 s** |

- Durações e porcentagens: medido nas tabelas de planos; mediana e intervalos entre rostos: medido
  (recálculo a partir dos quadros das tabelas). No V03 o trecho com o jump cut conta como 1 (2,13 s).
- **Os mínimos (0,50–0,63 s)** são frases de 2 ou 3 palavras: "It isn't." (V03 f3376–f3387, 500 ms, 12 q do
  V03), "syphilis." (V03, 630 ms, 15 q), "It's not." (V04 R6, 630 ms, 15 q). 10 dos 67 trechos têm menos de
  1 s: as 5 aberturas curtas e 5 negações/remates de 2 a 4 palavras.
- **Os máximos (3,4–4,4 s)** são a assinatura da série ("This is Chasing Beauty episode 97, and today
  we're looking at camouflage.", V04 R2, 4,38 s) e conclusões de uma frase longa (V03 3,42 s, V01 3,46 s).
- **O rosto não fica parado para leitura:** é sempre a pessoa falando; o que se lê sobre ele é a legenda
  (família Legenda e texto). O tempo em tela do trecho é o tempo da frase, nada mais.
- **Frequência:** o rosto volta em média a cada 8,6 a 13,8 s de vídeo (V03 o mais frequente, V05 o menos).
  O maior trecho só de cena chega a 16–19,6 s em todos os vídeos.

### Em que momento do roteiro o rosto volta (67 trechos)

Classificação das frases feita pelos analistas em (b) de cada `V0X.md`, reagrupada aqui em 7 tipos
(inferido no reagrupamento; as frases são medidas).

| tipo da frase dita no rosto | V01 | V02 | V03 | V04 | V05 | total |
|---|---|---|---|---|---|---|
| abertura (dêitico "olha isso" ou prova) | 1 | 1 | 1 | 1 | 1 | 5 |
| virada ou negação curta ("But…", "It isn't.", "Not exactly.") | 7 | 1 | 6 | 7 | 5 | **26** |
| anúncio: assinatura da série ou troca de capítulo | 7 | 1 | 1 | 2 | 1 | 12 |
| afirmação curta de choque, remate, piada ou opinião forte | 0 | 0 | 6 | 3 | 2 | 11 |
| conclusão (parcial ou final) | 1 | 0 | 3 | 0 | 3 | 7 |
| pergunta retórica | 0 | 0 | 3 | 0 | 0 | 3 |
| pessoal: pedido, convite, CTA (só no anúncio de vagas) | 0 | 3 | 0 | 0 | 0 | 3 |

- **Regra (5 vídeos):** o rosto pega a frase CURTA que vira o rumo ou fecha um raciocínio; a cena pega tudo
  o que descreve, data, nomeia, lista, mede ou cita. Virada/negação sozinha é 39 % das voltas (26 de 67).
- **O que nunca vai para o rosto (V04 contou: 0 de 13):** data, nome de pessoa na 1ª menção, lista,
  exemplo, descrição. Número só aparece no rosto quando é o próprio choque da frase ("He was 23,", V03;
  "Nearly 4,000 years ago… the one exception", V05). Ocorrência, 2 casos.
- **Pergunta no rosto é regra dentro de 1 vídeo** (V03: 3 perguntas). Nos outros, a pergunta-tese fica em
  cena (V01 A08/A09, V04 A04 e A35, V05 A07).

### O que fica sobre o rosto

| vídeo | só legenda | título ou texto por cima |
|---|---|---|
| V01 | 15 de 16 trechos | 1: título da série (V01-A10, f376–f412, 1,54 s) |
| V02 | 6 de 6 | nenhum |
| V03 | 19 de 20 | 1: título da série (V03-A06, f464–f503, 1,67 s) |
| V04 | 12 de 13 | 1: título-pergunta do gancho (V04-A01) já no quadro 0 do 1º trecho |
| V05 | 5 de 12 | 7: texto grande palavra a palavra (V05-A08, A12, A18, A35, A41, A47, A50); a legenda some nesses trechos |

O desenho desses textos está em P01 (legenda), P02 (título sobre o rosto) e P03 (texto grande). Aqui só a
regra: em 3 dos 5 vídeos o rosto recebe texto 1 vez, no gancho ou na assinatura da série; texto grande em
vários rostos é regra dentro de 1 vídeo (V05).

### Primeiro e último plano de cada vídeo

| vídeo | 1º plano | 1º corte cai em | último plano |
|---|---|---|---|
| V01 | rosto 0,71 s, "Look at this suit." | "suit." +208 ms (no meio da palavra) | rosto 2,54 s, a tese ("It works so well because it never tried to.") |
| V02 | rosto 0,79 s, "In under a year, I've" | "I've" +32 ms (meio da frase) | rosto 1,17 s, CTA ("The link to apply is in my bio.") |
| V03 | rosto 0,92 s, "Look at this hair," | "long," −62 ms (logo depois do objeto) | rosto 2,21 s, último remate do recap ("and spread until even the cook had one.") |
| V04 | rosto + título 1,25 s, "Look at these pants," | "green," −19 ms (logo depois do objeto) | cena 10,72 s (V04-A48 a A50), fecho que liga o tema de volta à origem |
| V05 | rosto 1,29 s, "Look at the flags of all 195…" | dentro do número (−247 ms antes de "countries") | cena 7,38 s (V05-A53), a imagem do gancho repetida |

- **Abertura (regra, 5 vídeos):** todo vídeo começa no rosto, por 0,71–1,29 s (17 a 31 q). Em 4 dos 5 a
  1ª frase é um dêitico ("Look at this/these/the…") e o corte para a cena cai na palavra do objeto ou logo
  depois dela. O rosto não espera a frase terminar.
- **Fecho:** 3 de 5 terminam no rosto (1,17–2,54 s) com a tese, o remate ou o CTA; 2 terminam numa cena
  longa (7,4–10,7 s) que fecha o laço com o gancho. Regra em 3 vídeos para "fecha no rosto"; regra em 2
  vídeos para "fecha em cena de callback". Nenhum tem cartela final.
