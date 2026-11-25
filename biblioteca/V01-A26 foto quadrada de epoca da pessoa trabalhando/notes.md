# V01-A26 · foto quadrada de época: a pessoa trabalhando (abre o "momento da ideia")
- Categoria: P06 · Imagem em cartão com câmera viva (provisória do analista: (provisória) foto impressa com borda de papel, sozinha)
- Fonte: V01 quadros f1671–f1722 (69,63–71,75 s; 52 quadros ≈ 2167 ms) · 24 fps
- Fala: "On June 21st, 1951,"
- Tipo de fala: data
- Gatilho: corte seco em f1671 = 69625 ms, −105 ms antes da palavra nº 221 "On" (69730 ms).
- Quadro-chave: f1700
- Camadas ativas: cena de tela cheia | legenda | b-roll
- Leitura dos strips: strip.jpg = quadros f1669 a f1681, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 13 células. strip-geral.jpg = quadros f1669 a f1723, de 2 em 2, 28 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-canto-borda.jpg = quadro f1700, região x90 y150 150x130 px, ampliada 4× sem suavizar · detalhe-fundo-realce.jpg = quadro f1700, região x0 y1080 300x180 px, ampliada 2× sem suavizar, contraste ×6 em volta da média.


## LEITURA DE EDITOR
- Por que esta cena aqui: a fala dá uma data exata, que marca o "momento da virada"; a imagem é a pessoa trabalhando, para a data ter um rosto antes de a ideia aparecer.
- Por que este design: uma foto só, quadrada e centrada, sem rótulo: a data já está na legenda e a foto só precisa dizer "foi aqui, foi ele".
- Por que estas cores: P&B neutro de arquivo sobre a mesa escura; o branco da roupa é o ponto mais claro da tela e puxa o olho para a pessoa.
- Por que estes efeitos: borda de papel e sombra caída para baixo (≈ 18 px embaixo, nada em cima) (alinhado ao reestudo) fazem a foto ser um objeto impresso; os pontos de poeira da própria foto confirmam que é documento de época.
- Por que este movimento: estalo curto na entrada (o corte "bate") e aproximação constante e leve deriva para cima à direita, que empurra o olhar para o rosto e prepara a folha que cai por cima.
- Sensação do movimento: impacto seco seguido de avanço contínuo, como uma câmera de mesa que se aproxima sem parar (escala +6 %/s, sem desacelerar), em passos de 12 imagens/s.

## FORMA (fixa: reproduzir igual)
- Igual a V01-A02 na forma (foto impressa sozinha, borda de papel, estalo de 3 imagens, deriva). Medidas próprias (med.py/inc.py, quadro cheio):
  - Foto QUADRADA P&B com borda de papel ≈ 8 px: assentada f1675 x103–619, y207–723 = 517x517 px (71,8 % da largura, 40,4 % da altura), centro (50,0 %, 36,3 %); giro ≈ 1,0° anti-horário.
- Movimento:
  - Entrada: corte seco, maior e mais girada: lado f1671 584 px (113 %) → f1673 537 (104 %) → f1675 517 (100 %). Estalo, desacelerando: 4 q (167 ms) da entrada ao 1º quadro assentado (remedido, f1671–f1675; antes contado como 6 q). (medido)
  - Permanência: aproxima devagar: 517 → 550 (f1700) → 579 px (f1721) = +12 % em 1,9 s (≈ 6 %/s). (medido)
  - Saída: a folha de papel de V01-A27 cai por cima em f1723 (a foto fica atrás, aparecendo pela borda direita). (medido)
  - Cadência 12 imagens/s. (medido)
- Ritmo: 2167 ms; assentada, sem peça nova, aproximando +6 %/s com deriva (alinhado ao reestudo) de f1675 a f1722 = 1958 ms. (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- Textura (reestudo 20/11):
  - Fundo (mesa): a mesma das outras cenas: liso com nuvens largas. f1700 região 0,760,720,80: #201c1d, luma 28,7, grão 0,44, manchas 0,72, ac1 +0,52; parado (diferença 0,00–0,03 entre quadros fora do corte). Detalhe com realce: nuvens suaves + blocos de compressão de 8 px, nada de fibra.
  - Foto: papel fotográfico P&B neutro com poeira. f1700 parede escura 140,200,140,100: #413f42, grão 1,71 níveis, manchas 1,63, ac1 +0,66 (grão de 2–3 px, mais macio que o da foto da estação anterior, V01-A24), grão por canal 1,71/1,71/1,71 (cinza puro). No detalhe: pontos isolados claros e escuros de 1–3 px (poeira de arquivo), anda com a foto. Grão VIVO nos claros (medido, teste novo: f1700×f1702 e f1700×f1704 alinhados pela afim da foto, pixels lisos: claros resíduo/σ 1,23, correlação +0,19/+0,20; escuros 0,68/0,64, correlação +0,75/+0,79): as áreas claras da foto e o papel ganham grão novo a cada imagem, a parede escura anda rígida com a foto (corrigido na conferência: era "anda com a foto" para a foto inteira; a conferência mediu num claro da foto +0,02, resíduo/σ 1,30).
  - Borda de papel: off-white quente mosqueado, ≈ 8 px; mais clara embaixo (#e7e2da) que à esquerda (#d5d1cb) e à direita (#d0cac2), em cima a mais escura (#b7b3ad); entre a borda e a imagem há uma linha cinza de 1–2 px (a margem da própria foto). Cantos retos.
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: o mesmo foco de luz largo do fundo (luma 28–38 em volta da foto, mais escuro para o rodapé); nenhuma vinheta de canto aplicada.
  - Vinheta da imagem: nenhuma visível (a foto escurece embaixo por conteúdo, não por máscara).
  - Borda borrada: nenhuma.
  - Sombra (medido, f1700, perfil alinhado na borda real): embaixo −55 % no contato (16 contra 35), volta ao fundo em 18 px; à esquerda −34 %, volta em 15 px; à direita −37 %, 13 px (medido na conferência); em cima só 1 px (medido na conferência). Sombra CAÍDA para baixo: longa embaixo, média dos lados, nada em cima (corrigido na conferência: era embaixo 17 px, esquerda 12, direita 10, força 30–40 %).
  - Fio escuro: nenhum; desfoque de movimento: nenhum (a entrada é estalo de escala, sem deslize). Profundidade, brilho, aberração: nenhum (medido em f1700). Grão global: nenhum aplicado no quadro (a mesa é parada); o grão vivo mora nos claros da foto (ver Textura) (corrigido na conferência: era "nenhum").
- Câmera (reestudo 20/11): só a foto anda (a mesa fica parada): f1675 → f1689 escala ×1,0350 (+6,1 %/s), centro (+0,80, −0,90 px/q), giro −0,03°; f1701 → f1715 ×1,0367 (+6,4 %/s), centro (+0,97, −1,04 px/q), giro −0,04°. Aproximação CONSTANTE (não desacelera) com deriva diagonal para cima e à direita ≈ 1,3 px/q. Fim da cena (medido, f1708 → f1720, região 0,0,720,830): ×1,0308 (+6,2 %/s), centro (+0,74, −0,84 px/q): mesma velocidade até a folha cair, sem freio nem recuo. Paralaxe de camada (foto × mesa).
- Cadência (reestudo 20/11): 12 imagens/s na foto (perfil f1670–f1690, região da foto: 84,7 / 0,00 / 23,8 / 0,03 / 20,6 / 0,01 / 8,4 / 0,53 / 8,9 / 3,3 / 10,1 / 0,04 …); mesa parada.
- Legenda nesta cena (reestudo 20/11): 2 blocos: o 1º (3 palavras, dia e mês) entra no MESMO quadro do corte (f1671) e fica 1,33 s; o 2º (1 palavra, o ano; f1703–f1724) atravessa a saída (a folha cai por cima em f1723). Texto #efdf52, caixa 229x30 px, centro 68,1 %. Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px de altura (y847–892), sobre a mesa (medido na conferência; corrigido na conferência: era ≈ 75 %, estimativa grosseira). Atrás da tarja: só a mesa (a foto termina em y716). Nenhum outro texto (o "texto branco grande" do censo nesta cena é a camisa branca da foto, falso positivo). Nenhum sumiço.

## CONSTRUÇÃO
1. fundo: mesa #181516–#201c1d com foco de luz largo (ver V01-A24), parada, sem grão animado.
2. sombra da foto: preto, caída para baixo: embaixo escurece 55 % no contato e some em 18 px; dos lados 34–37 % e some em 13–15 px; em cima só 1 px (corrigido na conferência: era preto ≈ 35 %, desfoque ≈ 15 px, deslocada 3 px); acompanha a foto.
3. foto: imagem P&B neutra quadrada com borda de papel off-white ≈ 8 px (mais clara embaixo), cantos retos, giro ≈ 1,0° anti-horário; grão VIVO nos claros (ruído cinza ≈ 3 níveis sorteado de novo a cada imagem, só onde a foto é clara; nas sombras o grão anda rígido com a foto) (corrigido na conferência: era foto toda parada); assentada em x103–619, y207–723 (71,8 % da largura, centro 50,0 % × 36,3 %). Entrada no corte: 0 ms lado 113 % e mais girada → 83 ms 104 % → 167 ms 100 % (estalo que desacelera, sem deslize). Depois escala constante +6 %/s com deriva ≈ (+0,9, −1,0) px/q até 2167 ms (lado 579 px em f1721). Passos de 2 quadros.
4. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, centro 68 %; o 1º bloco entra no quadro do corte.
- Linha do tempo (ms a partir do corte f1671 = 69625 ms): 0 corte seco + foto a 113 % + 1º bloco de legenda · 167 ms foto assenta · 167–2167 ms aproximação constante · 1333 ms 2º bloco de legenda (o ano) · 2167 ms a folha de V01-A27 cai por cima (a foto continua atrás, visível à direita).
- Parâmetros que dependem do conteúdo: formato da foto (quadrado aqui); o giro (± 1°, alterna com a foto anterior); direção da deriva (puxa para o rosto da pessoa).
- O que NÃO fazer: estalo longo (passa de 4 quadros e vira "zoom"), parar a foto, aproximação com ease (aqui ela é constante), cortar a foto na saída (a próxima peça cai POR CIMA, a foto fica embaixo), limpar a poeira da foto, congelar o grão dos claros (ele troca a cada imagem), sombra simétrica em volta (ela cai para baixo).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "a pessoa no momento do trabalho/da descoberta": foto de época.
- Nesta referência as lacunas foram preenchidas com: cientista de camisa branca curvado sobre um microscópio.
- Receita de tratamento de cada imagem: foto real de época, P&B, formato quadrado, borda de papel, ≈ 72 % da largura, giro ~1°.
- Regra de escolha: data exata do "momento da virada" → foto da pessoa trabalhando (não do resultado ainda).
- Teste de generalização: (1) Claude Code: "em 12 de março de 2024," → foto do dev digitando à noite. (2) café: "numa manhã de 1901," → foto antiga do inventor na bancada.
- Receita de tratamento (reestudo 20/11): foto real de época, P&B neutro (grão macio ≈ 1,7 níveis de 2–3 px, sem tinta sépia), com a poeira e os pontos do original mantidos; contraste natural (preto da parede ≈ #3f3d40, branco da roupa ≈ #e9e7ea); formato quadrado; borda off-white ≈ 8 px com margem cinza fina por dentro; sombra caída para baixo: embaixo −55 % em 18 px, lados 13–15 px, em cima 1 px (alinhado ao reestudo).

- Confiança: tamanhos, giro e tempos medido.
