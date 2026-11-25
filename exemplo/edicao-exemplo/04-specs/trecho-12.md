# Trecho 12 · Print da conversa + o roteiro cai por cima · P06 + P09 · Ref V04-A15, V01-A45
Fala: "Na mesma conversa, por exemplo, você pode pedir pra ele criar um roteiro"   ·   Janela no clipe: 25 860 a 29 102 ms   ·   Entra por: corte seco (vindo do rosto, trecho 11)

Clipe: 1080x1920, 23,976 fps, 1 q = 41,708 ms. Quadros do clipe entre parênteses (f = round(ms / 41,708)).
Os tempos de palavra são do whisper aparado; o principal reconfere no envelope. Todo gatilho está escrito
relativo ao início da palavra. **Este trecho NÃO termina em corte:** a mesa continua no trecho 13, que empurra
tudo para fora (ver `trecho-13.md`).

## 1 · Linha do tempo da cena (relativa às palavras)

| passo | o que acontece | gatilho (palavra, índice, deslocamento em ms) | duração (ms · quadros) | curva |
|---|---|---|---|---|
| 1 | Corte seco do rosto para a mesa já montada: cartão vertical com o print da conversa, sem estalo (V04 nunca estala) | 40 ms antes de "Na" (100) → f620 (25 859 ms; −28 ms da palavra medida) | 0 q (corte) | — |
| 2 | Câmera, fase 1: zoom-in + deriva do conteúdo para baixo, desde o 1º quadro | do corte até o passo 3 | 62 q ≈ 2 586 ms (f620–f681) | linear (constante) |
| 3 | O cartão do roteiro cai por cima, no meio da cena, com estalo de 2 degraus | 40 ms antes de "roteiro" (112) → f682 (28 445 ms; −57 ms da palavra) | 4 q = 167 ms (f682–f685), assentado em f686 | degraus secos de 2 q (sem interpolação) |
| 4 | Câmera, fase 2: zoom-in continua, deriva para; âncora do zoom no centro do cartão do roteiro | de f686 até o início do empurrão do trecho 13 (f724) | 38 q ≈ 1 585 ms | linear |
| 5 | Saída: o conjunto (cartão da conversa + cartão do roteiro) é empurrado para baixo-esquerda pelo 1º cartão do carrossel | ver `trecho-13.md` passo 1 (k = 0 em f724) | 12 q | ease-in |

Na tela neste trecho: conversa sozinha 2 586 ms; conversa + roteiro ≈ 1 794 ms até o empurrão (f682–f724),
atravessando a fronteira 29 102 ms sem nenhum evento nela.

## 2 · FORMA (copiar igual) — px de 1080x1920

- **Fundo / mesa:** a mesa global do motor (molde de "O cartão": base #10110c, topo #171612, centro #22211d em
  luz radial difusa, sem textura, sem glow). Na referência V04-A15 a vinheta é mais forte: centro #0d0c08,
  cantos #060405 a #080703 (medido, f1232). Use a global; a diferença está nas dúvidas.
- **Peça 1 · cartão da conversa (P06, V04-A15):**
  - No corte (f620): caixa externa **912 × 1134 px** (84,4 % × 59,1 %), centro **(535, 703)** = (49,5 %, 36,6 %),
    giro **−0,7°** (anti-horário: topo sobe para a direita). Medido em V04-A15 f1232: 84,6 % × 60,4 %, centro
    (49,5 %, 36,6 %), −0,7° (reconferido com `ferr.py geometria`: bateu, 84,6 % × 60,4 %, centro (49,5, 36,7)).
    A altura vem do formato 4:5 do print (a pintura do V04-A15 tem 609 × 773 = 0,79, praticamente 4:5).
  - Borda de papel **12 px**, cantos retos, #d5d0c8 na área iluminada (escurece com a vinheta; no V04 lê
    #9a8d7a no topo e #71685d nas laterais, medido f1232). Na referência a borda tem 9 px em 720 = 13,5 px
    (medido); o molde global do cartão é 8 px em 720 = 12 px. Área da imagem: 888 × 1110 px (4:5 exato).
  - Sem sombra (no máximo 1 px escuro colado à borda). Fica abaixo de tudo.
- **Câmera, fase 1 (f620–f681):** zoom **+8 %/s** (×1,00325 por quadro) em torno do centro do quadro
  (540, 960), mais deriva do conteúdo **4,8 px/q para baixo e 0,5 px/q para a esquerda**. Medido por registro
  de pontos em V04-A15 f1230–f1279: ×1,031 a ×1,035 a cada 10 q (constante), o ponto central do quadro desce
  29 a 34 px (720) a cada 10 q e anda 3 px para a esquerda; ×1,177 em 49 q no total. A nota dizia "+8 %/s,
  centro descendo de 36,6 para 46,0 %": bateu.
  - Estado no fim da fase 1 (f681), calculado: cartão ×1,223 = 1115 × 1387 px, centro ≈ (504, 1001); sangra
    ≈ 18 px de cada lado. Corta em movimento? Não há corte aqui; a câmera só muda de regime.
- **Peça 2 · cartão do roteiro (P09, V01-A45):**
  - Assentado (f686): caixa externa **867 × 424 px** (80,3 % × 22,1 %), centro **(530, 632)** = (49,1 %, 32,9 %),
    giro **+1,2°** (horário: topo desce para a direita). Caixa: medida da nota (remedida, f3695). Giro: medido
    agora por regressão da borda de cima em 6 colunas (f3681 e f3695: +1,18°; a nota não trazia giro).
  - Borda de papel 12 px #d5d0c8, cantos retos, sem sombra. Área da imagem 843 × 400 px (≈ 2,1:1, horizontal).
  - Fica por cima do cartão da conversa, na metade de cima: o topo e a base do cartão de trás continuam visíveis
    (em f682 o cartão da conversa vai de y ≈ 307 a y ≈ 1694; o roteiro ocupa y 420 a 844).
  - **Estalo (escala em torno do próprio centro + giro), degraus de 2 q:**
    f682–f683: **×1,09** e giro **−1,3°** · f684–f685: **×1,02** e **+0,5°** · f686 em diante: ×1,00 e +1,2°.
    Medido agora em V01-A45 pela largura entre as bordas na linha y300–330: 620 → 582 → 569 px (720), e pela
    inclinação da borda de cima: −1,33° → +0,51° → +1,18°. **A nota está errada nesse ponto** ("631 → 621 →
    622 px": mediu o anúncio de trás); o valor novo bate com o molde do P09 (110 → 103 → 100 %). O centro não se
    desloca (a subida de 15 px da borda de cima em 720 é a própria escala).
  - Depois de assentado acompanha a mesa (está deitado nela): entra na fase 2 da câmera.
- **Câmera, fase 2 (f686 até o empurrão, f724):** zoom **+8 %/s** com âncora no centro do cartão do roteiro
  (530, 632), deriva zero. Inferido: no V01-A45 a foto que caiu fica parada (±2 px f3681–f3695, medido) e o P09
  diz "parado ou com deriva/aproximação leve"; aqui a câmera nunca para, então segue aproximando e para de
  derivar para o roteiro não escorregar. Estado calculado em f724 (×1,15 sobre f686): roteiro 997 × 488 px no
  mesmo centro; conversa ≈ 1283 × 1597 px, centro ≈ (500, 1056), sangra ≈ 100 px de cada lado (sangrar no fim
  do zoom é variação vista: V04-A47, V05-A25, V03-A01).
- **Texto:** nenhum além da legenda global (tarja amarela a 67 % da altura), que passa por cima do cartão da
  conversa.
- **Taxa de imagem:** 24 (23,976) imagens/s; o estalo anda em degraus de 2 q.
- **Som:** nenhum efeito (P06 e P09: nenhum nos 18 casos, medido).
- **Confiança:** caixa, centro e giro do cartão da conversa = medido (V04-A15, reconferido). Zoom e deriva da
  fase 1 = medido (registro de pontos). Caixa do roteiro = medido (nota). Giro e estalo do roteiro = medido
  agora. Âncora e deriva zero na fase 2 = inferido. Formato 4:5 e área de imagem = conteúdo deste vídeo.

## 3 · CONTEÚDO (deste vídeo)

| lacuna (papel) | preenchida com | receita de tratamento |
|---|---|---|
| imagem que mostra literalmente o sujeito da frase ("na mesma conversa") | print real da MESMA conversa do Claude já vista no trecho 5, rolada até mostrar os slides gerados acima e, embaixo, o pedido novo ("crie um roteiro…") | print de tela, recorte retangular 4:5 vertical, cor original, sem filtro, sem recorte de fundo; o pedido novo no terço de baixo do recorte (a legenda cobre a base do cartão); texto legível no tamanho final |
| prova real da frase, caindo por cima ("criar um roteiro") | print real do documento do roteiro que o Claude gerou (Docs), faixa do topo: título + primeiras linhas | print de tela, faixa horizontal ≈ 2,1:1, cor original, sem filtro; o título no terço de cima da faixa; legível em ≈ 1 s |

Regra de escolha: P06 literal (a conversa nomeada); P09 prova documental literal do objeto nomeado no fim da
frase ("roteiro"), entrando na palavra.

## 4 · IMAGENS NECESSÁRIAS

| # | o que é, exatamente | papel | de onde pode vir | formato e tamanho mínimo | tratamento a aplicar |
|---|---|---|---|---|---|
| 12-1 | Print da conversa do Claude (a mesma do trecho 5) com os slides acima e o pedido do roteiro | cartão vertical (P06) | print do próprio Felipe | 4:5, ≥ 1300 × 1625 px (o cartão chega a ×1,41: 1283 px de largura); ideal 1440 × 1800 | recorte 4:5, sem filtro, borda de papel 12 px pelo motor |
| 12-2 | Print do documento do roteiro gerado (título e primeiras linhas) | cartão que cai por cima (P09) | print do próprio Felipe | ≈ 2,1:1, ≥ 1000 × 476 px (chega a ×1,15: 997 px); ideal 2000 × 950 | faixa horizontal, sem filtro, borda 12 px pelo motor |

Nada para baixar da internet neste trecho.

## 5 · Piso de leitura e ritmo

- Cena de tela cheia ≥ 1,5 s: a mesa fica de f620 até o empurrão (f724) = 4,34 s, e segue no trecho 13. OK.
- Conversa sozinha, completa: 2 586 ms (P06: mediana 2 168 ms, faixa 1 293 a 3 629). OK.
- Roteiro por cima: 1 794 ms na tela até o empurrão; assentado 1 585 ms (f686–f724). P09 dá "na tela" 1 167 a
  3 000 ms (mediana 1 646) e "completo até sair" 709 a 1 543 ms: aqui fica **≈ 40 ms acima do máximo medido
  para "completo"**, dentro do limite de 3,0 s. Não há o que mudar sem quebrar a sincronia do trecho 13.
- Imagem de série ≥ 1,2 s: as duas passam.

## 6 · Dúvidas e o que não foi possível medir

- **Mesa:** a vinheta do V04 é bem mais forte que o molde global (V03). Usei a global para o vídeo inteiro ficar
  com uma mesa só; se o motor tiver vinheta por cena, os valores do V04 estão na seção 2.
- **Borda:** 12 px (molde global) contra 13,5 px medidos no V04-A15. Diferença de 1,5 px, deixei o molde.
- **Fase 2 da câmera** (âncora no roteiro, deriva zero) é inferida: a referência do P09 (V01) não tem câmera
  andando por baixo; a do P06 (V04) não tem nada caindo por cima.
- **Tamanho no fim:** com +8 %/s por 4,3 s o cartão da conversa chega a ×1,41 e sangra. A referência V04-A15 durou
  só 2,17 s. Se ficar grande demais no render, a alternativa medida é o zoom lento do P08 (+5 %/s) só na fase 2.
- Não medido: se a foto do V01-A45 tem 1 px de sombra (a nota não diz).
