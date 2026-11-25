# V04-A03 · foto em cartão (borda clara) tela cheia + recorte do objeto entra deslizando no centro
- Categoria: P16 · Colagem de recortes (provisória do analista: (provisória) foto em cartão sobre fundo escuro com zoom contínuo + recorte sobreposto)
- Fonte: V04 quadros f154–f206 (6,42–8,59 s; 53 quadros ≈ 2211 ms) · 23,976 fps
- Fala: "Nothing in a forest looks like this,"
- Tipo de fala: comparação (contraste: "nada em X se parece com isso")
- Gatilho: corte seco em f154 (6423 ms), 97 ms antes da palavra nº 20 "Nothing" (6520 ms). Conferido: pausa da fala f151,0–f154,9 (silencios) e a legenda troca para "Nothing in a" em f154.
- Quadro-chave: f190
- Camadas ativas: legenda | cena de tela cheia | som (voz)
- Leitura dos strips: strip.jpg = quadros f152 a f167, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha (corte + deslize do recorte); strip-geral.jpg = quadros f152 a f208, de 2 em 2, 8 colunas. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-recorte.jpg = quadro f190, região x420 y760 120x110 px, ampliada 3× sem suavizar (canto do recorte sobre a foto); detalhe-borda-cartao.jpg = f190, x0 y1030 220x90, 3× (borda clara de papel fotográfico e fundo); detalhe-foto.jpg = f190, x330 y200 120x120, 3×, contraste ×6 (grão da foto).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala sai do objeto e vai para o lugar onde ele deveria funcionar; o corte seco na pausa marca a virada de assunto.
- Por que este design: a foto do lugar enche o quadro como uma cópia fotográfica, e o quadrado do objeto colado no meio é um "intruso" que o olho acha na hora; a composição já é a prova da frase.
- Por que estas cores: verdes e marrons lavados e quentes, todos na mesma família do objeto; o intruso não é mais saturado, é só mais escuro e chapado, então a dúvida "combina ou não?" fica para o espectador.
- Por que estes efeitos: borda clara de papel fotográfico (≈ 10 px) diz "foto de arquivo"; a vinheta do quadro escurece a borda do cartão e puxa o olho para o quadrado.
- Por que este movimento: zoom lento e linear (+7 a +9 %/s) no cartão inteiro, e o quadrado chega rápido em 3 quadros na palavra "Nothing".
- Sensação do movimento: aproximação calma, quase documental, com um "tapa" rápido do recorte; produzida pelo contraste entre o deslize de 125 ms e a escala lenta sem curva.

## FORMA (fixa: reproduzir igual)
- Design:
  - Cartão: foto retangular com borda clara fina tipo papel fotográfico: borda ≈ 9 px (y130–y138 em f155, ≈1,3 % da largura do cartão), cor #94846f na borda de cima sob a vinheta (f155, x360 y131–137) (medido). Em f155 o cartão ocupa x14 y127 701x919 = x 1,9 %, y 9,9 %, larg 97,4 %, alt 71,8 %, centro (50,6 %, 45,8 %), retinho (ângulo ≈ 0°) (medido, script de limiar).
  - Fundo: quase preto quente com vinheta: #13100b (f165, x360 y1150), cantos #010101–#060405 (medido). A borda esquerda do cartão fica escurecida pela vinheta (#2b2d20 em f165 x30 y650) (medido).
  - Recorte sobreposto: quadrado recortado do objeto-tema, um pouco abaixo do centro da foto: em f190 x≈258–498 × y≈576–838 (larg 33 %, alt 20,5 %, centro (52,5 %, 55 %)), girado ≈ 4–5° no sentido anti-horário (borda de cima sobe para a direita), sem borda, sem sombra visível (remedido, f190; antes: "≈ 20 % da largura, centro ≈ (50 %, 45 %)", observado). A troca de f154→f160 muda a área x202–699 y351–798 (medido em `dif`), o que confirma a entrada pela direita.
  - Legenda por cima do cartão, na faixa de sempre (y≈856).
- Movimento:
  - Entrada da cena: corte seco em f154 (dif 36,6) (medido).
  - Zoom contínuo e linear do cartão: altura do cartão entre as bordas de papel 71,3 % (f155, y133–1045) → 81,0 % (f190, y53–1089) → 84,7 % (f206, y21–1105) = escala ×1,19 em 51 quadros (2,13 s) ≈ +8,5 %/s (remedido por perfil de coluna em x600, f155/f190/f206; antes: 71,8 % → 79,1 % (f190) → 82,3 % (f206), ×1,146, +6,9 %/s); dif quadro a quadro estável 7–9 (sem aceleração) (medido). Centro fixo em (50 %, 45 %) (medido). Em f170 o cartão já passa das bordas laterais.
  - Recorte: entra deslizando da direita para o centro em 3 quadros f155–f157 (≈125 ms), rápido, assenta em f158 (remedido: folha de 1 em 1 e `perfil` com dif 14,3 e 17,4 em f156–f157 e 5,8 em f158; f155 na borda direita, f156 ≈ 60 %, f157 ≈ 40 %, f158 no lugar). Depois acompanha o zoom do cartão.
  - Saída: corte seco f206→f207 para A04 (dif 55,8) (medido).
  - Cadência: 24 q/s, sem quadros repetidos (dif ≥ 6 em todo quadro) (medido).
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| recorte do objeto desliza da direita até o centro do cartão | f155 | 3 quadros (125 ms), assenta f158 (remedido) | deslize horizontal | rápido, desacelera no fim (observado) | nº 20, 1ª palavra da frase nova (6520 ms) | f155 = 6465 ms → −55 ms |

- Ritmo: começa 0 ms após A02 (corte direto). Design completo (recorte assentado) de f158 a f206 = 49 quadros ≈ 2044 ms (remedido) na tela (em movimento de zoom, sem novo elemento). Próximo: corte para A04 em f207.
- Som: nenhum efeito destacável (pausa f151–f155 com piso −65,2 dB; áudio mono) (medido).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Fundo/mesa (abaixo do cartão): liso escuro quente #0d0b07, luma 11, grão 0,37, manchas 1,20 (f190 x250 y1150 200x100); f190×f191 correlação +0,33 no lugar e +0,44 alinhado, com a câmera andando: não é PARADA nem VIVA (VIVA exige correlação perto de 0 com o quadro parado); é ruído de compressão sobre preto liso; para construir: liso, sem grão próprio, que anda com a câmera (medido) (corrigido na conferência: era "`--q2 200` VIVA").
  - Foto do ambiente (dentro do cartão): papel fotográfico com grão forte (família papel fotográfico / grão de filme), #7a7460, luma 116, grão 22,0, manchas 14,8, ac1 +0,51 (grão fino de 1–2 px), grão cinza (B/G/R 22,03/22,01/22,03) (f190 x300 y300 80x80); anda com a câmera (`--q2 200`: +0,75 depois de alinhar). No detalhe-foto com realce: pontilhado fino de alto contraste, sem retícula.
  - Borda do cartão: faixa clara lisa ≈ 10 px, luma 130–165 (#a4..), com uma linha mais escura de 1–2 px no limite de fora (detalhe-borda-cartao), cai para o fundo em 2–3 px (`sombra` baixo f190: 60 foto → 162–165 borda → 93 → 40 → 22).
  - Recorte do objeto: tecido fotográfico real, #6c5945, grão 5,33, manchas 17,7 (f190 x300 y640 80x80); borda reta cortada a faca, sem contorno, sem papel em volta.
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: forte, luma 100/102/79/44/21 % (f190); só na região do cartão 100/100/83/59/43 % → a foto escurece para as bordas junto com o quadro (vinheta de quadro desta cena; corrigido na conferência: era "a mesma de A02", e cada cena tem a sua).
  - Luz da cena (correção 20/11, medido f190, perfis p75 na foto do cartão, que é a superfície clara mais larga): centro da poça ≈ (32–45 %, 32–39 %) (platô do perfil p75 e ajuste parabólico), luma de pico 143 (p75); a 100 px da borda esquerda 61 % e a 100 px da direita (x620) 46 % do centro; topo e base da foto a 48 % do pico vertical. Mesa: (360,1060) 59,3 cai na borda de baixo da foto; (360,1180) 14,3 é mesa. Centro e força próprios desta cena, não um multiplicador fixo do vídeo.
  - Borda borrada do quadro: nitidez 100/136/112/59/26 % (f190); na região do cartão 100/105/98/69/52 % (borda perde ≈ metade do detalhe).
  - Sombra do recorte: nenhuma mensurável (lado direito f190: 84→72 contínuo, sem vale; lado de baixo: vale de ≤ 5 níveis em 4 px, dentro do ruído). Sombra do cartão sobre a mesa: nenhuma (mesa 22–23 colada na borda).
  - Fio/halo/brilho: só a linha escura de 1–2 px no limite externo da borda de papel. Aberração: nenhuma (+0,01 px, f190). Desfoque de movimento: sem desfoque de movimento (medido na conferência: borda de 2 a 9 px a 56–107 px por quadro) (corrigido na conferência: era "não medido no deslize de 3 q; observado no strip como borrão leve no quadro do meio").
- Câmera (reestudo 20/11): zoom linear centrado, sem giro, em 3 pares (região x40 y100 640x700): começo f160→f172 +9,0 %/s, −1,0 px/q para cima; meio f176→f188 +9,3 %/s, −1,08 px/q (medido na correção); fim f192→f204 +7,1 %/s, −0,85 px/q. Uma fase só, com leve desaceleração no último terço (9 → 7 %/s). Recorte e foto com a MESMA escala (f192→f204: recorte +3,52 %, foto +3,52 % em 12 q) → sem paralaxe, o recorte está colado na foto.
- Cadência (reestudo 20/11): 24 imagens/s (`perfil` f158–f172: 10,0 a 13,0 em todo quadro, sem quadros ≈ 0).
- Legenda nesta cena (reestudo 20/11): 3 a 4 blocos de 2 a 3 palavras; o 1º troca no corte (f154). Tarja 58 % aqui (medido direto, colunas do meio: f160 58/58 %, f165 57/57 %, f175 60/60 %, fundo 76–102); vale para o vídeo 59 % (56 a 64), altura 48 px (y844–891), raio ≈ 7–8 px, folga 3–5 px dos lados e 11 px em cima (corrigido na conferência: era "52 % (luma 35 dentro × 73 fora) em f165"); texto #eee817. Atrás da tarja: troncos claros e chão de folhas (o fundo mais claro até aqui, luma 73–83). A partir de f184 o detector do censo se confunde com o chão amarelado (centro x 44 %, largura 282–287 px e opacidade falsa de 15–17 %): é erro de medida, não mudança da legenda (o still f190 mostra a tarja normal em volta do texto). Nenhum outro texto na tela.

## CONSTRUÇÃO
1. mesa: chapado #0d0b07 (só aparece abaixo e nos lados do cartão).
2. cartão: foto do ambiente vertical com borda clara lisa de ≈ 10 px (#a49385 a #a89485 sob a vinheta), linha escura de 1–2 px no limite externo, sem sombra; no 1º quadro x 1,9 % y 9,9 % larg 97,4 % alt 71,8 %, centro (50,6 %, 45,8 %), 0°. Grão forte de cópia fotográfica (σ ≈ 22 níveis, 1–2 px).
3. recorte do objeto: quadrado reto cortado a faca, sem contorno nem sombra, ≈ 33 % × 20,5 % do quadro, centro (52,5 %, 55 %), girado −4 a −5°. Entra da borda direita até o lugar em 3 quadros (125 ms), rápido e freando, a partir de 42 ms do corte.
4. câmera (camadas 1–3 juntas): escala linear +9 %/s caindo a +7 %/s, centrada em (50 %, 45 %), sobe ≈ 1 px/q; sem giro.
5. efeito de quadro: luz desta cena, poça centrada em ≈ (38 %, 35 %) (79 % a 0,55–0,75 do raio, 44 % a 0,75–0,90, 21 % na borda; a 100 px da borda 61 % à esquerda e 46 % à direita) + desfoque radial suave na borda. Sem desfoque de movimento no deslize do recorte.
6. legenda V04-L01 por cima.
- Linha do tempo (ms a partir do corte f154): 0 ms corte seco, cartão no lugar; 42–167 ms recorte desliza da direita; 167 ms assentado; zoom contínuo até 2211 ms; corte seco para A04.
- Parâmetros que dependem do conteúdo: proporção da foto do ambiente; tamanho e lugar do recorte (onde o objeto "deveria" se esconder).
- O que NÃO fazer: pôr contorno, sombra ou borda branca no recorte (ele tem que parecer colado na foto); zoom com curva; tirar a borda clara do cartão; deixar a foto sem grão; borrar o recorte no deslize (não há desfoque de movimento); reaproveitar a vinheta de outra cena (centro e força são desta).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "foto do ambiente/contexto real" com que o objeto é comparado (onde ele deveria se misturar);
  - "recorte do objeto do tema" (o mesmo objeto da cena anterior, em pedaço quadrado), posto dentro do ambiente.
- Nesta referência as lacunas foram preenchidas com: foto de floresta de faias; quadrado de tecido camuflado.
- Receita de tratamento de cada imagem: foto real de ambiente, vertical, cores naturais um pouco lavadas e quentes, impressa como cópia fotográfica com borda clara fina; o recorte é um quadrado reto sem sombra, colado no centro, para parecer "fora do lugar".
- Regra de escolha: frase de contraste ("nada em X se parece com isso") → mostra o ambiente X literal com o objeto colado no meio, para o espectador VER que não combina. Teste em 2 temas: Claude Code → foto de um escritório comum com um quadrado de tela de terminal colado no centro ("nada num escritório parece isso"); café → foto de uma padaria com um quadrado de grão verde cru no centro.
- Receita de tratamento (reestudo 20/11): foto real do ambiente, tons lavados e quentes (#7a7460 médio), grão forte de cópia (σ ≈ 22 níveis), borda clara de papel fotográfico de ≈ 10 px; recorte = pedaço reto do objeto, sem tratamento extra, mesma luz da foto.
- Teste de generalização: Claude Code → foto de um escritório comum em cartão com borda clara e um quadrado de tela de terminal colado no meio; café → foto de uma padaria em cartão com um quadrado de grão verde cru colado no meio.

- Confiança: bordas, cores, zoom e cortes = medido; tamanho e posição do recorte, curva do deslize e ausência de sombra = observado.
