# V01-A21 · transição em chicote para a esquerda (2ª data da linha do tempo)
- Categoria: P11 · Viagem de câmera entre peças (provisória do analista: (provisória) transição: deslize horizontal com borrão de movimento (chicote), trocando de foto)
- Fonte: V01 quadros f1439–f1451 (59,96–60,46 s; 13 quadros ≈ 542 ms) · 24 fps
- Fala: "1945,"
- Tipo de fala: data (2ª data da sequência)
- Gatilho: começa em f1439 = 59958 ms, +18 ms depois do início da palavra nº 190 "1945," (59940 ms).
- Quadro-chave: f1443
- Camadas ativas: transição | cena de tela cheia | grafismo (linha do tempo, ponto anda) | legenda
- Leitura dos strips: strip.jpg = quadros f1436 a f1453, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 18 células; cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-borrao-chicote.jpg = quadro f1443, região x0 y150 720x560 px, ampliada 1× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: nova data falada ("1945") = nova estação; o mesmo chicote de V01-A19 repete a regra e o espectador já entende "o tempo andou".
- Por que este design: nenhum elemento próprio; a régua embaixo é o que muda (o ponto corre para o ano novo).
- Por que estas cores: as das fotos.
- Por que estes efeitos: borrão horizontal só nas imagens rápidas (no detalhe f1443: rastro de ≈ 20–30 px nas bordas verticais das fotos).
- Por que este movimento: rápido e freando forte, junto com o ponto da régua, para que imagem e régua contem o mesmo salto.
- Sensação do movimento: "pulou para a próxima data"; produzida por passos de −52 → −26 → −8 px na chegada e diferença por imagem 51 → 59 → 45 → 25 → 16 → 14 → 12 a 12/s.

## FORMA (fixa: reproduzir igual)
- Igual a V01-A19 (conferido em 3 medidas: saída para a esquerda com borrão, foto nova chega pela direita freando, linha do tempo parada). Diferença: aqui o ponto da linha do tempo anda do ano da estação anterior para o ano novo junto com o deslize (ver V01-A25).
- Movimento (med.py, região acima da linha do tempo):
  - Saída: f1441–f1443 o conteúdo cobre a tela toda com rastro (caixa x0–719). (medido)
  - Entrada: borda esquerda da foto nova f1445 x128 → f1447 x76 → f1449 x50 → f1451 x42 (passos 52, 26, 8 px: ease-out forte). (medido)
  - Duração f1439 → f1451 ≈ 12 q (500 ms), 12 imagens/s. (medido)
  - Ponto da linha do tempo: diferença na faixa da linha de f1439 a f1449 (2–5 por imagem), ou seja, o ponto anda junto com o deslize (pela posição, de f1437 a f1451, ver V01-A25) (alinhado ao reestudo). (medido)
- Ritmo: 4,2 s depois do chicote anterior (V01-A19). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11): sem superfície própria; mesa parada por trás, fotos com borda off-white e grão de arquivo (a foto nova é filmagem P&B).
- Efeitos (reestudo 20/11): desfoque de movimento horizontal nas imagens rápidas (f1441–f1445; detalhe f1443: bordas verticais das fotos com rastro de ≈ 20–30 px, horizontais nítidas); nítido na chegada (f1449–f1451). Sem fade, sem escala. Vinheta, brilho, grão global, aberração: nenhum.
- Câmera (reestudo 20/11): deslize horizontal puro (sem escala nem giro), fotos para a esquerda; mesa e régua paradas. Foto nova (linha y400): f1445 borda esquerda x137 → f1447 x84 → (medida antiga) f1449 x50 → f1451 x42.
- Cadência (reestudo 20/11): 12 imagens/s: `perfil` f1438–f1452: 0,02 / 51,2 / 2,6 / 59,2 / 0,04 / 45,3 / 0,04 / 25,0 / 0,04 / 16,3 / 0,04 / 13,7 / 0,04 / 11,6 / 0,06 (o resíduo 2,6 em f1440 é o ponto da régua, que anda nos mesmos passos).
- Legenda nesta cena (reestudo 20/11): o bloco da data (2 palavras) entrou em f1435, 4 quadros ANTES do chicote, e vai até f1453; o bloco seguinte (sujeito + verbo, 2 palavras) entra em f1454, depois que a foto assentou. Atrás da tarja: a mesa → tarja preta pura lida como preta (74 % no vídeo, medida direta da conferência); a régua 42 px acima.

## CONSTRUÇÃO
1. igual a V01-A19, com: fotos da estação anterior saem para a esquerda de 0 ms (f1439) a ≈ 250 ms, com borrão de ≈ 20–30 px; foto nova chega pela direita freando (x137 em 250 ms, x84 em 333 ms, x50 em 417 ms, x42 em 500 ms).
2. régua: o ponto corre do ano 1 ao ano 2 nos mesmos quadros (ver V01-A25: x164 → 250 de f1437 a f1451).
- Linha do tempo (ms a partir de f1439): −167 legenda da data · −83 ponto começa a sair · 0 chicote · 83–167 pico · 500 foto assentada · 500 ponto no ano novo · 625 legenda seguinte.
- Parâmetros que dependem do conteúdo: as fotos de saída e chegada; a distância que o ponto anda (proporcional aos anos).
- O que NÃO fazer: chicote sem o ponto da régua andar junto; borrão vertical ou em todas as imagens; mudar a direção (é sempre para a esquerda).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: nenhuma imagem própria.
- Nesta referência as lacunas foram preenchidas com: (não se aplica)
- Receita de tratamento de cada imagem: não se aplica.
- Regra de escolha: nova data falada = novo chicote para a esquerda + ponto da linha do tempo anda até a data.
- Teste de generalização: (1) Claude Code: "em 2023," → chicote para o print do lançamento de 2023, ponto anda. (2) café: "em 1884," → chicote para a foto da 1ª máquina, ponto anda.

- Confiança: posições e tempos medido; borrão observado.
