# V04-A07 · transição "mergulho no disco": a câmera entra no círculo até a imagem de dentro ocupar a tela
- Categoria: P15 · Lupa e janela circular (provisória do analista: (provisória) transição de zoom através de uma janela circular)
- Fonte: V04 quadros f648–f674 (27,03–28,11 s; 27 quadros ≈ 1126 ms) · 23,976 fps
- Fala: "and look straight down"
- Tipo de fala: mecanismo (o ponto de vista muda: "e olhar direto para baixo")
- Gatilho: o zoom acelera a partir de f648 (27028 ms), 28 ms após o início da palavra nº 91 "and" (27000 ms); o aro sai do quadro em f659–f660, durante a palavra nº 93 "straight" (27440 ms; f660 = 27528 ms → +88 ms). Conferido na folha f640–f683 e no `perfil`.
- Quadro-chave: f662
- Camadas ativas: legenda | cena de tela cheia | transição
- Leitura dos strips: strip.jpg = quadros f640 a f683, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha (o mergulho inteiro e a chegada do cartão seguinte); não há strip-saida nem strip-geral (cena < 48 quadros). Cada célula traz o nº do quadro e o tempo. Reestudo 20/11: detalhe-mergulho.jpg = quadro f656, região x200 y250 300x300 px, ampliada 2× sem suavizar (quadro do meio do mergulho: sem borrão de movimento); detalhe-canto.jpg = f670, x0 y0 300x300, 2× (canto escurecido e mole da foto de dentro).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala diz "olhar direto para baixo" e a câmera faz exatamente isso: entra na lente; a transição é a própria ilustração da frase.
- Por que este design: nenhum elemento novo; o disco de A06 vira portal, e a foto de dentro passa a ser o mundo inteiro.
- Por que estas cores: as mesmas de A06 (P&B quente); a continuidade de cor esconde a troca de "plano".
- Por que estes efeitos: a vinheta de quadro continua por cima da foto de dentro (luma a 25 % na borda em f670), então o espectador sente que ainda está "olhando por um visor".
- Por que este movimento: aceleração exponencial até o aro sair do quadro e frenagem longa sobre a imagem de dentro, como um mergulho que pousa.
- Sensação do movimento: queda/mergulho com pouso suave; vem da escala que sobe de +38 %/s a +61 %/s em 10 quadros e cai para +26 %/s em 15 quadros, sem borrão de movimento.

## FORMA (fixa: reproduzir igual)
- Design: o mesmo disco de V04-A06 (aro creme grosso, foto P&B dentro). Ao fim, a foto de dentro do disco ocupa a tela toda, com vinheta escura nas bordas (observado).
- Movimento:
  - Zoom contínuo para dentro do disco, centrado nele: o aro cresce e sai pelas bordas laterais em f656–f659 e pelas de cima/baixo em f659–f660 (observado).
  - Curva (dif global por quadro, medido em `perfil`): 23,8 (f644) → 25,7 → 26,8 → 27,6 → 28,8 (f648) → 28,4 → 28,6 → 29,5 → 29,3 → 30,6 → 31,5 → 32,7 → 33,8 → 34,2 (pico f657) → 31,6 → 31,2 → 28,4 (f660) → 26,8 → 25,6 → 25,2 → 25,0 → 24,5 → 23,6 → 23,1 → 23,0 → 22,5 → 21,7 → 21,3 → 21,5 → 21,0 → 20,5 (f674). Ou seja: acelera por ≈10 quadros até o aro sair (f657), depois desacelera e segue num zoom lento sobre a foto de dentro (f660–f674).
  - Saída: o cartão seguinte (V04-A08) entra deslizando pela esquerda por cima, a partir de f675.
  - Cadência 24 q/s (sem quadros repetidos) (medido).
- Passos internos: nenhum além da curva acima.
- Ritmo: 1,13 s de transição. Anterior: o disco não chega a assentar; cresce devagar e sem parar desde o fim da fase rápida em f612 (remedido em V04-A06), e o zoom só acelera a partir de f648. O recorte do agente de A06 ainda cruza a base do quadro até f650 e some em f651 (remedido, folha f646–f663). Próximo: A08 entra em f675.
- Som: nenhum efeito destacável (áudio mono, voz contínua) (observado no envelope).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Foto de dentro do disco (agora em tela cheia): foto aérea P&B quente de alto contraste (família impressão antiga / grão de filme), #857b71, luma 125, grão 16,7, manchas 25,6, ac1 +0,75 (f670 x300 y400 100x100); anda com a câmera (`--q2 674`: +0,65). No detalhe: realces pontilhados e linhas brancas onduladas sobre preto-cinza, sem retícula de impressão.
  - Aro creme: o mesmo de A06 (liso, sem textura), visto só até sair do quadro em f659–f660.
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: forte e mantida durante o mergulho: luma 100/80/74/51/38 % (f650) e 100/86/70/44/25 % (f670).
  - Borda borrada: nitidez 100/95/46/18/15 % (f650) e 100/106/93/68/36 % (f670) → o canto fica mole (detalhe-canto).
  - Desfoque de movimento: sem desfoque de movimento (medido na conferência: borda de 2 a 9 px a 56–107 px por quadro); aqui também nítido no quadro de velocidade máxima (f656, detalhe-mergulho), com escala de +2 %/q.
  - Luz da cena (correção 20/11, medido f670, perfis p75 na foto de dentro já em tela cheia): centro da poça ≈ (41–43 %, 39–61 %) (platô do perfil p75 e ajuste parabólico; em y o claro do meio da foto pesa), luma de pico 200 (p75); a 100 px da borda esquerda 39 % e em x620 57 % do centro; no alto do quadro 21 % e na base 27 % do pico vertical (o claro do meio da foto pesa: confiança média). Mesa nos pontos fixos: não há mesa em f670 (a foto cobre a tela: (360,1060) 62,4 e (360,1180) 48,7). Centro e força próprios desta cena.
  - Sombra, fio, brilho, aberração: nenhum (o aro tem só o fio externo de 2 px de A06).
- Câmera (reestudo 20/11): escala por pares de 4 quadros, região x0 y100 720x700: f644→f648 +38,5 %/s; f650→f654 +55,9 %/s; f654→f658 +60,8 %/s (pico, ≈ +2,0 %/q); f662→f666 +39,5 %/s; f668→f672 +25,8 %/s. Centro anda −3 a −4 px/q para cima-esquerda no pico e −1,6 px/q no fim (o mergulho mira o centro do disco, que está à direita/abaixo do centro do quadro). Giro 0°. Uma câmera só (o disco e o cartão de fora escalam juntos).
- Cadência (reestudo 20/11): 24 imagens/s (`perfil` f640–f674 sobe suave de 18,2 a 30,5 em f655 e desce a 15,7, sem degraus nem quadros ≈ 0).
- Legenda nesta cena (reestudo 20/11): 3 blocos de 1 a 2 palavras (a última palavra da frase já cai em A08), 6 a 18 quadros cada; tarja 59 % (medido direto, colunas do meio: f650 53/58 %, f660 62/60 %, f670 60/60 %; altura 48 px y844–891, folga 11 px em cima; corrigido na conferência: era "59 % (mediana, 53–62 %)" do censo, mesmo valor) sobre a foto clara (luma 152–200, o fundo mais claro do vídeo até aqui); texto #e5e51c a #eae91b. O 3º bloco atravessa a saída (f659–f676, entra em A08). Censo marca "texto branco grande" nesses quadros: falso positivo (realces brancos da foto aérea).

## CONSTRUÇÃO
1. herdado de A06: cartão + disco com aro creme e foto aérea dentro + vinheta de quadro.
2. câmera: zoom centrado no centro do disco, curva exponencial em velocidade: começa em +38 %/s (0 ms), sobe até +61 %/s em ≈ 375 ms (f657, quando o aro sai do quadro), cai para +40 %/s em ≈ 650 ms e +26 %/s em 1000 ms, seguindo lento até a entrada de A08. Sem desfoque de movimento.
3. efeito de quadro: a vinheta forte + borda mole de A06 continua durante o mergulho e, com a foto de dentro em tela cheia, a poça fica em ≈ (42 %, 50 %) (39 % a 100 px da borda esquerda, 57 % a 100 px da direita). É a luz desta cena, não um valor fixo do vídeo.
4. legenda V04-L01.
- Linha do tempo (ms a partir de f648): 0 ms o zoom passa a acelerar (28 ms depois da 1ª palavra do trecho); 334–459 ms o aro sai pelas laterais e depois por cima/baixo (f656–f659); 459 ms pico de velocidade; 500–1126 ms frenagem sobre a foto de dentro; 1126 ms A08 entra deslizando por cima.
- Parâmetros que dependem do conteúdo: a imagem dentro do disco (precisa aguentar ampliação ×3 sem perder textura).
- O que NÃO fazer: cortar para a imagem de dentro em vez de mergulhar; zoom linear; borrão radial de velocidade; tirar a vinheta quando a foto de dentro vira tela cheia.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "imagem dentro da janela circular" (o que se passa a ver ao entrar).
- Nesta referência as lacunas foram preenchidas com: foto aérea P&B de trincheiras.
- Receita de tratamento de cada imagem: foto P&B de alto contraste, cheia de textura, que aguenta ser ampliada até a tela inteira; a vinheta escura da cena continua por cima.
- Regra de escolha: a fala muda o ponto de vista ("olhar direto para baixo", "pelo periscópio") → a câmera entra na janela que representa esse olhar. Teste em 2 temas: Claude Code → disco com o print do código, a câmera mergulha e o print vira a tela inteira em "olha o que ele vê por dentro"; café → disco com a lupa sobre um grão, a câmera mergulha e a textura do grão ocupa a tela.
- Receita de tratamento (reestudo 20/11): foto P&B quente de alto contraste e muita textura fina (grão ≈ 17, realces pontilhados), resolução suficiente para ser ampliada ≈ 3× sem virar borrão; nenhum tratamento próprio de borda (a vinheta é do quadro).
- Teste de generalização: Claude Code → a lente mostra um print de código; a câmera mergulha nela e o print vira a tela inteira na frase "olha o que ele vê por dentro"; café → a lente mostra a superfície de um grão; a câmera mergulha e a textura do grão vira a tela na frase "visto de perto".

- Confiança: curva e quadros = medido; momentos de saída do aro = observado no strip.
