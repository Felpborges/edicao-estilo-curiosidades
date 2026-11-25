# V04-A16 · foto em cartão entra pela diagonal (de cima-direita) e empurra a anterior para baixo-esquerda
- Categoria: P10 · Troca de cartão por empurrão ou cobertura (provisória do analista: (provisória) troca de cartão por empurrão (push) diagonal)
- Fonte: V04 quadros f1281–f1337 (53,43–55,76 s; 57 quadros ≈ 2377 ms) (conferido, f1337: o cartão sai empurrado para cima pela obra de V04-A17 e a última faixa dele aparece no topo em f1337; antes: f1281–f1323, 43 quadros) · 23,976 fps
- Fala: "charge, and he filled the unit with artists,"
- Tipo de fala: ação narrada ("encheu a unidade de artistas")
- Gatilho: o canto do novo cartão aparece no alto à direita em f1281 (53428 ms), 88 ms após o início da palavra nº 176 "charge," (53340 ms). Conferido no strip e no `perfil` (dif 7,8 → 11,5 em f1280→f1281).
- Quadro-chave: f1310
- Camadas ativas: legenda | cena de tela cheia | transição (empurrão) | som (voz)
- Leitura dos strips: strip.jpg = quadros f1277 a f1296, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-empurrao.jpg = quadro f1286, região x0 y100 720x700 px, ampliada 1× sem suavizar (o cartão novo sobreposto ao anterior no pico do empurrão diagonal); detalhe-borda-cartao.jpg = f1310, x520 y640 200x140, 3× (borda clara e canto).

## LEITURA DE EDITOR
- Por que esta cena aqui: a frase continua sem pausa ("…in charge, and he filled…"); a troca de imagem precisa ser contínua, então é empurrão, não corte.
- Por que este design: foto de arquivo dos artistas trabalhando, em cartão; nada por cima.
- Por que estas cores: P&B quente claro (#d0c2ac), mais claro que o retrato pintado anterior: a cena "abre".
- Por que estes efeitos: vinheta forte (12 % na borda); nenhuma sombra entre os cartões.
- Por que este movimento: empurrão diagonal (o novo desce de cima-direita, o velho sai por baixo-esquerda) a ≈ 62 px/q no pico com giro de −0,5°/q; depois pan lento para a esquerda (−4 px/q) com zoom leve.
- Sensação do movimento: fluxo contínuo, "e então…"; a diagonal e o giro dão energia de página virada com a mão.

## FORMA (fixa: reproduzir igual)
- Design: foto P&B de arquivo, horizontal, borda clara, em f1300: x62 y179 658x572 = x 8,6 %, y 14,0 %, larg 91,4 %, alt 44,7 %, centro (54,3 %, 36,3 %), −0,8° (medido). Fundo quase preto com vinheta (medido, cantos #000000–#020202).
- Movimento:
  - Empurrão diagonal: o novo cartão desce do canto superior direito enquanto o anterior (A15) escorrega para baixo-esquerda e sai; ≈15 quadros f1281–f1295 (≈625 ms); curva: dif 11,5 (f1281) → 14,6 → 17,8 → 20,8 → 23,1 → 23,4 (pico f1286) → 22,5 → 21,0 → 18,6 → 18,0 → 17,1 → 11,8 → 9,8 → 8,6 → 6,8 (f1295) (medido em `perfil`).
  - Depois zoom lento: altura 44,7 % (f1300) → 46,0 % (f1320) (≈ +3 % em 0,8 s) (medido), com pan constante de ≈ −4 px/q para a esquerda no mesmo trecho (alinhado ao reestudo).
  - Saída: a peça de A17 sobe de baixo empurrando a partir de f1324; este cartão sobe e sai pelo topo em 14 q (f1324–f1337) (conferido).
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| empurrão diagonal (entra de cima-direita, anterior sai por baixo-esquerda) | f1281 | 15 quadros (625 ms) | push diagonal | lento-rápido-lento, pico f1286 | nº 176, fim da oração anterior (53340 ms) | +88 ms |

- Ritmo: cartão assentado e parado f1296–f1323 ≈ 1,15 s.
- Som: pausa f1291,1–f1294,0 com piso −68,7 dB: nenhum efeito durante o empurrão (medido em `silencios`).
- Textura (reestudo 20/11):
  - Mesa: preto (cantos #000000–#020202, nota antiga); liso, grão 0,21, PARADA (f1310×f1311, x300 y1000 200x100: +1,00; medido).
  - Foto de arquivo: papel fotográfico P&B quente com grão forte (família papel fotográfico), #d0c2ac, luma 196, grão 17,3, manchas 32,0, ac1 +0,70 (f1310 x250 y350 120x120); anda com a câmera (`--q2 1320`: +0,83 alinhado).
  - Borda do cartão: clara lisa ≈ 8 px, corte reto (detalhe-borda-cartao).
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: forte, luma 100/103/74/26/12 % (f1310); no cartão 100/93/74/56/51 %.
  - Luz da cena (correção 20/11, medido f1310, perfis p75 na foto do cartão, a superfície clara mais larga): centro da poça ≈ (57–59 %, 22–27 %) (ajuste parabólico e platô), luma de pico 209 (p75); a 100 px da borda esquerda 35–42 % e em x620 61–67 % do centro (mais luz à direita); base do cartão a 29–33 % do pico vertical. Mesa: (360,1060) 5,9 e (360,1180) 2,0 (razão 3,0). Centro e força próprios desta cena, não um multiplicador fixo do vídeo.
  - Borda borrada: nitidez 100/65/35/12/6 % (f1310).
  - Sombra entre os cartões no empurrão: nenhuma visível (detalhe-empurrao, f1286: borda clara do novo direto sobre o velho). Desfoque de movimento: sem desfoque de movimento (medido na conferência: borda de 2 a 9 px a 56–107 px por quadro); no pico do empurrão (f1286, −56 px/q) a borda mede 6,5 px, sem rastro (corrigido na conferência: era "leve no pico (f1286)").
  - Aberração: nenhuma (0,00 px).
- Câmera (reestudo 20/11): no empurrão o conteúdo anda −61,9 px/q (esquerda) e +18,7 px/q (baixo), giro −0,49°/q, escala −10 %/s (f1283→f1286); freando: −20,8 / +4,7 px/q, giro −0,14°/q (f1289→f1292). Depois: pan constante −4,0 a −4,2 px/q para a esquerda com zoom +3,4 a +3,6 %/s (f1300→f1322). Fases: empurrão (f1281–f1295, pares f1283→f1286 e f1289→f1292), pan + zoom (f1296–f1323), saída empurrada por A17 (f1324–f1337; o par f1326→f1332 não é confiável: a peça que sobe domina os pontos). (A nota antiga media só o zoom, ≈ +3 % em 0,8 s; o pan lateral não estava registrado.)
- Cadência (reestudo 20/11): 24 imagens/s (`perfil` da nota: curva contínua 11,5 → 23,4 → 6,8).
- Legenda nesta cena (reestudo 20/11): bloco de 2 palavras (f1279–f1290, atravessa a entrada) → a legenda SOME 3 quadros (f1291–f1293, pausa) → bloco de 6 palavras (f1294–f1319) → bloco de 1 palavra (f1320–f1338, atravessa a saída por empurrão). Tarja sobre a mesa preta (luma 16–18) abaixo do cartão: não se distingue e não dá medida direta (fundo ≤ 60); vale o valor do vídeo, 59 % (56 a 64), altura 48 px (y844–891), raio ≈ 7–8 px, folga 3–5 px dos lados e 11 px em cima (medido na conferência). Nenhum outro texto.

## CONSTRUÇÃO
1. mesa: preto.
2. cartão anterior (A15) saindo por baixo-esquerda, empurrado.
3. cartão novo: foto P&B quente de grão forte (σ ≈ 17), horizontal, borda clara ≈ 8 px, x 8,6 % y 14 % larg 91,4 % alt 44,7 % (centro 54,3 %, 36,3 %) ao assentar, −0,8°; entra de cima-direita por cima do anterior em 15 q (625 ms), pico ≈ 62 px/q no 5º–6º quadro, girando −0,5°/q e endireitando; sem sombra.
4. câmera depois: pan −4 px/q para a esquerda + zoom +3,5 %/s, constantes.
5. efeito de quadro: luz desta cena, poça com centro em ≈ (58 %, 25 %) (26 % a 0,75–0,90 do raio, 12 % na borda; a 100 px da borda ≈ 40 % à esquerda e 64 % à direita) + borda mole. Sem desfoque de movimento no empurrão.
6. legenda V04-L01 (some 125 ms na pausa).
- Linha do tempo (ms a partir de f1281): 0–625 ms empurrão diagonal (pico ≈ 210 ms; começa 88 ms depois da última palavra da oração anterior); 417–542 ms legenda some; 625–1793 ms pan + zoom; 1793 ms A17 começa a empurrar de baixo; o cartão sai pelo topo até ≈ 2377 ms.
- Parâmetros que dependem do conteúdo: a foto; a direção do empurrão (varia de cena a cena: esquerda, diagonal, baixo).
- O que NÃO fazer: repetir a mesma direção de empurrão em cenas seguidas (aqui: esquerda em A14, diagonal em A16, de baixo em A17); sombra entre cartões; parar a câmera depois do empurrão; borrar o cartão no empurrão (não há desfoque de movimento); copiar a vinheta de outra cena.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "foto de arquivo das pessoas que a fala agrupa" (o time, o grupo).
- Nesta referência as lacunas foram preenchidas com: foto P&B de artistas da unidade trabalhando ao ar livre.
- Receita de tratamento de cada imagem: foto real de época, P&B/sépia, horizontal, cartão com borda clara.
- Regra de escolha: "encheu a unidade de X" → foto documental de X em ação. Teste em 2 temas: Claude Code → foto do time de engenharia numa mesa; café → foto antiga de colhedores no cafezal.
- Receita de tratamento (reestudo 20/11): foto de arquivo P&B quente, clara, grão forte (σ ≈ 17), borda clara de ≈ 8 px.
- Teste de generalização: Claude Code → foto do time trabalhando num escritório, empurra pela diagonal o retrato anterior na frase "e ele montou um time de designers"; café → foto antiga de colhedores no campo empurra pela diagonal o retrato do fazendeiro.

- Confiança: tempos, curva e caixa = medido; direção diagonal do empurrão = observado no strip.
