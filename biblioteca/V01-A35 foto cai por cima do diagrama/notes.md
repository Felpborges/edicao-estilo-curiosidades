# V01-A35 · foto real cai por cima do diagrama (prova no mundo real, por pouco tempo)
- Categoria: P09 · Cartão que cai por cima da cena (provisória do analista: (provisória) foto impressa sobreposta a um diagrama (interrupção curta))
- Fonte: V01 quadros f2491–f2518 (103,79–104,96 s; 28 quadros ≈ 1167 ms) · 24 fps · por cima de V01-A34
- Fala: "So even soaking wet,"
- Tipo de fala: exemplo (a situação real, "mesmo encharcado")
- Gatilho: entra em f2491 = 103792 ms, −48 ms antes da palavra nº 337 "So" (103840 ms).
- Quadro-chave: f2505
- Camadas ativas: b-roll (foto) | cena de tela cheia (diagrama atrás) | legenda
- Leitura dos strips: strip.jpg = quadros f2489 a f2497, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 9 células; cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-canto-borda-sombra.jpg = quadro f2505, região x100 y570 160x110 px, ampliada 3× sem suavizar · detalhe-queda-f2492.jpg = quadro f2492, região x60 y200 600x500 px, ampliada 1× sem suavizar (1º quadro da queda).


## LEITURA DE EDITOR
- Por que esta cena aqui: no meio da explicação abstrata, "mesmo encharcado" pede a prova do mundo real; uma foto viva de alguém dentro da água fria, por pouco mais de 1 s, e de volta ao diagrama.
- Por que este design: foto de borda de papel caída POR CIMA do disco (que continua visível em volta): é um parêntese, não uma troca de cena.
- Por que estas cores: P&B granulado no meio de um diagrama colorido: o contraste de linguagem marca "isto é real".
- Por que estes efeitos: a mesma borda e sombra das outras fotos, para a peça parecer impressa e pousada sobre o diagrama.
- Por que este movimento: estalo com giro (cai torta e endireita) e, por baixo, o conjunto inteiro recua devagar, abrindo espaço para o corte seguinte.
- Sensação do movimento: "olha isso" rápido (167 ms) e passageiro; a imagem dentro da foto se mexe (vídeo), então a peça não fica morta.

## FORMA (fixa: reproduzir igual)
- Design: foto horizontal P&B (a situação real da frase), borda de papel off-white, no centro do disco da estrutura (que continua visível em volta): f2505 x≈124–590, y≈272–632 = 466x360 px (64,7 % · 28,1 %), centro (49,0 %, 35,3 %); no 1º quadro assentado f2496 a borda esquerda está em x≈122 e a cena toda ainda afasta devagar (f2495 x≈112–598 × y≈264–640) (remedido, f2505, varredura na linha y560 e na coluna x360; antes ≈ 70 %, observado; a caixa do med.py pegava o disco de trás: f2495 x7–711, y160–762)
- Movimento: cai com estalo, maior e girada ≈ 4° (f2492, 1º quadro com a foto; f2491 ainda é igual a f2490), assenta em f2496 (borda esquerda x114 → x122): 4 q (remedido); depois acompanha o recuo do conjunto (−2,3 %/s) (alinhado ao reestudo), com o vídeo andando dentro; some SECO em f2519 quando o diagrama de trás troca para V01-A36 (some junto com a troca). Cadência 12 imagens/s. (tempos medido; tamanho medido na remedição f2505 (alinhado ao reestudo))
- Ritmo: 1167 ms, a sobreposição mais curta do vídeo. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Foto: vídeo P&B com grão forte. f2505 região do céu de espuma 160,290,200,60: #a7a5a8, grão 4,13 níveis, manchas 5,78, ac1 +0,60 (grão de 2 px), cinza neutro (4,14/4,13/4,13); VIVA porque é vídeo (o conteúdo muda a cada imagem). O teste novo de grão vivo não separa grão de conteúdo aqui (f2505×f2507: claros 1,47, escuros 1,48, correlação +0,07…+0,11 em todas as faixas = o vídeo muda tudo).
  - Borda de papel: off-white #e7e3d8 embaixo, #d9d3cd–#d7d4cd nos lados, #c9c7c2 em cima; ≈ 6 px.
  - Diagrama de baixo (V01-A34) visível em volta, com o agente de fora e as unidades; parado (teste novo f2505×f2507, região 60,660,600,170: escuros resíduo/σ 0,90, correlação +0,61; claros com poucos pixels, 1,22 / +0,43, sem decisão).
- Efeitos (reestudo 20/11):
  - Sombra da foto sobre o diagrama: curta e fraca dos lados; logo fora da borda o diagrama cai para L74–82 (contra ≈ 85–90 um pouco mais longe em cima). Nos 4 lados (medido, f2505, perfil alinhado): em cima nada (−4 %, 2 px); embaixo o fundo cai para 29–40 logo abaixo da borda contra 43–55 a 20–30 px (≈ −25 a −45 %, volta em ≈ 30 px; sobre as unidades do diagrama, que têm conteúdo: baixa confiança); esquerda e direita não se separam do desenho das unidades. Leitura: a mesma sombra caída para baixo das outras fotos, longa embaixo e nada em cima (corrigido na conferência: era "força ≈ 10–15 %, largura ≈ 10 px" em volta).
  - Desfoque de movimento na queda: nenhum (f2492 nítido, só maior e girado ≈ 4°).
  - Vinheta, brilho, aberração, profundidade: nenhum.
- Câmera (reestudo 20/11): o conjunto de baixo (disco + foto anterior) RECUA: f2496 → f2516 escala ×0,9806 (−2,3 %/s), centro (+0,05, −0,07 px/q), giro −0,05°. Fim da cena (medido, f2504 → f2516, região 0,0,720,830): ×0,9889 (−2,2 %/s), centro (+0,05, +0,36 px/q): o mesmo recuo até a troca. A foto nova assenta e acompanha. Mesa parada.
- Cadência (reestudo 20/11): 12 imagens/s com troca de fase no meio: f2492–f2500 mudam os quadros pares; f2500, f2501 e f2502 são iguais (1 imagem segurada por 3 quadros); de f2503 em diante mudam os ímpares (perfil região da foto: 79,8 / 0 / 19,3 / 0 / 14,6 / 0 / 12,0 / 0 / 11,7 / 0,00 / 0,00 / 11,7 / 0 / 11,4 / 0,09 / 12,2 …). O vídeo dentro da foto também anda a 12.
- Legenda nesta cena (reestudo 20/11): 2 blocos: o 1º (3 palavras) entra em f2490, 2 quadros ANTES da foto cair; o 2º (1 palavra, o estado; f2513–f2520) atravessa a saída (a foto some em f2519 com a troca do diagrama). Texto #eade53, 68 %. Atrás da tarja: a mesa (o disco termina em y≈755). Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #181516, parada.
2. cena de baixo: V01-A34 completa (disco das unidades + agente de fora + foto de trás), parada na textura (sem grão vivo), recuando −2,3 %/s até o fim.
3. sombra da foto: caída para baixo: embaixo ≈ −25 a −45 % no contato, some em ≈ 30 px; dos lados curta e fraca (≈ 10 px, ≈ 10–15 %); em cima nada (corrigido na conferência: era curta e fraca em volta).
4. foto: vídeo P&B horizontal (≈ 4:3) com grão de ≈ 4 níveis, borda de papel off-white ≈ 6 px, centrada sobre o disco: assentada x≈124–590, y≈272–632 (64,7 % × 28,1 %, centro 49,0 % × 35,3 %). Entrada: 0 ms (f2492) maior e girada ≈ 4°, 83 ms intermediária, 167 ms (f2496) assentada e quase reta; o vídeo de dentro corre a 12 imagens/s.
5. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Linha do tempo (ms a partir do 1º quadro da foto, f2492 = 103833 ms): −83 ms 1º bloco de legenda · 0 foto cai · 167 ms assenta · 875 ms 2º bloco (1 palavra) · 1125 ms a foto some SECA junto com a troca do diagrama para V01-A36 (f2519).
- Parâmetros que dependem do conteúdo: a foto (a situação real citada), a proporção.
- O que NÃO fazer: tirar o disco de baixo (ele tem de continuar visível em volta), saída com animação (some seca, junto com a troca), foto parada (é vídeo), foto colorida (aqui contrasta por ser P&B), ficar mais de ≈ 1,2 s.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "a situação real da frase": foto/vídeo literal.
- Nesta referência as lacunas foram preenchidas com: pessoas encharcadas no mar bravo.
- Receita de tratamento de cada imagem: foto/vídeo real P&B, horizontal, borda de papel, ≈ 65 % da largura (alinhado ao reestudo), por cima do diagrama.
- Regra de escolha: no meio de uma explicação em diagrama, quando a fala cita a situação real ("mesmo encharcado"), uma foto literal cai por cima por ~1 s e o diagrama volta já no estado seguinte.
- Teste de generalização: (1) Claude Code: no meio do diagrama de blocos, "mesmo com 200 arquivos abertos" → print de uma IDE cheia de abas por 1 s. (2) café: no meio do diagrama das células, "mesmo com leite fervendo" → foto do leite espumando por 1 s.
- Receita de tratamento (reestudo 20/11): vídeo real P&B neutro com grão de ≈ 4 níveis (2 px), contraste alto (espuma clara, água escura), borda off-white ≈ 6 px, sombra caída para baixo (≈ 30 px embaixo, curta e fraca dos lados, nada em cima) (alinhado ao reestudo); cai torto ≈ 4° e endireita.
- Teste de generalização (reestudo 20/11): (1) Claude Code: "mesmo com o computador desligado" → vídeo P&B de um notebook se fechando cai por cima do diagrama por ≈ 1 s. (2) café: "mesmo depois de uma hora" → vídeo P&B de uma xícara esquecida na mesa cai por cima do diagrama.

- Confiança: tempos, tamanho e posição medido (remedição f2505) (alinhado ao reestudo).
