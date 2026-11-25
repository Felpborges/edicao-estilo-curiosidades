# V05-A21 · página de livro científico desliza por cima e uma elipse é desenhada
- Categoria: P20 · Documento com marca-texto (provisória do analista: (provisória) transição por objeto (página/papel que desliza e cobre a tela) + marcação desenhada à mão)
- Fonte: V05 quadros f1205–f1268 (50,27–52,89 s; 64 quadros ≈ 2669 ms) · 23,976 fps
- Fala: "Just a tiny gland of clear slime,"
- Tipo de fala: mecanismo (explicação técnica: a parte do corpo que guarda o segredo)
- Gatilho: a página aparece em f1205 (50 262 ms) DURANTE o fim da palavra nº 181 "inside." (começa 49 920 ms → +342 ms; o chiado do "s" está no envelope em f1204–f1206), 528 ms antes da nº 182 "Just" (50 790 ms) (conferido: a palavra dita em f1205 é "inside."; o JSON passou a apontar a nº 181). A elipse começa em f1231 (51 343 ms; 6 px roxos em f1231, traço curto em f1232), 137 ms antes de "gland" (#185, 51 480 ms) (conferido, `caixa` da cor roxa quadro a quadro; antes: f1233, −54 ms). Conferido nos strips (canto da página em f1205; 1º traço roxo em f1233).
- Quadro-chave: f1250
- Camadas ativas: transição (página por cima do card A20) | cena de corte (página) | grafismo (elipse) | legenda
- Leitura dos strips: strip.jpg = quadros f1203 a f1222, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 20 células. strip-saida.jpg = quadros f1231 a f1248, de 1 em 1, 8 colunas; 18 células (o desenho da elipse). strip-geral.jpg = quadros f1203 a f1268 (amostrado), 8 colunas. detalhe-pagina-entrando-f1208.jpg = quadro f1208, região x0 y0 720x700 px, ampliada 1× sem suavizar (meio do deslize: a borda direita da página está borrada pelo movimento; o card de A20 ainda aparece à direita). detalhe-elipse.jpg = quadro f1250, região x240 y430 200x160 px, ampliada 2× sem suavizar (a elipse roxa sobre a gravura). detalhe-papel-realce.jpg = quadro f1250, região x520 y170 180x120 px, ampliada 3× sem suavizar, contraste ×6 em volta da média (canto da página: borda nítida, sem sombra; o fundo escuro da vinheta).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala passa do "não tem cor" para o "onde está o segredo"; uma prancha científica antiga dá autoridade de fonte e a elipse aponta a parte exata.
- Por que este design: página de livro antigo que cobre quase a tela toda, levemente inclinada, e uma elipse fina à mão em volta do detalhe: "pesquisa de arquivo" com marca de professor.
- Por que estas cores: papel creme (#eed0ae no centro) com gravura colorida à mão; a elipse na COR-TEMA (#815685), único traço saturado: o detalhe é ligado ao tema pela cor.
- Por que estes efeitos: vinheta forte sobre a página (borda 13 %) como luz de mesa de leitura; nenhuma sombra: a página é tratada como imagem chapada sob a luz.
- Por que este movimento: a página entra deslizando rápido do canto superior esquerdo (7 q, com borrão de movimento) e cobre a cena anterior como quem põe um papel por cima; freia longo e a elipse se desenha na palavra da parte do corpo.
- Sensação do movimento: "olha aqui na fonte"; produzida pelo deslize de 292 ms com borrão, freio de 918 ms com leve recuo, traço da elipse de 459 ms e push lento final (+0,12 %/q).

## FORMA (fixa: reproduzir igual)
- Design: página de livro antigo (gravura científica colorida à mão, fundo creme #e2c5a7 em f1250 x360 y420; meio-tom #5a4f3e na borda inferior esquerda, medido, com vinheta forte) que ocupa quase a tela toda, levemente inclinada, com margens escuras finas nas laterais (observado ≈ 4–6 %). Marcação: elipse ROXA #815685 (mediana dos pixels roxos, f1250) de traço fino (≈ 3 px) feita à mão, uma volta fechada e uniforme no quadro cheio (alinhado ao reestudo), em volta do detalhe citado; caixa da elipse x250–429 y444–574 (24,9 % × 10,2 % do quadro; centro 47,1 %, 39,8 %) (medido).
- Movimento:
- Passos internos:

| passo | quadros | duração | tipo | curva (dif) | gatilho |
|---|---|---|---|---|---|
| página entra | f1205–f1211 | 7 q ≈ 292 ms | desliza do canto superior esquerdo para baixo/direita, inclinada, cobrindo card e cena | 3 → 8 → 14 → 17 → 19 (pico f1209) → 15 | pausa antes da 1ª palavra da frase (−528 ms) |
| página assenta | f1212–f1233 | 22 q ≈ 918 ms | freio longo + leve zoom-out (a página encolhe e mostra a margem escura) | 14 → 10 → 8 → 6 → 3 → 2 | as 3 primeiras palavras da frase |
| elipse desenhada | f1231–f1241 (conferido; antes f1233) | 11 q ≈ 459 ms | traço roxo cresce ao redor do detalhe (sentido horário, uma volta fechada; alinhado ao reestudo) | — | o nome do detalhe (#185) −137 ms |
| parado | f1242–f1268 | 27 q ≈ 1126 ms | design parado, câmera em push lento +0,12 %/q (alinhado ao reestudo) | 1–2 | a descrição do detalhe |

- Saída: corte seco em f1269 (dif 59) para a cena de recortes (A22).
- Ritmo: design completo (página + elipse) parado ≈ 1,1 s.
- Som: nenhum efeito detectado (lateral −120 dB de 50 a 53 s).
- Textura (reestudo 20/11):
  - Papel da página: família papel antigo escaneado (liso com grão fino). `textura` f1250 região 420,620,60,60 (papel limpo no centro): #eed0ae, grão 5,1, manchas 4,0, ac1 +0,58 / ac2 −0,03 (grão fino de 1–2 px, sem fibra direcional). No canto alto (540,190,140,50, sob vinheta): #5e5142, grão 0,47 (a vinheta esmaga o grão). Detalhe realçado: papel sem fibra visível, gradiente suave da vinheta.
  - Gravura: traço fino de gravura com cor aplicada à mão em verde (observado no detalhe).
  - Elipse: família tinta (traço digital), cor-tema #815685, ≈ 3–4 px, borda levemente macia; no detalhe f1250 aparece como uma volta só, fechada e uniforme (a "2ª volta" da nota antiga não é visível no quadro cheio).
- Efeitos (reestudo 20/11):
  - Vinheta forte por cima da página: `borda` f1250 luma 100 · 85 · 61 · 27 · 13 %; nitidez cai junto (sem desfoque próprio).
  - Sombra da página: nenhuma. `sombra` f1250 borda esquerda (y600): papel 100–108 → queda nítida para 34 em 2 px, depois o fundo segue a vinheta (35 → 22) sem faixa escura; topo (x300): papel 120–138 → 75 em 2 px, sem sombra.
  - Desfoque de movimento: SIM na entrada (detalhe f1208: borda direita da página borrada na direção do deslize).
  - Sem grão de filme, sem brilho, sem aberração.
- Câmera (reestudo 20/11): f1242→f1266 ×1,030 (+0,12 %/q, +3,0 %/s), centro quase parado (−0,1 px/q): push lento depois de assentar (a nota antiga dizia "quase fixa"). Remedido na correção: f1210→f1218 sem medida (a página desliza e cobre a cena: 5 de 526 pontos); f1225→f1235 +6,3 %/s (+0,26 %/q), +1,1/+0,9 px/q (a página ainda assenta); f1255→f1266 +2,9 %/s (+0,12 %/q), centro parado: mesmo valor da nota no fim.
- Cadência (reestudo 20/11): 24 imagens/s (dif da entrada muda em todos os quadros; a elipse cresce em todos os 11 q).
- Legenda nesta cena (reestudo 20/11): o bloco da negação (f1182–f1216) ATRAVESSA a entrada da página (f1205) e só troca 12 q depois (4 palavras com o nome do detalhe, f1217–f1245); a descrição do detalhe (3 palavras, f1246–f1269) atravessa o corte de saída (f1269). Tarja 66–69 % (f1250: luma dentro 49 × fora 156); sobre o papel claro a tarja aparece cinza-marrom. Sem outro texto.

## CONSTRUÇÃO
1. por baixo: a cena anterior com o card (A20), que vai sendo coberta.
2. página: imagem de prancha científica antiga (papel creme #eed0ae, gravura com cor à mão), ocupando ≈ 90 % da largura e sangrando embaixo e à direita, inclinação leve (< 2°), sem sombra; posição final com a borda esquerda em x ≈ 68 e o topo em y ≈ 178.
3. vinheta forte presa à tela por cima da página (100 · 85 · 61 · 27 · 13 %).
4. elipse: traço na cor-tema, 3–4 px, em volta do detalhe citado (24,9 % × 10,2 % do quadro, centro 47 %, 40 %), presa à página.
5. animação (ms a partir de f1205, durante o fim da palavra anterior): 0–292 ms a página desliza do canto superior esquerdo para a posição, rápida (pico em ≈ 167 ms), com desfoque de movimento na direção do deslize; 292–1210 ms freio longo com leve recuo (a margem escura aparece); 1084 ms a elipse começa (137 ms antes da palavra da parte) e fecha em 459 ms, sentido horário; 1210–2669 ms push lento +0,12 %/q.
6. legenda por cima; corte seco no fim.
- Linha do tempo (ms a partir de f1205): 0 página entra · 292 cobre tudo · 500 troca a legenda · 1084–1543 elipse · 1543–2669 parado com push lento · 2669 corte seco.
- Parâmetros que dependem do conteúdo: a prancha/página (fonte de época sobre o assunto); onde fica a elipse (a parte citada); a palavra que dispara.
- O que NÃO fazer: não dar sombra à página; não entrar sem borrão de movimento; não usar elipse branca ou preta (é na cor-tema); não deixar a página sem vinheta; não parar a câmera de vez.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "documento de época que mostra a anatomia/estrutura do assunto"; "o detalhe exato que a fala nomeia" (circulado).
- Nesta referência as lacunas foram preenchidas com: prancha científica antiga de moluscos; a glândula do búzio.
- Receita de tratamento de cada imagem: scan de livro/gravura antiga, cores desbotadas originais, papel creme liso com grão fino, sem fibra visível (alinhado ao reestudo), borda do papel visível, leve inclinação; vinheta; marcação em roxo (a cor-tema) com traço de caneta fino, uma volta fechada (alinhado ao reestudo).
- Regra de escolha: explicação técnica com fonte de época. Quando a fala nomeia uma parte pequena de algo ("a tiny gland"), mostra-se o desenho científico e circula-se a parte.

- Receita de tratamento de cada imagem (reestudo 20/11): página escaneada de livro antigo, cor original (creme e cores de aquarela), sem filtro sépia extra, sob vinheta forte (13 % na borda), sem sombra.
- Receita de ILUSTRAÇÃO (reestudo 20/11): a ilustração é a própria gravura de época; a marcação é uma elipse de traço fino na cor-tema desenhada por cima, revelada por traço que cresce.
- Teste de generalização: reel sobre Claude Code: "o segredo está numa camada escondida" → página de um artigo científico antigo sobre redes neurais desliza por cima e uma elipse na cor-tema marca o diagrama da camada. Reel sobre café: "o segredo está na película da semente" → prancha botânica antiga do cafeeiro desliza e a elipse marca a película.

- Confiança: tempos e curva medidos; cor e caixa da elipse medidas; margens e inclinação da página observadas.
