# V05-A02 · transição: a cor some (dessaturação para sépia)
- Categoria: P23 · B-roll 3D com cor seletiva (provisória do analista: (provisória) transição de cor dentro do mesmo plano (dessaturar para sépia))
- Fonte: V05 quadros f158–f164 (6,59–6,84 s; 7 quadros ≈ 292 ms) · pasta com folga f156–f168 · 23,976 fps
- Fala: "Now try to find purple."
- Tipo de fala: comparação (comando que vira jogo: procurar o que não existe)
- Gatilho: começa em f158 (6590 ms), 70 ms antes do início da palavra nº 26 "purple." (6660 ms); a cor zera em f164, 180 ms depois do início de "purple". Conferido com a saturação medida quadro a quadro (`med.py sat`) e com a legenda "to find purple." que entra em f150–f152.
- Quadro-chave: f166
- Camadas ativas: b-roll (continua V05-A01) | legenda | transição
- Leitura dos strips: strip.jpg = quadros f154 a f170, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 17 células. detalhe-sepia-realce.jpg = quadro f166, região x260 y480 180x180 px, ampliada 2× sem suavizar, contraste ×6 em volta da média (o realce estica a tinta e a faz parecer azulada: leia só a estrutura). detalhe-meio-da-transicao.jpg = quadro f161, região x260 y480 180x180 px, ampliada 2× sem suavizar (o meio da queda de cor: cinza-esverdeado com resto de cor).

## LEITURA DE EDITOR
- Por que esta cena aqui: na palavra do assunto procurado, o mundo perde a cor; é a virada do gancho para o "jogo" e a regra visual de todo o bloco seguinte (só o que importa tem cor).
- Por que este design: não troca a imagem nem corta; muda só a cor do mesmo plano em movimento, para o espectador sentir que a cor foi "tirada" do mundo que ele acabou de ver.
- Por que estas cores: sépia quente (R > G > B, ≈ 19 níveis entre canais), não cinza neutro: lê como "arquivo, passado", combina com a história antiga e deixa espaço para o roxo saltar depois.
- Por que estes efeitos: a vinheta continua igual (centro 100 %, borda 12 %); nada mais muda, para a troca de cor ser o único evento.
- Por que este movimento: queda de saturação lento-rápido-lento em 7 q, junto de um pequeno empurrão de câmera (+10 % em ≈ 12 q) que marca a virada sem corte.
- Sensação do movimento: "a cor escorre" num piscar (292 ms) enquanto a câmera dá um passo à frente; produzida pela curva de saturação com miolo de −0,11/q e pelo pico de zoom de +1,6 %/q exatamente no miolo da queda.

## FORMA (fixa: reproduzir igual)
- Design: o mesmo plano em movimento continua; o que muda é só a cor. Depois da transição a imagem fica monocromática em sépia quente: claro #dcc4aa (f166, x360 y560) · meio-tom #c5af99 (f166, x250 y640) · cantos #09090a (f166, x0 y0) (medido, 1 pixel por amostra). Média de área (remedição, f166): centro x330–390 × y530–590 #b29e8c, meio-tom x220–280 × y610–670 #918272, canto x0–40 × y0–40 #0e0e0f; a tinta fica em R > G > B com ≈ 19 níveis entre canais (sépia quente). Luminância do centro quase igual antes e depois (≈ 165 a 185), então é dessaturação + tinta sépia, não escurecimento.
- Movimento (curva da saturação média do quadro, medido): f157 0,719 · f158 0,693 · f159 0,596 · f160 0,508 · f161 0,384 · f162 0,277 · f163 0,218 · f164 0,196 · f165+ 0,192 a 0,195 (estável). Curva lento-rápido-lento, com o miolo (f160–f162) caindo ≈ 0,11 por quadro; 7 quadros ≈ 292 ms. A câmera não para durante a transição (dif 7 a 8 por quadro) e dá um empurrão de ≈ ×1,10 com pico no miolo da queda (corrigido no reestudo, f156–f172; antes "igual à deriva").
- Ritmo: 5,3 s depois do corte para o b-roll; a sépia vale até f415 (A04–A07 todos em sépia com cor seletiva) e volta no fim do vídeo (V05-A53, f3938–f3947, 10 quadros, mesma curva).
- Som: nenhum efeito detectado (canal lateral em −120 dB de 6,0 a 7,5 s).
- Textura (reestudo 20/11):
  - Cartões em sépia: impressão lisa, igual à de A01 (a textura não muda com a cor). `textura` f166 região 260,480,200,160: cor média #998979, grão 10,6 (desenho das peças), manchas 25,8, ac1 +0,66 / ac2 +0,23 / ac4 0,00, grão B/G/R 10,3/10,6/10,7 (cinza: a tinta sépia não acrescenta grão colorido); no canto escuro (30,60,120,120) grão 3,96, manchas 13,3, ac1 +0,72 (o mesmo de A01: nenhum grão novo junto com a sépia). f166 × f168: anda com a câmera (alinhado −12,9 px, correlação +0,90). Detalhe: estrutura idêntica à de A01; no meio da transição (f161) a imagem passa por um cinza-esverdeado com resto de cor nas peças vermelhas.
- Efeitos (reestudo 20/11): vinheta global igual à de A01 (`borda` f166: 100 · 73 · 44 · 24 · 12 %; borda #100f10); nitidez cai com a luma (100 · 80 · 49 · 28 · 19 %), sem desfoque extra. Tinta sépia por igual em todo o quadro (claro #dcc4aa, meio #c5af99). Sem grão, sem brilho, sem borda borrada, sem aberração (medido em f166).
- Câmera (reestudo 20/11): durante a queda de cor há um empurrão curto que a 1ª passada não viu: f156→f160 ×1,009 (+0,23 %/q), f160→f164 ×1,065 (+1,59 %/q, pico; 391 de 600 pontos concordam), f164→f168 ×1,029 (+0,72 %/q), f166→f172 ×1,018 (+0,30 %/q). Total ≈ ×1,10 em ≈ 12 q, ease-in-out com o pico no miolo da dessaturação. O deslize lateral desacelera de 10,7 px/q (f148→f156) para 6,0 px/q (f166→f172); o centro sobe −4,4 px/q no pico. Corrigido no reestudo: "a câmera não para durante a transição (igual à deriva)" passa a "a câmera dá um empurrão de ≈ ×1,10 sincronizado com a queda de cor e a deriva freia" (f156–f172).
- Cadência (reestudo 20/11): 24 imagens/s (saturação muda em todos os quadros f158–f164; deriva sem quadros repetidos).
- Legenda nesta cena (reestudo 20/11): o bloco do assunto procurado (3 palavras, f152–f170) atravessa a transição inteira; a tarja não muda nada com a sépia (68 %, o valor do vídeo; o censo dava ≈ 64 % em f166, luma dentro 35 × fora 96; texto #efe716) (alinhado ao reestudo). Sem outro texto.

## CONSTRUÇÃO
1. fundo: o mesmo plano de A01 (imagem da coleção + câmera em deriva), sem corte.
2. filtro de cor sobre a camada 1 (abaixo da vinheta): saturação de 0,72 → 0,19 e tinta sépia (mapa de tons: preto #09090a, meio #c5af99, claro #dcc4aa; R > G > B ≈ 19 níveis). Curva da saturação por quadro a partir de f157: 0,719 · 0,693 · 0,596 · 0,508 · 0,384 · 0,277 · 0,218 · 0,196 · estável 0,19 (ease-in-out, 7 q = 292 ms).
3. vinheta global de A01, parada, sem mudança.
4. câmera: empurrão de ×1,00 → ×1,10 entre 0 e ≈ 500 ms (pico +1,6 %/q em ≈ 125–250 ms), enquanto o deslize lateral cai de 10,7 para 6 px/q; depois segue a deriva lenta de A03.
5. legenda por cima, sem troca no início da transição.
- Linha do tempo (ms a partir de f158, início da transição): −70 ms antes da palavra do assunto procurado · 0 começa a queda · 83–250 miolo (−0,11 de saturação por quadro) e pico do zoom · 250 cor zerada (180 ms depois do início da palavra) · ≈ 580 o zoom volta a ≈ 0,3 %/q · 667 entra o objeto de A03.
- Parâmetros que dependem do conteúdo: a palavra que dispara (o nome do que será procurado); a tinta pode variar se a paleta do vídeo pedir, mas a regra é "dessaturar para monocromático quente".
- O que NÃO fazer: não cortar para uma versão sépia (tem que ser contínuo, no mesmo movimento); não escurecer junto (a luma do centro fica ≈ igual); não usar cinza neutro; não fazer a queda linear nem longa (> 10 q); não deixar a câmera seguir a deriva sem o pequeno empurrão.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "a cor/qualidade que vai ser procurada e que NÃO existe" (o que some); "cena que já está na tela" (não muda).
- Nesta referência as lacunas foram preenchidas com: o mundo das bandeiras perde todas as cores na palavra "purple", preparando o jogo de achar o único roxo.
- Receita de tratamento de cada imagem: a mesma imagem do plano anterior, com saturação a ≈ 0,19 e tinta sépia (tons de #dcc4aa a #09090a); vinheta preservada; daqui em diante só o elemento procurado ganha cor (cor seletiva, ver A03–A06).
- Regra de escolha: comparação/ausência. Quando a fala pede para procurar uma coisa que quase não existe, tira-se a cor de tudo para que a coisa procurada, quando aparecer, seja a única cor da tela.

- Receita de tratamento de cada imagem (reestudo 20/11): a imagem anterior com saturação 0,19 e tinta sépia quente; vinheta e textura inalteradas; nenhum grão acrescentado.
- Teste de generalização: reel sobre Claude Code: "agora tente achar um app que faz isso sozinho" → a mesa de apps perde a cor na palavra "sozinho". Reel sobre café: "agora procure um café sem amargor" → a mesa de pacotes vira sépia na palavra "sem amargor".

- Confiança: curva de saturação medida; cores medidas; o papel narrativo ("preparar o jogo de achar") é inferido.
