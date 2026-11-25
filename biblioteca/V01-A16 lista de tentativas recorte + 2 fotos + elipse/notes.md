# V01-A16 · lista de tentativas: recorte no disco + 2 fotos que caem por cima + elipse à mão
- Categoria: P08 · Pilha de cartões (provisória do analista: (provisória) montagem de lista: um item por imagem, empilhando (recorte + fotos))
- Fonte: V01 quadros f944–f1057 (39,33–44,04 s; 114 quadros ≈ 4750 ms) · 24 fps
- Fala: "Long johns, surplus Air Force survival suits. Some just greased up their skin."
- Tipo de fala: lista (as tentativas, uma por item)
- Gatilho: corte seco em f944 = 39333 ms, −107 ms antes da palavra nº 127 "Long" (39440 ms). Cada item da lista entra na 1ª palavra do item (tabela abaixo).
- Quadro-chave: f1000
- Camadas ativas: cena de tela cheia | grafismo (elipse à mão) | legenda | b-roll (fotos)
- Leitura dos strips: strip.jpg = quadros f942 a f951, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 10 células. strip-saida.jpg = quadros f966 a f977 (entrada da foto 1 e início da elipse), mesma regra, 12 células. strip-geral.jpg = quadros f942 a f1059, de 3 em 3, 40 células. Cada célula traz o nº do quadro e o tempo. Detalhes do reestudo: detalhe-gravura-recorte.jpg = quadro f955, região x270 y300 150x150 px, ampliada 3× sem suavizar · detalhe-elipse.jpg = quadro f1000, região x430 y350 200x240 px, ampliada 2× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: depois do rosto dizer "tentaram de tudo", a fala lista 3 tentativas; o editor dá 1 imagem por item, cada uma caindo na 1ª palavra do item, e a pilha cresce como a lista.
- Por que este design: o 1º item é objeto (recorte no disco, como os palcos), os 2 seguintes são imagens de época (uma foto e uma filmagem) que caem por cima (alinhado ao reestudo), cobrindo parte do anterior: a lista vira um monte de tentativas acumuladas.
- Por que estas cores: tudo P&B (gravura e arquivo) sobre o creme do disco; o único acento é o amarelo da elipse, que diz "é este aqui" numa foto cheia de gente.
- Por que estes efeitos: a gravura em hachura diagonal traz cara de catálogo antigo; a elipse de marcador translúcido, com o traço sobreposto no começo/fim, é a mão do autor apontando.
- Por que este movimento: estalos de 3 imagens a cada item (≈ 1–2 s), a elipse se desenha devagar (≈ 667 ms) desacelerando, a pilha cresce devagar.
- Sensação do movimento: enumeração com ritmo de "e… e… e…", com uma pausa de ênfase no item circulado; produzida por 3 entradas de 167 ms coladas às palavras (+33 a +63 ms), a elipse revelada em 16 quadros e zoom de +5 a +6 %/s.

## FORMA (fixa: reproduzir igual)
- Design (quadro cheio):
  - Item 1: disco creme ≈ 70 % da largura + recorte de ilustração/gravura P&B do item 1, com contorno de adesivo off-white, centrado: caixa f949 x110–610, y196–770 = 501x575 px (69,6 % · 44,9 %), centro (50,3 %, 38,1 %). (medido com med.py)
  - Item 2: foto horizontal P&B com borda de papel, cai por cima cobrindo a metade de baixo do item 1 (o recorte continua visível em cima e a ponta de baixo dele aparece embaixo): caixa do conjunto f973 x37–631, y140–748; a foto mede ≈ 590 px de largura (82 %), reta (0°). (medido / inclinação medido com inc.py, borda superior 0,0°)
  - Elipse à mão em amarelo-mostarda translúcido (mesmo traço de V01-A15, ≈ 5–6 px (alinhado ao reestudo)), contornando UMA figura da foto 2: caixa x441–623, y363–581 = 182x218 px (25,3 % da largura, 17,0 % da altura), centro (532, 472) = (73,9 %, 36,9 %), no terço direito (remedido, f1000; antes ≈ 130x150 px observado); cor do traço #928832 sobre a foto (translúcido, como A15). (medido)
  - Item 3: filmagem P&B em cartão (movimento interno) vertical-quadrada (alinhado ao reestudo), cai por cima, um pouco à direita, com a pilha aparecendo atrás à esquerda: conjunto f1021 x32–657, y133–735; ≈ 1,4° de giro. (medido)
- Movimento:
  - Item 1: corte seco; pop em 3 imagens = 4 q até o 1º quadro assentado (f944 → f948; perfil 54,1 · 19,2 · 12,1 · depois 7,7 de base) (remedido): caixa f945 448x629 → f947 506x592 → f949 501x575 (disco cresce e recorte encolhe, igual a V01-A01). (medido)
  - Item 2: entra em f968, maior, assenta em 3 imagens = 4 q (f968 → f972; perfil 25,6 · 13,8 · 10,4 · depois 9,2 de base) (remedido): largura do conjunto f969 642 → f971 605 → f973 595 px. (medido)
  - Elipse: o traço se desenha de f976 a ≈ f992 (≈ 16 q, 667 ms), região da elipse com diferença 10 por imagem até f988 e caindo para 5 em f994 (revelação contínua, desacelera no fim). (medido no perfil, região x400 y500 300x300)
  - Item 3: entra em f1016, assenta em 3 imagens = 4 q (f1016 → f1020; perfil 31,7 · 13,1 · 9,3 · depois 4,5) (remedido): largura do conjunto f1017 666 → f1019 637 → f1021 626 px. (medido)
  - Pilha aproxima em zoom contínuo, +6 %/s no item 1 e ≈ +4 %/s constante do item 3 ao corte (alinhado ao reestudo) (caixa cresce para 664x641 até f1055). Cadência 12 imagens/s. (medido)
  - Saída: corte seco para o A-roll em f1058. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | item 1 recorte no disco | f944 | 4 q (167 ms) (remedido) | pop desencontrado | estalo | nº 127, 1ª palavra do item 1 | −107 ms |
  | item 2 foto por cima | f968 | 4 q (167 ms) (remedido) | escala 108 → 100 % | estalo | nº 129, 1ª palavra do item 2 (40270) | +63 ms |
  | elipse à mão | f976 | ≈ 16 q (667 ms) | traço se revela | desacelera | nº 130, 2ª palavra do item 2 (40620) | +47 ms |
  | item 3 foto por cima | f1016 | 4 q (167 ms) (remedido) | escala 106 → 100 % | estalo | nº 134, 1ª palavra do item 3 (42300) | +33 ms |
- Ritmo: item 1 sozinho 24 q (1000 ms); item 2 no topo 48 q (2000 ms); item 3 no topo 42 q (1750 ms). Um item novo a cada 1,0–2,0 s, exatamente no início de cada item da lista falada. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Mesa e disco creme: os de V01-A01 (o disco ferve).
  - Recorte do item 1: família impressão antiga com retícula (gravura em hachura): `textura` f955 em 290,330,60,120: #8c8983, grão 62,4 (!), ac1 +0,04, ac2 −0,65, ac4 +0,15 → padrão periódico de linhas diagonais com período ≈ 4 px (detalhe-gravura-recorte: hachura diagonal fina, pespontos em pontinhos), cinza puro. Anda com a câmera (f955×f957 +0,96 alinhada). Teste novo (f955×f957, alinhado pela cena 0,0,720,820, região 260,300,200,150): resíduo ÷ σ 0,49–0,72 em todas as faixas = PARADA (é desenho de linhas, sem grão vivo). Contorno off-white como os outros adesivos. (medido)
  - Fotos dos itens 2 e 3: arquivo P&B com grão (como V01-A12), bordas off-white ≈ 7 px de canto vivo; a do item 3 é filmagem (movimento interno). Grão VIVO nos claros (corrigido na conferência: era "como V01-A12", lido como parado). Teste novo, alinhado pela afim da foto, pixels lisos: item 2 (foto parada) f990×f992, região 80,320,330,300: claros resíduo ÷ σ 0,94 (2,35 níveis) × escuros 0,32 e médios 0,45 → vivo parcial nos claros; item 3 f1040×f1042, região 90,270,530,400: claros 1,23 (3,4 níveis) × escuros 0,65 → VIVO nos claros (a conferência mediu 1,20 no mesmo par). (medido)
  - Elipse: marcador amarelo translúcido, ≈ 5–6 px, mais claro e limão sobre a foto clara (detalhe-elipse), com o traço DUPLO no lado esquerdo, onde começa e termina (sobreposição de ≈ 1/6 da volta).
- Efeitos (reestudo 20/11):
  - Sombras: a do adesivo no disco como em V01-A01/A11 (dos lados, quase nada em cima). As das fotos CAEM PARA BAIXO (`sombra` alinhada): item 2 (f990, caixa 36,290,600,370) embaixo −52 % no 1º px fora, volta em 16 px; direita −44 %, 10 px; item 3 (f1040, caixa 56,236,600,468) embaixo −61 %, volta em 19 px; direita −34 %, 10 px; em cima as duas caem sobre o recorte e o disco (conteúdo, não medível); a esquerda do item 3 cai sobre a foto de trás (não medível). (medido; corrigido na conferência: era "contato curto como A12")
  - Vinheta, brilho, desfoque de movimento (entradas nítidas), profundidade, grão global, aberração: nenhum (f955, f1000).
- Câmera (reestudo 20/11): zoom in contínuo do grupo: `camera` f950→f964 (item 1) ×1,0358 (+6,2 %/s), sobe 1,8 px/q; f1024→f1054 (item 3) ×1,0604 (+4,8 %/s), 0,1 px/q. Remedido em 3 janelas com a região 0,0,720,820: f1020→f1032 +4,2 %/s, f1032→f1044 +4,2 %/s, f1044→f1056 +4,0 %/s, giro ≤ 0,02° (na região da pilha 40,120,640,620: +3,3 e +4,0 %/s, giro ±0,2°) → constante até o corte. A conferência leu +1,4 → +7,0 → +7,1 %/s e giro −0,4 a −0,6°; não reproduzi (provável contaminação pelo movimento da filmagem do item 3). (medido) A pilha cresce de 501x575 para 664x641 px até f1055. Fundo parado.
- Cadência (reestudo 20/11): 12 imagens/s (`perfil` f1024–f1031: 11,3 / 0,02 / 11,7 / 0,04 / 8,2 / 0,02 / 9,8 / 0,01); a elipse avança 1 vez por imagem.
- Legenda nesta cena (reestudo 20/11): 5 blocos, 1 por pedaço de item: o item 1 (f944–f964, 2 palavras, no MESMO quadro do corte), a 1ª metade do item 2 (f965–f988, 3 palavras; foto 2 em f968), a 2ª metade do item 2 (f989–f1015, 2 palavras; elipse terminando), a 1ª metade do item 3 (f1016–f1036, 3 palavras; foto 3 no MESMO quadro f1016), a 2ª metade do item 3 (f1037–f1057, 3 palavras). A legenda escreve nomes próprios com maiúsculas (o texto não segue a transcrição automática). Atrás da tarja: a mesa (a pilha termina em y≈735–770) → tarja preta pura lida como preta (74 % no vídeo, medida direta da conferência). Nenhum outro texto (o "branco grande" do censo em f944–f967 é o contorno do adesivo).

## CONSTRUÇÃO
1. fundo: mesa fixa.
2. item 1: disco creme ≈ 70 % da largura + recorte da gravura do objeto (hachura diagonal, P&B) com contorno de adesivo; caixa x110–610 y196–770 em f949, centro 50,3 % × 38,1 %. Entrada em 0 ms (f944): pop desencontrado (disco cresce, recorte encolhe) em 3 imagens até 167 ms.
3. item 2: foto horizontal P&B ≈ 82 % da largura, reta (0°), com grão vivo nos claros (re-sorteado a 12/s) e sombra caída para baixo (16 px embaixo a −52 %, 10 px dos lados, nada medível em cima), cai em 1000 ms (f968) cobrindo a metade de baixo do item 1 (ficam à mostra o alto do recorte e as pontas de baixo); 108 → 100 % em 3 imagens.
4. elipse: marcador amarelo translúcido 5–6 px, 182 × 218 px, centro 73,9 % × 36,9 %, em volta de UMA figura da foto 2; revelada de 1333 ms (f976) a ≈ 2000 ms (f992), desacelerando, começa e termina à esquerda com sobreposição; fica até o item 3 cobrir.
5. item 3: foto P&B (filmagem) quase quadrada, +1,4°, grão vivo nos claros e sombra caída para baixo (19 px embaixo a −61 %, 10 px dos lados), cai em 3000 ms (f1016) um pouco à direita, a pilha aparecendo à esquerda; 106 → 100 % em 3 imagens.
6. câmera: zoom in do grupo +6 %/s no item 1 e ≈ +4 %/s constante do item 3 até o corte; fundo parado.
- Linha do tempo (ms a partir de f944): 0 item 1 + legenda do item 1 · 875 legenda (1ª metade do item 2) · 1000 item 2 · 1333–2000 elipse · 1875 legenda (2ª metade do item 2) · 3000 item 3 + legenda (1ª metade do item 3) · 3875 legenda (2ª metade do item 3) · 4750 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: quantos itens (1 imagem por item), qual item é objeto (recorte no disco) e quais são fotos, qual figura circular.
- O que NÃO fazer: mostrar todos os itens juntos (cada um cai na sua palavra); elipse perfeita, fechada sem sobreposição ou opaca; colorir a gravura; fotos sem cobrir parte da anterior; fotos com grão parado ou com sombra igual em volta (o grão dos claros é vivo e a sombra cai para baixo).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "item 1 da lista": objeto recortado (quando é uma coisa).
  - "item 2 da lista": foto de época mostrando o item em uso.
  - "detalhe a destacar no item 2": o que circular à mão.
  - "item 3 da lista": foto ou filmagem de época da tentativa (alinhado ao reestudo).
- Nesta referência as lacunas foram preenchidas com: ceroula longa (gravura); trajes de sobrevivência da Força Aérea (foto, elipse em um homem vestido); nadador besuntado de graxa (filmagem) (alinhado ao reestudo).
- Receita de tratamento de cada imagem: objeto = recorte com adesivo sobre disco creme; fotos = arquivo P&B com grão, borda de papel, giro pequeno alternado, ≈ 82–87 % da largura, cada uma cobrindo parte da anterior. (reestudo 20/11) Medido: o objeto do item 1 vem como GRAVURA de catálogo antigo (hachura diagonal de período ≈ 4 px, P&B, grão 62 por causa das linhas), recortada com adesivo; as fotos são P&B neutro com grão de filme vivo nos claros (resíduo ÷ σ 0,94–1,23 × 0,32–0,65 nos escuros), sem vinheta, sombra caída para baixo.
- Receita de ILUSTRAÇÃO (reestudo 20/11): quando o item é um objeto de época, usa-se gravura/ilustração impressa em linhas (hachura) em P&B, recortada com contorno de adesivo e posta no disco creme; a anotação é elipse de marcador amarelo translúcido, 5–6 px, traço à mão com sobreposição de ≈ 1/6 da volta onde começa e termina, revelada como traço em ≈ 16 quadros, desacelerando.
- Regra de escolha: lista falada de tentativas → 1 imagem literal por item, na ordem e na palavra de cada item; quando a foto tem muita gente, uma elipse à mão aponta quem/qual é o item.
- Teste de generalização: (1) Claude Code: "tentaram de tudo: prompts gigantes, planilhas de contexto, copiar e colar" → recorte de um rolo de papel enorme; print de planilha (elipse numa célula); foto de alguém com Ctrl+C. (2) café: "tentaram açúcar, leite, até sal" → recorte de um açucareiro; foto antiga de leiteiro (elipse na garrafa); foto de saleiro.

- Confiança: caixas, escalas e tempos medido; tamanho e posição da elipse observado; cor da elipse igual à medida em A15.
