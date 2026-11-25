# Auditoria r2 · plano_04_05 (trechos 4 e 5, quadros 145–262)
*20/11/2026 · 2ª rodada (corte 04), perfil V03 · arquivo: `05-cenas-r2/plano_04_05.py` · cópia do arquivo de antes no scratchpad do agente*

## 1 · Refs lidas e o que medem de câmera
| Ref | o que mede | uso aqui |
|---|---|---|
| V03-A21 (pilha, lista) | push-in **+6,6 %/s** logo depois do 1º estalo (até ≈ +1043 ms); recuo −7,5 %/s enquanto o 1º item "age"; na lista −5,6 → **−1,4 %/s** ("quase para para o olho contar"); "não fazer: câmera correndo na hora da lista" | fases 1 a 3 da pilha |
| V03-A10 (etiqueta + push-in) | +4,5 %/s enquanto a etiqueta se escreve; depois um **sino de push-in** (+12,9 → **+29,6** → +12,8 %/s) quando a frase segue adiante; ainda ≈ +10 %/s no corte | pico depois de "Design" |
| V04-A08 (print + elipse) | +14,9 %/s no fim do deslize; +8,9 %/s com a foto parada; +4,2 %/s no fim. **"Desaceleração contínua da câmera ao longo da cena (9 → 4 %/s)"**; a elipse anda com a foto (pintada nela), sem pausa medida; deslize ≈ 6 q acelerando + ≈ 10 q assentando | câmera do print, curva do deslize |

## 2 · Tabela da câmera (taxa medida = 100·ln(z2/z1)/Δt)
Palavras: Elas 6110 · Slides 6706 · Docs 7380 · **Design 7860** · dentro 8835 · **chat 9260** (ms).

**Pilha** (âncora (540, 780) + descida 240 → 0 px até q192, iguais ao corte 03):
| fase | quadros | pedida | medida | zoom no fim |
|---|---|---|---|---|
| push-in depois do estalo do cartão SLIDES (A21) | q145–q157 | +6,6 | +6,60 | 1,034 |
| vira na etiqueta SLIDES | q157–q163 | 6,6 → −4 | +1,30 (média) | 1,037 |
| lista, abre devagar (A21 −5,6 → −1,4) | q163–q177 | −4 → −1,4 | −2,70 (média) | 1,021 |
| lista quase parada (A21) | q177–q188 | −1,4 | −1,40 | 1,014 |
| subida, só a partir de "Design" (7860 ms) | q188–q192 | −1,4 → +14 | +1,45 / +10,60 | 1,024 |
| **pico +14 %/s em 7995 ms = q192, "Design" +135 ms** | q192–q194 | +14 | +13,64 | 1,036 |
| freio longo 900 ms até +8 (painel) | q194–q214 | 14 → 8 | +12,5 / +10,9 / +8,9 | 1,132 (q214) |
| +8 por baixo do print | q214–q219 | +8 | +8,00 | 1,151 |
Zoom no 1º quadro 1,000 · em q214 (último com a pilha inteira à vista) 1,132 (corte 03: 1,14 em q212).

**Print** (zoom = 1 no quadro em que assenta, q222; âncora agora (530, 864) = centro da elipse):
| fase | quadros | pedida | medida | zoom no fim |
|---|---|---|---|---|
| deslize (9 q, lento-rápido-lento) com a câmera a +15 → +12 | q213–q222 | 15 → 12 | +13,50 | 1,000 |
| traço da elipse, a câmera segue desacelerando | q223–q231 | 12 → 4,5 | +9,50 / +6,17 | 1,0315 (fecha) |
| depois da elipse, desacelera até o corte | q231–q261 | 4,5 → 2 | +4,13 / +3,33 / +2,46 | 1,0743 (q261) |
O corte (q262) pega a câmera andando (+2 %/s).

## 3 · Quadro seguro e tempo de leitura (geometria das peças + quadros cheios q205 e q261)
- Pilha em q210: cartão SLIDES x 7–939, DOCS x 173–1063, DESIGN y 869–1405; etiquetas inteiras (SLIDES y ≥ 71). Em q213–q214 o canto esquerdo do SLIDES chega a x 0, mas o print já cobre essa área (borda direita do print em 269–296 px). O corte 03 chegava a −5/−6 px no mesmo ponto.
- Etiqueta DESIGN inteira até **q216** (corte 03: q214), porque o deslize agora começa devagar. Fica ≈ 790 ms depois do fim de "Design" (piso 700 ms). A trava `assert` do arquivo continua passando.
- Elipse (alfa da variante final): q231 x 45–1013 · **q261 x 25–1033**, y 660–1061. Inteira até o fim. Com a âncora antiga (648, 864) e a câmera da Ref, a borda esquerda sairia da tela, por isso mudei a âncora e reduzi a taxa depois da elipse.
- A caixa do chat (1062 px de largura ao assentar) já encosta nas bordas com zoom 1. Com qualquer zoom, as pontas dela saem do quadro (q261: print x −93 a 1175). O texto "Digite / para ver as Skills", o microfone e o "+" seguem visíveis. No corte 03 era igual.

## 4 · Acabamento que mudou
- Cartões SLIDES/DOCS/DESIGN: `pecas.cartao` do perfil (borda de papel pontilhada de 12 px, fios escuros, sombra caída `sombra_cartao`). `em_pilha=True` saiu. Cartão sobre cartão mostra sombra.
- Etiquetas: `pecas.com_sombra(etiqueta, 'etiqueta')`. Continuam com grão vivo, porque na A10 a tira de papel ferve.
- Print do chat: cartão do perfil, com borda de 12 px em vez de 13 (o perfil fixa a borda) e sombra. Tamanho total 1180 × 1824, igual ao corte 03.
- Elipse: `sem_grao=True` (traço à mão; sem sombra, como a A08).
- Cena: `base.cena(cam, semente=405)`, mesa do perfil e nenhuma vinheta. O véu branco-escuro do corte 03 sumiu do print.
- Movimento do print: a curva do deslize passou de ease-out para lento-rápido-lento (painel; a A08 acelera no curso e assenta depois). Mesmos quadros q213–q222, mesmo giro −1° → 0°. Durante o deslize o print vem ≈ 5 % menor (a câmera já anda) e chega a 100 % ao assentar.

## 5 · O que ficou igual
Gatilhos, antes e depois: `{"c1": 145, "e1": 162, "c2": 177, "e2": 179, "c3": 188, "e3": 190, "print": 213, "assenta_print": 222, "elipse": 223, "elipse_fecha": 231}`. São idênticos. O traço da elipse começa em q223, com 5 degraus de 2 q até q231. Também ficaram iguais as imagens, as posições e os tamanhos dos cartões e das etiquetas, `ALVO_CHAT`, o tamanho da elipse ao fechar (1000 × 380), a descida da pilha e o corte (145, 262). A folha de passo 4 r2 × corte 03 (`--perfil corte03`) mostra a mesma composição.

## 6 · Painel × Ref
1. **Trecho 5, "para enquanto a elipse é traçada":** a V04-A08 mede uma desaceleração contínua (15 → 9 → 4 %/s), sem pausa, com a elipse pintada na foto. **Valeu a Ref:** a câmera desacelera durante o traço (+9,5 → +6,2 %/s) e não para. Depois segue a ≈ +4 %/s, como pede o painel, mas cai até +2 %/s no corte para a elipse caber.
2. **Trecho 4, lista:** o painel pede +1 %/s e a A21 mede −5,6 → −1,4 %/s. **Valeu a Ref** (−4 → −1,4). As duas dizem "quase parada".
3. **Depois de "Design":** o painel pede "+8 %/s" e a A10 mede um sino de até +29,6 %/s. Fiz um pico de +14 %/s, dentro da faixa +11 a +61, com freio até os +8 do painel. Um pico maior passaria do quadro seguro (DOCS e SLIDES tocam as bordas a partir de ≈ ×1,14).
4. **Recuo de −7,5 %/s da A21** (entre o 1º item e a lista): não entrou. Aqui o 1º cartão já é item da lista, então não sobra um momento de "ação" antes dela.
5. **Descida de 240 px da pilha** (do corte 03): fica. Ela enquadra cada cartão quando entra (composição aprovada), mas anda mais que o pan da A21 (≤ 3 px/q). Esse ponto fica para o principal olhar.

## 7 · O que não consegui conferir
- O som do traço está em q223, e o 1º pixel continua em q223. Não ouvi o resultado: o render com som é do principal.
- O grão vivo no print branco fica forte no quadro cheio. É o perfil; não medi contra a Ref.
- Não abri o strip da A08 para conferir a curva exata do deslize: usei a descrição da nota.
