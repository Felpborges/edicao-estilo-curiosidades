# Trecho 07 (+ 08) · O pedido em tela cheia com marca-texto · P20 (layout B, tela cheia) · Ref V04-A35 (apoio: V04-A40, V01-A42, V02-A12)
Fala: "é só você pedir pra ele aquilo que você quer construir, como por exemplo uma apresentação comercial pro seu negócio. / A partir daí então,"   ·   Janela no clipe: 12.095 a 17.184 ms (f290 a f411; 122 q = 5.089 ms) — o plano ia de 12.136 a 17.244; os dois cortes foram puxados 1 q para antes da 1ª palavra (regra rosto ↔ cena)   ·   Entra por: corte seco (vindo do rosto, trecho 6) · Sai por: corte seco para a parede do trecho 9

Convenções: px de 1080x1920; ms no clipe limpo; (q) = quadros de 23,976 fps (1 q = 41,708 ms); fN = quadro N do
clipe. Palavras pelo índice de `palavras-corte.json`; entre colchetes o ataque reconferido no áudio
(`palavras-ataque.json`) quando difere do whisper. (M) medido · (O) observado · (I) inferido · (NM) não medido.
Este arquivo manda sobre `00-globais.md` onde divergir (curva e cor do marca-texto, vinheta da tela cheia).

## 1 · Linha do tempo da cena (relativa às palavras)
| passo | o que acontece | gatilho (palavra, índice, deslocamento em ms) | duração (ms · quadros) | curva |
|---|---|---|---|---|
| 1 | Corte seco rosto → print do compositor em tela cheia, já no tamanho final, sem estalo | 1 q antes do início de "é" (43): f290 = 12.095 ms = −41 ms (ref: −30 ms do "We", V04-A35) | 0 ms (corte) | — |
| 2 | Push-in contínuo da câmera, do 1º ao último quadro do plano | começa no corte (f290) | 5.089 ms (122 q) até o corte f412 | linear, +2,7 %/s (×1,145 no total) |
| 3 | Nada novo na tela (só o push-in) enquanto ele diz "é só você pedir … como por exemplo uma" | f290 a f356/357 | ≈ 2.795 ms (67 q) | — |
| 4 | Marca-texto 1 varre "apresentação comercial" da esquerda para a direita | −2 ms do início de "apresentação" (58): 1º pixel em f357 (14.890 ms) pelo whisper 14.876 · em f358 (14.932) pelo ataque [14.930] | 500 ms (12 q): f357–f368 (ou f358–f369) | **constante** (curva do V04, tabela na §2) |
| 5 | Marcado 1 completo, espera a fala | fim do passo 4 até o passo 6 | ≈ 540–580 ms (13–14 q) | — |
| 6 | Marca-texto 2 varre "meu negócio" | −2 ms do início de "seu" (61): 1º pixel em f383 (15.974) pelo whisper 15.976 · em f382 (15.933) pelo ataque [15.930] | 250 ms (6 q): f383–f388 (ou f382–f387) | constante |
| 7 | Pedido marcado completo, sem passo novo, câmera ainda empurrando (fim do trecho 7 + todo o trecho 8: "negócio. A partir daí então,") | do fim do passo 6 (≈ 16.183 ms) até o corte | ≈ 1.000 ms (24 q) | push-in segue |
| 8 | Corte seco para a coluna de slides (trecho 9) | 1 q antes de "ele" (67): f412 = 17.184 ms = −60 ms do whisper 17.244 · −41 ms do ataque [17.225] | 0 ms | — |

Respostas diretas:
- **A cena entra em "é" (43)**, 1 q antes (f290), na pausa depois de "fácil," (fim 12.056 ms).
- **Até o marca-texto começar (≈ 2,8 s, f290→f357) a câmera só faz o push-in lento de +2,7 %/s** (×1,08 até
  aí), sem peça nova, sem pan, sem digitação. Isso cabe na faixa medida do P20 "documento antes da 1ª marca"
  (0 a 3,8 s; V04-A40 2,3 s; V02-A10 3,8 s), embora acima da mediana (709 ms). Alternativa NÃO recomendada: o pan
  lateral do V04-A40 (47 q, acelera 10 q, cruzeiro, freia 14 q) antes da marca: a distância do pan nunca foi
  medida em px (NM no guia) e exigiria abrir o print maior que o quadro.

## 2 · FORMA (copiar igual) — px de 1080x1920
- **Fundo / mesa:** fora do print, preto quente: acima do print #0a0a06 (M, f2700 x360 y60) a #020202 nos cantos
  de cima (M, nota). Não há mesa visível: o "papel" ocupa a tela.
- **O print ("página") em tela cheia:** largura 100 % = 1080 px (x 0–1080), altura 85,9 % = 1.649 px, centro
  (540, 975) = (50,0 %, 50,8 %) → topo em y 151, base em y 1.800 (M, nota V04-A35: x0 y100 720x1100). Giro 0° (O,
  still). Cantos vivos; sem borda de cartão, sem sombra (tela cheia). A borda de cima do print fica visível
  (faixa escura de 151 px acima) (O, still). Sem moldura de janela de navegador/sistema (regra P20).
- **Luz/vinheta da tela cheia (sobrepõe o print; manda sobre a vinheta média dos globais):** mancha de luz
  presa à tela, multiplicar, medida em 11 pontos de luminância relativa ao centro no V04-A35 f2700 (M):
  centro (50 %, 46 %) = 1,00 · (50 %, 23 %) = 0,82 · (50 %, 10 %) = 0,50 · (50 %, 78 %) = 0,42 · (50 %, 93 %) =
  0,19 · laterais na altura do centro (6 %, 46 %) = 0,43 e (96 %, 46 %) = 0,35 · cantos de cima (6 %/96 %, 16 %) =
  0,27/0,24 · cantos de baixo (6 %/96 %, 90 %) = 0,15/0,14. Elipse com centro em (540, 883), queda suave
  (smoothstep) (forma I a partir dos pontos M). É forte: o centro do print fica quase branco-creme (#fbf5cb sobre o
  papel da ref) e as bordas ficam marrom-escuras.
- **Texto do print (é o texto REAL do compositor; o editor não digita nada):** escalar o print para que a
  entrelinha do texto do pedido fique em **61 px (3,2 % da altura)** e o corpo em **≈ 34 px** (M na ref: linhas a
  41 px em 720; ≈ 50 caracteres em 600 px). Linha do 1º trecho marcado a **y ≈ 718–756 (37,4–39,4 %)** (M, linha 1
  da ref). Pedido em 2 linhas é igual à ref (linha 1 termina em "comercial", linha 2 começa em "para o meu…"); em 1
  linha também vale (as 2 passadas ficam na mesma linha, como as passadas do V01-A42). Não forçar quebra que a
  interface real não faz. A legenda (P01, y 1266–1336) passa por cima do print, como na ref (O).
- **Câmera:** push-in linear **+2,7 %/s** = ×1,0011 por quadro, de f290 a f411 (×1,145 no total) (M, V04-A35
  ×1,053 de f2666 a f2712 por registro de pontos). Âncora do zoom NM na ref; usar o centro do trecho marcado 1
  (I), para o texto marcado não andar para fora. Não para em nenhum momento; corta ainda em movimento (M).
- **Marca-texto:** cor **#ecc039** (M, V04-A35 f2700; o molde global #efcb3b fica dentro da tolerância), atrás das
  letras (multiplicar, I), opacidade 100 %. Faixa reta de **38 px de altura (2,0 %)** (M: 25 px em 720, remedido
  por mim: y479–504 em f2675–f2684) = 0,61 da entrelinha, centrada na altura das letras; borda levemente
  irregular de caneta (O), ±2 px (I). Largura = exatamente o trecho lido + ≈ 3 px de cada lado (I).
  Sob a vinheta ele escurece junto com o papel (M: #ecc039 no centro → #765e17 a x 89 %).
  - Curva: **a do V04 (quase constante), não a lento-rápido-lento do molde global/D7**, porque a referência
    escolhida é o V04-A35 (o guia registra que a curva varia por vídeo: constante no V04 e no V01, acelera e freia
    no V02). Largura da mancha da linha 1, quadro a quadro, remedida por mim (`ferr.py caixa`, f2664–f2675), em
    fração do comprimento final: **4 · 11 · 19 · 27 · 34 · 44 · 52 · 59 · 69 · 77 · 88 · 100 %** (12 q). Usar
    essa tabela tal como está (1º quadro já com 4 %).
  - Linha 2 (6 q): linear, 1/6 por quadro (nota: "6 quadros, 1º amarelo f2677, completa em f2682"; minha
    remedição com tom mais escuro achou 6 q também, 2 q mais tarde: dentro da folga).
  - Ordem: a passada 2 **espera a fala** (como o V01-A42), em vez de começar 1 q depois da 1ª como na ref: aqui
    "seu negócio" vem 540 ms depois (sincronia manda).
  - O marca-texto nunca sai antes do corte (M, regra P20).
- **Taxa de imagem:** 23,976 imagens/s (push-in e marca-texto andam a cada quadro, M na ref).
- **Som:** nenhum (M na ref).
- Confiança: caixa da página, cor e altura do marca-texto, curva da linha 1, push-in = M; borda irregular,
  multiplicar, âncora do zoom = I/O.

## 3 · CONTEÚDO (deste vídeo)
| lacuna (papel) | preenchida com | receita de tratamento |
|---|---|---|
| a fonte escrita que a fala parafraseia | print real do compositor do Claude (caixa de mensagem) com o pedido digitado e NÃO enviado: "Crie uma apresentação comercial para o meu negócio" | print digital, cor original da interface (creme claro do Claude), tela cheia 1080 × 1649, sem barra de navegador, abas, dock ou bordas de sistema; giro 0°; sem borda, sem sombra; vinheta-spot da §2 por cima; push-in |
| o trecho que a fala lê, passada 1 | "apresentação comercial" (fala: "apresentação comercial", 58–59) | marca-texto #ecc039 atrás do texto |
| o trecho que a fala lê, passada 2 | "meu negócio" (fala: "seu negócio", 61–62; a fala troca "meu" por "seu": é a mesma coisa, marcar o texto real) | idem |
Regra de escolha (P20): instrução/tarefa → o documento-modelo (aqui, o próprio pedido) com o trecho marcado no ritmo da fala.

## 4 · IMAGENS NECESSÁRIAS
| # | o que é, exatamente | papel | de onde pode vir | formato e tamanho mínimo | tratamento a aplicar |
|---|---|---|---|---|---|
| 1 | Print da tela de conversa nova do Claude (claude.ai ou app desktop) com o pedido "Crie uma apresentação comercial para o meu negócio" digitado na caixa de mensagem, sem enviar; enquadrado na região da caixa (com o que houver acima, como a saudação, e abaixo, como os botões da caixa) | documento lido | print do próprio Felipe (é o único jeito de ser real) | PNG, recorte com proporção ≈ 0,655 (1080:1649); resolução tal que o texto do pedido fique com corpo ≈ 34 px **sem ampliar mais que 1,5×** (captura em tela retina 2×, ou zoom do navegador a 150–200 %, para o texto ficar grande em relação à caixa) | recortar sem cromo; não retocar o texto; cor original; vinheta-spot e push-in no motor |

## 5 · Piso de leitura e ritmo
- Cena de tela cheia: 5.089 ms (≥ 1,5 s ✓). P20 na ref: mín 1.960, mediana 3.587, máx 6.875 ms ✓.
- Texto parado depois da última palavra marcada: "negócio." termina em 16.433 ms; corte em 17.184 → **751 ms
  (≥ 700 ✓)**. Marcado completo sem passo novo: ≈ 1.000 ms (ref 1,3 s no V04-A35; mediana P20 709 ms) ✓, com a
  câmera andando ✓.
- Ponto de atenção: 2,8 s de documento antes da 1ª marca (ref mediana 709 ms; máx 3,8 s). Dentro da faixa, mas
  é o trecho mais longo sem passo novo do vídeo. A fala não lê o pedido antes de "apresentação", então não há
  o que marcar antes (regra: nunca marcar trecho que a fala não lê). Solução se o Felipe achar parado: nenhuma
  dentro da forma sem medir o pan do V04-A40; deixar como está.
- Velocidade: a linha 1 da ref tem 265 px em 720 (36,8 % da largura); "apresentação comercial" a 34 px de corpo dá
  ≈ 374–400 px (≈ 35–37 %): mesma velocidade da ref (≈ 33 px/q em 1080) (I, depende do print).

## 6 · Dúvidas e o que não foi possível medir
- Reconferido por mim: (1) altura do marca-texto 25 px em 720 → bate com a nota; (2) duração e curva da linha 1:
  12 q quase constante (nota diz 13 q: diferença de 1 q, dentro da folga); (3) cor #ecc039 no centro e
  escurecimento sob a vinheta → bate. A linha 2 só foi parcialmente remedida (tom escuro sob a vinheta).
- NM: âncora do push-in na ref; forma exata da vinheta (11 pontos, não um mapa); modo de mistura (I).
- O tamanho do texto depende do print real: o motor deve medir a caixa de cada palavra marcada no print já
  escalado e aplicar a regra "largura = trecho + 3 px".
- Divergência com `00-globais.md` (D7): aqui a curva do marca-texto é a constante do V04 (tabela acima), por
  pedido do principal e por ser a da referência escolhida.
- Tempos de palavra: usei whisper e ataque; onde diferem dou os dois quadros. O principal escolhe depois de
  reconferir no áudio.
