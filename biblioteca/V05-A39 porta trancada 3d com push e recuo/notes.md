# V05-A39 · porta trancada (3D): push-in na palavra da ação e recuo na palavra do lugar
- Categoria: P24 · Cena 3D narrativa (provisória do analista: (provisória) cena 3D low-poly de personagem, câmera que aproxima e depois abre)
- Fonte: V05 quadros f2792–f2882 (116,49–120,25 s; 91 quadros ≈ 3795 ms) · 23,976 fps
- Fala: "Later, emperors in Constantinople locked the dyers inside palace walls,"
- Tipo de fala: ação narrada
- Gatilho: entra por corte seco em f2792 (116 450 ms), 90 ms antes do início da palavra nº 393 "Later," (116 540 ms). Conferido: dif 31 em f2792; legenda "Later, emperors" no mesmo quadro.
- Quadro-chave: f2850
- Camadas ativas: b-roll 3D | legenda
- Leitura dos strips: strip.jpg = quadros f2820 a f2845, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 26 células (o push na palavra "locked"). strip-geral.jpg = quadros f2792 a f2882 (amostrado). detalhe-luz-quente-porta.jpg = quadro f2850, região x0 y100 720x700 px, ampliada 1× sem suavizar (porta e parede de tijolo em foto nítida, personagem na cor-tema, barra 3D com textura de madeira).

## LEITURA DE EDITOR
- Por que esta cena aqui: "trancaram os tintureiros dentro do palácio" é uma ação física; a cena mostra quem tem poder travando a porta.
- Por que este design: porta grande à esquerda, o personagem na cor-tema à direita segurando a trava: o gesto de controle no centro da composição.
- Por que estas cores: aqui o cenário é QUENTE e em cor (tijolo vermelho, madeira), diferente dos fundos P&B das cenas anteriores; o personagem na cor-tema com faixa dourada continua sendo o ponto mais saturado.
- Por que estes efeitos: vinheta forte (borda a 24 %) e borda bem mais mole que o centro (nitidez 10 %): o olho fica no gesto.
- Por que este movimento: aproxima no verbo ("locked", pico 63 ms antes) e abre subindo na palavra do lugar ("palace walls") para mostrar a parede inteira; corta ainda em movimento.
- Sensação do movimento: aperto e soltura; o push curto dá o "clique" da tranca e o recuo acelerado dá a sensação de prisão grande.

## FORMA (fixa: reproduzir igual)
- Design: a passagem do lugar (arco com porta) à esquerda; quem controla, vestido na cor-tema (#714748 em f2820, x360 y500, medido), fecha a passagem; os personagens controlados atrás dela; mundo 3D low-poly de A09, iluminação quente lateral, vinheta.
- Movimento (dif global, medido):
- Passos internos:

| passo | quadros | duração | tipo | curva (dif) | gatilho |
|---|---|---|---|---|---|
| deriva lenta | f2793–f2823 | 31 q | aproximação muito lenta | 3–4 | sujeito e lugar da frase |
| push-in | f2824–f2841 | 18 q ≈ 751 ms | aproximação lento-rápido-lento, curta: ×1,0015 por 2 q na deriva, ×1,0047 por 2 q no pico (f2830–f2832), ×1,002 em f2838 (registro de pontos, remedição) | 3 → 6 → 8 (pico f2832) → 4 | o verbo de ação (#397, 118 180 ms): pico f2832 = 118 117 ms, −63 ms |
| a ação de controle se completa (a passagem é travada) | f2850–f2856 | ≈ 7 q | ação do personagem (observado) | 2–4 | o objeto da ação |
| recuo (zoom-out) subindo | f2857–f2882 | 26 q ≈ 1084 ms | abre devagar acelerando até velocidade constante; não é só zoom: a imagem também DESCE ≈ 17 px/q (câmera sobe recuando): ×0,998 e +10 px por 2 q em f2858, ×0,988 e +35 px em f2866, ×0,986 e +36 px em f2874, ×0,989 e +28 px em f2879 (registro de pontos, remedição) | 4 → 7 → 10 (constante f2867–f2882) | o lugar (#401, 119 540 ms): f2857 = 119 161 ms, −379 ms (corrigido na conferência: a coluna gatilho trazia as falas entre aspas) |

- Saída: corte seco em f2883 (dif 36) ainda em movimento (o recuo não freia antes do corte).
- Ritmo: 3,8 s; dois movimentos de câmera opostos ligados às palavras de ação (aproxima no verbo de ação, abre no lugar para mostrar a parede inteira) (corrigido na conferência: eram as palavras citadas).
- Som: nenhum efeito detectado (lateral −120 dB).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

- Textura (reestudo 20/11):
  - fundo (porta de madeira e parede de tijolo, foto real em cor, nítida): foto · #35291f na parede · grão 3,77 · manchas 6,14 · ac1 +0,62 · anda com a câmera (f2850×f2856: +0,91 depois de alinhar).
  - barra de trava: objeto 3D com textura fotográfica de madeira clara, nítida.
  - personagem: corpo de blocos na cor-tema com trama leve e faixa dourada; cabeça de mosaico antigo (pastilhas visíveis, contorno dourado).
- Efeitos (reestudo 20/11): vinheta global forte (100 → 83 → 63 → 38 → 24 % da luma; `borda` f2850) e borda borrada mais forte que a vinheta (nitidez 100 → 78 → 33 → 13 → 10 %): desfoque radial de borda; fundo e personagem igualmente nítidos no centro (sem profundidade de campo aqui); sombra: a do render; halo, aberração, grão de filme: nenhum (medido em f2850).
- Câmera (reestudo 20/11): 3 fases. Deriva f2795→f2820 +2,2 %/s (o deslize e o giro medidos vêm do personagem; o fundo só aproxima); push-in e recuo como na remedição. Remedido na correção (região x40 y80 640x700): começo +1,8 %/s (f2795→f2807, 341 de 600 pontos); push +7,3 %/s (f2824→f2832, 248 pontos; o giro de 1°/q ali vem do personagem) e +7,0 %/s (f2832→f2842, 443 pontos); depois +2,0 %/s (f2835→f2847, já no fim do push); fim −16,4 %/s com a imagem descendo 14,2 px/q (f2867→f2880, 285 pontos), batendo com o recuo abaixo; no recuo final f2867→f2880: ×0,907 em 13 q (−16,5 %/s) e a imagem desce 14,8 px/q (câmera sobe recuando), velocidade constante até o corte.
- Cadência (reestudo 20/11): 24 imagens/s (o recuo muda a cada quadro, dif 10 constante).
- Legenda nesta cena (reestudo 20/11): tarja 69 % (p10 63, p90 71; direta na correção f2850: 72 % em cima e 69 % embaixo, fundo 105/65; 51 px, y 809–859), texto #f1e816, 28 px (35 com descendente), centro y 65,5 %; atrás da tarja: a parte baixa da porta e do personagem (luma fora 64–66, meio-tom); 4 blocos de 2 a 3 palavras: o 1º entra no corte e o 4º, com o lugar, ATRAVESSA o corte de saída (corrigido na conferência: eram as falas entre aspas) (f2853–f2892, entra 9 q na cena seguinte); nenhum outro texto.

## CONSTRUÇÃO
1. fundo: foto real em cor de uma porta antiga em arco e parede de tijolo, nítida, quente; ocupa a metade de cima e o centro.
2. personagem 3D low-poly na cor-tema (faixa dourada), cabeça com textura de mosaico, à direita (x ≈ 58–90 %, cabeça em y ≈ 27–35 %).
3. barra de trava: peça 3D com textura de madeira; o personagem a encaixa na porta de +2419 a +2669 ms.
4. vinheta forte (borda 24 %) + desfoque de borda (nitidez na borda ≈ 10 % do centro).
5. câmera: 0–1293 ms deriva +2,2 %/s · 1335–2085 ms push-in lento-rápido-lento (pico em +1668 ms, 63 ms antes do verbo de ação) · 2711–3795 ms recuo subindo que acelera até −16,5 %/s e +14,8 px/q (imagem desce), corte em movimento.
6. legenda amarela V05-L01, tarja preta a 68 % (aqui 69–72), 51 px de altura (y 809–859), raio ≈ 8–9 px.
- Linha do tempo (ms a partir do corte): 0 corte seco · +1335 push-in começa · +1668 pico · +2085 push termina · +2419 a trava fecha · +2711 recuo começa (379 ms antes do lugar dito; corrigido na conferência: era a palavra citada) · +3795 corte seco em movimento (a legenda segue para a próxima cena).
- Parâmetros que dependem do conteúdo: o objeto do controle (porta, cofre, portão), quem controla na cor-tema, a palavra da ação e a palavra do lugar.
- O que NÃO fazer: frear o recuo antes do corte; câmera parada; cenário em P&B (aqui é cor quente); vinheta sem desfoque de borda.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "ação de controle/posse descrita" (trancar, guardar, proibir); "quem controla, com a cor-tema"; "os controlados" (ficam atrás da passagem).
- Nesta referência as lacunas foram preenchidas com: imperador trancando os tintureiros dentro do palácio.
- Receita de tratamento de cada imagem: igual a A09.
- Regra de escolha: ação literal; o movimento de câmera reforça o verbo (aproximar = foco na ação; abrir = mostrar o lugar).
- Receita de tratamento (reestudo 20/11): foto real do lugar em cor quente (sem dessaturar), nítida; vinheta forte com borda mole.
- Receita de ILUSTRAÇÃO (reestudo 20/11): 3D low-poly "colagem" com cabeça em mosaico antigo e objeto 3D com textura fotográfica (madeira); destaque por cor-tema + dourado.
- Teste de generalização: reel sobre Claude Code → um executivo na cor-tema tranca a porta da sala do servidor, a câmera aproxima em "trancou" e abre em "dentro da sede"; reel sobre café → um barão na cor-tema fecha o portão do armazém, aproxima em "fechou" e abre em "fazenda inteira".

- Confiança: tempos e curvas medidos; viga observada.
