# V02-C00 · cortes secos entre rosto e cenas
- Categoria: P25 · Corte seco e apresentador em plano único (provisória do analista: (provisória) corte seco (sem transição, sem som) entre o A-roll único e as cenas de tela cheia)
- Fonte: V02, os 13 cortes do vídeo (tabela abaixo); clip e strips de exemplo em f86–f137 (3,59–5,71 s; 52 quadros ≈ 2169 ms) · 23,976 qps
- Fala: (exemplo) "platforms, and now I need your help. I"
- Gatilho: cada corte cai na fronteira de frase ou de oração, entre -46 e +56 ms do início da palavra que abre o novo plano (mediana -5 ms; tabela). Conferido no envelope em todos os cortes de entrada de cena (ver notes das pastas A).
- Quadro-chave: f100
- Camadas ativas: A-roll | transição (corte seco)
- Leitura dos strips:
  - strip.jpg: quadros f86 a f93, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 8 células; cada célula traz o nº do quadro e o tempo. (corte cena → rosto em f90)
  - strip-saida.jpg: quadros f130 a f137, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 8 células; cada célula traz o nº do quadro e o tempo. (corte rosto → cena em f134)
  - strip-geral.jpg: quadros f84 a f138, de 2 em 2, 8 colunas, da esquerda para a direita, linha a linha; 28 células; cada célula traz o nº do quadro e o tempo.

## FORMA (fixa: reproduzir igual)
- Design do A-roll (um único enquadramento no vídeo inteiro):
  - Plano: meio primeiro plano (do topo da cabeça à cintura/mãos), câmera fixa, frontal, à altura dos olhos. Topo do cabelo em y≈110 (8,6 %), olhos em y≈340 (26,6 %), queixo em y≈570 (44,5 %), ombros ocupando a largura toda; as mãos gesticulam na metade de baixo (y≈700–1100). Observado (vista 1:1 de f0).
  - Rosto (detector Haar, testa ao queixo, 21 medições em todos os trechos): largura 45,1–51,4 % do quadro (mediana ≈ 48 %), altura 25,4–28,9 %, centro x 43,2–50,0 % (mediana ≈ 48 %), centro y 28,3–32,6 % (mediana ≈ 30,7 %). A variação vem só do movimento da cabeça. Medido.
  - Escala e posição da câmera: IDÊNTICAS em todos os trechos de rosto: transformação do fundo em relação a f0 (pontos ORB no fundo, 39–82 pontos válidos) = escala 0,999–1,001 e deslocamento < 1,5 px em f10, f18, f90, f110, f133, f527, f550, f572, f956, f975, f992, f1213, f1240, f1261, f1309, f1320, f1336. Não há punch-in, zoom, reenquadramento nem estabilização. Medido.
  - Cor: fundo liso (parede) numa cor média dessaturada #538176 (f0, x650 y150) / #53837a (f0, x640 y600) / #4a746b (f0, x30 y150, canto mais escuro), roupa lisa escura quase preta, pele quente; borda de um móvel em primeiro plano, marrom #603f1b, na faixa de baixo (f0, y≈1262–1280). Tratamento cinematográfico: contraste suave, a cor do fundo puxada para um tom frio dessaturado (#538176), pele alaranjada, fundo desfocado (profundidade de campo curta: o objeto pessoal da parede está borrado). Medido (cores) + observado (tratamento).
  - Luz: suave e frontal-lateral, sem sombras duras; nenhum elemento gráfico sobre o rosto além da legenda. Observado.
- Movimento:
  - Todos os 13 cortes são secos (1 quadro de troca, dif 39,8–125,3), sem fade, sem whoosh, sem flash, sem zoom de transição. Nenhum corte rosto → rosto (nenhum jump cut visível: dentro de cada trecho de rosto a maior diferença entre quadros vizinhos é 4,8–8,7, só gesto). Medido.
  - Nenhum efeito sonoro em corte algum (canal lateral -120 dB nos 13 quadros de corte). Medido.
- Tabela de todos os cortes:

| corte | quadro | tempo | antes → depois | dif | palavra que abre o plano novo | desloc. |
|---|---|---|---|---|---|---|
| 1 | f19 | 0,79 s | rosto → cena (A01) | 86,7 | nº 5 "I've" | +32 ms |
| 2 | f90 | 3,75 s | cena (A01) → rosto | 101,1 | nº 14 "and" | +44 ms |
| 3 | f134 | 5,59 s | rosto → cena (A02) | 46,8 | nº 20 "I" | -11 ms |
| 4 | f527 | 21,98 s | cena (A06) → rosto | 42,9 | nº 67 "I'm" | -9 ms |
| 5 | f573 | 23,90 s | rosto → cena (A07) | 57,9 | nº 72 "I'm" | -41 ms |
| 6 | f676 | 28,19 s | cena (A07) → cena (A08) | 39,8 | nº 86 "Ideally," | -5 ms |
| 7 | f760 | 31,70 s | cena (A08) → cena (A09) | 86,3 | nº 98 "You'll" | -42 ms |
| 8 | f956 | 39,87 s | cena (A09) → rosto | 54,7 | nº 128 "Now," (39920 ms) | -46 ms |
| 9 | f993 | 41,42 s | rosto → cena (A10) | 125,3 | nº 132 "I" | -14 ms |
| 10 | f1146 | 47,80 s | cena (A10) → cena (A11) | 55,6 | nº 154 "Editors," | +10 ms |
| 11 | f1213 | 50,59 s | cena (A11) → rosto | 52,3 | nº 162 "If" | +2 ms |
| 12 | f1262 | 52,64 s | rosto → cena (A12) | 63,4 | nº 172 "you." | +47 ms |
| 13 | f1309 | 54,60 s | cena (A12) → rosto | 71,4 | nº 182 "apply" (54540 ms) | +56 ms |

- Planos de rosto: f0–f18 (19 q, 792 ms) · f90–f133 (44 q, 1835 ms) · f527–f572 (46 q, 1919 ms) · f956–f992 (37 q, 1543 ms) · f1213–f1261 (49 q, 2044 ms) · f1309–f1336 (28 q, 1168 ms). Total 223 quadros = 9,30 s (16,7 % do vídeo). Medido.
- Ritmo: rosto e cena se alternam; 3 vezes uma cena corta direto para outra cena (cortes 6, 7 e 10). Intervalo entre cortes: mínimo 19 q (f0→f19), máximo 196 q (f760→f956). Medido.
- Som: nenhum efeito nos cortes; a voz é contínua através de todos eles. Medido.
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - o A-roll do apresentador (enquadramento fixo, frontal, meio primeiro plano)
  - quais frases ficam no rosto (as de relação direta com o espectador) e quais vão para cena
- Nesta referência as lacunas foram preenchidas com: o criador de suéter azul-marinho, numa parede verde-petróleo com uma sacola pendurada (o objeto pessoal), mesa de madeira na borda de baixo; ficam no rosto: abertura do pedido ("And now I need your help"), a negação ("I'm not looking for experts"), "Now, how to apply", "If you love these videos, I want to work with you" e o CTA final.
- Receita de tratamento de cada imagem: A-roll cinematográfico, câmera fixa, fundo liso desfocado com 1 objeto pessoal, cor dessaturada com pele quente; nada de zoom digital.
- Regra de escolha: o rosto fica com o que é PESSOAL e relacional (pedido, negação, convite, CTA); tudo o que é fato, número, lista, lugar, dinheiro ou instrução vai para cena. Cada volta ao rosto dura 0,8–2,0 s. Teste de generalização: (1) Claude Code: "e agora eu preciso de você" no rosto; "já são 3 mil alunos" vira cena de gráfico. (2) Café: "eu não sou barista" no rosto; "o Brasil exporta 40 milhões de sacas" vira cena.

- Confiança: quadros de corte, dif, escala e posição da câmera, cores, durações, ausência de som = medido · tratamento de cor, luz e posição dos olhos/queixo = observado · leitura do que fica no rosto = inferido (padrão em 6 trechos).
