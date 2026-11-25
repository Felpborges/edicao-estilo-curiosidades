# G7 · Ritmo, tempo em tela e piso de leitura

> Extraído do GUIA-DE-ESTILO do Estilo 03 (treino com 5 reels de referência). Onde o texto cita `still.png`, `strip.jpg` ou `clip.mp4` de uma Ref (ex.: V01-A28), nesta skill só existem `biblioteca/<ID> …/notes.md` (a medida) e `thumb.jpg` (miniatura). Onde cita "o Felipe", é o autor do método: veja `references/decisoes-do-autor.md`.

## G7 · Ritmo

### G7.1 Tabela por vídeo

| medida | V01 | V02 | V03 | V04 | V05 |
|---|---|---|---|---|---|
| duração | 158,75 s | 55,76 s | 171,76 s | 160,54 s | 165,46 s |
| planos (corte a corte) · mediana | 35 · 3,08 s | 14 · 2,42 s | 45 · 2,38 s | 42 · 2,61 s | 39 · 3,63 s |
| plano mais curto · mais longo | 0,71 s (rosto, abertura) · 13,25 s | 0,79 s (rosto, abertura) · 16,39 s | 0,50 s ("It isn't." e "Why?") · 17,48 s | 0,63 s ("It's not.") · 11,97 s | 0,88 s ("Not at all.") · 12,93 s |
| cortes secos por 10 s | 2,14 (34) | 2,33 (13) | 2,56 (44, com o jump cut) | 2,55 (41) | 2,30 (38) |
| eventos visuais por 10 s | 8,25 (131) | 9,9 (55) | 7,10 (122) | 7,5 (121) | 9,91 (164) |
| critério do analista | corte + elemento novo + passo interno + transição | idem + **início de movimento de câmera** | corte + elemento novo; **sem** câmera e sem passo de etiqueta | troca de unidade + passo interno; sem zoom contínuo | idem V02 + **cada palavra do texto grande** |
| intervalo mediano entre eventos | 1,08 s | 0,77 s | 1,08 s | 1,13 s | 0,75 s |
| maior trecho sem evento novo | 3,46 s (rosto) | 2,42 s (contagem regressiva) | 7,26 s (callback com push-in) | 4,63 s (faixa de b-roll) | 6,0 s (deriva final) |
| palavras/s | 3,38 | 3,34 (3,51 sem pausas) | 3,36 | 3,35 | 3,23 (3,67 só fala) |
| pausas ≥ 60 ms, limiar único −40 dBFS (`SOM.md`): n (≥ 100 ms) · mediana · p90 · máx | 118 (58) · 90 · 190 · 280 ms | 36 (16) · 80 · 200 · 320 | 113 (48) · 90 · 150 · 250 | 112 (69) · 110 · 160 · 190 | 104 (45) · 90 · 140 · 270 |
| rosto puro | 19,6 % (31,2 s) | 16,7 % (9,3 s) | 18,7 % (32,1 s) | 13,3 % (21,3 s) | 8,3 % (13,8 s) |
| rosto com overlay | 1,0 % (título) | 0 % | 1,0 % (título) | 0,8 % (título-pergunta) | **8,5 % (texto grande)** |
| tela cheia | 79,4 % | 83,3 % | 80,4 % | 85,9 % | 83,2 % |
| sincronia das entradas: mediana · p10 a p90 (recalculado em 2026-11-20; 1 entrada por pasta, sem legenda e rosto) | −48 ms · −152 a +96 (46 pastas) | 0 ms · −40 a +46 (12) | −62 ms · −139 a +6 (31) | −29 ms · −157 a +90 (50) | −25 ms · −113 a +133 (53) |
| sincronia dos cortes | mediana −46 ms | −46 a +56 ms | −4 a −170 ms, quase sempre antes | 93 % dentro da pausa | 1–3 q antes da 1ª palavra |
| legenda: blocos · duração mediana | 200 · 792 ms | 92 · 542 ms | 229 · 751 ms | 259 · 584 ms | **178 · 792 ms** (recontado na remedição) |
| legenda: palavras/bloco (média) · entrada × 1ª palavra | 2,7 · +12 ms | 2,0 · +50 ms | 2,5 (recalculado) · 0 ms | 2,07 · +8 ms | **2,80 · −58 ms** (recalculado em 2026-11-20 sobre a recontagem; era 2,95 · −96 ms) |

Leitura: o ritmo da **fala** é praticamente igual nos 5 vídeos (3,2–3,4 palavras/s, pausa mediana de 80–110 ms, máxima
de 190–320 ms com o limiar único do `SOM.md`; a análise do V05 dava 470 ms com outro limiar, −36,5 dB). O
ritmo da **edição** fica numa faixa estreita: 2,1–2,6 cortes e 7–10 eventos por 10 s, um evento novo a cada 0,75–1,13 s.
As diferenças de eventos/10 s vêm mais do critério de contagem do que do vídeo: V02 e V05 contam movimentos de câmera e
o V05 conta palavras do texto grande.

Sincronia (recalculado em 2026-11-20 sobre os `eventos.json` corrigidos): nos 5 juntos, 192 entradas de pasta,
mediana **−38 ms**, p10 −137 ms, p90 +106 ms; 92 entram antes (< −40 ms), 68 junto (±40 ms), 32 depois. Os valores
antigos da tabela misturavam critérios: o V03 dava −13 ms com 126 medidas (entradas + passos internos); pela entrada
de cada pasta dá −62 ms. Como a transcrição adianta 1 a 3 q nos inícios de frase (conferente), a entrada real tende a
ser ainda um pouco mais "antes" do que esses números dizem.

### G7.2 A curva ao longo do vídeo

- **V01:** plana, 7–11 eventos por 10 s do começo ao fim. Só a janela de 60–70 s cai para 4 (linha do tempo com fotos
  longas). Os cortes se concentram nas voltas ao rosto. Abre com 10 cenas e 1 rosto nos primeiros 15,6 s; fecha no
  callback do objeto + rosto final (6 eventos em 150–158 s).
- **V02:** plana na 1ª metade (11 eventos por 10 s até 30 s); cai para 7 e 5 no bloco "como se candidatar"
  (documento para ler).
- **V03:** respira. Picos na tese (10–20 s, 14 eventos: colagem de 7 retratos com círculos) e na citação da fonte
  (70–80 s, 12); vale em 50–60 s (3: push-in longo do callback). **Os cortes aceleram no fim**: 6 cortes em 160–170 s
  (alternância rosto/imagem do recap).
- **V04:** respira em ondas. Picos de 10–12 nos trechos de mecanismo (hook, explosão, violão, manchas e cores); vales de
  3–6 na narrativa com cartões que só dão zoom. **Fecha sem nenhum corte** (150–160,5 s: uma sequência animada).
- **V05:** ondas em janelas de 15 s, de 4,7 a 15,3 eventos por 10 s. **Abre lento** (0–15 s: 4,7, um b-roll contínuo
  com câmera), adensa em 30–45 s (15,3) e fecha lento (150–165 s: 6,0, deriva final de 6 s).
- **Regra (3 de 5):** o estilo não acelera de forma contínua. Respira em ondas: adensa nos trechos de mecanismo ou de
  lista e alonga nos de narrativa ou callback. O fecho tende a uma imagem longa em movimento, sem corte (V04, V05) ou com
  rosto final (V01, V03).

### G7.3 Tempo em tela medido

*Recalculado em 2026-11-20.* "Na tela" = da entrada à saída da pasta, sobre os `eventos.json` corrigidos (só pastas de
camada "cena de corte" e "b-roll", 146 no total). Os `f_out` que o conferente estendeu (V01-A43, V03-A13, V04-A09,
V04-A16) já entram. "Parado" = do último passo ou assentamento de elemento até a saída, sem nova entrada; zoom lento de
câmera é permitido, pan e reenquadramento não. No V04 ele vem agora **medido quadro a quadro nas notas remedidas**
(registros `remedicao/V04-a.md` e `V04-b.md`): o critério antigo "último passo + 6 q" errava por mais de 2 q em 34 das 47 cenas, para
mais e para menos (de −2,3 s a +1,7 s), porque as entradas do V04 duram de 3 a 52 q e várias cenas nunca chegam a parar.
No V01, a tabela do analista com as correções da remedição (A18, A28, A32, A34, A36 e +2 q nas peças cujo estalo
passou de 6 para 4 q). No V03, a tabela do analista (critério: do último elemento até o corte, câmera andando). No V05,
agregado por tipo com os valores remedidos.

| vídeo | cenas na tela: mín · mediana · máx | parado depois de completo: mín · mediana · máx | cenas < 1,5 s na tela | < 1,0 s |
|---|---|---|---|---|
| V01 | 1167 · 3583 · 12917 ms (33) | 0 · 1083 · 2417 ms (54 peças; 10 abaixo de 700 ms: A34 0, A37 300, A46 300, A09 375, A42 400, A27 417, foto 1 da A17 583, A31 600, foto 2 da A07 667, retrato da A18 667) | V01-A35 (1167), V01-A02 (1458) | nenhuma cena; peças de série: foto 1 da V01-A17 (750), foto 2 da V01-A07 (833), retrato da V01-A18 (833) |
| V02 | 1710 · 3504 · 8175 ms (11) | 167 · ≈ 375 · ≈ 2000 ms (mediana das peças listadas ao lado) | nenhuma | nenhuma cena; níveis do mapa V02-A08 (parados 167 · 167 · 500), objetos da lente V02-A05 (334 · 292 · 792, remedido), documentos V02-A07 (375 · 250 · 375, remedido), número do V02-A01 com marca-texto 292 ms (remedido) |
| V03 | 1293 · 3921 · 10427 ms (24) | 540 · 1730 · 7260 ms (30 cenas; 3 abaixo de 700: V03-A03, A04, A16; com o critério do V04, A12 tem 1,79 s quase parado entre dois push-ins e A30 só 0,29 s depois do push-in de 36 q) | V03-A01 (1293) | nenhuma; etiqueta "nome" do V03-A14 inteira só ≈ 460 ms antes do fade (f1522–f1532; 540 ms contando o começo do fade) |
| V04 | 1168 · 2586 · 6089 ms (47) | **0 · 1080 · 2790 ms** (47, medido; antes 0 · 1290 · 3090 inferido). 15 abaixo de 700 ms: 7 que **nunca param** (A06, A18, A20, A23, A24, A26, A45) e A30 130, A29 210, A31 330, A02 460, A25 460, A49 540, A50 630, A04 670 | V04-A31 (1168), V04-A18 (1210); transições V04-A07 (1126), V04-A43 (542) | V04-A43 (542, mergulho) |
| V05 | 1043 · 3629 · 11512 ms (31) | texto grande **292 · 417 · 709 ms** (remedido: A35 459, A41 417, A47 417, A50 626; A08 e A18 292; A12 709); rótulos 1043 · 1147 · 1335 (A10 remedido 1043, A16, A37 1168, A49); números 918 · 1700 · 3500; fotos de tela cheia 1400 · 2000 · 2200; círculos completos do A53 375 ms | V05-A05 (1043); texto grande V05-A18 (834), V05-A47 (1168), V05-A50 (1418) | V05-A18 (834, "Not at all."); peça de colagem: moeda do V05-A52 (23 q = 959 ms) |

Resumo:
- Como unidade, **a cena quase nunca fica abaixo de 1,5 s**: 6 de 146 pastas (4,1 %) e nenhuma abaixo de 1,0 s
  (recalculado em 2026-11-20; eram 7 com o V04-A09, que passou a 1,88 s com o `f_out` corrigido).
- O tempo curto mora **dentro** das cenas. Peças de pilha ficam de 750 a 1100 ms antes de serem cobertas (V01). Níveis
  de lista ficam parados por 167–500 ms (V02). No V04, 7 de 47 cenas nunca param e mais 8 param menos de 700 ms; a
  mediana do parado medido é 1,08 s, não 1,29 s. O texto grande fica parado 292–709 ms, mediana 417 ms (V05).
- Os planos de rosto abaixo de 1,0 s são 10:
  - V01: 0,71 e 0,96 s.
  - V02: 0,79 s.
  - V03: 0,50 · 0,50 · 0,63 s.
  - V04: 0,63 · 0,79 · 0,88 s.
  - V05: 0,88 s.

  São viradas de 2–3 palavras e a abertura: fala, não leitura.

### G7.4 Piso de leitura (proposto, a confirmar com o Felipe)

**Proposto, não confirmado.** O Felipe disse: "nada pode ficar só 1 segundo em tela; não dá tempo de ler, de entender a
imagem, de ler o texto". No Estilo 01 ele delegou os valores. Proponho os mesmos aqui. A lista do que fica abaixo foi
refeita em 2026-11-20 com os valores medidos das notas remedidas.

| piso | valor | quanto da referência fica abaixo (IDs) |
|---|---|---|
| cena de tela cheia na tela | **≥ 1,5 s** | 6 de 146 pastas: V01-A02 (1458), V01-A35 (1167), V03-A01 (1293), V04-A18 (1210), V04-A31 (1168), V05-A05 (1043). Mais 2 transições do V04 (A07 1126, A43 542) e 1 grafismo do V03 (A31, 1418). Déficit total ≈ 1,7 s em 712 s |
| bloco de texto parado depois da última palavra | **≥ 700 ms** | texto grande do V05: 6 de 7 (parado 292–626 ms, mediana 417: A08 292, A18 292, A41 417, A47 417, A35 459, A50 626; só A12 passa, com 709); etiqueta de nome do V03-A14 (≈ 460 ms); marcações finais do V02 (A01 292 ms com marca-texto, A11 ≈ 167–250 ms). Títulos da série (V01-A10 1542 ms e V03-A06 1668 ms na tela): parado depois da última palavra **não medido** |
| imagem de série (pilha, colagem, lista) na tela | **≥ 1,2 s** | V01: 6 peças (A07 foto 1 1083 e foto 2 833; A12 foto 1 1083; A16 item 1 1000; A17 foto 1 750; A18 retrato 833) e a cena V01-A35 (1167); V04-A31 (1168); V05-A52 moeda (959). V03: topo da pilha do V03-A11 por 375 ms numa enumeração (redator do P08); as outras peças de pilha do V03 não medidas uma a uma |
| último item de lista parado antes do corte | **≥ 700 ms** | V02-A07 (3º documento 375 ms, remedido), V02-A08 (3º nível do mapa 500 ms), V04-A29 (última cor 209 ms, 5 q, remedido), V04-A25 (manchas 460 ms, remedido), V05-A53 (3 círculos completos 375 ms). Dentro do piso: V01-A16 (1583), V01-A28 (833, remedido), V02-A05 (792), V03-A21 e A19 (880), V03-A22 (1130, remedido) |
| cena que nunca para (só V04) | sem piso proposto | 7 de 47 cenas do V04 não chegam a ficar completas e paradas (A06, A18, A20, A23, A24, A26, A45): a leitura acontece em movimento. Se o piso valer para "completo e parado", elas quebram a regra; se valer para "na tela", passam (todas ≥ 1,2 s) |
| legenda | fora do piso | é fala transcrita (blocos de 542–792 ms de mediana); não entra |
| rosto | fora do piso (a confirmar) | 10 planos abaixo de 1,0 s (ver 7.3) |

**O que muda no ritmo se o piso for aplicado (inferido):**
- **Cenas (≥ 1,5 s):** quase nada no total, porque só 4,1 % das cenas ficam abaixo. Mas a mudança é local. Esticar uma
  cena curta empurra a entrada da seguinte para **depois** da palavra (até +457 ms no V05-A05), e a referência entra
  em mediana 38 ms **antes**. O conserto que preserva a sincronia é juntar a cena curta com a vizinha num plano
  contínuo, como o V02 e o V04 já fazem por deslize ou empurrão.
- **Imagens de série (≥ 1,2 s):** no V01 as pilhas trocam uma foto a cada 1,0–1,1 s. Com o piso, cai ≈ 1 foto a cada 6,
  ou a pilha dura mais que a frase. Os eventos por 10 s do V01 cairiam de 8,3 para ≈ 7,5 (estimativa).
- **Texto grande (≥ 700 ms parado):** é o que mais pesa. O rosto com texto teria de durar ≈ 280 ms a mais (700 − 417).
  Isso pede alongar a pausa depois da frase de ≈ 140 para ≈ 420 ms, acima da maior pausa medida no V05 (270 ms com o
  limiar único do `SOM.md`; 470 ms com o limiar de −36,5 dB da análise), ou deixar o texto ficar sobre a cena
  seguinte, coisa que a referência nunca faz.
- **Último item de lista (≥ 700 ms):** antecipar a entrada do último item (entrar na sílaba anterior) ou segurar o corte
  até a pausa. Custa ≈ 250–500 ms por lista.
- **Cenas do V04 que nunca param:** se o piso pedir "parado", seria preciso frear o movimento antes do corte, o que
  muda a assinatura do V04 (movimento que corta andando). Proposta: o piso vale para "na tela" nessas cenas.
- **Saldo:** o vídeo fica ≈ 1–3 % mais lento em eventos por 10 s e as pausas pós-virada crescem um pouco. A fala, o
  número de cenas e a proporção rosto × cena não mudam.

---
