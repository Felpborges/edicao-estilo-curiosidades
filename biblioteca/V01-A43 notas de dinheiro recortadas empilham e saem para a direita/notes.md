# V01-A43 · notas de dinheiro recortadas se empilham uma a uma e saem para a direita
- Categoria: P16 · Colagem de recortes (provisória do analista: (provisória) recortes de objeto empilhando (contagem visual), sem disco)
- Fonte: V01 quadros f3496–f3548 (145,67–147,83 s; 53 quadros ≈ 2208 ms) (conferido, f3548: o maço continua saindo, borrado, por trás do anúncio de V01-A44 até f3548; antes: f3496–f3541, 46 quadros) · 24 fps
- Fala: "But he didn't want the money."
- Tipo de fala: virada ("mas ele não queria o dinheiro")
- Gatilho: corte seco em f3496 = 145667 ms, −123 ms antes da palavra nº 485 "But" (145790 ms). Nota 3 em f3506 = 146083 ms, +63 ms depois da nº 486 "he" (146020 ms). Saída começa em f3532 = 147167 ms, +107 ms depois da nº 490 "money." (147060 ms) (conferido: o perfil mostra o 1º passo em f3531, 1 quadro antes).
- Quadro-chave: f3520
- Camadas ativas: cena de tela cheia | legenda | transição (saída)
- Leitura dos strips: strip.jpg = quadros f3494 a f3511, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 18 células. strip-saida.jpg = quadros f3530 a f3544, mesma regra, 15 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-nota-borda-sombra.jpg = quadro f3520, região x60 y600 170x110 px, ampliada 3× sem suavizar · detalhe-saida-f3538.jpg = quadro f3538, região x60 y280 660x440 px, ampliada 1× sem suavizar (meio da saída).


## LEITURA DE EDITOR
- Por que esta cena aqui: a frase é curta e tem um único objeto ("o dinheiro"); o editor mostra o objeto literal empilhando, e o tira da tela na palavra "dinheiro", como quem recusa.
- Por que este design: três recortes do objeto em leque sobre a mesa vazia, sem disco nem moldura: o objeto sozinho fala mais alto; o espaço vazio em volta é o "não".
- Por que estas cores: o objeto dessaturado, com um único detalhe na cor original (azul), sobre a mesa escura; nada mais compete.
- Por que estes efeitos: margem clara própria do objeto, grão fino preso ao recorte e sombra caída para baixo (alinhado ao reestudo): parece dinheiro de papel jogado na mesa.
- Por que este movimento: três batidas rápidas (uma a cada 4–6 quadros) e uma saída em cascata para a direita, acelerando e borrando: o dinheiro é "empurrado" para fora.
- Sensação do movimento: acúmulo rápido e rejeição; a saída é a recusa em gesto.

## FORMA (fixa: reproduzir igual)
- Design (med.py, quadro cheio):
  - Recorte 1: foto real do objeto citado, recortada justa, dessaturada com um detalhe na cor original, sem disco, direto no fundo escuro, levemente girada: f3498 x76–590, y308–577 = 515x270 px (71,5 % · 21,1 %), centro (45,6 %, 34,6 %).
  - Recortes 2 e 3: cada uma cai por cima, deslocada ≈ 50–70 px PARA BAIXO e com giro diferente, formando um leque/monte; conjunto final f3510 x72–621, y310–688 = 550x379 px. (medido)
  - Contorno: borda clara fina do próprio objeto + sombra caída para baixo (embaixo 15 px, lados 11–16 px, em cima quase nada) (alinhado ao reestudo) (sem adesivo grosso). (observado)
- Movimento:
  - Recorte 1: corte seco; f3496 539 px → f3498 515 (105 → 100 %). Estalo de 1 imagem. (medido)
  - Recorte 2: f3500 (conjunto 564x315) → f3502 552x320. (medido)
  - Recorte 3: f3506 (558x391) → f3508 548x381 → f3510 550x379. Ritmo de empilhar: um recorte a cada 4–6 q (167–250 ms). (medido)
  - Saída: o monte desliza para a DIREITA com borrão, em cascata de trás para a frente (corrigido no reestudo, f3538: os recortes de trás já andaram ≈ 50 e ≈ 230 px enquanto o da frente ainda está no lugar; antes "o monte" como bloco): borda esquerda f3530 x67 → f3534 x73 → f3538 x103 → f3540 x133 (acelera), enquanto o anúncio de V01-A44 cai por cima em f3541; o monte segue visível, borrado, na faixa direita por trás do anúncio até f3548 e some em f3549. (medido; conferido, f3548)
  - Cadência 12 imagens/s (fase par). (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | recorte 1 | f3496 | 2 q (83 ms) | escala 105 → 100 % | estalo | nº 485 | −123 ms |
  | recorte 2 | f3500 | 2–4 q | cai deslocada | estalo | nº 485 | +44 ms |
  | recorte 3 | f3506 | 4 q | cai deslocada | estalo | nº 486 | +63 ms |
  | monte sai para a direita | f3532 | ≈ 17 q (708 ms) até f3548 (conferido; antes ≈ 10 q) | deslize com borrão | acelera (ease-in) | nº 490 | +107 ms |
- Ritmo: monte completo, sem peça nova, aproximando +2,6 → +2,0 %/s, de f3510 a f3530 (833 ms) (alinhado ao reestudo). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)
- Textura (reestudo 20/11):
  - Mesa (medida limpa, f3520, grande área vazia): #151112, luma 18,1, grão 0,31, manchas 0,44, ac1 +0,55; PARADA (correlação +0,89 / +0,90 entre f3520 e f3524). Mapa de luz (mediana por faixa de 160 px, esq/meio/dir): y0–160 21,4/23,9/21,9 · y160–320 31,9/36,6/30,9 · y320–480 35,6/41,3/36,6 · y480–640 34,9/43,5/35,6 · y640–800 29,9/33,9/30,9 · y800–960 22,9/23,9/22,9 · y960–1120 18,9/20,5/18,9 · y1120–1280 14,5/14,5/14,5. Pico do foco em y≈400–600 (≈ 35–45 % da altura), centro 5–8 níveis acima dos lados.
  - Objeto recortado: gravura impressa dessaturada (cinza puro, 22,3 nos 3 canais, ac1 alto = traço de gravura) com um detalhe na cor original (azul); anda rígido (+0,93 depois de alinhar). Teste novo (f3520×f3522, afim do monte, pixels lisos de luma > 200): claros resíduo/σ 0,80–0,82, correlação +0,63…+0,65; escuros 0,55–0,57, +0,82 → PARADO: sem grão vivo medível nas margens claras (mesmo veredito). Margem branca própria do objeto (sem adesivo).
- Efeitos (reestudo 20/11):
  - Sombra do objeto na mesa (coluna x330, f3520): logo abaixo da borda 25,6 → 36,6 em ≈ 18 px (≈ −30 %), difusa. Nos 4 lados (medido, f3520, perfil alinhado no monte): embaixo −48 % no contato, volta em 15 px; à esquerda −39 %, 11 px; à direita −31 %, 16 px; em cima −9 %, 5 px (só 7 linhas, baixa confiança). Caída para baixo (corrigido na conferência: era ≈ −30 % só embaixo).
  - Vinheta global: o foco de luz da mesa (anéis do quadro inteiro f3520: 107 → 90 → 46 → 27 → 21, com o objeto no centro).
  - Desfoque de movimento: sim, horizontal, na saída (f3538: as notas que já andam estão borradas na proporção da velocidade).
  - Grão fino por cima do objeto (detalhe), que anda com o recorte: o teste novo não acha grão vivo aqui (ver Textura) (corrigido na conferência: a CONSTRUÇÃO dizia "grão de cartão vivo"). Aberração, brilho: nenhum.
- Câmera (reestudo 20/11): o monte APROXIMA enquanto empilha (medido, região 60,300,600,400, sem a faixa da legenda): f3510 → f3522 ×1,0128 (+2,6 %/s), centro (−0,97, +0,22 px/q); f3520 → f3530 ×1,0084 (+2,0 %/s), centro (−0,44, +0,37 px/q): aproxima e freia até a saída em f3532 (corrigido na conferência: era "parada enquanto empilha"). Mesa parada (diferença ≤ 0,05).
- Cadência (reestudo 20/11): 12 imagens/s (perfil região do monte f3527–f3542: 25,8 / 0,26 / 24,8 / 0,08 / 34,9 / 0,38 / 38,6 / 0,05 / 39,4 / 0,24 / 41,5 / 0,01 / 42,6 / 0,04 / 92,4 (anúncio cai) / 0,00): a saída acelera devagar.
- Legenda nesta cena (reestudo 20/11): 2 blocos (o 1º, 3 palavras, no quadro do corte; o 2º, 3 palavras com o objeto citado, f3519–f3539) e o 1º bloco da cena seguinte entra em f3540, 1 quadro antes do anúncio cair. Texto #eade53, 68 %. Atrás da tarja: a mesa (o monte termina em y≈688). Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #151112 com foco de luz (pico ≈ 40 em y≈400–600 no centro; 21–24 no topo; 14,5 no rodapé), parada.
2. sombra de cada objeto: caída para baixo: embaixo −48 % no contato, some em 15 px; lados −31 a −39 %, 11–16 px; em cima quase nada (corrigido na conferência: era difusa ≈ 18 px, −30 %).
3. recorte 1: objeto real dessaturado (um detalhe na cor original), margem clara própria, leve giro; x76–590, y308–577 em f3498 (71,5 % × 21,1 %); entra no corte a 105 % → 100 % em 2 quadros.
4. recortes 2 e 3: caem por cima, cada um ≈ 50–70 px mais baixo e com giro diferente (leque); conjunto final x72–621, y310–688.
5. grão fino por cima de cada recorte, preso ao recorte (não sortear de novo a cada imagem: o teste novo não acha grão vivo aqui) (corrigido na conferência: era "grão de cartão vivo").
6. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Animação: recortes em 0, 167 e 417 ms, cada um com estalo de 2–4 quadros; o monte aproxima +2,6 → +2,0 %/s até a saída. Saída em cascata a partir de 1500 ms: os recortes de TRÁS saem primeiro (o de cima da pilha visual, depois o do meio) e o da frente por último, todos para a DIREITA, acelerando (diferença 25 → 43 por imagem) com borrão horizontal proporcional à velocidade; o anúncio de V01-A44 cai por cima em 1875 ms e o resto do monte some, borrado, até 2208 ms. Passos de 2 quadros.
- Linha do tempo (ms a partir do corte f3496 = 145667 ms): 0 recorte 1 + legenda · 167 ms recorte 2 · 417 ms recorte 3 · 583–1500 ms monte completo, aproximando (alinhado ao reestudo) · 958 ms 2º bloco de legenda · 1500 ms saída começa · 1833 ms legenda seguinte · 1875 ms anúncio cai por cima · 2208 ms último resto some.
- Parâmetros que dependem do conteúdo: o objeto (o que a fala nomeia), o detalhe que fica colorido, quantos recortes.
- O que NÃO fazer: pôr disco ou adesivo grosso (aqui o objeto fica solto na mesa), saída em bloco sem cascata, saída sem borrão, saída com velocidade constante, monte parado (ele aproxima).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o objeto que simboliza o que foi recusado/ganho": 3 recortes iguais do mesmo tipo de objeto, de valores ou ângulos diferentes.
- Nesta referência as lacunas foram preenchidas com: 3 cédulas antigas de dólar (10, 5, 1).
- Receita de tratamento de cada imagem: foto real do objeto, recortada justa (sem adesivo grosso), cor original dessaturada, cada cópia girada diferente.
- Regra de escolha: palavra abstrata de valor ("o dinheiro") → objeto literal que a representa, multiplicado (empilhar = "muito"); quando a fala nega ("não quis"), o maço sai da tela.
- Teste de generalização: (1) Claude Code: "mas ele não quis cobrar pela ferramenta" → 3 recortes de cartões de crédito empilhando e saindo. (2) café: "mas ele não quis a patente" → 3 recortes de selos/carimbos de patente empilhando e saindo.
- Receita de tratamento (reestudo 20/11): foto real do objeto recortada justa, dessaturada para cinza puro com UM detalhe deixado na cor original, margem clara própria, grão fino preso ao recorte (sem grão vivo), sombra caída para baixo (embaixo −48 % em 15 px, lados −31 a −39 % em 11–16 px, em cima quase nada) (alinhado ao reestudo); leque de 3 cópias com giros diferentes.
- Teste de generalização (reestudo 20/11): (1) Claude Code: "mas ele não quis cobrar pela ferramenta" → 3 recortes de cartões de crédito/notas empilhando e saindo para a direita. (2) café: "mas ele não quis vender a receita" → 3 recortes de cheques antigos dessaturados, assinatura em azul, empilhando e saindo.

- Confiança: caixas e tempos medido; contorno e direção observado.
