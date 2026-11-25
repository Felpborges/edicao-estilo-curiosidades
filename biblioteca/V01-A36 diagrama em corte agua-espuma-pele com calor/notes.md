# V01-A36 · diagrama em corte (água / faixa de células / pele) com calor que fica
- Categoria: P18 · Diagrama chapado com estados (provisória do analista: (provisória) diagrama em corte dentro de disco com aro)
- Fonte: V01 quadros f2519–f2558 (104,96–106,58 s; 40 quadros ≈ 1667 ms) · 24 fps
- Fala: "the foam still insulates."
- Tipo de fala: conclusão (do mecanismo: "a espuma continua isolando")
- Gatilho: troca seca em f2519 = 104958 ms, −122 ms antes da palavra nº 341 "the" (105080 ms). Calor em f2525 = 105208 ms, +88 ms depois da nº 342 "foam" (105120 ms) (remedido).
- Quadro-chave: f2550
- Camadas ativas: cena de tela cheia | grafismo | legenda
- Leitura dos strips: strip.jpg = quadros f2515 a f2534, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 20 células; cada célula traz o nº do quadro e o tempo. Novos do reestudo (20/11): detalhe-celulas-calor.jpg = quadro f2550, região x200 y500 240x180 px, ampliada 2× sem suavizar · detalhe-aro-sombra.jpg = quadro f2550, região x520 y620 150x150 px, ampliada 3× sem suavizar.


## LEITURA DE EDITOR
- Por que esta cena aqui: a frase fecha o raciocínio ("ainda isola"); o editor troca o close das células por um corte em camadas que mostra o RESULTADO: água em cima, barreira no meio, calor que fica embaixo.
- Por que este design: o mesmo disco com aro, agora com 3 faixas horizontais empilhadas: leitura de cima para baixo, frio → barreira → quente.
- Por que estas cores: teal (frio, água) e laranja (calor) separados pela faixa de células escuras em papel creme; é a síntese do código de cores do vídeo.
- Por que estes efeitos: degradês em sentidos opostos (o teal clareia perto da barreira, o laranja escurece e satura para baixo) dão profundidade às faixas; o calor tem mancha de aerógrafo viva, a água é lisa.
- Por que este movimento: troca seca do diagrama (o parêntese da foto some junto) e o calor sobe da base em 250 ms, na palavra "espuma": o efeito aparece logo depois de nomear a causa.
- Sensação do movimento: conclusão firme e calma; um único gesto (o calor enchendo) e depois só a aproximação lenta.

## FORMA (fixa: reproduzir igual)
- Mesma linguagem do corte de V01-A14/A15 (disco com aro, faixas horizontais), agora com: área de fora em teal em cima (o agente de fora, com ondas), faixa do meio com o padrão da estrutura em unidades escuras (a barreira vista de lado), base creme = a camada de dentro, com o benefício em laranja #e48750 (f2550, 360,640) em degradê subindo da base. Conjunto f2523 x17–704, y162–763 (688x602 px, disco + foto que ainda aparece atrás). Só o disco, em f2550: borda externa x≈47–667, y≈157–775 = diâmetro ≈ 620 px (86 % da largura), centro ≈ (357, 466) px = (49,6 %, 36,4 %) (medido, remedição f2550, varredura na linha y460 e na coluna x360). (cor e caixa medido; faixas observado)
- Movimento: troca seca do disco da estrutura para este corte (f2519; med.py: caixa f2519 688x644 → f2521 688x614 → f2523 688x602 = assenta em 2 imagens); o benefício (laranja) cresce da base de f2525 a f2531 (6 q, 250 ms; perfil 23,5 → 13,8 → 9,4 → 7,7 = tremor) (remedido); depois sem estado novo, só o grão vivo do laranja e a aproximação +4,2 %/s (alinhado ao reestudo). Saída por corte seco para o A-roll em f2559. Cadência 12 imagens/s. (medido; crescimento do laranja observado)
- Ritmo: 1667 ms; completo, sem estado novo e aproximando +4,2 %/s (alinhado ao reestudo), de f2531 a f2558 (1167 ms) (remedido). (medido)
- Som: nenhum efeito detectado (áudio mono). (medido)
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Faixa do agente de fora: teal lisa, #2a5b64 (f2550 região 150,270,200,40), grão 0,50, manchas 2,33 (degradê), PARADA (correlação +0,70 / +0,75; teste novo f2550×f2552, afim do disco, região 100,250,500,100: resíduo/σ 0,66, correlação +0,79 = PARADA, mesmo veredito). Degradê vertical: #234850 (L65) no topo → #2f6974 (L94) junto da barreira. Traços claros curtos horizontais (ondulação), como em V01-A34.
  - Faixa do benefício: laranja com mancha de aerógrafo, #cf7a46 (f2550 região 200,640,250,60), grão 1,31, manchas 5,10, VIVA (correlação +0,21 / +0,25; teste novo f2550×f2552, região 100,580,520,90: claros resíduo/σ 1,23, correlação +0,06; médios 1,23, +0,08 = VIVA, mesmo veredito). Degradê vertical: #e9ad6e (L182) junto da barreira → #e4a16a (L172) → #c56d38 (L124) → #a05123 (L95) na base (mais escuro e saturado embaixo).
  - Faixa das unidades: unidades escuras com reflexo curvo (como V01-A33) em papel creme granulado, PARADA (teste novo, região 60,390,600,140: resíduo/σ 0,88–0,91, correlação +0,63); faixa creme lisa entre as unidades e o benefício.
- Efeitos (reestudo 20/11):
  - Aro e sombra do disco (coluna x360, f2550): miolo → aro creme L208–222 de 8 px (y770–777) → fio escuro de 1 px (L11,6 em y779) → mesa voltando de 19 a 28 em ≈ 20 px (sombra curta e difusa). Nos 4 lados (medido, f2550, perfil alinhado): embaixo −46 % no contato, volta em 20 px; em cima −15 %, volta em 6 px; à direita −30 % a +4 px, volta em ≈ 29 px (sobre a foto de trás, baixa confiança); à esquerda a foto de trás encosta e não se mede. Caída para baixo, como as das fotos.
  - Degradê: sim, nas faixas teal e laranja (sentidos opostos). Brilho: reflexos nas células.
  - Vinheta, desfoque, aberração: nenhum (medido em f2550). Grão global: nenhum aplicado; o grão vivo está só na faixa laranja (ver Textura).
- Câmera (reestudo 20/11): o disco aproxima devagar: f2531 → f2545 escala ×1,0244 (+4,2 %/s), centro (−0,10, +0,16 px/q), giro 0,00°. Fim da cena (medido, f2544 → f2556, região 0,0,720,830): ×1,0206 (+4,2 %/s), centro (−0,10, +0,04 px/q): o mesmo ritmo até o corte. A foto de trás segue atrás (laterais). Mesa parada.
- Cadência (reestudo 20/11): 12 imagens/s (perfil f2518–f2536: 0,31 / 72,5 / 3,0 / 27,3 / 0,02 / 17,1 / 0,04 / 7,8 / 0,28 / 4,9 / 0,28 / 4,2 …; o 3,0 em f2520 é o fim da troca).
- Legenda nesta cena (reestudo 20/11): 3 blocos: o último da cena anterior (1 palavra; f2513–f2520) atravessa a troca (f2519); o 2º (2 palavras, f2521) entra 2 quadros depois da troca; o 3º (2 palavras, a conclusão; f2534–f2558) termina no corte seco. Texto #eade53, 68 %. Atrás da tarja: a mesa (o disco termina em y≈779). Tarja preta pura a 74 % (73,6–75,8 no vídeo), 46 px (y847–892) (medido na conferência; corrigido na conferência: era ≈ 75 %). Nenhum sumiço, nenhum outro texto.
- Entrada do texto (reestudo 20/11): não há texto do editor.

## CONSTRUÇÃO
1. fundo: mesa #181516, parada.
2. foto de trás (V01-A32), visível nas laterais.
3. disco: aro creme 8 px + fio escuro 1 px + sombra caída para baixo (embaixo −46 % no contato, some em 20 px; em cima −15 %, 6 px); Ø ≈ 620 px (86 % da largura), centro (49,6 %, 36,4 %) em f2550.
4. faixas (recortadas pelo círculo, de cima para baixo): agente de fora em teal liso e PARADO com degradê #234850 → #2f6974 e traços claros (≈ 40 % do diâmetro); faixa das unidades escuras com reflexo em papel creme, parada (≈ 22 %); faixa creme lisa fina; benefício em laranja com mancha de aerógrafo e grão VIVO (re-sorteado a cada imagem) e degradê #e9ad6e → #a05123 até a base.
5. legenda: tarja preta pura a 74 %, 46 px de altura, texto #eade53, 68 %.
- Animação: 0 ms (f2519) troca seca do disco anterior para este, a 107 % da altura → 83 ms 102 % → 167 ms 100 %; 250–500 ms o laranja enche a faixa de baixo subindo da base (6 quadros); depois só aproximação +4,2 %/s. Passos de 2 quadros.
- Linha do tempo (ms a partir da troca, f2519 = 104958 ms): 0 troca seca (a foto de cima some junto) · 83 ms 2º bloco de legenda · 250 ms o benefício (laranja) começa a subir · 500 ms laranja completo · 625 ms 3º bloco (a conclusão) · 1667 ms corte seco para o rosto.
- Parâmetros que dependem do conteúdo: as faixas (o que está fora, a barreira, o que está protegido) e o estado que "fica" (a cor quente aqui).
- O que NÃO fazer: deixar o teal vivo e o laranja parado (é o contrário), faixas sem degradê, laranja chapado sem mancha, mudar de disco com transição suave (é seco), esquecer o aro e o fio escuro.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas:
  - "o sistema em corte": 3 faixas (fora / barreira / dentro).
  - "o benefício que se mantém": cor quente que fica do lado de dentro.
- Nesta referência as lacunas foram preenchidas com: água / espuma / pele; calor.
- Receita de tratamento de cada imagem: vetorial chapado no mesmo disco com aro de papel; a faixa do meio repete o padrão de células da cena anterior (continuidade).
- Regra de escolha: conclusão do mecanismo ("então mesmo molhado, isola") → o corte mostra as 3 camadas e o estado bom (quente) aparece e fica.
- Teste de generalização: (1) Claude Code: corte "ruído / blocos isolados / projeto", e o projeto acende verde e fica. (2) café: corte "ar / crema / café", e o café fica dourado quente.
- Receita de ILUSTRAÇÃO (reestudo 20/11): corte em faixas horizontais dentro do disco: meio externo em teal liso com degradê e traços curtos de ondulação; barreira como faixa de células escuras com reflexo em papel creme; meio protegido em laranja de aerógrafo com grão vivo e degradê que escurece para a base; separação por cor chapada, sem contornos.
- Teste de generalização (reestudo 20/11): (1) Claude Code: "mesmo com um pedido malicioso, o arquivo protegido continua seguro" → disco com faixa teal de "pedidos" em cima, faixa de blocos escuros no meio, faixa laranja embaixo que se enche na palavra "seguro". (2) café: "mesmo no frio, a garrafa térmica mantém o café quente" → disco com ar frio teal em cima, parede de células no meio, café laranja embaixo enchendo.

- Confiança: cor, caixa e tempos medido; desenho das faixas observado.
