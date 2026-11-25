# Auditoria 2ª rodada · plano_03 (q73–q145)
*20/11/2026 · trecho 3: "que podem fazer você economizar centenas de dólares por ano." · Ref V01-A43 · perfil V03*

## 1 · A Ref lida e o que ela mede de câmera
`<T>/biblioteca/V01-A43 notas de dinheiro recortadas empilham e saem para a direita/notes.md`, blocos Câmera (reestudo
20/11), Cadência, Sensação e CONSTRUÇÃO.
- Câmera medida: o monte APROXIMA enquanto se forma e até a saída, sem pico: f3510→f3522 +2,6 %/s, f3520→f3530 +2,0 %/s
  ("aproxima e freia até a saída"). Mesa parada. A CONSTRUÇÃO repete: "o monte aproxima +2,6 → +2,0 %/s até a saída" e
  proíbe "monte parado".
- Sensação: "acúmulo rápido e rejeição". O acúmulo vem das 3 batidas das cédulas, não da câmera.
- A Ref não mede nada antes de f3510; lá a nota 1 fica sozinha só 167 ms. Aqui ela fica 1,3 s (q73–q105).
- A saída em cascata da Ref não entra: a cena sai por corte seco (ajuste adotado no corte 03, inalterado).

## 2 · Linha do painel × Ref (o que valeu)
Painel (`03-plano/escolhas-r2.md`, trecho 3): "Repouso de +3 %/s; pico em “centenas” (+30 %/s, freio de 0,9 s); corta andando."
- **Pico em "centenas": NÃO entra.** A Ref medida só deriva (+2,6 → +2,0 %/s) justamente no trecho em que o monte se
  forma; pela regra do briefing a Ref manda onde contradiz o painel.
- **Repouso +3 %/s: vale** para a nota 1 sozinha (q73–q105), momento que a Ref não tem.
- **"Corta andando": vale** (compatível com a Ref): a câmera ainda aproxima +2,0 %/s no último quadro.

## 3 · Tabela da câmera
`base.zoom_fases(t(73), [(t73, 3,0), (t105, 3,0), (t105+2q, 2,6), (t115+6q, 2,6), (t115+15q, 2,0)])`, âncora no centro do
monte (520, 754), sem pan. t115 = monte completo (nota 3 assentada, 4 q depois de entrar, como f3506→f3510 na Ref).

| fase | quadros | taxa pedida | taxa que sai (100·ln(z2/z1)/Δt) |
|---|---|---|---|
| repouso, nota 1 sozinha | q73–q105 | +3,0 %/s (painel) | +3,00 %/s |
| entra a nota 2 ("centenas") | q105–q107 | 3,0 → 2,6 | +2,80 %/s |
| monte se forma | q107–q121 | +2,6 %/s (Ref) | +2,60 %/s |
| freio | q121–q130 | 2,6 → 2,0 (Ref) | +2,30 %/s |
| fim, corta andando | q130–q144 | +2,0 %/s (Ref) | +2,00 %/s |
| conferência: janela da Ref f3510–f3522 ≡ q115–q127 | | +2,6 | +2,50 |
| conferência: janela da Ref f3520–f3530 ≡ q125–q135 | | +2,0 | +2,08 |

Zoom: q73 = 1,000 · q144 (último quadro) = 1,081 (corte 03: 1,089 linear). Pico: nenhum (a Ref não tem).

## 4 · Acabamento (o que mudou)
- Sombra feita à mão (`com_sombra` local, 3 px, 40 %) removida; agora `pecas.com_sombra(rgba, 'recorte')` direto sobre a
  cédula (recorte justo, sem contorno de adesivo): V03 dy 8, σ 11, 43 %. Medido no q144, coluna x380–420, abaixo da nota da
  frente: 23,2 no contato → 31,7 a 30 px (≈ −27 %), volta em ≈ 25 px; no corte 03 era 18,4 → 25,1 em 10 px. Entre as
  notas a sombra quase não aparece: cai para baixo, e a borda de baixo de cada nota está coberta pela nota da frente.
- Mesa do perfil (luz central) e grão vivo de `base.cena(..., semente=3)`. Grão vivo sobre as cédulas: σ passa-alta numa
  área clara da nota 10,2 (corte 03: 8,2), luma igual (173).
- **Grão:** a correção da V01-A43 diz "grão preso ao recorte, sem grão vivo" para o objeto de valor. Seguido o perfil
  do vídeo (V03, grão vivo sobre as imagens), porque o acabamento é um só no reel. Divergência registrada aqui.
- Nenhuma vinheta ou véu por cima (o plano não tinha vinheta própria; `base.VINHETA = None`). Sem borrão.

## 5 · O que ficou igual
- Gatilhos antes e depois: `{'nota1': 73, 'nota2': 105, 'nota3': 111}` (iguais). f0/f1 73–145, nome, ordem e z das peças.
- Composição: NOTAS (posições e giros), CENTRO_MONTE, estalos de entrada (`cd.pop`), imagem `nota-100`. Folha passo 4
  r2 × corte 03 (`--cenas 05-cenas --perfil corte03`) lado a lado: mesma composição quadro a quadro.

## 6 · Quadro seguro e leitura
- Fim (q144) e momento de "centenas" (q105–q120, passo 1): as três cédulas e os "100" seguem legíveis; legenda legível.
  Não há pico, então não há fim de pico a conferir.
- **Para o agente principal:** as cédulas saem pelas DUAS laterais desde o 1º quadro. Causa: `ctx.rgba` devolve a imagem
  real no tamanho nativo (`nota-100.png` = 1200×505) e ignora `NOTA = (735, 312)` da spec; o monte fica ≈ 63 % maior que
  o da spec (x108–932) e que o da Ref (que cabe no quadro). Já era assim no corte 03 aprovado; não mexi (composição
  fixa). A câmera nova aproxima menos (×1,081 contra ×1,089), então não piora.

## 7 · O que não consegui conferir
- Movimento em velocidade real (sem `--render`, por regra): só folhas de quadros.
- O grão vivo trocando quadro a quadro não foi medido aqui (confiado ao motor; a folha mostra o pontilhado nas notas).

Arquivos de conferência (scratchpad): `folha-r2.jpg`, `folha-corte03.jpg`, `folha-r2-monte.jpg`, `q144.png`,
`q144-corte03.png`, `crop-sombra.png`, `crop-baixo.png` em
`<scratchpad>`.
