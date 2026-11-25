# Trecho 02 · Três discos creme, um por ferramenta + etiqueta · P14 + P05 · Ref V01-A28, V04-A09
Fala: "três ferramentas de IA totalmente gratuitas"   ·   Janela no clipe: 960 a 3178 ms (cena: q22 a q75 = 917,6 a 3128,1 ms)   ·   Entra por: corte seco (vindo do rosto, trecho 1)

*Spec do agente-s1, 20/11/2026. Quadros do clipe a 23,976 fps (q = nº do quadro, tempo = q × 41,708 ms). Tempos
das palavras = transcrição (`palavras-corte.json`), a reconferir no envelope antes de construir (ver §6).*

## 1 · Linha do tempo da cena (relativa às palavras)

Cadência: segue o `00-globais.md` §8 (**23,976 imagens/s**; pops e assentamentos em degraus de 2 q, sem interpolar).
A referência (V01) anda a 12 imagens/s com tremor de stop-motion; isso fica como opção "stop-motion", só sob pedido.
Os pops abaixo já estão em degraus de 2 q, então valem nos dois modos; deriva, pan e etiqueta andam quadro a quadro.

| passo | o que acontece | gatilho (palavra, índice, deslocamento em ms) | duração (ms · quadros) | curva |
|---|---|---|---|---|
| 1 | Corte seco do rosto para a mesa escura já com o grupo 1 (disco 1 + recorte 1, Docs) em pop desencontrado | 42 ms antes do início de "três" (5) → q22 | 167 ms · 4 q (2 imagens), assenta em q26 | estalo, sem quadros intermediários |
| 2 | Grupo 2 (disco 2 + recorte 2, Design) pipoca por cima, à direita e mais alto | 72 ms antes do início de "ferramentas" (6) → q28 | 167 ms · 4 q, assenta em q32 | estalo |
| 3 | Câmera desce o conjunto inteiro (ver §2, Câmera) | de q32 a q46 | 584 ms · 14 q | linear, em degraus de 2 q |
| 4 | Grupo 3 (disco 3 + recorte 3, Slides) pipoca embaixo, na frente | 32 ms depois do início de "de" (7) = 88 ms antes de "IA" (8) → q42 | 167 ms · 4 q, assenta em q46 | estalo |
| 5 | Câmera passa a andar para a direita | de q46 até o corte (q75) | 1209 ms · 29 q | linear, degraus de 2 q |
| 6 | Etiqueta "GRÁTIS" entra deslizando pela borda direita do quadro, subindo na diagonal, e cola na borda de baixo do recorte 3 | início 228 ms antes de "gratuitas" (10) → q53; assenta 19 ms antes da palavra → q58 | 209 ms · 5 q (q53→q58) | ease-out (rápida e freia) |
| 7 | Tudo parado (só deriva da câmera), etiqueta legível | q58 a q75 | 709 ms · 17 q | — |
| 8 | Saída: corte seco para o trecho 3 (notas) | 50 ms antes de "que" (11) → q75 | 1 q | corte seco |

Diferença de cadência (registrada, pedido do principal): **a referência NÃO sustenta "uma peça por palavra"**. No
V01-A28 os três grupos entram um por **meia-frase**, ≈ 1,0 s entre eles (26 q e 24 q a 24 fps), sempre na 1ª palavra
da meia-frase (−203, −60 e −20 ms, medido). Aqui a fala dá 250 ms (6 q) entre o grupo 1 e o 2 e 584 ms (14 q) entre o 2
e o 3: 4× e 1,7× mais rápido. O mais perto disso no estilo: V03-A07 (4 itens em 2,0 s, ≈ 0,5–0,67 s cada, P14) e o
empilhar de cópias do V01-A43 (167–250 ms, P16). O grupo 2 começa 83 ms depois de o grupo 1 assentar; nenhuma
entrada se sobrepõe à anterior (pop de 167 ms < 250 ms). Mantida a colocação pedida porque a sincronia manda; cada
entrada fica dentro da faixa de gatilho do P14 (−121 a +73 ms da palavra do item).

## 2 · FORMA (copiar igual) — px de 1080x1920

- **Fundo / mesa:** **a do `00-globais.md`** (uma só no vídeo). Para conferência, a mesa medida na Ref (V01-A28 f1910 e
  V01-A01): topo #161213, meio nas laterais #221e1f, centro baixo (50 %, 78 %) #181415, rodapé #100e0f, luz central
  fraca (#1f1d20), sem textura. É um pouco mais fria e menos vinhetada que o molde V03 do global, mas a diferença
  fica dentro da faixa vista.
- **Ordem das camadas (reconferida no recorte ampliado de f1910, observado):** fundo → disco 1 → disco 2 → disco 3 →
  recorte 1 → recorte 2 → recorte 3 → etiqueta → legenda. **Todos os discos ficam atrás de todos os recortes**
  (o arco do disco 2 passa por trás do recorte 1); o disco mais novo fica por cima do disco mais velho, com sombra
  escura curta na borda sobre o disco de baixo.
- **Disco (os 3):** creme de papel com grão, sem aro e sem contorno: #cac3b1 na luz, #c7c0ae na lateral (A28 f1910,
  medido); faixa do molde #c6bdac a #dbd3c0. Sombra escura curta na borda (observado; 3 px em 1080, inferido).
- **Disposição final (q46, os 3 assentados, antes de a câmera andar para a direita)** — medido por ajuste de círculo na
  borda de cada disco em V01-A28 f1850/f1876/f1900/f1910 (agente-s1), ×1,5:

  | peça | centro (x, y) | tamanho | giro | confiança |
  |---|---|---|---|---|
  | disco 1 | (381, 644) | Ø 674 (nasce Ø 642 em q26 e cresce, ver Câmera) | — | medido (resíduo 0,6 px) |
  | recorte 1 · Docs | (396, 686) | 400 × 918 (proporção 1:2,3) | 0° | posição medida; largura = inferido (adaptação, §6) |
  | disco 2 | (759, 593) | Ø 492 (nasce Ø 483 em q32) | — | medido (resíduo 0,3–0,8 px) |
  | recorte 2 · Design | (779, 532) | 362 × 644 (9:16) | 0° | topo medido; tamanho = inferido (adaptação) |
  | disco 3 | (557, 1035) | Ø 460 | — | medido aproximado (só ≈ 120° do arco de baixo visível; faixa Ø 380–460) |
  | recorte 3 · Slides | (562, 1012) | 576 × 324 (16:9) | 0° | centro medido; tamanho = inferido (adaptação) |
  | etiqueta | (618, 1183) | 191 × 56 | −1,5° | ver Etiqueta |

  - Regras de encaixe recorte × disco (medido em A28, valem se o principal ajustar tamanhos): recorte 1 passa
    **96 px acima do topo** do disco 1 e **179 px abaixo da base** (topo y 203 e base y 1121 em q26), centrado 15 px à
    direita do centro do disco; recorte 2 passa **141 px acima do topo** do disco 2 (topo y 186 em q32, base y 830); o
    recorte 3 fica centrado no disco 3 (+5, −23 px), cobrindo a faixa do meio, e passa da borda do disco dos dois lados.
  - Conjunto final (q46): x 44–1005 × y 210–1265 = 89 % × 55 % do quadro (A28: 90 % × 57 %, medido). A base fica logo acima
    da caixa da legenda (y ≈ 1273).
  - O que sangra: nada no assentado; com a câmera andando para a direita, o disco 2 encosta/sangra a borda direita no
    fim (≈ +78 px, inferido).
- **Recorte (os 3), receita de forma** (seção "O recorte", V01 = regra; A01 medido): contorno de adesivo off-white
  uniforme de **15 px** (10 px em 720, luminância 202–233), com textura de papel, e sombra fina escura em volta
  (≈ 2 px, observado). Cor original da fonte, sem filtro.
- **Câmera** (medido em A28 por ajuste de círculo; o caminho entre os pontos é inferido linear):
  - grupo 1: escala **+6 %/s** em torno do centro do disco 1, de q26 até o corte (A28: Ø 428 → 466 em 36 q);
    grupos 2 e 3: **+2 %/s** (A28 disco 2: 322 → 328 em 24 q);
  - **conjunto inteiro desce 1,7 px/q** de q32 a q46 (A28 f1876→f1900: +27 px em 720, todos os discos juntos) = 24 px;
  - **conjunto inteiro anda 2,7 px/q para a direita** de q46 até o corte (A28 f1900→f1918: +32 px em 18 q, em 720) =
    ≈ 78 px; vertical ≈ +0,3 px/q.
  - Deriva e pan contínuos, quadro a quadro (global). Só no modo "stop-motion": degraus de 2 q e tremor de ±2 a 3 px
    por imagem (A01, observado).
  - Corta em movimento (o corte para o trecho 3 cai com a câmera andando).
- **Entrada de cada grupo** (pop desencontrado: o disco cresce, o recorte encolhe; valores por imagem de 2 q):
  - grupo 1 (medido em A28 f1846/f1848/f1850): disco **95 % → 100,7 % → 100 %**; recorte **107,8 % → 102,6 % → 100 %**.
    Recorte e disco entram no MESMO quadro (q22).
  - grupo 2 (medido f1872/f1874/f1876): disco **84 % → 100,5 % → 100 %**; recorte ≈ **106 % → 101,5 % → 100 %**
    (inferido do topo y73 → y103 → y113 com a base fixa). Mesmo quadro (q28).
  - grupo 3: disco não medido (atrás do recorte); usar o do grupo 2. Recorte **108 % → 102,5 % → 100 %** (molde; A28
    assenta em 2 imagens, f1896→f1900, medido). Mesmo quadro (q42).
  - Sem borrão, sem quadros intermediários, sem quique.
- **Etiqueta "GRÁTIS"** (P05 variante B, V04-A09):
  - Posição final: atravessando a **borda de baixo do recorte 3**, à direita do centro: começa a 43 % da largura do
    recorte (x 522) e vai até x 713; ≈ 1/3 da altura da tira dentro do recorte e 2/3 abaixo (y 1155–1211). Anda junto
    com o grupo 3 (escala e câmera). (A09: tira de x 314–541 sobre a borda de baixo de um cartão de 628 px, começando a
    43 % da largura dele, medido; "1/3 dentro" observado na folha ampliada.)
  - Tira: **191 × 56 px**, papel creme **#ddc5b1** com grão (A09 medido), bordas de papel cortado levemente
    irregulares, sombra curta embaixo 3 px (observado), sem contorno, sem canto arredondado. Comprimento = texto + 16 px
    de margem de cada lado (11 px em 720, medido em A13). Altura: 56 px (faixa 52–60; A09 ≈ 35–37 px em 720 na folha
    ampliada, A13 40 px medido).
  - Texto: `GRÁTIS`, caixa-alta, uma linha, **Inter Bold** (como no global; alternativas Arimo Bold / Arial Bold),
    corpo **41 px** = altura de maiúscula **30 px** (20 px em 720, observado na folha ampliada de A09; a nota dizia
    "condensada", mas a folha ampliada mostra largura normal), cor **#111111**, alinhado à esquerda com margem de 16 px,
    centrado na vertical da tira.
  - **Diferença em relação ao `00-globais.md` §5:** o global traz o molde da variante A (V03): tira de 84 px, maiúscula
    de 42 px, papel #b5b1a8, margem de 33 px. Esta spec usa a variante B medida na Ref escolhida (V04-A09): tira de
    56 px, maiúscula de 30 px, papel #ddc5b1, margem de 16 px. O guia separa as duas variantes (V04: letras de 17 a
    21 px em 720). Se o principal preferir uniformizar com o global: tira 84 × 271 px, maiúscula de 42 px.
  - Entrada (reconferida em A09 com `dif` quadro a quadro, f796→f801, medido): vem de fora pela **borda direita do
    quadro**, só a ponta visível no 1º quadro, **sobe na diagonal** e freia. Deslocamento restante até a posição final,
    por quadro (1080): q53 **(+528, +77)** → q54 (+354, +69) → q55 (+211, +47) → q56 (+101, +23) → q57 (+29, +8) → q58
    **(0, 0)**. Giro: ≈ +4° (horário) em q53–q54 → ≈ 0° em q55–q56 → −1,5° assentada (observado na folha ampliada; a
    nota dizia −3°). 5 q = 209 ms (a nota dizia 4 q observado; o `dif` mostra movimento em f796, 797, 798, 799, 800 e
    parada em f801).
  - Saída: fica até o corte (A09: fica até a cena acabar).
- **Taxa de imagem:** 23,976 imagens/s (global), com pops em degraus de 2 q. A Ref anda a 12 (opção "stop-motion").
- **Som:** nenhum (A28 e A09, medido).

## 3 · CONTEÚDO (deste vídeo)

| lacuna (papel) | preenchida com | receita de tratamento |
|---|---|---|
| item 1 da lista (grupo 1, o maior, à esquerda) | **Claude Docs**: o documento real que o Felipe gerou, página em pé | print do próprio Felipe, captura de rolagem cortada em 1:2,3 (página longa em pé), cor original, sem filtro; recorte retangular com contorno de adesivo off-white 15 px + textura de papel + sombra fina; 0° |
| item 2 (grupo 2, à direita e alto) | **Claude Design**: uma peça vertical real feita na ferramenta (ex.: story/capa 9:16) | print do próprio Felipe, 9:16, mesmo tratamento |
| item 3 (grupo 3, embaixo e na frente) | **Claude Slides**: um slide real da apresentação que ele gerou | print do próprio Felipe, 16:9, mesmo tratamento |
| dado que o espectador guarda (etiqueta) | `GRÁTIS` | sem imagem; o texto como a fala diz, caixa-alta (ver dúvida 1) |

Regra de escolha (P14): sempre o LITERAL; o "retrato oficial" de cada ferramenta é **o resultado real dela**. O ícone
oficial fica como reserva: um ícone quadrado maior que o disco cobre o palco inteiro e quebra a regra "recorte maior
que o disco, com o disco aparecendo", e o estilo não usa ícone (G5: "nenhuma ilustração gerada, ícone ou 3D").
Por que essa ordem (Docs, Design, Slides) e não a do trecho 4: a forma pede peças altas nos grupos 1 e 2 e uma peça
larga e baixa no grupo 3 (em A28 o 3º recorte é uma pessoa sentada, mais larga que alta). A fala do trecho 2 não diz os
nomes, então a ordem não quebra sincronia. Ver dúvida 2.

## 4 · IMAGENS NECESSÁRIAS

| # | o que é, exatamente | papel | de onde pode vir | formato e tamanho mínimo | tratamento a aplicar |
|---|---|---|---|---|---|
| 1 | Página do documento gerado no Claude Docs, rolagem vertical (título + 1ª dobra legíveis no topo) | item 1 | print do próprio Felipe (tela do chat) | PNG, ≥ 600 × 1380 px (1,5× o tamanho na tela) | corte 1:2,3; contorno adesivo 15 px; sombra fina |
| 2 | Peça vertical gerada no Claude Design | item 2 | print do próprio Felipe | PNG, ≥ 545 × 966 px | 9:16; mesmo tratamento |
| 3 | Um slide gerado no Claude Slides (o mais legível, com título grande) | item 3 | print do próprio Felipe | PNG, ≥ 864 × 486 px | 16:9; mesmo tratamento |
| — | Etiqueta | — | gerada no motor (texto + papel) | — | grão de papel, borda irregular |

Os arquivos 1 a 3 são os MESMOS do trecho 15 (callback): gerar uma vez, com o contorno já aplicado.

## 5 · Piso de leitura e ritmo

- Cena de tela cheia: q22→q75 = **2210 ms** (≥ 1,5 s, ok).
- Imagem de série (cada grupo até o corte): grupo 1 2210 ms, grupo 2 1960 ms, grupo 3 **1376 ms** (≥ 1,2 s, ok).
- Texto parado (etiqueta completa até o corte): q58→q75 = **709 ms** (≥ 700 ms, ok por 9 ms). Para fechar o piso, a
  etiqueta começa a deslizar **228 ms antes** de "gratuitas" e assenta 19 ms antes da palavra. Em A09 ela começa
  140 ms antes e assenta 68 ms depois. Copiar A09 à risca (início em q55) deixaria só 625 ms parada (abaixo do piso; o
  mínimo visto no P05 é 540 ms). Alternativa, se o principal preferir A09 exato: atrasar o corte do trecho 3 até q77
  (+33 ms depois de "que"; fora da faixa do P16, de 19 a 123 ms antes).
- Ritmo: 3 peças + 1 etiqueta em 2,2 s (A28: 3 peças em 3,9 s).

## 6 · Dúvidas e o que não foi possível medir

1. **"GRÁTIS" quebra uma regra do P05.** O guia diz que a etiqueta é só para **data ou nome próprio**, "nunca para outra
   palavra (verbo, adjetivo, conceito)". "Gratuitas" é adjetivo. Há precedente de número em tira só no V02 (anúncio:
   contador, duração m:ss). Alternativa mais perto da regra: `US$ 0`. Decisão do Felipe ou do principal.
2. Ordem das ferramentas nos discos (Docs, Design, Slides) ≠ ordem do trecho 4 (Slides, Docs, Design). Se o principal
   quiser a ordem do trecho 4, o Slides (16:9) vai para o disco 1 e a regra de altura do recorte 1 não fecha.
3. **Proporção dos recortes:** em A28 os recortes são pessoas em pé, estreitas: 0,47 × 1,43 o Ø do disco. Prints de
   página e de slide não têm essa forma. Mantidos o transbordo vertical e a regra de o disco aparecer dos dois lados
   (largura ≤ 0,75 Ø). As larguras são inferidas.
4. Disco 3: só o arco de baixo está visível (Ø 380 a 460 conforme o trecho do arco); o pop do disco 3 não foi medido.
5. Taxa de imagem: o global adota 24 imagens/s; a Ref (V01) anda a 12. Se o Felipe pedir o modo "stop-motion", a
   deriva e o pan passam a degraus de 2 q com tremor, e a etiqueta (V04, medida a 24) pode ficar a 24 ou ir para 12
   (3 imagens: q53, q55, q57, assentada em q58).
6. Tempos de transcrição a reconferir no envelope: "três" (p 0,71; o início marcado, 960 ms, coincide com o fim de
   "lançar"; o whisper dava 1160 ms), "IA" (p 0,67), "que" (p 0,63). Se "três" começar ≈ 200 ms depois, o corte (q22)
   passa a antecipar demais: mover para 50 ms antes do início real.
7. Não medido: altura exata das letras da etiqueta em A09 (o giro contamina a caixa); a sombra dos discos em px.
