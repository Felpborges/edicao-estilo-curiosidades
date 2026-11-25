# V02-A07 · pilha de documentos antigos com marca-texto
- Categoria: P20 · Documento com marca-texto (provisória do analista: (provisória) documentos de arquivo (papel) que caem um sobre o outro numa pilha, cada um com um trecho marcado em amarelo)
- Fonte: V02 quadros f573–f675 (23,90–28,15 s; 103 quadros ≈ 4296 ms) · 23,976 qps
- Fala: "I'm looking for fast learners, people who can pick up something new every week."
- Tipo de fala: descrição
- Gatilho: entra por corte seco em f573 (23899 ms), -41 ms antes da palavra nº 72 "I'm" (23940 ms); conferido no envelope (pausa de 400 ms antes de "I'm"; o corte cai no fim da pausa). Marca-texto 1 em f594, +155 ms depois de nº 75 "fast" (24620 ms). Documento 2 entra em f609, -338 ms antes de nº 77 "people" (25740 ms), dentro da pausa de 300 ms depois de "learners,". Marca-texto 2 em f630, +57 ms depois de nº 80 "pick" (26220 ms). Documento 3 entra em f640, +135 ms depois de nº 82 "something" (26560 ms). Marca-texto 3 em f660, -132 ms antes de nº 85 "week." (27660 ms).
- Quadro-chave: f670
- Camadas ativas: legenda | grafismo (cena de tela cheia) | som
- Leitura dos strips:
  - strip.jpg: quadros f572 a f619, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 48 células; cada célula traz o nº do quadro e o tempo.
  - strip-saida.jpg: quadros f638 a f677, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 40 células; cada célula traz o nº do quadro e o tempo.
  - strip-geral.jpg: quadros f571 a f676, de 3 em 3, 8 colunas, da esquerda para a direita, linha a linha; 36 células; cada célula traz o nº do quadro e o tempo.
  - detalhe-doc1-inteiro-f600.jpg: quadro f600, região x30 y280 660x420 px, ampliada 1× sem suavizar (o 1º documento inteiro, com marca-texto e bordas escurecidas de papel velho).
  - detalhe-cartao-sombra-sobre-jornal.jpg: quadro f670, região x380 y560 240x120 px, ampliada 3× sem suavizar (borda do cartão de cima, sombra sobre o recorte de jornal, grão dos dois papéis).
  - detalhe-foto-grao.jpg: quadro f670, região x160 y190 200x110 px, ampliada 3× sem suavizar (grão da foto P&B presa atrás).
  - detalhe-marca-texto-cartao.jpg: quadro f670, região x190 y530 330x45 px, ampliada 3× sem suavizar (marca-texto atrás do texto, pontas arredondadas).
  - detalhe-doc2-caindo-f614.jpg: quadro f614 (meio da queda do 2º documento), região x0 y0 720x840 px, ampliada 1× sem suavizar (procura de desfoque de movimento).

## LEITURA DE EDITOR
- Por que esta cena aqui: depois da negação dita no rosto, a qualidade abstrata pedida (aprender rápido e sempre) precisa de prova concreta: documentos de pesquisas diferentes se acumulam no ritmo da frase.
- Por que este design: a pilha que cresce É a ideia de novidade constante; cada documento real com uma linha marcada diz "isto foi lido e entendido"; deslocamentos e giros pequenos fazem a pilha parecer feita à mão.
- Por que estas cores: papéis de época com tons diferentes (amarelado, cinza de impressão, bege) contra o tampo escuro; o amarelo do marca-texto é o fio que liga os três.
- Por que estes efeitos: cada folha tem sombra difusa que aparece nos 4 lados sobre o papel de baixo (−40 a −80 níveis) e, sobre o tampo, sobretudo para baixo e para a direita (em cima só um véu de −4 níveis): é o que faz a pilha ter espessura; o grão forte da impressão P&B e da foto (≈ 20 níveis) diz "arquivo".
- Por que este movimento: cada documento CAI do alto e freia (12 a 17 q), a câmera recua e sobe devagar para manter a pilha enquadrada; o marca-texto vem logo depois de cada pouso.
- Sensação do movimento: acúmulo rápido e ritmado, "pá, marca; pá, marca; pá, marca", como alguém jogando provas na mesa. Produzida pela alternância queda (ease-out) → varredura (ease-out) a cada 0,6–0,9 s, com som de papel nos pousos.

## FORMA (fixa: reproduzir igual)
- Design:
  - Fundo: tampo escuro #201f1b (74 % da área em f600) / #1f1e1a (f670). Medido.
  - Documento 1 (horizontal): documento de arquivo pequeno em papel amarelado #e8e1b7 (f600, x200 y330), impresso em tinta de 2 cores (azul/vermelha antiga), cantos vivos, inclinado ≈ 2°, sombra curta; f600 x41 y294 628x392 (5,7 % · 23,0 %; 87,2 % x 30,6 %), centro (49,3 %, 38,3 %). Medido.
  - Documento 2: impressão de arquivo P&B (página impressa com retícula), retangular, com borda serrilhada leve, menor que o 1º, cai por cima e o cobre em parte. Observado.
  - Documento 3: carta datilografada sobre papel bege claro #d6ceb9 (remedido, f670 x555 y525; o #cbc5ba antigo, x150 y700, caiu no doc 2), com uma foto P&B (imagem do assunto do documento) presa atrás, no alto (tons #a9a9a8–#b7b7b6). Observado + cores medidas.
  - Pilha final (f670): tudo junto ocupa x75 y175 570x659 (10,4 % · 13,7 %; 79,2 % x 51,5 %), centro (50,0 %, 39,4 %); cada folha nova deslocada e girada uns poucos graus em relação à de baixo; a de baixo continua visível nas bordas. Medido.
  - Marca-texto: amarelo #f0d84a (tolerância 55) sobre UMA linha/trecho de cada documento: f600 linha principal do doc 1, ≈ 462 px de largura (64 % da largura) em y ≈ 448; f640 linha de título do doc 2, x154 y315 412x47 (57 % da largura); f670 trecho do doc 3, x198 y539 312x32 (43,3 % x 2,5 %). Medido.
- Movimento:
  - Entrada: corte seco em f573 (dif 76,1); o doc 1 já chega em movimento e assenta em ≈ 16 quadros (f573–f589, ≈ 667 ms): dif 20,4 · 17,9 · 15,9 · 14,1 · 12,3 · 12,2 · 9,2 · 7,0 · 4,8 · 2,8. Desaceleração longa (ease-out). Depois, deriva lenta (dif ≈ 2–2,8 em f590–f604). Medido.
  - Marca-texto 1: f594–f600, 7 quadros ≈ 292 ms, varre da esquerda para a direita. Observado (folha 2 em 2 + strip).
  - Documento 2: cai do alto (f609 a borda aparece no topo, f612–f616 desce, assenta ≈ f620), ≈ 12 quadros ≈ 500 ms, com a câmera acompanhando; dif 8,2 (f609) · 16,3 · 21,4 · 24,9 · 26,5 · 29,6 (f615, pico) · 27,3 · 24,7 · 23,1 · 21,6 (f621) · 15,4 · 10,5 (f625). Medido.
  - Deriva entre os passos: f625–f639 dif ≈ 10,5–11,3 constante (a câmera avança/afasta devagar e sem freio). Medido.
  - Marca-texto 2: f630–f634, 5 quadros ≈ 209 ms (largura completa só em f635). Curva ease-out: largura 9 % · 25 % · 41 % · 51 % · 56 % · 58 % (f630–f635). Medido (remedição, caixa #f0d84a).
  - Documento 3: cai do alto f640–f656 (≈ 17 quadros ≈ 709 ms); dif 14,6 · 20,7 · 24,5 · 25,2 (f644, pico) · 22,4 · 21,1 · 17,1 · 13,9 · 10,8 · 6,7 · 4,6 (f656). Medido.
  - Marca-texto 3: f660–f667, 8 quadros ≈ 334 ms (remedido; f664 tem só 90 % da largura). Curva ease-out com freio longo: largura 5 % · 14 % · 26 % · 34 % · 39 % · 42 % · 43 % · 43,3 % (f660–f667). Medido (remedição, caixa #f0d84a).
  - Permanência: completo f667–f675 = 9 quadros ≈ 375 ms (remedido), com deriva (dif 2,4–3,3). Medido.
  - Saída: corte seco para o mapa (V02-A08) em f676 (dif 44,3). Medido.
- Passos internos:

| passo | quadro de início | duração | tipo de movimento | curva | palavra-gatilho e deslocamento |
|---|---|---|---|---|---|
| doc 1 em cena (corte) e assenta | f573 | 16 q ≈ 667 ms | corte + deslize/escala residual | ease-out longo | nº 72, o pronome que abre a frase (23940 ms): -41 ms |
| marca-texto 1 | f594 | 7 q ≈ 292 ms | varredura esq. → dir. | linear | nº 75, o adjetivo da qualidade (24620 ms): +155 ms |
| doc 2 cai sobre a pilha | f609 | ≈ 12 q ≈ 500 ms | queda do alto + câmera | acelera e freia | nº 77, 1ª palavra da 2ª parte da frase (25740 ms): -338 ms |
| marca-texto 2 (linha de título) | f630 | 5 q ≈ 209 ms | varredura | ease-out (remedido) | nº 80, o verbo de aprender (26220 ms): +57 ms |
| doc 3 cai sobre a pilha | f640 | ≈ 17 q ≈ 709 ms | queda do alto + câmera | acelera e freia | nº 82, o objeto (o novo) (26560 ms): +135 ms |
| marca-texto 3 (trecho) | f660 | 8 q ≈ 334 ms (remedido, f660–f667) | varredura | ease-out, freio longo (remedido) | nº 85, a última palavra (a frequência) (27660 ms): -132 ms |

- Ritmo: começa 1 quadro depois do fim do rosto (f527–f572, 46 q ≈ 1919 ms de rosto antes). Um passo novo a cada ≈ 15–21 quadros (≈ 0,6–0,9 s): doc → marca → doc → marca → doc → marca. Cada documento fica sozinho e completo (marcado) por: doc 1 f600–f608 ≈ 9 q (375 ms); doc 2 f634–f639 ≈ 6 q (250 ms); doc 3 f667–f675 ≈ 9 q (375 ms, remedido). Medido.
- Som: efeitos estéreos (canal lateral) em f588–f592 (pico -34,6 dB; colado ao pouso do doc 1, f589, e logo antes do marca-texto 1) e f623–f637 (pico -37,7 dB; do pouso do doc 2 até o marca-texto 2). Nada no corte de entrada nem na queda do doc 3. Leitura de envelope: sons curtos de papel/marcador, bem abaixo da voz (voz ≈ -12 a -20 dB). Medido (envelope); natureza inferida.
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Tampo: o mesmo, liso, parado na tela, luz fixa (f650: 28,0 no topo, 33,5 a y960, 26,5 no pé, 23,9 nos cantos, igual a f200).
  - Documento 1: papel amarelado de época. f600, região x634 y420 22x140 (margem entre os fios azuis): #e3dcb2, luma 218,5, grão 2,62 níveis, manchas 1,22, ac1 +0,45, grão cinza (2,73/2,63/2,69). As bordas do papel escurecem para um bege-marrom (papel envelhecido; detalhe-doc1-inteiro-f600). Família: papel com fibra (antigo). Impressão em tinta azul, vermelha e verde com leve borrão de tipografia.
  - Documento 2 (impressão P&B): papel cinza claro com pontilhado e manchas fortes, tipografia preta pesada com falhas de tinta (detalhe-doc2-caindo-f614). Família: impressão antiga com retícula.
  - Documento 3 (cartão datilografado): f670, região x380 y390 190x12: #ccc4af, luma 196,2, grão 4,66 níveis, manchas 1,89, ac1 +0,48, grão cinza. Família: cartão (grão áspero visível no detalhe-cartao-sombra-sobre-jornal).
  - Foto P&B presa atrás: f670, região x160 y190 180x50 (céu): #9c9b9a, luma 155, grão 20,4 níveis, manchas 11,9, ac1 +0,57, grão cinza (20,39/20,42/20,41). Família: grão de filme (da própria foto).
  - Marca-texto: amarelo #f0d84a translúcido por TRÁS do texto, bordas macias, pontas arredondadas, passa a linha em ≈ 4 a 8 px de cada lado (detalhe-marca-texto-cartao).
- Efeitos (reestudo 20/11):
  - Sombra das folhas sobre o tampo (sombra4 f600, doc 1, caixa x45 y300 620x380): embaixo −9,8 níveis em ≈ 22 px; à direita −13,3 em 23 px; à esquerda −6,2 em 19 px; em cima nenhuma. Perto do canto inferior direito (linha horizontal em y670): 16 a 7 colado contra 34 do tampo, voltando em ≈ 35–40 px (as sombras de baixo e da direita se somam no canto). Remedido na correção 20/11 com perfil alinhado na borda real (f600, mesma caixa): embaixo fio 12 (−69 %) e 20 contra 38 (−18 níveis, −47 %) até ≈ 19 px (corrigido na conferência: era "−9,8 níveis em ≈ 22 px", medida sem alinhar a borda do papel girado); à direita 1 a 6 nos 3 primeiros px (borda escura do papel velho somada à sombra) e 17–22 → 34 em ≈ 15 px; EM CIMA −4 níveis (31 contra 35, −11 %) até ≈ 13 px (corrigido na conferência: era "em cima nenhuma"); à esquerda não medível (borda sem contraste limpo).
  - Sombra de folha sobre folha (sombra4 f670, cartão de cima, caixa x137 y375 450x250): nos 4 lados, com mais força embaixo: em cima −39 níveis, embaixo −80, laterais −54 a −58, sempre colada e sumindo em 24 a 29 px. Sobre papel claro a sombra difusa (≈ 25 px) aparece inteira; sobre o tampo escuro só o lado de baixo/direita se nota. Leitura: é UMA sombra difusa de ≈ 25 px deslocada para baixo, não sombras diferentes.
  - Borda das folhas: transição de 2 px (corte limpo de tesoura), sem fio claro; o documento 1 tem as bordas escurecidas de papel velho (vinheta própria do documento).
  - Desfoque de movimento: nenhum (f614, meio da queda do doc 2: a tipografia do doc 2 está nítida no detalhe).
  - Aberração de cor: nenhuma (f670, foto: +0,00/+0,01 px). Brilho, halo, profundidade de campo, grão global: nenhum (medido em f670).
- Câmera (reestudo 20/11): o tampo fica parado; a camada da pilha recua e desce na tela o tempo todo para acompanhar a pilha que cresce para cima. f576 → f586 (assentamento do doc 1): escala −0,30 %/q, conteúdo +11 px/q para baixo e −4,6 px/q para a esquerda, giro −0,02 °/q; f626 → f636: −0,12 %/q, +3,8 px/q para baixo; f660 → f670: −0,09 %/q, +0,8 px/q para baixo; fim f667 → f675 (região x0 y0 720x820, 558 de 600 pontos; medido na correção 20/11): −0,08 %/q, +0,55 px/q para baixo (mesmo valor). Freia mas nunca para. Cada documento novo tem a sua própria queda (de cima, ease-out) somada ao recuo comum.
- Cadência (reestudo 20/11): 24 imagens/s (`perfil` f609–f625 na queda do doc 2: 12,5 → 44,7 (f615) → 19,2, sem quadros parados alternados).
- Legenda nesta cena (reestudo 20/11): tarja 50 % (f600, f650, f670: luma dentro 17 × fora 33–37; direta 49,6–50,9 % na conferência; altura 76 px); cor #f3e912 a #f8e912; centro 67,9–68,3 %. Blocos: pronome + verbo entra junto do corte (f573–f583), preposição + adjetivo f584–f601, o substantivo com ponto f602–f615, 1 q sem legenda em f616 (na pausa, quando o doc 2 cai), substantivo + relativo f617–f625, verbo + partícula (3 pal.) f626–f637, o objeto (2 pal.) f638–f656 (o bloco mais largo da cena: 437 px de texto = 61 % da largura), a frequência com ponto f657–f674, o 1º bloco da frase seguinte (1 pal.) f675–f687 ATRAVESSA o corte de saída (f676) e termina já no mapa. Atrás da tarja: o tampo, colado logo abaixo da borda de baixo do documento 1 (a pilha desce até y ≈ 830, a 0 a 15 px do topo da tarja). Outro texto na tela: o texto dos documentos, inclusive título e corpo do doc 2 com letras de 35 a 44 px (o detector marca "texto branco grande" em f617–f674, mas é texto preto sobre papel claro: falso positivo); a legenda divide a tela com esse texto sem conflito porque fica abaixo da pilha.
- Entrada do texto (reestudo 20/11): o texto dos documentos não anima (vem impresso); o que entra é o marca-texto (3 varreduras ease-out de 5 a 8 q, ver Movimento).

## CONSTRUÇÃO
1. fundo: tampo liso parado na tela, com a luz oval fixa.
2. camada da pilha (recua e desce devagar o tempo todo: −0,3 → −0,09 %/q, +11 → +0,8 px/q para baixo).
3. documento 1: documento de arquivo em papel amarelado #e3dcb2 (grão ≈ 2,6, bordas escurecidas), 87 % × 31 % do quadro, centro (49 %, 38 %), girado ≈ 2°; sombra difusa ≈ 25 px deslocada para baixo/direita (no tampo: −18 níveis embaixo até 19 px, forte à direita até 15 px, fraca em cima, −4 níveis até 13 px) (corrigido na conferência: era "−10 embaixo, −13 à direita, nada em cima"). Já está na tela no corte e assenta em 16 q (0 a 667 ms, ease-out).
4. marca-texto 1 sobre a linha principal: 292 ms a partir de 875 ms (f594–f600), esquerda → direita.
5. documento 2: impressão de arquivo P&B, papel cinza com retícula e tipografia pesada, menor, cai do alto por cima de parte do 1 de 1500 a 2000 ms (f609–f620, acelera e freia); deslocado e girado alguns graus.
6. marca-texto 2 na linha de título: 2375 a 2583 ms (f630–f635, ease-out 9 → 58 %).
7. documento 3: cartão bege #ccc4af de grão forte (≈ 4,7) com foto P&B granulada (≈ 20 níveis) presa atrás no alto; cai do alto de 2792 a 3500 ms (f640–f656, pico em f644, ease-out); sombra difusa sobre os papéis de baixo (−40 em cima a −80 embaixo, 24–29 px).
8. marca-texto 3 num trecho do cartão: 3542 a 3875 ms (f660–f667, ease-out com freio longo).
9. legenda (camada fixa, tarja preta 50 %, altura 76 px; ver V02-L02); a pilha final termina logo acima da tarja (y ≈ 65 %).
- Linha do tempo (ms a partir do corte f573): 0 corte (doc 1 assentando) · 667 assentado · 875 marca 1 · 1500 doc 2 cai · 2375 marca 2 · 2792 doc 3 cai · 3542 marca 3 · 3875 completo, deriva · 4296 corte seco para o mapa.
- Parâmetros que dependem do conteúdo: nº de documentos (1 por pedaço da frase), quais documentos, a linha marcada em cada um, o instante de cada queda (na palavra).
- O que NÃO fazer: documentos digitais limpos sem grão; empilhar sem giro e sem deslocamento; sombra só embaixo sobre papel (sobre papel ela aparece nos 4 lados); queda linear ou com quique; marca-texto por cima do texto; câmera parada enquanto a pilha cresce.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - documentos de arquivo REAIS dos temas já tratados (provas de que o assunto foi pesquisado), um por passo da frase
  - trecho de cada documento que o marca-texto destaca (a frase que resume o achado)
- Nesta referência as lacunas foram preenchidas com: bilhete de trem antigo, recorte de jornal sobre chapéus de palha, carta oficial com foto de prédio; trechos marcados: a linha principal do bilhete, a manchete, uma frase da carta.
- Receita de tratamento de cada imagem: scans de documentos antigos, cor original do papel (amarelado, P&B, bege), recortados pela borda do papel, sem moldura, sombra curta, levemente girados; empilhados com deslocamento; texto legível o bastante para o marca-texto fazer sentido.
- Regra de escolha: quando a fala descreve uma QUALIDADE abstrata da pessoa/coisa ("aprende rápido, aprende algo novo toda semana"), a cena mostra PROVAS concretas da variedade (documentos de pesquisas diferentes) se acumulando num ritmo rápido, um por pedaço da frase. Teste de generalização: (1) Claude Code: "você não precisa saber programar, só aprender rápido" → caem na pilha um print de documentação, um trecho de erro no terminal, um README, cada um com uma linha marcada. (2) Café: "um bom barista testa algo novo toda semana" → caem fichas de receitas de métodos diferentes, cada uma com a proporção marcada.

- Receita de tratamento (reestudo 20/11): documentos = scans reais com a cor do papel original (amarelado #e3dcb2, cinza de jornal, bege #ccc4af), grão do próprio papel de 2,6 a 4,7 níveis, bordas de papel velho escurecidas quando o original tem; fotos de arquivo P&B com grão forte (≈ 20 níveis) e sem nenhuma correção de cor; recorte limpo pela borda do papel, sombra difusa ≈ 25 px para baixo.
- Receita de ILUSTRAÇÃO (reestudo 20/11): não há ilustração; o único traço do editor é o marca-texto amarelo translúcido atrás do texto.
- Teste de generalização: (1) Claude Code: "você não precisa saber programar, só aprender rápido" → caem na mesa um print impresso de documentação, uma tira de erro de terminal e um README antigo, cada um com uma linha marcada em amarelo. (2) café: "um bom barista testa algo novo toda semana" → caem fichas de receita de métodos diferentes (uma amarelada, um recorte de revista, um cartão), cada uma com a proporção marcada.

- Confiança: caixas, cores, curvas de queda e assentamento, efeitos sonoros = medido · detalhes de cada documento e varredura dos marca-textos = observado (folha 2 em 2 + strips 1 em 1) · natureza dos sons = inferido.
