# V01-A32 · duas fotos macro do material; a 2ª cai por cima e leva um zoom forte
- Categoria: P08 · Pilha de cartões (provisória do analista: (provisória) foto impressa com borda de papel + punch-in animado na foto)
- Fonte: V01 quadros f2246–f2346 (93,58–97,75 s; 101 quadros ≈ 4208 ms) · 24 fps
- Fala: "The warmth comes from the material. He built his suit out of foam neoprene,"
- Tipo de fala: virada (a explicação verdadeira começa: "o calor vem do material") + descrição
- Gatilho: corte seco em f2246 = 93583 ms, −117 ms antes da palavra nº 303 "The" (93700 ms). Foto 2 em f2292 = 95500 ms, −60 ms antes da nº 309 "He" (95560 ms). Zoom começa em f2300 = 95833 ms, −187 ms antes da nº 312 "suit" (96020 ms).
- Quadro-chave: f2330
- Camadas ativas: cena de tela cheia | legenda | b-roll (fotos)
- Leitura dos strips: strip.jpg = quadros f2244 a f2253, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 10 células. strip-saida.jpg = quadros f2290 a f2318 (foto 2 e o zoom), mesma regra, 29 células. strip-geral.jpg = quadros f2244 a f2346, de 3 em 3, 35 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-canto-borda-sombra.jpg = quadro f2330, região x0 y700 140x150 px, ampliada 3× sem suavizar · detalhe-foto-macro.jpg = quadro f2330, região x200 y300 200x150 px, ampliada 2× sem suavizar.


## LEITURA DE EDITOR
- Por que esta cena aqui: depois de derrubar a crença, a fala aponta o verdadeiro responsável, "o material"; o editor mostra o material de verdade, em foto macro colorida, antes de abrir o diagrama.
- Por que este design: duas fotos macro empilhadas (a 2ª cai por cima e é maior) e um zoom forte na 2ª: do objeto para a estrutura, preparando a lupa da cena seguinte.
- Por que estas cores: foto colorida real (preto profundo do material, fio laranja, forro rosado) depois de muitos diagramas: a mudança de linguagem marca "agora é o real".
- Por que estes efeitos: a mesma borda de papel e sombra caída para baixo das outras fotos (alinhado ao reestudo); a foto tem o próprio desfoque de macro (profundidade da lente), nada aplicado.
- Por que este movimento: estalo nas duas fotos (cada uma no começo da sua frase) e um zoom com aceleração e freada fortes (até +192 %/s no meio) que "mergulha" no material justamente quando a fala nomeia o material.
- Sensação do movimento: impacto, impacto, mergulho; o zoom em ease-in-out de 833 ms é o movimento mais rápido e mais suave da cena, e dá a sensação de entrar dentro da coisa.

## FORMA (fixa: reproduzir igual)
- Design (med.py, quadro cheio):
  - Foto 1 horizontal larga (macro colorido de um corte de material, fundo claro): assentada f2250 x38–682, y288–645 = 645x358 px (89,6 % da largura, 28,0 % da altura), centro (50,0 %, 36,5 %), borda de papel, giro ≈ 2° (observado).
  - Foto 2 (macro do material em corte com um elemento de escala ao lado), cai por cima e fica maior: assentada f2296 x18–711, y240–703 = 694x464 px (96,4 % · 36,3 %); depois do zoom ocupa f2316 a tela inteira na largura e y43–827 (61 % da altura), quase sem borda visível. (medido)
- Movimento:
  - Foto 1: corte seco; largura f2246 716 (111 %) → f2248 666 (103 %) → f2250 645 (100 %). Estalo de 4 q até o 1º quadro assentado (remedido, f2246–f2250). (medido)
  - Foto 2: entra em f2292 maior (altura 531, 114 %) → f2294 482 (104 %) → f2296 464 (100 %). Estalo de 4 q (remedido, f2292–f2296). (medido)
  - Zoom na foto 2: altura f2300 485 → f2304 545 → f2308 669 → f2312 752 → f2316 785 → (f2344 818): aumentos por 4 q de 60, 124, 83, 33 px = acelera e desacelera (ease-in-out), ≈ 1,7×, centrado. Pelo perfil da região, o zoom começa em f2300, tem o pico de velocidade em f2308 e só para em f2320 (f2318 ainda 7,7; f2320 3,7 = deriva): 20 q (833 ms) (remedido, perfil f2296–f2350; antes 16 q / 667 ms). (medido)
  - Saída: a lupa de V01-A33 nasce em cima da foto 2 em f2346. (medido)
  - Cadência 12 imagens/s. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | foto 1 | f2246 | 4 q (167 ms) (remedido) | escala 111 → 100 % | estalo | nº 303 | −117 ms |
  | foto 2 por cima | f2292 | 4 q (167 ms) (remedido) | escala 114 → 100 % | estalo | nº 309 | −60 ms |
  | zoom na foto 2 | f2300 | 20 q (833 ms) (remedido, para em f2320) | escala 1 → 1,7× | ease-in-out | nº 312 | −187 ms |
- Ritmo: foto 1 46 q (1917 ms); foto 2 54 q (2250 ms), derivando +3,2 %/s depois do zoom (alinhado ao reestudo), de f2320 a f2345 (1083 ms) (remedido). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Fotos: fotografia colorida macro com desfoque de lente próprio. f2330 região 420,120,180,120 (fundo escuro da foto 2): #040104, luma 1,5, grão 0,20, manchas 0,33: pretos esmagados e lisos, PARADOS (correlação +0,74). O grão visível nos escuros está no próprio material fotografado (detalhe). Mas os CLAROS são VIVOS (medido, teste novo, foto 1 em f2270×f2272, afim da foto, pixels lisos: claros da foto, região 480,320,180,120, resíduo/σ 1,48, correlação +0,05; escuros 0,59, correlação +0,84; foto 2 depois do zoom, f2330×f2332: claros 1,12, correlação +0,41, escuros 0,44, +0,91): grão novo a cada imagem só onde a foto é clara (corrigido na conferência: era "PARADA" para a foto inteira, medida só nos pretos).
  - Borda de papel: off-white #e5e0d8–#e9e4d8 com fibra (detalhe), ≈ 13 px depois do zoom (y809–822 em f2330; ≈ 8 px antes do zoom × 1,7) e ≈ 11 px à esquerda (x0–10). Grão VIVO (medido, f2270×f2272, faixa da borda de baixo 30,600,660,80, luma > 200: resíduo/σ 1,47, correlação +0,05).
  - Mesa: a de sempre, parada (diferença ≤ 0,11 por quadro na faixa y960–1260 durante o zoom).
- Efeitos (reestudo 20/11):
  - Sombra da foto (f2330): embaixo fio escuro de 1–2 px (L35 → 14,6) e volta a 23 em ≈ 20 px; à esquerda 62 → 28,8 e volta a 34–35 em ≈ 5 px. Nos 4 lados (medido, foto 1 em f2270, perfil alinhado e linhas y420–520): embaixo −52 % no contato, volta ao fundo em 18 px; esquerda −25 % e direita −24 %, voltam em 13–14 px; em cima −16 % só no 1º px, volta em 7 px. Sombra CAÍDA para baixo: longa embaixo, média dos lados, quase nada em cima (corrigido na conferência: era "sombra curta, mais longa embaixo", sem os lados).
  - Vinheta: nenhuma aplicada (a foto escurece por conteúdo). Borda borrada: nenhuma; o desfoque é da lente da foto (fundo do macro).
  - Desfoque de movimento no zoom: nenhum visível (o zoom não arrasta a imagem).
  - Brilho, aberração: nenhum. Grão global: nenhum aplicado no quadro (mesa parada); o grão vivo mora nos claros das fotos e da borda de papel (corrigido na conferência: era "nenhum").
- Câmera (reestudo 20/11): a câmera é a FOTO. Foto 1: f2252 → f2270 escala ×1,0170 (+2,3 %/s), centro (+0,05, +0,11 px/q). Zoom da foto 2 por trechos de 4 quadros: f2300 → f2304 +3,0 %/q (centro +8,2, −2,6 px/q); f2306 → f2310 +4,6 %/q (+16,3, −4,4 px/q, pico); f2316 → f2320 +0,29 %/q (+1,1, −0,25 px/q); depois f2322 → f2340 +3,2 %/s (+0,48, −0,39 px/q). Fim da cena (medido, f2332 → f2344, região 0,0,720,830): ×1,0159 (+3,2 %/s), centro (+0,48, −0,41 px/q): a mesma deriva até a lupa nascer, sem recuo. O ponto de mira do zoom fica à direita e acima do centro (a imagem anda para a direita e para cima enquanto cresce). Mesa parada.
- Cadência (reestudo 20/11): 12 imagens/s também no zoom forte (perfil f2297–f2322: 0,07 / 9,4 / 0,01 / 12,4 / 0,01 / 15,8 / 0,01 / 19,7 / 0,01 / 25,5 / 0,01 / 27,7 / 0,01 / 24,0 / 0,01 / 19,1 / 0,01 / 15,3 / 0,00 / 10,7 / 0,07 / 7,1 / 0,07 / 3,4): curva em sino, pico em f2308.
- Legenda nesta cena (reestudo 20/11): 5 blocos (3, 3, 4, 3, 1 palavras): o 1º entra no quadro do corte (f2246); o 3º (4 palavras: a pessoa e o que ela construiu) entra em f2293, 1 quadro DEPOIS da foto 2 (f2292); o bloco de 1 palavra (o nome do material; f2327–f2344) termina 1 quadro antes da lupa; o seguinte (3 palavras, f2345) atravessa a entrada da lupa (f2346). Texto #e9de53–#eade54, 68 %. Atrás da tarja: a mesa (a foto 2 depois do zoom vai até y827, 20 px acima da tarja). Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %, estimativa grosseira). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #181516 com foco de luz largo, parada.
2. foto 1: macro colorida horizontal com borda de papel off-white ≈ 8 px, grão vivo nos claros (ruído ≈ 3 níveis sorteado de novo a cada imagem na foto clara e na borda; pretos lisos e parados), sombra caída para baixo (embaixo −52 % no contato, some em 18 px; lados −25 %, 13–14 px; em cima só 1 px), giro ≈ 2°; assentada em x38–682, y288–645 (89,6 % × 28,0 %). Entra no corte a 111 % → 103 % → 100 % (167 ms) e deriva +2,3 %/s.
3. foto 2 (por cima): macro do material em corte, maior: assentada x18–711, y240–703 (96,4 % × 36,3 %). Entra a 114 % → 104 % → 100 % (167 ms). Zoom de 100 % a ≈ 170 % em 833 ms com ease-in-out forte (pico ≈ +4,6 % por quadro no meio), mirando um ponto à direita e acima do centro; depois deriva +3,2 %/s. A borda de papel escala junto (≈ 13 px no fim) e a foto sangra pela direita e por cima.
4. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Linha do tempo (ms a partir do corte f2246 = 93583 ms): 0 foto 1 + legenda · 167 ms assentada · 1917 ms foto 2 cai por cima · 1958 ms bloco de legenda da pessoa e do que ela construiu · 2083 ms assentada · 2250 ms zoom começa · 2500 ms pico · 3083 ms zoom termina · 3083–4167 ms deriva · 4167 ms a lupa (V01-A33) nasce por cima.
- Parâmetros que dependem do conteúdo: o ponto de mira do zoom (onde está a estrutura que a próxima lupa vai abrir), a proporção das fotos.
- O que NÃO fazer: zoom linear ou com ease só no fim (é sino: acelera e freia), zoom a 24 imagens/s, cortar a foto 1 antes da 2 cair, perder a borda de papel no zoom (ela escala junto), clarear os pretos da foto, congelar o grão dos claros, sombra simétrica em volta.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o material da solução, de perto" (2 fotos macro: uma geral, uma com escala/medida).
- Nesta referência as lacunas foram preenchidas com: corte de neoprene vermelho/preto; corte de neoprene com régua ao lado.
- Receita de tratamento de cada imagem: fotos macro reais em cor, luz de estúdio, fundo claro ou escuro neutro, horizontais, borda de papel; a 2ª com elemento de escala (régua) para dar tamanho.
- Regra de escolha: "o segredo está no material" → mostra o material real de perto; o zoom aproxima no ponto que a próxima frase vai abrir (a lupa).
- Teste de generalização: (1) Claude Code: "o segredo está no arquivo de instruções" → print do arquivo inteiro; 2º print com o trecho e números de linha, zoom no trecho. (2) café: "o segredo está na moagem" → foto macro do pó; 2ª com régua de micras, zoom nos grãos.
- Receita de tratamento (reestudo 20/11): foto macro COLORIDA real, sem dessaturar, com pretos esmagados (luma ≈ 1–2) e desfoque de lente próprio; sem vinheta; grão vivo nos claros da foto e da borda, pretos parados (alinhado ao reestudo); borda de papel off-white ≈ 8 px com fibra, sombra caída para baixo: embaixo −52 % em 18 px, lados 13–14 px, em cima 1 px (alinhado ao reestudo).
- Teste de generalização (reestudo 20/11): (1) Claude Code: "o segredo está no arquivo de instruções" → foto 1 de um terminal aberto, foto 2 (por cima) da tela com o arquivo de instruções, zoom forte numa linha dele. (2) café: "o sabor vem da torra" → foto 1 do saco de café, foto 2 macro de grãos torrados, zoom forte na superfície oleosa de um grão.

- Confiança: caixas, escalas e tempos medido; giro da foto 1 observado.
