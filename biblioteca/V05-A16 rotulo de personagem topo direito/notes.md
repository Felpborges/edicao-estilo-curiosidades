# V05-A16 · rótulo de personagem no canto superior direito
- Categoria: P04 · Rótulo e número digitados sobre a cena (provisória do analista: (provisória) rótulo de 2 linhas (linha cinza pequena + nome branco) digitado e apagado letra a letra)
- Fonte: V05 quadros f1016–f1053 (42,38–43,92 s; 38 quadros ≈ 1585 ms) · 23,976 fps
- Fala: "(It came) from a spiny sea snail called (the murex)."
- Tipo de fala: pessoa (quem é o personagem e de onde)
- Gatilho: a linha pequena aparece em f1016 (42 374 ms), 26 ms antes do início da palavra nº 154 "from" (42 400 ms) e 6 quadros depois do corte. Conferido no strip (f1016 linha cinza fraca) e com `med.py big` (o nome branco começa a ter pixels em f1020–f1021).
- Quadro-chave: f1030
- Camadas ativas: b-roll 3D (A15) | grafismo (rótulo) | legenda
- Leitura dos strips: strip.jpg = quadros f1014 a f1026, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 13 células. strip-saida.jpg = quadros f1048 a f1055, de 1 em 1, 8 colunas; 8 células. detalhe-rotulo.jpg = quadro f1030, região x515 y140 140x85 px, ampliada 3× sem suavizar (sobretítulo cinza e nome branco sobre o fundo escuro desfocado).

## LEITURA DE EDITOR
- Por que esta cena aqui: o personagem acabou de aparecer; o rótulo diz o ofício e o lugar dele, como crédito de entrevistado em documentário.
- Por que este design: o mesmo molde do rótulo de lugar (A10), agora no canto superior DIREITO, porque o lado esquerdo está ocupado pela mão com o objeto; sobretítulo = ofício, nome = cidade.
- Por que estas cores: nome branco #fff9f4 e sobretítulo cinza sólido #928a84 sobre o fundo sépia escuro: dois níveis de leitura sem caixa.
- Por que estes efeitos: nenhum; o fundo escuro e desfocado dá o contraste.
- Por que este movimento: sobretítulo acende inteiro, nome digitado com onda de fade e desfoque, apaga da esquerda para a direita 1 quadro antes de o objeto saltar para a câmera, abrindo espaço.
- Sensação do movimento: crédito discreto que se escreve e se apaga; produzida pelo fade de 5 q da linha 1, 1 letra nova por quadro na linha 2 com fade de 5 q por letra (≈ +21 %/q), e saída de 4 q (corrigido na conferência: era fade de 3–4 q por letra e saída de 3 q).

## FORMA (fixa: reproduzir igual)
- Design: igual a V05-A10 (linha 1 sans pequena cinza + linha 2 sans bold branca, sem caixa), mas no canto SUPERIOR DIREITO: alinhado à esquerda em x528 (73,3 % da largura); nome branco x528–606 y179–214 (10,8 % × 2,7 %; centro x 78,8 %, y 15,4 %) (medido com `med.py white`, limiar 215); linha cinza logo acima, x528–634 y150–166 (medido, remedição f1030, `caixa --cor #8a8a8a --tol 25`; antes "≈ y160–172, observado"). A altura (y179–214) é a mesma de A10 (y181–211): os rótulos ficam sempre na faixa de 14–17 % da altura; o lado (esquerdo ou direito) muda para não cobrir o personagem (inferido).
- Movimento: linha 1 com fade de ≈ 5 q, todas as letras juntas (f1015–f1019) (alinhado ao reestudo). Nome digitado: as 2 primeiras letras já aparecem fracas e borradas em f1017 (folha recortada f1014–f1025; a contagem por limiar de branco só pega a partir de f1020: 8 (f1020) → 184 (f1021) → 387 (f1022) → 495 (f1023) → 732 (f1024, completo)) = 8 quadros para 4 letras, cada letra com fade e desfoque (remedido; antes "5 quadros", que contava só os pixels acima do limiar). Permanência f1024–f1050. Saída apagando da esquerda para a direita: 732 (f1050) → 421 (f1051, caixa começa em x552) → 233 (f1052, x575) → 0 (f1053) = 3 quadros pela contagem de pixels claros (medido); por letra (miolo × fundo local) a 1ª vai 100 → 71 → 38 → 13 → 0 (f1050–f1054) e a 4ª 95 → 56 → 19 → 0 (f1052–f1055): a saída leva 4 q (f1051–f1054) e o último traço some em f1055 (corrigido na correção: era 3 q, vazio em f1053).
- Ritmo: completo e parado 27 quadros ≈ 1126 ms; termina de sair no 1º quadro do salto do objeto (A17 começa em f1054; o nome fica vazio em f1055), abrindo espaço (corrigido na correção: era 1 q antes do salto).
- Som: nenhum efeito detectado.
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11): letras chapadas (liso); fundo atrás = foto de praia em sépia desfocada (A15, grão 2,9, luma ≈ 20–70). Detalhe f1030: borda limpa, sem contorno.
- Efeitos (reestudo 20/11): nenhum (sem caixa, sem sombra, sem brilho; medido em f1030 e visto no detalhe).
- Câmera (reestudo 20/11): rótulo fixo na tela; a cena atrás está parada (A15: ×1,0015).
- Cadência (reestudo 20/11): 24 imagens/s (a borda direita do nome avança em todos os quadros f1020–f1023).
- Legenda nesta cena (reestudo 20/11): legenda amarela ligada embaixo (2 blocos: 4 palavras f1021–f1046; o nome do objeto com o artigo f1047–f1073); o rótulo dá ofício e cidade, que a fala não diz; sem conflito de espaço (rótulo y150–214, legenda y821–855). Tarja 66 % (f1030).
- Entrada do texto (reestudo 20/11):
  - Sobretítulo (inteiro): p98 na caixa f1014 71 · f1015 79 · f1016 91 · f1017 102 · f1018 114 · f1019 140 (completo): fade de ≈ 5 q (f1015–f1019, 208 ms); por letra (média de 10 letras, miolo × fundo local) f1014 ≈ 8 · f1015 26 · f1016 47 · f1017 63 · f1018 80 · f1019 100 %, todas juntas (medido na correção); quase igual ao de A10, que remedido dá 6 q (corrigido na correção: era "mais longo que o de A10 (4 q)"). Cor final #928a84 sobre fundo de luma ≈ 20: como em A10 (#8a8a8a sobre fundo de luma ≈ 99) o cinza fica ≈ igual com fundos diferentes, então é CINZA SÓLIDO, não branco translúcido (medido nos dois rótulos).
  - Nome (digitado): p98 f1017 108 · f1018 140 · f1019 177 · f1020 212 · f1021 243 (1ª letra em fade de 4–5 q); borda direita f1020 x549 · f1021 570 · f1022 585 · f1023 606 · f1024 607 (completo): 1 letra nova por quadro (4 letras), cada uma com fade e desfoque de 5 q: 1ª f1017 16 · 30 · 53 · 80 · 101 (f1021); 2ª f1018 8 · 27 · 53 · 77 · 99 (f1022); 3ª f1019 6 · 25 · 50 · 76 · 96 (f1023); 4ª f1019 4 · 13 · 22 · 45 · 76 · 101 (f1024) (medido na correção: miolo de cada letra × anel de fundo local no mesmo quadro, com a máscara da letra tirada do quadro completo); corrigido na conferência: era 3–4 q por letra; total f1017–f1024 = 8 q (confirma a remedição).
  - Saída: nome f1051 669 px claros · f1052 356 (borda esquerda x554) · f1053 1 · f1054 0 (apaga da esquerda para a direita em 3 q); sobretítulo f1051 217 · f1052 6 · f1053 0 (2 q). Total 3 q (125 ms) pela contagem de pixels claros; por letra o nome leva 4 q (f1051–f1054: 1ª 71 → 38 → 13 → 0; a 4ª ainda 19 % em f1054 e 0 em f1055), ≈ 1 letra apagando por quadro (corrigido na correção).
  - Letra (f1030): nome sans bold, haste 5 px (≈ 0,28 da altura-x, como A10), cor #fff9f4; sobretítulo sans semibold pequena, maiúscula ≈ 12 px (y151–163), haste 2 px, cor #928a84. Margem: x528 (73,3 %); entrelinha topo a topo ≈ 28 px (151 → 179).

## CONSTRUÇÃO
1. (cena A15 por baixo, parada.)
2. sobretítulo: sans semibold, maiúscula 12 px, cinza sólido #8e8a86, alinhado à esquerda em x528 (73,3 %), topo y151 (11,8 %).
3. nome: sans bold, maiúscula ≈ 24 px, altura-x ≈ 18 px, branco #fff9f4, alinhado em x528, topo y179 (14 %); sem caixa, sem sombra.
4. regra do lado: rótulo no canto superior do lado OPOSTO ao do objeto/gesto do personagem (aqui o objeto está à esquerda → rótulo à direita), sempre alinhado à esquerda e na faixa de 12–17 % da altura.
5. animação (ms a partir do corte da cena f1010): 208 ms sobretítulo começa (fade 5 q, ≈ 26 → 47 → 63 → 80 → 100 %, todas as letras juntas); 292 ms nome começa (1 letra nova por quadro, cada letra 16 → 30 → 53 → 80 → 100 % em 5 q, com desfoque), completo em 584 ms; parado até 1709 ms; 1709 ms apaga da esquerda para a direita, cada letra 100 → 71 → 38 → 13 → 0 em 4 q, 1 letra por quadro; vazio em 1877 ms, no 2º quadro do salto do objeto (A17) (corrigido na conferência: era fade de 3–4 q por letra, saída de 3 q e vazio 1 q antes do salto).
- Linha do tempo (ms a partir de f1010): 208 sobretítulo · 292–584 nome · 584–1709 parado · 1709–1877 saída · 1835 objeto começa a saltar (o último traço do nome some 1 q depois) (corrigido na correção: era saída até 1835).
- Parâmetros que dependem do conteúdo: o texto (ofício/papel; nome do lugar ou pessoa) e o lado.
- O que NÃO fazer: não usar branco translúcido no sobretítulo (é cinza sólido); não deixar o rótulo quando outro elemento grande vai entrar; não alinhar à direita no canto direito (é alinhado à esquerda a partir de x 73 %).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "papel/ofício do personagem" (linha 1); "lugar de onde ele é" (linha 2).
- Nesta referência as lacunas foram preenchidas com: "Purple dyer" / "Tyre".
- Receita de tratamento de cada imagem: sem imagem; texto puro.
- Regra de escolha: apresentação de personagem. 1º plano de um personagem novo ganha rótulo de documentário (quem é + de onde), mesmo sem a fala dizer.

- Teste de generalização: reel sobre Claude Code: personagem de engenheiro → sobretítulo "Engenheira de software", nome "Anthropic". Reel sobre café: personagem de pastor → sobretítulo "Pastor de cabras", nome "Kaffa".

- Confiança: tempos e posição do nome medidos; linha cinza medida por cor na remedição de f1030 (não passa no limiar de branco) (alinhado ao reestudo).
