# Auditoria r2 · plano_07_08 (q290–q412) · pedido em tela cheia com marca-texto
*2026-11-20 · perfil V03 · arquivo: `05-cenas-r2/plano_07_08.py` (corte 03 intocado em `05-cenas/`)*

## 1 · A Ref lida e o que ela mede de câmera
`<T>/biblioteca/V04-A35 pagina de livro com marca-texto/notes.md`:
- "Câmera (reestudo 20/11)": aproximação lenta e centrada, +2,7 %/s (f2666→f2712), deslize 0/−0,1 px/q, giro 0, linear, sem aceleração.
- "Câmera em 3 pares (correção 20/11, medido)": começo f2665→f2671 **+2,0 %/s** (o marca-texto da linha 1 corre de f2664 a ≈f2676, então esta é a câmera DURANTE a varredura); meio f2686→f2692 **+2,1 %/s** (depois das duas varreduras); fim f2707→f2713 **+1,9 %/s**. "Fase única: aproximação linear."
- "Por que este movimento" / "Sensação": página quase parada para dar leitura; o marca-texto corre linear "e a câmera quieta". Sem pico, sem pausa diferente durante a marca, sem borrão.
- Antes da varredura: a Ref não tem esse trecho (a varredura começa no próprio corte). Aqui há 2,8 s de print antes da 1ª marca.

## 2 · Câmera construída (ZoomPorTaxa, âncora no centro do trecho marcado 1, como no corte 03)
Chaves: (q290, +2,7) → (t1 − 250 ms, +2,7) → (q358, +2,0) → (fim da 2ª varredura q388, +2,0) → (q412, +1,9).

| fase | trecho | taxa pedida | taxa que sai (100·ln(z2/z1)/Δt) |
|---|---|---|---|
| repouso antes da marca ("é só você pedir … como por exemplo") | q290–q351 | +2,7 %/s | +2,70 %/s |
| freio para a varredura (rampa 250 ms) | q351–q357 | 2,7 → 2,0 | +2,46 %/s |
| varredura 1 "apresentação comercial" | q358–q369 | +2,0 | +2,00 %/s |
| entre as varreduras | q369–q382 | +2,0 | +2,00 %/s |
| varredura 2 "negócio" | q382–q388 | +2,0 | +2,00 %/s |
| "negócio. A partir daí então," (segue freando) | q388–q411 | 2,0 → 1,9 | +1,95 %/s |
| últimos 6 q | q405–q411 | ≈1,9 | +1,92 %/s |

Zoom: 1,0000 em q290 · 1,1269 em q411 (corte 03: 1,1363, linear em z, +2,61 → +2,38 %/s). **Nenhum pico**: a palavra do pico do painel ("apresentação", i58, ataque 14.930 ms = q358) é exatamente o 1º quadro da varredura 1. Corta andando (+1,9 %/s).

## 3 · Painel × Ref (o que valeu)
- Painel trecho 7: "Quase parada (+0,3 %/s) enquanto o marca-texto varre; pico em 'apresentação comercial' (+20 %/s)". O pico cairia em cima da varredura 1. A Ref mede a câmera quieta (+2,0 %/s) enquanto o marca-texto corre e nenhum pico na cena: **valeu a Ref, sem pico**.
- "+0,3 %/s" na varredura: a Ref mede +2,0 %/s nesse momento (e chama isso de "quase parada"). **Valeu a Ref: +2,0**. Diferença visível mínima (≈ 0,9 % de zoom em 500 ms).
- Antes da marca (Ref silenciosa, painel sem número para esse trecho): repouso +2,7 %/s, o valor da Ref na cena toda (e o do corte 03, já aprovado).
- Painel trecho 8 "segue freando": coincide com a Ref (fim +1,9 %/s); aplicado 2,0 → 1,9.
- Consequência para o agente principal: a câmera desta cena fica quase igual a uma aproximação contínua (2,7 → 2,0 → 1,9). É o que a Ref medida faz ("fase única"), então a regra "nunca zoom igual do 1º ao último" tem aqui a exceção prevista no briefing. Se o Felipe quiser sentir a "parada" na marca, o caminho é baixar a varredura para perto de +0,3 (fora da Ref) ou subir o repouso antes (até +6,7 do V03), e isso é decisão dele.

## 4 · Acabamento que mudou
- Saiu `c.vinheta = spot_tela_cheia(...)` (luz de cena do V04, centro creme e bordas marrom-escuras) e a função/constante `SPOT`. `base.cena` do V03 não põe vinheta por cima. Folha: print claro e uniforme de ponta a ponta.
- Mesa do perfil (faixa escura acima do print, de 151 px no 1º quadro a ≈ 66 px no último) com luz central, parada na tela.
- Grão vivo do perfil sobre o print (semente 7), visível em q411 cheio. Print sem sombra e sem borda (tela cheia, como a Ref "sem borda, sem sombra"; não há sombra feita à mão para trocar).
- Marca-texto: `modo='multiplica'`, sem grão próprio; o grão do papel cai sobre ele (a cobertura do grão vem do print, o modo multiplica não mexe nela), como a Ref: "não tem textura própria, pega a do papel".

## 5 · O que ficou igual
- Cortes q290–q412; print, posição, tamanho; MARCA_1/MARCA_2, cor #ecc039 (do_guia), sementes das faixas, tabelas VARRE_1 (12 q) e VARRE_2 (6 q); âncora da câmera.
- Dicionário `eventos` (a chave deste plano chama `eventos`, não `gatilhos`; não mudei), impresso antes e depois, idêntico:
  `{"corte_entrada": 290, "corte_saida": 412, "marca_1": 358, "marca_1_completa": 369, "marca_2": 382, "marca_2_completa": 387}`.
- Composição conferida lado a lado com o corte 03 (`--cenas 05-cenas --perfil corte03`, q290–q412 passo 4): mesma.

## 6 · Quadro seguro e leitura
- q411 cheio: "Crie uma apresentação comercial para o meu / negócio" inteiro (início "Crie" em x ≈ 48, "meu" termina em x ≈ 990), as duas faixas inteiras, legenda "A partir daí então," legível. Única coisa na borda: a moldura direita da caixa de texto do print encosta em x ≈ 1075 (já era assim no corte 03, com zoom maior).
- Varreduras quadro a quadro (q356–q389, passo 1): faixa 1 começa em q358 e completa em q369; faixa 2 de q382 a q387; nada sai da tela.
- Nada entra e sai rápido: o marcado fica parado de q388 ao corte (≈ 1,0 s).

## 7 · Folhas (scratchpad)
`<scratchpad>`: `folha-r2.jpg` (passo 4), `folha-c03.jpg` (corte 03, passo 4), `folha-varreduras.jpg` (q356–q389, passo 1), `q411.png`, `q370.png`. Todos pela trava `leve.py` (pico ≤ 0,74 GB).

## 8 · O que não conferi
- Vídeo em movimento (sem `--render`): a sensação da troca 2,7 → 2,0 só foi vista em números e folha.
- Intensidade do grão sobre um print quase branco (luma ≈ 245) não foi medida contra a Ref; é o `grao_vivo` do perfil sem ajuste.
- Corte de entrada q290 e saída q412 contra as cenas vizinhas da r2 (só carreguei este plano).
