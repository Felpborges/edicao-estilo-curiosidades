# Auditoria 2ª rodada · plano_12_13 (q619 a q789, trechos 12 e 13)
*2026-11-20 · perfil V03 · arquivo: `05-cenas-r2/plano_12_13.py` (original do corte 03 intacto em `05-cenas/`).*

## 1 · As Refs lidas e o que elas medem de câmera
- **V04-A15** (cartão da conversa, P06): zoom contínuo **+7,7 → +8,7 %/s** (leve aceleração), conteúdo descendo
  **2,3 → 2,75 px/q em 720** (= 3,45 → 4,1 px/q em 1080), giro 0, sem evento. "O que NÃO fazer": zoom com curva, parar a
  câmera. Sem desfoque.
- **V01-A45** (o roteiro que cai, P09), nota corrigida: o cartão que cai fica **quase parado, ≈ +0,9 %/s**, ≈ 1,2 s, e é
  coberto ≈ 1,5 s depois de cair; o movimento de +6,4 %/s era do vídeo de dentro. Cai e assenta em 2 a 3 imagens.
- **V04-A16** (empurrão, P10): empurrão de 15 q sem desfoque de movimento (borda nítida a 56–107 px/q); depois **pan −4 px/q
  em 720 (≈ −6 px/q em 1080) para a esquerda + zoom +3,4 a +3,6 %/s**, constantes; não para depois do empurrão. Durante o
  empurrão o registro de pontos dá −10 %/s e giro −0,49°/q, mas é o movimento das peças, não câmera.
- Nenhuma das três Refs tem pico na palavra.

## 2 · Fases da câmera (o que foi construído) e conferência
Taxa pedida = chave do `base.zoom_fases`; taxa medida = 100·ln(z(t2)/z(t1))/(t2−t1), calculada sobre a função da cena.

| fase | quadros | palavra | taxa pedida | taxa medida | âncora / deriva |
|---|---|---|---|---|---|
| 1 · repouso da conversa | q619 → q682 | "Na mesma conversa … criar um" | +7,7 → +8,7 %/s | q619–625 +7,75 · q676–682 +8,65 | centro da tela; conteúdo desce 3,45 → 4,1 px/q e 0,5 px/q ← (medido: 3,5 px/q em q619–629; 238 px até q682) |
| 2 · freio na queda | q682 → q690 | "roteiro" (q683) | +8,7 → +0,9 %/s em 8 q | q682–690 +4,80 (média); por quadro 8,2 · 7,2 · 6,3 · 5,3 · 4,3 · 3,3 · 2,4 · 1,4 | deriva para nos 4 q do estalo (q682–686); âncora passa ao centro do roteiro (530, 632) em q686 |
| 3 · quase parada | q690 → q726 | "que depois ele consegue" | +0,9 %/s | +0,90 | centro do roteiro, sem deriva |
| 4 · empurrão | q726 → q741 | "transformar" (q728) → assenta em "carrosséis" (q741) | +0,9 → +3,5 %/s | +2,20 (média) | peças do empurrão em posição de TELA (a câmera não pesa) |
| 5 · repouso do maço | q741 → q788 | "em carrosséis no Instagram … material." | +3,5 %/s | +3,50 (1ª e 2ª metade iguais) | pivô (900, 703): o centro do cartão 1 anda 535 → 509 px (≈ 0,55 px/q ←); corta andando |

- Zoom no 1º quadro (q619) ×1,0000; no último (q788) ×1,3873. Marcos: q682 ×1,240 · q686 ×1,255 · q726 ×1,278 · q741 ×1,295.
- **Pico:** nenhum (as três Refs não têm). O único momento "forte" é o empurrão das peças (q727–q741), que não é câmera.
- **Desfoque de movimento:** nenhum (a cena não tinha `borrao`; continua sem).

## 3 · Gatilhos (antes = depois)
`{corte_entrada 619, roteiro_cai 682, roteiro_assenta 686, empurrao_k0 726, empurrao_k1 727, carrossel1_assenta 741,
carrossel2 756, corte_saida 789}`, iguais (antes calculado com as fórmulas do corte 03; depois lido do dicionário). O
dicionário do plano ganhou a chave `gatilhos` (o arquivo do corte 03 não a tinha). Corte de entrada q619 intocado.

## 4 · O que mudou de acabamento
- Os 4 cartões usam o cartão do perfil (borda de papel pontilhada, fio escuro por fora e por dentro, sombra caída do perfil).
  Saiu `em_pilha=True` do cartão 2 (sombra antiga).
- **Escala de raster:** os cartões são rasterizados a K× (conversa 1,5; roteiro 1,25; carrossel 1,167) e desenhados a 1/K.
  `pecas.cartao_do_perfil` não recebe largura de borda, então com K a borda ficaria 12/K px na tela (8 px na conversa) e a
  sombra também encolheria. A cena tem um auxiliar `cartao_k` que, só durante a chamada, multiplica a borda do perfil por K
  (e restaura) e passa a sombra do perfil ×K a `pecas.com_sombra`: na tela ficam 12 px de borda e dy 12 / σ 8 / 56 %.
  Efeito que sobra: o fio de 1 px e o pontilhado ficam 1/K na tela (fio ≈ 0,7–0,9 px).
- Sombra: some sobre a mesa escura (cartão da conversa e carrossel 1 sozinho); aparece embaixo e dos lados do roteiro sobre a
  conversa e do cartão 2 sobre o 1 (conferido em q690 e q788).
- Sem vinheta (a do corte 03 escurecia os cantos e as pontas dos cartões). Mesa do perfil parada, grão vivo com `semente=1213`.
- Câmera: corte 03 = +8 %/s constante até o empurrão (conversa chegava a ×1,41) e +3,4 %/s depois. Agora o freio na queda do
  roteiro deixa a conversa em ×1,28 no empurrão (sangra menos).

## 5 · O que ficou igual
Cortes, gatilhos, ordem e camadas das peças, tamanhos e posições na tela (912 × 1134 em (535, 703) −0,7°; roteiro 867 × 424 em
(530, 632) +1,2° com estalo 1,09/1,02/1,00 e −1,3/+0,5/+1,2°; empurrão P_EMPURRAO e DX_ANTIGO; cartão 2 +54/+38 px, +1,8°,
estalo 1,10/1,03), imagens, deriva da fase 1 em direção. Comparado lado a lado com o corte 03 (`--cenas 05-cenas --perfil
corte03`, mesma folha q619–789 passo 4): mesma composição.

## 6 · Painel × Ref (vale a Ref)
- **Trecho 12, painel "repouso de +3 %/s":** a Ref V04-A15 mede +7,7 a +8,7 %/s com deriva para baixo. Valeu a Ref.
- **Trecho 12, "freia quando o roteiro cai":** bate com V01-A45 (+0,9 %/s depois da queda). Usado; o freio dura 8 q.
- **Trecho 13, "empurrão em carrosséis":** o empurrão é gatilho fixo em "transformar" (q727, k = 1) e assenta em q741, no
  ataque de "carrosséis". Não mudei gatilho.
- **Trecho 13, "repouso de +4 %/s":** a Ref V04-A16 mede +3,4 a +3,6 %/s. Valeu a Ref (+3,5).
- **Pan do V04-A16 (≈ −6 px/q em 1080) não copiado:** em 47 q levaria o maço ≈ 280 px para a esquerda e cortaria o cartão 1
  (quadro seguro). Ficou só o efeito do pivô à direita, ≈ 0,55 px/q para a esquerda.
- Giro de −0,5°/q do cartão novo no empurrão (A16, registro de pontos misturado com a peça que sai): não aplicado; é
  movimento de peça, não câmera, e a spec mediu o empurrão na folha sem giro.

## 7 · Quadro seguro e leitura
- q788 com o pivô no centro do cartão 1 (1ª versão): o canto de cima à direita do cartão 2 saía do quadro (borda + ≈ 8 px da
  imagem). Pivô levado para (900, 703): em q788 o cartão 2 vai até x ≈ 1073 e o cartão 1 começa em x ≈ 12. Tudo inteiro.
- Nos 2 quadros do estalo do cartão 2 (q756–757, ×1,10) a borda direita encosta/sai do quadro: igual ao corte 03, é o estalo.
- O pedido "Agora crie um roteiro…" da conversa fica coberto pelo roteiro a partir de q682 (igual ao corte 03); a conversa fica
  sozinha 2,6 s antes. Legenda legível em todos os quadros vistos.
- Roteiro na tela q682–q739 ≈ 2,4 s; cartão 1 do carrossel no topo q727–q755 ≈ 1,2 s; cartão 2 q756–q788 ≈ 1,4 s.

## 8 · O que não consegui conferir
- Movimento em vídeo (só folhas e quadros; `--render` é do agente principal): a passagem fase 1 → freio → quase parada e a
  troca de pivô em q741 só foram vistas em folha de 1 em 1 e em números.
- Se a quase parada de 1,5 s (q690–q726) sobre um print parado lê como "morta": na V01-A45 o vídeo de dentro andava.
- Folhas: `.../scratchpad/e3-r2/plano_12_13/` (folha-geral.jpg, folha-corte03.jpg, folha-queda.jpg, folha-empurrao.jpg,
  q690.png, q788b.png).
