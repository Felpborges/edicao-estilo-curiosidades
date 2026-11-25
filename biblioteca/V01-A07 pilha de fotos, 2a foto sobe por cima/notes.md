# V01-A07 · pilha de fotos: foto vertical + 2ª foto que entra por cima na metade de baixo
- Categoria: P08 · Pilha de cartões (provisória do analista: (provisória) pilha de fotos impressas (montagem por empilhamento))
- Fonte: V01 quadros f255–f300 (10,62–12,50 s; 46 quadros ≈ 1917 ms) · 24 fps
- Fala: "freezing water for hours."
- Tipo de fala: exemplo (prova real da frase, em 2 imagens)
- Gatilho: corte em f255 = 10625 ms, +265 ms depois do início da palavra nº 36 "freezing" (10360 ms). 2ª foto em f281 = 11708 ms, −52 ms antes da palavra nº 39 "hours." (11760 ms).
- Quadro-chave: f290
- Camadas ativas: cena de tela cheia | legenda | b-roll (fotos)
- Leitura dos strips: strip.jpg = quadros f253 a f262, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 10 células. strip-saida.jpg = quadros f279 a f288 (entrada da 2ª foto), mesma regra, 10 células. Cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-pilha-bordas.jpg = quadro f290, região x0 y330 130x140 px, ampliada 3× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a frase termina na prova mais forte ("água quase congelando, por horas"); o editor dá duas imagens, uma para cada meia-frase, empilhadas, para a prova parecer abundante.
- Por que este design: pilha de fotos impressas (uma vertical grande + uma horizontal por cima, e outras 2 só pelas bordas atrás) = "álbum de evidências"; o volume da pilha diz "tem muito mais disso".
- Por que estas cores: o branco-azulado frio da neve e do mar (#7b92b2) puxa a sensação de frio; o editor não pinta nada, escolhe fotos frias.
- Por que estes efeitos: borda off-white com sombra caída para baixo em cada camada da pilha (alinhado ao reestudo), para se ler a profundidade entre as fotos.
- Por que este movimento: cada foto bate na pilha com estalo de 2 imagens; a foto de baixo sobe devagar para dar lugar à de cima, que entra subindo de baixo.
- Sensação do movimento: fotos jogadas uma sobre a outra na mesa, rápidas e físicas; produzida por 108 → 102 → 100 % em 2 imagens de 12/s, foto 2 com 104,7 % e deslocada, e a foto 1 subindo ≈ 1,9 px/q.

## FORMA (fixa: reproduzir igual)
- Design:
  - Foto 1 vertical (retrato) com borda de papel ≈ 7 px (topo y100–106 na coluna 360, f261), grande: caixa da pilha x12–712 · y91–831 = 701x741 px (97,4 % da largura, 57,9 % da altura) em f261; atrás dela aparecem bordas de outras 2–3 fotos (pilha), deslocadas para os lados (observado: tiras de foto à esquerda e à direita). Inclinação ≈ 0,8° horário. (medido com med.py/inc.py; pilha observado)
  - Foto 2 horizontal, entra por cima cobrindo a metade de baixo da foto 1, inclinada para o outro lado (a borda de cima mede −12° no detector em f287, influenciada pela foto de trás; inclinação real observado ≈ 2–3° anti-horário). Caixa do conjunto f287: x9–704, y63–826. (medido / observado)
- Movimento:
  - Foto 1: corte seco já maior e assenta em 2 imagens: altura da pilha f255 801 px (108 %) → f257 757 (102 %) → f259 741 (100 %). (medido)
  - Foto 2: entra em f281 maior (caixa do conjunto 720x783) e assenta em 2–3 imagens (f283 690x765, f285 693x759). Direção: sobe de baixo (observado no strip-saida). (medido / observado)
  - Fotos com vídeo dentro (diferença contínua). Cadência 12 imagens/s. (medido)
  - Saída: corte seco em f301 para V01-A08. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | foto 1 (vertical) | f255 | 4 q (167 ms) | escala 108 → 100 % | estalo | nº 36, a palavra do frio, no meio do bloco | +265 ms |
  | foto 2 (horizontal, por cima) | f281 | 4–6 q (167–250 ms) | sobe de baixo + escala | estalo | nº 39, a palavra do tempo, fim da frase | −52 ms |
- Ritmo: foto 1 sozinha 26 quadros (1083 ms); foto 2 por cima 20 quadros (833 ms). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- Textura (reestudo 20/11):
  - Fundo: a mesa de V01-A01.
  - Bordas de papel (todas as fotos da pilha): off-white #d7d7cc–#dad8cb, luma 214–220, 7 px (`sombra` f290 na borda de cima da foto 2: +15…+21), grão fino, canto vivo (detalhe-pilha-bordas).
  - Imagens: família foto de câmera, frias; `textura` f290 em 100,450,250,80 (foto 2): #7b92b2, grão 4,1, manchas 4,0, ac1 +0,67, grão cinza. Teste novo de grão (alinhado pela afim de cada foto, pixels lisos): foto 1 f271×f273 (região 100,120,500,600): resíduo ÷ σ 1,37 nos claros × 1,71 nos escuros, resíduo absoluto 1,4–1,7 níveis: sem excesso nos claros (o vídeo de dentro mexe tudo); foto 2 f293×f295 (60,420,600,380): 1,14 nos claros × 0,60 nos escuros, resíduo 1,55 × 0,88 → sinal fraco de grão vivo nos claros, de amplitude pequena (σ 1,4). Baixa confiança: as duas são vídeo. (medido) As fotos de trás da pilha são impressões inteiras com a própria borda, vistas só como tiras de 40–60 px nos lados.
- Efeitos (reestudo 20/11):
  - Sombra da foto 1 (`sombra` 4 lados alinhada, f271, caixa 60,76,584,720): CAI PARA BAIXO: embaixo, sobre a mesa, −51 % no 1º px fora e volta em 16 px; em cima −13 % só no 1º px (volta em 2); dos lados, sobre as fotos de trás, −22 % (esq) e −27 % (dir), voltam em 15–16 px. (medido; corrigido na conferência: era "sem deslocamento")
  - Sombra de uma foto sobre a outra (borda de cima da foto 2 sobre a foto 1, f290 x250–290): depois da borda, a foto 1 começa a luma 86 e sobe para 107 em ≈ 16 px: sombra suave de ≈ 16 px, −20 % no contato. Em f293 o topo da foto 2 cai sobre a parte escura da foto 1 (luma 2–17) e não dá para medir; embaixo encosta na tarja; dos lados a borda da foto de trás fica a 9–10 px, e só se vê a queda junto à borda (linhas y560–640: à direita 127 → 59, à esquerda 117 → 101), sem espaço para a sombra voltar ao fundo. (medido; o "sem deslocamento" antigo vinha só da borda de cima: corrigido na conferência)
  - Vinheta, borda borrada, brilho, desfoque de movimento, profundidade, grão global, aberração: nenhum (f290; a entrada da foto 2 em f281 é nítida no strip-saida).
- Câmera (reestudo 20/11): `camera` não serve aqui (os vídeos de dentro das fotos andam e contaminam a medida: f259→f279 deu ×0,9665 com giro −2°, incoerente com as bordas). Pelas bordas (coluna x360, limiar 60): pilha f255 770 px → f257 745 → f259 726 (assenta); f259 → f279 a foto 1 SOBE (topo y104 → y66, ≈ 1,9 px/q) e encolhe ≈ 1,8 % (726 → 713, ≈ −2 %/s) para abrir espaço; depois da foto 2 (f281) o conjunto desce e cresce de leve (base y809 em f285 → y839 em f299). Fim da cena, `camera` f289→f299 na região da foto 2 (0,380,720,440, sem a faixa da legenda): ×1,0241 (+5,9 %/s), anda (+4,4; +3,7) px/q, giro 0° (medido; pode ter um pouco do vídeo de dentro; a borda de baixo desce 2,1 px/q). Não para antes do corte. Fundo parado.
- Cadência (reestudo 20/11): 12 imagens/s nas fotos e nos vídeos de dentro (medida antiga; entradas em f255, f257, f259 e f281, f283, f285, todos ímpares).
- Legenda nesta cena (reestudo 20/11): 3 blocos: o de onde age (f239–f265, 4 palavras, vem da cena anterior e ATRAVESSA o corte f255 por 11 quadros, exceção à regra troca = corte), o de quanto tempo (f266–f299, 3 palavras; troca 15 quadros antes da foto 2) e a pergunta que abre a cena seguinte (f300, 3 palavras, entra 1 quadro antes do corte f301, a outra exceção). Atrás da tarja: a mesa escura; a base da pilha chega a y829–839, encostando no topo da tarja (y847); censo: 0,75 em 8 quadros em que a foto passa por trás; opacidade real da tarja preta pura 74 % (medida direta da conferência). Cor #e8dd54. Nenhum outro texto.

## CONSTRUÇÃO
1. fundo: mesa fixa.
2. fotos de trás da pilha (2): impressões com borda off-white, deslocadas ≈ 40–60 px para a esquerda e para a direita da foto 1, um pouco mais baixas, inclinadas ±1°; aparecem só pelas bordas; entram junto com a foto 1.
3. foto 1 (vertical): caixa da pilha x12–712 y91–831 em f261 (97,4 % × 57,9 %), borda 7 px, sombra caída para baixo (embaixo −51 %, some em 16 px; dos lados −22/−27 %, 15–16 px; em cima só 1 px), inclinação +0,8° (corrigido na conferência: era "sombra 16 px −20 % sem deslocamento"). Entrada no corte (0 ms): 108 % → 83 ms 102 % → 167 ms 100 %. De 167 a 1000 ms sobe ≈ 1,9 px/q e encolhe ≈ 2 %/s.
4. foto 2 (horizontal): entra em 1083 ms (f281) por cima da metade de baixo, inclinada para o lado oposto (≈ −2 a −3°), vinda de baixo, com ≈ 104,7 % (caixa do conjunto 720x783 → 690x765 → 693x759), assenta em 2–3 imagens (167–250 ms), depois desce e cresce de leve até o corte (+5,9 %/s no fim). Mesma borda e sombra; sobre a foto 1, a sombra da borda de cima é de 16 px a −20 %.
5. vídeos dentro das fotos: correm a 12/s.
- Linha do tempo (ms a partir do corte f255): 0 foto 1 108 % (legenda da cena anterior ainda na tela) · 167 assentada, começa a subir · 458 legenda de quanto tempo · 1083 foto 2 entra de baixo · 1250–1333 assentada · 1875 legenda da pergunta seguinte · 1917 corte seco.
- Parâmetros que dependem do conteúdo: quantas fotos (uma por meia-frase), orientação de cada uma (vertical para personagem, horizontal para lugar), lado da inclinação (alterna).
- O que NÃO fazer: pilha sem as bordas das fotos de trás (perde o volume); sombra preta forte ou simétrica em volta (cai para baixo: 16 px embaixo a −51 %, 15 px dos lados a −22/−27 %, nada em cima; entre fotos 16 px a −20 %; corrigido na conferência: era "não deslocar"); a foto 1 parada quando a 2 entra (ela sobe para abrir espaço); fotos com cor quente nesta frase de frio.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "imagem 1 da situação" (vertical, personagem em ação).
  - "imagem 2 que reforça a mesma ideia" (horizontal, plano mais aberto).
- Nesta referência as lacunas foram preenchidas com: surfista de roupa preta andando na neve com a prancha; surfista entrando no mar com montanhas nevadas.
- Receita de tratamento de cada imagem: fotos/vídeos reais, cor fria, impressos com borda de papel off-white ≈ 7–8 px e sombra caída para baixo; foto 1 vertical grande, foto 2 horizontal menor; leve giro oposto entre as duas; mais 2–3 fotos de "pilha" aparecendo só pelas bordas atrás. (reestudo 20/11) Medido: tons frios (#7b92b2), saturação baixa, contraste médio, grão da filmagem ≈ 4 níveis, sem vinheta; borda off-white 7 px luma ≈ 215; sombra entre fotos 16 px −20 %; sobre a mesa 16 px a −51 % embaixo.
- Regra de escolha: duas provas visuais da mesma frase, uma por meia-frase ("near freezing" → neve; "for hours" → no mar).
- Teste de generalização: (1) Claude Code: "devs passam horas no terminal" → foto vertical de alguém na mesa à noite + foto horizontal da tela cheia de código por cima. (2) café: "baristas acordam às 4h" → foto vertical do barista na rua escura + foto horizontal da máquina ligando.

- Confiança: escalas e tempos medido; direção da foto 2 e pilha de trás observado; inclinação da foto 2 observado (o detector mistura as fotos).
