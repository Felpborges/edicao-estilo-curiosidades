# V01-A28 · três recortes de pessoas, cada um no seu disco, entram um a um e saem em cascata
- Categoria: P14 · Disco creme com recorte (provisória do analista: (provisória) colagem de recortes-adesivo de pessoas sobre discos creme (montagem de "vozes"))
- Fonte: V01 quadros f1846–f1939 (76,92–80,79 s; 94 quadros ≈ 3917 ms) · 24 fps (remedido: o recorte 3 ainda aparece na borda de baixo até f1938–f1939)
- Fala: "Now, ask a surfer how a wetsuit works and you'll probably hear this."
- Tipo de fala: anúncio (vira o capítulo: "pergunte a um X e você vai ouvir isto")
- Gatilho: corte seco em f1846 = 76917 ms, −203 ms antes da palavra nº 243 "Now," (77120 ms). Recorte 2 em f1872 = 78000 ms, −60 ms antes da nº 247 "how" (78060 ms). Recorte 3 em f1896 = 79000 ms, −20 ms antes da nº 251 "and" (79020 ms). Saída começa em f1920 = 80000 ms, −80 ms antes da nº 255 (remedido; f1918 ainda é igual a f1917) "this." (80080 ms).
- Quadro-chave: f1910
- Camadas ativas: cena de tela cheia | legenda | transição (saída em cascata)
- Leitura dos strips: strip.jpg = quadros f1844 a f1853, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 10 células. strip-saida.jpg = quadros f1917 a f1936 (saída em cascata e o disco seguinte), mesma regra, 20 células. strip-geral.jpg = quadros f1844 a f1936, de 2 em 2, 47 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-adesivo-retícula.jpg = quadro f1910, região x225 y560 150x140 px, ampliada 3× sem suavizar · detalhe-borda-disco.jpg = quadro f1910, região x30 y330 110x110 px, ampliada 3× sem suavizar · detalhe-saida-f1922.jpg = quadro f1922, região x0 y120 720x760 px, ampliada 1× sem suavizar (meio da saída em cascata).


## LEITURA DE EDITOR
- Por que esta cena aqui: a fala troca de capítulo e convoca "o público que todo mundo pergunta"; três pessoas diferentes viram uma pequena multidão, uma por meia-frase, antes de o mito ser explicado.
- Por que este design: recortes de corpo inteiro em poses diferentes, cada um no seu disco creme de tamanho diferente, sobrepostos em pirâmide (esquerda, direita alta, frente embaixo): colagem de revista, leitura de "várias vozes".
- Por que estas cores: P&B em retícula sobre discos creme e mesa escura; nenhum acento de cor, porque o assunto aqui é gente, não o mecanismo (a cor volta no diagrama seguinte).
- Por que estes efeitos: retícula de impressão e adesivo branco irregular dizem "recortado de revista"; a sombra curta do recorte sobre o disco dá o empilhado físico.
- Por que este movimento: cada pessoa entra com pop no começo da sua meia-frase; no fim, todas saem em cascata para lados diferentes, desfocando, o que "limpa a mesa" e abre espaço para a explicação.
- Sensação do movimento: acúmulo rítmico (um "tum" a cada ≈ 1 s) e depois dispersão rápida e borrada, como papéis varridos da mesa; entre um e outro, o grupo respira (aproxima e depois recua devagar).

## FORMA (fixa: reproduzir igual)
- Design (med.py, quadro cheio):
  - Recorte 1: pessoa 1 do público citado, em P&B (silhueta escura), de pé, recortada com contorno de adesivo off-white, sobre um disco creme; conjunto no lado ESQUERDO: assentado f1850 x35–477, y134–745 = 443x612 px (61,5 % da largura, 47,8 % da altura), centro (35,6 %, 34,0 %).
  - Recorte 2: pessoa de costas em P&B, sobre um 2º disco menor atrás, no lado DIREITO e mais alto; conjunto dos dois assentado f1876 x28–659, y113–751 = 631x638 px (87,6 % · 49,8 %) (remedido, f1876; o y89 não existe em nenhum quadro: f1872 y73 no pop, f1874 y103, f1876 y113).
  - Recorte 3: pessoa sentada abraçando os joelhos, P&B, num 3º disco pequeno, EMBAIXO no centro, na frente dos outros dois; conjunto dos três f1899 x21–670, y120–844 (90 % · 57 %).
  - Disco 1 (o maior, atrás do recorte 1) em f1910: borda esquerda x42, topo y201, diâmetro ≈ 456 px (63 % da largura), centro ≈ (37,5 %, 33,5 %) (medido, remedição f1910; o diâmetro sai do topo e da borda esquerda). Discos 2 e 3 não medidos isoladamente (ficam atrás dos recortes).
  - Discos de tamanhos diferentes e sobrepostos; recortes sempre na frente dos discos; o último a entrar fica na frente. (observado)
- Movimento:
  - Recorte 1: corte seco; pop desencontrado em 2 imagens: caixa f1846 397x660 → f1848 447x628 → f1850 443x612 (disco cresce, recorte encolhe; igual a V01-A01). (medido)
  - Recorte 2: entra em f1872 (diferença 10,7), assenta em f1876 (topo y73 → y103 → y113: 2 imagens em movimento, 4 q) (remedido, f1876). (medido)
  - Recorte 3: entra em f1896 (diferença 14,2), assenta em f1898–f1900 (2 imagens). (medido)
  - Saída em cascata, um por vez, cada um para um lado, com borrão de movimento: recorte 1 sai para a ESQUERDA (f1920–f1925; o disco 1 ainda é uma lasca na borda até f1931), recorte 2 para a DIREITA (f1926–f1929), recorte 3 para BAIXO (f1930–f1939, já por baixo do disco novo). 12 q (500 ms) do 1º movimento até o disco seguinte (V01-A29) cair em f1932; 20 q (833 ms) até o recorte 3 sumir (remedido, f1920–f1939). Diferença por imagem 7,6 → 13,3 → 27,1 → 23,8 → 19,2 → 16,4 → 16,6 → 67,8 (disco novo). (medido; direções observado no strip-saida)
  - Cadência 12 imagens/s (fase par nesta saída). (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | pessoa 1 (esquerda) | f1846 | 4 q (167 ms) | pop desencontrado | estalo | nº 243 | −203 ms |
  | pessoa 2 (direita, alto) | f1872 | 4 q (167 ms) | pop | estalo | nº 247 | −60 ms |
  | pessoa 3 (embaixo, frente) | f1896 | 4 q (167 ms) | pop | estalo | nº 251 | −20 ms |
  | saída em cascata esq. → dir. → baixo | f1920 (remedido) | 20 q (833 ms) (remedido) | deslizes com borrão | acelera | nº 255 | −80 ms |
- Ritmo: um recorte novo a cada ≈ 1,0 s; os três juntos, sem peça nova e recuando −3,5 a −4,2 %/s (alinhado ao reestudo), de f1900 a f1919 (≈ 833 ms) (remedido). (medido)
- Som: nenhum efeito detectado (áudio mono). Obs.: o canal lateral tem um pico isolado em 77,7 s (f1865, −32 dB), sem relação visível com um evento; ver análise (d). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Fundo (mesa): a mesma de sempre, luma 26–35, parada (diferença 0,00–0,09 por quadro na faixa y950–1250).
  - Disco creme: papel com fibra fina. f1910 região 60,420,90,110: #cec7b5, luma 199, grão 5,25 níveis, manchas 2,54, ac1 +0,55 (≈ 2 px), grão cinza (5,23/5,26/5,25). VIVA: depois de alinhar o deslocamento da peça, a correlação do grão entre imagens seguidas fica em +0,24 a +0,30 (f1904 × f1906, f1910 × f1912), enquanto a retícula do recorte, medida igual, dá +0,71: o papel do disco "ferve" a cada imagem (textura trocada ou re-sorteada), as fotos não. Remedido com o teste novo (alinhado pela afim do conjunto, pixels lisos, f1910×f1912 e ×f1914, região 50,330,110,220): claros resíduo/σ 1,45 e 1,32, correlação +0,11 e +0,09 → VIVO (mesmo veredito da nota). No detalhe: mosqueado fino sem fibra direcional, borda do disco limpa com 1 px escuro.
  - Recortes: impressão antiga com retícula. f1910 região 470,420,50,70 (área escura do recorte): #333030, grão 18,1 níveis, autocorrelação ac1 +0,32 · ac2 −0,38 · ac4 +0,58 = padrão periódico de ≈ 4 px; no detalhe, retícula de pontos a 45°, cinza neutro (18,04/18,10/18,10). Anda rígida com a peça (correlação +0,71 após alinhar; remedido com o teste novo, f1910×f1912/f1914: escuros resíduo/σ 0,72–0,80, correlação +0,67…+0,76 = rígida, mesmo veredito).
  - Adesivo: off-white quente #eae2d5–#efe7dc, ≈ 9–10 px (linha y640: x206–215), contorno que suaviza a silhueta (não segue os dedos nem os fios de cabelo), com a mesma fibra do disco.
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: só o foco de luz largo da mesa. Vinheta da imagem: o disco escurece levemente para a borda (143 → 86 nos últimos 8 px do disco 1, f1910) e termina num fio escuro de 1–2 px (29 contra fundo 33–35).
  - Borda borrada: nenhuma nas peças paradas.
  - Sombra: o recorte projeta sombra difusa sobre o que está embaixo: disco a 165 colado no adesivo contra 199 no resto (−17 %), largura ≈ 15 px (x189 → x204 em y640); sobre a mesa, 26 → 18 junto do adesivo. Sombra do disco na mesa (medido, f1910, linhas y400–440 e perfil alinhado): à esquerda −39 % no contato (22 contra 36) e volta ao fundo em ≈ 9 px; em cima nada (−4 %, 1 px); embaixo −23 %, volta em ≈ 20 px (só 41 linhas de varredura, baixa confiança) (corrigido na conferência: era "o disco quase não projeta sombra na mesa, só o fio de 1–2 px").
  - Desfoque de movimento: sim, na saída: em f1922 o recorte que sai está todo desfocado (≈ 8–12 px, desfoque geral, não só arrasto), enquanto o disco dele, ainda parado, segue nítido.
  - Profundidade, grão global, brilho, aberração: nenhum (medido em f1910).
- Câmera (reestudo 20/11): o grupo inteiro anda junto e muda de direção. f1852 → f1866 (só recorte 1): escala ×1,0194 (+3,4 %/s), centro (−0,08, −0,73 px/q), giro −0,03°. f1900 → f1914 (os três): recorte 1 ×0,9752 (−4,2 %/s, +1,65 px/q para a direita), recorte 2 ×0,9796 (−3,5 %/s, +1,07 px/q), giro ≤ 0,15°: depois que o 3º entra, o conjunto RECUA (afasta) devagar. Fim, antes da cascata (medido, f1906 → f1918, região 0,100,720,730): ×0,9817 (−3,6 %/s), centro (+1,45, +0,05 px/q): o recuo segue igual até a saída; os últimos 20 quadros (f1920–f1939) são a cascata, sem câmera própria. Mesa parada. Sem paralaxe entre recortes e discos (andam juntos).
- Cadência (reestudo 20/11): 12 imagens/s nas peças (perfil f1877–f1896: 0,12 / 8,1 / 0,05 / 11,1 / 0,06 / 11,5 / 0,08 / 11,5 … nos quadros ímpares ≈ 0); mesa parada (≤ 0,09).
- Legenda nesta cena (reestudo 20/11): 5 blocos (4, 3, 3, 1 e 2 palavras); o 1º (4 palavras, o pedido ao público citado; f1846–f1873) entra no MESMO quadro do corte; o último (2 palavras, o anúncio; f1917–f1935) atravessa a saída em cascata e o disco seguinte (f1932). Texto #eade53, centro 68 %. Atrás da tarja: a mesa (o recorte 3 chega a y≈838–844, a 3–9 px da tarja, sem encostar). Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px de altura (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %, estimativa grosseira). O "texto branco grande" do censo em f1872–f1929 é o adesivo branco dos recortes (falso positivo). Nenhum sumiço.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #181516 com foco de luz largo, parada.
2. discos (um por recorte, atrás dele): papel creme #cec7b5 com grão de 5 níveis que muda a cada imagem (re-sortear o ruído a cada 2 quadros), leve escurecimento nos últimos 8 px e fio escuro de 1–2 px; sombra curta na mesa: −39 % no contato à esquerda, some em ≈ 9 px, nada em cima (corrigido na conferência: era sem sombra). Disco 1 Ø ≈ 456 px (63 % da largura), centro ≈ (37,5 %, 33,5 %); disco 2 menor, à direita e mais alto; disco 3 o menor, embaixo no centro.
3. recortes: foto P&B de corpo inteiro, retícula de pontos a 45° com passo ≈ 4 px, adesivo off-white ≈ 10 px de contorno suavizado, sombra difusa ≈ 15 px (−17 % de luma) sobre o que está embaixo. Recorte 1: x35–477, y134–745 com o disco (61,5 % × 47,8 %); conjunto 1+2: 87,6 % × 49,8 %; conjunto dos 3: x21–670, y120–844. O último a entrar fica na frente.
4. animação: cada par disco+recorte entra com pop desencontrado (disco cresce enquanto o recorte encolhe para o lugar) em 2 imagens (167 ms, 4 quadros). Grupo: aproxima +3,4 %/s enquanto há 1 recorte; com os 3, recua −3,5 a −4,2 %/s com deriva para a direita ≈ 1,1–1,7 px/q. Saída em cascata: recorte 1 para a esquerda (f1920–f1925), recorte 2 para a direita (f1926–f1929), recorte 3 para baixo (f1930–f1939), cada um acelerando e desfocando ≈ 8–12 px; o disco de cada recorte sai depois dele. Passos de 2 quadros.
5. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Linha do tempo (ms a partir do corte f1846 = 76917 ms): 0 corte + recorte 1 (pop 167 ms) + legenda · 1083 ms recorte 2 · 2083 ms recorte 3 · 2167–3083 ms os três juntos, recuando · 3083 ms recorte 1 sai à esquerda · 3333 ms recorte 2 sai à direita · 3500 ms recorte 3 sai para baixo · 3583 ms o disco da cena seguinte cai por cima · 3917 ms último resto some.
- Parâmetros que dependem do conteúdo: quantas pessoas (3 aqui, uma por meia-frase), as poses (variar: de pé, de costas, sentada), o tamanho de cada disco.
- O que NÃO fazer: fotos em tons contínuos (tem de ter retícula visível), adesivo que segue todos os detalhes da silhueta, discos sem a textura viva, saída em que tudo sai junto ou para o mesmo lado, saída sem desfoque, câmera parada com os três na tela.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "pessoas do público citado" (3 tipos diferentes, todos reconhecíveis como esse público): fotos recortadas.
- Nesta referência as lacunas foram preenchidas com: surfista com prancha; surfista de roupa de costas; surfista sentada na areia.
- Receita de tratamento de cada imagem: fotos reais de pessoas inteiras, convertidas para P&B de alto contraste, recortadas com adesivo off-white ≈ 10 px, cada uma sobre um disco creme de tamanho diferente; poses variadas (de pé, de costas, sentada).
- Regra de escolha: "pergunte a um X" → mostra-se uma pequena multidão de X (3 recortes), um por meia-frase; antes do "você vai ouvir isto", tudo sai para abrir a explicação comum.
- Teste de generalização: (1) Claude Code: "pergunte a um dev como o Claude lembra das coisas" → 3 recortes de devs (de fone, de pé com café, sentado no chão com notebook). (2) café: "pergunte a um barista" → 3 recortes de baristas em poses diferentes.
- Receita de tratamento (reestudo 20/11): foto de pessoa inteira, recortada, P&B de alto contraste convertida em retícula de pontos a 45° (passo ≈ 4 px na tela 720), preto da roupa #333030 com pontos claros, adesivo off-white quente ≈ 10 px de contorno arredondado; sombra difusa curta para baixo e para a esquerda sobre o disco.
- Receita de ILUSTRAÇÃO (reestudo 20/11): disco = círculo de papel creme chapado (#cec7b5) com grão vivo de ≈ 5 níveis, sem desenho, com fio escuro de 1–2 px na borda; serve de "palco" para o recorte e se destaca da mesa pelo contraste e por uma sombra curta (−39 % no contato, ≈ 9 px, nada em cima) (corrigido na conferência: era "sem sombra").
- Teste de generalização (reestudo 20/11): (1) Claude Code: "pergunte a qualquer dev como o Claude lembra das coisas e ele vai dizer isto" → 3 recortes em retícula (dev de fone sentado, dev de pé com caneca, dev de costas para a tela) em 3 discos, saindo em cascata no "isto". (2) café: "pergunte a um barista e você vai ouvir isto" → 3 baristas recortados em poses diferentes, mesma entrada e saída.

- Confiança: caixas, tempos e cadência medido; direções da cascata e ordem de profundidade observado.
