# V02-A08 · mapa com pintura amarela e zoom em dois saltos
- Categoria: P22 · Mapa com marcação (provisória do analista: (provisória) mapa escuro em tons de cinza; a região citada é pintada de amarelo e a câmera salta (zoom) para a sub-região seguinte)
- Fonte: V02 quadros f676–f759 (28,19–31,66 s; 84 quadros ≈ 3504 ms) · 23,976 qps
- Fala: "Ideally, you're in the US. If you're in New York, even better."
- Tipo de fala: lugar
- Gatilho: entra por corte seco em f676 (28195 ms), -5 ms antes da palavra nº 86 "Ideally," (28200 ms); conferido no envelope (f674 -35,2 dB, f675 -18,1, f676 -11,2: o corte cai no ataque da palavra). Pintura do país em f698, -148 ms antes de nº 90 "US." (29260 ms). 1º salto de zoom em f711 (29655 ms), ≈ -45 ms ANTES do ataque real de nº 91 "If" (remedido no envelope: f710 -28,7 dB, f711 -41,4 dB de silêncio, f712 -24,3 dB = ataque ≈ 29700 ms; a transcrição marca "If" em 29540 ms, ≈ 160 ms antes do som real, e dava +115 ms). Pintura do estado em f722, -127 ms antes de nº 94 "New" (30240 ms). 2º salto em f730, +87 ms depois de nº 95 "York," (30360 ms). Pintura da cidade em f742, -122 ms antes de nº 96 "even" (31070 ms).
- Quadro-chave: f756
- Camadas ativas: legenda | grafismo (cena de tela cheia: mapa) | transição (zoom)
- Leitura dos strips:
  - strip.jpg: quadros f676 a f723, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 48 células; cada célula traz o nº do quadro e o tempo.
  - strip-saida.jpg: quadros f724 a f761, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 38 células; cada célula traz o nº do quadro e o tempo.
  - strip-geral.jpg: quadros f674 a f760, de 2 em 2, 8 colunas, da esquerda para a direita, linha a linha; 44 células; cada célula traz o nº do quadro e o tempo.
  - detalhe-pintura-borda-agua.jpg: quadro f756, região x330 y480 200x140 px, ampliada 3× sem suavizar (a pintura amarela com o grão do papel e as estradas por baixo, contorno escuro fino na costa).
  - detalhe-terra-papel-realce.jpg: quadro f756, região x30 y940 150x120 px, ampliada 3× sem suavizar, contraste ×6 em volta da média (o "papel" cinza da terra).
  - detalhe-tarja-sobre-terra-e-agua.jpg: quadro f756, região x170 y820 380x100 px, ampliada 2× sem suavizar (a mesma tarja cinza sobre a terra e preta sobre a água).
  - detalhe-salto-f720-empalidece.jpg: quadro f720 (pico do 1º salto), região x0 y0 720x820 px, ampliada 1× sem suavizar.
  - detalhe-faixa-legenda-f716.jpg e detalhe-faixa-legenda-f720.jpg: quadros f716 e f720, região x0 y600 720x340 px, ampliada 1× (f716 sem legenda; f720 legenda sobre a pintura amarela).

## LEITURA DE EDITOR
- Por que esta cena aqui: a fala afunila um LUGAR em níveis (de preferência o lugar maior; se for o menor, melhor ainda); o mapa é a tradução literal, e cada nível vira um salto de zoom com a pintura chegando ≈ 120–150 ms antes do nome.
- Por que este design: mapa sem rótulos (só forma e cor) para que a legenda dê o nome; o amarelo é a única informação; o nível anterior empalidece para mostrar "dentro disso, aqui".
- Por que estas cores: água = o próprio tampo escuro (o mapa é um recorte de papel cinza sobre a mesa), terra em cinzas quentes, destaque no mesmo amarelo-ouro de todas as marcações do canal.
- Por que estes efeitos: a terra tem grão de papel (≈ 4,6 níveis) e a pintura deixa ver o grão e as estradas por baixo: parece tinta passada no papel, não preenchimento de vetor.
- Por que este movimento: o zoom salta com ataque e freio (pico ≈ +14 %/q) em vez de um zoom contínuo, então cada nível tem o seu "tranco"; o zoom não para no fim, dando a sensação de "chegar cada vez mais perto".
- Sensação do movimento: mergulho em degraus, rápido e preciso, como um mapa de GPS que aproxima; a pintura varre de oeste para leste como um pincel. Produzida por saltos de 16–19 q com pico de escala ≈ ×1,14 por quadro + varredura lento-rápido-lento de 9 q.

## FORMA (fixa: reproduzir igual)
- Design:
  - Água (mar) = o próprio tampo escuro #21201b (64 % da área em f690) / #24231e (f690, x650 y700). Medido.
  - Terra fora do foco: cinza médio quente #7c786f (f690, x300 y150), chapado. Medido.
  - Terra da região 1 (a maior citada, em foco): cinza claro #a9a59a (f690, x300 y500) com textura de linhas finas de estradas/divisas (desvio 17). No zoom máximo a terra vira #b0ab9f–#b4aea2 (f756, x200 y300) com a mesma textura. Medido.
  - Pintura: amarelo-ouro #c8a809 (dominante 4,1 % em f756) / #bea114 (f708, x300 y500, com a textura por baixo); a pintura é semitransparente sobre a textura de estradas. Medida a área (caixa #bea114 / #c8a809 tol 40 com a faixa da legenda y > 815 fora da região): região 1 pintada em f708 x88–601 y312–628 (514x317 px; 71,4 % x 24,8 %); região 3 pintada em f756 x176–553 y218–713 (378x496 px; 52,5 % x 38,8 %). Medido (remedição, f708 e f756; com a legenda junto a altura da região 1 dava 579 px).
  - Região pintada anterior: quando a câmera salta para a sub-região, a pintura de cima perde força e vira amarelo-pálido (creme amarelado) em ≈ 2 quadros, quase um corte (remedido: pixels amarelos da região 1: 172 mil em f719 → 109 mil em f720 → 13 mil em f721; da região 2: 105 mil em f740 → 4 mil em f741). O empalidecer acontece no pico de velocidade de cada salto. Medido (remedição).
  - Sem rótulos, sem nomes no mapa, sem pinos: só cor. Observado.
- Movimento:
  - Entrada: corte seco em f676 (dif 44,3); o mapa começa com a câmera quase parada (escala ≤ 0,2 %/q, sem push-in de verdade) (alinhado ao reestudo) (dif 0,7 → 2,4 de f677 a f699, acelerando aos poucos). Medido.
  - Pintura da região 1: f698–f706, 9 quadros ≈ 375 ms (completa em f705), preenchimento por varredura da esquerda (oeste) para a direita (leste); borda da pintura em x115 · 145 · 193 · 276 · 384 · 463 · 543 · 602 (f698–f705): lento-rápido-lento, não linear (remedido, caixa #c8a809); dif sobe a 5,3 em f702. Medido.
  - Parada curta: f707–f710 (dif 1,1 · 0,28 · 0,25). Medido.
  - 1º salto (região 1 → região 2): f711–f729, ≈ 19 quadros ≈ 792 ms, zoom in rápido na direção da sub-região (para cima e para a direita); dif 6,0 · 9,9 · 13,3 · 16,7 · 19,0 · 22,3 · 25,5 · 28,2 · 30,1 (f719, pico) · 26,3 · 27,4 · 27,1 · 26,2 · 22,8 · 20,9 · 14,8 (f726) · 13,0 · 12,7 · 11,8. Ataque em 8 quadros, freio em ≈ 10. A pintura da região 2 entra em f722–f726 (≈ 5 q) durante o freio. Medido (perfil) + observado (pintura).
  - 2º salto (região 2 → região 3): f730–f745, ≈ 16 quadros ≈ 667 ms; dif 11,8 · 12,6 · 14,2 · 16,2 · 18,2 · 20,1 · 21,8 · 22,0 · 21,9 · 22,8 · 23,3 (f740, pico) · 21,5 · 19,2 · 18,5 · 19,3 · 13,9 (f745). Pintura da região 3 f742–f748 (≈ 7 q), em pedaços (subdivisão a subdivisão). Medido + observado.
  - Deriva final: f746–f759, dif ≈ 10,6 → 8,0; o zoom continua FORTE até o corte, ≈ +3,8 %/q (região 3 pintada: 333 → 401 px de largura entre f753 e f758) (corrigido no reestudo, f753–f758: dizia "o zoom continua devagar"). Medido.
  - Saída: corte seco para a cena seguinte (V02-A09) em f760 (dif 93,5). Medido.
- Passos internos:

| passo | quadro de início | duração | tipo de movimento | curva | palavra-gatilho e deslocamento |
|---|---|---|---|---|---|
| mapa em cena (corte) + avanço lento | f676 | 22 q | corte + câmera quase parada, ≤ 0,2 %/q (alinhado ao reestudo) | acelerando de leve | nº 86, o advérbio que abre a frase (28200 ms): -5 ms |
| região 1 pintada de amarelo | f698 | 9 q ≈ 375 ms | varredura oeste → leste | lento-rápido-lento (remedido) | nº 90, o nome do lugar 1 (29260 ms): -148 ms |
| 1º salto de zoom (região 1 → região 2) | f711 | ≈ 19 q ≈ 792 ms | zoom in + deslocamento | ataque 8 q, freio 10 q | nº 91, a conjunção que abre a 2ª frase (ataque real ≈ 29700 ms no envelope): ≈ -45 ms (remedido; pela transcrição dava +115) |
| região 2 pintada, região 1 empalidece | f722 | ≈ 5 q ≈ 209 ms | preenchimento + fade | — | nº 94, 1ª palavra do nome do lugar 2 (30240 ms): -127 ms |
| 2º salto de zoom (região 2 → região 3) | f730 | ≈ 16 q ≈ 667 ms | zoom in | ataque 10 q, freio 5 q | nº 95, fim do nome do lugar 2 (30360 ms): +87 ms |
| região 3 pintada, região 2 empalidece | f742 | ≈ 7 q ≈ 292 ms | preenchimento em partes + fade | — | nº 96, o intensificador do fecho (31070 ms): -122 ms |

- Ritmo: começa 1 quadro depois da V02-A07 (corte direto de uma cena para outra, sem rosto no meio). A pintura da região 1 completa fica parada f707–f710 (≈ 167 ms) antes do salto; a região 2 completa f726–f729 (≈ 167 ms) já em movimento; a região 3 completa f748–f759 ≈ 12 quadros (500 ms), em deriva. Medido.
- Som: nenhum efeito estéreo (canal lateral -120 dB de f676 a f760). Nada nos saltos de zoom. Medido.
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Água = o TAMPO, parado na tela: f756 região x560 y700 140x100: #24231e, luma 34,7, grão 0,14, manchas 0,30, f756 × f758 PARADA (correlação +0,78) mesmo com o mapa em zoom de ≈ +4 %/q. O mapa é uma camada de "terra" recortada que anda sobre o tampo fixo; a água não é desenhada. Família: liso.
  - Terra em foco: papel cinza com grão. f756 região x30 y940 150x120: #afaba0, luma 170,9, grão 4,59 níveis, manchas 2,42, ac1 +0,42 (grão de 1 a 2 px), grão cinza (4,59/4,59/4,59), sem vinheta; com estradas em linhas escuras finas de 1 px. f708 × f709 (mapa quase parado): PARADA (+0,89); f756 × f758 (zoom): muda porque escala junto com o mapa. Família: papel com fibra.
  - Terra fora de foco: #767269 (f700, x250 y250), grão 6,8 níveis.
  - Pintura: amarelo #c6a60b (f756 região x380 y400 100x60), grão 8,7 níveis com canais diferentes (B 5,95 / G 9,06 / R 8,86: o grão do papel aparece através da tinta), manchas 4,35; as estradas continuam visíveis como linhas escuras; contorno escuro de 1 a 2 px na linha da costa (detalhe-pintura-borda-agua). É tinta em modo multiplicar sobre o papel, não amarelo chapado.
- Efeitos (reestudo 20/11):
  - Vinheta: nenhuma no mapa (borda f756 na região da terra x0 y0 440x820: 96 % do centro no anel externo); a água recebe a luz fixa do tampo.
  - Sombra da terra sobre a água: nenhuma (no detalhe a costa encosta direto no tampo, só o contorno escuro de 1 a 2 px).
  - Empalidecer da região anterior: a pintura do nível acima vira creme amarelado em ≈ 2 q no pico de cada salto (detalhe-salto-f720-empalidece).
  - Desfoque de movimento: nenhum (f720, pico do 1º salto a ≈ +14 %/q: estradas nítidas no detalhe).
  - Brilho, halo, aberração, profundidade de campo, grão global: nenhum (medido em f756).
- Câmera (reestudo 20/11): o tampo (água) fica parado; a camada do mapa escala. f686 → f696 (avanço inicial): −0,17 %/q (na verdade quase parado; o "push-in" do texto antigo é ≤ 0,2 %/q); 1º salto f714 → f720: +14,2 %/q (×2,21 em 6 q), conteúdo −46/+9 px/q; 2º salto f732 → f738: +13,7 %/q, −25/−36 px/q (vai para cima e para a direita); final f748 → f758: +5,2 %/q no `camera` e +3,8 %/q pela largura da região 3 pintada (333 → 401 px de f753 a f758); fim f751 → f759 (região x0 y0 720x820, sem a faixa da legenda, 361 de 600 pontos; medido na correção 20/11): +4,0 %/q (+157 %/s), conteúdo −0,4/−3,3 px/q (sobe), mesmo valor. O zoom NÃO desacelera até parar: a cena termina com o mapa ainda aproximando forte (corrigido no reestudo, f753–f758: a nota dizia "deriva final… o zoom continua devagar").
- Cadência (reestudo 20/11): 24 imagens/s (`perfil` f744–f759: 16,5 → 10,2 sem quadros parados alternados; nos saltos o perfil antigo sobe e desce liso).
- Legenda nesta cena (reestudo 20/11): tarja 50 % (direta 49,6–50,9 % na conferência; altura 76 px) sobre a terra (f725–f738 luma dentro 73 × fora 151; f744–f759 83 × 169) e sobre a água (17 × 35) (corrigido na conferência: era "= 52 %" e "= 51 %", razão lida com o fundo longe da tarja); no mesmo bloco ela fica cinza sobre a terra e preta sobre a água (detalhe-tarja-sobre-terra-e-agua, f756). Blocos: o advérbio de abertura f675–f687 entra 1 q ANTES do corte de entrada (f676), ainda sobre a pilha da V02-A07; pronome + verbo f688–f694; preposição + artigo + lugar 1 com ponto f695–f715; 1 q sem legenda (f716, confirmado no detalhe-faixa-legenda-f716); conjunção + pronome + preposição f717–f724 sobre a PINTURA AMARELA (o detector do censo confunde a tinta com a legenda em f716–f723: a tabela "sai do padrão" com centro 53,3 % é falso positivo; a legenda real continua no lugar fixo, detalhe-faixa-legenda-f720); o nome do lugar 2 (2 pal.) f725–f738; 5 q SEM legenda f739–f743 (209 ms, na pausa antes do fecho, enquanto a região 3 é pintada); o fecho (2 pal. com ponto) f744–f759 até o corte. Amarelo sobre amarelo: a tarja escurece a tinta a um oliva e o texto continua legível. Outro texto: nenhum (mapa sem rótulos).
- Entrada do texto (reestudo 20/11): não há texto do editor nesta cena.

## CONSTRUÇÃO
1. fundo: tampo liso parado na tela, com a luz oval fixa; ele é a ÁGUA do mapa.
2. camada do mapa (escala e anda): só a terra, recortada pela costa, sem rótulos; terra fora do foco #767269, terra do nível em foco #afaba0, as duas com grão de papel (4,6 a 6,8 níveis) e estradas em linhas escuras de 1 px; contorno escuro de 1–2 px na costa; sem sombra.
3. pinturas: amarelo #c6a60b em multiplicar sobre a terra (o grão e as estradas aparecem através), uma por nível citado.
4. linha do tempo da camada 2–3: corte seco em 0 ms com o mapa do nível maior; pintura 1 varre oeste → leste de 917 a 1292 ms (f698–f706, 9 q, lento-rápido-lento); parada curta; salto 1 de 1458 a 2250 ms (f711–f729, ataque 8 q até ≈ +14 %/q, freio 10 q) com a pintura 1 empalidecendo para creme em 2 q no pico e a pintura 2 entrando de 1917 a 2125 ms (f722–f726); salto 2 de 2250 a 2875 ms (f730–f745, pico ≈ +14 %/q) com a pintura 2 empalidecendo e a pintura 3 entrando em partes de 2750 a 3042 ms (f742–f748); zoom contínuo de ≈ +4 %/q até o corte.
5. legenda (camada fixa; a tarja preta 50 %, altura 76 px, fica cinza sobre a terra, oliva sobre a tinta, preta sobre a água).
- Linha do tempo (ms a partir do corte f676): 0 corte · 917 pinta nível 1 · 1458 salto 1 · 1917 pinta nível 2 · 2250 salto 2 · 2750 pinta nível 3 · 3042 completo, zoom seguindo · 3504 corte seco para a cena seguinte.
- Parâmetros que dependem do conteúdo: o mapa (forma da terra), quantos níveis a fala cita, a região de cada nível, o centro de cada salto.
- O que NÃO fazer: desenhar a água (ela é o tampo parado); pôr nomes, pinos ou bordas de país; pintar com amarelo chapado opaco (a tinta deixa ver grão e estradas); zoom contínuo sem degraus; parar o zoom no fim; sombra sob a terra.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - mapa da região maior citada (país/continente)
  - região citada primeiro (a ser pintada) e sub-região citada depois (o foco do zoom), em quantos níveis a fala pedir
- Nesta referência as lacunas foram preenchidas com: América do Norte; região 1 = o país (EUA), região 2 = o estado (Nova York), região 3 = a cidade (Nova York), pintada bairro a bairro; o zoom ia para o nordeste do país.
- Receita de tratamento de cada imagem: mapa vetorial sem rótulos, água = cor do tampo escuro, terra em cinzas quentes (fora do foco mais escuro, em foco mais claro com textura fina de estradas), destaque só em amarelo-ouro semitransparente; ao descer de nível, o destaque anterior empalidece.
- Regra de escolha: qualquer LUGAR citado vira mapa; uma fala que afunila ("de preferência no país X; se for na cidade Y, melhor ainda") vira um zoom em saltos, um salto por nível citado, com a pintura chegando ≈ 120–150 ms antes do nome. Teste de generalização: (1) Claude Code: "a maioria dos usuários está no Brasil, e em São Paulo mais ainda" → mapa da América do Sul, Brasil pintado, salto para o estado, salto para a capital. (2) Café: "o melhor café vem de Minas, e do Sul de Minas especialmente" → Brasil → Minas pintado → zoom e pintura do Sul de Minas.

- Receita de tratamento (reestudo 20/11): mapa = terra recortada em papel cinza quente com grão (≈ 4,6 níveis), estradas finas, sem rótulos; destaque em tinta amarela multiplicada (#c6a60b) que deixa ver o papel; nível anterior empalidece para creme.
- Receita de ILUSTRAÇÃO (reestudo 20/11): o mapa é uma ilustração plana em 2 cinzas + amarelo, sem preenchimento de água, com contorno escuro fino só na costa, destacada do fundo pelo contraste cinza claro × tampo escuro; revelada por corte seco e depois por pintura em varredura; o traço não ferve.
- Teste de generalização: (1) Claude Code: "a maioria dos usuários está no Brasil, e em São Paulo mais ainda" → América do Sul em papel cinza sobre a mesa, Brasil pintado de oeste a leste, salto para o estado, salto para a capital. (2) café: "o melhor café vem de Minas, e do Sul de Minas especialmente" → Brasil → Minas pintado → salto e pintura do Sul de Minas.

- Confiança: cores, curvas dos zooms, cortes, ausência de efeito, larguras das pinturas = medido · direção da varredura, empalidecer da região anterior, pintura em partes = observado (folha 2 em 2 e strips 1 em 1) · alturas das áreas pintadas = não medido (a caixa da cor pega a legenda junto).
