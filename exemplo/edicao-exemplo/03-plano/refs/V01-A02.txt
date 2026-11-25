# V01-A02 · foto-vídeo impressa, inclinada, com borda de papel
- Categoria: P06 · Imagem em cartão com câmera viva (provisória do analista: (provisória) foto (ou vídeo dentro da foto) impressa com borda de papel, sozinha no fundo escuro)
- Fonte: V01 quadros f55–f89 (2,29–3,71 s; 35 quadros ≈ 1458 ms) · 24 fps
- Fala: "The second you jump in,"
- Tipo de fala: ação narrada
- Gatilho: corte seco em f55 = 2292 ms, −48 ms antes do início da palavra nº 8 "The" (2340 ms); envelope confirma a voz subindo em f55–f56 (−35 → −16 dB). Entra no começo da frase que descreve a ação.
- Quadro-chave: f70
- Camadas ativas: cena de tela cheia | legenda | b-roll (vídeo dentro da foto)
- Leitura dos strips: strip.jpg = quadros f53 a f64, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 12 células; cada célula traz o nº do quadro e o tempo. strip-saida.jpg = quadros f81 a f92, mesma regra, 12 células. Detalhe do reestudo: detalhe-borda-papel.jpg = quadro f70, região x40 y150 130x130 px, ampliada 3× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala passa do objeto para a ação ("no segundo em que você pula"); o editor troca o objeto parado por gente fazendo a ação, em filmagem real, para o espectador se pôr no lugar.
- Por que este design: foto impressa sozinha, horizontal e grande (86 % da largura), no terço de cima: lê-se como "prova" de álbum; a inclinação de 1,7° tira a cara de tela e põe a de papel colado à mão.
- Por que estas cores: a cor da própria filmagem, fria e levemente apagada (mar cinza-azulado #7b8591), contrasta com a borda off-white quente e com a mesa quase preta.
- Por que estes efeitos: a borda de papel com fio escuro e a sombra caída para baixo (alinhado ao reestudo): o mínimo para a foto parecer um objeto físico; sem vinheta aplicada nem brilho.
- Por que este movimento: a foto cai grande e girada e assenta em 3 imagens (estalo), depois a câmera se afasta devagar enquanto o vídeo de dentro corre: duas camadas de vida (a ação e o papel).
- Sensação do movimento: "jogou a foto na mesa" seguido de um recuo suave; produzida pelo salto 112,7 → 104,1 → 100,3 % com giro 4,1° → 1,7° em 3 imagens de 12/s e pelo zoom out de ≈ −5 %/s.

## FORMA (fixa: reproduzir igual)
- Design (f70, quadro cheio):
  - Fundo escuro igual ao de V01-A01 (#151112 → #221e1f, degradê vertical). (medido em A01, mesmo fundo)
  - Foto horizontal com borda de papel off-white de 8 px (1,1 % da largura): topo y171–178 na coluna 360 e esquerda x56–63 na linha 400; cor da borda #a5a7ac a #d5d0c8 conforme a luz (luminância 170–213); logo fora da borda, sombra caída para baixo (19 px embaixo, 11 nos lados, 1 px em cima) (alinhado ao reestudo). (medido)
  - Caixa da foto girada: x50–669, y163–639 = 620x477 px (86,1 % da largura, 37,3 % da altura), centro (50,3 %, 31,4 %). (medido com med.py)
  - Inclinação assentada ≈ 1,7° no sentido horário (borda de cima desce para a direita; f59 1,6–1,7°, f70 1,6–1,8°). (medido com inc.py)
  - Conteúdo da foto anda (vídeo dentro da moldura): diferença 4–6 a cada imagem. (medido)
- Movimento:
  - Entrada: corte seco já com a foto maior e mais girada, assentando em 3 imagens (6 quadros, 250 ms): largura f55 712 px (112,7 %) → f57 658 (104,1 %) → f59 634 (100,3 %) → f61 632 (100 %); giro f55 4,1° → f59 1,7°. Curva: desaceleração forte (salto grande na 1ª imagem, depois pequenos), sem sobra. (medido)
  - Cadência: 12 imagens/s (diferença ≈ 0 nos quadros pares f56, f58, f60…). (medido)
  - Permanência: deriva lenta para TRÁS (afasta): largura 632 → 606 px de f61 a f81 (−4,1 % em 0,83 s) e sobe 26 px (y174 → y148). (medido)
  - Saída: a próxima cena (V01-A03) cai por cima em f83 e esta foto desliza para a ESQUERDA por baixo dela até sumir: visível na borda esquerda de f83 a f89 (4 imagens ≈ 292 ms), some em f90. (observado no strip-saida)
- Ritmo: 1458 ms na tela; assentada e legível de f61 a f82 = 917 ms. Desde o evento anterior (A01): 1583 ms. (medido)
- Som: nenhum efeito detectado (áudio mono; meio só com voz). (medido)
- Textura (reestudo 20/11):
  - Fundo (mesa): o mesmo de V01-A01, papel escuro quase liso: `textura` f70 em 100,680,500,140 #242020, grão 0,33, manchas 0,65, ac1 +0,55, PARADA (f70×f80 +0,74). A poça de luz é a MESMA de A01 e não segue a foto (coluna x25 em f70: 17 / 28 / 36 em y480 / 28 / 14, idêntica a f40 com o disco no meio): a luz é do fundo, fixa.
  - Borda de papel: família papel fotográfico (off-white liso com grão leve), luma 223–233 (#ebe2d6), 7 px de largura medidos na base (linha +23…+29 do perfil em x300–340), canto vivo (90°, sem arredondar; detalhe-borda-papel). A cor muda com o ponto (#a5a7ac a #d5d0c8 na nota antiga): é a luz da mesa somada à borda, não uma cor pintada.
  - Imagem (vídeo dentro da foto): família foto de câmera (grão do próprio vídeo, 4,4 níveis, ac1 +0,63, cinza), anda com a câmera e com o vídeo (f70×f72: +0,24 no lugar → +0,79 alinhada). Teste novo de grão (f70×f72, alinhado pela afim da foto, região 120,200,480,380, só pixels lisos): resíduo ÷ σ 1,01 nos claros, 1,02 nos médios e 0,86 nos escuros: sem diferença entre claros e escuros, ou seja, sem camada de grão vivo própria dos claros; o resíduo alto é o movimento do próprio vídeo (inconclusivo para grão sobreposto; medido).
- Efeitos (reestudo 20/11):
  - Sombra da foto: CAI PARA BAIXO. `sombra` nos 4 lados, alinhada na borda real de cada linha (f70, caixa 50,163,620,476, terço central de cada lado): embaixo −53 % no 1º px fora (luma 18,5 × 39,6 do fundo) e volta ao fundo em 19 px; esquerda −27 % e direita −33 %, voltam em 11 px; em cima só 1 px (−18 %) e o fundo já em +2 px. (medido; corrigido na conferência: era "1–2 px escuros, ≈ −30 %, retorno em ≈ 8 px, sem deslocamento visível", medido só embaixo)
  - Fio escuro interno: 2 px mais escuros na foto junto à borda (luma 81 × 92 da rocha, +20…+21).
  - Vinheta da própria imagem (`borda` na região da foto): luma 100 % → 86 % na borda, nitidez estável (98 %): queda pequena, em boa parte do próprio conteúdo (rocha escura embaixo à direita); vinheta aplicada fraca ou nenhuma (inferido).
  - Borda borrada: nenhuma (nitidez da borda 98 % do centro). Brilho/halo: nenhum. Desfoque de movimento na entrada: nenhum (strip f55–f61: cada imagem nítida). Profundidade: nenhuma. Grão global: nenhum além do da filmagem. Aberração: não medida.
- Câmera (reestudo 20/11): zoom out contínuo. `camera` na região da foto f61→f71: ×0,9772 (−5,4 %/s), giro +0,10°; f71→f81: ×0,9775 (−5,3 %/s), giro +0,19°; fim da cena f75→f82 (região 30,140,660,520, sem a faixa da legenda): ×0,9878, −4,1 %/s, giro +0,17° → constante e só levemente mais lento no fim, sem parar antes da saída (medido). A translação medida (+1,9 a +3,2 px/q para a direita) é o vídeo de dentro panorâmico, não a moldura; a moldura sobe ≈ 1,3 px/q (y174 → y148 de f61 a f81, medida antiga). O fundo fica parado: só a foto recua.
- Cadência (reestudo 20/11): 12 imagens/s na moldura E no vídeo de dentro: `perfil` f62–f70 na região da foto: 0,00 nos pares, 8,6–12,4 nos ímpares. O vídeo-fonte foi reamostrado para 12/s junto com a colagem.
- Legenda nesta cena (reestudo 20/11): 3 blocos: o começo da frase (f55–f67, 3 palavras, entra no MESMO quadro do corte), o verbo da ação (f68–f79, 2 palavras) e o complemento (f80–f96, 2 palavras, atravessa a chegada de V01-A03 em f83). Cor #ebe055 (f70). Tarja preta pura sobre o fundo escuro: luma 7 × 26 fora (opacidade não medível aqui); no vídeo, medida direta 74 %, altura 46 px (medido na conferência; corrigido na conferência: era "censo ≈ 70 %"). Atrás da tarja só a mesa: a foto termina em y639, 210 px acima. Nenhum outro texto.

## CONSTRUÇÃO
1. fundo: a mesa fixa de V01-A01 (escuro #151112–#221e1f com poça de luz em y≈37,5 %, parada).
2. foto: retângulo 4:3 horizontal com a imagem (vídeo) dentro, caixa girada x50–669 y163–639 (86,1 % da largura, centro 50,3 % × 31,4 %), borda de papel off-white #ebe2d6 de 7–8 px de canto vivo, fio escuro de 2 px por dentro e sombra caída para baixo por fora: embaixo −53 % no contato, some em 19 px; nos lados −27/−33 %, some em 11 px; em cima só 1 px (corrigido na conferência: era "sombra de contato de 1–2 px (−30 %) se dissolvendo em 8 px"). Inclinação final +1,7° (horário). Entrada no corte (0 ms) com 112,7 % e 4,1°; 83 ms 104,1 %; 167 ms 100,3 % e 1,7°; 250 ms 100 % (desaceleração forte, sem sobra).
3. vídeo dentro da foto: corre do começo ao fim, reamostrado a 12 imagens/s.
4. câmera: de 250 ms até a saída, zoom out da foto a −5,3 %/s, quase linear (−4,1 %/s nos últimos 7 quadros), subindo ≈ 1,3 px/q; fundo parado.
5. saída: em 1167 ms (f83) a cena seguinte cai por cima e esta foto desliza para a esquerda por baixo dela, visível na borda até 1458 ms (f89).
- Linha do tempo (ms a partir do corte f55): 0 foto 112,7 %/4,1° + 1º bloco de legenda (começo da frase) · 83 104,1 % · 167 100,3 %/1,7° · 250 assentada, começa o zoom out · 542 2º bloco (o verbo da ação) · 1042 3º bloco (o complemento) · 1167 cena seguinte por cima, esta desliza à esquerda · 1458 some.
- Parâmetros que dependem do conteúdo: proporção da imagem (aqui 4:3 horizontal; vertical pede largura ≈ 60–70 %), o lado da inclinação (alterna entre fotos seguidas), se é vídeo ou foto parada.
- O que NÃO fazer: vídeo a 24 imagens/s dentro de uma colagem a 12; borda branca pura ou com cantos arredondados; sombra simétrica em volta ou só de contato (ela cai para baixo: 19 px embaixo, 11 nos lados, 1 px em cima; corrigido na conferência: era "não fazer sombra grande deslocada (é 1–2 px de contato)"); assentar com curva suave em 10+ quadros (são 3 imagens); centralizar a foto no meio da tela (fica no terço de cima, longe da legenda).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "imagem da ação descrita na frase": vídeo curto (ou foto) real da situação que a fala narra.
- Nesta referência as lacunas foram preenchidas com: vídeo de um surfista de roupa de borracha pulando de uma pedra no mar.
- Receita de tratamento de cada imagem: vídeo/foto real, cor original levemente dessaturada (observado), enquadramento horizontal 4:3 aproximado, ação no centro; impresso como foto de papel com borda off-white de 8 px e sombra caída para baixo (19 px embaixo, 11 nos lados, 1 em cima; corrigido na conferência: era "sombra fina"); inclinado ~2°. (reestudo 20/11) Medido: tons frios e apagados (céu/mar #7b8591, saturação baixa), contraste médio, grão só o da filmagem (4,4 níveis), sem vinheta aplicada (queda de 14 % para a borda vem do conteúdo), sem desfoque; borda off-white 7 px luma ≈ 228 de canto vivo; vídeo reamostrado a 12 imagens/s.
- Regra de escolha: ilustração literal da ação narrada ("você pula na água" → alguém pulando na água), em filmagem real.
- Teste de generalização: (1) Claude Code: "no segundo em que você dá enter…" → vídeo de tela com o terminal rodando, em moldura de foto inclinada. (2) café: "no segundo em que a água toca o pó…" → vídeo do café sendo coado, mesma moldura.

- Confiança: tamanhos, ângulos e tempos medido; cor exata da borda medido em 2 pontos; dessaturação e saída para a esquerda observado.
