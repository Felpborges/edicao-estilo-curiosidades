# V01-A27 · folha de papel + caneta recortada que desenha o diagrama da ideia, traço a traço
- Categoria: P19 · Marcação e desenho à mão (provisória do analista: (provisória) desenho à mão animado numa folha de papel (caneta-adesivo que "escreve"))
- Fonte: V01 quadros f1723–f1845 (71,79–76,88 s; 123 quadros ≈ 5125 ms) · 24 fps
- Fala: "he wrote down the idea that flipped everything. The diver doesn't have to be dry to stay warm."
- Tipo de fala: ação narrada → mecanismo (a ideia resumida em uma frase)
- Gatilho: a folha cai em f1723 = 71792 ms, −68 ms antes da palavra nº 225 "he" (71860 ms); a caneta começa a desenhar em f1725 = 71875 ms, junto da nº 225 "he" (71860 ms; voz sobe em f1726) (conferido, f1725; antes: f1728 / "wrote").
- Quadro-chave: f1840
- Camadas ativas: cena de tela cheia (foto de trás) | grafismo animado (desenho + caneta) | legenda
- Leitura dos strips: strip.jpg = quadros f1721 a f1736, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 16 células. strip-saida.jpg = quadros f1796 a f1812 (a água fina sendo pintada), mesma regra, 17 células. strip-geral.jpg = quadros f1721 a f1847, de 3 em 3, 43 células. Cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-caneta-ponta.jpg = quadro f1840, região x370 y400 170x150 px, ampliada 3× sem suavizar · detalhe-traco-agua-bolhas.jpg = quadro f1840, região x130 y320 170x150 px, ampliada 3× sem suavizar · detalhe-papel-realce.jpg = quadro f1840, região x30 y90 200x150 px, ampliada 2× sem suavizar, contraste ×6 em volta da média.


## LEITURA DE EDITOR
- Por que esta cena aqui: a fala diz "ele escreveu a ideia"; em vez de ilustrar o resultado, a tela MOSTRA o ato de escrever, e o desenho é a própria explicação, montada na ordem da frase.
- Por que este design: folha de caderno quase da altura da tela, caneta de verdade recortada e traço de caneta: parece o rascunho original da pessoa, não um infográfico.
- Por que estas cores: papel creme e tinta escura (o "documento"), e só duas cores de sistema por cima, teal (água) e laranja (calor), as mesmas dos outros diagramas do vídeo, para o espectador já saber o que cada cor significa.
- Por que estes efeitos: as cores entram como tinta sobre o papel (a fibra aparece por baixo), a folha tem borda escurecida e sombra; o adesivo branco da caneta separa um objeto "de verdade" do desenho chapado.
- Por que este movimento: o traço avança na velocidade de uma mão, sem pausa, e a caneta segue a ponta; o espectador acompanha o raciocínio sendo construído, e o resultado (calor) só aparece na última palavra.
- Sensação do movimento: escrita contínua e ritmada (diferença 9–17 por imagem em toda a cena), sem cortes, como assistir alguém pensando no papel; a folha que cai com estalo e depois respira devagar dá o "tum" do início.

## FORMA (fixa: reproduzir igual)
- Design (quadro cheio):
  - Folha retangular vertical de papel creme amarelado #d4c5a6 (f1760, 150,700) com textura e vincos leves, sombreada mais escura na borda (#a3947d em 600,200); assentada f1729 x87–658, y89–804 = 571x715 px (79,3 % da largura, 55,9 % da altura), centro (51,4 %, 35,9 %) (conferido, f1729: a borda x686 era a foto de trás; antes: x87–686, 600x718, 83,3 %), levemente girada. A foto anterior (V01-A26) aparece atrás pela direita. (medido com med.py e cor)
  - Recorte do instrumento de escrita (preto) com contorno de adesivo off-white, inclinada ~45°, com a ponta exatamente no fim do traço que está sendo desenhado (segue o traço). (observado)
  - Desenho: linha preta acastanhada #2d251a de ≈ 4 px de miolo + 1 px de antisserrilhado de cada lado (corrigido no reestudo, f1840; antes "≈ 3 px"), traço contínuo de contorno (parte 1: a figura principal em contorno simples), depois a parte 2 em traço duplo em volta dela, a parte 3 como bolinhas pequenas de contorno dentro da parte 2, a parte 4 como faixa fina teal pintada entre as duas, e por último o resultado: mancha laranja #e39a5e (f1840, 360,600) com 3 linhas onduladas, no centro da figura. Estilo de diagrama de caderno. (observado; cores medido)
- Movimento:
  - Folha: cai por cima com estalo de 3 imagens: caixa f1723 653x803 (109 %) → f1725 611x743 (102 %) → f1727 599x717 (100 %); assenta em 4 quadros (f1723→f1727, 167 ms) (conferido, f1727). Depois aproxima devagar até 694x831 em f1845 (+16 % em 4,9 s ≈ 3 %/s). (medido)
  - Desenho: revelação contínua do traço na velocidade de uma mão (diferença 9–17 por imagem durante TODA a cena, f1725–f1843, sem pausa maior que 2 imagens). O instrumento acompanha a ponta do traço; entre partes ela "pula" para o próximo início. (medido no perfil, região x100 y150 520x700; instrumento observado)
  - Saída: corte seco em f1846 para V01-A28. (medido)
  - Cadência 12 imagens/s (perfil ≈ 0 nos quadros pares). (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | folha cai | f1723 | 4 q (167 ms) (conferido, f1727; antes 6 q) | escala 109 → 100 % | estalo | nº 225 | −68 ms |
  | instrumento desenha a parte 1 (contorno da figura) | f1725 (conferido; antes f1728) | ≈ 23 q (958 ms) | traço se revela atrás do instrumento | constante | nº 225 (71860) | +15 ms |
  | parte 2 (traço duplo em volta) | f1750 | ≈ 22 q (917 ms) | idem | constante | nº 230 (72920) | −3 ms |
  | parte 3 (bolinhas dentro da parte 2) | f1768 | ≈ 20 q (833 ms) | bolinhas uma a uma | constante | nº 232 (73550) | +117 ms |
  | parte 4 (faixa teal fina) pintada | f1800 | ≈ 24 q (1000 ms) | pincelada que acompanha o instrumento | constante | nº 236 (75180) | −180 ms |
  | resultado: mancha laranja + 3 ondas no centro | f1830 | ≈ 14 q (583 ms) | mancha cresce + 3 ondas desenhadas | constante | nº 241 (76220) | +30 ms |
  (início dos passos observado no strip-geral; ritmo contínuo medido no perfil)
- Ritmo: 5125 ms, a cena mais longa de desenho; nenhum instante parado: o diagrama só fica completo no último ≈ 0,5 s (f1835–f1845). (medido)
- Som: nenhum efeito detectado (áudio mono; nenhum ruído de escrita audível no envelope). (medido)
- (conferido, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL na FORMA; o que era fica no bloco CONTEÚDO.)
- Textura (reestudo 20/11):
  - Folha: papel com fibra, creme amarelado, com sombreado próprio. f1840 região 60,110,200,90: #a4957e, grão 1,62 níveis, manchas 1,93, ac1 +0,65, direção levemente horizontal (h +0,69 × v +0,61), grão cinza (1,62/1,62/1,62). Cor varia na folha: topo L131–153 (#90816a–#a69780), meio-lado L175–177 (#bdad93), embaixo no centro L203 (#d9caab): mais escura em cima e nos cantos, mais clara embaixo no centro. Detalhe com realce: fibras e riscos horizontais finos (papel pautado gasto), manchas largas. Borda da folha com aro escurecido de ≈ 4 px (156 → 26 nos últimos px). Grão VIVO nos claros (medido, teste novo: f1838×f1840 e f1838×f1842 alinhados pela afim da folha, pixels lisos: claros resíduo/σ 1,49 e 1,48, correlação +0,21 e +0,20; escuros 0,85/0,67, correlação +0,70/+0,81): o papel ganha grão novo a cada imagem; a fibra e a pauta andam com a folha (corrigido na conferência: era "anda com a folha, parada em relação a ela").
  - Preenchimento laranja (cor quente de sistema): tinta granulada sobre o papel. f1840 região 250,580,60,60: #da9f66, grão 14,1 níveis, manchas 15,2, ac1 +0,69, grão VERTICAL (h +0,50 × v +0,88: estrias de pincel seco/lápis de cor no sentido vertical), grão colorido (B/G/R 12,2/13,9/15,6). VIVO (medido, teste novo: f1838×f1840/f1842, região 220,540,140,140: claros resíduo/σ 1,16/1,17, correlação +0,24/+0,18) (corrigido na conferência: era "PARADO entre quadros do mesmo estado, +0,96", medido dentro do mesmo par de quadros repetidos). Degradê radial: #e0955a no centro da mancha quente → #e4ad74 / #dfb072 a 120 px.
  - Faixa teal (cor fria de sistema): #6b9393 (teal acinzentado, a fibra do papel aparece por baixo), com linha ondulada escura no meio.
  - Zona entre as linhas (a camada intermediária): lavagem cinza-bege #b6a794 (L169) sobre papel #cebea5 (L191), ≈ 88 % do papel.
  - Tinta do traço: miolo #2d251a (preto acastanhado, não preto puro) de ≈ 4 px + 1 px de antisserrilhado de cada lado (linha x98–122, f1840); espessura quase constante, borda levemente irregular.
  - Instrumento de escrita: foto real recortada (preto brilhante com reflexo, anel metálico), adesivo branco irregular de ≈ 8–10 px em volta, borda do adesivo ondulada à mão.
- Efeitos (reestudo 20/11):
  - Vinheta do quadro: mesa com o foco de luz largo de sempre (fundo 21 em cima da folha, 24–32 nos lados).
  - Vinheta da imagem (folha): sim, própria do papel: topo a ≈ 65–75 % da luma do centro de baixo; lados a ≈ 87 %.
  - Borda borrada: nenhuma (nitidez cai na borda só por não ter desenho).
  - Sombra da folha (medido, f1840, linhas y400–500): à esquerda −30 % no contato (24 contra 34) e ainda subindo a +28 px, onde o quadro acaba (corrigido na conferência: era 26 → 32 em ≈ 20 px); em cima quase nenhuma (51 → 21, fundo 21); embaixo a borda da folha (y≈839) encosta na tarja e não se mede; à direita fica a foto de trás. Sombra muito fraca; o que separa a folha é o aro escuro da borda.
  - Sombra do adesivo do instrumento: fina e escura na borda externa (observado no detalhe, 1–2 px).
  - Desfoque de movimento: nenhum (o desenho é revelado, não deslizado). Aberração, brilho: nenhum. Grão global: nenhum aplicado no quadro; o grão vivo mora nos claros do papel e da tinta (ver Textura) (corrigido na conferência: era "nenhum").
- Câmera (reestudo 20/11): a folha aproxima sobre o próprio centro; f1760 → f1774 escala ×1,0213 (+3,7 %/s), centro (−0,14, +0,01 px/q), giro +0,14°; f1821 → f1835 ×1,0183 (+3,2 %/s), centro (−0,09, −0,12 px/q), giro 0,00°. Fim da cena (medido, f1831 → f1843, região 0,0,720,830): ×1,0134 (+2,7 %/s), centro (−0,05, −0,16 px/q): freia um pouco no fim, sem recuo. Quase constante. A foto de trás (V01-A26) continua aproximando por conta própria (diferença 8–16 por imagem na faixa x660–710); a mesa fica parada. (O par f1729 → f1743 não mede: o desenho novo engana o casamento de pontos.)
- Cadência (reestudo 20/11): 12 imagens/s em TODAS as camadas: desenho (perfil f1722–f1745: 97,2 / 0,08 / 11,7 / 0,00 / 16,3 / 0,00 / 14,9 / 0,00 / 14,0 …), margem da folha e foto de trás, todas com ≈ 0 nos quadros pares.
- Legenda nesta cena (reestudo 20/11): 7 blocos; o último bloco da cena anterior (f1703–f1724) atravessa a queda da folha (f1723); os seguintes trocam dentro da cena e o último (3 palavras, a conclusão; f1820–f1845) sai junto do corte (f1846). Texto #e5dc52–#eadf53. A folha cresce por baixo da tarja: até ≈ f1790 atrás dela está a mesa (luma 7 dentro × 26 fora); depois a borda de baixo da folha entra sob a tarja (f1840: papel L190–200 fora, L48–50 dentro, preto puro: o papel vira #353128). A ferramenta dá 56 % em f1840 porque mistura papel e mesa na medida de "fora"; o valor certo é 74 % (73,6–75,8 no vídeo), tarja de 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %). Folga da tarja em f1840: 5 px à esquerda (tarja x209, texto x214), 11 px em cima (tarja y847, topo das maiúsculas y858), ≈ 5 px embaixo (descendentes y887, tarja até y892, 46 px; corrigido na conferência: era y893, 6 px). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor (o desenho não tem rótulo).

## CONSTRUÇÃO
1. fundo: mesa #181516 com foco de luz largo, parada.
2. foto anterior (V01-A26) continua atrás, visível na faixa direita (x≈660–710), aproximando +6 %/s.
3. sombra da folha: à esquerda −30 % no contato, que some devagar (ainda visível a 28 px); em cima quase nenhuma (corrigido na conferência: era ≈ 6 níveis em ≈ 20 px).
4. folha: papel creme pautado gasto (#d4c5a6 no centro de baixo, #90816a–#a69780 no topo), retângulo vertical 79 % × 56 % da tela (x87–658, y89–804 em f1729), quase sem giro, aro escuro de ≈ 4 px na borda; grão VIVO nos claros do papel (ruído cinza ≈ 2–3 níveis sorteado de novo a cada imagem; a fibra e a pauta andam com a folha) (corrigido na conferência: era papel parado). Entrada: 0 ms a 109 % → 83 ms 102 % → 167 ms 100 % (estalo). Depois escala +3,5 %/s até 5125 ms (694x831 em f1845).
5. desenho (filho da folha, escala junto): traço #2d251a de ≈ 4 px revelado ao longo do caminho em velocidade constante (≈ 1 caminho por 0,8–1,0 s); preenchimentos em modo multiplicar sobre o papel: zona intermediária #b6a794 (lavagem), faixa fina da cor fria de sistema (teal #6b9393) com linha ondulada, mancha da cor quente de sistema (laranja) em degradê radial #e0955a → #e4ad74 com grão vertical forte (≈ 14 níveis), também com grão vivo nos claros, e 3 linhas onduladas desenhadas por cima.
6. instrumento de escrita: foto recortada com adesivo branco irregular 8–10 px, inclinada ≈ 45° (ponta para baixo à esquerda), com a ponta presa ao fim do traço em cada imagem; entre partes ela salta para o próximo início.
7. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Linha do tempo (ms a partir da queda da folha, f1723 = 71792 ms): 0 folha cai (estalo 167 ms) · 83 ms o instrumento começa a parte 1 (contorno da figura, ≈ 958 ms) · 1125 ms parte 2 (contorno duplo em volta) · 1875 ms parte 3 (bolinhas uma a uma) · 3208 ms parte 4 (faixa teal pintada) · 4458 ms resultado (mancha quente cresce + 3 ondas, ≈ 583 ms) · 4958–5125 ms diagrama completo · 5125 ms corte seco.
- Parâmetros que dependem do conteúdo: o desenho (quantas partes, em que ordem: a ordem da frase), as cores de sistema usadas (teal = frio, laranja = quente), o instrumento recortado.
- O que NÃO fazer: preencher com cor chapada opaca (a cor tem de deixar ver o papel), traço preto puro e fino demais (é ≈ 4 px, preto acastanhado), mostrar o desenho pronto e só "revelar" com máscara de varredura (o traço segue um caminho, como mão), pausar o instrumento, animar a 24 imagens/s, esquecer o grão vertical da mancha quente, congelar o grão do papel (ele troca a cada imagem nos claros), usar folha branca limpa.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "a ideia central, em diagrama": o desenho que a pessoa teria rabiscado, em partes, na ordem da explicação.
  - "instrumento de escrita": recorte da caneta/lápis.
- Nesta referência as lacunas foram preenchidas com: corpo + roupa + bolhas + fina camada de água + calor no peito; caneta-tinteiro preta.
- Receita de tratamento de cada imagem: folha de papel real (foto de papel envelhecido creme), traço preto acastanhado de ≈ 4 px tipo caneta (alinhado ao reestudo), cores de destaque do sistema (teal, laranja) em tinta translúcida com grão, multiplicada sobre o papel (alinhado ao reestudo), instrumento recortado com adesivo.
- Regra de escolha: "ele escreveu a ideia" → a ideia é DESENHADA na tela, na mesma ordem em que a fala a resume, terminando no resultado (aqui: quente).
- Teste de generalização: (1) Claude Code: "ele escreveu num guardanapo: o agente não precisa lembrar, precisa anotar" → caneta desenha um robô, depois um caderno ao lado, setas, e o caderno acende. (2) café: "ele anotou: a água não precisa ferver" → caneta desenha um bule, um termômetro em 92°, e o café dourado no fim.
- Receita de tratamento (reestudo 20/11): folha = foto de papel de caderno real, gasto, creme amarelado, com pauta fraca e sombreado escuro no topo; instrumento = foto real recortada com adesivo branco irregular; todas as cores do desenho em multiplicar sobre o papel.
- Receita de ILUSTRAÇÃO (reestudo 20/11): diagrama de caderno em corte, feito de contornos de caneta (#2d251a, ≈ 4 px, irregularidade leve) + preenchimentos de tinta translúcida com grão (laranja de calor com estrias verticais ≈ 14 níveis, teal acinzentado da água, lavagem cinza do material); formas simples (silhueta de busto, faixas paralelas que acompanham o contorno, bolinhas abertas de tamanhos variados, ondas de calor em 3 linhas); se destaca do fundo por estar dentro da folha clara; o traço não "ferve" (fica parado depois de desenhado); é revelado pela caneta, parte por parte, na ordem da fala.
- Teste de generalização (reestudo 20/11): (1) Claude Code: "ele anotou: o agente não precisa lembrar de tudo" → a caneta desenha um contorno de cabeça, depois um caderno ao lado ligado por uma seta, e o caderno ganha preenchimento laranja no fim. (2) café: "ele escreveu: a água não precisa ferver" → a caneta desenha um bule em corte, a faixa de água teal dentro e o vapor laranja só no final.

- Confiança: tamanhos, cores e tempos medido; ordem e conteúdo das partes do desenho observado.
