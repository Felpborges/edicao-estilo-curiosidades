# G11 · Dúvidas em aberto e pontos de baixa confiança

> Extraído do GUIA-DE-ESTILO do Estilo 03 (treino com 5 reels de referência). Onde o texto cita `still.png`, `strip.jpg` ou `clip.mp4` de uma Ref (ex.: V01-A28), nesta skill só existem `biblioteca/<ID> …/notes.md` (a medida) e `thumb.jpg` (miniatura). Onde cita "o Felipe", é o autor do método: veja `references/decisoes-do-autor.md`.

## G11 · Dúvidas para o Felipe e pontos de baixa confiança

### G11.1 Dúvidas

1. **O 3D do V05 entra no padrão ou fica como opção?** Só 1 de 5 vídeos tem 3D, mas nele o 3D ocupa 57,7 %. Os outros 4
   usam só imagem real.
   - (a) padrão;
   - (b) opção, para quando o tema não tem foto, pintura ou filme real (ex.: uma cena de 3.000 anos atrás);
   - (c) fora.

   **Adotada: (b).** Noutro pipeline ele já recusou objeto 3D "com cara de brinquedo". O projeto de reels talking head
   é isolado, então isso fica só como motivo para perguntar, não como regra.
2. **O texto grande palavra a palavra sobre o rosto (V05) entra no padrão?**
   - (a) em toda virada no rosto;
   - (b) opção;
   - (c) fora.

   **Adotada: (b).** No padrão, a virada fica no rosto só com a legenda (4 de 5 vídeos). Se entrar, ele cai no piso de
   700 ms (dúvida 4).
3. **O V02 pesa no roteiro?** É um anúncio de vagas, não uma curiosidade.
   - (a) peso cheio;
   - (b) peso só na forma (design, movimento, legenda, A-roll);
   - (c) excluir.

   **Adotada: (b).** O roteiro, a abertura, o fecho e a proporção rosto × cena vêm de V01, V03, V04 e V05.
4. **Piso de leitura.**
   - (a) os valores da 7.4 (cena ≥ 1,5 s; texto ≥ 700 ms parado; imagem de série ≥ 1,2 s; último item ≥ 700 ms);
   - (b) outros valores dele;
   - (c) a referência pura (cenas de até 1,04 s; peças de 750 ms; texto grande parado 292 ms; 7 cenas do V04 que nunca
     param).

   **Adotada: (a), provisória,** porque a regra dele ganha da referência no ritmo, como no Estilo 01. Pergunta
   ligada: **o rosto entra no piso?** A referência tem 10 planos de rosto abaixo de 1,0 s ("It isn't.", "It's not.").
   Adotada: rosto fora do piso, por ser fala e não leitura.
5. **As imagens de arquivo e de pintura são do estilo ou do tema?** Os 4 temas são históricos (roupa de mergulho,
   peruca, camuflagem, roxo).
   - (a) estilo: sempre imagem de época, mesmo em tema atual;
   - (b) tema: a imagem real certa para a frase, de qualquer época, com o mesmo tratamento (cartão, borda, sombra,
     mesa escura).

   **Adotada: (b).** Fica a regra de nunca usar ilustração genérica. Num reel sobre Claude Code, o print real ou a foto
   real vão em cartão.
6. **A cor da marcação à mão muda por vídeo?** Amarelo em V01–V03 (de #b9b04d a #f0d830), creme no V04 (#fdefd7),
   creme-claro (≈ #e3d7c9 a #e8dcd0, medido na remedição; as 1ªs notas diziam "branco"), roxo (#815685) e preto nos mapas no V05.
   - (a) sempre amarelo;
   - (b) a cor de destaque do vídeo.

   **Adotada: (a), amarelo-ouro #e0b830** (3 vídeos; casa com a legenda e o marca-texto).
7. **Pausas: 80–110 ms da referência × 30 ms da seção 6 do `CLAUDE.md`.** A fala das referências tem pausa mediana de
   80–110 ms (≥ 60 ms) e máxima de 190–320 ms com o limiar único de −40 dBFS do `SOM.md` (470 ms no V05 só com o
   limiar de −36,5 dB da análise).
   - (a) cortar com 30 ms de respiro (regra da casa, do vídeo do Joseph);
   - (b) deixar ≈ 90 ms (a referência).

   **Adotada: (b), provisória.** Pela regra-mãe, o ritmo é forma e a forma copia a referência. Com 30 ms a fala fica
   mais rápida que a do fineasjackson.
8. **Som: ninguém ouviu o áudio.** Os 5 analistas leram envelope e espectrograma. "Sem música" está medido nos 5. Os
   efeitos foram achados só onde o áudio tem canal lateral (V02: 11 trechos de papel e caneta; V05: 4 graves de
   transição). V03 e V04 são mono perfeito, e lá um efeito baixo misturado à voz passaria. Pedido: o Felipe ouvir 3
   trechos: V02 f1047–f1061 (caneta), V05 f451–f489 (antes do título) e V04 f738–f760 (explosão).
   - (a) sem efeitos;
   - (b) efeitos raros de objeto e de virada, 20–30 dB abaixo da voz.

   **Adotada: (b).**
9. **Cadência de 12 imagens/s.** Só o V01 anima as cenas a 12 imagens/s; os outros 4 andam a 24.
   - (a) 24 sempre;
   - (b) 12 nas cenas (efeito stop-motion);
   - (c) escolha por vídeo.

   **Adotada: (a).**
10. **Tamanho e altura da legenda.** V02 tem 42 px (3,3 %) e o V05 sobe para 64 % da altura. Os outros 3 ficam em
    ≈ 25 px a 67 %.

    **Adotada: 25 px a 67 %** (V01, V03, V04). Pergunta: para PT-BR no celular, 25 px não fica pequeno? O V02 sugere
    que o próprio criador já testou maior.
11. **Assinatura da série.** Os 4 reels de curiosidade dizem "This is Chasing Beauty episode N" entre 14,7 e 20 s.
    - (a) o Felipe cria uma série com nome e número;
    - (b) só "e hoje a gente vai ver X";
    - (c) nada.

    **Adotada: (a) como lacuna.** A forma é título de 2 linhas sobre o rosto; o nome é dele.
12. **Câmera viva no 3D.** Nas cenas 3D do V05 a câmera fica fixa por até 3,0 s (A36, a única confirmada
    por registro de pontos; outras 5 sem movimento visível pela dif, até 8,3 s), o que contradiz a regra "a câmera
    nunca para" dos outros 4. Se o 3D entrar (dúvida 1): **adotada, câmera fixa com o personagem agindo**, como no V05.
13. **Entrada de cartão: estalo ou corte seco limpo?** (redatores do cartão e da pilha) V01 e V03 entram com estalo de
    4 q (escala + giro no V03); V04 entra por corte seco ou deslize; V05 por deslize de borda (P09) ou lento-rápido-lento.
    - (a) estalo em toda entrada de cartão, etiqueta e disco;
    - (b) corte seco limpo;
    - (c) estalo nas peças que caem sobre a cena (pilha, etiqueta) e corte seco na troca de cena.

    **Adotada: (c), provisória.** É o que V01 e V03 fazem: a 1ª imagem da cena entra no corte e as peças seguintes
    estalam.
14. **Etiqueta de papel: modelo do V03 ou do V04?** (redator do cartão)
    - (a) V03: tira cinza-clara presa no topo do cartão, nasce no comprimento final, estalo leve, sai em fade de 6 q;
    - (b) V04: tira creme que desliza da lateral girando e cola embaixo do cartão.

    **Adotada: (a)** (5 ocorrências no V03 contra 4 no V04, e é o molde do P05).
15. **Recorte com contorno branco ou limpo?** (redator do disco e da lupa) V01 a V03 usam contorno claro (10–12 px no
    V01, 3–4 no V02, 6–10 irregular no V03); V04 e V05 usam recorte limpo com sombra suave. Junto: a lupa leva o aro
    preto interno do V01-A05 (não medido)?
    - (a) contorno sempre;
    - (b) sem contorno;
    - (c) contorno só sobre o disco creme, limpo quando o recorte fica solto na mesa.

    **Adotada: (c), provisória;** aro da lupa só claro, até medir o preto.
16. **Diagrama chapado (P18) para explicar mecanismo, e com que cores?** (redator do diagrama, `MAPA`) É o recurso mais
    usado para frase de mecanismo (9 frases), mas só existe no V01. Lá o teal marca o que vem de fora e o laranja, o
    benefício.
    - (a) padrão para toda frase de mecanismo, com teal e laranja fixos em qualquer tema;
    - (b) opção C do editor, com as cores de estado tiradas do tema;
    - (c) fora.

    **Adotada: (b).**
17. **A câmera persegue o cartão de que se fala ou só deriva?** (redator da pilha) No V03 ela viaja até o cartão
    citado; no V01 e no V04 só deriva ou dá zoom lento.
    - (a) só zoom lento contínuo;
    - (b) viagem até o cartão citado quando a fala muda de peça;
    - (c) as duas, a viagem só em pilha de 3 ou mais.

    **Adotada: (a) como padrão e (b) como opção (P11).**
18. **Empurrão, cobertura, faixa em letterbox e transformações encadeadas sem corte (quase só V04) viram padrão?**
    (redatores da câmera e da colagem) Junto: o tratamento "cara de arquivo" da faixa vale para vídeo atual, como uma
    gravação de tela?
    - (a) padrão;
    - (b) opção, para quando a fala continua o mesmo fio;
    - (c) fora.

    **Adotada: (b);** a faixa vale para qualquer vídeo real, com o mesmo tratamento (bordas esfumadas, fundo chapado).
19. **Rótulo digitado (P04, só V05) no lugar da etiqueta de papel?** (redator da legenda) E, se o texto grande (P03,
    dúvida 2) ou o rótulo entrarem, qual serifada itálica com acento em PT-BR?
    - (a) rótulo digitado como padrão;
    - (b) etiqueta de papel como padrão, rótulo como opção;
    - (c) fora.

    **Adotada: (b);** serifada a escolher com ele (alternativa livre: Source Serif Bold Italic).
20. **Sincronia do corte: um valor só ou dois?** (redator do apresentador) O corte cai −39 ms antes da 1ª palavra
    (mediana dos 5; p10 −114, p90 +17).
    - (a) −40 ms em todo corte;
    - (b) saída do rosto a −60 ms e entrada no rosto a −25 ms.

    **Adotada: (a).**
21. **Fecho no rosto ou numa cena de callback?** (redator do apresentador, `MAPA`) V01, V02 e V03 fecham no rosto;
    V04 e V05 numa cena longa em movimento. Junto: sem CTA, como as 4 curiosidades?
    - (a) callback da imagem do gancho e corte para o rosto na frase-tese final;
    - (b) callback longo sem rosto;
    - (c) rosto com CTA falado (como o V02).

    **Adotada: (a), sem CTA.**
22. **Bruto gravado com outro enquadramento: recortar para a escala-padrão?** (redator do apresentador) Molde: rosto
    com ≈ 50 % da largura, centro a ≈ 30 % da altura, olhos a 27–29 %.
    - (a) recortar sempre para o molde;
    - (b) usar como veio.

    **Adotada: (a)**, porque o enquadramento é forma.
23. **Documento: sempre fonte real? E a fonte em outra língua leva caixa de tradução (V03-A16)?** (redator da
    marcação)
    - (a) fonte real sempre, com caixa de tradução quando não estiver em PT-BR;
    - (b) fonte real sem tradução;
    - (c) documento recriado em PT-BR.

    **Adotada: (a).**
24. **Empilhar cópias iguais bem rápido (167–250 ms cada) para dizer "muito"?** (redator da colagem; ocorrência do
    V01-A43)
    - (a) opção;
    - (b) fora.

    **Adotada: (a)**, como ocorrência marcada.
25. **3D: com que ferramenta gerar personagens e cenário?** (redator do 3D) Só vale se a dúvida 1 ficar em (a) ou
    (b).
    - (a) a decidir com ele na Fase D, junto do motor de render;
    - (b) não usar 3D até haver ferramenta testada.

    **Adotada: (a).**
26. **Proporção de rosto do reel do Felipe: 14 a 21 % do tempo, como a referência?** (`MAPA`)
    - (a) sim, na faixa;
    - (b) mais rosto, porque ele é o ativo de marca.

    **Adotada: (a)**, pela regra-mãe (ritmo é forma).
27. **Corte seco ou plano contínuo nas trocas cena → cena?** (revisor do apresentador) O corte seco é minoria nas
    trocas cena → cena (13 % no V01; 43 a 45 % nos outros): o resto vem por deslize, empurrão, chicote ou peça que cai
    por cima.
    - (a) seguir a proporção da referência (maioria sem corte);
    - (b) corte seco quando a ideia muda, plano contínuo quando a fala continua o mesmo fio (`MAPA`, regra 6).

    **Adotada: (b)**, que reproduz a proporção pela fala.

### G11.2 Baixa confiança

*Revista em 2026-11-20 depois da conferência (25 animações), da remedição (179 pastas) e da passada de vazamento (209
notas).*

**O que a remedição resolveu:**
- **"Parado depois de completo" do V04:** era inferido (último passo + 6 q) e errava por mais de 2 q em 34 de 47 cenas.
  Agora está medido quadro a quadro nas notas (tabela da 7.3).
- **Tamanhos observados:** recortes, objetos, discos, lupas, marcas à mão, balões e etiquetas do V01, V03, V04 e V05
  foram medidos por borda, matiz ou registro de pontos (seções 4 e 5). Todos estavam menores que o real.
- **Durações de passos internos:** estalos (4 q, não 6), traços e marca-textos (contados do 1º pixel), digitação,
  push-ins e entradas com a câmera andando foram remedidos quadro a quadro, não mais de strip amostrado.
- **Câmera "fixa" e "parada":** recontada (seção 6). V04: 13 pastas "paradas" tinham câmera andando. V05: só a A36 é
  fixa de fato.
- **Legenda do V05:** recontada (178 blocos, até 6 palavras, tarja de 42 px).
- **Giro dos cartões:** medido, com convenção de sinal fixada (seção 5).
- **Gatilhos na palavra seguinte:** 4 corrigidos (V04-A49, V05-A21, V05-A40, V05-A45).
- **Conteúdo vazado na FORMA:** 160 de 209 notas reescritas pelo papel (784 trechos).
- **Etiquetas:** altura da tira do V03 e letra da etiqueta de data do V04 medidas (seção 3).

**O que continua de baixa confiança (declarado pelos analistas e confirmado depois):**
- **Fontes:** todas identificadas por comparação visual. Legenda e título com confiança média; etiquetas do V04 e
  serifada itálica do V05 com confiança baixa.
- **Som:** leitura de envelope e espectro, sem escuta (os 5). V03 e V04 são mono perfeito. Os nomes dos efeitos
  ("whoosh", "papel", "explosão") são leitura. A nota V05-C00 ainda diz que não há efeito de corte no canal lateral, o
  que contradiz as 3 subidas do `SOM.md`.
- **Transcrição:**
  - a transcrição adianta 1 a 3 q nos inícios de frase (conferente: V01-L03 +130 ms, V05-A13 ≈ +100 ms e mais 3);
    os gatilhos do JSON tendem a dizer "depois da palavra" quando a imagem entra junto. Foi sugerido um campo
    `gatilho_envelope_ms`; não foi criado;
  - V02 "If" ≈ 160 ms **antes** do ataque real (não atrasada, como dizia a 1ª passada); "New" e "York," não conferidos;
  - V05 "failed." ≈ 270 ms tarde;
  - V04 com nomes errados ("Criticism" = Cubism; "Cévolat" = Scévola);
  - V03 "kings" ≈ 110 ms.

  Nenhum JSON de transcrição foi corrigido.
- **Gatilhos ainda não reconferidos** com deslocamento de −250 ms ou mais (candidatos a "palavra seguinte"):
  V01-A04 (−422), V01-A13 (−293), V04-A10 (−403, cai na pausa, provavelmente certo), V04-A24 (−286), V04-A35 (−269),
  V04-A37 (−296).
- **Texto dos blocos de legenda:** atribuído pela transcrição, com ±1 palavra na borda (os 5).
- **Opacidade da tarja:** medida direto no reestudo nos 5 vídeos (74 / 50 / 73,5 / 59 / 68 %); raio dos cantos medido
  no V04 e no V05, observado nos outros.
- **Curva do marca-texto (P20):** varia por vídeo. Lento-rápido-lento ou ease-out no V02 e no V03-A16; miolo quase
  constante no V04 (A35, A40) e no V01-A42 (medido por área). A regra "nenhuma varredura é linear" só fecha para o
  traço à mão (ease-out em 19 medidas). O rolo do V04-A48 parece atravessar em velocidade constante (observado).
- **Câmera das cenas 3D A15, A19, A23, A27, A40 (V05):** medida só pela dif global, que escondeu zoom de 2 a 6 %/s em
  outras cenas do mesmo vídeo.
- **Convenção do `f_out`:** sem regra única. No chicote, a cena anterior segue visível na borda (V01-A18 até f1346,
  V01-A20 até f1444) mas a nota para antes; em V01-A02 e A03 o deslize de saída entra no `f_out`. Na cobertura e no
  empurrão o `f_out` foi marcado cedo em 4 de 25 conferidas; as outras trocas por cobertura (P09, P10, P11) não foram
  reconferidas. V05-A19 fecha em f1207, mas a cena aparece até ≈ f1211.
- **Unidade de pasta diferente por analista:**
  - V01: uma pasta para o palco + uma por peça;
  - V03: divide a cena no ponto de troca de assunto;
  - V04: nova pasta quando muda o foco.

  Isso mexe nas contagens de pasta por princípio e nos tempos em tela da 7.3. Fronteiras discutíveis: V04-A06/A07
  (talvez uma animação só), V04-A42/A43 (a aceleração do mergulho começa em f3291, dentro do A42), o pano roxo de
  V05-A30/A31, a pintura que desce e o cruzado que entra no V05-A42, a revelação por varredura do V05-A52.
- **Análises `V0X.md`:** não foram reescritas (errata no topo de cada uma). As tabelas de tempo em tela do V01 e do
  V04, a de blocos de legenda do V05 e a linha "Transições" do V04 estão velhas; vale a nota.

**O que continua sem medida (juntando os "Fora do escopo" dos 8 lotes e os "não medido" que restaram):**
- V01: aro preto grosso interno da lupa do A05; disco pequeno do A13 em f652; discos 2 e 3 do A28; giro da foto 2 do
  A16; tamanho da foto 2 do A38 (borda clara sobre fundo claro); salto do perfil em f1437 (A20, antes do chicote) que
  nenhuma nota descreve; giro extra no estalo do V01.
- V02: cor do nível empalidecido no mapa (A08) e o gatilho de "York,"; curva e duração da A02; cascata da A10.
- V03: escala inicial do recorte; letras das etiquetas; câmera em %/s nas pilhas; cartões 2 a 4 do A11 e do A17;
  curva completa do chicote A13 (só início, fim e 4 velocidades).
- V04: etiquetas do A10 (borda clara sobre fundo claro, observadas); borda clara fina do recorte do A03; rolo do A48
  (≈ 6 % da altura, observado); curva e duração do contorno do A49 e do A02; px por quadro nos pans; faixa do A46
  medida em 1 quadro.
- V05: personagens do A40 e personagens 3D em geral fora da A15 (observados); diâmetro dos círculos; linha cinza do
  A49; margens do A21; sombra do texto grande; linha de apoio do A49; digitação de A31, A33 e A43 (pode estar 1 a 3 q
  curta); `still.png` do A34 que não bate com o `f_chave` (parece ≈ f2424, não f2432).
- Todos: borrão nos pans e deslizes (só ausência de registro); escurecimento do fundo na entrada dos cartões que caem
  (P09); fim real das trocas por cobertura em V01-A45 e V05-A20; efeitos sonoros baixos por baixo da voz nos vídeos
  mono; tempo parado dos títulos da série (V01-A10, V03-A06) depois da última palavra; tempo de cada peça nas pilhas
  do V03; recontagem de eventos visuais com critério único.

**Contradições que restaram:**
1. **Tamanho e posição da legenda** (V02 e V05 × os outros).
   - V02: 42 px, tarja de 76 px de y830 a y905, contra 42–47 px nos outros.
   - V05: o topo do texto está em y821 (64,1 %, recalculado e confirmado na remedição), e não perto de 67 %; centro
     da tarja a 65,2 %.

   Conferido por `caixa` em 2 quadros por vídeo, numa folha de 1 quadro e na remedição: **é diferença real, não erro**.
2. **Cantos e opacidade da tarja** (diferença real entre vídeos, medida no reestudo). V01 74 %; V02 50 %; V03 73,5 %; V04
   59 %; V05 68 %. Não há molde médio: vale a do perfil escolhido (seção 12.2).
3. **Palavras por bloco no V03.** A análise e a nota V03-L01 dizem "mediana 3 palavras (1–5)"; a tabela a.3 (229
   blocos) dá **mediana 2, média 2,5**.
4. **Sincronia da legenda** (V05 × V02). V05 entra **58 ms antes** da 1ª palavra (recalculado sobre a recontagem; a
   nota ainda traz −96 ms sobre os 167 blocos antigos). V02 entra **50 ms depois**. V01, V03 e V04 ficam entre 0 e
   +12 ms. Molde: 0 ms.
5. **Cadência de 12 imagens/s** (V01 × V02–V05). O V01 anima a cena inteira a 12; V02 a V05 andam a 24, mas os
   estalos, pops e assentamentos andam de 2 em 2 q em todos (seção 6). Não é erro de medida: é diferença entre vídeos.
6. **Estalo de entrada** (V01, V03 × V04, V05). V01: 4 q, ≈ 110 → 103 → 100 %. V03: ×1,11–1,14 com giro, 4 q. V04
   entra por deslize ou corte sem estalo. V05 entra lento-rápido-lento. O estalo é regra em 2 vídeos, não em 5 (dúvida
   13).
7. **Luz e vinheta** (diferença real entre vídeos, medida no reestudo). V01: poça de luz fixa. V02: 3 fundos, sem vinheta
   por cima. V03: luz central elíptica. V04: poça de luz por cena, por cima das peças. V05: vinheta só nas cenas. Não há
   molde no meio: vale a do perfil escolhido (seção 12.2).
8. **Câmera viva** (V01–V04 × 3D do V05). "A câmera quase nunca para" vale para os 4, para as cenas 2D do V05, para
   as 8 do P23 e para 8 das 14 do P24. Só a A36 está confirmada fixa (3,0 s).
9. **Critério de evento visual** (seção c de cada vídeo). Cada analista contou de um jeito (tabela 7.1). Os eventos por
   10 s **não são comparáveis** entre vídeos sem recontar com um critério só. A conta que dá para comparar é a de
   cortes por 10 s (2,1–2,6). O mesmo vale para a sincronia antiga da 7.1 (o V03 contava passos internos).
10. **Peso do título da série** (V01 × V03). V01: "regular". V03: "seminegrito". Mesma família, Open Sans. Molde:
    SemiBold.
11. **Rosto no V01** (dentro da própria análise). "31,2 s (19,6 %)" de rosto puro e "32,7 s (20,6 %)" nas 8 camadas;
    a 2ª conta inclui o plano com o título. Não é erro, mas os dois números aparecem sem aviso.
12. **Curva do marca-texto** (V02 × V01, V04): lento-rápido-lento num, quase constante nos outros (acima).
13. **"Parado" com dois critérios no V04:** o lote V04-a mediu "elemento parado" (A30 0,13 s porque a câmera
    reenquadra); o V04-b aceitou "sem nova entrada, câmera seguindo" (A28 2,5 s com afastamento de −4,7 %/s). A 7.3 usa
    os valores como estão nas notas.
14. **Notas × remedição por 1 q:** texto grande do V05 (notas de A35, A41, A50 com 1 q a mais de parado), V04-A35 (13 ×
    12 q), V04-A14 e A37 (13 × 14 q, 10 × 11 q), saída do V03-A27 (8 × ≈ 11 q). A 7.3 usa a remedição.
15. **Frases velhas nas notas:** V01-A44 "nenhum trecho parado" × 1500 ms na tabela do analista; V01-A41 "estado final
    1 s" × ≈ 750 ms pelos quadros; V04-A50 "≈ 13 quadros"; V04-A40 com a contagem antiga de amarelo; V05-A51 gatilho
    f3557 × f3553 no Movimento; V01-A38 "à direita" (o still mostra centrada).
16. **Cor da marcação no V05:** a dúvida 6 da 11.1 fala em "branco"; o medido é creme-claro (#e8dcd0, #e3d7c9) com o
    quadro em sépia.
17. **Sombra do disco** (V01 tem, com fio escuro de 1–2 px; no V03 a sombra é multiplicativa e some sobre a mesa: reestudo) e **ordem dos anéis da lupa** (A05 claro por fora, A30 preto por fora);
    centro do disco no V03 (29,7 a 33,5 %, por blob) abaixo da faixa do V01.

---
