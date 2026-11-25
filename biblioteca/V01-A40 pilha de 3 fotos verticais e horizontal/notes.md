# V01-A40 · pilha de 3 fotos (2 verticais + 1 vídeo horizontal) para "o que aconteceu depois"
- Categoria: P08 · Pilha de cartões (provisória do analista: (provisória) pilha de fotos impressas (montagem por empilhamento))
- Fonte: V01 quadros f2965–f3093 (123,54–128,88 s; 129 quadros ≈ 5375 ms) · 24 fps
- Fala: "By 1953, he'd even designed one for his daughter. So the Navy loved it, right?"
- Tipo de fala: data + pergunta ("então a instituição adorou, certo?")
- Gatilho: corte seco em f2965 = 123542 ms, −108 ms antes da palavra nº 408 "By" (123650 ms). Foto 2 em f2997 = 124875 ms, +35 ms depois da nº 411 "even" (124840 ms). Foto 3 em f3041 = 126708 ms, −22 ms antes da nº 417 "So" (126730 ms).
- Quadro-chave: f3060
- Camadas ativas: cena de tela cheia | legenda | b-roll (fotos e vídeo)
- Leitura dos strips: strip.jpg = quadros f2963 a f2972, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 10 células. strip-saida.jpg = quadros f3039 a f3048 (entrada da foto 3), mesma regra, 10 células. strip-geral.jpg = quadros f2963 a f3095, de 3 em 3, 45 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-pilha-bordas-sombra.jpg = quadro f3060, região x560 y640 110x220 px, ampliada 3× sem suavizar · detalhe-foto-colorida.jpg = quadro f2985, região x120 y150 240x200 px, ampliada 2× sem suavizar.


## LEITURA DE EDITOR
- Por que esta cena aqui: três fatos em sequência (a data, o caso pessoal, a instituição) viram três fotos que se empilham, uma por meia-frase; a última é a instituição, para a pergunta "adorou, certo?" ter um alvo antes da virada no rosto.
- Por que este design: pilha de fotos de época com giros alternados, duas verticais e uma horizontal por cima: álbum de recortes; cada foto nova cobre a anterior sem apagá-la.
- Por que estas cores: a 1ª foto é colorida saturada (azul de época), as outras P&B: a cor marca a 1ª prova e o P&B devolve ao "arquivo".
- Por que estes efeitos: borda de papel e sombra forte para baixo de cada foto sobre a de baixo: profundidade de pilha física.
- Por que este movimento: estalo de 4 quadros em cada foto, na palavra; a pilha inteira aproxima devagar o tempo todo.
- Sensação do movimento: "tum, tum, tum" de álbum sendo montado, com respiração lenta entre batidas; a pergunta fica no ar e o corte para o rosto responde.

## FORMA (fixa: reproduzir igual)
- Igual a V01-A12/A17 na forma (borda de papel, cada foto nova cai por cima com estalo de 3 imagens (2 em movimento + a assentada = 4 q), giros alternados). Medidas próprias (med.py/inc.py):
  - Foto 1 VERTICAL colorida (tons azuis saturados; o produto em uso, na época): assentada f2969 x108–590, y129–808 = 483x680 px (67,1 % da largura, 53,1 % da altura), centro (48,5 %, 36,6 %); giro ≈ 1,8° anti-horário.
  - Foto 2 VERTICAL P&B (o caso pessoal citado), quase do mesmo tamanho, por cima e um pouco à direita: conjunto f3001 x98–634, y119–834.
  - Foto 3 HORIZONTAL (vídeo P&B da instituição que vai reagir, em movimento), cai por cima no meio, mais larga: conjunto f3045 x62–645, y128–838; a foto 3 sozinha em f3060 vai de x58–652, y≈247–692 = 594x445 px (82,5 % · 34,8 %), centro (49,6 %, 36,7 %) (medido, remedição f3060); as verticais aparecem acima e abaixo dela.
- Movimento:
  - Foto 1: altura f2965 759 (112 %) → f2967 704 (103,5 %) → f2969 680 (100 %). Estalo. (medido)
  - Foto 2: conjunto f2997 558x764 → f2999 539x724 → f3001 537x716. (medido)
  - Foto 3: largura do conjunto f3041 635 → f3043 595 → f3045 584 (109 → 102 → 100 %). (medido)
  - Pilha cresce devagar até 618x752 em f3090. Cadência 12 imagens/s. (medido)
  - Saída: corte seco para o A-roll em f3094. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | foto 1 vertical colorida | f2965 | 4 q (167 ms) (remedido, assenta f2969) | escala 112 → 100 % | estalo | nº 408 | −108 ms |
  | foto 2 vertical P&B | f2997 | 4 q (167 ms) (remedido, assenta f3001) | escala 107 → 100 % | estalo | nº 411 | +35 ms |
  | foto 3 vídeo horizontal | f3041 | 4 q (167 ms) (remedido, assenta f3045) | escala 109 → 100 % | estalo | nº 417 | −22 ms |
- Ritmo: foto 1 no topo 32 q (1333 ms); foto 2 44 q (1833 ms); foto 3 53 q (2208 ms). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Foto 1 (colorida): fotografia de época com cor saturada, f2985 região 200,250,150,100: #294686 (azul profundo), grão 9,96 (inclui conteúdo), manchas 23,0, ac1 +0,70, grão levemente colorido (9,57/10,00/10,02); PARADA (+0,97): foto estática. Teste novo (f2985×f2987, afim da foto, pixels lisos; par idêntico f2985×f2986: 0,04): claros resíduo/σ 0,90, correlação +0,56; escuros 0,89, +0,63: sem a diferença claros × escuros das fotos P&B; quase parada (mesmo veredito, com ressalva: uma parte pequena do grão troca nas duas faixas).
  - Foto 2 (P&B vertical): teste novo (f3020×f3021/f3022, afim da pilha): claros resíduo/σ 0,72–0,74, correlação +0,70…+0,72; escuros 0,43–0,50, +0,87…+0,90 → PARADA (sem grão vivo nos claros nesta foto).
  - Foto 3 (vídeo P&B): céu #929093, grão 1,66 níveis, manchas 6,31, ac1 +0,60, cinza puro; VIVA (vídeo).
  - Bordas: off-white #e6e2da (embaixo) e #c5c4be (em cima), ≈ 6–8 px, cantos retos.
- Efeitos (reestudo 20/11):
  - Sombra da foto 3 sobre a foto 2 (f3060, sombra4): embaixo forte, 225 (borda) → 46 a +5 px → 97 a +30 px (≈ −50 %, ≈ 25 px); em cima fraca (141 → 134 → 155, ≈ −12 %). Lados (medido, f3060, perfil alinhado, 148 linhas cada, sobre a mesa): à esquerda −27 % no contato, volta em 10 px; à direita −41 %, volta em 9 px. Sombra deslocada para BAIXO, difusa, média dos lados.
  - Desfoque: o borrão que se vê no barco é do vídeo original (não aplicado). Vinheta, aberração, brilho: nenhum.
- Câmera (reestudo 20/11): a pilha aproxima de forma quase constante: f2971 → f2985 escala ×1,0194 (+3,3 %/s), centro (+0,22, +0,23 px/q); f3003 → f3017 ×1,0118 (+2,0 %/s), centro (−0,28, +0,13 px/q); giro 0,0°. Fim da cena (medido, f3079 → f3091, região 0,0,720,830): ×1,0095 (+1,9 %/s), centro (−0,09, +0,12 px/q): o mesmo ritmo até o corte, sem recuo. Mesa parada (≤ 0,27 por quadro).
- Cadência (reestudo 20/11): 12 imagens/s nas fotos e no vídeo da foto 3 (perfil f3045–f3060: 21,1 / 0,00 / 14,3 / 0,15 / 12,5 / 0,01 / 14,1 / 0,00 / 11,4 …, fase ímpar).
- Legenda nesta cena (reestudo 20/11): 7 blocos (2, 2, 3, 2, 3, 2, 1 palavras); o 1º (2 palavras, a data) entra no quadro do corte; o 3º (3 palavras; f3003) 6 quadros DEPOIS da foto 2; o 5º (3 palavras, nomeia a instituição; f3040) 1 quadro ANTES da foto 3; o último (1 palavra, a pergunta; f3078–f3093) termina no corte. Texto #eade53, 68 %. Atrás da tarja: a mesa; a borda de baixo da foto 2 termina em y≈841, colada no topo da tarja (y≈843–847 já escuro: sombra da foto + tarja). Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era L6–8 × mesa 26 ≈ 72–75 %). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #181516, parada.
2. foto 1 vertical COLORIDA, borda off-white, giro ≈ 1,8° anti-horário: x108–590, y129–808 (67,1 % × 53,1 %, centro 48,5 % × 36,6 %).
3. foto 2 vertical P&B por cima, quase do mesmo tamanho, um pouco à direita (conjunto x98–634, y119–834), giro oposto.
4. foto 3 vídeo P&B horizontal por cima, no meio: x58–652, y≈247–692 (82,5 % × 34,8 %); as verticais aparecem acima e abaixo dela.
5. sombra de cada foto sobre a de baixo: difusa ≈ 25 px, deslocada para baixo, até −50 % de luma embaixo, −27 a −41 % nos lados (some em 9–10 px), ≈ −12 % em cima.
6. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Animação: cada foto entra no seu quadro de gatilho a 107–112 % e assenta em 4 quadros (100 % → estalo); a pilha aproxima +2 a +3 %/s do começo ao fim. Passos de 2 quadros.
- Linha do tempo (ms a partir do corte f2965 = 123542 ms): 0 foto 1 + legenda · 167 ms assenta · 1333 ms foto 2 · 1500 ms assenta · 3125 ms bloco de legenda que nomeia a instituição · 3167 ms foto 3 · 3333 ms assenta · 5375 ms corte seco para o rosto.
- Parâmetros que dependem do conteúdo: quais fotos (a última = quem vai reagir), quais são vídeo, qual tem cor.
- O que NÃO fazer: alinhar as fotos sem giro, sombra igual nos 4 lados (é para baixo), trocar as fotos em vez de empilhar, deixar a pilha parada.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o produto em uso, na época" (vertical).
  - "um caso pessoal/afetivo citado" (vertical).
  - "a instituição que vai reagir" (vídeo horizontal, entra na pergunta retórica).
- Nesta referência as lacunas foram preenchidas com: dois mergulhadores de costas no mar com as primeiras roupas; a filha com a roupa, agachada nas pedras; barco da Marinha (UDT) em velocidade.
- Receita de tratamento de cada imagem: fotos de época (uma colorida saturada, uma P&B) e filme P&B, borda de papel, verticais ≈ 67 % da largura, horizontal ≈ 81 %, giros de 1–2°.
- Regra de escolha: depois da invenção, uma foto por fato ("testou", "fez uma para a filha") e, na pergunta retórica sobre a instituição, o vídeo da instituição.
- Teste de generalização: (1) Claude Code: "em 2024 ele já usava em produção, até o filho usava. Então a empresa amou, certo?" → print do sistema em produção; foto do filho no notebook; vídeo do escritório da empresa. (2) café: "em 1905 já vendia no bar, até a esposa servia. Então a cidade amou, certo?" → foto do bar; foto da esposa; filme da praça da cidade.
- Receita de tratamento (reestudo 20/11): fotos de época: uma colorida com cor original saturada (sem dessaturar), as outras P&B neutras (grão ≈ 1,7 níveis, cinza puro), vídeo quando houver; bordas off-white 6–8 px, giros alternados ±1–2°, sombra difusa para baixo.
- Teste de generalização (reestudo 20/11): (1) Claude Code: "em 2024 ele já usava o agente até para o projeto da filha; então a empresa adorou, certo?" → foto colorida de 2024, foto P&B do projeto pessoal, vídeo P&B do prédio da empresa por cima. (2) café: "em 1910 ele já servia o café na família; então os bares adoraram, certo?" → foto colorida antiga, foto da família, vídeo P&B de um bar por cima.

- Confiança: caixas, escalas e tempos medido; conteúdo e tons observado.
