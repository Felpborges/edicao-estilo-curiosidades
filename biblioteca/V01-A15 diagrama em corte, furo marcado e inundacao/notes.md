# V01-A15 · diagrama em corte sozinho: furo marcado à mão, água inunda, calor apaga
- Categoria: P18 · Diagrama chapado com estados (provisória do analista: (provisória) diagrama em corte dentro de disco com aro (tela cheia), com marcação à mão e estados que mudam)
- Fonte: V01 quadros f808–f898 (33,67–37,42 s; 91 quadros ≈ 3792 ms) · 24 fps
- Fala: "If water got in, it flooded the wool and the wool stopped working."
- Tipo de fala: consequência (o que acontece quando o sistema falha)
- Gatilho: corte seco em f808 = 33667 ms, −23 ms antes da palavra nº 109 "If" (33690 ms).
- Quadro-chave: f860
- Camadas ativas: cena de tela cheia | grafismo (marcação à mão) | legenda
- Leitura dos strips: strip.jpg = quadros f806 a f820, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 15 células. strip-saida.jpg = quadros f836 a f852 (a inundação), mesma regra, 17 células. strip-geral.jpg = quadros f806 a f900, de 2 em 2, 48 células. Cada célula traz o nº do quadro e o tempo. Detalhes do reestudo: detalhe-circulo-a-mao.jpg = quadro f830, região x200 y330 130x130 px, ampliada 3× sem suavizar · detalhe-frente-inundacao.jpg = quadro f846, região x420 y370 230x130 px, ampliada 2× sem suavizar · detalhe-rotulo-contorno.jpg = quadro f860, região x150 y395 150x70 px, ampliada 3× sem suavizar.

## LEITURA DE EDITOR
- Por que esta cena aqui: logo depois da virada no rosto ("até que não funcionou"), a fala conta a falha; o editor volta ao MESMO diagrama, agora sozinho na mesa, e mostra a falha nele.
- Por que este design: reusar o corte que o espectador já aprendeu poupa explicação; tirar a pilha de fotos de trás isola o problema; um círculo à mão aponta o furo como professor no quadro.
- Por que estas cores: o teal (água) invade o laranja (fibras aquecidas) e o laranja da base apaga para creme: a troca quente → frio conta a história sem palavras; o amarelo-limão translúcido da marca é a única cor "de caneta" e se lê como anotação.
- Por que estes efeitos: o círculo é traço de marcador translúcido (escurece sobre o preto, esverdeia sobre o teal), aberto e com sobreposição no fim; a frente da inundação é irregular, orgânica; o rótulo ganha contorno creme para ler sobre o teal.
- Por que este movimento: o traço se desenha em 4 imagens enquanto o bico de água fura a barreira; a água varre a camada da esquerda para a direita, acelerando e freando; o calor apaga devagar no fim.
- Sensação do movimento: "olha aqui… e aí tudo encharcou": tensão rápida no círculo e inevitabilidade na varredura; produzida pelo traço revelado em ≈ 250 ms, a varredura de ≈ 583 ms com pico em f846 (diferença 21,5) e o apagamento de ≈ 500 ms, a 12/s.

## FORMA (fixa: reproduzir igual)
- Mesmo diagrama de V01-A14 (faixas: área de fora em teal = o agente externo, faixa preta = a camada externa, camada do meio texturizada, base creme com o benefício em laranja), agora SOZINHO no centro do fundo escuro, sem fotos atrás. (conferido: mesmas cores e faixas no strip)
- Design (quadro cheio): disco com aro off-white: caixa f810 x62–659, y182–779 = 598x598 px (83,1 % da largura, 46,7 % da altura), centro (50,2 %, 37,9 %). (medido com med.py) Em f860 (still): x63–672, y170–778 = 609x608 px (84,6 % da largura) (medido, remedição f860).
- Marcação à mão: círculo aberto desenhado em amarelo-mostarda (≈ #b9b04d, medido aproximado; translúcido como marca-texto), traço 8 px de espessura (alinhado ao reestudo), ≈ 90 x 95 px (x216–305, y346–441; ≈ 12,5 % da largura), centro ≈ (260, 393), em volta do ponto de falha na faixa preta (remedido, f830 ampliado; antes ≈ 80 px); cor #8e8219 sobre a faixa preta e #9da734 sobre o teal (translúcido). Visível de f812 a f841: some seco em f842, quando o agente começa a inundar a camada do meio, por isso NÃO aparece no still f860 (remedido, folha f806–f852). (medido)
- Ponto de falha: um bico teal (o agente) atravessa a faixa preta e pinga na camada do meio. (observado)
- Rótulo da camada do meio (1 palavra, sans bold caixa alta preta pequena, COM contorno creme em volta das letras; caixa do contorno x165–282, y414–446 = 117x32 px, 2,5 % da altura) volta quando a camada do meio troca para a cor do agente. (remedido, f860; antes sem menção ao contorno)
- Movimento:
  - Entrada: corte seco com assentamento de 1–2 imagens: caixa f808 548 px (91,6 %) → f810 598 (100 %) → f812 592 (99 %). Estalo com leve sobra. (medido)
  - Deriva: cresce devagar até 636 px em f896; zoom +4,3 %/s no começo, freando para +3,0 %/s no fim (alinhado ao reestudo). (medido)
  - Cadência: 12 imagens/s, fase nos quadros pares (perfil: f810, f812…). Textura da camada do meio animada o tempo todo (diferença 5–13 por imagem). (medido) (corrigido no reestudo: como em V01-A14, o desenho de fibras não ferve; a diferença vem da deriva da câmera, +4,3 %/s, sobre linhas de alto contraste, e da varredura.)
  - Saída: corte seco para o A-roll em f899. (medido)
- Passos internos:
  | passo | quadro | duração | movimento | curva | palavra-gatilho | deslocamento |
  |---|---|---|---|---|---|---|
  | diagrama aparece | f808 | 4 q (167 ms) | escala 92 → 100 % | estalo | nº 109, 1ª palavra da condição | −23 ms |
  | círculo amarelo se desenha + bico do agente fura a faixa | f812 | ≈ 6 q (250 ms) o traço (completo em f818; some em f842); o bico cresce até f830 | revelação do traço a mão (stroke) + gota descendo | contínua | nº 110, o agente nomeado (33820) | +13 ms |
  | o agente inunda a camada do meio da esquerda para a direita | f838 | ≈ 14 q (583 ms), pico f846 (diferença 21,5) | varredura horizontal da cor teal sobre a textura | acelera e desacelera | nº 114, o verbo da invasão (34800) | +117 ms |
  | rótulo da camada do meio reaparece sobre ela, já na cor do agente | f850 (remedido; antes f852) | 1 imagem | aparece seco | — | nº 116, o nome da camada (35460) | −43 ms |
  | o benefício (laranja da base) apaga (vira creme) | f868 | ≈ 12 q (500 ms) | fade da cor | contínua | nº 120, o verbo da perda (36380) | −213 ms |
  (quadros medido no perfil da região x60 y250 600x600; o resto observado no strip-geral)
- Ritmo: 3792 ms (a cena de diagrama mais longa até aqui); estado final sem passo novo (o zoom segue a +3,0 %/s) de f880 a f898 = 750 ms (alinhado ao reestudo). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Mesa: a de V01-A01 (poça de luz visível em volta do disco).
  - Diagrama: as superfícies de V01-A14 (teal #41828d liso, faixa preta, fibras desenhadas, base creme com laranja granulado #e8b97c; aro greige). Teste novo (f884×f886, alinhado pela cena 0,0,720,820): base creme apagada, claros (250,640,220,110) resíduo ÷ σ 1,26 (4,5 níveis) = VIVA; teal de cima (200,220,320,120) σ 1,16 e resíduo 1,35 níveis, perto do piso = PARADO. (medido)
  - Fibras molhadas: depois da varredura a faixa fica teal #40787f com os rabiscos trocados por linhas onduladas azul-escuras finas (detalhe-frente-inundacao).
  - Marca à mão: traço de marcador amarelo-limão translúcido, 8 px (linha y395 x214–222), largura levemente irregular, sem grão; luma 120–127 sobre o preto (lido #544913, oliva escuro) e #7a9862 sobre o teal (verde-amarelado) → tinta transparente (≈ 55–60 % ou modo de mistura multiplicar/sobrepor; inferido pela mudança de cor com o fundo).
- Efeitos (reestudo 20/11):
  - Vinheta do quadro (`borda` f860): 100 / 66 / 48 / 23 / 16 % com nitidez caindo junto: é o disco claro no meio da mesa escura + a poça de luz, não vinheta aplicada.
  - Frente da inundação: borda irregular, orgânica, sem esfumado nem espuma; a cor cobre as fibras e o desenho embaixo troca de estilo.
  - Rótulo: contorno creme de ≈ 3 px em volta das letras pretas quando está sobre o teal (detalhe-rotulo-contorno).
  - Bico de água no furo: teal com fios claros de 2 px nas laterais (realce de borda), atravessando a faixa preta.
  - Sombra do disco sobre a mesa: CAI PARA BAIXO (`sombra` 4 lados alinhada, f860, caixa 63,170,609,608): embaixo −49 % no 1º px fora e volta em 19 px; esquerda −31 % e direita −24 %, voltam em 15–17 px; em cima −12 % só no 1º px (medido; corrigido na conferência: era "nenhum").
  - Brilho, desfoque de movimento, profundidade, grão global, aberração: nenhum (f830, f846, f860).
- Câmera (reestudo 20/11): zoom in lento do disco: `camera` f820→f836 ×1,0287 (+4,3 %/s), (+0,70, +0,29) px/q; f880→f896 ×1,0196 (+3,0 %/s), (−0,14, −0,40) px/q (desacelera). Mesa parada (a poça de luz não acompanha).
- Cadência (reestudo 20/11): 12 imagens/s, fase nos pares; o traço do círculo avança 1 vez por imagem (f812, f814, f816, f818: ≈ 1/3, 2/3, 90 %, fechado).
- Legenda nesta cena (reestudo 20/11): 4 blocos: a condição (f808–f831, 4 palavras, entra no MESMO quadro do corte), a consequência até o artigo (f832–f851, 3 palavras; a varredura começa em f838), o nome da camada dito duas vezes (f852–f875, 4 palavras; o rótulo voltou 2 quadros antes, f850), o fim da consequência (f876–f898, 2 palavras; o laranja começou a apagar em f868, 8 quadros antes). Atrás da tarja: a mesa (o disco termina em y≈779) → tarja preta pura lida como preta (74 % no vídeo, medida direta da conferência). Outro texto junto: o rótulo do diagrama (de f850 em diante). Cor #e9dd54.
- Entrada do texto (reestudo 20/11): o rótulo reaparece seco em f850, 100 % no quadro, já com contorno creme (sem fade, escala ou deslocamento); a marca à mão NÃO é texto: é revelada como traço em 4 imagens (f812 → f818), sentido horário, começando em cima à esquerda e terminando com sobreposição no mesmo ponto; some seco em f842.

## CONSTRUÇÃO
1. fundo: mesa fixa (poça de luz).
2. disco do diagrama (o mesmo de V01-A14, sem a pilha atrás): caixa x62–659 y182–779 em f810 (83,1 % da largura), centro 50,2 % × 37,9 %; estado inicial = água teal em cima até a faixa preta, fibras laranja, base com laranja (creme da base com grão vivo trocado a cada imagem; teal, faixa preta e fibras parados). Sombra caída para baixo na mesa: embaixo −49 %, some em 19 px; dos lados −24/−31 %, 15–17 px; em cima só 1 px. Entrada em 0 ms (f808): 91,6 % → 83 ms 100 % → 167 ms 99 %. Zoom +4,3 → +3,0 %/s até o corte.
3. bico de água: em 167 ms (f812) uma ponta teal atravessa a faixa preta no terço esquerdo (x≈260) e começa a pingar na faixa de fibras, crescendo até ≈ 917 ms (f830).
4. marca à mão: círculo de marcador amarelo-limão translúcido (≈ 55–60 %), traço 8 px, ≈ 90 × 95 px em volta do bico (centro 260, 393), revelado em sentido horário de 167 ms a 417 ms (f812–f818), fecha com sobreposição; some seco em 1417 ms (f842).
5. varredura: de 1250 ms (f838) a ≈ 1833 ms, o teal cobre a faixa de fibras da esquerda (do bico) para a direita, frente irregular, ease-in-out (pico em f846); as fibras viram linhas onduladas azul-escuras finas.
6. rótulo da camada: em 1750 ms (f850), preto caixa alta bold com contorno creme de 3 px, à esquerda do centro, 100 % no quadro.
7. apagamento: de 2500 ms (f868) a ≈ 3000 ms o laranja da base desbota até creme #d6cec1 (fade).
- Linha do tempo (ms a partir de f808): 0 disco + legenda da condição · 167 bico + início do traço · 417 círculo fechado · 1000 legenda da consequência · 1250 varredura · 1417 círculo some · 1750 rótulo · 1833 legenda do nome da camada · 2500 laranja começa a apagar · 2833 legenda do fim da consequência · 3000 estado final parado · 3792 corte seco para o rosto.
- Parâmetros que dependem do conteúdo: onde fica o ponto de falha (onde o círculo é desenhado), a direção da invasão, o que apaga no fim.
- O que NÃO fazer: círculo amarelo opaco ou perfeito (é marcador translúcido, à mão, com sobreposição); círculo aparecendo inteiro (é revelado em 4 imagens); varredura com borda reta (é irregular); manter o círculo durante a inundação (some quando a água começa a varrer); rótulo sem contorno sobre o teal; disco sem sombra (cai para baixo, como as fotos).

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o diagrama do sistema" já apresentado antes (reaproveitado do passo anterior).
  - "o ponto de falha": onde marcar o círculo à mão.
  - "o que invade" e "o que se perde": duas cores que mudam de estado.
- Nesta referência as lacunas foram preenchidas com: corte da roupa antiga (água fora, borracha, lã, corpo); furo na borracha; água entra e inunda a lã, calor some; rótulo "WOOL".
- Receita de tratamento de cada imagem: mesmo corte vetorial do passo anterior (continuidade), marcação a mão em amarelo translúcido, traço irregular aberto.
- Receita de ILUSTRAÇÃO (reestudo 20/11): o diagrama de V01-A14 (faixas chapadas, fibras em rabisco, aro greige) recebe três camadas de "anotação": (a) marca de marcador amarelo-limão translúcido (≈ 55–60 %), traço 8 px de largura irregular, círculo aberto que fecha com sobreposição, revelado como traço em 4 imagens; (b) o agente que invade é cor chapada com frente irregular que varre a faixa e troca o desenho de dentro (rabiscos claros → linhas onduladas escuras finas); (c) o benefício que se perde desbota por fade para o creme. Rótulos pretos ganham contorno creme de 3 px quando o fundo fica escuro/frio.
- Regra de escolha: na virada ("until it didn't" → "if water got in…"), reusa-se o mesmo diagrama e mostra-se a falha nele: marca o ponto, anima a consequência, apaga o benefício.
- Teste de generalização: (1) Claude Code: o corte "arquivo / HOOK / erro" do passo anterior; marca à mão um buraco no hook e o vermelho invade a camada do arquivo. (2) café: o corte "água / filtro / pó"; marca um rasgo no filtro e o pó vaza para o café.

- Confiança: tamanhos, tempos e curva medido; cor da marcação medido aprox.; rótulo e direção da inundação observado.
