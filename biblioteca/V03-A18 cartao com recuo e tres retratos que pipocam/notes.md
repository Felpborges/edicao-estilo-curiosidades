# V03-A18 · cartão já visto (callback) com recuo de câmera + três retratos que pipocam (evolução no tempo)
- Categoria: P08 · Pilha de cartões (provisória do analista: (provisória) cartão tela cheia → recuo → pilha de cartões (antes × depois))
- Fonte: V03 quadros f2196–f2338 (91,61–97,51 s; 143 quadros ≈ 5964 ms) · 23,976 fps
- Fala: "Charles II wore a black wig to hide his gray. A few decades later, the most fashionable hair in Europe was white."
- Tipo de fala: callback + comparação no tempo ("antes" → "décadas depois")
- Gatilho: corte seco em f2196 (91590 ms), 100 ms ANTES do início da palavra nº 308 "Charles" (91690 ms).
- Quadro-chave: f2320
- Camadas ativas: cena de corte (cartões) | legenda
- Leitura dos strips: strip.jpg = f2194 a f2204, de 1 em 1, 8 colunas, linha a linha (corte); strip-saida.jpg = f2260 a f2302, de 1 em 1 (os três retratos pipocam); strip-geral.jpg = f2194 a f2338, de 4 em 4. Detalhe do reestudo: detalhe-canto-sombra.jpg = quadro f2320, região x90 y370 170x130 px, ampliada 3× sem suavizar (canto do último retrato por cima do anterior: borda de papel pontilhada e a sombra difusa sobre o cartão de baixo).

## LEITURA DE EDITOR
- Por que esta cena aqui: a frase compara duas épocas; o "antes" é uma imagem que o público já viu (callback), então ela volta sem estalo e recua para dar lugar ao "depois".
- Por que este design: o cartão antigo fica no fundo da pilha e três exemplos novos o cobrem um a um; a pilha mostra que o "depois" virou moda (vários casos), não um caso isolado.
- Por que estas cores: retratos com a cor original; o contraste narrativo (peruca preta × perucas brancas) vem das próprias imagens, e a mesa quase preta deixa os brancos saltarem.
- Por que estes efeitos: borda de papel ≈ 8 px e sombra que cai para baixo (≈ 17 px) entre cartões separam retratos de tons parecidos; nenhum outro efeito.
- Por que este movimento: o recuo (−19 a −24 %/s) abre espaço enquanto os exemplos entram; quando o último entra, a câmera inverte e mergulha nele (+32 a +41 %/s) na palavra "white", o dado da frase.
- Sensação do movimento: de "abrir o arquivo" e depois "fechar no achado"; produzida pela inversão da câmera (recuo que desacelera → push-in forte) e pelos 3 estalos a cada ≈ 0,7 s.

## FORMA (fixa: reproduzir igual)
- Design: o MESMO cartão do personagem da V03-A14 (reaproveitado ≈ 30 s depois), quase tela cheia sobre o fundo escuro #10110c (f2320, x360 y1240 e x40 y1100) (medido). Três retratos novos em cartões de borda branca grossa (#e8e6e0), em cascata para baixo: 2º embaixo-direita, 3º embaixo-esquerda, 4º embaixo-direita por cima; o último vai de x138 a x645 e de y407 a y958 em f2320 (507 × 551 px = 70,4 % × 43,0 %), centro (54,3 %, 53,3 %), borda de 8 px, girado ≈ 1,5° horário (remedido, f2320, saltos de borda nas linhas y500/y700/y900 e colunas x250/x550; antes: 397 × 526 px, 55,1 % × 41,1 %, centro 47,0 %/52,3 %, blob da borda); todos girados alternadamente (observado). Sem etiqueta.
- Movimento: corte seco sem estalo (pico f2196 = 67,9, depois < 7) (medido). Recuo de câmera f2221–f2261 (41 q ≈ 1,71 s): diferença 13 → 24,1 (f2236–f2237) → 17,5, lento-rápido-lento; o cartão encolhe e sobe abrindo espaço embaixo (medido pelo perfil; direção observada). Retratos pipocam com estalo de 2 degraus: f2262 (30,0 / 18,6 em f2264), f2281 (27,8 / 15,3 em f2283), f2297 (24,3 / 15,1 em f2299) (medido). Câmera deriva o resto da cena (dif 12–13 constante = velocidade linear) (medido). (corrigido no reestudo, f2266–f2338: a dif constante esconde uma inversão; pela `camera`, o recuo segue até ≈ f2297 desacelerando, −24,0 %/s em f2266–f2279 e −6,6 %/s em f2285–f2296, e de ≈ f2300 ao corte vira PUSH-IN forte, +41,1 %/s em f2302–f2320 e +32,3 %/s em f2322–f2338.) Saída: corte seco para o A-roll em f2339.
- Passos internos:

| passo | quadro início | duração | tipo | palavra-gatilho (nº) | deslocamento |
|---|---|---|---|---|---|
| cartão (callback) | f2196 | — | corte seco | o nome da pessoa do callback (308) | −100 ms |
| recuo de câmera | f2221 | 41 q (1,71 s) de pico; o recuo continua mais lento até ≈ f2297 (corrigido no reestudo) | zoom-out lento-rápido-lento | a cor do "antes" (312, 92620 ms) | +25 ms |
| retrato 2 | f2262 | 4 q | pop | o salto no tempo (320, 94320 ms) | +27 ms |
| retrato 3 | f2281 | 4 q | pop | o superlativo (323, 95100 ms) | +37 ms |
| retrato 4 | f2297 | 4 q | pop | o objeto da moda (325, 95840 ms) | −37 ms |
| push-in forte no retrato 4 | ≈ f2300 | 38 q até o corte | zoom +32 a +41 %/s (reestudo, `camera`) | o objeto da moda e a cor do "depois" | — |

- Ritmo: 1º cartão sozinho 1,04 s antes do recuo; os 3 retratos em 1,46 s (um a cada ≈ 0,7 s); pilha completa ≈ 1,7 s até o corte (sempre derivando).
- Som: nenhum efeito detectado (áudio mono, só voz) (medido).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- (correção da conferência, 2026-11-20: falas, nomes e objetos usados como âncora de tempo ou como descrição na FORMA e na CONSTRUÇÃO trocados pelo PAPEL; a fala literal fica só em Fala, Gatilho e CONTEÚDO)
- Textura (reestudo 20/11):
  - mesa: liso, #12130e (f2290, x40 y990 640x260), grão 0,32 níveis, manchas 0,34, ac1 +0,52 (compressão), grão cinza (0,32 nos 3 canais); PARADA na tela (f2290 × f2300 +0,80; f2304 × f2316 +0,76 com a câmera em push-in ×1,17: as faixas de luma 22/21/19/17/16 ficam idênticas). Degradê vertical 25 → 17 do pé das peças à borda de baixo; horizontal quase plano (18–21, um pouco mais claro no meio).
  - borda de papel dos cartões: papel com pontilhado (detalhe-canto-sombra), ≈ 8 px, clara (#d0cac0 aprox.), fio cinza de ≈ 1 px por fora.
  - imagens: pintura a óleo e pastel com a textura original; fundo marrom do último retrato #755e36 (f2320, x560 y470 70x90), grão 2,40 níveis, manchas 2,56, ac1 +0,56, grão cinza; anda com a câmera (muda de escala, por isso a correlação simples dá −0,03). GRÃO VIVO por cima, nos claros (corrigido na conferência: era "grão global: nenhum"): f2290×f2291 alinhado pela afim da peça (×1,0029, 517 pontos), resíduo do grão fino 5,6 níveis nos claros (|dif| 7,2) × 0,45 nos escuros; f2290×f2292 6,8 × 0,5 (piso sem grão: A-roll f2150×f2151, 0,57 nos claros) (medido).
- Efeitos (reestudo 20/11):
  - vinheta global: nenhuma radial; o quadro f2290 escurece do centro (98) para a borda (25), mas é a mesa preta em volta das peças, não um escurecimento aplicado (a mesa tem 18–21 de luma de lado a lado).
  - vinheta da imagem: nenhuma.
  - sombra: cai para BAIXO (corrigido na conferência: era "difusa em volta, 15–25 %, sem deslocamento visível"). Último cartão em f2320, perfil alinhado na borda real nos 4 lados (caixa 138,407,507,551): embaixo, sobre a mesa, −52 % colado à borda (22 → 10 de luma), volta em 17 px; à direita, sobre a mesa, −33 %, 10 px; à esquerda, sobre o retrato de baixo, −31 %, 15 px; em cima −13 % (medido). Leitura: preta, forte e longa embaixo, média dos lados, fraca em cima.
  - fio na borda: fio cinza de ≈ 1 px. Grão global: vivo nos claros das imagens (ver Textura; corrigido na conferência: era "nenhum"). Brilho, halo, desfoque de movimento, profundidade, aberração: nenhum (medido no detalhe f2320; pops sem borrão na folha geral).
- Câmera (reestudo 20/11): muda de direção 2 vezes. f2200→f2218: push-in leve +5,0 %/s (o callback "respira"). f2226→f2256: recuo −19,4 %/s com a cena subindo 5,8 px/q. f2266→f2279: recuo −24,0 %/s (sobe 5,1 px/q). f2285→f2296: recuo desacelera, −6,6 %/s. f2302→f2320: PUSH-IN forte +41,1 %/s indo para o último retrato (centro anda −3,6; −6,3 px/q); f2322→f2338: +32,3 %/s até o corte; remedido sem a faixa da legenda (região 0,0,720,820): f2326→f2338 +29,1 %/s (−3,4; −5,6 px/q) e f2332→f2338 +23,1 %/s: o push-in alivia um pouco nos últimos 6 q mas não para (medido). Giro 0 (±0,03°). A mesa não acompanha (fixa).
- Cadência (reestudo 20/11): 24 imagens/s na câmera (perfil f2300–f2312: 15,2 · 18,2 · 16,0 · 16,7 · 17,7 · 18,3 … sem quadros repetidos); estalos dos retratos em degraus de 2 q (picos f2262/f2264, f2281/f2283, f2297/f2299).
- Legenda nesta cena (reestudo 20/11): 8 blocos (#121–#128), 1–5 palavras (mediana 2,5); #121 entra no quadro do corte (f2196) e #128 sai no corte (f2338): nenhum atravessa. Tarja 73,5 %, altura 46 px (y846–892) (medido na conferência: 73,0–75,1 em 10 quadros do V03; remedido aqui em 7 quadros do lote, 73,0–74,2 onde o fundo é limpo) (corrigido na conferência: era ≈ 71 %, mediana do censo); texto #eee250; centro y 68,1 %. Atrás da tarja: a roupa vermelha e branca do retrato do callback (f2196–f2260, luma fora 100–133: tarja visível como faixa escura), depois a mesa preta (f2262–f2297, luma ≈ 27: tarja some), depois o último retrato que cresce por baixo dela (f2298–f2338). Trocas × pops: o #125 (f2277) entra 4 q antes do retrato 3 (f2281); o #126 (f2286) não coincide com pop; o retrato 4 (f2297) cai 10 q antes do #127 (f2307): legenda segue a fala, os pops seguem a palavra forte. "Texto branco grande" do censo (64 q) = falso positivo (roupas e cabelos brancos das pinturas).

## CONSTRUÇÃO
1. fundo: mesa #12130e, camada FIXA na tela (não anda nem cresce com a câmera), degradê vertical luma 25 → 17 de cima para baixo na metade de baixo; sem textura.
2. grupo da câmera (tudo abaixo anda junto, sem paralaxe interna):
   2a. cartão do "antes" (imagem já vista no vídeo): ocupa a tela toda no corte (sangra nas 4 bordas, f2198), sem estalo, sem borda visível no início.
   2b. retrato 2: ≈ 50 % × 40 % do quadro na hora do pop, embaixo-direita, giro ≈ +2°, borda de papel ≈ 8 px + fio de 1 px, sombra preta caída para baixo: ≈ −50 % e 17 px embaixo, ≈ −30 % e 10–15 px dos lados, ≈ −13 % em cima (corrigido na conferência: era difusa 15–25 %, 15 px em volta). Pop em degraus de 2 q (grande → médio → assentado em 4 q).
   2c. retrato 3: mesmo molde, embaixo-esquerda, giro ≈ −3°, por cima do 2.
   2d. retrato 4: mesmo molde, embaixo-direita por cima de todos; em f2320 (já com push-in) 507 × 551 px = 70,4 % × 43,0 %, centro (54,3 %, 53,3 %), giro ≈ 1,5° horário.
3. câmera do grupo: 0–1043 ms push-in leve +5 %/s; 1043–4213 ms recuo −19 a −24 %/s que desacelera para −6,6 %/s, com a cena subindo ≈ 5 px/q (o "antes" encolhe e sobe, abrindo espaço embaixo); de ≈ 4338 ms até o corte, push-in forte +32 a +41 %/s em direção ao centro do retrato 4 (a cena anda ≈ −3,6; −6,2 px/q), aliviando para ≈ +23 %/s nos últimos 6 q, sem parar. Curvas: rampas suaves, sem paradas.
3b. grão vivo por cima das imagens (não da mesa): ruído cinza de 1–2 px, novo a cada quadro, ≈ 5–7 níveis nos claros, ≈ 0 no preto (corrigido na conferência: faltava).
4. legenda (V03-L01) fixa por cima, tarja preta 73,5 %, 46 px.
- Linha do tempo (ms a partir do corte): 0 callback · 1043 começa o recuo · 2753 retrato 2 · 3545 retrato 3 · 4213 retrato 4 · ≈ 4338 câmera inverte para push-in · 5964 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: quantos exemplos do "depois" (3 aqui), em que palavras pipocam (as palavras fortes da 2ª frase), o tamanho do callback (mesmo enquadramento da 1ª aparição), para qual exemplo a câmera mergulha (o último, que carrega o dado).
- O que NÃO fazer: dar estalo no callback (ele volta por corte seco simples); manter a câmera em velocidade constante (aqui ela recua, desacelera e inverte); fazer a mesa crescer com o zoom; centralizar os retratos novos (eles caem em cascata alternando lados); sombra igual nos 4 lados (ela cai para baixo); imagens sem grão ou com grão parado.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: (1) imagem do "antes" (já mostrada no vídeo); (2)–(4) três imagens do "depois", de pessoas/casos diferentes da mesma época nova.
- Nesta referência as lacunas foram preenchidas com: o retrato do rei de peruca preta; três retratos de nobres de peruca branca.
- Receita de tratamento de cada imagem: retratos de busto em cor natural, cartões de borda branca grossa girados alternadamente; o "antes" reaproveitado com o mesmo tratamento da 1ª aparição.
- Regra de escolha: MUDANÇA NO TEMPO ("X did A. A few decades later, everyone did B") → o "antes" (callback) recua e vários exemplos do "depois" pipocam por cima, um por palavra forte. Em outros temas: reel sobre Claude Code, "em 2023 todo mundo usava ChatGPT no navegador; um ano depois, o terminal virou moda" → print antigo recua, 3 prints de terminais pipocam; reel sobre café, "no começo era coado; décadas depois, todo mundo queria espresso" → foto do coador recua, 3 fotos de espresso pipocam.
- Receita de tratamento de cada imagem (reestudo 20/11): retratos de busto com a cor original e a textura da pintura (grão 2,4 níveis no fundo liso), sem dessaturar, sem vinheta própria, com o grão vivo do grupo nos claros (corrigido na conferência: era "sem grão acrescentado"); enquadramento de busto com a cabeça no terço de cima do cartão; borda de papel pontilhado ≈ 8 px + fio de 1 px + sombra caída para baixo.
- Teste de generalização: reel sobre Claude Code → "em 2023 todo mundo programava copiando do chat; um ano depois, o normal era o agente no terminal": print do chat (já mostrado antes) recua, três prints de terminais de pessoas diferentes pipocam, câmera mergulha no último na palavra "terminal". Reel sobre café → "nossos avós tomavam coado; décadas depois, a moda era espresso": foto do coador (callback) recua, três fotos de xícaras de espresso de cafés diferentes, mergulho na última na palavra "espresso".

- Confiança: perfil, estalos, cor e caixa do último cartão = medido; reaproveitamento da imagem, layout e giros = observado.
