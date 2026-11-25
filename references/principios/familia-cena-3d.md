# Família · Cena 3D (regras comuns aos princípios dela)

> Extraído do GUIA-DE-ESTILO do Estilo 03 (treino com 5 reels de referência). Onde o texto cita `still.png`, `strip.jpg` ou `clip.mp4` de uma Ref (ex.: V01-A28), nesta skill só existem `biblioteca/<ID> …/notes.md` (a medida) e `thumb.jpg` (miniatura). Onde cita "o Felipe", é o autor do método: veja `references/decisoes-do-autor.md`.

# Família · Cena 3D

> **Nota do redator (9-cena-3d.md).** > **Aviso único da família (vale para P23 e P24).** As duas cenas 3D só existem no V05 (23 pastas,
> > ≈ 97 s de 165,5 s, ou seja 59 % do vídeo). Os outros 4 vídeos contam a mesma coisa com imagens reais
> > em cartão (família Imagem em cartão). Força máxima possível aqui: "regra dentro de 1 vídeo".
> > **Não se sabe se o 3D é o caminho novo do criador ou uma escolha só daquele vídeo** (o próprio V05
> > mistura as cenas 3D com fotos reais em cartão, P06/P09). É uma dúvida para o Felipe decidir: usar a Cena 3D
> > como opção normal do editor, só quando o tema não tiver imagem real, ou nunca.
> > Medidas de cor: "saturação do quadro" é a métrica `med.py sat` dos analistas (0 a 1, média do quadro,
> > **medido**). "Croma" e "S" são calculados por mim a partir dos hex amostrados nos `notes.md`
> > (croma = maior canal − menor canal, 0 a 255; S = saturação HSV; matiz em graus), **calculado**,
> > 1 ponto por amostra.
> 
> **Acabamento comum da família (reestudo de 20/11; vale para P23 e P24).** Tamanhos em px do quadro 720x1280.
> - **Perfil:** a família só aparece no V05, então o perfil é um só, o **Perfil V05**. Não emprestar para uma cena 3D o papel que
>   ferve do V01 e do V03, a sombra multiplicativa do V03 nem a vinheta global do V04 (globais §12.2: nunca misturar perfis).
> - **A regra "a mesa fica parada e só as peças andam" NÃO vale nesta família.** Aqui a câmera é uma câmera de verdade: a imagem
>   inteira anda e escala junto. Em A01 o topo e o baixo andam −10,85 e −10,53 px/q, sem paralaxe porque a superfície é plana
>   (**medido**); em A09 o recipiente da frente corre mais que a parede do fundo, paralaxe de cena 3D real (**observado** no strip).
>   Ficam PARADOS na tela só a vinheta (A01: "não mover a vinheta junto com a câmera"), o feixe de luz (A23: correlação no lugar
>   +0,83, **medido**), a legenda e os rótulos de P04.
> - **Grão:** nenhum grão de filme acrescentado nas 23 pastas. Bases pretas e chãos lisos ficam lisos e parados: base A30 grão 0,27,
>   A36 0,28 (correlação +1,00), chão A15 0,47, A23 0,78 (**medido**; a conferência fixou "mesa e fundos chapados do V05 são
>   PARADOS", +0,90 a +1,00). O detalhe que se vê é o do material da imagem e anda com a câmera (A01 +0,98 e A02 +0,90 depois de
>   alinhar). A sépia não acrescenta grão colorido (A02 B/G/R 10,3/10,6/10,7). O "grão 4,0" do canto de A01 é a imagem macia mais
>   compressão, não ruído.
> - **Vinheta:** só nas cenas (o rosto não tem), multiplicativa, parada na tela, por cima das imagens e também dos objetos que saltam
>   para a câmera (A17: borda a 27 % por cima do objeto gigante). A nitidez cai junto com a luma: é escurecimento, não desfoque,
>   com duas exceções de borda mole (A04 close: nitidez 11 % × luma 34 %; A39: nitidez 10 % × luma 24 %). Lida em A04 como duas
>   partes somadas (**observado** na comparação de planos): uma vinheta de tela fixa (borda a 34–44 % nos closes) e a queda de luz
>   da própria cena nos planos abertos (borda a 7–22 %). A força de cada cena está no princípio.
> - **Sombra:** nenhuma sombra de composição. Só a da própria imagem ou do próprio render: contato de 4–5 px tirando 38 % entre peças
>   planas (A01, **medido**); contato suave dos personagens no chão (P24, **observado**). O que passa por cima da cena não projeta
>   sombra (lupa A03, objeto que salta A17: **medido**). As sombras de painel (≈ 120 px a 55 %) e de cartão (≈ 30 px a 30 %) do
>   Perfil V05 são de outras famílias e não entram aqui.
> - **Desfoque de movimento:** quase nunca. Nenhum no push-in de A01, na lupa de A03, no travelling de A09 (personagem nítido em
>   f690) e no salto de A17 (bordas nítidas a meio caminho, f1056). Existe em 2 casos: a página que entra pela esquerda em A53
>   (rastro horizontal de 40–60 px, f3796) e os pedaços que caem em A44 ("leve", não medido em px). **Diferença com os globais
>   §12.2**, que dão "V05: entradas de objeto com desfoque de 20–60 px": nesta família o objeto que salta entra nítido; só a peça
>   plana que desliza para dentro leva rastro.
> - **Cadência:** 24 imagens/s em todas as camadas das 23 pastas (câmera, personagens, varreduras de cor, círculos, partículas,
>   fogo); nenhum degrau de 2 quadros e nenhuma camada a 12 imagens/s (**medido** no `perfil` de cada nota).
> - **Câmera por fases:** nenhuma cena usa um zoom linear do 1º ao último quadro como regra. Repouso entre −2,3 e +3 %/s; picos na
>   palavra de +7 a +14 %/s nas cenas de personagem e até +71 %/s nos mergulhos de P23; recuos de −14,7 a −20 %/s quando a cena
>   abre; a câmera para ou quase para enquanto o personagem ou o objeto age (A15, A23, trechos de A09 e A38). Muitos planos cortam
>   em movimento (A04, A05, A07, A30, A38, A39, A40, A44, A46, A53).
> - **Legenda sobre a Cena 3D (Perfil V05):** tarja preta pura a 68 % (66–72), 51 px de altura (y 809–859), raio ≈ 8–9 px, 12 px
>   acima das maiúsculas e 11 px abaixo da linha de base, texto 28 px (35 com descendente), centro em y ≈ 65,5 %, miolo #f0e816
>   (globais; nas notas #eee716 a #f3e714). Vale a decisão da conferência: os 59–67 % de várias notas eram estimativa do censo.
>   A cara da tarja muda com o fundo: sobre a base preta das cenas de personagem (luma fora 26–32) ela some e o amarelo fica solto;
>   sobre roupa ou pedra em meio-tom (luma 42–66) vira uma caixa escura discreta; sobre tecido claro em close (A05, luma 154–160)
>   vira um retângulo cinza nítido. As imagens e o objeto que salta passam por baixo dela; círculos, rótulos e etiquetas ficam
>   acima, sem encostar. Troca de bloco e sumiços: em cada princípio.
