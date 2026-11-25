# V01-A38 · duas fotos caem por cima do diagrama e saem em cascata (a de cima primeiro)
- Categoria: P09 · Cartão que cai por cima da cena (provisória do analista: (provisória) fotos impressas sobrepostas a um diagrama (interrupção com saída))
- Fonte: V01 quadros f2714–f2785 (113,08–116,04 s; 72 quadros ≈ 3000 ms) · 24 fps · por cima de V01-A37
- Fala: "That's why a wetsuit is supposed to fit so tight."
- Tipo de fala: consequência ("por isso a roupa tem de ser justa") + exemplo
- Gatilho: foto 1 em f2714 = 113083 ms, −37 ms antes da palavra nº 369 "That's" (113120 ms). Foto 2 em f2744 = 114333 ms, +213 ms depois da nº 374 "supposed" (114120 ms).
- Quadro-chave: f2760
- Camadas ativas: b-roll (fotos) | cena de tela cheia (diagrama atrás) | legenda | transição (saída)
- Leitura dos strips: strip.jpg = quadros f2712 a f2722, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 11 células. strip-saida.jpg = quadros f2774 a f2786 (saída em cascata), mesma regra, 13 células. strip-geral.jpg = quadros f2712 a f2786, de 2 em 2, 38 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-saida-f2780.jpg = quadro f2780, região x0 y100 720x760 px, ampliada 1× sem suavizar (meio da saída) · detalhe-canto-sobreposicao.jpg = quadro f2760, região x560 y600 110x150 px, ampliada 3× sem suavizar.


## LEITURA DE EDITOR
- Por que esta cena aqui: "por isso tem de ser justa" é a consequência prática da regra; o editor interrompe o diagrama com a prova real (alguém vestindo a roupa apertada) e depois tira as fotos para mostrar o diagrama já no estado seguinte.
- Por que este design: duas fotos empilhadas na metade de cima, a 2ª menor e deslocada (plano geral → detalhe), deixando o pé do diagrama aparecer embaixo: o espectador não perde o fio.
- Por que estas cores: P&B real sobre o diagrama colorido; a mudança de linguagem diz "isto é o mundo real".
- Por que estes efeitos: borda de papel e sombra da foto de cima sobre a de baixo: pilha física; na saída, borrão horizontal forte: as fotos são "puxadas" da mesa.
- Por que este movimento: cada foto cai na sua meia-frase; a saída em cascata (a de cima primeiro, cada uma para um lado) revela o diagrama como se tirássemos papéis de cima dele.
- Sensação do movimento: duas batidas e uma varrida rápida (417 ms) com arrasto; a pilha inteira sobe e recua devagar enquanto está na tela.

## FORMA (fixa: reproduzir igual)
- Design:
  - Foto 1 horizontal P&B em vídeo (alinhado ao reestudo) (a prova real da frase, plano geral), borda de papel, ≈ 92 % da largura, na METADE DE CIMA da tela (f2730: x33–694, y≈136–638, levemente girada; 92 % × 39 %), cobrindo a parte de cima do diagrama (a maior parte da silhueta do sujeito); a parte de baixo do diagrama continua visível embaixo. (conferido, f2730, por varredura de bordas: o y93 de antes era o topo do disco teal atrás, não a foto; antes: ≈ 95 %, y≈93–600)
  - Foto 2 horizontal P&B (a mesma prova, em detalhe), menor (≈ 75 %), cai por cima da foto 1, mais baixa e centrada na largura (f2760 x84–628, y313–726) (alinhado ao reestudo).
- Movimento:
  - Foto 1: cai com estalo (diferença f2714 46,4 em relação ao diagrama) e assenta em ≈ 2 imagens (topo f2716 y93 → f2718 y92). (medido)
  - Foto 2: cai em f2744 e assenta em 2 imagens (topo do conjunto y86 → 87). (medido)
  - Saída em cascata, de cima para baixo da pilha, com borrão: foto 2 desliza para a DIREITA (f2776–f2780) e foto 1 para a ESQUERDA (f2780–f2785); o diagrama reaparece em f2784–f2786 já no estado novo. Diferença por imagem: f2776 17,5 · f2778 26,3 · f2780 28,1 · f2782 28,0 · f2784 20,1 · f2786 7,2. Total 10 q (417 ms). (medido; direções observado no strip-saida)
  - Cadência 12 imagens/s (fase par). (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | foto 1 (metade de cima) | f2714 | 4 q (167 ms) | cai + assenta | estalo | nº 369 | −37 ms |
  | foto 2 (detalhe) por cima | f2744 | 4 q (167 ms) | cai + assenta | estalo | nº 374 | +213 ms |
  | saída: foto 2 → direita, foto 1 → esquerda | f2776 | 10 q (417 ms) | deslizes com borrão | acelera | nº 379 (115750) | +167 ms |
- Ritmo: foto 1 sozinha 30 q (1250 ms); foto 2 por cima 32 q (1333 ms). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Foto 2 (detalhe, por cima): papel fotográfico P&B com grão forte. f2760 região 430,560,150,80: #7f7d80, grão 11,0 níveis (inclui textura da areia), manchas 14,9, ac1 +0,66, cinza puro (11,04 nos 3 canais); rígida (correlação +0,87 depois de alinhar): foto parada. Teste novo (f2756×f2758 e ×f2760, afim da foto 2, região 100,330,520,380): não decide; claros resíduo/σ 1,71–1,75, correlação +0,06…+0,09, mas os escuros também mudam (3,2–5,0, correlação +0,08…+0,12) e o alinhamento casa só 299–345 pontos: ou a foto 2 também tem movimento interno (vídeo) ou o casamento falha; baixa confiança.
  - Foto 1 (plano geral, embaixo): P&B, céu #a5a3a6 com grão 4,79 (cinza puro); é VÍDEO (a pose da pessoa muda entre f2760 e f2780).
  - Bordas de papel: off-white #e7e0d3 (embaixo), #d8d1ca / #d7d3ca (lados), #d3cec6 (em cima), ≈ 6–8 px, cantos retos.
- Efeitos (reestudo 20/11):
  - Sombra da foto 2 sobre a foto 1 (f2760, sombra4): logo fora da borda a foto de baixo cai para 85–110 e volta a ≈ 120–130 em 15–20 px; mais forte embaixo (85) e à direita (92), mais fraca em cima (109). Remedido com o perfil alinhado nos 4 lados (f2760): embaixo −40 % no contato, volta em 21 px; à direita −32 %, 18 px; à esquerda −29 %, 15 px; em cima −18 %, 18 px (sobre a foto de baixo, que tem conteúdo). Sombra caída para baixo, mais fraca em cima (os números da nota estavam no mesmo sentido; força corrigida: era ≈ 15–30 %).
  - Desfoque de movimento: sim, forte e HORIZONTAL na saída (f2780: a foto 1 deslizando para a esquerda com arrasto de ≈ 15–25 px; a borda da foto 2 já saindo à direita, borrada).
  - Vinheta, aberração, brilho, profundidade: nenhum.
- Câmera (reestudo 20/11): a pilha sobe e recua: foto 1 f2720 → f2740 escala ×0,9893 (−1,3 %/s), centro (+0,07, −0,41 px/q); foto 2 f2748 → f2762 ×0,9858 (−2,4 %/s), centro (−0,27, −1,86 px/q), giro +0,08°. Fim, antes da saída (medido, f2762 → f2774, região da foto 2): ×0,9941 (−1,2 %/s), centro (−0,11, −1,73 px/q): a pilha continua subindo e recuando devagar até a saída em f2776. O diagrama de trás segue com a câmera dele (V01-A37). Mesa parada.
- Cadência (reestudo 20/11): 12 imagens/s nas fotos e na saída (perfil região da foto 2 f2745–f2790: 0,00 / 14,0 / 0,00 / 11,4 … / 0,00 / 51,8 / 0,00 / 77,7 / 0,00 / 58,5 / 0,00 / 44,8 / 0,04 / 23,8 / 0,00 / 6,0): a saída tem pico em f2778 e freia em 4 imagens.
- Legenda nesta cena (reestudo 20/11): 4 blocos (2, 2, 3 e 2 palavras); o 1º entra em f2715, 1 quadro DEPOIS da foto 1; o bloco seguinte (3 palavras, f2777–f2791) atravessa a saída em cascata. Texto #eade53, 68 %. Atrás da tarja: pés da silhueta e borda de baixo do disco teal (em cima) e mesa (embaixo); tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. (cena de baixo: V01-A37, que continua mudando de estado escondida.)
2. sombra das fotos: caída para baixo: embaixo −40 % no contato, some em ≈ 20 px; lados −29 a −32 %, 15–18 px; em cima ≈ −18 % (corrigido na conferência: era difusa 15–20 px, 15–30 %).
3. foto 1 (vídeo P&B, plano geral): borda off-white ≈ 7 px, levemente girada; f2730 x33–694, y≈136–638 (92 % × 39 %), cobrindo a metade de cima do diagrama.
4. foto 2 (foto P&B, detalhe): ≈ 75 % da largura, mais baixa e centrada na largura (alinhado ao reestudo) (f2760 x84–628, y313–726), por cima da foto 1.
5. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Animação: foto 1 cai em 0 ms (f2714) maior → assenta em 167 ms; foto 2 cai em 1250 ms → assenta em 1417 ms; a pilha sobe ≈ 0,4–1,9 px/q e recua −1,3 a −2,4 %/s. Saída em 2583 ms: foto 2 desliza para a DIREITA e a foto 1 para a ESQUERDA logo depois, as duas acelerando com borrão horizontal forte; o diagrama de trás aparece completo em 3000 ms (f2786). Passos de 2 quadros.
- Linha do tempo (ms a partir da foto 1, f2714 = 113083 ms): 0 foto 1 · 42 ms 1º bloco de legenda · 1250 ms foto 2 · 2583 ms saída começa (foto 2 → direita) · 2750 ms foto 1 → esquerda · 2917 ms o bloco seguinte de legenda já na tela · 3000 ms diagrama de volta, já no estado seguinte.
- Parâmetros que dependem do conteúdo: as duas imagens (plano geral + detalhe da mesma prova), quais delas são vídeo.
- O que NÃO fazer: tirar as fotos com fade ou corte (é deslize com borrão, de cima para baixo da pilha, cada uma para um lado), cobrir o diagrama inteiro (o pé dele fica visível), deixar o diagrama no mesmo estado quando volta.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "prova real da frase, plano geral" e "a mesma prova, em detalhe".
- Nesta referência as lacunas foram preenchidas com: pessoa fechando a roupa justa; close das mãos no zíper.
- Receita de tratamento de cada imagem: fotos/vídeos reais P&B, horizontais, borda de papel, a 1ª grande na metade de cima, a 2ª menor por cima e deslocada.
- Regra de escolha: "por isso X precisa ser Y" → prova real de Y (o objeto sendo usado assim), geral e depois detalhe; ao terminar a frase, a pilha se desfaz e devolve o diagrama.
- Teste de generalização: (1) Claude Code: "por isso o prompt precisa ser curto" → print de um prompt de 3 linhas; close no contador de tokens; saem em cascata. (2) café: "por isso o tamper precisa ser firme" → foto do barista prensando; close da mão; saem em cascata.
- Receita de tratamento (reestudo 20/11): P&B neutro com grão de foto ≈ 5 níveis no céu (cinza puro), contraste alto; plano geral em vídeo + detalhe em foto; bordas off-white 6–8 px; a de cima faz sombra caída para baixo na de baixo (embaixo −40 %, ≈ 20 px; lados 15–18 px; em cima ≈ −18 %) (alinhado ao reestudo).
- Teste de generalização (reestudo 20/11): (1) Claude Code: "por isso o arquivo de instruções tem de ser curto" → foto 1 de alguém rolando um arquivo enorme, foto 2 de um arquivo curto por cima, saem em cascata e o diagrama volta. (2) café: "por isso a tampa tem de fechar bem" → foto 1 de alguém fechando a garrafa, foto 2 do detalhe da rosca, saída em cascata.

- Confiança: tempos e intensidade medido; tamanhos das fotos e direções da saída observado.
