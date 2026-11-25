# SOM · Estilo 03 Curiosidades (@fineasjackson, V01 a V05)

*Passo 10 do treino · 2026-11-20 · medido com o mesmo critério nos 5 vídeos. Ninguém ouviu o áudio:
tudo sai do envelope de 10 ms (`audio/V0X-envelope.csv`), de análises numéricas do wav estéreo e de
2 espectrogramas. Scripts em `_ferramentas/som/` (os que leem o wav usam a cópia do scratchpad).*

## 1 · Resumo

1. **Só voz.** Nenhum dos 5 tem música ou cama de fundo. Uma cama constante teria de estar abaixo de
   ≈ −59 dBFS (V05) a −66 dBFS (V04), ou seja, 42 a 50 dB abaixo da voz: inaudível no celular.
2. **A voz é idêntica nos 5:** mono no centro, −14,1 a −14,3 LUFS integrado, faixa de loudness (LRA) de
   2,2 a 4,1 LU (compressão forte), fala com RMS médio de −16,3 a −16,6 dBFS.
3. **Efeitos são exceção, não regra.** 3 vídeos (V01, V03, V04) não têm efeito confirmado. V02 (o anúncio
   de vagas) tem 11 trechos de foley de papel e caneta; V05 tem 4 sons graves longos (3 subidas que
   estouram no corte e 1 ambiência).
4. **Corte seco não leva som** em 167 de 170 cortes (nos 2 vídeos mono, nenhum sinal nas pausas). As 3 exceções são as subidas de V05, sempre em
   virada de capítulo, com o pico 40 a 50 ms antes do corte.
5. **Pop de cartão, etiqueta, legenda, texto grande, chicote, zoom, cena 3D, explosão e fogo: nunca têm
   efeito medido** (0 em 129 eventos de V01 e 0 nesses tipos em V05). Chicotes que caem em pausa
   (V01 f197, f1339, f1532; V03 f3754) ficam em silêncio de −54 a −62 dBFS.
6. **Silêncio quase não existe.** Pausas de 60 a 320 ms, mediana 80 a 110 ms; fim de frase ≈ 140 ms;
   pergunta e virada não ganham pausa maior. Começa a falar em 20 a 80 ms e acaba 120 a 350 ms depois
   da última palavra, com o som caindo até o silêncio digital.
7. **O corte cai no silêncio** (63 % dos 170) e a 1ª palavra do plano novo vem ≈ 47 ms depois. A imagem
   nova entra antes da palavra: mediana −40 ms (192 entradas).
8. **Molde:** voz a −14 LUFS, sem música, sem efeito por padrão. Se quiser efeito, só foley baixo nas
   anotações à mão (estilo V02) ou 1 a 3 subidas graves que estouram no corte de uma virada (estilo V05).

## 2 · Tabela por vídeo

| | V01 | V02 | V03 | V04 | V05 |
|---|---|---|---|---|---|
| duração | 158,8 s | 55,8 s | 171,8 s | 160,6 s | 165,5 s |
| canais | estéreo, quase mono (lateral > −60 dB em 0,28 % das janelas, só em sibilantes) | voz mono + efeitos estéreo (lateral > −60 dB em 6,8 %) | mono (L = R em 100 %) | mono (L = R em 100 %) | voz mono + efeitos estéreo (4,1 %) |
| loudness integrado | −14,1 LUFS | −14,2 | −14,1 | −14,3 | −14,3 |
| LRA | 2,3 LU | 2,3 | 2,2 | 3,2 | 4,1 |
| pico real | −1,6 dBTP | −0,1 | −1,4 | +0,5 (estoura) | −0,5 |
| voz: RMS médio / mediana / p95 (dBFS, meio, 10 ms) | −16,3 / −18,5 / −11,1 | −16,5 / −19,7 / −11,0 | −16,3 / −18,2 / −11,4 | −16,6 / −20,2 / −10,7 | −16,5 / −20,1 / −10,6 |
| piso das pausas: mínimo de cada pausa, mediana / p25 | −59,4 / −63,3 | −59,6 / −64,2 | −58,9 / −62,9 | −61,9 / −66,4 | −56,0 / −59,1 |
| voz × piso (média da voz − mediana do piso) | 43 dB | 43 dB | 43 dB | 45 dB | 40 dB |
| música | não | não | não | não | não (piso 3 a 6 dB mais alto que os outros, constante) |
| efeitos | 0 | 11 trechos (10 ações) | 0 | 0 confirmados, 1 possível | 4 |
| a que estão colados | n/d | marca-texto, elipse, rasgo, notas, subida do gráfico | n/d | 1ª explosão (possível) | 3 cortes de virada, 1 portal |
| efeitos por minuto | 0 | 11,8 | 0 | 0 a 0,4 | 1,45 |
| pausas ≥ 60 ms (n · ≥ 100 ms) | 118 · 58 | 36 · 16 | 113 · 48 | 112 · 69 | 104 · 45 |
| pausa: mediana · p10 · p90 · máx (ms) | 90 · 60 · 190 · 280 | 80 · 60 · 200 · 320 | 90 · 60 · 150 · 250 | 110 · 60 · 160 · 190 | 90 · 60 · 140 · 270 |
| antes da 1ª palavra | 30 ms | 20 ms | 20 ms | 80 ms | 30 ms |
| depois da última palavra | 350 ms, cai a −86 dBFS | 120 ms, cai a −57 | 300 ms, cai a −92 | 190 ms, cai a −93 | 240 ms, cai a −68 |

Critérios: "fala" = janelas dentro das palavras da transcrição; "pausa" = canal do meio abaixo de
−40 dBFS por ≥ 60 ms (mesmo limiar nos 5, porque o loudness é igual nos 5); "lateral" = (L − R)/2.

## 3 · Música: a evidência e o limite

**Hipótese testada:** "há uma trilha por baixo da voz". Se houvesse, ela continuaria nas pausas, que
são o único lugar onde ela aparece sozinha.

1. **Piso das pausas.** O mínimo de cada pausa fica em −56 a −62 dBFS de mediana (tabela acima). Por janela
   de 15 s, a mediana desse mínimo fica dentro de uma faixa de 3 a 9 dB por vídeo, sem subir em nenhum trecho e sem
   tendência (medido); a tabela vai de −53 a −66 dBFS:

   | vídeo | 0 s | 15 | 30 | 45 | 60 | 75 | 90 | 105 | 120 | 135 | 150 | 165 |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|
   | V01 | −55,3 | −57,1 | −59,9 | −62,2 | −63,0 | −58,0 | −58,3 | −60,0 | −58,7 | −57,6 | −60,6 | |
   | V02 | −58,7 | −61,2 | −53,2 | −57,2 | | | | | | | | |
   | V03 | −59,4 | −55,2 | −61,1 | −56,9 | −62,8 | −57,6 | −60,1 | −60,8 | −57,1 | −59,4 | −58,6 | −59,0 |
   | V04 | −58,2 | −56,8 | −63,6 | −58,2 | −62,7 | −61,9 | −62,1 | −66,0 | −62,8 | −61,1 | −57,9 | |
   | V05 | −56,8 | −56,5 | −54,0 | −56,8 | −54,0 | −55,5 | −57,2 | −54,4 | −57,4 | −54,8 | −56,8 | |

2. **Canal lateral nas pausas:** −120 dB (zero digital) na mediana das pausas dos 5 vídeos. Trilha
   estéreo apareceria aqui primeiro. Nos vídeos estéreo (V02, V05) o lateral só acende nos efeitos.
3. **Graves nas pausas** (< 150 Hz): mediana −56 a −64 dBFS por vídeo, sem trecho mais alto. Bumbo ou baixo de
   música levantariam os graves de forma periódica.
4. **Tom nas pausas.** O espectro médio de 31 a 103 trechos de pausa por vídeo não tem pico tonal acima
   de +8 dB do entorno; os picos que existem caem em 86 a 215 Hz (altura da voz dele, rabo de fala) ou
   são isolados (medido no wav).
5. **Fim do vídeo:** depois da última palavra o som cai até −86 a −93 dBFS em V01, V03 e V04 (silêncio
   digital). Nenhum vídeo tem música de saída.

**Limite da afirmação.** Uma cama constante levantaria o mínimo de quase todas as pausas até o nível
dela. Pelo p25 desse mínimo, ela teria de estar abaixo de ≈ −59 dBFS (V05), −63 (V01, V03), −64 (V02)
ou −66 dBFS (V04): 42 a 50 dB abaixo da voz. Uma trilha de reel comum fica 15 a 25 dB abaixo da voz e
seria vista com folga. **Confiança: alta para "não há música audível"; não dá para excluir um ruído de
sala ou uma cama mono abaixo de −59 dBFS.** V05 é o único com piso um pouco mais alto e mais grave
(constante do começo ao fim, compatível com ruído de sala ou compressão mais forte): é o 1º trecho
para ouvir (seção 7).

## 4 · Efeitos sonoros

### 4.1 Como foi procurado (igual nos 5)

- **Detector estéreo** (V01, V02, V05): trechos com lateral > −60 dB, juntando buracos de até 150 ms,
  com ≥ 100 ms de duração. Para cada trecho: espectro do lateral no wav (faixas), forma do envelope e o
  evento visual mais próximo.
- **Detector mono** (os 5): agudos (> 6 kHz) e graves (< 150 Hz) relativos ao meio. **Teste de
  sensibilidade:** aplicado aos 11 efeitos conhecidos de V02, ele não os separa do acaso (percentil
  dos efeitos 78 a 99, acaso 91 a 96). Conclusão: **debaixo da voz, num vídeo mono, um efeito no nível
  dos de V02 (20 a 40 dB abaixo da voz) não é detectável por envelope.** Só dá para ver efeito mono que
  caia numa pausa e passe de ≈ −55 dBFS.
- **Teste das pausas** (os 5): pausas que contêm um corte × pausas sem evento. Se houvesse whoosh ou pop
  no corte, as pausas com corte seriam mais altas. São **mais baixas** nos 5 (mínimo mediano −58,0 a
  −65,1 dBFS com corte, contra −55,3 a −59,4 sem evento), porque são as pausas de fim de frase.
- **V04** (os 2 trechos citados na análise): espectrograma `scratchpad/e3/som/V04-explosao.png` e
  `V04-rolo.png` + envelope por 50 ms.
- **V01:** os 2 picos laterais da análise (64,92 s e 77,78 s) têm 96 a 97 % da energia em 6 a 12 kHz,
  duram 50 a 70 ms e caem nos "s" de "physicist" e "ask a surfer": artefato de codificação em
  sibilante, não efeito. Os outros 17 blipes laterais duram 10 a 60 ms e ficam abaixo de −42 dB.

### 4.2 Todos os efeitos localizados

Nível relativo à voz = nível do lateral menos o RMS médio da fala do mesmo vídeo (−16,5 dBFS). É um
**limite inferior**: o lateral só mostra a parte estéreo do efeito. Deslocamento = início do som menos o
1º quadro do evento visual (negativo: o som vem antes).

**V02** (11 trechos; 23,976 qps)

| # | tempo (s) | dur. | lateral pico / RMS | rel. à voz (pico / RMS) | faixa (energia do lateral) | evento visual colado | desloc. |
|---|---|---|---|---|---|---|---|
| E1 | 2,67–3,12 | 450 ms | −32,9 / −37,8 | −16 / −21 dB | agudo: 2–6 kHz 53 %, 6–12 kHz 46 % | V02-A01 f64 coluna sobe + câmera inclina | +1 ms |
| E2 | 12,73–12,89 | 160 ms | −54,2 / −60,5 | −38 / −44 dB | muito agudo: > 6 kHz 100 % | V02-A04 f300–f305 linha do tempo entra e pousa | +217 ms (fraco) |
| E3 | 24,54–24,69 | 150 ms | −34,6 / −42,2 | −18 / −26 dB | agudo: 6–12 kHz 59 %, 2–6 kHz 30 % | V02-A07 f594 marca-texto 1 | −235 ms |
| E4 | 25,97–26,56 | 590 ms | −37,7 / −46,9 | −21 / −30 dB | misto: 0,5–2 kHz 40 %, 6–12 kHz 40 % | V02-A07 f630 marca-texto 2 (acaba 133 ms antes do doc 3 pousar, f640) | −306 ms |
| E5 | 36,09–36,68 | 590 ms | −38,0 / −45,6 | −22 / −29 dB | agudo: 6–12 kHz 57 % | V02-A09 f846–f876 notas se abrem em leque (som na 2ª metade, acaba com o leque) | +805 ms do início do leque |
| E6 | 42,35–42,61 | 260 ms | −38,9 / −48,6 | −22 / −32 dB | médio-grave: 150 Hz–2 kHz 89 % | **nenhum** (V02-A10, folha parada para leitura) | n/d |
| E7 | 43,66–44,26 | 600 ms | −24,6 / −40,0 | −8 / −24 dB (o mais forte) | agudo: 2–12 kHz 99 % | V02-A10 f1049 elipse à mão | −92 ms |
| E8 | 45,19–45,59 | 400 ms | −40,3 / −52,7 | −24 / −36 dB | médio-agudo: 2–6 kHz 79 % | V02-A10 f1085 1ª linha do marca-texto | −64 ms |
| E9 | 45,74–46,33 | 590 ms | −41,4 / −53,2 | −25 / −37 dB | médio: 0,5–2 kHz 73 % (pulsos) | V02-A10 f1089 cascata de marca-texto (continuação de E8) | +320 ms |
| E10 | 47,04–47,75 | 710 ms | −27,3 / −39,4 | −11 / −23 dB | agudo: 2–12 kHz 97 % | V02-A10 f1127 parte da folha se separa (rasgo); o som acaba 48 ms antes do corte f1146 | +35 ms |
| E11 | 50,03–50,23 | 200 ms | −29,4 / −40,1 | −13 / −24 dB | grave-médio: 150–500 Hz 50 % | V02-A11 f1206 marca-texto no número | −270 ms |

Leitura (inferido): E1 sopro de subida; E2 tique de pouso; E3, E4, E8, E9, E11 marcador riscando; E5
farfalhar de notas; E7 caneta riscando; E10 papel rasgando; E6 sem explicação visual (papel?). Os
efeitos têm L e R com o mesmo RMS: são sons estéreo abertos, não sons jogados para um lado.

**V05** (4 trechos; 23,976 qps)

| # | tempo (s) | dur. | lateral pico / RMS | rel. à voz (pico / RMS) | faixa | forma | evento visual colado | desloc. |
|---|---|---|---|---|---|---|---|---|
| R1 | 18,83–20,42 | 1590 ms | −26,5 / −40,0 | −10 / −24 dB | grave: < 500 Hz 71 % (pico 132 Hz) | sobe 1,15 s até o pico em 19,98 s, cai em 0,44 s | **corte f480** (cena → rosto com título V05-A08); fala: "...for the entire world?" → "This is" | pico 40 ms antes do corte |
| R2 | 36,99–38,60 | 1610 ms | −23,8 / −36,4 | −7 / −20 dB | grave: < 500 Hz 94 % (pico 107 Hz) | sobe 1,54 s até 38,53 s e para seco no corte | **corte f925** (rosto com texto grande V05-A12 → mapa V05-A13); fala: "the one exception." | pico 50 ms antes do corte; fim +20 ms |
| A3 | 87,18–89,40 | 2220 ms | −38,2 / −47,4 | −22 / −31 dB | médio: 150 Hz–2 kHz 95 % | nível plano o plano inteiro | **portal** V05-A28 f2087 → foto de Sídon V05-A29; acaba no corte f2144 | início +135 ms; fim −23 ms |
| R4 | 124,56–126,02 | 1460 ms | −27,4 / −39,1 | −11 / −23 dB | grave: < 500 Hz 71 % (pico 149 Hz) | sobe 1,03 s até 125,59 s, cai em 0,43 s | **corte f3012** (rosto com texto grande V05-A41 → cruzados V05-A42); fala: "their monopoly backfired." | pico 40 ms antes do corte |

Nas subidas, o fim da frase e a pausa antes do corte ficam preenchidos pelo próprio efeito: o canal do
meio fica em ≈ −25 a −35 dBFS nesse vão (8 a 19 dB abaixo da média da voz). Ou seja: as pausas de virada
de V05 não são silêncio, são o efeito subindo (observado no envelope de 50 ms). Leitura (inferido): R1,
R2, R4 = "riser" ou "swell" grave; A3 = ambiência da foto (vento, mar ou multidão?).

**V04** (mono; 1 possível)

| tempo | o quê | evento | desloc. | confiança |
|---|---|---|---|---|
| 30,80 s | transiente de banda larga (20 Hz a > 12 kHz), ≈ 10 ms, no meio de "from above", onde a fala não tem consoante explosiva | V04-A08 f738, 1ª explosão pequena | +20 ms | baixa (mono, voz por cima) |

Não confirmados em V04: o risco de 31,6 s cai no início de "their" (fala); a energia grave de 151,6 a
152,5 s (rolo de impressão, V04-A48) é compatível com voz rouca de fim de frase ("printed on cloth") e a
pausa seguinte não tem ronco. Explosões 2 (f748) e 3 (f758): nada fora da fala.

**V01 e V03:** nenhum efeito.

### 4.3 Teste inverso: que tipo de evento visual tem som junto

Eventos = cortes secos (tabelas de planos) + entradas das pastas A (`eventos.json`) + passos internos
(tabelas dos `notes.md`), tipo atribuído por palavras-chave e conferido à mão nos casos com som
(621 eventos). "Com som" = um efeito começa entre 400 ms antes e 300 ms depois do evento, ou, nos
cortes, o pico de um efeito cai a ±100 ms dele. "Acaso" = a mesma medida em instantes a cada 50 ms.

| tipo de evento | V01 (estéreo) | V02 (estéreo) | V03 (mono) | V04 (mono) | V05 (estéreo) | total medido |
|---|---|---|---|---|---|---|
| corte seco | 0 / 34 | 0 / 13 | 0 sinal / 44 | 0 sinal / 41 | **3 / 38** (risers de virada) | 3 / 85 nos estéreo |
| pop de cartão / foto / recorte | 0 / 36 | 1 / 12 (fraco) | n/d / 59 | n/d / 41 | 0 / 21 | 1 / 69 |
| chicote / deslize | 0 / 11 | 1 / 3 (coluna que sobe) | n/d / 3 | n/d / 6 | 0 / 5 | 1 / 19 |
| marca-texto | 0 / 5 | **5 / 11** | n/d / 1 | n/d / 2 | n/d / 0 | 5 / 16 |
| traço à mão (círculo, elipse, seta, contorno) | 0 / 20 | 1 / 5 (elipse) | n/d / 3 | n/d / 3 | 0 / 12 | 1 / 37 |
| etiqueta (nome, data) | 0 / 4 | 0 / 4 | n/d / 28 | n/d / 4 | 0 / 13 | 0 / 21 |
| texto grande palavra a palavra | n/d | n/d | n/d | n/d / 2 | 0 / 32 como gatilho (2 blocos ficam por baixo de um riser) | 0 / 32 |
| zoom / câmera | 0 / 1 | 0 / 4 | n/d / 7 | n/d / 5 | 0 / 7 | 0 / 12 |
| portal (zoom para dentro do aro) | n/d | n/d | n/d | n/d / 2 | 1 / 4 (ambiência) | 1 / 4 |
| cena 3D (eventos dentro de cenas 3D) | n/d | n/d | n/d | n/d | 0 / 44 | 0 / 44 |
| troca de estado (cor, água, calor) | 0 / 14 | 0 / 3 | n/d | n/d / 6 | 0 / 9 | 0 / 26 |
| explosão, fogo, tiro, desmoronamento | n/d | n/d | n/d | 1 possível / 4 | 0 / 6 | 0 / 6 nos estéreo |
| papel físico (rasgo, notas, tesoura) | 0 / 1 | **2 / 4** (leque, rasgo) | n/d / 2 | n/d / 1 | n/d | 2 / 5 |
| **acaso** (instante qualquer) | 0 % | 13,9 % | n/d | n/d | 1,7 % (pico ±100 ms: 0,5 %) | |

"n/d" nos mono = não detectável debaixo da voz (4.1). "0 sinal" nos cortes mono = o teste das pausas não
mostrou nada (as pausas com corte são as mais silenciosas). Chicotes que caem em pausa ficam em silêncio:
V01 f197 (whoosh borrado, 8,21 s: meio −51 a −62 dBFS, agudos −78 a −80), f1339 e f1532 (−57 a −62 antes
do 1º som da fala), V03 f3754 (−54 a −58). Leitura: em V02, marca-texto tem som em 45 % dos casos contra
14 % do acaso (3,3×); em V05, corte com pico de efeito em 8 % contra 0,5 % do acaso, mas só nos 3 cortes
de virada de capítulo; todos os outros tipos ficam no acaso ou abaixo.

## 5 · Regras

Força: **[3+]** regra em 3 ou mais vídeos · **[2]** em 2 vídeos · **[1]** dentro de 1 vídeo · **[oc.]** ocorrência.

1. **Sem música, do início ao fim.** 5 de 5; cama possível só abaixo de −59 dBFS. **[3+]**
2. **Voz mono no centro, −14 LUFS, compressão forte** (LRA 2,2 a 4,1 LU; RMS médio da fala −16,3 a
   −16,6 dBFS; o integrado varia só 0,2 LU entre os 5). **[3+]**
3. **Corte seco não leva whoosh nem pop.** 0 de 34 (V01), 0 de 13 (V02), 0 de 35 cortes comuns (V05),
   nenhum sinal nos 85 de V03 e V04. **[3+]**
4. **Pop de cartão, etiqueta, legenda, texto grande, zoom e troca de cor não levam efeito.** 1 de 69
   pops (um tique fraco, −38 dB, em V02), 0 de 21 etiquetas, 0 de 32 palavras de texto grande, 0 de 26 trocas nos estéreo. **[3+]**
5. **Chicote e whoosh visual são mudos.** 0 de 11 em V01, 0 de 5 em V05; os que caem em pausa ficam em
   silêncio (V01, V03). A única exceção é o gráfico que sobe com a câmera em V02 (E1, um sopro). **[3+]**
6. **Fala corrida, respiro curto:** pausa mediana 80 a 110 ms, p90 140 a 200 ms, máxima 190 a 320 ms;
   fim de frase ≈ 140 ms (178 casos); antes de pergunta ≈ 120 ms (11) e antes de virada ("But", "So",
   "Instead"...) ≈ 140 ms (39): a virada não ganha silêncio maior. **[3+]**
7. **Começa e acaba seco:** 1ª palavra em 20 a 80 ms; 120 a 350 ms depois da última palavra o som cai ao
   piso ou ao silêncio digital; sem música nem efeito de saída. **[3+]**
8. **O corte cai no silêncio entre frases:** 63 % dos 170 cortes caem em pausa (V02, o anúncio, é a
   exceção: 15 %); a 1ª palavra do plano novo vem mediana +47 ms depois do corte (p10 −3, p90 +147). **[3+]**
9. **A imagem antecipa a palavra:** entrada das pastas A mediana −40 ms da palavra-gatilho (p10 −162,
   p90 +103; 96 antes, 65 junto, 31 depois). V02 é o único com mediana 0. **[3+]**
10. **Explosão, fogo e cena 3D são mudos.** V05: 0 de 6 explosões, fogo ou tiro, 0 de 44 eventos em cena
    3D; V04: 1 transiente possível em 4. **[2]**
11. **Quando há foley, é de papel e caneta, colado à anotação à mão:** marca-texto (5 de 11), elipse,
    rasgo, notas em leque, gráfico que sobe; 150 a 710 ms; 2 a 12 kHz na maioria; pico 8 a 38 dB e RMS 21 a
    44 dB abaixo da voz. O som do marcador começa **60 a 310 ms antes** do traço aparecer; o de
    movimento físico cai junto (+1 e +35 ms). **[1]** (só V02, que é um anúncio, não uma curiosidade)
12. **Subida grave que estoura no corte de virada de capítulo:** 1,0 a 1,5 s de subida, energia < 500 Hz,
    pico 40 a 50 ms antes do corte, cauda de 0,4 s ou corte seco; nas 3 viradas "pergunta-tese → título",
    "a única exceção → a história" e "deu errado → a consequência". Preenche a pausa da virada. **[1]**
    (V05, 3 vezes)
13. **Ambiência por baixo de uma foto de lugar, do portal até o corte.** **[oc.]** (V05 A3)
14. **Um foley sem evento visual** (V02 E6, folha parada). **[oc.]**

## 6 · Molde de som para um vídeo novo (qualquer tema)

| item | recomendado | faixa vista |
|---|---|---|
| voz | mono no centro; **−14 LUFS integrado**; pico real ≤ −1 dBTP; compressão forte (LRA ≈ 3 LU); fala com RMS médio ≈ −16,5 dBFS | −14,1 a −14,3 LUFS · LRA 2,2–4,1 · pico −1,6 a +0,5 dBTP (V04 estoura; não copiar) |
| piso entre frases | ruído de sala limpo ≈ −60 dBFS (mínimo da pausa); sem gate que deixe silêncio digital no meio | mediana do mínimo −56 a −62 dBFS |
| música | **não tem.** Os 5 são só voz; o ritmo vem da fala corrida e dos cortes. | 0 de 5 |
| efeitos | **nenhum por padrão** (3 de 5 vídeos). | 0 a 11,8 por minuto (V01, V03, V04: 0; V05: 1,45; V02: 11,8) |
| efeito opcional A: foley de anotação | papel ou caneta só quando a cena mostra a mão anotando: marca-texto, círculo/elipse, rasgo, notas; 150–700 ms; RMS ≈ 30 dB abaixo da voz (pico ≥ 8 dB abaixo); o som começa 60–300 ms antes do traço aparecer | V02: 10 ações em 56 s |
| efeito opcional B: subida de virada | 1 a 3 por vídeo, só no corte de virada de capítulo (pergunta-tese → título; "a exceção"; "deu errado"); grave (< 500 Hz), 1,0–1,5 s de subida, pico 40–50 ms antes do corte, cauda ≤ 0,45 s; no vão antes do corte o efeito fica ≈ 8–19 dB abaixo da média da voz | V05: 3 em 165 s |
| efeito opcional C: ambiência | só sob uma foto de lugar que entra por portal; nível plano ≈ 30 dB abaixo da voz, do portal até o corte | V05: 1 |
| NUNCA leva efeito | corte seco comum, pop de cartão ou recorte, etiqueta, legenda, palavra do texto grande, chicote ou deslize, zoom, troca de cor, cena 3D, explosão ou fogo desenhados | 0 em todos os medidos |
| silêncios | sem silêncio dramático: respiro ≈ 90 ms entre blocos, ≈ 140 ms no fim de frase, máximo ≈ 300 ms; a pausa de pergunta e de virada é igual à de fim de frase (ou, no estilo V05, preenchida pela subida) | mediana 80–110 · máx 190–320 ms |
| começo e fim | voz em ≤ 80 ms; termina 150–350 ms depois da última palavra, com o som caindo ao silêncio; sem vinheta | 20–80 ms · 120–350 ms |
| sincronia com a imagem | corte na pausa, ≈ 50 ms antes da 1ª palavra do plano novo; imagem nova ≈ 40 ms antes da palavra que ela mostra | mediana −40 ms (p10 −162, p90 +103) |

Teste de generalização: num reel sobre Claude Code, a voz sai a −14 LUFS sem trilha, os prints e
cartões entram mudos; se a cena mostrar o Claude "riscando" uma linha do código com marca-texto, pode
entrar o foley do marcador 0,1–0,3 s antes do traço; a subida grave só no corte de "e foi aí que deu
errado". Num reel sobre café: mesma voz, sem trilha; a moka, o grão e a etiqueta "1933" entram mudos; o
foley de papel só se a cena rasgar ou anotar uma ficha; a subida só na virada da história.

## 7 · O que o Felipe precisa ouvir (com fone)

1. **Música muito baixa?** V05 0 a 30 s e as pausas 22,9–23,3 s e 103,6–104,1 s (piso mais alto que nos
   outros). Comparar com V04 105–120 s (o piso mais limpo).
2. **V05 18,8–20,4 s:** o som que sobe até o corte do título. Subida? sopro? acorde?
3. **V05 37,0–38,6 s:** "the one exception." até o corte para o mapa. Mesmo som do item 2?
4. **V05 87,2–89,4 s:** foto de Sídon depois do portal. Que ambiência é (vento, mar, multidão)?
5. **V05 124,6–126,0 s:** "backfired." até os cruzados. Subida com impacto no corte, ou só subida?
6. **V02 43,7–44,3 s** (elipse: caneta?), **45,2–46,3 s** (cascata de marca-texto), **47,0–47,8 s** (rasgo),
   **2,7–3,1 s** (coluna sobe: sopro?), **36,1–36,7 s** (notas) e **42,4–42,6 s** (sem nada na tela: o que é?).
7. **V04 30,6–31,1 s:** há um estalo de explosão em "from above"? E **151,6–152,6 s**: o rolo tem som?
8. **V01 8,1–8,4 s:** o whoosh borrado da imagem é mudo mesmo?

## 8 · Confiança

- **Medido:** loudness, picos, níveis da voz, piso e duração das pausas, presença e forma de todo som no
  canal lateral, faixas de frequência dos efeitos estéreo, deslocamentos em ms contra quadros e
  palavras, teste das pausas nos cortes, o "0 de N" dos vídeos estéreo.
- **Observado:** forma das subidas de V05 e o meio a −25/−35 dBFS no vão antes do corte (envelope de
  50 ms); o transiente de V04 a 30,80 s (espectrograma).
- **Inferido:** todo nome de efeito (sopro, marcador, caneta, papel, riser, ambiência, impacto) e o que
  a ambiência de V05 representa; a ausência de efeito mono debaixo da voz em V01, V03 e V04 (não é
  detectável, só não há sinal nas pausas).
- **Limites:** (1) em V01, V03 e V04 um efeito baixo debaixo da voz passaria despercebido; (2) o nível dos
  efeitos estéreo é limite inferior (só a parte L − R); (3) os tipos de evento vêm de palavras-chave dos
  `notes.md`, conferidos à mão só nos eventos com som; (4) amostra pequena: as regras 11 a 14 saem de um
  vídeo cada, e V02 é um anúncio, não uma curiosidade.
- **Onde este arquivo discorda das análises:** V04 tinha 2 transientes de explosão e um rolo prováveis;
  aqui só 30,80 s fica sem explicação pela fala (31,6 s é o início de "their"; o rolo não se confirma).
  V02 f588–f592 estava atribuído ao documento que pousa; pelo tempo, ele é do marca-texto 1 (−235 ms; o
  documento entrou por corte 0,9 s antes). V05: R1 e R4 são subidas com pico no corte, não um som "para o
  título" nem um impacto separado. Pausas: com o limiar único de −40 dBFS, a máxima de V05 é 270 ms (a
  análise deu 470 ms com −36,5 dB), e as pausas de virada de V05 estão cheias do próprio efeito.
