# V05-A13 · mapa: círculo desenhado, rótulo, imagem dentro do círculo e zoom-portal
- Categoria: P22 · Mapa com marcação (provisória do analista: (provisória) mapa ilustrado com marcador de lugar (círculo + nome) que vira portal para a cena seguinte)
- Fonte: V05 quadros f925–f973 (38,58–40,58 s; 49 quadros ≈ 2044 ms) · 23,976 fps
- Fala: "And on the coast of Lebanon, the city of Tyre"
- Tipo de fala: lugar
- Gatilho: entra por corte seco em f925 (38 580 ms), 100 ms depois do início da palavra nº 137 "And" (38 480 ms). O círculo começa a ser traçado em f928 (+5 ms do início de "on", #138, 38 700 ms… f928 = 38 705 ms). Conferido: dif 89,4 em f925 (`perfil`); strip de entrada (traço visível a partir de f928). (conferido pelo envelope: a voz de "And" só sobe em f925, −14,5 dB depois de −25 a −28 dB em f922–f924; o corte cai JUNTO da voz, ≈ 0 ms, e não +100 ms; o JSON mantém +100 porque o `confere` mede contra a transcrição.)
- Quadro-chave: f940
- Camadas ativas: cena de corte (mapa) | grafismo (círculo, rótulo, imagem no círculo) | legenda | transição (zoom pelo círculo)
- Leitura dos strips: strip.jpg = quadros f926 a f973, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 48 células (recorte x250 y520 420x260 do quadro, só a área do círculo, na pasta foi gravado o quadro inteiro). detalhe-costa.jpg = quadro f940, região x400 y200 160x160 px, ampliada 3× sem suavizar (linha da costa em degraus com fios escuros, mar liso, terra com textura de papel). detalhe-papel-realce.jpg = quadro f940, região x520 y860 160x160 px, ampliada 2× sem suavizar, contraste ×6 em volta da média (o pontilhado do papel e a vinheta entrando pela direita). detalhe-circulo-rotulo.jpg = quadro f940, região x285 y505 280x140 px, ampliada 2× sem suavizar (círculo preto chapado e nome em sans bold marrom-escura).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala dá um lugar; o mapa situa o espectador em 1 s e o círculo vira a porta para a cena seguinte (o mergulho leva do "onde" para o "o quê").
- Por que este design: mapa plano de 2 cores (mar e terra), sem fronteiras nem nomes além do lugar citado; círculo preto + nome em sans à direita, como num atlas escolar.
- Por que estas cores: mar azul-acinzentado #465e64 e terra bege-papel #ad9a83, ambos dessaturados (cabem na paleta sépia do vídeo); o preto do marcador é o único contraste forte.
- Por que estes efeitos: textura de papel na terra, costa em degraus com fios escuros (relevo de papel recortado) e vinheta (borda 41 %): parece um mapa físico impresso, não um gráfico de computador.
- Por que este movimento: a câmera já aproxima devagar desde o corte; o círculo se desenha, o nome se digita, a imagem abre dentro do círculo e a câmera mergulha nele acelerando: o mapa "vira" a cena.
- Sensação do movimento: viagem: aproximação constante e depois queda para dentro; produzida pelo push de +1,06 %/q, pelo traço de 7 q, pela máscara que abre em 5 q e pelo mergulho que só acelera (+3,1 %/q em f952–f958, dif até 21,7 no fim).

## FORMA (fixa: reproduzir igual)
- Design: mapa plano ilustrado, de tela cheia, mar à esquerda em azul-acinzentado #3f535a (f940, x100 y400) com linhas de profundidade paralelas à costa (contorno da costa repetido em faixas mais claras), terra à direita bege-papel #ad9a82 (f940, x600 y900) com textura de papel e vinheta escura nos cantos (#61574b em x100 y1150) (medido). Marcador: círculo de traço PRETO, espessura ≈ 6 px (x296–301 na linha y600), diâmetro 136 px (18,9 % da largura) em f940, centro (359, 575) = (49,9 %, 44,9 %) (medido com `med.py`, lum < 35). Rótulo: nome do lugar em sans bold preta-marrom #271c16 (corrigido no reestudo, f940: mediana dos pixels do nome; antes #1a1a1a), x460–542 y561–598 (11,4 % × 2,9 %), à direita do círculo, alinhado pelo meio do círculo (centro y 45,3 %), 33 px de folga do círculo (medido com `caixa`). Imagem dentro do círculo: vídeo da cena seguinte, recortado em círculo pela borda interna do traço.
- Movimento:
- Passos internos:

| passo | 1º quadro | completo | duração | tipo | gatilho |
|---|---|---|---|---|---|
| corte para o mapa | f925 | — | 0 | corte seco | a 1ª palavra da frase (#137) +100 ms |
| círculo se desenha | f928 | f934 | 7 q ≈ 292 ms | traço preto que cresce a partir do topo, no sentido anti-horário, até fechar | a 2ª palavra da frase (#138) +5 ms |
| rótulo do nome do lugar | f933 | f939 (corrigido no reestudo, f933–f939: digitação medida por quadro; antes f932–f937) | 8 q ≈ 334 ms até 100 % (alinhado ao reestudo) | letras surgem uma a uma, da esquerda para a direita, cada uma com fade de 5–6 q (≈ +19 %/q), 1 letra nova a cada ≈ 0,7 q; 100 % só em f940 (corrigido na correção: 8 q, f933–f940) | a palavra de lugar genérica, antes do nome (#140, 38 960 ms) −88 ms |
| imagem dentro do círculo | f945 | f949 | 5 q ≈ 209 ms | mancha da imagem cresce do centro até encher o círculo (máscara circular que abre) | o nome da região (#142, 39 340 ms) +73 ms |
| zoom pelo círculo (portal) | f952 | f973 | 22 q ≈ 918 ms | câmera mergulha no círculo: diâmetro 136 px (f940) → 158 (f950) → 210 (f960) → maior que o quadro (f966); o rótulo cresce junto e sai pela direita (f962–f966); curva que só acelera: dif 4,2 (f952) → 6,6 (f960) → 11,7 (f966) → 21,7 (f973) | a frase com o nome do lugar (#143–146): f952 = 39 706 ms, 1ª palavra dela 39 780 (−74) |

- Saída: não há corte: quando a borda do círculo sai do quadro (≈ f972), a imagem da cena seguinte já é a tela cheia (V05-A14); a velocidade cai em seguida (dif 14,6 em f974, 9,8 em f975), ou seja, o mergulho acelera até o fim e o freio fica na cena nova.
- Ritmo: o mapa fica 2,0 s; o marcador completo (círculo + nome) fica parado ≈ 5 quadros (f940–f944; corrigido na correção: era ≈ 8 q, f937–f944, mas o nome só fica cheio em f940) antes de a imagem aparecer dentro dele; a câmera do mapa já se aproxima devagar desde o início (dif 1,8 a 3,2).
- Som: o efeito estéreo de 36,9–38,6 s termina no corte de entrada (f925 = 38,58 s); nada novo no portal (lateral −120 dB de 38,7 a 41 s).
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)
- Textura (reestudo 20/11):
  - Terra: família papel com fibra (pontilhado fino). `textura` f940 região 480,880,160,160: #ad9a83, grão 4,07, manchas 3,0, ac1 +0,32 / ac2 −0,16 (grão fino de 1–2 px), direção horizontal +0,54 × vertical +0,10 (fibra horizontal), grão cinza (B/G/R 4,08/4,07/4,08). Detalhe realçado: pontilhado irregular denso, sem manchas grandes. f940 × f944: anda com a câmera (é do mapa).
  - Mar: família liso. `textura` f940 região 60,350,160,160: #465e64, grão 0,43, manchas 2,2 (chapado com degradê suave).
  - Costa: 3 faixas paralelas no mar, cada uma limitada por um fio escuro de ≈ 3 px (mais escuro que o mar), como camadas de papel recortado com sombra interna; a terra encosta no mar com uma borda escura (detalhe f940).
  - Círculo e nome: chapados, sem textura.
- Efeitos (reestudo 20/11): vinheta (`borda` f940: luma 100 · 90 · 77 · 59 · 41 %; nitidez cai junto: 100 · 69 · 40 · 19 · 10 %, mapa liso). Fios escuros de relevo na costa. Círculo: preto puro, borda nítida, sem sombra. Nome: sem sombra. Sem grão de filme, sem aberração, sem brilho.
- Câmera (reestudo 20/11): f928→f944: ×1,183 (+1,06 %/q, +28,7 %/s), centro sobe −2,3 px/q (aproximação constante desde o corte, com o círculo centrado). Portal f952→f958: ×1,201 (+3,1 %/q, +108 %/s); fim f960→f966: +5,4 %/q (+352 %/s), centro sobe −14 px/q (172 de 453 pontos, região 0,0,720,790, medido na correção): só acelera até sair do círculo. O círculo e o nome estão presos ao mapa (crescem junto).
- Cadência (reestudo 20/11): 24 imagens/s (dif muda em todos os quadros do portal; o traço do círculo cresce em todos os 7 q).
- Legenda nesta cena (reestudo 20/11): volta no quadro do corte (f925, depois do rosto sem legenda). 3 blocos no mapa (5 palavras f925–f939; o nome da região sozinho f940–f951; 5 palavras com o nome do lugar f952–f975); o 3º ATRAVESSA o portal e entra na cena A14. Tarja mediana 68 % (f940: luma dentro 60 × fora 186 → 68 %); sobre a terra clara a tarja fica marrom-acinzentada. Texto #f0e918. O nome no mapa aparece 1,3 s ANTES de a voz dizer o nome (rótulo f933–f940; o nome falado em f965,8) e 19 q antes de a legenda mostrá-lo (f952): o rótulo antecipa a fala.
- Entrada do texto (reestudo 20/11): nome do lugar, digitado: p2 de luma na caixa f932 197 · f933 173 · f934 136 · f935 101 · f936 65 · f937 23 (1ª letra faz fade de 4–5 q); borda direita dos pixels escuros f936 x482 · f937 504 · f938 539 · f939 541 (completo). opacidade por letra (miolo × anel de fundo local, com cada quadro alinhado ao f940 por casamento de pontos para tirar o push da câmera, medido na correção): 1ª f933 19 · 38 · 58 · 76 · 90 · 97 · 100 (f940); 2ª f933 6 · 17 · 36 · 54 · 75 · 96 (f938); 3ª f935 16 · 35 · 56 · 76 · 95 (f939); 4ª f935 5 · 16 · 40 · 61 · 81 · 100 (f940). Cada letra leva 5–6 q (≈ +19 %/q), 1 letra nova a cada ≈ 0,7 q (as 4 começam entre f933 e f935); total f933–f940 (8 q ≈ 334 ms) (corrigido na correção: era ≈ 1 letra por quadro com fade de 3–4 q e fim em f939, 7 q); corrigido no reestudo: "f932–f937, 6 q" → "f933–f939, 7 q" (medido por quadro). Letra (f940): sans bold, maiúscula 30 px (y561–590), altura-x 22 px (y569–590), descendente até y597; haste 5 px → 0,23 (semibold a bold); largura 82 ÷ 4 ÷ 22 = 0,93; cor #271c16 (preto-marrom quente, não cinza neutro; corrigido no reestudo: antes #1a1a1a).

## CONSTRUÇÃO
1. mapa: ilustração plana de tela cheia, 2 cores: mar #465e64 liso com degradê leve; terra #ad9a83 com textura de papel pontilhado (grão ≈ 4, fibra horizontal). Costa em 3 degraus paralelos no mar (cada um +8 a +12 de luma em relação ao de fora), cada degrau limitado por um fio escuro de ≈ 3 px. Sem fronteiras, sem outros nomes.
2. vinheta presa à tela: 100 · 90 · 77 · 59 · 41 % do centro para a borda.
3. marcador (preso ao mapa): círculo de traço preto de 6 px, diâmetro 136 px (18,9 % da largura) no início, centrado no lugar e no centro do quadro (49,9 %, 44,9 %).
4. nome (preso ao mapa): sans bold, altura-x 22 px, cor #271c16, à direita do círculo com folga de 33 px, alinhado pelo meio do círculo.
5. imagem da cena seguinte recortada pelo círculo (máscara circular interna ao traço).
6. animação (ms a partir do corte f925): câmera push +1,06 %/q desde 0 e subindo 2,3 px/q; 125 ms o círculo começa no topo e fecha no sentido anti-horário em 292 ms; 333 ms o nome começa a ser digitado (1 letra nova a cada ≈ 0,7 q, cada letra 0 → 100 % em 5–6 q, ≈ +19 %/q, preso ao mapa) e fica completo em 626 ms (corrigido na correção: era 1 letra/q com fade de 3–4 q, completo em 584 ms); 834–1000 ms tudo parado (exceto a câmera); 834 ms a imagem abre do centro do círculo até enchê-lo em 209 ms; 1126 ms o mergulho começa (ease-in: +3 %/q, acelerando até a borda do círculo sair do quadro em ≈ 1960 ms) e o nome sai pela direita junto; o freio acontece já na cena seguinte.
7. legenda por cima, voltando no corte.
- Linha do tempo (ms a partir do corte f925): 0 corte (na 1ª palavra da frase) · 125 círculo · 333–626 nome digitado · 834 imagem abre no círculo · 1126 mergulho · ≈ 1960 a cena seguinte enche a tela · 2044 fim (sem corte).
- Parâmetros que dependem do conteúdo: o recorte do mapa (o lugar no centro), o nome, a imagem que abre no círculo (1º quadro da cena seguinte).
- O que NÃO fazer: não usar mapa de satélite nem com fronteiras e nomes; não usar círculo vermelho ou com brilho; não mostrar o nome depois da voz (ele vem antes); não frear o mergulho no mapa; não cortar seco para a cena seguinte.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "região geográfica do fato" (o mapa); "ponto exato do lugar citado" (posição do círculo); "nome do lugar" (rótulo); "imagem/cena do que existia nesse lugar" (o que aparece no círculo e vira a cena seguinte).
- Nesta referência as lacunas foram preenchidas com: costa do Mediterrâneo oriental; o ponto de Tiro; "Tyre"; navios de vela roxa.
- Receita de tratamento de cada imagem: mapa plano estilizado (sem fronteiras, sem estradas), 2 cores (mar frio dessaturado, terra bege) com linhas de profundidade na costa, textura de papel e vinheta; marcador preto de traço grosso; rótulo sans bold escuro; a imagem dentro do círculo é a própria cena seguinte (vídeo), recortada em círculo.
- Regra de escolha: localização literal. Quando a fala cita um lugar, mostra-se o mapa com o lugar marcado e entra-se nele pelo círculo, ligando o "onde" ao "o quê" sem corte.

- Receita de tratamento de cada imagem (reestudo 20/11): mapa ilustrado em 2 cores dessaturadas, terra com papel pontilhado, costa em degraus com fio escuro, vinheta de 41 % na borda.
- Receita de ILUSTRAÇÃO (reestudo 20/11): mapa de papel recortado em camadas: preenchimento chapado, contornos de costa repetidos em 3 degraus com fio escuro, textura de papel só na terra; marcador = círculo preto de traço desenhado; revelado por corte seco e explorado por zoom-portal.
- Teste de generalização: reel sobre Claude Code: "e em São Francisco, um laboratório…" → mapa da baía em 2 cores, círculo preto no bairro, nome digitado, abre a imagem do prédio e mergulha. Reel sobre café: "nas montanhas da Etiópia…" → mapa do Chifre da África, círculo na região, nome digitado, abre a imagem da plantação e mergulha.

- Confiança: tempos dos passos medidos no strip (±1 quadro); geometria e cores medidas; sentido do traço observado.
