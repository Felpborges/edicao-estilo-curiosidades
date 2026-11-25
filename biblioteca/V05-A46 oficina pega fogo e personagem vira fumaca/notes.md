# V05-A46 · a oficina pega fogo e o personagem vira fumaça (3D)
- Categoria: P24 · Cena 3D narrativa (provisória do analista: (provisória) cena 3D com efeito de fogo (overlay de chamas reais) e dissolução do personagem)
- Fonte: V05 quadros f3199–f3286 (133,43–137,05 s; 88 quadros ≈ 3670 ms) · 23,976 fps
- Fala: "the last palace workshops burned. And a 3,000-year-old craft (dyed…)"
- Tipo de fala: consequência
- Gatilho: entra por corte seco em f3199 (133 430 ms), 70 ms antes do início da palavra nº 436 "the" (133 500 ms). Conferido: dif 44 em f3199 (`perfil`).
- Quadro-chave: f3230
- Camadas ativas: b-roll 3D | efeito (fogo, fumaça) | legenda
- Leitura dos strips: strip.jpg = quadros f3260 a f3288, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 29 células (a dissolução em fumaça). strip-geral.jpg = quadros f3199 a f3286 (amostrado). detalhe-fogo-sobreposto.jpg = quadro f3230 (fogo cheio), região x0 y100 720x800 px, ampliada 1× sem suavizar. detalhe-personagem-vira-fumaca.jpg = quadro f3272 (meio do sumiço), região x150 y150 420x700 px, ampliada 1× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: "as últimas oficinas queimaram" e "o ofício morreu": o fim é físico (fogo) e simbólico (o artesão some); a cena faz as duas coisas sem cortar.
- Por que este design: o artesão de pé à esquerda com o objeto do ofício na mão, a bancada com o recipiente à direita, e o prédio real ao fundo; o fogo nasce na bancada e cresce pela direita.
- Por que estas cores: a cena inteira vira laranja-avermelhada quando o fogo está cheio (cor média #4e2112 → #512312) e volta ao marrom quando sobra fumaça: a cor da cena conta o incêndio.
- Por que estes efeitos: fogo e fumaça REAIS sobrepostos em modo claro (somam luz), não desenhados; o personagem fica translúcido e some: o "fim do ofício" literal.
- Por que este movimento: o fogo cresce até cheio exatamente na palavra "burned"; o personagem desaparece durante "3,000-year-old craft"; push-in lento o tempo todo.
- Sensação do movimento: perda; o fogo quente e rápido seguido de um esvaziamento lento e silencioso.

## FORMA (fixa: reproduzir igual)
- Design: o personagem do ofício (low-poly) de pé diante do lugar que acaba (imagem real ao fundo, sépia), com os objetos do ofício (material na cor-tema). O modo como acaba entra como efeito REAL (vídeo sobreposto em modo de mistura claro), cresce à direita e cobre a cena; a cor média do quadro vai de #422a1d (f3200) para #4e2112 (f3215) e #512312 (f3230, mais vermelho-alaranjado), depois volta a marrom #4e2f20 (f3250, fumaça clara) e #3d251a (f3285) (medido, média do quadro inteiro).
- Movimento (dif global, medido): f3200–f3245 o efeito cresce (dif 2 → 5, com 6,5 em f3245); f3248–f3260 o efeito some e fica fumaça (dif 2); f3263–f3284 o personagem se DISSOLVE em fumaça e some (dif 3,4 → 6,5 em f3272 → 2), observado: corpo fica translúcido e vira silhueta. Câmera: push-in lento e contínuo o plano todo, não citado antes (remedido por registro de pontos: ×1,011 de f3200 a f3212 na imagem do fundo; ×1,031 e −30 px, −20 px de f3255 a f3285 ≈ +2,2 a +2,5 %/s).
- Passos internos:

| passo | quadros | tipo | gatilho |
|---|---|---|---|
| o efeito cresce | f3203–f3245 | overlay de vídeo real + tom laranja | o sujeito e o verbo da destruição (#439–440): efeito cheio no verbo (134 700 ms ≈ f3230) |
| o efeito vira fumaça | f3245–f3260 | fumaça clara, o efeito some | a conjunção que abre a frase seguinte |
| personagem desaparece | f3263–f3284 | dissolve em fumaça | a idade do ofício (#443–444) (corrigido na conferência: a coluna trazia as falas entre aspas) |

- Saída: corte seco em f3287 (dif 47) para o rosto.
- Ritmo: 3,7 s; 3 estados (efeito, fumaça, vazio).
- Som: nenhum efeito detectado no canal lateral.
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

- Textura (reestudo 20/11):
  - fundo (fachada de palácio, foto real): P&B tingida de laranja pelo fogo · #692e18 em f3230 · grão 3,65 · manchas 12,31 · ac1 +0,82 · anda com a câmera.
  - chão/bancada: superfície granulada com pontinhos claros cintilantes (granito/areia), textura fotográfica; vira #4e2f20 depois do fogo.
  - fogo e fumaça: vídeo real de chamas sobre fundo preto, sobreposto em modo de mistura claro (as chamas somam luz e deixam a cena atrás visível nas áreas escuras).
  - personagem: blocos lisos marrom-escuros, cabeça de retrato pintado; objeto do ofício em foto recortada, cor natural.
- Efeitos (reestudo 20/11): vinheta global fraca nesta cena (100 → 107 → 101 → 75 → 56 % da luma; nitidez → 45 %; `borda` f3230) porque o fogo ilumina as bordas; grade de cor laranja na cena toda durante o fogo (o canal R tem mais grão: B/G 3,6 × R 4,1); dissolve do personagem em fumaça (corpo translúcido, f3263–f3284); sombra, halo, aberração, grão de filme: nenhum adicionado (medido em f3230).
- Câmera (reestudo 20/11): confirmo a remedição (push-in lento e contínuo de +2,2 a +2,5 %/s, com deriva para cima-esquerda no fim); 3 pares na correção (região x40 y80 640x700): começo +2,3 %/s (f3201→f3213, 537 de 600 pontos), meio +2,8 %/s (f3236→f3248, 347 pontos, com o fogo), fim +2,8 %/s e −0,7 px/q (f3270→f3285, 541 pontos): uma fase só.
- Cadência (reestudo 20/11): 24 imagens/s (o vídeo do fogo e o dissolve mudam a cada quadro; `perfil` f3266–f3276: 7–9,4, sem quadro repetido).
- Legenda nesta cena (reestudo 20/11): 3 blocos: 3 palavras (entra no corte), 2 palavras e 5 palavras (f3245–f3286, sai no corte para o rosto) (corrigido na conferência: eram as falas entre aspas); texto #eee716, 28 px (35 com descendente), centro y 65,5 %; atrás da tarja: o chão escuro (luma fora 26–32), tarja quase invisível (opacidade só medível em 3 quadros: 66 %; vale a do vídeo, 68 %; 51 px, y 809–859); nenhum outro texto.

## CONSTRUÇÃO
1. fundo: foto real da fachada do lugar, P&B quente, ocupando y 0–58 %.
2. chão e bancada: superfície granulada escura com pontinhos claros (y 58–100 %); recipiente do ofício sobre a bancada à direita.
3. personagem do ofício 3D low-poly à esquerda (x 10–50 %, cabeça y 10–20 %), com o objeto do ofício na mão (foto recortada).
4. fogo: vídeo real de chamas em modo de mistura claro (tela/adição), nasce na bancada em +167 ms e cresce até cobrir a metade direita em +1293 ms; some e vira fumaça clara de +1918 a +2544 ms.
5. grade de cor: cena inteira puxada para laranja-vermelho durante o fogo (#422a1d → #512312), volta ao marrom com a fumaça (#4e2f20 → #3d251a).
6. dissolve do personagem: opacidade 1 → 0 com fumaça subindo do corpo de +2669 a +3545 ms.
7. vinheta fraca (borda 56 %).
8. câmera: push-in +2,3 a +2,8 %/s, quase linear, do início ao corte, com deriva leve para cima-esquerda no fim.
9. legenda amarela V05-L01.
- Linha do tempo (ms a partir do corte): 0 corte seco · +167 o fogo começa · +1293 fogo cheio (no verbo da destruição) · +1918 o fogo vira fumaça · +2669 o personagem começa a sumir (na idade do ofício) (corrigido na conferência: eram as palavras citadas) · +3545 vazio · +3670 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: o tipo de fim (fogo, água, poeira, apagão) e o vídeo real do efeito; o personagem e o objeto do ofício.
- O que NÃO fazer: fogo desenhado ou opaco (é vídeo real em modo claro); manter a cor da cena durante o fogo; cortar para mostrar o sumiço (é dentro do plano); vinheta forte (o fogo ilumina as bordas).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "o lugar/ofício que acaba"; "o modo como acaba" (fogo); "quem desaparece com ele".
- Nesta referência as lacunas foram preenchidas com: oficina do palácio que queima; o tintureiro some na fumaça (o ofício morre).
- Receita de tratamento de cada imagem: 3D low-poly + fundo real sépia; vídeo de fogo/fumaça real sobreposto; dissolução do personagem.
- Regra de escolha: fim/morte de algo abstrato (um ofício) mostrado como o personagem que o representa desaparecendo.
- Receita de tratamento (reestudo 20/11): foto real do lugar em P&B quente; efeito físico em vídeo real (fogo, fumaça) sobreposto em modo claro com grade de cor da cena acompanhando o efeito.
- Receita de ILUSTRAÇÃO (reestudo 20/11): 3D low-poly "colagem" + elementos de vídeo real; o personagem desaparece por dissolve com fumaça.
- Teste de generalização: reel sobre Claude Code → a sala de servidores antiga pega fogo e o operador some em fumaça na palavra "acabou"; reel sobre café → o armazém de sacas pega fogo e o torrador some na palavra "desapareceu".

- Confiança: tempos e cores medidos; dissolução observada.
