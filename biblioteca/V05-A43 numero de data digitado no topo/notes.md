# V05-A43 · número de data digitado no topo da cena
- Categoria: P04 · Rótulo e número digitados sobre a cena (provisória do analista: (provisória) data (número sozinho) digitada sobre a cena, sem rótulo)
- Fonte: V05 quadros f3059–f3111 (127,59–129,76 s; 53 quadros ≈ 2211 ms; f_in corrigido no reestudo de f3063 para f3059) · 23,976 fps
- Fala: "(in) 1204, shattering the snail trade."
- Tipo de fala: data
- Gatilho: o 1º algarismo aparece, fraco e desfocado, em f3059 (127 586 ms), 26 ms depois do início da palavra nº 420 "1204," (127 560 ms) (corrigido no reestudo, folha f3057–f3068 de 1 em 1: f3058 vazio, f3059 "1" fraco; antes "f3063, +187 ms", pelo limiar de branco). Conferido com `med.py big` (pixels brancos > 215: 0 em f3062 → 202 em f3063 → 1242 em f3066).
- Quadro-chave: f3090
- Camadas ativas: b-roll 3D (A42) | grafismo (data) | legenda
- Leitura dos strips: strip.jpg = quadros f3060 a f3070, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 11 células. detalhe-data-letras.jpg = quadro f3090, região x310 y140 140x55 px, ampliada 3× sem suavizar. Folhas f3057–f3061 e f3061–f3068, de 1 em 1, recorte x310 y140 140x55, no scratchpad do reestudo.

## LEITURA DE EDITOR
- Por que esta cena aqui: o ano é dito no meio da frase; escrevê-lo no topo fixa a data sem interromper a narração.
- Por que este design: só o número, sem rótulo, sem caixa, centrado um pouco à direita entre as cabeças dos personagens, no céu da pintura.
- Por que estas cores: branco puro sobre a pintura escura do fundo.
- Por que estes efeitos: foco por algarismo (desfocado → nítido), igual às etiquetas: a mesma assinatura de "texto do editor" em todo o vídeo.
- Por que este movimento: digitação rápida que começa junto com a palavra do ano; fica até o corte.
- Sensação do movimento: carimbo de data que aparece "escrito na hora", rápido e discreto.

## FORMA (fixa: reproduzir igual)
- Design: número em sans semibold branca, sem caixa, sem linha cinza, no TOPO e um pouco à direita do centro: x324–433 y151–183 (15,1 % × 2,5 %; centro x 52,6 %, y 13 %) (medido com `med.py white`). Altura dos algarismos 33–34 px (2,6 % da altura), a mesma dos algarismos de A31 (34 px; os 43 px de A31 contam a vírgula) (alinhado ao reestudo).
- Movimento: digitado da esquerda para a direita, 1 algarismo novo por quadro (o 1º em f3059, o 4º em f3062), cada algarismo nascendo desfocado e transparente e levando 5 q até 100 %: miolo 12 → 28 → 50 → 76 → 98 % (opacidade integrada 16 → 37 → 60 → 79 → 99 %); o número inteiro fica nítido e parado em f3066 (8 q ≈ 334 ms = 4 algarismos + 4 q de foco) (medido na correção, miolo de cada algarismo × fundo de f3058, região x318 y145 125x45; corrigido na conferência: era 3–4 q por algarismo; o intervalo f3059–f3066 do reestudo se confirma). Sem saída: fica até o corte f3112.
- Ritmo: completo e parado f3066–f3111 = 46 quadros ≈ 1,9 s.
- Som: nenhum efeito detectado.

- Textura (reestudo 20/11): texto vetorial liso; fundo = céu escuro da pintura histórica (ver V05-A42).
- Efeitos (reestudo 20/11): desfoque por algarismo na entrada, que dura até o 4º quadro do algarismo (medido na correção: miolo 4 a 10 pontos abaixo da opacidade integrada nos 3 primeiros quadros, 12/16, 28/37, 50/60; nítido no 5º) (corrigido na conferência: era ≈ 3 px só no 1º quadro); sombra, caixa, contorno, brilho: nenhum (medido em f3090).
- Câmera (reestudo 20/11): o número é fixo na tela (não acompanha o push-in da cena: `perfil` na caixa do número cai para 1,0 em f3070 com a câmera ainda andando +1 %/s, resíduo do fundo).
- Cadência (reestudo 20/11): 24 imagens/s (estado novo a cada quadro na entrada).
- Legenda nesta cena (reestudo 20/11): a legenda continua embaixo (o bloco com o ano dito está na tela quando o número entra; tarja de 51 px, y 809–859, 68 %; direta na correção f3060: 65/69 %); número no topo (y 11,8–14,4 %), legenda em y 64–67 %: os dois dizem o mesmo ano ao mesmo tempo.
- Entrada do texto (reestudo 20/11; remedida na correção): ver Movimento (f3059–f3066, 1 algarismo novo por quadro, cada um 0 → 100 % em 5 q, miolo 12 → 28 → 50 → 76 → 98 %, com o desfoque sumindo no 5º quadro; o 4º algarismo 5 → 13 → 27 → 48 → 76 → 98 % de f3061 a f3066; sem deslocamento, sem escala, sem cursor; sem saída: some no corte) (corrigido na conferência: era 0 → 100 % em 3–4 q). Letra (f3090, limiar 200): algarismos 34 px de altura (2,6 % da altura), haste 6 px → peso 0,18 (semibold), 0,81 da altura por algarismo, cor #fdf9f4; posição x324–433 × y151–184, centro x 52,6 %.

## CONSTRUÇÃO
1. número: sans semibold (SF Pro Display Semibold; alt. Inter SemiBold), algarismos 34 px (2,6 %), branco #fdf9f4, centrado em x 52,6 %, topo y 11,8 %; fixo na tela.
2. entrada: cascata de 1 algarismo por quadro (42 ms), cada algarismo opacidade 0,16 → 0,37 → 0,60 → 0,79 → 1 em 5 q (≈ +20 %/q) e desfoque ≈ 3 px que some no 5º quadro; duração = nº de algarismos + 4 q (corrigido na conferência: era 0 → 1 em 3–4 q).
3. sem saída animada: some no corte seco.
4. legenda amarela continua embaixo.
- Linha do tempo (ms a partir do corte de A42, f3012): +1960 1º algarismo (26 ms depois do início do ano dito; corrigido na conferência: era o ano citado) · +2252 número nítido · +4171 corte.
- Parâmetros que dependem do conteúdo: o número (ano); a posição horizontal (entre as cabeças, onde houver céu escuro).
- O que NÃO fazer: pôr rótulo ou caixa; contador animado; digitação seca sem foco; algarismo que acende em 3 quadros (leva 5); deixar o número acompanhar a câmera.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "ano/data dito na fala".
- Nesta referência as lacunas foram preenchidas com: "1204".
- Receita de tratamento de cada imagem: sem imagem.
- Regra de escolha: número dito → número escrito (data falada vira data na tela, logo depois de dita).
- Receita de tratamento (reestudo 20/11): sem imagem; precisa de fundo escuro ou médio no topo.
- Teste de generalização: reel sobre Claude Code → "2022" no topo da cena do lançamento; reel sobre café → "1727" no topo da cena da chegada das mudas.

- Confiança: tempos e geometria medidos.
