# V05-A49 · rótulo de pessoa + lugar e ano dentro da foto
- Categoria: P04 · Rótulo e número digitados sobre a cena (provisória do analista: (provisória) rótulo de 2 linhas (linha cinza pequena + linha branca) digitado e apagado letra a letra)
- Fonte: V05 quadros f3352–f3412 (139,81–142,31 s; 61 quadros ≈ 2544 ms; f_out corrigido no reestudo de f3410 para f3412) · 23,976 fps
- Fala: "when a teenager in London tried to make (a malaria medicine)"
- Tipo de fala: pessoa
- Gatilho: a linha cinza aparece ≈ f3352 (139 811 ms), 121 ms depois do início da palavra nº 451 "when" (139 690 ms); a linha branca começa a ser digitada em f3355 (139 932 ms; 1ª letra já visível, fraca e desfocada, na folha de 1 em 1; corrigido no reestudo; a remedição dizia f3357 e a 1ª passada f3359), 22 ms depois de "teenager" (#453, 139 910 ms). Conferido com `med.py big` (pixels > 215 na faixa y255–310: 0 em f3358 → 99 em f3359 → 1482 em f3370) e no strip.
- Quadro-chave: f3380
- Camadas ativas: cena de corte (foto, A48) | grafismo (rótulo) | legenda
- Leitura dos strips: strip.jpg = quadros f3350 a f3372, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 23 células. strip-saida.jpg = quadros f3398 a f3412, de 1 em 1, 8 colunas; 15 células. detalhe-rotulo-na-foto.jpg = quadro f3380, região x110 y245 240x65 px, ampliada 3× sem suavizar. Folhas de entrada (f3349–f3372, recorte x115 y250 240x60) e de saída (f3400–f3411, recorte x100 y110 280x70), de 1 em 1, no scratchpad do reestudo.

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala diz "um adolescente em Londres" sem o nome; o rótulo dá o nome, o lugar e o ano por escrito enquanto a voz conta a história.
- Por que este design: 2 linhas de documentário (nome em cinza pequeno, lugar + ano em branco grande) DENTRO da foto, no fundo liso do retrato acima do ombro: o rótulo é a "legenda da foto", e anda com ela.
- Por que estas cores: cinza médio para o nome (informação secundária) e branco para lugar e ano (o que a fala diz).
- Por que estes efeitos: a mesma assinatura de todo texto do editor: cada letra nasce desfocada e foca.
- Por que este movimento: nome primeiro (inteiro, por fade), depois lugar e ano digitados na palavra "teenager"; sai antes dos objetos chegarem, da esquerda para a direita.
- Sensação do movimento: ficha de arquivo sendo preenchida; discreto e rápido, nunca compete com a foto.

## FORMA (fixa: reproduzir igual)
- Design: igual a V05-A10 (linha 1 sans pequena cinza + linha 2 sans bold branca, sem caixa), conferido, mas DENTRO da foto, no canto superior esquerdo do retrato: linha branca x125–330 y274–302 em f3380 (17,4–45,8 % × 21,4–23,6 %), linha cinza logo acima (≈ y258–270, observado). O rótulo anda com a foto (a caixa desliza de x134 para x128 durante o zoom, medido), ou seja, está preso à imagem, não à tela.
- Movimento: linha cinza inteira com fade + foco (f3351 16 % → 28 → 52 → 67 → 85 → f3356 100 %, 6 q, medido na correção pela opacidade integrada com a câmera compensada; o reestudo já dava f3351–f3356). Linha branca digitada da esquerda para a direita f3355–f3370 (16 quadros ≈ 667 ms para 11 caracteres visíveis: ≈ 1,2 caractere novo por quadro na palavra do lugar, f3355–f3359, uma pausa de 3 q na vírgula e no espaço, e 1 algarismo por quadro, f3362–f3365; cada caractere leva 5 a 6 q até 100 %, ≈ +20 %/q: 1º 19 → 38 → 61 → 86 → 100 %, penúltimo 9 → 25 → 45 → 65 → 83 → 99 %) (medido na correção, opacidade integrada de cada letra × fundo de f3349, com cada quadro alinhado ao de referência pela câmera; corrigido na conferência: era ≈ 0,9 caractere por quadro e foco em ≈ 3 q; borda direita x163 → 184 → 203 → 222 → 228 → 241 → 248 → … → 334). Apagamento: a linha cinza some inteira com fade + desfoque em f3403–f3405; a linha branca é apagada da esquerda para a direita, cada letra perdendo opacidade e ganhando desfoque, de f3403 a ≈ f3412 (medido na correção pelo branco que resta no rótulo, que anda com a foto: 98 % em f3403 → 93 → 83 → 78 → 65 → 50 → 36 → 23 → f3411 no piso; o último algarismo ainda aparece fraco em f3411; corrigido no reestudo, folha f3400–f3411; a remedição dizia f3403–f3408 com resto em f3409, lido pelo limiar de branco), durante o movimento de câmera de A48: o rótulo sobe junto com a foto (y274 em f3380 → y141 em f3402), confirmando que está preso à imagem.
- Ritmo: completo e parado f3370–f3401 = 32 quadros ≈ 1,3 s.
- Som: nenhum efeito detectado.

- Textura (reestudo 20/11): texto vetorial liso; fundo = o fundo cinza liso do retrato P&B (V05-A48).
- Efeitos (reestudo 20/11): desfoque por letra na entrada e na saída (≈ 3 px no 1º/último quadro de cada letra; pela folha; o miolo não deu medida limpa porque o rótulo anda com a foto e o alinhamento deixa ±1 px); sombra, caixa, contorno, brilho: nenhum (medido em f3380).
- Câmera (reestudo 20/11): o rótulo é preso à foto (acompanha o zoom e a descida da câmera de A48: sobe de y274 a y141 entre f3380 e f3402, remedição) — diferente de A37, A43 e A45, que ficam fixos na tela.
- Cadência (reestudo 20/11): 24 imagens/s.
- Legenda nesta cena (reestudo 20/11): a legenda amarela continua normal embaixo (3 blocos de 2 a 4 palavras; tarja de 51 px, y 809–859, 68 %) (corrigido na conferência: eram as falas entre aspas); o rótulo diz o lugar ao mesmo tempo que a legenda; ficam a ≈ 40 pontos de distância.
- Entrada do texto (reestudo 20/11), folha f3349–f3372 de 1 em 1:
  - linha cinza (nome): f3351 16 % e desfocada → f3352 28 → f3353 52 → f3354 67 → f3355 85 → f3356 100 % (medido na correção; corrigido na conferência: era ≈ 40–70 % em f3352–f3354); entra inteira (não é digitada); 6 q ≈ 250 ms.
  - linha branca (lugar, ano), remedida na correção caractere a caractere: a palavra do lugar começa em f3355 e as 6 letras começam até f3359 (≈ 1,2 por quadro); a vírgula em f3359; pausa até f3362; os 4 algarismos começam um por quadro de f3362 a f3365; tudo com opacidade cheia em f3370 e nítido em f3372; cada caractere 0 → 100 % em 5 a 6 q (≈ +20 %/q) com desfoque ≈ 3 → 0 px; sem cursor, sem deslocamento próprio (corrigido na conferência: eram ≈ 0,9 caractere por quadro, ≈ 3 q por caractere, e as letras citadas).
  - saída (folha f3400–f3411): a linha cinza some inteira primeiro (f3403–f3405); a branca é apagada da esquerda para a direita, mesma receita invertida, até ≈ f3412.
  - letra (f3380, limiar 200): linha branca maiúscula 24 px (1,9 % da altura), haste 4 px → peso 0,17 (semibold), 0,59 da caixa por caractere, cor #fcfaf6; linha cinza ≈ 14 px de caixa (observado), cor ≈ #8c8986 (cinza médio, medida fraca por ser fina), alinhada à esquerda em x 17,2 %; linha branca à esquerda em x 17,4 %, topo y 21,4 %.

## CONSTRUÇÃO
1. rótulo preso à foto (filho da camada do cartão de A48), no fundo liso do retrato, canto superior esquerdo: x 17,2 %, linha cinza com topo em y 19,7 %, linha branca com topo em y 21,4 % (posições em f3380).
2. linha cinza: sans semibold ≈ 14 px de caixa, #8c8986; fade + foco (desfoque 3 → 0) da linha inteira em 6 q, opacidade 0,16 → 0,28 → 0,52 → 0,67 → 0,85 → 1.
3. linha branca: sans semibold, maiúscula 24 px, #fcfaf6; cascata de ≈ 1,2 caractere por quadro na palavra, pausa de 3 q na vírgula e no espaço, 1 algarismo por quadro no ano; cada caractere opacidade ≈ 0,2 → 0,4 → 0,6 → 0,8 → 1 em 5–6 q com desfoque 3 → 0 px (corrigido na conferência: era ≈ 0,9 caractere/q e 0 → 1 em ≈ 3 q).
4. saída: linha cinza inteira em 3 q (fade + desfoque); linha branca da esquerda para a direita com a cascata invertida (≈ 9 q).
- Linha do tempo (ms a partir do corte de A48, f3316): +1460 linha cinza começa · +1626 1ª letra branca (22 ms depois da palavra que apresenta a pessoa; corrigido na conferência: era a palavra citada) · +2252 rótulo com opacidade cheia (nítido em +2336) · +3629 saída começa (junto da descida da câmera) · +4004 vazio.
- Parâmetros que dependem do conteúdo: nome (linha cinza), lugar + ano (linha branca); o canto da foto que for liso e escuro/médio; nº de caracteres define a duração.
- O que NÃO fazer: fixar o rótulo na tela (aqui ele anda com a foto); caixa ou sombra; digitar a linha cinza; caractere que acende em 3 quadros (leva 5 a 6); deixar até o corte.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "nome da pessoa" (linha 1, pequena); "lugar e ano" (linha 2).
- Nesta referência as lacunas foram preenchidas com: "William Perkin" / "London, 1856".
- Receita de tratamento de cada imagem: sem imagem; texto sobre a foto.
- Regra de escolha: apresentação de pessoa real: quem (linha cinza) + onde e quando (linha branca), entrando quando a fala apresenta a pessoa ("a teenager in London").
- Receita de tratamento (reestudo 20/11): sem imagem; precisa de área lisa e média/escura dentro da foto.
- Teste de generalização: reel sobre Claude Code → sobre o retrato do pesquisador: "Nome do pesquisador" em cinza e "Toronto, 2012" em branco; reel sobre café → sobre o retrato do mercador: "Nome do mercador" e "Santos, 1890".

- Confiança: digitação e posição medidas; linha cinza e apagamento medidos na correção pela opacidade integrada (o miolo não deu medida limpa) (alinhado ao reestudo).
