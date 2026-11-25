# Auditoria r2 · plano_14 · "Então, ao invés de você pagar pelo Gamma ou pelo Canva,"

*2026-11-20 · quadros 789 a 845 · Ref V04-A02 · perfil V03 · semente do grão 14*

## 1 · A Ref lida e o que ela mede de câmera

`<T>/biblioteca/V04-A02 …/notes.md`, blocos "Câmera (reestudo 20/11)", "Cadência", "Sensação do movimento" e CONSTRUÇÃO
item 7: repouso +8 %/s → pico de até +44 %/s no contorno do detalhe → freio → recuo de −10 a −11 %/s até o corte, sem
nenhum quadro parado, sem paralaxe, giro ≤ 0,03°/q, sem desfoque de movimento, 24 imagens/s.

Remedi agora as janelas que a nota não detalha (`ferr2.py camera V04 qa qb --regiao 0,250,400,560`, região do objeto):

| janela Ref | taxa | o que é |
|---|---|---|
| f32–f44 | +8,1 %/s | repouso |
| f100–f112 | +8,5 %/s | fim do freio do empurrão |
| f104–f116 | −2,8 %/s | virada |
| f110–f122 | −11,2 %/s | recuo já instalado (o 1º item comparado entra em f118) |
| f114–f126 | −12,7 %/s | passa do ponto enquanto o 1º item desliza |
| f122–f134 | −10,7 %/s | recuo |
| f130–f142 | −10,4 %/s | recuo; o 2º item comparado entra em f136 |
| f140–f152 | −10,4 %/s | recuo até o corte |

O ponto que fica parado na tela (centro anda ÷ (s − 1)) cai na borda esquerda do objeto do tema, à meia altura dele:
f32–44 em (137, 532) em 720, com a borda do objeto em x 132; no recuo entre x −69 e +75, y 597–652 (lá o objeto
sangra a borda esquerda).

O empurrão forte (+44 %/s) da Ref é do detalhe contornado ("bordas duras"); esta fala não tem detalhe, então ele não
entra (mesma decisão da spec 14 no corte 03).

## 2 · Tabela da câmera (quadros da Ref levados ao 1º quadro do Gamma: f118 ↔ q815)

| fase | quadros | taxa pedida | taxa que sai (100·ln(z2/z1)/Δt) | zoom |
|---|---|---|---|---|
| repouso | q789–q803 | +8,0 %/s | +8,0 %/s | 1,0000 → 1,0478 |
| virada (pára em "pagar", i131, q808) | q803–q808 | +8,0 → −2,8 | +1,4 %/s | 1,0478 → 1,0508 (máx. 1,0530 em q806) |
| virada | q808–q813 | −2,8 → −11,2 | −7,7 %/s | 1,0508 → 1,0341 |
| recuo, passa do ponto (Gamma desliza q815–q821) | q813–q817 / q817–q825 | −11,2 → −12,7 → −10,7 | −11,9 / −11,7 %/s | 1,0341 → 0,9749 |
| recuo (Canva desliza q827–q834) | q825–q833 | −10,7 → −10,4 | −10,5 %/s | 0,9749 → 0,9412 |
| recuo até o corte (corta andando) | q833–q844 | −10,4 | −10,4 %/s | 0,9412 → 0,8973 |

- Zoom no 1º quadro: 1,0000 (q789). No último: 0,8973 (q844).
- **Pico:** nenhum. A taxa máxima de aproximação é o repouso (+8 %/s); o máximo de zoom (×1,053) cai em q806, no começo
  da virada.
- Âncora do zoom: (200, 922) = borda esquerda do maço, à meia altura (o análogo da Ref). Por isso o conteúdo escorrega
  para a direita no repouso e para a esquerda no recuo, sem pan à parte (centro do maço: 511 → 527 em q806 → 479 em q844).
- Sem desfoque de movimento, sem giro de câmera.

## 3 · O que mudou de acabamento

- Mesa do perfil V03 (luz central) parada na tela, grão vivo do perfil (semente 14); nenhuma vinheta por cima (a do
  corte 03 saiu).
- Cédulas: o `recorte_com_sombra` local (sombra feita à mão para contornar o defeito antigo do `pecas.recorte`) saiu.
  Agora: cédula reduzida ao raster 1,15× e `pecas.com_sombra(…, 'recorte')`, com dy/sigma multiplicados por 1,15 para a
  sombra sair na medida do perfil na tela. Sobre a mesa escura ela some, como o perfil manda.
- Logos: `pecas.recorte_do_perfil` (contorno branco ondulado de 16 ± 4 px + sombra do perfil). O raster agora é 1:1 com
  a tela no quadro assentado (antes 1,067× para o contorno de 15 px); a figura é 370 − 2·16 = 338 px e 336 − 32 = 304 px,
  e o total com o contorno continua 370 e 336 px na tela no quadro em que assentam. Sombra visível sobre o papel e sobre
  o logo de baixo.
- Papel creme: `pecas.papel` já sai com o pontilhado fixo do perfil (mantive a fibra lenta de ±3 níveis por cima) e
  ganhou a sombra do perfil tipo 'cartao' (decisão minha: o perfil V03 põe sombra caída em toda peça; o pedido só citava
  o pontilhado). Sobre a mesa escura ela quase não aparece; sobre as cédulas, sim.
- O helper `cv2_blur` virou `cv2.GaussianBlur` direto; o `recorte_com_sombra` saiu do arquivo.

## 4 · O que ficou igual

- `base.CORTES['plano_14']` = (789, 845); dicionário devolvido com as mesmas chaves (`nome`, `f0`, `f1`, `cena`; este plano
  não tinha `gatilhos` no corte 03 e continua sem).
- Gatilhos (impressos antes e depois): Gamma visível em q815 (`de`), assenta em q821; Canva visível em q827, assenta em
  q834. Frações de deslize quadro a quadro, giros (−4°/+6° e +5°/+10°), descidas (−24 e +135 px) iguais.
- Composição no quadro do corte (q789): centros das 3 notas (495,852), (542,931), (505,1005) e do papel (938,789),
  idênticos ao corte 03; logos com 370 e 336 px no quadro assentado. Gamma assenta em (846, 708) (spec: 850, 706;
  corte 03: 883, 679); Canva em (760, 960) (spec: 798, 962; corte 03: 793, 962). A diferença é só da câmera.
- Ordem das camadas: notas → papel → Gamma → Canva.

## 5 · Painel × Ref

- Painel: "Recuo de −10 %/s a cada logo, um por palavra; pico leve em 'Canva'."
- Ref: o 2º item comparado entra no meio do recuo (−10,4 %/s em f130–f142), sem pico. **Valeu a Ref: sem pico em
  "Canva".** O recuo de −10 a −11 %/s durante os dois logos é o do painel e o da Ref.
- Ref × corte 03: o corte 03 virava a câmera a partir do 1º quadro do Gamma; na Ref o recuo já está instalado 2 q antes
  do 1º item (vira entre f106 e f116). Agora a virada vai de q803 a q813 e a câmera passa por zero em "pagar".

## 6 · Conferência visual

- Folha da cena (passo 4): `<scratchpad>/e3-r2/plano_14_15/p14-r2-passo4.jpg`; corte 03 na mesma folha:
  `p14-c03-passo4.jpg`; recuo e entradas dos logos (passo 2, q813–q845): `p14-r2-virada-passo2.jpg`; último quadro
  cheio: `p14-q844.png`. (`<scratchpad>` = `<scratchpad>`)
- Composição igual ao corte 03; sombra do perfil sob os logos e sob o papel; nenhuma vinheta; contorno ondulado visível.
- Quadro seguro: no último quadro (q844) as notas, o papel e os dois logos estão inteiros (nada encosta na borda); legenda
  legível. No máximo do zoom (q806) o papel encosta na borda direita, como no corte (e como o cartão da Ref).
- Tempo de leitura: o recuo não tira nada da tela. Canva continua com ≈ 0,5 s assentado antes do corte (igual ao corte
  03 e à Ref; limite da fala).

## 7 · O que não consegui conferir / para o principal olhar

- Não vi em movimento (nada de `--render`): a virada (q803–q813) só foi vista em folha.
- O papel creme com pontilhado fixo + grão vivo parece lixa na folha reduzida; no quadro cheio lê como papel granulado.
  É o valor do perfil (`papel_fixo` 8), não mexi.
- A sombra 'cartao' no papel é escolha minha (perfil inteiro); se o principal preferir o papel sem sombra, é tirar a
  linha `pap = pecas.com_sombra(...)`.
