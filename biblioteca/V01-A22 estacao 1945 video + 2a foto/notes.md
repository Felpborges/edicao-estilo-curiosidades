# V01-A22 · estação "1945" da linha do tempo: vídeo do evento + 2ª imagem por cima
- Categoria: P21 · Linha do tempo e dado em papel (provisória do analista: (provisória) estação de linha do tempo: foto(s) impressa(s) acima da régua de anos)
- Fonte: V01 quadros f1443–f1531 (60,13–63,79 s; 89 quadros ≈ 3708 ms) · 24 fps (remedido: 1º quadro nítido da foto nova, depois do borrão do chicote, é f1443, borda esquerda em x234)
- Fala: "1945, he watched the first atomic test in the New Mexico desert."
- Tipo de fala: data (o evento que a pessoa testemunhou naquele ano)
- Gatilho: a foto chega pela direita em f1443 = 60125 ms (remedido), +185 ms depois do início da palavra nº 190 "1945," (59940 ms) (chegada do chicote V01-A21). 2ª imagem em f1475 = 61458 ms, −42 ms antes da nº 195 "atomic" (61500 ms).
- Quadro-chave: f1500
- Camadas ativas: cena de tela cheia | grafismo (linha do tempo) | legenda | b-roll (vídeo)
- Leitura dos strips: strip.jpg = quadros f1471 a f1482 (entrada da 2ª imagem), de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 12 células. strip-geral.jpg = quadros f1443 a f1533, de 2 em 2, 46 células. Cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-filme-vinheta.jpg = quadro f1500, região x60 y230 200x180 px, ampliada 2× sem suavizar, contraste ×6 em volta da média.

## LEITURA DE EDITOR
- Por que esta cena aqui: 2ª estação da biografia; a fala nomeia um evento ("viu o primeiro teste"), e o editor mostra o próprio evento filmado, depois um 2º ângulo na palavra-chave.
- Por que este design: a mesma estação de V01-A20 (foto grande acima da régua, 2ª por cima), agora com filmagem em vez de documento: a repetição da forma deixa o conteúdo falar.
- Por que estas cores: P&B de filme antigo, com o clarão branco no centro e bordas escuras (vinheta da própria película).
- Por que estes efeitos: a vinheta forte e o grão vivo vêm do filme de época; o editor só acrescenta a borda de papel.
- Por que este movimento: chegada pelo chicote, 2ª imagem estala com giro oposto na palavra "atômico"; deriva lenta de recuo enquanto o filme corre.
- Sensação do movimento: testemunho de um momento histórico, contemplativo depois do impacto; produzida pela entrada 110 → 103 → 100 % em 3 imagens e recuo de −1,7 %/s.

## FORMA (fixa: reproduzir igual)
- Igual à estação de V01-A20 (conferido: foto horizontal ≈ 88 % da largura com borda de papel acima da régua, chegada por chicote, 2ª imagem cai por cima). Medidas próprias:
- Design (med.py, região acima da régua):
  - Foto 1 (vídeo P&B do evento): assentada f1451 x42–675, y228–712 = 634x485 px (88,1 % · 37,9 %), centro (50,0 %, 36,7 %).
  - Foto 2 (outro vídeo P&B do mesmo evento, mais aberto), mesmo tamanho, cai por cima com giro ≈ 2° oposto, um pouco deslocada (a foto 1 aparece por trás no alto e à esquerda): assentada f1479 x47–684, y232–721 = 638x490 px (88,6 % · 38,3 %), lado direito ≈ 10 px mais alto que o esquerdo (remedido, f1479; o x37–685 × y220–721 de antes era a caixa das duas fotos juntas).
- Movimento:
  - Foto 1: chega pela direita (V01-A21): borda esquerda f1443 x234 → f1445 x136 → f1447 x80 → f1449 x52 → f1451 x43 (assentada), 8 q desacelerando (remedido). Vídeo dentro anda (a ação filmada evolui). (medido)
  - Foto 2: entra em f1475 maior (716x566, 110 %) → f1477 668x514 (103 %) → f1479 assentada (100 %). Estalo de 2 imagens em movimento (2 q cada) e assenta na 3ª: 4 q da entrada ao assentado (remedido, f1475–f1479). (medido)
  - Saída: chicote para a esquerda em f1532 (V01-A23). (medido)
  - Cadência 12 imagens/s. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | vídeo 1 chega (chicote) | f1443 (remedido) | 8 q (333 ms) (remedido) | deslize da direita | ease-out | nº 190, a data | +185 ms |
  | vídeo 2 por cima | f1475 | 4 q (167 ms) (remedido, assenta f1479) | escala 110 → 100 % | estalo | nº 195, a palavra-chave do evento | −42 ms |
- Ritmo: vídeo 1 no topo 32 q (1333 ms) (remedido); vídeo 2 no topo 57 q (2375 ms). (medido)
- Som: nenhum efeito detectado (áudio mono; o evento filmado NÃO tem som próprio audível). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Mesa: a de V01-A01 (parada).
  - Filmagens: família grão de filme (P&B neutro), `textura` f1500 em 100,280,200,100 (filme 2, céu): #7a787b, grão 1,1, manchas 2,5, ac1 +0,61, cinza puro; VIVA (f1500×f1502 +0,03): o grão muda a cada imagem porque é filme correndo (detalhe-filme-vinheta com realce: manchas e grão de película). Teste novo (f1500×f1502, sem alinhar: a câmera anda só −0,14 % em 2 quadros; região 80,260,570,420, pixels lisos): claros resíduo 2,70 níveis (÷ σ 1,67) × escuros 0,55 (1,23) → VIVO e mais forte nos claros, confirmado (medido).
  - Bordas: off-white ≈ 7 px de canto vivo (como V01-A20).
- Efeitos (reestudo 20/11):
  - Vinheta da imagem (`borda` f1500 no filme 2): luma 100 / 79 / 59 / 49 % do centro para a borda (o anel externo, 57 %, já pega a borda de papel), nitidez 100 → 38 %: vinheta FORTE e borda macia, que são da própria película antiga (clarão no centro), não aplicadas pelo editor (inferido: o filme 1 tem outro desenho de luz).
  - Sombras CAEM PARA BAIXO (`sombra` alinhada): filme 1 sozinho (f1465, caixa 42,228,634,485): embaixo −53 % no 1º px fora, volta em 18 px; em cima −22 %, volta em 6 px (quase só o 1º px); filme 2 (f1500, caixa 47,232,638,490): embaixo −58 %, volta em 17 px; em cima −19 %, 1 px forte e volta em 10; lados encostam na borda do quadro (não medidos) (medido; corrigido na conferência: era "sombras de contato curtas entre as fotos"). Brilho aplicado, desfoque de movimento (fora do chicote), grão global sobre a tela, aberração: nenhum.
- Câmera (reestudo 20/11): recuo lento das fotos: `camera` na faixa de cima f1485→f1527 ×0,9702 (−1,7 %/s), desce 0,26 px/q; mesa e régua paradas.
- Cadência (reestudo 20/11): 12 imagens/s (`perfil` f1490–f1497: 0,33 / 2,66 / 0,27 / 2,51 / 0,05 / 2,07 / 0,48 / 2,12), inclusive o filme de dentro.
- Legenda nesta cena (reestudo 20/11): blocos: a data (até f1453, atravessa a chegada), sujeito + verbo (f1454–f1467, 2 palavras), o evento (f1468–f1489, 3 palavras; a 2ª imagem entra em f1475, no meio do bloco, na palavra-chave do evento), a última palavra repetida + o começo do lugar (f1490–f1506, 4 palavras), o fim do lugar (f1507–f1530, 2 palavras), a data seguinte (f1531, 1 quadro antes do chicote). Atrás da tarja: a mesa → tarja preta pura lida como preta (74 % no vídeo, medida direta da conferência); a régua acima com o ano 2 aceso.

## CONSTRUÇÃO
1. fundo: mesa fixa; régua (V01-A25) com o ano 2 aceso.
2. filme 1 (P&B do evento, correndo a 12/s): chega pelo chicote (V01-A21), borda esquerda x234 (0 ms = f1443) → x136 → x80 → x52 → x43 (333 ms, assentado); caixa x42–675 y228–712 (88,1 % × 37,9 %), borda off-white 7 px, sombra caída para baixo (18 px embaixo a −53 %, quase nada em cima); grão de película vivo, mais forte nos claros.
3. filme 2 (outro ângulo, mesmo tamanho): cai em 1333 ms (f1475) com 110 % e ≈ 2° de giro oposto → 103 % (1417 ms) → 100 % (1500 ms); deslocado deixando o filme 1 aparecer no alto e à esquerda; sombra caída para baixo (17 px embaixo a −58 %, 1 px forte em cima) (corrigido na conferência: era "sombra de contato curta").
4. deriva: recuo −1,7 %/s até o chicote de saída (3708 ms, f1532).
- Linha do tempo (ms a partir de f1443): 0 filme 1 chegando · 333 assentado · 458 legenda (sujeito + verbo) · 1042 legenda (o evento) · 1333 filme 2 · 1500 assentado · 1958 legenda (começo do lugar) · 2667 legenda (fim do lugar) · 3667 legenda (data seguinte) · 3708 chicote.
- Parâmetros que dependem do conteúdo: o evento e o 2º ângulo; foto ou filme.
- O que NÃO fazer: acrescentar vinheta ou grão por cima de imagens que não têm (a vinheta aqui é do filme); filme a 24/s; 2ª imagem sem giro oposto; sombra igual em volta (cai para baixo).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o evento da data": vídeo de época do acontecimento.
  - "o mesmo evento, outro ângulo": 2º vídeo/foto.
- Nesta referência as lacunas foram preenchidas com: dois filmes do teste Trinity (clarão e nuvem).
- Receita de tratamento de cada imagem: filme real P&B, granulado, horizontal, impresso com borda de papel, ≈ 88 % da largura, acima da régua. (reestudo 20/11) Medido: P&B neutro, grão de película vivo (muda a cada imagem), vinheta própria forte (bordas a ≈ 50 % da luma do centro) e bordas macias, contraste alto no clarão; reamostrado a 12/s; borda off-white 7 px.
- Regra de escolha: a data vem com o evento que a fala nomeia, em filmagem literal; o 2º ângulo entra na palavra-chave do evento ("atomic").
- Teste de generalização: (1) Claude Code: "em 2023, ele viu o primeiro agente rodar sozinho" → vídeo de tela do agente rodando; 2º vídeo do log correndo. (2) café: "em 1884, viu a 1ª máquina a vapor de café" → filme antigo da máquina soltando vapor; foto do balcão.

- Confiança: caixas, escalas e tempos medido; ausência de som de efeito medido pelo envelope.
