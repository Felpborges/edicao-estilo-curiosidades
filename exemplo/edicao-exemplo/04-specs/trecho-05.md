# Trecho 05 · Print do chat em cartão + elipse à mão · P06 + P19 · Ref V04-A08
Fala: "e ficam dentro do chat que você já utiliza."   ·   Janela no clipe: 8218 a 10930 ms (plano); a cena real vai
de q212 (8842,2 ms, 1º quadro do print) até q261 (último quadro; corte em q262 = 10927,6 ms)   ·   Entra por:
movimento (o print desliza da esquerda e cobre a pilha do trecho 04, sem corte)

*Spec escrita em 20/11/2026. Convenções do `00-globais.md` (1080x1920; 1 q = 41,708 ms; giro + = horário; (M)
medido · (O) observado · (I) inferido · (NM) não medido). Onde diverge dos globais, vale este arquivo.
Reconferir no envelope "dentro" (30), "chat" (32) e "E" (37) antes de travar os quadros.
De 8218 a 8842 ms ("e ficam dentro") a pilha do trecho 04 continua na tela: o limite do plano em 8218 não é
evento visual (ver §5, o motivo é o piso da etiqueta DESIGN).*

## 1 · Linha do tempo da cena (relativa às palavras)

| passo | o que acontece | gatilho (palavra, índice, deslocamento em ms) | duração (ms · quadros) | curva |
|---|---|---|---|---|
| 1 | O cartão do print entra pela **esquerda**, borda direita na frente, cobrindo a pilha (que segue com a câmera dela por baixo) | 1º quadro visível **+84 ms** depois de "dentro" (30) → **q212** (8842,2). Ref: +73 ms (M) | cobre a largura toda em q219 (7 q); assenta em **q221** (9217,5); 9 q = 375 ms de movimento | ease-out quadrático (tabela §2) |
| 2 | Zoom lento contínuo do cartão (câmera), até o corte | começa em q221 | q221 → q261 (1710 ms) | linear |
| 3 | **Elipse amarela à mão** se desenha em volta do lugar do chat onde as ferramentas aparecem | 1º pixel **19 ms antes** de "chat" (32) → **q222** (9259,2). Molde P19 −35 ms (mediana −36; metade entre −98 e +44) (M). Ref V04-A08: +67 ms da palavra anterior ao alvo (M) | **375 ms (9 q)**: q222–q230, em 5 degraus de 2 q; completa a partir de q230 (9592,9) | degraus: 25 → 45 → 65 → 85 → 100 % do traço |
| 4 | Elipse completa e parada (só o zoom anda) | q230 → q261 | 1335 ms (32 q) | — |
| 5 | Saída: **corte seco** para o rosto (trecho 06) | **39 ms antes** de "E" (37) → **q262** (10927,6), dentro da pausa 10858–10966 (globais §9: 1 q antes, M) | 0 q | seco |

## 2 · FORMA (copiar igual) — px de 1080x1920

**Fundo / mesa:** a mesa global por trás; só aparece nas faixas de cima e de baixo enquanto o cartão não sangra
(ver abaixo) e, até q218, à direita da borda do print (com a pilha do trecho 04 por cima, ainda no zoom dela).
Vinheta global (`00-globais.md` §1) **por cima do print** (V04-A08: cantos #1e1d19–#2a2622 sobre a foto em f685,
M; força da vinheta sobre um print claro NM).

**Cartão do print** (P06 com a entrada da Ref):
- Tamanho assentado: **1180 × 1824 px** (109 % × 95 % do quadro), borda **13 px #e8e6e0** (≈ 9 px no V04, M; a
  vinheta escurece sozinha, globais §2), cantos retos, giro **0°** assentado, sem sombra além de 1 px.
- Posição assentada (q221): centro **(540, 950)**: x −50 a 1130 (sangra as duas laterais), **y 38 a 1862**.
  Ou seja, a borda de cima fica visível a ≈ 2 % e a de baixo a ≈ 97 % até o zoom tirá-las (O na Ref: borda de
  cima visível em y ≈ 15–25 px de 720 de f679 a f697; borda de baixo de y ≈ 1188 para 1257 de 1280 de f681 a
  f697, com a cena anterior aparecendo embaixo; folha recortada de 1 em 1).
- Altura e largura são forma (95 % de altura; mais largo que o quadro); a proporção 0,647:1 sai daí.
- **Entrada (deslize da esquerda):** só translação horizontal, y fixo. Posição da **borda direita** do cartão
  por quadro (fórmula: x = 240 + 890 · (1 − (1 − k/9)²), k = 0…9):

  | quadro | q212 | q213 | q214 | q215 | q216 | q217 | q218 | q219 | q220 | q221 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | borda direita (px) | 240 | 427 | 592 | 735 | 855 | 954 | 1031 | 1086 | 1119 | 1130 |
  | Ref V04-A08 ×1,5 (O) | 240 | 420 | 585 | 720 | 840 | 972 | 1053 | — | — | — |

  A linha da Ref foi lida por mim na folha de 1 em 1 f675–f681 (±20 px em 720): **bate com o ease-out
  quadrático** nos 7 primeiros quadros. Giro durante o deslize: −1,0° no q212 → 0° no q221, linear (Ref "leve
  giro", O; valor I). Sem borrão (globais §8). 24 imagens/s, uma posição por quadro (M: o perfil muda a cada q).
- **Diferença registrada:** na Ref o deslize não para em 9 q: depois de cobrir o quadro o conteúdo continua
  andando para a direita ≈ 400 px (em 720) com freio, até f691 (17 q no total, ≈ 710 ms; O na folha f680–f695,
  perfil `ferr.py` alto até f691 e base 6–7 a partir de f692, M). Aqui o freio foi encurtado para 9 q porque a
  elipse precisa nascer em "chat" com a imagem já parada (no q222 a imagem da Ref ainda andaria ≈ 70 px/q).
- **Zoom (câmera) depois de assentar:** **+4,3 %/s linear** (s = 1 + 0,043·t, t desde q221), âncora **(648, 864)**
  = (60 %, 45 %). Taxa M (a elipse da Ref cresce de 32,1 para 35,0 % da largura de f727 a f776 = ×1,090 em 2,04 s);
  âncora I (do deslocamento do centro da elipse, 33,8 → 31,4 % e 57,1 → 58,2 %). Até q261: ×1,074. Com isso a
  faixa de mesa de cima some em ≈ q247 e a de baixo em ≈ q253 (I; na Ref a de baixo ainda aparece em f697, M/O).
  Corta em movimento.
- Taxa de imagem: 23,976 imagens/s.

**Elipse (P19 forma (a), Ref V04-A08):**
- **Cor: amarelo-ouro #e0b830** (guia G2, molde "marcação à mão", e G11.1 item 6, "Adotada: (a), amarelo-ouro
  #e0b830"). **Troca registrada:** a Ref V04-A08 usa creme #fff7de (M); a forma (tamanho, espessura, giro,
  duração, degraus, sentido) fica a da Ref, só a cor muda para a cor única de marcação do vídeo. Opaca, sem
  preenchimento, sem sombra, sem brilho. **Atenção:** `00-globais.md` §6 adotou #e8d840 (molde P19, V03) e cita
  #e0b830 como alternativa (D6); o pedido desta spec manda o amarelo-ouro do guia = #e0b830. Unificar nos globais.
- Espessura **12 px** (8 px em 720, M em V04-A08: y632–639 na coluna x260; reconferido no still: ≈ 7–8 px, bate).
  Borda levemente irregular de caneta (O; variação de largura ±1 px, I). Os globais dão 4,5 px (traço do V03);
  aqui vale a Ref.
- Tamanho na hora em que fecha (q230): **347 × 335 px** (32,1 % × 17,4 % do quadro; 231 × 223 px em 720, M,
  remedido). Reconferido no still f776: x ≈ 100–352 · y ≈ 628–861 em 720 = a caixa já crescida pelo zoom da nota
  (35 % × 18,3 %) — **bateu**. Forma: elipse quase redonda (1,04:1 na caixa), **eixo maior inclinado 35–40°
  subindo da esquerda-baixo para a direita-cima** (O). Se o alvo do print for uma faixa horizontal (fileira de
  botões ou linha de menu), alongar a elipse no formato dele mantendo a altura ≥ 1,3 × a do alvo (P19: "no formato
  do detalhe", até 4,5:1 em volta de linha de texto, M); o alvo + folga visível dentro.
- Presa ao print (herda o zoom; cresce ×1,057 de q230 a q261).
- Desenho (trim path), **sentido horário começando na esquerda-baixo** (≈ 8 h no relógio), sobe pela esquerda,
  passa por cima, desce pela direita, volta por baixo e **termina passando um pouco do começo** (as pontas se
  cruzam à esquerda, ≈ 5 % do perímetro, O):

  | quadros | q222–q223 | q224–q225 | q226–q227 | q228–q229 | q230 → |
  |---|---|---|---|---|---|
  | traço desenhado | 25 % | 45 % | 65 % | 85 % | 100 % + cruzamento |

  **Medido por mim nesta passada:** o perfil `ferr.py` da região da elipse tem picos só em f718, f720, f722, f724
  e f726 (8,4 · 11,6 · 7,3 · 8,1 · 6,3 contra base ≈ 6): o traço avança **em degraus de 2 q**, e a folha recortada
  de 1 em 1 (f716–f727) mostra f718 = f719, f720 = f721, f722 = f723, f724 = f725, fechado em f726. A nota dizia
  "¼ no 1º quadro, depois velocidade constante": os 9 q e o ¼ inicial batem; a "velocidade constante" é na verdade
  ≈ 20 % a cada 2 q. Os globais dão ease-out cúbico contínuo de 7 q: aqui vale a Ref.
- Posição: em volta do alvo, onde ele estiver no print. Restrições de tela (na hora em que fecha, q230): centro
  entre **y 770 e 1100** (40–57 %; Ref 57,1 %, M; P19 mediana 35 %), x entre 25 e 75 %, e **base da elipse ≤ y 1200**
  (com o zoom até o corte ela chega a ≈ 1220, acima da tarja que começa em 1266; na Ref a base encosta na tarja no
  fim, ocorrência, M).

**Confiança:** deslize (posições dos 7 primeiros quadros O, curva I ajustada a elas, duração encurtada I); tamanho
e posição do cartão O; taxa de zoom M (indireta), âncora I; elipse: cor do guia, espessura e caixa M, inclinação
e sentido O, degraus de 2 q M (perfil) + O (folha), cruzamento O; gatilhos dentro das faixas M.

## 3 · CONTEÚDO (deste vídeo)

| lacuna (papel) | preenchida com | receita de tratamento |
|---|---|---|
| "imagem do lugar" que a fala nomeia ("dentro do chat") | print real da tela do chat do Claude, a mesma que o espectador já usa | print sem filtro, cor original (tema claro ou escuro, o que o Felipe usa), sem moldura de janela/navegador, recortado em 0,647:1; nítido o bastante para o zoom ×1,07 |
| "o alvo que a fala nomeia" | o ponto da interface onde Slides, Docs e Design aparecem (o seletor/menu das ferramentas, de preferência aberto mostrando os três nomes) | o alvo inteiro visível, com espaço livre em volta para a elipse (P19); grande o bastante para a elipse dar ≈ 32 % da largura; posicionado no recorte para cair entre 40 e 57 % da altura e 25–75 % da largura |
| efeito da consequência / versão depois (V04-A08) | **não usado**: a fala não tem consequência sobre o alvo | — |

Regra de escolha (P19): marca-se o referente literal da palavra dita (onde as ferramentas moram, em "chat"), nunca
enfeite.

## 4 · IMAGENS NECESSÁRIAS

| # | o que é, exatamente | papel | de onde pode vir | formato e tamanho mínimo | tratamento a aplicar |
|---|---|---|---|---|---|
| 4 | Captura da tela do chat do Claude (claude.ai no computador ou app no celular) com o lugar das ferramentas Slides, Docs e Design visível, idealmente com o menu aberto | o lugar + o alvo da elipse | **print do próprio Felipe** (é a prova mais forte e o único jeito de garantir a interface real); alternativa: imagem oficial do anúncio (só com o "sim" dele para baixar) | PNG, recorte vertical 0,647:1, mínimo **1180 × 1824** (mais o zoom ×1,074 → ideal **≥ 1300 × 2010**); desktop em tela retina (recorte vertical em volta da caixa de mensagem) ou celular (recortar para tirar barra de status e teclado) | nenhum além do cartão e da vinheta global; não redesenhar nem limpar a interface; sem dados pessoais visíveis na conversa (conferir antes) |

## 5 · Piso de leitura e ritmo

| peça | tempo | piso | situação |
|---|---|---|---|
| cena de tela cheia (print) | 1º quadro q212 → q261 = **2085 ms**; cobrindo a largura toda q219 → q261 = **1793 ms** | ≥ 1,5 s | ok |
| elipse completa e parada | q230 → q261 = **1335 ms** (Ref: 960 ms, M; P19 mediana 930) | — | ok |
| imagem parada antes da elipse | **1 q** (q221 → q222 = 42 ms) | Ref: 1,54 s (V04-A08); P19 mínimo visto 167 ms (V03-A31) | **abaixo do mínimo visto**. A fala dá 436 ms entre o início do print (q212) e "chat"; o início do print não pode vir antes de q212 sem a etiqueta DESIGN do trecho 04 ficar < 700 ms depois de "Design". Solução adotada: priorizar a sincronia (traço na palavra) e a etiqueta; a imagem já está à vista desde q212 (430 ms antes do traço), só o freio é que termina 1 q antes. Alternativa se o render mostrar "traço junto com a imagem": elipse em q224 (+65 ms de "chat", dentro da faixa P19 −365 a +112, M) |
| pilha do trecho 04 sob o print | segue visível à direita até q218 e nas faixas da mesa até ≈ q253 | — | ok |

Ritmo: 3 eventos em 2,1 s (entrada, elipse, corte) — Ref: 6 eventos em 5,0 s (com os efeitos de consequência que
aqui não existem).

## 6 · Dúvidas e o que não foi possível medir

- **Cor da marcação:** #e0b830 (G2/G11 do guia, pedido desta spec) × #e8d840 (`00-globais.md` §6). Unificar nos
  globais antes de construir; vale para todos os traços à mão do vídeo.
- **Espessura 12 px** em amarelo-ouro é bem mais pesada que os traços amarelos do V03 (3–4 px em 720 = 4,5–6 px). A
  Ref manda 12; se o Felipe achar grosso, a faixa P19 permite 4,5–12 px.
- **Sentido do deslize:** o conteúdo anda para a DIREITA (o cartão vem da esquerda, M na Ref). Os globais §11 listam
  "pan com o conteúdo andando para a direita" como "nunca"; aquilo é pan de câmera, isto é entrada de cartão
  (V04-A08, medido). Mantido pela Ref; a alternativa P10 (cobertura pela direita, 12 q, ease-out) existe se o
  principal quiser uniformizar.
- **Freio encurtado** (9 q contra ≈ 17 q da Ref) e **gap de 1 q** antes da elipse: forçados pela fala (ver §5).
- **O cartão não fica 100 % tela cheia de imediato:** na Ref ele tem ≈ 95 % da altura e as bordas de cima e de baixo
  ficam à mostra por ≥ 16 q (O). Reproduzido. A nota antiga ("100 % × 99,6 % em f685") mediu um bloco claro que
  inclui a faixa da cena anterior; a folha recortada mostra a borda de baixo do cartão em y ≈ 1188–1257 de 1280.
- **Vinheta sobre print claro:** força NM; na Ref a foto é escura. Conferir no render que os cantos do print não
  fiquem brancos chapados (globais D9).
- **Onde ficam as ferramentas na interface do chat:** não sei (depende do print real). As restrições de posição do
  §2 dizem como recortar o print para o alvo cair na zona certa.
- Âncora do zoom (60 %, 45 %) e a queda das faixas de mesa = I. Inclinação da elipse (35–40°) e sentido do traço = O.
- Não medido: a velocidade da Ref depois de f681 em px por quadro com `caixa` (li na folha, ±20 px em 720).
