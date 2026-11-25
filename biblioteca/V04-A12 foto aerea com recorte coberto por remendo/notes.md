# V04-A12 · foto aérea em tela cheia + recorte do objeto + remendo de "terreno" que desliza e cobre o objeto
- Categoria: P16 · Colagem de recortes (provisória do analista: (provisória) foto em tela cheia com recorte que é escondido por outro recorte)
- Fonte: V04 quadros f1064–f1136 (44,38–47,38 s; 73 quadros ≈ 3045 ms) · 23,976 fps
- Fala: "He hid a gun under a canvas, painted to blend in with the ground."
- Tipo de fala: ação narrada (o que o personagem fez: "escondeu X debaixo de uma lona pintada")
- Gatilho: corte seco em f1064 (44379 ms), 61 ms antes da palavra nº 141 "He" (44440 ms). Conferido: pausa f1062,1–f1065,5 (silencios) e legenda "He hid a gun" em f1064.
- Quadro-chave: f1068
- Camadas ativas: legenda | cena de tela cheia | grafismo (recortes) | som (voz)
- Leitura dos strips: strip.jpg = quadros f1062 a f1084, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha (corte, objeto e remendo cobrindo); strip-geral.jpg = quadros f1062 a f1138, de 2 em 2, 8 colunas. Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-recorte.jpg = quadro f1068, região x100 y500 220x120 px, ampliada 3× sem suavizar (borda do recorte frio sobre a foto); detalhe-remendo.jpg = f1080, x100 y300 400x300, 1× (o remendo com trama de lona); detalhe-canto.jpg = f1107, x0 y0 260x260, 2× (vinheta e borda mole); detalhe-foto.jpg = f1107, x250 y950 120x120, 3×, contraste ×6 (grão da foto aérea).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala narra a primeira invenção do personagem; a cena faz a ação na frente do espectador (o objeto está lá, e some).
- Por que este design: vista aérea do lugar + o objeto recortado por cima + um remendo da mesma vista impresso em lona que o cobre: o "truque" fica visível e literal.
- Por que estas cores: o objeto é frio (cinza-azulado #797d82, com realces #c5cbd3) sobre uma foto quente verde-oliva (#7e7c63): o contraste de temperatura faz o olho achá-lo em 1 quadro; o remendo devolve tudo ao verde-oliva.
- Por que estes efeitos: vinheta de quadro forte (29 % na borda) e borda mole (17 % de nitidez) fazem parecer uma foto vista de cima por um visor; a trama de lona no remendo é a pista visual de "lona pintada".
- Por que este movimento: o remendo entra rápido da esquerda na palavra "under" (−1 ms) e a câmera recua (zoom out) acelerando e freando, para mostrar que o objeto sumiu na paisagem inteira.
- Sensação do movimento: truque de mágica: "estava aqui, sumiu"; vem do deslize curto e rápido do remendo seguido do recuo da câmera, que afasta o olhar do lugar do objeto.

## FORMA (fixa: reproduzir igual)
- Design:
  - Fundo: foto do lugar onde algo é escondido, vista de cima, colorizada (verde-oliva, ocre), ocupando a tela inteira (bloco 100 % x 95,5 % em f1066), com vinheta escura forte nas bordas e cantos (#050400–#201d12 em f1066) (medido).
  - Recorte do objeto escondido: render/foto (alinhado ao reestudo) em cinza-azulado claro (cor-chave #c8d0dc), vista de cima/diagonal, sem fundo; em f1068 vai da ponta traseira do objeto em x≈100 até a ponta dianteira, que sai pela borda direita do quadro (x720, y≈358–372), e de y≈358 (topo do objeto) a y≈595 (base): ≈ x 14–100 %, larg ≥ 86 %, alt 18,5 %, centro ≈ (57 %, 37 %), deitado na diagonal (remedido, f1068, perfis de linha y555 e de coluna x510/x550/x715; antes: x247 y379 371x211 = larg 51,5 %, a `caixa` da cor só pegou as partes claras do objeto). Destoa de propósito da paleta do fundo (frio sobre quente) (observado).
  - Remendo (o que esconde): retângulo da mesma textura do fundo, cobrindo a área do objeto, fundido com a foto (sombras da foto por cima), sem borda (observado).
- Movimento:
  - Entrada: corte seco em f1064 (dif 54,0) (medido).
  - O recorte do objeto anda devagar para a direita (deriva f1064–f1076) (observado).
  - Remendo: entra deslizando da esquerda em 5 quadros f1076–f1080 (≈210 ms) e cobre o objeto; curva acelera até o fim: dif 5,0 (f1076) → 7,4 → 10,6 → 14,2 → 15,5 (f1080) → 13,1 → 12,0 → 11,0 (medido em `perfil`; o zoom de fundo continua). O objeto já está todo coberto em f1081, mas o remendo segue deslizando e freando até f1086 (dif 13,1 → 12,0 → 11,0 → 9,9 → 8,1 → 5,7) e assenta em f1087 (dif 4,4, piso do zoom) (remedido, `perfil` f1078–f1094 e folha de 1 em 1).
  - Depois: a câmera recua (zoom out) acelerando e freando, pico ≈ −19 %/s, sobre a foto sem objeto visível (f1081–f1136) (alinhado ao reestudo).
  - Saída: corte seco f1136→f1137 para A13 (pausa f1133,8–f1137,4).
- Passos internos:

| passo | quadro de início | duração | tipo | curva | palavra-gatilho | deslocamento |
|---|---|---|---|---|---|---|
| remendo da textura do fundo desliza da esquerda e esconde o objeto | f1076 | 5 quadros (210 ms) | deslize horizontal | acelera, pico em f1080 | nº 145, a palavra que diz o disfarce (44880 ms) | f1076 = 44879 ms → −1 ms |

- Ritmo: objeto visível f1064–f1079 ≈ 0,67 s; depois 2,3 s da foto "sem nada" (sem nova entrada, só o recuo da câmera (alinhado ao reestudo), de f1087 a f1136 = 50 quadros ≈ 2,09 s; remedido) enquanto a fala explica o disfarce.
- Som: nenhum efeito destacável (áudio mono) (observado no envelope).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Foto aérea colorizada: papel fotográfico pintado (família papel fotográfico), #7e7c63, luma 123, grão 12,2, manchas 23,7, ac1 +0,60 (f1068 x300 y400 120x120); em f1107 numa área de campo #524a2c, grão 2,9, manchas 5,1 (x250 y950); anda com a câmera (o `--q2` deu "VIVA" só porque a câmera recua 29 px no trecho e o alinhamento ficou parcial, +0,49; não é grão vivo).
  - Recorte do objeto: render/foto fria cinza-azulada, #797d82, luma 124, grão 19,6 (detalhe do metal), manchas 31,8 (f1068 x470 y470 60x30); recorte rente, borda dura de 1–2 px, sem contorno.
  - Remendo (a "lona"): a mesma foto aérea com trama de tecido por cima (família tecido): em f1107, onde o remendo está, ac4 = +0,48 contra −0,07 na mesma foto sem remendo (f1068) → padrão periódico de ≈ 4 px, a trama de lona (detalhe-remendo); grão 9,4, manchas 17,9.
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: forte, luma 100/99/86/57/32 % (f1068) e 100/98/83/51/29 % (f1107).
  - Luz da cena (correção 20/11, medido f1107, perfis p75 na foto em tela cheia, a superfície clara mais larga): centro da poça ≈ (49 %, 27–38 %) (platô e ajuste parabólico; em x os dois dão 49 %), luma de pico 124 (p75); a 100 px da borda esquerda 57–61 % e a 100 px da direita 54–66 % do centro; no alto do quadro 31 % e na base 14 % do pico vertical (cai mais embaixo). Mesa: não há (a foto cobre a tela: (360,1060) 69,0 e (360,1180) 58,0). Centro e força próprios desta cena, não um multiplicador fixo do vídeo.
  - Borda borrada do quadro: nitidez 100/96/60/34/16 % (f1068) e 100/111/60/31/17 % (f1107) (detalhe-canto: canto escuro e mole). Confere o teste do briefing (f1107: borda a ≈ 29 % da luma e ≈ 17 % da nitidez).
  - Sombra do recorte: quase nenhuma; embaixo da ponta traseira um vale de ≈ 15 níveis a 12–17 px (f1068: 138 → 107 → 125), compatível com sombra suave curta OU com o terreno (confiança baixa). Lado direito: nenhuma.
  - Fio/brilho: nenhum. Aberração: nenhuma (−0,02 px).
- Câmera (reestudo 20/11): recua (zoom OUT) o tempo todo, acelerando e freando: f1064→f1074 −3,0 %/s (com o objeto ainda visível); f1095→f1107 −19,1 %/s, conteúdo sobe 1,6 px/q; f1120→f1132 −5,5 %/s. Giro ≤ 0,01°/q. (Corrigido no reestudo: a nota dizia "zoom lento contínuo" sem direção; é afastamento, com pico ≈ 1,4 s depois do remendo.)
- Cadência (reestudo 20/11): 24 imagens/s (`perfil` f1076–f1090: 7,3 → 28,2 (f1080) → 6,4, curva contínua).
- Legenda nesta cena (reestudo 20/11): 5 blocos de 2 a 4 palavras, 11 a 20 quadros; o 1º troca no corte (f1064). O último bloco termina em f1133 e o 1º bloco da cena seguinte (com a data) ENTRA 3 quadros ANTES do corte (f1134, corte em f1137): a legenda adianta a próxima frase dentro da cena velha, na pausa. Tarja 59 % (medido direto, colunas do meio: f1070 53/55 %, f1100 66/59 %, f1125 58/59 %, fundo 87–109; altura 48 px y844–891, folga 3–5 px dos lados e 11 px em cima) (corrigido na conferência: era "55 % (mediana, 42–64 %)" do censo; vale para o vídeo 59 %, 56 a 64) sobre a foto verde-oliva (luma 78–96). Nenhum outro texto.

## CONSTRUÇÃO
1. foto aérea colorizada em tela cheia (verde-oliva/ocre, saturação baixa, grão σ ≈ 12), sem borda visível.
2. recorte do objeto: foto/render frio cinza-azulado, deitado na diagonal, ≈ 86 % × 18,5 % do quadro, centro (57 %, 37 %), sangrando a borda direita; sem contorno, sombra no máximo muito leve; deriva devagar para a direita.
3. remendo: retângulo da MESMA foto aérea (mesmo registro, encaixa com o fundo) com textura de lona sobreposta (trama de ≈ 4 px, contraste baixo), sem borda; entra da esquerda em 5 q (210 ms) acelerando, cobre o objeto em f1081 e freia até assentar em f1087.
4. câmera (camadas 1–3): zoom out −3 %/s → −19 %/s (pico ≈ 1,4 s depois do remendo) → −5,5 %/s.
5. efeito de quadro: luz desta cena, poça com centro em ≈ (49 %, 30 %) (51 % a 0,75–0,90 do raio, 29 % na borda; a 100 px da borda ≈ 55–65 % dos dois lados; a base do quadro cai mais que o topo) + borda mole (17 % da nitidez no anel externo). Sem desfoque de movimento no remendo.
6. legenda V04-L01 (a frase seguinte entra 125 ms antes do corte de saída).
- Linha do tempo (ms a partir de f1064): 0 ms corte seco, objeto visível; 500 ms remendo começa (1 ms antes da palavra que diz o disfarce); 709 ms objeto todo coberto; 959 ms remendo assentado; 1300–1800 ms pico do recuo; 2919 ms legenda da próxima cena entra; 3045 ms corte seco para A13.
- Parâmetros que dependem do conteúdo: a vista do lugar; o objeto escondido; o material do disfarce (aqui lona: trama de tecido; em outro tema, a textura do material que esconde).
- O que NÃO fazer: remendo de cor chapada ou de outra imagem (tem que ser a mesma foto, com a textura do material por cima); fade em vez de deslize; câmera aproximando (aqui ela se afasta); copiar a vinheta de outra cena (centro e força são desta).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "lugar onde algo é escondido" (foto de fundo, vista de cima);
  - "objeto escondido";
  - "o que esconde" (remendo com a mesma textura do fundo).
- Nesta referência as lacunas foram preenchidas com: foto aérea de campo; canhão de campanha; lona pintada como chão.
- Receita de tratamento de cada imagem: fundo = foto real colorizada de tons quentes com vinheta; objeto = render/foto recortada em tom frio (alinhado ao reestudo) que destoa; remendo = pedaço da própria textura do fundo, sem borda, para "sumir".
- Regra de escolha: fala de esconder/disfarçar ("escondeu X debaixo de Y") → mostra X, e na palavra "debaixo/sob" Y desliza e some com X. Teste em 2 temas: Claude Code → print de uma tela com uma chave de API em destaque, e um retângulo com a mesma cor do fundo desliza por cima e a esconde ("esconde a chave no .env"); café → mesa de madeira com um grão verde, e um pedaço da madeira desliza e o cobre.
- Receita de tratamento (reestudo 20/11): foto aérea de arquivo colorizada à mão (verde-oliva, ocre), grão médio; o objeto vem de outra fonte, frio (cinza-azulado) de propósito, para destacar; o remendo é a mesma foto com textura do material do disfarce.
- Receita de ILUSTRAÇÃO (reestudo 20/11): recorte do objeto em render/foto de produto frio, rente, sem contorno; "remendo" = máscara retangular de textura (tecido) aplicada sobre a própria foto, revelada por deslize lateral; não ferve.
- Teste de generalização: Claude Code → print de uma página com um botão vermelho recortado por cima; um remendo da mesma página, com textura de papel, desliza e esconde o botão na frase "ele escondeu o botão"; café → foto aérea de uma lavoura com um trator recortado; um remendo da mesma lavoura com trama de tela de sombreamento desliza e o esconde.

- Confiança: cortes, curva do remendo e gatilho = medido; caixa do objeto = medido aproximado; deriva do objeto e fusão do remendo = observado.
