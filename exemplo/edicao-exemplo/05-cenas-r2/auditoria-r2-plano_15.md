# Auditoria r2 · plano_15 · "você tem tudo em uma única conversa."

*2026-11-20 · quadros 845 a 888 · Ref V04-A15 · perfil V03 · semente do grão 15*

## 1 · A Ref lida e o que ela mede de câmera

`<T>/biblioteca/V04-A15 …/notes.md`, blocos "Câmera (reestudo 20/11)", "Cadência", "Sensação do movimento" e
CONSTRUÇÃO item 3: zoom +7,7 %/s (f1232→f1244) e +8,7 %/s (f1262→f1274), conteúdo descendo 2,3 → 2,75 px/q (720),
giro 0°: "leve aceleração", sem pico, sem parar, 24 imagens/s, corta andando. "O que NÃO fazer: zoom com curva;
parar a câmera." A descida do cartão (4,8 px/q em 1080) vem da medida por registro de pontos da mesma Ref
(`04-specs/trecho-12.md`: o ponto central desce 29 a 34 px em 720 a cada 10 q) e ficou.

## 2 · Tabela da câmera

Chaves: +7,7 %/s em t0 + 9 q e +8,7 %/s em t0 + 39 q (os centros das duas janelas da Ref, contados do corte),
constante fora delas. `base.zoom_fases` no lugar do `zoom_linear` (que era linear no zoom: +8 %/s no 1º quadro e
≈ +7 %/s no último).

| trecho | quadros | taxa pedida | taxa que sai | zoom |
|---|---|---|---|---|
| começo | q845–q854 | +7,7 | +7,7 %/s | 1,0000 → 1,0293 |
| aceleração leve | q854–q866 | +7,7 → +8,1 | +7,9 %/s | 1,0293 → 1,0708 |
|  | q866–q875 | +8,1 → +8,4 | +8,3 %/s | 1,0708 → 1,1045 |
|  | q875–q884 | +8,4 → +8,7 | +8,5 %/s | 1,1045 → 1,1405 |
| até o corte (corta andando) | q884–q887 | +8,7 | +8,7 %/s | 1,1405 → 1,1530 |
| cena inteira | q845–q887 | ≈ +8 | +8,1 %/s | 1,0000 → 1,1530 (corte 03: 1,1401) |

- Pico: nenhum (pedido do painel e da Ref).
- Âncora do zoom: (500, 700), 40 px à esquerda do centro do cartão (ver quadro seguro). O cartão continua descendo
  4,8 px/q: centro na tela (540, 700) → (543, 808) em q866 → (546, 933) em q887.

## 3 · O que mudou de acabamento

- `pecas.cartao` com o perfil ativo devolve o cartão do perfil: borda de papel pontilhada de 12 px (#d2ccc0 do perfil),
  fio escuro de 1 px por fora e por dentro, sombra do perfil caída para baixo já incluída (RGBA 1042 → 1118 px, centro
  no mesmo lugar). Nenhuma sombra à mão havia neste plano.
- Mesa do perfil V03 (luz central) parada na tela; grão vivo do perfil (semente 15); a vinheta do corte 03 saiu.
- Câmera: `zoom_linear` → `base.zoom_fases` com as taxas da Ref (seção 2).

## 4 · O que ficou igual

- `base.CORTES['plano_15']` = (845, 888); dicionário com as mesmas chaves e `gatilhos` = {'corte_entrada': 845} antes e
  depois. Cartão entra a seco em q845 (`de` = q845).
- Composição: cartão quadrado de 1040 px, centro (540, 700) no corte, giro +0,7°, mesma imagem
  (`print-interface`), mesma descida.

## 5 · Painel × Ref

- Painel: "Aproximação contínua de +8 %/s até o corte, com o cartão descendo: é o fecho, sem pico."
- Ref: +7,7 → +8,7 %/s (leve aceleração), sem pico. **Valeu a Ref**, que só difere do painel em ±0,7 %/s; a média da
  cena dá +8,1 %/s.

## 6 · Quadro seguro e conferência visual

- Com a taxa da Ref e a âncora no centro do cartão, o último quadro chegava a ×1,153 e cortava 7 px a mais do começo
  das linhas da conversa (à esquerda: "Criou", "Montei", "formato" perdiam a 1ª letra). A conversa é o que a fala cita.
  Mudei a âncora para (500, 700): em q887 a borda esquerda corta igual ao corte 03 (as linhas "abri", "vale", "ordem"
  já encostavam lá) e a direita corta 13 px a mais (o último ícone da barra e a 3ª miniatura do carrossel, que já
  estavam cortados no corte 03). Tamanho do cartão não mudou.
- Folhas: cena inteira (passo 4) `<scratchpad>/e3-r2/plano_14_15/p15-r2-passo4.jpg`; corte 03 na mesma folha
  `p15-c03-passo4.jpg`; último quadro `p15-q887.png`; bordas lado a lado (corte 03 à esquerda, r2 à direita; em cima a
  borda esquerda, embaixo a direita) `p15-bordas-c03-vs-r2.jpg`. (`<scratchpad>` =
  `<scratchpad>`)
- Composição igual ao corte 03; borda de papel pontilhada e fio escuro visíveis; sombra caída some na mesa escura;
  nenhuma vinheta; legenda legível sobre o cartão em todos os quadros.

## 7 · O que não consegui conferir / para o principal olhar

- Não vi em movimento (nada de `--render`).
- O grão vivo do perfil cai forte sobre o branco da interface (k 0,045 × luma ≈ 11 níveis no branco): o texto continua
  legível, mas a interface fica granulada como papel. É o perfil; não marquei `sem_grao` porque o print é imagem, não
  texto do editor. Se o principal achar demais, é `sem_grao=True` na peça (a borda de papel perderia o grão junto).
- A descida de 4,8 px/q é da medida antiga por registro de pontos; o reestudo dá 2,3 → 2,75 px/q em 720 (3,5 → 4,1 em
  1080) numa região que também sofre o zoom. Não mexi (muda a composição do fim); fica anotado.
