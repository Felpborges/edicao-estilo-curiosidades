# V04-A35 · página de livro impressa em tela cheia + marca-texto amarelo que corre sobre a citação
- Categoria: P20 · Documento com marca-texto (provisória do analista: (provisória) documento/fonte com marca-texto (citação))
- Fonte: V04 quadros f2664–f2714 (111,11–113,24 s; 51 quadros ≈ 2127 ms) · 23,976 fps
- Fala: "We made that." So was he right?"
- Tipo de fala: citação (a frase exata da pessoa, mostrada na fonte impressa) + pergunta de virada
- Gatilho: corte seco em f2664 (111111 ms). A transcrição juntou "said," e "We" no token nº 374 'said,"We' (110580 ms); pela pausa da fala f2661,1–f2664,7 (silencios) o "We" começa ≈111140 ms, então a cena entra ≈ −30 ms antes do "We" (corrigido pelo envelope). Em relação à palavra nº 375 "made" (111380 ms): −269 ms. A legenda troca para "We made" em f2665.
- Quadro-chave: f2700
- Camadas ativas: legenda | cena de tela cheia | grafismo (marca-texto) | som (voz)
- Leitura dos strips: strip.jpg = quadros f2662 a f2687, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha (folha de trabalho recortada em x0 y330 720x180, 4 colunas; a da pasta é o quadro inteiro, 8 colunas); strip-geral.jpg = quadros f2662 a f2716, de 2 em 2, 8 colunas, da esquerda para a direita, linha a linha. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-marca-texto-crescendo.jpg = quadro f2670, região x380 y465 300x90 px, ampliada 3× sem suavizar (marca-texto no meio do crescimento: frente com borda macia, letras aparecendo por baixo); detalhe-marca-texto.jpg = quadro f2700, região x380 y465 300x90 px, ampliada 3× sem suavizar (marca-texto completo, escurecendo para a direita com a vinheta).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala é uma citação; mostrar a página impressa onde ela está escrita é a prova ("está no livro"), e o marca-texto aponta a frase enquanto ela é dita.
- Por que este design: a página ocupa a tela toda (sem cartão nem borda), texto serifado de livro real; só a frase citada é marcada, em 2 linhas, no terço de cima.
- Por que estas cores: papel creme quente #f1dab6 e tinta preta do livro; o amarelo do marca-texto é o mesmo "amarelo de atenção" da legenda, o que liga o que se ouve ao que se lê.
- Por que estes efeitos: vinheta da cena forte numa página clara (centro 194 → borda 37 de luma): a luz parece de luminária sobre o livro e o olho cai no meio, onde está a frase (alinhado ao reestudo).
- Por que este movimento: página quase parada (+2,7 %/s) para dar leitura; o marca-texto corre linear, na velocidade da fala, como uma mão marcando.
- Sensação do movimento: de estudo, de alguém sublinhando a prova ao vivo; produz isso o crescimento linear da esquerda para a direita, sem easing, e a câmera quieta.

## FORMA (fixa: reproduzir igual)
- Design:
  - Página de livro real (texto serifado preto em papel creme #fceac6, f2700 mediana dos claros em x100 y600 500x200) ocupando a tela toda: bloco claro x0 y100 720x1100 (100 % x 85,9 %, centro (50,0 %, 50,8 %)) em f2670 (medido); cabeçalho do livro visível no topo; vinheta escura nos cantos de cima (#020202) (medido).
  - Marca-texto: faixa amarela #ecc039 (f2700, mediana dos pixels amarelos em x0 y300 720x250) de altura ≈ 25 px (2,0 %), cobrindo a frase citada em 2 linhas; linha 1 em f2700 = x392–657 × y479–502 (265 px = 36,8 % da largura) e linha 2 = x≈60–107 × y520–543 (remedido, f2700, perfil de cor ao longo da linha: a cor escurece para a direita com a vinheta, de #ecc0.. a #8a7115, e a tolerância antiga cortava a ponta em x607). Bordas da faixa levemente irregulares (observado).
  - A legenda amarela (com caixa escura) fica sobre o texto do livro, em y≈856 (medido).
- Movimento:
  - Entrada: corte seco f2664 (dif 83,7) (medido). A página quase parada (zoom leve: ×1,053 de f2666 a f2712 ≈ +2,7 %/s, registro de pontos) (remedido).
  - Marca-texto: cresce da esquerda para a direita, velocidade constante; linha 1 de f2664 a ≈f2676 (≈13 quadros ≈ 540 ms) e linha 2 em f2677–f2682 (6 quadros ≈ 250 ms; 1º amarelo em f2677, completa em f2682) (remedido, perfil da linha 2 e folha ampliada f2674–f2685).
  - Saída: corte seco f2714→f2715 (dif 87,2) para o A-roll (medido).
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| marca-texto na linha 1 | f2664 | ≈13 quadros (540 ms) | revelação da esquerda para a direita (wipe) | linear | nº 375, 2ª palavra da citação (111380 ms) | −269 ms (≈ −30 ms da 1ª palavra real da citação) |
| marca-texto na linha 2 | f2677 (remedido) | 6 quadros (250 ms) | wipe | linear | nº 376, a palavra que fecha a citação (111800 ms) | f2677 = 111653 ms → −147 ms |

- Ritmo: citação toda marcada e parada f2683–f2714 ≈ 1,3 s (remedido) (inclui a pergunta de virada).
- Som: pausa f2687,9–f2690,8 com piso −66,9 dB, sem efeito (medido).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Página (papel de livro escaneado/fotografado): #f1dab6 entre linhas, luma 220, grão 10,8 níveis (inclui resto de letras), manchas 4,3, ac1 +0,53, direção horizontal +0,78 × vertical +0,27 (as linhas de texto), grão cinza; anda com a câmera (f2700×f2708 +0,62 depois de alinhar +1,9 px) (f2700, x300 y600 300x14). Média da área com texto #b9a288, grão 31 níveis (letras).
  - Tinta do livro: serifada preta-marrom, impressão real com leve irregularidade (detalhe).
  - Marca-texto: amarelo-ouro aplicado em modo multiplicar (as letras pretas aparecem por cima, sem perder contraste), ≈ #e8c040 no miolo claro, escurecendo com a vinheta até ≈ #8a7115 na ponta direita; bordas de cima e de baixo levemente irregulares, frente de crescimento macia (≈ 3–4 px) (detalhe-marca-texto-crescendo.jpg). Não tem textura própria: pega a do papel.
  - Fundo acima da página: liso, luma 13 → 8 (f2700, y60–90).
- Efeitos (reestudo 20/11):
  - Vinheta da cena (f2700): luma 100/80/59/37/19 %, nitidez 100/93/69/28/3 % (sobre papel claro a vinheta é a mais visível do vídeo) (alinhado ao reestudo).
  - Luz da cena (correção 20/11, f2700, medido): centro da poça em (50 %, 40 %) (ajuste sobre a página, σ 0,06, igual em f2670; a conferência achou o pico do perfil de uma linha em x ≈ 47 %, y ≈ 40 %); luma 249 no centro (40 px), a 100 px das bordas 63 % (esq) e 62 % (dir) do centro; a página cobre os pontos da mesa: 81 em (360,1060) e 53 em (360,1180) (razão 1,5). A luz é desta cena, por cima da página e do marca-texto; os anéis acima valem só aqui (não é um multiplicador fixo do vídeo).
  - Borda da página: sem borda de cartão; o papel termina reto no topo (y≈90) e cai de 93 para 13 em 3 px; sem sombra (fundo plano 13–8).
  - Fio, brilho, aberração, profundidade, desfoque de movimento, grão global: nenhum.
- Câmera (reestudo 20/11): aproximação lenta e centrada: f2666→f2680 ×1,016 (+2,7 %/s), 0,0/−0,1 px/q; f2695→f2712 ×1,019 (+2,7 %/s), 0,0/−0,1 px/q; giro 0 (linear, sem aceleração).
- Câmera em 3 pares (correção 20/11, medido, `camera` com região x12 y101 696x715: começo f2665→f2671 +2,0 %/s; meio f2686→f2692 +2,1 %/s; fim f2707→f2713 +1,9 %/s; deslize 0/−0,05 px/q. Fase única: aproximação linear (pares curtos dão +1,9 a +2,1 %/s; a nota dá +2,7 %/s de f2666 a f2712).
- Cadência (reestudo 20/11): 24 imagens/s (perfil x0 y460 720x100, f2665–f2684: 3,6–4,9 em todos os quadros; o marca-texto avança ≈ 22 px por quadro, todo quadro).
- Legenda nesta cena (reestudo 20/11): amarela #f0e618, altura 27 px; atrás da tarja o papel com texto (luma 130–139): é onde a tarja fica mais visível. Tarja preta a 59 % fixa no vídeo (medida direta aqui: 58–62 % em f2665, f2671 e f2676, papel de 115–148 a 2–6 px fora) (corrigido na conferência: era "censo 56 % (55–61 %); 62–66 % contra o papel acima"). 5 blocos: a aspa + 1ª palavra da citação vem do rosto e fica 1 quadro (f2664) · o começo da citação (2 palavras na tela, com a aspa) · o fim da citação com a aspa (1, 292 ms, o mais curto) · 3 (a pergunta de virada) · 1 (fim da pergunta). A tarja cobre linhas do livro: a legenda NÃO desvia da página.
- Entrada do texto (reestudo 20/11): o marca-texto é o "texto do editor" da cena: cresce da esquerda para a direita em velocidade constante (≈ 22 px/q ≈ 530 px/s) sobre a linha 1 (x392 → 657 em ≈ 12–13 quadros) e depois sobre a linha 2 (6 quadros); sem fade, sem escala; a frente é macia (3–4 px) e a cor entra cheia.

## CONSTRUÇÃO
1. fundo: tela fixa quase preta (só aparece acima da página, y0–90).
2. página: foto/scan de página de livro real em papel creme, tela cheia (x0–720 × y≈90–1200), sem borda e sem sombra; corte seco em 0 ms.
3. marca-texto: retângulo amarelo-ouro ≈ #e8c040, alt 25 px (2 % do quadro), em modo multiplicar sobre a linha citada, bordas superior/inferior levemente irregulares, frente macia 3–4 px. Linha 1: cresce linear de x392 a x657 de 0 a 540 ms; linha 2: cresce de x≈60 a x≈107 de 542 a 792 ms.
4. câmera sobre 2 + 3: aproximação linear +2,7 %/s, centrada, a cena toda.
5. luz da cena por cima de tudo (página e marca-texto; não é vinheta fixa do vídeo): poça centrada em (50 %, 40 %), luma 249 no centro, a 100 px das bordas 62–63 % do centro; anéis medidos com `borda` 100/80/59/37/19 % (f2700); a frase marcada fica perto do centro da luz (corrigido na conferência: era "vinheta da cena 100/80/59/37/19 %, centro ≈ 40 % da altura", lida como fixa do vídeo) (alinhado ao reestudo).
6. legenda L01 (aqui na variação L03, sobre papel claro).
- Linha do tempo (ms a partir de f2664): 0 corte seco e marca-texto começa (≈ −30 ms da 1ª palavra real da citação) · 42 legenda do começo da citação · 540 linha 1 completa · 542 linha 2 começa · 792 citação toda marcada · 793 legenda do fim da citação · 1084 a pergunta de virada · 1710 fim da pergunta · 2127 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: o documento (página real onde a citação está), quantas linhas a frase ocupa, a velocidade (a frase marcada termina quando a citação termina de ser dita).
- O que NÃO fazer: marca-texto opaco por cima das letras; crescer com easing; pôr a página em cartão com borda; recriar o texto digitado (tem que ser a página real); marcar mais do que a frase dita. Pôr uma vinheta fixa igual em todas as cenas: a luz é desta cena, com centro e força próprios, por cima de fundo e peças (correção 20/11).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "fonte escrita da citação" (página de livro, artigo, carta, post);
  - "trecho citado" (a frase que a fala lê, marcada).
- Nesta referência as lacunas foram preenchidas com: página de "The Autobiography of Alice B. Toklas"; a frase de Picasso "it is we that have created that".
- Receita de tratamento de cada imagem: foto/scan real da página, tela cheia, papel creme, luz forte desta cena (centro ≈ 50 %, 40 %; borda a 19 %) (alinhado ao reestudo); marca-texto amarelo-ouro desenhado por cima, com borda irregular de caneta.
- Regra de escolha: quando a fala CITA alguém, mostra a fonte real com o trecho sendo marcado no ritmo da leitura (prova + leitura). Teste em 2 temas: Claude Code → print da documentação oficial com a frase marcada; café → página de um livro de história do café com a frase marcada.

- Receita de tratamento (reestudo 20/11): página real fotografada/escaneada, papel creme quente #f1dab6, tinta preta, sem correção de cor, nitidez alta no centro; a vinheta da cena faz a "luz de leitura". Marca-texto: amarelo-ouro em multiplicar, 2 % da altura do quadro, bordas levemente irregulares (alinhado ao reestudo).
- Teste de generalização: Claude Code → print da documentação oficial em tela cheia com o marca-texto correndo sobre a frase citada pelo criador; café → página do diário de um mercador com a frase "isto é ouro" marcada enquanto é lida.

- Confiança: corte, cores e caixa = medido; quadros do wipe = observado quadro a quadro; correção do "We" = inferido pelo envelope.
