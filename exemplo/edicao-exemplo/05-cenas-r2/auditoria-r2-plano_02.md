# Auditoria r2 · plano_02 ("três ferramentas de IA totalmente gratuitas")
*20/11/2026 · quadros 25 a 73 (o último pintado é o q72) · perfil V03 · semente 2*

## 1 · O que as Refs medem de câmera
- **V01-A28** (discos; "Câmera (reestudo 20/11)"): com 1 recorte o grupo aproxima **+3,4 %/s**; depois que o 3º entra o
  conjunto **recua −3,5 a −4,2 %/s** (−3,6 no fim, f1906→f1918) e deriva para a direita **+1,07 a +1,65 px/q em 720**
  (+1,45 no fim); vertical +0,05 px/q; giro ≤ 0,15°; mesa parada; sem paralaxe disco × recorte. Sem palavra-chave com pico:
  na palavra do anúncio o grupo sai em cascata. Cadência 12 imagens/s nas peças.
- **V04-A09** (etiqueta): zoom quase constante **+13,1 → +12,2 → +11,5 %/s** a cena toda, conteúdo sobe 1,5–1,7 px/q;
  sem pico; a etiqueta entra em 3–4 q contra esse zoom. A nota diz que a etiqueta **não tem sombra** (é o V04, sem sombras).
- **Painel** (`escolhas-r2.md`, trecho 2): "Repouso de +3 %/s; pico em “gratuitas”, quando a etiqueta cola (+25 %/s com
  freio longo); corta andando."

## 2 · A câmera construída (âncora no centro do conjunto, (525, 786); zoom 1 em q44 = a disposição da spec)
| fase | de → até | taxa pedida | taxa que sai da função | zoom |
|---|---|---|---|---|
| repouso (A28, 1 e 2 recortes) | q25 → q44 (1043–1835 ms) | +3,4 %/s | +3,40 %/s | 0,9734 → 1,0000 |
| vira para recuo | q44 → q46 (2 q) | +3,4 → −3,8 | (rampa) | 1,0000 → 0,9998 |
| recuo (A28, os 3 na mesa; etiqueta entra q51–q56) | q46 → "gratuitas" (1919–2530 ms) | −3,8 %/s | −3,80 %/s | 0,9998 → 0,9769 |
| subida (começa NA palavra) | 2530 → 2665 ms | −3,8 → +25 (média +10,6) | +10,60 %/s | 0,9769 → 0,9910 |
| pico | 2665 ms ≈ q63,9 (q64), 135 ms depois de "gratuitas" (ataque 2530 ms, q60,7) | +25 %/s | +24,94 %/s | 0,991 |
| freio longo (900 ms, para +3,4), cortado no meio | 2665 → 3003 ms (q72) | +25 → +16,3 (média +20,7) | +20,94 %/s | 0,9910 → 1,0636 |
| último passo | q71 → q72 | ≈ +16,6 | +17,39 %/s | corta andando |
- **Zoom no 1º quadro (q25) 0,9734; no último (q72) 1,0636.** Um pico só, na palavra "gratuitas" (q64).
- Pan de tela (pixel 1080): o conjunto desce 1,7 px/q de q33 a q44 (spec trecho-02, A28 f1876→f1900; mantido) e deriva
  para a direita **2,2 px/q** de q44 ao corte (A28 reestudo, 1,45 px/q em 720). Vertical depois de q44: 0.
- Sem desfoque de movimento, sem giro de câmera.

## 3 · O que mudou de acabamento
- Etiqueta GRÁTIS: a sombra feita à mão (`pecas._sombra(a, 0, 3, 1,5, 0,35)` + `_junta`) saiu; entrou
  `pecas.com_sombra(tira, 'etiqueta')` (V03: dy 10, σ 9, 45 %). Medido no q72, coluna x 680: 201 na etiqueta → 129 logo
  abaixo, sobre o disco 3 (−36 %; perfil −33 a −41 %). A borda de papel cortado (alfa irregular de até 1 px em cima e
  embaixo) continua, agora gravada no alfa da própria tira. O papel da tira é o pontilhado do perfil (`pecas.papel`).
- Discos e recortes: acabamento do perfil via `comum_discos.py` (disco do perfil, recorte com contorno ondulado, sombra
  caída), sem mudança no meu arquivo.
- Grão vivo do perfil sobre todas as peças, inclusive a etiqueta (é papel, não texto do editor); `semente=2`.
- Nenhuma vinheta (base.VINHETA = None). A mesa com luz central vem de `base.cena`.
- O crescimento por grupo do corte 03 (grupo 1 +6 %/s, grupos 2 e 3 +2 %/s em torno do próprio disco, até o corte) era
  a câmera feita à mão: saiu (`S = 1`). Agora a câmera única faz esse papel. Em q44 os tamanhos e posições são os da
  tabela da spec (zoom 1, deslocamento 0), iguais aos do corte 03 nesse quadro.

## 4 · O que ficou igual
- Gatilhos, impressos antes e depois, idênticos:
  `{'grupo1': 25, 'grupo2': 29, 'grupo3': 40, 'desce': (33, 44), 'direita': (44, 73), 'etiqueta': (51, 56)}`.
- `nome`, `f0`, `f1`; ordem das camadas; imagens, disposição, tamanhos; pops dos grupos; deslize e giro da etiqueta;
  texto, cor (#ddc5b1 da A09), corpo e posição da etiqueta. Folha do corte 03 × corte 04 (passo 4) conferida lado a lado:
  mesma composição.

## 5 · Painel × Ref
- **Depois que o 3º assenta (q44 → "gratuitas")** o painel pede repouso +3 %/s; a A28 mede **recuo −3,5 a −4,2 %/s**.
  Valeu a Ref: −3,8 %/s.
- **Antes (1 e 2 recortes)**: painel +3, A28 +3,4: valeu a Ref (+3,4).
- **Pico em "gratuitas" (+25 %/s, freio longo)**: nenhuma das Refs mede esse momento com pico (A28 sai em cascata na
  palavra do anúncio; A09 anda a +13 → +11,5 %/s constante). Como a A28 não tem esse momento da fala, valeu o painel.
  Diferença a registrar: na A09 a câmera não acelera quando a etiqueta cola.
- **"Quando a etiqueta cola"**: a etiqueta assenta em q56 (gatilho fixo do corte 03, piso de 700 ms), 195 ms antes de
  "gratuitas"; o pico cai 135 ms depois da palavra (q64), ≈ 330 ms depois de a etiqueta colar.
- **Sombra da etiqueta**: a A09 diz "sem sombra"; o briefing manda a sombra do perfil V03 ('etiqueta'). Valeu o
  briefing (acabamento do perfil).

## 6 · Quadro seguro e tempo de leitura (conferido no q64 e no q72, pixel 1080)
- q72: disco 1 esquerda x 74; topo y 277; **disco 2 passa 16 px da borda direita (x 1096)**: é o palco, o print
  "Design" acaba em x ≈ 1013, inteiro. Disco 3 desce até y 1295 e passa por baixo da tarja (y 1270–1339), como as peças
  da Ref. GRÁTIS: base y 1238 (acima da tarja), direita x 786: inteira e legível. Os três prints inteiros.
- No corte 03 o disco 2 já encostava na borda direita no fim (pan de 2,7 px/q).
- GRÁTIS fica parada (só câmera) de q56 a q72 = 17 q ≈ 709 ms; a câmera não a tira da tela.
- Legenda legível em todas as folhas.

## 7 · Folhas (scratchpad)
- `…/scratchpad/e3-r2/plano_02/folha-corte03.jpg` (corte 03, passo 4) · `folha-r2-v1.jpg` (r2, passo 4) ·
  `folha-r2-pico.jpg` (q57–q73, passo 1) · `q72.png` · `det-etiq-q72.png` (sombra da etiqueta, 3×).

## 8 · O que não conferi
- O movimento em vídeo (sem `--render`): só folhas e a tabela da função.
- As imagens das Refs (strip, detalhes): li só as `notes.md`.
- A cadência de 12 imagens/s que a A28 mede nas peças: o perfil V03 anda a 24 (cadencia_q 1); não mexi.
- A cor da etiqueta: ficou #ddc5b1 (A09, composição aprovada), não a do perfil V03 (#a8a79c). Decisão do principal.
- A descida de 1,7 px/q (q33–q44) vem da spec antiga; o reestudo da A28 não a mede de novo.
