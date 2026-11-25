# V01-A06 · foto-vídeo do lugar, entra depois de um "whoosh" borrado
- Categoria: P06 · Imagem em cartão com câmera viva (provisória do analista: (provisória) foto impressa com borda de papel, sozinha (entrada por transição com borrão))
- Fonte: V01 quadros f199–f254 (8,29–10,58 s; 56 quadros ≈ 2333 ms) · 24 fps
- Fala: "And yet, in this, surfers can sit in near"
- Tipo de fala: virada (contraste "e mesmo assim" com prova real)
- Gatilho: entra em f199 = 8292 ms, −38 ms antes da palavra nº 27 "And" (8330 ms); a virada da frase ("and yet") puxa a troca de cena.
- Quadro-chave: f215
- Camadas ativas: cena de tela cheia | legenda | b-roll (vídeo na foto) | transição
- Leitura dos strips: strip.jpg = quadros f193 a f206, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 14 células. strip-geral.jpg = quadros f197 a f255, de 2 em 2, 8 colunas, 30 células. Cada célula traz o nº do quadro e o tempo. Detalhe do reestudo: detalhe-canto-foto.jpg = quadro f215, região x600 y640 110x130 px, ampliada 3× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala vira ("e mesmo assim") do problema para a prova contrária; o editor troca o diagrama por filmagem real em plano aberto e marca a virada com a única transição borrada do trecho.
- Por que este design: foto quase do tamanho da largura (93 %), horizontal, levemente inclinada, sozinha: "isto existe de verdade" em escala grande, sem enfeite.
- Por que estas cores: o azul frio da filmagem (#61779c) carrega "água gelada" sem precisar de diagrama; contra a mesa escura e a borda off-white quente.
- Por que estes efeitos: o borrão de 2 imagens na saída da cena anterior é o "whoosh" visual (sem som) que separa explicação de prova; a foto em si só tem a borda de papel e a sombra caída para baixo (alinhado ao reestudo).
- Por que este movimento: chega grande e assenta em 3 imagens; depois a câmera recua um pouco e volta a avançar devagar enquanto o vídeo corre: a foto respira.
- Sensação do movimento: virada de página rápida e depois contemplação; produzida por 2 imagens borradas (f195, f197), foto 110,7 → 103,7 → 100,4 → 100 % em 3 imagens de 12/s, e deriva −2 % / +4,6 % por segundo.

## FORMA (fixa: reproduzir igual)
- Design (f215, quadro cheio): foto horizontal com borda de papel off-white de ≈ 8 px (topo y239–246 na coluna 360, cor #b9bcc4 aprox. em f203); caixa x20–689, y241–752 = 670x512 px (93,1 % da largura, 40,0 % da altura), centro (50,3 %, 38,8 %); inclinada ≈ 1,1–1,3° no sentido anti-horário (borda de cima sobe para a direita). Dentro, vídeo real em tom frio azulado. Fundo escuro de sempre. (medido com med.py e inc.py)
- Movimento:
  - Transição de entrada: a cena anterior (V01-A03) faz um "whoosh" de 2 imagens com borrão de movimento (f195, f197); em f199 a foto já cobre a tela, maior (714 px de largura) e com um pedaço do disco anterior ainda escapando pelo canto inferior esquerdo; assenta em 3 imagens: largura f199 714 → f201 690 → f203 684 → f205 681 px (≈ 105 → 101 → 100 %). Curva de estalo. (medido)
  - Permanência: a câmera respira em 3 fases, recua −2 %, para e avança +4,6 %/s, ver Câmera (alinhado ao reestudo) (largura 670–700 px, leve giro), vídeo correndo dentro. (medido)
  - Saída: corte seco em f255 para V01-A07. (medido)
  - Cadência: 12 imagens/s. (medido)
- Ritmo: 2333 ms na tela; assentada de f205 a f254 = 2083 ms. Desde o evento anterior (lupa A05): 1333 ms. (medido)
- Som: nenhum efeito detectado no whoosh (áudio mono; o meio só mostra a voz em f193–f200). (medido)
- Textura (reestudo 20/11):
  - Fundo: a mesa de V01-A01 (parada, poça de luz).
  - Borda de papel: off-white #e3e2d4–#e8e3d3, luma 222–227, 7 px (`sombra` baixo em x300–360: +39…+45), grão fino visível no detalhe, canto vivo.
  - Imagem (vídeo): família foto de câmera, `textura` f215 em 100,300,200,100: #61779c, grão 9,2, manchas 6,3, ac1 +0,60, direção horizontal forte (h +0,94 × v +0,26: são as ondas), grão cinza. Teste novo de grão (f215×f217, alinhado pela afim da foto, região 60,280,600,440, pixels lisos): resíduo ÷ σ 1,29 nos claros, 1,27 nos médios, 1,16 nos escuros: igual em todas as faixas, então não há camada de grão vivo só nos claros; o resíduo é o movimento do próprio vídeo (medido; inconclusivo para grão sobreposto).
- Efeitos (reestudo 20/11):
  - Sombra da foto: CAI PARA BAIXO. `sombra` alinhada na borda real (f215, caixa 20,241,670,512): embaixo −56 % no 1º px fora (luma 15 × 33) e volta ao fundo em 20 px; em cima −14 % só no 1º px, volta em 7 px; direita −40 % (luma 21 × 35, linhas y450–520), volta em ≈ 12 px; esquerda −32 % (23 × 34), volta em ≈ 15 px (a borda do quadro fica a 20 px). (medido; corrigido na conferência: era "1 px −45 %, retorno em ≈ 15 px, sem deslocamento", medido só embaixo)
  - Vinheta da imagem (`borda` f215): 100 / 95 / 98 / 94 / 101 %, nitidez 94–117 % → nenhuma vinheta nem borda borrada.
  - Desfoque de movimento: só na transição de entrada (é a saída de V01-A03 em f195 e f197; ver lá); a foto chega nítida já em f199.
  - Brilho, profundidade, grão global, aberração: nenhum (f215).
- Câmera (reestudo 20/11): altura da foto medida na coluna x360: f199 561 px → f201 526 → f203 509 → f205 507 (assenta) → f217 497 (−2 % em 0,5 s, recua) → f229 498 (para) → f241 510 → f253 521 (+4,6 % no último 1 s, avança). `camera` f241→f253: ×1,0273 (+5,5 %/s), sobe 1,3 px/q. Respira: recua, para e avança, sem voltar a zero. A posição desce ≈ 9 px na assentada (topo y210 → y240) e depois sobe 24 px no avanço. Fundo parado.
- Cadência (reestudo 20/11): 12 imagens/s na foto e no vídeo de dentro (`perfil` f207–f214: 11,4 / 0,00 / 10,9 / 0,00 / 11,1 / 0,05 / 10,9 / 0,00).
- Legenda nesta cena (reestudo 20/11): 4 blocos: a virada (f198–f208, 2 palavras, entra 1 quadro ANTES da foto, ainda sobre o borrão da cena anterior), o apontador da prova (f209–f219, 2 palavras), quem age (f220–f238, 3 palavras), onde age (f239–f265, 4 palavras, atravessa o corte de saída f255 por 11 quadros, uma das 3 exceções do vídeo). Atrás da tarja: só a mesa escura (a foto termina em y≈746–770); tarja preta pura lida como preta (luma 7 × 28; opacidade do vídeo 74 %, medida direta da conferência). Nenhum outro texto.

## CONSTRUÇÃO
1. fundo: mesa fixa.
2. foto: retângulo horizontal ≈ 4:3, caixa x20–689 y241–752 (93,1 % × 40 %, centro 50,3 % × 38,8 %), borda off-white 7 px de canto vivo, sombra caída para baixo: embaixo −56 % no contato, some em 20 px; dos lados −32/−40 %, some em 12–15 px; em cima só 1 px (corrigido na conferência: era "sombra de contato de 1 px (−45 %) dissolvendo em 15 px"); inclinação −1,2° (anti-horário). Vídeo dentro, reamostrado a 12/s.
3. entrada: no 1º quadro depois do borrão (0 ms = f199) a foto já cobre a tela com 110,7 % (altura 561 px), deslocada para cima e à esquerda, e um pedaço do disco anterior escapa no canto inferior esquerdo; 83 ms 103,7 %; 167 ms 100,4 %; 250 ms 100 %. Desaceleração forte, sem sobra.
4. câmera da foto: 250–750 ms recua 2 %; 750–1250 ms parada; 1250–2333 ms avança +4,6 %/s subindo 1,3 px/q. Fundo parado.
5. saída: corte seco em 2333 ms (f255).
- Linha do tempo (ms a partir de f199): −42 legenda da virada · 0 foto 110,7 % · 250 assentada · 417 legenda do apontador · 875 legenda de quem age · 1667 legenda de onde age · 2333 corte seco (a legenda continua 11 quadros na cena seguinte).
- Parâmetros que dependem do conteúdo: proporção da imagem; lado da inclinação (alterna com a foto anterior: A02 +1,7°, aqui −1,2°); vídeo ou foto.
- O que NÃO fazer: sombra simétrica em volta (cai para baixo); transição de whoosh com som ou com rastro direcional longo (são 2 imagens de borrão uniforme); foto a 100 % parada; inclinar sempre para o mesmo lado; vídeo a 24/s.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o lugar/situação extrema que prova a frase": vídeo real, plano aberto.
- Nesta referência as lacunas foram preenchidas com: surfistas sentados nas pranchas em mar frio.
- Receita de tratamento de cada imagem: vídeo real em plano aberto, cor fria um pouco dessaturada (observado), horizontal, impresso com borda de papel de 8 px e sombra caída para baixo (20 px embaixo, 12–15 nos lados, 1 em cima; corrigido na conferência: era "sombra fina"), inclinado ~1°. (reestudo 20/11) Medido: azul frio #61779c com saturação média-baixa, contraste baixo, grão da filmagem 9,2 níveis, sem vinheta, nítido; borda off-white 7 px luma ≈ 225; vídeo a 12 imagens/s.
- Regra de escolha: literal da situação narrada, em plano aberto, para dar escala ("surfistas ficam horas em água gelada" → surfistas na água).
- Teste de generalização: (1) Claude Code: "e mesmo assim, empresas inteiras rodam isso em produção" → vídeo aberto de um escritório/sala de servidores. (2) café: "e mesmo assim, baristas tiram 500 cafés por dia" → vídeo aberto de um balcão cheio.

- Confiança: tamanhos, tempos, inclinação medido; tom de cor observado; borrão do whoosh observado no strip.
