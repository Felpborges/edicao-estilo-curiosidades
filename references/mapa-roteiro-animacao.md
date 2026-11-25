# MAPA-ROTEIRO-ANIMACAO · Estilo 03 Curiosidades

*Criado em 2026-11-20 · amostra: 5 reels de @fineasjackson (V01 a V05), 259 frases, 192 pastas de animação (A), 25 princípios (P01 a P25). Fontes: `transcricoes/V0X.json`, `analises/V0X.md` (a) e (b), `analises/V0X-eventos.json`, `analises/principios.json`, `biblioteca/*/notes.md` (Regra de escolha). Contagens feitas por script sobre os JSON; o tipo de fala é leitura minha (ver seção 10).*

---

## 1 · Como ler este mapa

- **Unidade = frase.** Cada frase da transcrição (até ponto, ? ou !) é uma linha. Quando a edição corta para o rosto no meio da frase, a frase foi dividida no corte, porque a edição trata cada pedaço como um beat (15 divisões; ex.: V03 #15 e #16, "…comece por uma careca, | uma careca real."). Uma divisão de 1 palavra foi juntada de volta (V03 "And").
- **Na tela** é medido (quadros dos `eventos.json` e das tabelas de planos): `rosto` = A-roll puro com legenda; `rosto + Axx Pxx` = texto sobre o rosto; `entra Axx Pxx` = pasta cuja palavra-gatilho cai nesta frase; `segue Axx Pxx` = pasta que já estava e cobre 50 % ou mais da frase; `→ corta para` = a cena entra na última palavra de uma frase de rosto.
- **P01 (legenda amarela) e P25 (corte seco, plano único)** estão em todas as frases e não entram nas contagens por tipo.
- **"4 curiosidades"** = V01, V03, V04 e V05 (237 frases). **V02** é anúncio de vagas do criador (22 frases): aparece nas tabelas, mas fica fora das regras de roteiro; quando entra numa contagem, está marcado.
- **Força da amostra:** **regra** = 3 vídeos ou mais · **regra em 2 vídeos** · **regra em 1 vídeo** = 2 vezes ou mais num só vídeo · **ocorrência** = 1 vez.
- Número de frase: `V03 #29` = frase 29 da tabela do V03 (seção 2). Número de pasta: `V03-A12`.

### Nomes curtos dos princípios

| P | nome | vídeos | | P | nome | vídeos |
|---|---|---|---|---|---|---|
| P01 | legenda amarela em tarja | 5 | | P14 | disco creme com recorte | V01 V03 |
| P02 | título sobre o rosto | V01 V03 V04 | | P15 | lupa e janela circular | V01 V02 V04 |
| P03 | texto grande sobre o rosto | V05 | | P16 | colagem de recortes | V01 V02 V04 V05 |
| P04 | rótulo e número digitados | V05 | | P17 | objeto que se transforma | V04 V05 |
| P05 | etiqueta de papel (ano, nome) | V03 V04 | | P18 | diagrama chapado com estados | V01 |
| P06 | imagem em cartão, câmera viva | V01 V03 V04 V05 | | P19 | marcação e desenho à mão | V01 V02 V03 V04 |
| P07 | imagem em tela cheia em deriva | V03 V05 | | P20 | documento com marca-texto | 5 |
| P08 | pilha de cartões | V01 V03 V04 | | P21 | linha do tempo e dado em papel | V01 V02 |
| P09 | cartão que cai por cima | V01 V05 | | P22 | mapa com marcação | V02 V05 |
| P10 | troca por empurrão ou cobertura | V03 V04 | | P23 | 3D com cor seletiva | V05 |
| P11 | viagem de câmera entre peças | V01 V03 V04 V05 | | P24 | cena 3D narrativa | V05 |
| P12 | faixa de b-roll em letterbox | V04 | | P25 | corte seco, plano único | 5 |
| P13 | afastamento que revela quantidade | V03 V04 V05 | | | | |

### Tipos de fala (22)

Parti da lista do briefing. **Criei** `crença comum`, `contexto` e `ação narrada` (apareceram muito e puxam cenas diferentes). **Fundi** "opinião ou comentário" com as frases-ponte em `comentário ou ponte`; "fato histórico com data" virou `fato com data` e inclui marcos sem ano ("na Primeira Guerra", "décadas depois"); "descrição de objeto" absorve o batismo ("isso se chamava X"); "exemplo" absorve a prova.

| código | tipo | definição (1 linha) | exemplo inventado (outro tema: a lâmpada) |
|---|---|---|---|
| GO | gancho com objeto | o apresentador aponta o objeto do tema ou dá um comando ao espectador | "Olha esta lâmpada." |
| PE | pergunta | pergunta-tese, pergunta retórica ou crença em forma de pergunta ("…, né?") | "Então por que ela não esquenta?" |
| AN | anúncio | diz o que vem sem dar o dado: série, "hoje o assunto é X", abertura de capítulo, "e ele disse:" | "A resposta veio de uma fábrica de vidro." |
| CR | crença comum | o que todo mundo diz ou acha, antes de ser desmentido | "Pergunte a um eletricista e ele vai dizer isto." |
| CT | contexto | como as coisas eram, sem ação nem data nova | "Antes, toda casa usava vela." |
| DO | descrição de objeto | aparência, material, partes ou nome de uma coisa | "Fina, de vidro, com um fio em espiral." |
| ME | mecanismo | como funciona, etapas de um processo, causa física | "A corrente aquece o fio até ele brilhar." |
| NA | ação narrada | fato da história contado como ação de alguém, sem data nova | "Ele trancou o laboratório e testou mil fios." |
| DA | fato com data | fato que abre com ano ou marco de tempo | "Em 1879, o fio durou 13 horas." |
| PS | pessoa | apresenta alguém: nome, cargo, quem era | "Este é o inventor, um telegrafista de 30 anos." |
| LU | lugar | a frase gira em torno de um lugar | "Tudo aconteceu num galpão perto do porto." |
| NU | número | o dado central é uma quantidade | "Foram mais de 6.000 materiais testados." |
| LI | lista | três itens ou mais em sequência | "Bambu, platina, linha de algodão." |
| CO | comparação | X como Y, X mais que Y, metáfora | "Brilhava como dez velas juntas." |
| CI | citação | cita fonte, documento ou fala de alguém | "O jornal escreveu: 'uma luz sem chama'." |
| VI | negação ou virada | "não é", "mas…", "até que…": desmentido ou mudança de rumo | "Mas não foi ele quem inventou." |
| EX | exemplo ou prova | caso concreto que prova o que foi dito | "Uma delas está acesa até hoje num quartel." |
| CQ | consequência | o efeito do que veio antes ("então", "por isso") | "Por isso o vidro precisa de vácuo." |
| OP | comentário ou ponte | frase de opinião ou de passagem, sem dado novo para mostrar | "Ele sabia que isso não bastava." |
| PI | piada | trocadilho ou remate cômico | "Ideia brilhante. Literalmente." |
| CL | conclusão | fecha um trecho ou o vídeo | "A lâmpada nunca foi sobre a luz." |
| CTA | CTA | pedido ao público | "Comenta qual objeto eu explico depois." |

---

## 2 · Todas as frases, por vídeo

Resumo em português, sem citar a referência como regra (nomes próprios trocados por papéis quando não importam). Tempos em s.

### V01 · roupa de mergulho (57 frases · 16 no rosto)

| # | tempo (s) | fala (resumo) | tipo | na tela |
|---|---|---|---|---|
| 1 | 0,03–0,76 | Olha esta roupa de mergulho. | gancho com objeto | rosto → corta para A01 P14 na última palavra |
| 2 | 0,92–2,06 | Ela não é à prova d'água. | negação ou virada | segue A01 P14 |
| 3 | 2,34–5,10 | Ao pular, a água fria entra na roupa. | mecanismo | entra A02 P06, A03 P14 |
| 4 | 5,38–8,14 | Pelo pescoço, pelas mangas, contra a pele. | lista | entra A04 P11, A05 P15 · segue A03 P14 |
| 5 | 8,33–12,20 | Mesmo assim surfistas ficam horas na água gelada. | exemplo ou prova | entra A06 P06, A07 P08 |
| 6 | 12,56–15,56 | Como uma roupa que deixa a água entrar aquece? | pergunta | entra A08 P06, A09 P18 |
| 7 | 15,74–17,38 | Este é o episódio 93 da série | anúncio | rosto + A10 P02 |
| 8 | 17,38–19,32 | e hoje o assunto é a roupa de mergulho. | anúncio | entra A11 P14 |
| 9 | 19,54–22,64 | Antes dela, a ideia era ficar seco. | contexto | rosto |
| 10 | 22,91–28,84 | No início dos anos 1950, borracha por fora, lã por dentro. | fato com data | entra A12 P08, A13 P14 |
| 11 | 29,24–32,22 | A lã aquecia e a borracha barrava a água. | mecanismo | entra A14 P18 |
| 12 | 32,43–33,52 | Até que deixou de funcionar. | negação ou virada | rosto |
| 13 | 33,69–37,26 | Se a água entrava, a lã encharcava e parava. | consequência | entra A15 P18 |
| 14 | 37,46–39,24 | Então os mergulhadores tentaram de tudo. | anúncio | rosto |
| 15 | 39,44–41,99 | Ceroulas, macacões de sobrevivência da aviação. | lista | entra A16 P08 |
| 16 | 42,30–43,88 | Alguns só passavam graxa na pele. | lista | segue A16 P08 |
| 17 | 44,10–45,46 | E a Marinha estava pior. | negação ou virada | rosto |
| 18 | 45,77–48,66 | Os mergulhadores dela ficavam horas na água fria. | contexto | entra A17 P08 |
| 19 | 49,02–50,82 | E ficar seco não funcionava. | consequência | segue A17 P08 |
| 20 | 51,04–53,12 | A resposta veio de um físico nuclear. | anúncio | rosto |
| 21 | 53,43–55,56 | Ele ajudou a construir a bomba atômica. | pessoa | entra A18 P14 |
| 22 | 55,78–59,46 | Em 1943, recrutado para um laboratório secreto. | fato com data | entra A25 P21, A19 P11, A20 P21 |
| 23 | 59,83–63,50 | Em 1945, assistiu ao primeiro teste atômico. | fato com data | entra A21 P11, A22 P21 · segue A25 P21 |
| 24 | 63,80–66,28 | Em 1951, era físico numa universidade. | fato com data | entra A23 P11, A24 P21 · segue A25 P21 |
| 25 | 66,54–69,50 | Nos fins de semana, atacou o problema dos mergulhadores. | comentário ou ponte | rosto |
| 26 | 69,73–74,12 | Em 21 de junho de 1951, anotou a ideia. | fato com data | entra A26 P06, A27 P19 |
| 27 | 74,39–76,88 | O mergulhador não precisa estar seco para se aquecer. | mecanismo | segue A27 P19 |
| 28 | 77,12–80,48 | Pergunte a um surfista e você vai ouvir isto. | crença comum | entra A28 P14 |
| 29 | 80,62–82,54 | Uma camada fina de água fica presa. | mecanismo | entra A29 P18, A30 P15 |
| 30 | 82,80–85,36 | O corpo aquece essa água e ela aquece você. | mecanismo | segue A29 P18, A30 P15 |
| 31 | 85,69–87,84 | Mas a água é péssima para aquecer. | negação ou virada | rosto |
| 32 | 88,04–91,45 | Ela tira calor 25 vezes mais rápido que o ar. | comparação | entra A31 P18 |
| 33 | 91,59–93,50 | Ele sabia que a água não ajudava. | comentário ou ponte | rosto |
| 34 | 93,70–95,36 | O calor vem do material. | mecanismo | entra A32 P08 |
| 35 | 95,56–99,66 | Neoprene de espuma, cheio de bolhas de gás. | descrição de objeto | entra A33 P15, A34 P18 · segue A32 P08 |
| 36 | 99,84–101,48 | Cada bolha isolada da vizinha. | mecanismo | segue A34 P18 |
| 37 | 101,79–103,64 | A água não entra numa bolha fechada. | mecanismo | segue A34 P18 |
| 38 | 103,84–106,31 | Então, mesmo encharcada, a espuma isola. | consequência | entra A35 P09, A36 P18 |
| 39 | 106,60–107,98 | Sobra uma única função para a roupa. | anúncio | rosto |
| 40 | 108,25–110,10 | Deixar entrar o mínimo de água. | mecanismo | entra A37 P18 |
| 41 | 110,32–112,96 | E impedir que ela seja trocada por água nova. | mecanismo | segue A37 P18 |
| 42 | 113,12–115,52 | Por isso a roupa tem que ser justa. | consequência | entra A38 P09 · segue A37 P18 |
| 43 | 115,75–117,66 | Um pouco de água na pele não faz mal. | mecanismo | segue A37 P18 |
| 44 | 117,90–120,80 | A água nova a cada movimento é que gela. | mecanismo | entra A39 P09 · segue A37 P18 |
| 45 | 121,02–123,44 | Ele testou as primeiras roupas naquele outono. | ação narrada | rosto |
| 46 | 123,65–126,44 | Em 1953, fez uma até para a filha. | fato com data | entra A40 P08 |
| 47 | 126,73–128,60 | Então a Marinha adorou, né? | pergunta | segue A40 P08 |
| 48 | 128,98–129,72 | Nem tanto. | negação ou virada | rosto |
| 49 | 129,90–133,53 | Temiam que as bolhas aparecessem no sonar. | mecanismo | entra A41 P16 |
| 50 | 133,74–135,51 | E engavetou a ideia por anos. | negação ou virada | rosto |
| 51 | 135,84–142,50 | Em 1957, devolveu a roupa com uma carta de recusa. | citação | entra A42 P20 |
| 52 | 142,71–145,56 | Mas ele já podia vender ao público. | negação ou virada | rosto |
| 53 | 145,79–147,34 | Mas ele não quis o dinheiro. | negação ou virada | entra A43 P16 |
| 54 | 147,50–150,37 | Colegas abriram uma empresa para fabricar. | ação narrada | entra A44 P20 |
| 55 | 150,62–152,96 | E ele garantiu que o lucro não fosse para ele. | ação narrada | segue A44 P20 |
| 56 | 153,17–156,04 | A roupa não aquece barrando a água. | conclusão | entra A45 P09, A46 P14 |
| 57 | 156,22–158,40 | Funciona porque nunca tentou. | conclusão | rosto |

### V02 · anúncio de vagas, conta à parte (22 frases · 6 no rosto)

| # | tempo (s) | fala (resumo) | tipo | na tela |
|---|---|---|---|---|
| 1 | 0,02–0,64 | Em menos de um ano, | número | rosto |
| 2 | 0,76–3,58 | cheguei a um milhão de seguidores. | número | entra A01 P21 |
| 3 | 3,71–5,52 | e agora preciso da sua ajuda. | anúncio | rosto |
| 4 | 5,60–7,89 | Faço duas séries (dois nomes próprios). | lista | entra A02 P15 |
| 5 | 7,99–10,96 | Vou ampliar as duas e abrir um canal novo. | anúncio | entra A03 P19 |
| 6 | 11,13–13,48 | Por isso estou contratando roteiristas e editores. | anúncio | entra A04 P20 |
| 7 | 13,70–19,62 | Já fiz vídeos de quatro temas diferentes. | lista | entra A05 P15, A06 P15 |
| 8 | 19,98–21,76 | Cada vídeo é um tema novo. | conclusão | segue A06 P15 |
| 9 | 21,99–23,54 | Não procuro especialistas. | negação ou virada | rosto |
| 10 | 23,94–28,01 | Procuro quem aprende rápido toda semana. | descrição de objeto | entra A07 P20 |
| 11 | 28,20–29,54 | De preferência no país X. | lugar | entra A08 P22 |
| 12 | 29,54–31,60 | Na cidade Y, melhor ainda. | lugar | segue A08 P22 |
| 13 | 31,74–34,84 | Pagamento: porcentagem da receita de cada vídeo. | número | entra A09 P16 |
| 14 | 34,98–37,09 | Receita de anúncio e de publicidade. | lista | segue A09 P16 |
| 15 | 37,29–39,64 | Se o canal cresce, seu ganho cresce. | consequência | segue A09 P16 |
| 16 | 39,92–41,26 | Agora, como se candidatar. | anúncio | rosto |
| 17 | 41,43–42,82 | Quero ver o seu trabalho. | CTA | entra A10 P20 |
| 18 | 43,04–47,54 | Roteirista: escreva as primeiras 250 palavras. | CTA | segue A10 P20 |
| 19 | 47,80–50,52 | Editor: mande uma edição de até um minuto. | CTA | entra A11 P21 |
| 20 | 50,59–52,76 | Se você gosta dos vídeos, quero trabalhar com você. | CTA | rosto → corta para A12 P20 na última palavra |
| 21 | 53,09–54,06 | Mostre do que é capaz. | CTA | segue A12 P20 |
| 22 | 54,18–55,66 | O link está na bio. | CTA | rosto |

### V03 · peruca (73 frases · 21 no rosto)

| # | tempo (s) | fala (resumo) | tipo | na tela |
|---|---|---|---|---|
| 1 | 0,02–0,80 | Olha este cabelo, | gancho com objeto | rosto |
| 2 | 0,98–4,62 | longo, cacheado, alto, caindo nos ombros. | descrição de objeto | entra A01 P06, A02 P07 |
| 3 | 4,89–5,88 | Não é dele. | negação ou virada | rosto |
| 4 | 6,13–10,02 | Este é o rei X, usando cabelo de outra pessoa. | pessoa | entra A03 P05 |
| 5 | 10,17–13,62 | Por cem anos, os homens mais poderosos fizeram igual. | exemplo ou prova | segue A03 P05 |
| 6 | 13,79–16,62 | Homens de cabelo bom cortavam para a peruca caber. | ação narrada | entra A04 P14 |
| 7 | 16,74–19,20 | Por que queriam tanto cabelo falso? | pergunta | entra A05 P07 |
| 8 | 19,40–21,16 | Este é o episódio 95 da série, | anúncio | rosto + A06 P02 |
| 9 | 21,16–23,32 | e hoje o assunto é a peruca. | anúncio | entra A07 P14 |
| 10 | 23,51–26,44 | Pergunte por quê e você ouve uma palavra: | crença comum | segue A07 P14 |
| 11 | 26,72–27,28 | a doença (a resposta comum). | crença comum | rosto |
| 12 | 27,40–29,80 | A doença faz o cabelo cair em falhas. | mecanismo | entra A08 P08 |
| 13 | 29,80–32,16 | E alguns escondiam isso com peruca. | comentário ou ponte | rosto |
| 14 | 32,32–34,85 | Mas doença não explica os homens saudáveis. | negação ou virada | entra A09 P08 |
| 15 | 35,08–36,90 | Para isso, comece por uma careca, | anúncio | segue A09 P08 |
| 16 | 37,09–38,03 | uma careca real. | negação ou virada | rosto |
| 17 | 38,21–41,84 | Em 1624, o rei começou a ficar careca. | fato com data | entra A10 P05 |
| 18 | 42,03–42,80 | Ele tinha 23 anos. | número | rosto |
| 19 | 43,12–45,92 | Cobriu com peruca e a corte copiou. | ação narrada | entra A11 P08 |
| 20 | 46,06–49,38 | No começo, peruca era esconder insegurança. | conclusão | segue A11 P08 |
| 21 | 49,65–52,52 | O filho dele tinha cabelo grosso, | pessoa | segue A11 P08 |
| 22 | 52,63–54,32 | até começar a cair também. | negação ou virada | rosto |
| 23 | 54,53–56,22 | Então o filho foi pelo caminho oposto. | negação ou virada | entra A12 P07 |
| 24 | 56,35–57,74 | Fez perucas enormes. | ação narrada | segue A12 P07 |
| 25 | 58,08–59,54 | É a peruca deste retrato. | exemplo ou prova | segue A12 P07 |
| 26 | 59,80–61,26 | Uma coroa feita de cabelo. | comparação | segue A12 P07 |
| 27 | 61,43–63,76 | A moda atravessou para outro país com outro rei. | lugar | entra A13 P11, A14 P05 |
| 28 | 64,07–68,14 | Em 1663, grisalho, adotou peruca preta. | fato com data | segue A14 P05 |
| 29 | 68,36–69,64 | De quem era o cabelo? | pergunta | rosto |
| 30 | 69,74–72,44 | A enciclopédia dizia: o melhor vinha das camponesas. | citação | entra A15 P10 |
| 31 | 72,66–74,02 | De preferência as que bebiam cerveja. | citação | entra A16 P20 |
| 32 | 74,24–76,63 | A cerveja, dizia, nutria o cabelo. | citação | segue A16 P20 |
| 33 | 76,74–78,30 | Alguns temiam que viesse de mortos. | crença comum | rosto |
| 34 | 78,54–84,78 | Em 1665, na peste, um funcionário não ousava usar a peruca. | fato com data | entra A17 P08 |
| 35 | 84,78–88,36 | Vai que o cabelo viesse de mortos da peste. | consequência | segue A17 P08 |
| 36 | 88,64–91,52 | Mas logo a peruca não pareceria cabelo de ninguém. | negação ou virada | rosto |
| 37 | 91,69–93,92 | O rei usava peruca preta para esconder o grisalho. | ação narrada | entra A18 P08 |
| 38 | 94,12–97,32 | Décadas depois, o cabelo da moda era branco. | fato com data | segue A18 P08 |
| 39 | 97,47–99,82 | Como deixar o cabelo de uma cor que não existe? | pergunta | rosto |
| 40 | 99,94–101,28 | Você não precisava de cabelo branco. | negação ou virada | entra A19 P14 |
| 41 | 101,50–102,42 | Precisava de pó. | mecanismo | segue A19 P14 |
| 42 | 102,68–104,16 | Primeiro, o cabelo era engordurado. | mecanismo | segue A19 P14 |
| 43 | 104,44–105,84 | Depois, polvilhado com amido. | mecanismo | segue A19 P14 |
| 44 | 106,07–107,12 | Geralmente de trigo. | mecanismo | segue A19 P14 |
| 45 | 107,32–109,14 | Casas grandes tinham uma sala só para isso. | lugar | entra A20 P14 |
| 46 | 109,34–110,58 | Você enfiava a cabeça numa cortina, | mecanismo | segue A20 P14 |
| 47 | 110,74–113,72 | de máscara, e o criado branqueava o cabelo. | mecanismo | entra A21 P08 |
| 48 | 113,89–117,24 | Cabelo branco dizia: tempo, criados e trigo de sobra. | lista | segue A21 P08 |
| 49 | 117,41–119,13 | Mas símbolo de status tem um problema. | negação ou virada | rosto |
| 50 | 119,37–120,72 | Todo mundo quer copiar. | comentário ou ponte | entra A22 P08 |
| 51 | 120,83–123,37 | Ficaram baratas e desceram de reis a advogados. | lista | segue A22 P08 |
| 52 | 123,38–127,08 | Depois a escriturários, balconistas, criados, cozinheiros. | lista | segue A22 P08 |
| 53 | 127,54–130,86 | Se o cozinheiro tem o mesmo cabelo, perde o sentido. | consequência | rosto |
| 54 | 131,05–134,54 | Nos anos 1760, os elegantes fizeram algo radical. | fato com data | entra A23 P05 |
| 55 | 134,89–136,24 | Usaram o próprio cabelo. | negação ou virada | rosto |
| 56 | 136,36–137,78 | Mas mantiveram o pó. | negação ou virada | entra A24 P07 |
| 57 | 137,99–138,98 | Este é um presidente famoso. | pessoa | entra A25 P05 |
| 58 | 139,16–140,66 | Todo mundo acha que é peruca. | crença comum | segue A25 P05 |
| 59 | 140,79–141,26 | Não é. | negação ou virada | rosto |
| 60 | 141,33–144,36 | É o cabelo dele, longo, preso e empoado. | descrição de objeto | entra A26 P07 |
| 61 | 144,60–146,34 | Mas o pó virou política. | negação ou virada | rosto |
| 62 | 146,55–149,68 | Em 1795, o país precisava de dinheiro para a guerra. | fato com data | entra A27 P08 |
| 63 | 149,68–151,22 | Então taxou o pó de cabelo. | consequência | segue A27 P08 |
| 64 | 151,37–152,32 | Uma moeda por ano. | número | segue A27 P08 |
| 65 | 152,38–156,53 | Quem pagava ganhou um apelido de trocadilho. | piada | segue A27 P08 |
| 66 | 156,75–159,53 | Em 1855, menos de mil pessoas pagavam. | número | entra A28 P13 |
| 67 | 159,69–161,06 | Quase todos eram criados. | negação ou virada | rosto |
| 68 | 161,40–161,68 | Por quê? | pergunta | rosto |
| 69 | 161,90–164,56 | Um criado empoado dizia algo sobre o patrão: | mecanismo | entra A29 P07 |
| 70 | 164,78–166,08 | que a casa tinha dinheiro. | conclusão | rosto |
| 71 | 166,22–168,08 | A peruca nasceu para esconder a careca, | conclusão | entra A30 P06 |
| 72 | 168,24–169,34 | virou coroa, | conclusão | entra A31 P19 |
| 73 | 169,58–171,49 | e se espalhou até o cozinheiro ter uma. | conclusão | rosto |

### V04 · camuflagem (54 frases · 13 no rosto)

| # | tempo (s) | fala (resumo) | tipo | na tela |
|---|---|---|---|---|
| 1 | 0,08–0,96 | Olha estas calças, | gancho com objeto | rosto + A01 P02 |
| 2 | 1,27–4,14 | verde, marrom e preto, manchas de borda dura. | descrição de objeto | entra A02 P16 |
| 3 | 4,53–6,30 | Não parecem folha nem casca. | comparação | segue A02 P16 |
| 4 | 6,52–11,54 | Nada na mata é assim, mas lá elas escondem você. | comparação | entra A03 P16, A04 P12 |
| 5 | 11,73–14,56 | Como um padrão que parece nada esconde? | pergunta | segue A04 P12 |
| 6 | 14,76–18,68 | Episódio 97; hoje o assunto é camuflagem. | anúncio | rosto |
| 7 | 19,13–21,74 | A história começa no céu. | anúncio | entra A05 P12 |
| 8 | 21,96–24,96 | Na Primeira Guerra, um problema novo: o avião. | fato com data | entra A06 P16 |
| 9 | 25,22–28,56 | O inimigo podia olhar de cima para você. | mecanismo | entra A07 P15, A08 P19 · segue A06 P16 |
| 10 | 28,58–33,05 | Se achassem o canhão, a artilharia o destruía. | consequência | segue A08 P19 |
| 11 | 33,23–38,54 | Em 1914, um artilheiro chamado X | pessoa | entra A09 P05, A10 P05 |
| 12 | 38,54–39,58 | teve uma ideia. | negação ou virada | rosto |
| 13 | 39,85–44,14 | Antes da guerra, ele pintava quadros em tons pastel. | pessoa | entra A11 P11 |
| 14 | 44,44–47,26 | Escondeu um canhão sob uma lona pintada. | ação narrada | entra A12 P16 |
| 15 | 47,44–51,14 | Em 1915, o exército criou a primeira unidade. | fato com data | entra A13 P05, A14 P10 |
| 16 | 51,35–56,98 | No fim do ano, ele comandava e chamou artistas. | ação narrada | entra A15 P06, A16 P10, A17 P10 |
| 17 | 57,39–59,58 | Aquele movimento era a arte mais estranha da cidade. | comentário ou ponte | rosto |
| 18 | 59,96–66,58 | Pintores quebravam um rosto ou violão em pedaços. | exemplo ou prova | entra A18 P08, A19 P17 |
| 19 | 66,93–68,76 | Muita gente dizia que aquilo parecia nada, | crença comum | entra A20 P20 |
| 20 | 69,02–70,92 | mas era o que o exército precisava. | negação ou virada | rosto |
| 21 | 71,04–73,34 | Então camuflagem deve parecer folha, né? | pergunta | entra A21 P16 |
| 22 | 73,59–74,00 | Não. | negação ou virada | rosto |
| 23 | 74,20–76,66 | O olho não acha a arma pela cor. | mecanismo | entra A22 P12 |
| 24 | 76,90–78,30 | Acha pelo contorno. | mecanismo | entra A23 P17 |
| 25 | 78,54–82,98 | Pintado de verde, do alto ainda é um canhão. | exemplo ou prova | entra A24 P13 · segue A23 P17 |
| 26 | 83,13–83,84 | Só que verde. | piada | rosto |
| 27 | 84,05–89,28 | Manchas que cruzam a borda quebram a forma. | mecanismo | entra A25 P17, A26 P13 |
| 28 | 89,46–90,29 | O olho vê pedaços. | consequência | segue A26 P13 |
| 29 | 90,65–92,07 | O pintor famoso entendeu na hora. | comentário ou ponte | rosto |
| 30 | 92,32–96,24 | Em 1915, escreveu a um amigo com um conselho. | fato com data | entra A27 P05, A28 P08 |
| 31 | 96,67–99,67 | Pinte os canhões de amarelo, verde, azul e branco. | citação | entra A29 P17 |
| 32 | 99,82–100,57 | Como um arlequim. | comparação | entra A30 P08 |
| 33 | 100,79–103,86 | Andava pela cidade com uma escritora. | ação narrada | entra A31 P10, A32 P08 |
| 34 | 103,86–108,46 | Passou um canhão camuflado, o primeiro que viram. | ação narrada | entra A33 P16 |
| 35 | 108,63–110,10 | Ele parou e ficou olhando. | ação narrada | entra A34 P06 |
| 36 | 110,34–111,38 | Então ele disse: | anúncio | rosto |
| 37 | 111,38–112,06 | "Nós fizemos isso." | citação | entra A35 P20 |
| 38 | 112,23–113,00 | Ele tinha razão? | pergunta | segue A35 P20 |
| 39 | 113,30–114,84 | Ele nunca pintou um canhão. | negação ou virada | rosto |
| 40 | 115,09–117,30 | Mas o chefe da unidade disse quase o mesmo. | negação ou virada | entra A36 P06 |
| 41 | 117,58–123,24 | O chefe disse que usava os métodos daqueles pintores. | citação | entra A37 P10, A38 P10 |
| 42 | 123,44–125,50 | Logo os pintores escondiam tudo. | exemplo ou prova | entra A39 P08 |
| 43 | 125,68–127,66 | No mar, não dá para esconder um navio. | negação ou virada | rosto |
| 44 | 127,83–131,30 | Em 1917, um pintor chamado Y | pessoa | entra A40 P20 |
| 45 | 131,30–132,26 | desistiu de esconder. | negação ou virada | rosto |
| 46 | 132,26–134,95 | Cobriu os navios de listras e zigue-zagues. | ação narrada | entra A41 P17 |
| 47 | 135,34–140,58 | O comandante no periscópio não sabia a direção. | mecanismo | entra A42 P15, A43 P15, A44 P13 |
| 48 | 140,97–143,48 | Mais de 4.000 navios foram pintados assim. | número | entra A45 P13 |
| 49 | 143,67–144,97 | Isso se chamava Dazzle. | descrição de objeto | entra A46 P12 |
| 50 | 145,17–147,09 | Mas tudo isso era só em canhões e navios. | negação ou virada | rosto |
| 51 | 147,50–149,42 | A maioria dos soldados usava uniforme liso. | contexto | entra A47 P06 |
| 52 | 149,79–152,58 | Levou mais de 10 anos para imprimir em tecido. | número | entra A48 P17 |
| 53 | 152,96–158,03 | Um dos primeiros padrões, de 1931, tinha nome. | fato com data | entra A49 P19 · segue A48 P17 |
| 54 | 158,11–160,38 | Parece saído de uma pintura daquele movimento. | conclusão | entra A50 P17 |

### V05 · roxo de Tiro (53 frases · 12 no rosto)

| # | tempo (s) | fala (resumo) | tipo | na tela |
|---|---|---|---|---|
| 1 | 0,03–1,54 | Olha as bandeiras dos 195 | gancho com objeto | rosto → corta para A01 P23 na última palavra |
| 2 | 1,54–2,78 | países do planeta. | gancho com objeto | segue A01 P23 |
| 3 | 3,07–4,64 | Vermelho, branco e azul estão em todas. | lista | segue A01 P23 |
| 4 | 4,92–5,86 | Dourado e verde também. | lista | segue A01 P23 |
| 5 | 6,02–7,03 | Agora tente achar o roxo. | gancho com objeto | entra A02 P23 · segue A01 P23 |
| 6 | 7,20–10,10 | Nenhum país usa roxo como cor principal. | negação ou virada | entra A03 P23 |
| 7 | 10,41–12,48 | Só um punhado tem um pontinho. | número | segue A04 P23 |
| 8 | 12,74–16,58 | Nas penas de uma ave, num leão, num arco-íris. | lista | entra A04 P23, A05 P23, A06 P23 |
| 9 | 16,78–19,78 | Por que uma cor era inalcançável? | pergunta | entra A07 P23 |
| 10 | 19,94–22,91 | Hoje o assunto é o roxo de Tiro. | anúncio | rosto + A08 P03 |
| 11 | 23,24–25,38 | No mundo antigo, fazer roxo era um pesadelo. | contexto | entra A09 P24, A10 P04 |
| 12 | 25,64–27,96 | Misturar tinta vermelha e azul dava marrom. | mecanismo | segue A09 P24 |
| 13 | 28,16–30,64 | E os roxos baratos tinham um defeito. | anúncio | segue A09 P24 |
| 14 | 30,85–31,86 | O sol os matava. | mecanismo | segue A09 P24 |
| 15 | 31,98–34,46 | Uma túnica no calor perdia a cor. | exemplo ou prova | entra A11 P09 · segue A09 P24 |
| 16 | 34,70–38,22 | Há 4.000 anos, tintureiros de uma ilha acharam a exceção. | fato com data | rosto + A12 P03 |
| 17 | 38,48–42,00 | Na costa de um país, uma cidade virou império. | lugar | entra A13 P22, A14 P24 |
| 18 | 42,13–44,60 | Vinha de um caramujo marinho com nome próprio. | descrição de objeto | entra A15 P24, A16 P04, A17 P24 |
| 19 | 44,88–46,66 | Então o caramujo é roxo por dentro, né? | pergunta | segue A15 P24 |
| 20 | 46,85–47,54 | Nem um pouco. | negação ou virada | rosto + A18 P03 |
| 21 | 47,71–50,40 | Abra uma concha viva: não tem roxo. | exemplo ou prova | entra A19 P24, A20 P09 |
| 22 | 50,79–55,76 | Só uma glândula de muco que paralisa a presa. | mecanismo | entra A21 P20, A22 P16 |
| 23 | 56,13–59,18 | Nada acontece até o líquido encontrar ar e sol. | mecanismo | rosto |
| 24 | 59,32–63,54 | Em minutos fica amarelo, verde, azul. | mecanismo | entra A23 P24 |
| 25 | 63,74–67,28 | Até travar num tom quase preto. | mecanismo | segue A23 P24 |
| 26 | 67,55–69,54 | Mas segure a lã contra o sol. | exemplo ou prova | entra A24 P06 |
| 27 | 69,73–73,20 | Como notou um escritor antigo: brilha como sangue. | citação | entra A25 P06 |
| 28 | 73,42–75,33 | Depois de fixada, nunca desbota. | conclusão | rosto |
| 29 | 75,76–79,94 | Para tingir uma barra de roupa, 10.000 conchas. | número | entra A26 P13 |
| 30 | 80,23–82,22 | E deixavam as glândulas em tinas quentes. | mecanismo | entra A27 P24 |
| 31 | 82,64–85,42 | Os pequenos eram esmagados inteiros. | mecanismo | rosto |
| 32 | 85,56–89,24 | Um morro de 40 m de conchas ainda existe. | número | entra A28 P22, A29 P07 |
| 33 | 89,52–93,44 | Nenhum país pagaria um corante mais caro que ouro. | comparação | entra A30 P24, A31 P04 |
| 34 | 93,66–96,74 | Em bandeiras feitas para rasgar no vento. | contexto | segue A30 P24, A31 P04 |
| 35 | 96,94–101,74 | Num mundo que desbota, parecia imortalidade. | comparação | entra A32 P07, A33 P04, A34 P11 |
| 36 | 101,86–103,62 | E os governantes o quiseram para si. | anúncio | rosto + A35 P03 |
| 37 | 104,12–106,94 | Em Roma, o imperador tornou crime vestir roxo. | pessoa | entra A36 P24, A37 P04 |
| 38 | 107,14–111,40 | Num recital, viu uma nobre de xale roxo. | ação narrada | entra A38 P24 |
| 39 | 111,51–116,25 | Os guardas a arrastaram e tomaram tudo. | ação narrada | segue A38 P24 |
| 40 | 116,54–123,44 | Imperadores trancaram os tintureiros no palácio. | ação narrada | entra A39 P24, A40 P24 |
| 41 | 123,72–125,46 | Aí o monopólio saiu pela culatra. | negação ou virada | rosto + A41 P03 |
| 42 | 125,64–129,82 | Cruzados saquearam a cidade em 1204. | fato com data | entra A42 P24, A43 P04 |
| 43 | 129,96–135,18 | Em 1453 a cidade caiu e as oficinas queimaram. | fato com data | entra A44 P24, A45 P04, A46 P24 |
| 44 | 135,44–136,96 | E um ofício de 3.000 anos | consequência | segue A46 P24 |
| 45 | 136,96–138,22 | morreu junto com o império (trocadilho). | piada | rosto + A47 P03 |
| 46 | 138,33–143,60 | Em 1856, um adolescente tentou fazer um remédio. | fato com data | entra A48 P16, A49 P04 |
| 47 | 143,71–144,95 | O experimento falhou. | negação ou virada | rosto + A50 P03 |
| 48 | 145,17–149,48 | Mas, ao lavar o béquer, a borra virou roxa. | negação ou virada | entra A51 P17 |
| 49 | 149,65–152,66 | Ele tinha inventado o primeiro corante sintético. | conclusão | rosto |
| 50 | 152,83–155,34 | De repente, o roxo não exigia 10.000 caramujos. | consequência | entra A52 P16 |
| 51 | 155,51–157,94 | Podia ser feito em fábrica por centavos. | consequência | segue A52 P16 |
| 52 | 157,94–161,78 | Mas a linguagem das bandeiras já estava escrita. | conclusão | entra A53 P23 |
| 53 | 161,91–165,24 | A cor mais poderosa chegou tarde demais. | conclusão | segue A53 P23 |

### Resumo por tipo (contagem por script)

Rosto = rosto puro + rosto com texto. Princípios = em quantas frases do tipo cada princípio estava na tela (uma frase pode ter mais de um); entre colchetes, os vídeos.

| tipo | frases (4 curiosidades) | V02 | rosto | cena | % rosto | princípios na tela (4 curiosidades) |
|---|---|---|---|---|---|---|
| VI negação ou virada | 34 | 1 (rosto) | 25 (22 + 3 com P03) | 9 | 74 % | P03 3 [5] · P14 2 [1,3] · P07 2 [3] · P16, P08, P06, P23, P17 1 cada |
| ME mecanismo | 34 | 0 | 2 | 32 | 6 % | P18 9 [1] · P14 6 [1,3] · P15 5 [1,4] · P24 5 [5] · P08 3 [1,3] · P16 3 [1,4,5] · P19 2 · P17 2 · P13 2 |
| DA fato com data | 20 | 0 | 1 (P03) | 19 | 5 % | P08 6 [1,3,4] · P05 5 [3,4] · P21 4 [1] · P11 3 [1] · P24 3 · P04 3 [5] · P19 2 · P16 2 |
| NA ação narrada | 16 | 0 | 1 | 15 | 6 % | P24 4 [5] · P08 3 [3,4] · P10 3 [4] · P20 2 · P16 2 · P06 2 · P14, P07, P17 1 |
| AN anúncio | 14 | 4 (2 rosto) | 9 (5 + 4 com P02/P03) | 5 | 64 % | P02 2 [1,3] · P14 2 [1,3] · P03 2 [5] · P08, P12, P24 1 |
| CL conclusão | 12 | 1 (cena) | 5 | 7 | 42 % | P23 2 [5] · P09, P14, P08, P06, P19, P17 1 |
| CQ consequência | 12 | 1 (cena) | 1 | 11 | 8 % | P18 3 [1] · P08 3 [1,3] · P09 2 [1] · P16 2 [5] · P19, P13, P24 1 |
| PE pergunta | 11 | 0 | 3 | 8 | 27 % | P06, P18, P08, P07, P12, P16, P20, P23, P24: 1 cada |
| LI lista | 9 | 3 (cena) | 0 | 9 | 0 % | P08 5 [1,3] · P23 5 [5] · P11, P15, P14 1 |
| EX exemplo ou prova | 9 | 0 | 0 | 9 | 0 % | P08 3 [1,4] · P06 2 [1,5] · P17 2 [4] · P09 2 [5] · P24 2 · P05, P07, P13 1 |
| PS pessoa | 8 | 0 | 0 | 8 | 0 % | P05 4 [3,4] · P14, P08, P11, P20, P24, P04 1 |
| NU número | 8 | 3 (1 rosto) | 1 | 7 | 12 % | P13 3 [3,4,5] · P08, P17, P23, P22, P07 1 |
| CI citação | 8 | 0 | 0 | 8 | 0 % | P20 4 [1,3,4] · P10 3 [3,4] · P17, P06 1 |
| CO comparação | 7 | 0 | 0 | 7 | 0 % | P07 2 [3,5] · P16 2 [4] · P04 2 [5] · P18, P12, P08, P24, P11 1 |
| GO gancho com objeto | 6 | 0 | 4 (3 + 1 com P02) | 2 | 67 % | P23 2 [5] · P02 1 [4] |
| CR crença comum | 6 | 0 | 2 | 4 | 33 % | P14 2 [1,3] · P05 1 · P20 1 |
| DO descrição de objeto | 6 | 1 (cena) | 0 | 6 | 0 % | P07 2 [3] · P24 2 [5] · P15, P18, P08, P06, P16, P12, P04 1 |
| OP comentário ou ponte | 6 | 0 | 5 | 1 | 83 % | P08 1 |
| CT contexto | 5 | 0 | 1 | 4 | 20 % | P24 2 · P04 2 [5] · P08 1 [1] · P06 1 [4] |
| LU lugar | 3 | 2 (cena) | 0 | 3 | 0 % | P11, P05, P14 [3] · P22, P24 [5] |
| PI piada | 3 | 0 | 2 (1 com P03) | 1 | 67 % | P08 1 [3] · P03 1 [5] |
| CTA | 0 | 6 (2 rosto) | n/a | n/a | n/a | só V02: P20 3 · P21 1 |
| **total** | **237** | **22** | **62** | **175** | **26 %** | |

**Com e sem V02:** frases no rosto 62 de 237 (26 %) sem o V02; 68 de 259 (26 %) com ele. Tipos que só o V02 traz: CTA (6). No V02, rosto = pedido, negação, transição, convite e CTA final (6 frases); cena = todo dado concreto (16).

### Cruzamento inverso: cada princípio, que falas o puxaram

Frases (todas, 5 vídeos; `*` = frase do V02).

| princípio | frases | vídeos | tipos de fala que o puxaram |
|---|---|---|---|
| P02 título sobre o rosto | 3 | V01 V03 V04 | AN 2 (nome da série), GO 1 (título-pergunta sobre o "olha isto") |
| P03 texto grande sobre o rosto | 7 | V05 | VI 3, AN 2, DA 1, PI 1 |
| P04 rótulo e número digitados | 9 | V05 | DA 3, CT 2, CO 2, DO 1, PS 1 |
| P05 etiqueta de papel | 12 | V03 V04 | DA 5, PS 4, EX 1, LU 1, CR 1 |
| P06 cartão, câmera viva | 12 | 4 | EX 2, NA 2, e 1 cada de ME, PE, DA, DO, CL, VI, CT, CI |
| P07 tela cheia em deriva | 11 | V03 V05 | DO 2, VI 2, CO 2, PE, NA, EX, ME, NU 1 |
| P08 pilha de cartões | 34 | V01 V03 V04 | DA 6, LI 5, EX 3, CQ 3, ME 3, NA 3, e 1 cada de 11 tipos |
| P09 cartão que cai por cima | 6 | V01 V05 | CQ 2, EX 2, ME 1, CL 1 |
| P10 empurrão ou cobertura | 7 | V03 V04 | CI 3, NA 3, DA 1 |
| P11 viagem de câmera | 7 | 4 | DA 3, LI, LU, PS, CO 1 |
| P12 faixa de b-roll | 5 | V04 | CO, PE, AN, ME, DO 1 |
| P13 afastamento, quantidade | 7 | V03 V04 V05 | NU 3, ME 2, EX 1, CQ 1 |
| P14 disco creme com recorte | 18 | V01 V03 | ME 6, VI 2, AN 2, CR 2, LI, DA, PS, CL, NA, LU 1 |
| P15 lupa e janela | 11 | V01 V02 V04 | ME 5, LI* 3, LI 1, DO 1, CL* 1 |
| P16 colagem de recortes | 17 | 4 | ME 3, CO 2, DA 2, NA 2, CQ 2, VI, NU*, LI*, CQ*, DO, PE 1 |
| P17 objeto que se transforma | 10 | V04 V05 | EX 2, ME 2, CI, NA, NU, DA, CL, VI 1 |
| P18 diagrama com estados | 15 | V01 | ME 9, CQ 3, PE, CO, DO 1 |
| P19 marcação à mão | 7 | 4 | DA 2, ME 2, AN* 1, CL 1, CQ 1 |
| P20 documento com marca-texto | 15 | 5 | CI 4, CTA* 3, NA 2, AN*, DO*, CR, PE, PS, ME 1 |
| P21 linha do tempo, dado em papel | 6 | V01 V02 | DA 4, NU* 1, CTA* 1 |
| P22 mapa | 4 | V02 V05 | LU* 2, LU 1, NU 1 |
| P23 3D cor seletiva | 12 | V05 | LI 5, GO 2, CL 2, VI, NU, PE 1 |
| P24 cena 3D narrativa | 24 | V05 | ME 5, NA 4, DA 3, CT 2, EX 2, DO 2, e 1 cada de 6 tipos |

---

## 3 · Regras de colocação

**R1 · Virada fica no rosto.** Frase de negação ou de "mas…" fica no rosto com legenda.
- Contagem: 25 de 34 viradas no rosto (74 %), nos 4 vídeos: V01 6/8, V03 9/13, V04 7/8, V05 3/5 (as 3 com texto grande P03). As viradas são o maior grupo do rosto: 25 dos 62 trechos de rosto (40 %).
- Forma: frase curta (as frases de rosto têm mediana de 5 a 7 palavras, contra 9 a 12 nas de cena), plano de rosto de 1,6 a 2,3 s (mediana por vídeo; mínimo 0,50 s em "Não é.").
- Força: **regra (4 vídeos)**.
- Exceções (9): quando a virada traz um fato concreto novo, ela mostra o fato: V01 #53 (cédulas, V01-A43 P16), V03 #14 (V03-A09 P08), V03 #23 (V03-A12 P07), V03 #40 (V03-A19 P14), V03 #56 (V03-A24 P07), V04 #40 (V04-A36 P06), V05 #6 (V05-A03 P23), V05 #48 (V05-A51 P17); e V01 #2, que é o 2º tempo do gancho e segue o objeto.

**R2 · Teste da regra "anuncia → rosto, descreve → mostra".**
- **Descreve → mostra: vale.** Frases com dado concreto (descrição, mecanismo, ação, data, pessoa, lugar, número, lista, comparação, citação, exemplo): 123 de 128 mostradas (96 %), nos 4 vídeos. Só descrição + mecanismo: 38 de 40 (95 %). As 5 no rosto: V01 #45 (ação que abre capítulo), V03 #18 ("tinha 23 anos", número de choque), V05 #16 (marco de tempo com texto grande), V05 #23 e #31 (mecanismo dito como ponte, sem objeto novo). **Regra (4 vídeos).**
- **Anuncia → rosto: vale em 2 de cada 3.** Anúncio + gancho: 13 de 20 no rosto (65 %), nos 4 vídeos. **Regra (4 vídeos), com exceções fixas.**
- **Onde falha:** (a) o anúncio que NOMEIA o tema mostra o objeto: "e hoje o assunto é X" → recorte do objeto no disco (V01 #8 V01-A11, V03 #9 V03-A07; regra em 2 vídeos); (b) a abertura de capítulo que muda de época vai para arquivo (V04 #7, faixa P12) ou segue a cena (V03 #15, V05 #13); (c) o maior motivo para voltar ao rosto não é anunciar, é virar (R1): viradas 25, anúncios 9, pontes 5, conclusões 5, ganchos 4, perguntas 3 dos 62 trechos de rosto; (d) no V05 o comando ao espectador ("agora tente achar o roxo") fica em cena.
- **Regra corrigida para o editor:** "virou, anunciou ou comentou → rosto; disse um substantivo que se fotografa → mostra".

**R3 · Pergunta-tese em cena, pergunta curta do meio no rosto.**
- Pergunta-tese do fim do gancho: 4 de 4 em cena, mostrando o objeto da pergunta sem responder: V01 #6 (V01-A08 P06 + A09 P18), V03 #7 (V03-A05 P07), V04 #5 (V04-A04 P12), V05 #9 (V05-A07 P23). **Regra (4 vídeos).**
- Pergunta de crença ("…, né?"): 3 de 3 em cena, mostrando o termo da crença (V01 #47, V04 #21 V04-A21 P16, V05 #19). **Regra (3 vídeos).**
- Pergunta curta no meio ("De quem era?", "Como…?", "Por quê?"): 3 de 3 no rosto, só no V03 (#29, #39, #68). **Regra em 1 vídeo.**

**R4 · Data puxa o ano escrito sobre a imagem da época.**
- Contagem: 21 frases com ano explícito, 4 vídeos, 0 no rosto. 16 de 21 (76 %) mostram o ano escrito: etiqueta de papel P05 (V03 #17, #28, #54; V04 #11, #15, #30) e etiqueta dentro de pilha ou grade (V03 #34 V03-A17, #62 V03-A27, #66 V03-A28; V04 #53 V04-A48); rótulo digitado P04 (V05 #42, #43, #46: 3 de 3); régua de anos P21 com chicote P11 (V01 #22, #23, #24).
- Imagem por baixo: foto ou retrato da época (pilha P08 ou cartão P06), nunca o rosto.
- Força: **regra (4 vídeos)**, com 3 formas de escrever o ano (P05 em V03 e V04, P04 em V05, P21 em V01).
- Exceções sem ano escrito: V01 #10 e #46 (pilha de fotos da época), V01 #26 (foto + ideia desenhada), V01 #51 (carta, P20), V04 #44 (documento com o nome marcado).
- Detalhe: nome e data em frases seguidas → uma etiqueta de cada vez, na ordem da fala (V03-A14); a etiqueta sai quando a frase passa da data para a ação (V04-A27).

**R5 · Pessoa citada puxa retrato; o nome é escrito só na 1ª vez.**
- Contagem: 18 frases com pessoa nomeada ou apresentada, 4 vídeos, 0 no rosto. Nome escrito em etiqueta P05 em 5 frases (V03, V04; mais etiquetas de nome dentro de pilhas, ex.: V03-A11, A17) e em rótulo P04 em 2 (V05-A37, A49); nome marcado no documento da pessoa em 1 (V04-A40). Retrato da pessoa ou de quem a representa na maioria (V01-A18, V03-A03, A10, A25, V04-A10, A15, A32, A34, V05-A36, A48) (contagem aproximada: inferido das Regras de escolha).
- Pessoa que volta à história: o mesmo retrato, sem nome (V04-A36, V03-A18).
- Força: **regra (4 vídeos)**.

**R6 · Pilha × cartão sozinho × tela cheia.**
- **Pilha P08** (19 pastas, V01 V03 V04, 34 frases): frase com 2 ou mais itens concretos, ou fato que pede mais de uma prova. Tipos: data 6, lista 5, exemplo 3, consequência 3, mecanismo 3, ação 3. Um cartão novo por meia-frase. **Regra (3 vídeos).**
- **Cartão sozinho P06** (12 pastas, 4 vídeos): uma prova só, um retrato num papel, uma reação, o objeto da pergunta (V01-A02, A08, V04-A15, A34, A36, A47, V05-A24). 11 de 12 entram por corte seco. **Regra (4 vídeos).**
- **Tela cheia P07** (8 pastas, V03 V05): imagem rica que a câmera "lê" durante a descrição física (V03-A01, A02, A26), panorama na pergunta-tese (V03-A05), ressalva ou resposta curta (V03-A24, A29), escala (V05-A29). **Regra em 2 vídeos.**
- Lista de 3 itens ou mais (19 frases com lista) nunca fica no rosto e quase nunca num cartão sozinho: vira pilha, fila ou um item por palavra.

**R7 · Disco creme com recorte (P14).** 11 pastas, V01 e V03, 18 frases. Puxado por: (a) o objeto-tema nomeado sozinho ("olha isto", "hoje o assunto é X", objeto da época): V01-A01, A11, A13, V03-A07; (b) mecanismo em etapas com recortes que agem: V01-A03, V03-A19, A20 (6 frases de mecanismo); (c) pessoa ou grupo citado: V01-A18, A28; (d) callback no fecho: V01-A46. **Regra em 2 vídeos.** No V04 o mesmo papel (objeto isolado) é feito por recorte sem disco sobre fundo escuro (P16, V04-A02); no V05, por 3D (P23).

**R8 · Diagrama (P18).** 8 pastas, só V01, 15 frases: mecanismo 9, consequência 3, pergunta, comparação, descrição 1 cada. Mecanismo explicado em 2 frases ou mais seguidas → um só diagrama que muda de estado a cada frase (V01-A14 → A15; A34; A37 dura 12,9 s com 3 trechos). **Regra em 1 vídeo.** Nos outros vídeos o mecanismo vira: disco com etapas (V03, P14), objeto que se transforma (V04, P17), lupa ou janela (V01 e V04, P15) ou cena 3D que troca de estado (V05, P24).

**R9 · Marcação à mão e marca-texto.**
- **Traço à mão** (P19 isolado: 5 pastas, 4 vídeos; mais cerca de 20 círculos e elipses dentro de outras pastas, ex.: V01-A16, A18, A20, V03-A03, A08, V05-A07, A21, A28, A29, A53; contagem aproximada pelo `resumo_forma`): aponta o detalhe que a frase nomeia, na palavra (o alvo, V04-A08; um rosto numa foto, V01-A20; a forma que dá o nome, V04-A49; a ideia escrita, V01-A27; a metáfora do fecho, V03-A31). **Regra (4 vídeos).**
- **Marca-texto amarelo** (10 pastas, 5 vídeos): só sobre texto real que a fala lê ou cita (carta V01-A42, anúncio V01-A44, texto antigo V03-A16, livro V04-A35, assinatura V04-A40); no V02, em instruções e números (5). Varre no ritmo da leitura. **Regra (5 vídeos).**

**R10 · Documento (P20).** 11 pastas, 5 vídeos. Citação de fonte: 8 de 8 citações em cena, 0 no rosto; 4 com documento e marca-texto (V01 #51, V03 #31, #32, V04 #37), 2 com documento que é coberto pela imagem do que ele diz (P10: V03 #30, V04 #41), 1 com as cores citadas entrando no objeto (V04 #31, P17) e 1 com imagem parada e push-in (V05 #27, P06). Também puxam documento: "muita gente dizia" (V04-A20, jornal), relação dinheiro-empresa (V01-A44), pessoa apresentada pela obra (V04-A40), parte técnica pequena (V05-A21, prancha). A frase que só anuncia a citação ("Então ele disse:") fica no rosto (V04 #36). **Regra (4 curiosidades).**

**R11 · Mapa, linha do tempo e número.**
- **Mapa P22** (3 pastas, V02 e V05): lugar dito como origem ou destino → mapa sem rótulos, pinta ou circula o ponto e mergulha nele (V02-A08, V05-A13, A28). **Regra em 2 vídeos (1 curiosidade).** Lugar sem mapa: foto do lugar (V01-A24, V04-A31), chicote lateral quando algo "atravessa" para lá (V03-A13), rótulo digitado (V05-A10, A37).
- **Linha do tempo P21:** 3 datas seguidas da mesma vida → régua com ponto que anda + chicote a cada data (V01-A19 a A25). **Ocorrência (1 sequência).** No V02, contador e gráfico de papel para número que muda (V02-A01, A11).
- **Número:** quantidade grande → afastamento que revela a quantidade (P13: grade que esvazia V03-A28, parede de 4.000 V04-A45, monte de 10.000 V05-A26): 3 de 8 frases de número, **regra (3 vídeos)**. Número com comparação → rótulo com o número (V05-A31, A33) ou diagrama lado a lado (V01-A31). Número curto de choque → rosto (V03 #18, ocorrência).

**R12 · Colagem e transformação.**
- **Colagem P16** (12 pastas, 4 vídeos, 17 frases): cada substantivo concreto vira um recorte que entra na palavra (itens e cores V04-A02, maquete do mecanismo V01-A41, dinheiro V01-A43 e V02-A09, antes × depois V05-A52, esquete com balões V05-A22). Tipos: mecanismo 3, comparação 2, data 2, ação 2, consequência 2. **Regra (4 vídeos).**
- **Transformação P17** (8 pastas: V04 7, V05 1; 10 frases): verbo de ação sobre o objeto ("pintar", "quebrar", "imprimir", "cobrir", "virar roxo") → a ferramenta aparece e o objeto muda na palavra do verbo. **Regra em 2 vídeos.**

**R13 · Troca por corte × por movimento.**
- Rosto ↔ cena: sempre corte seco (todos os trechos de rosto dos 5 vídeos; P25). **Regra (5 vídeos).**
- Entrada das pastas de cena: 106 de 182 por corte seco (58 %), 76 dentro do plano, sem corte (42 %). Por vídeo (corte × dentro): V01 19 × 26 · V03 24 × 6 · V04 28 × 21 · V05 27 × 19 · V02 8 × 4 (mais 4 pans de câmera no tampo).
- **Entra por corte** o que troca de assunto ou de imagem-base: P06 11/12, P07 7/8, P08 15/19, P16 11/12, P24 13/15, P12 4/4, P22 3/3, P05 7/9.
- **Entra sem corte** o que soma ao que já está: P04 8/8 (rótulos), P09 6/6 (cartão que cai por cima), P10 6/7 (empurrão), P11 6/7 (viagem de câmera), P15 7/9 (lupa), P18 5/8 (estados do diagrama), P19 4/5, P13 4/6.
- Leitura: movimento = continuidade do mesmo assunto (datas em série → chicote; nova foto do mesmo personagem → empurrão; detalhe → lupa; prova rápida → cartão por cima). Corte = assunto novo, imagem-base nova, ou rosto. **Regra (4 vídeos)**; o V03 corta mais (24 × 6), o V04 empurra mais (P10 só lá em volume).

**R14 · Uma imagem nova por frase.** 121 de 175 frases de cena (69 %) trazem pasta nova; as outras seguem a cena com passos internos (cartão que cai, estado, etiqueta). Eventos visuais a cada 1,0 a 1,2 s (mediana dos vídeos, seção (c) das análises). **Regra (4 vídeos).**

**R15 · Assinatura da série no rosto, logo após a pergunta-tese.** 4 de 4 curiosidades dizem "Este é [série] episódio N, e hoje…" entre 15 e 20 s, no rosto (V01 e V03 com título P02; V04 rosto puro; V05 texto grande P03). **Regra (4 vídeos).**

**R16 · O gancho começa no rosto e corta na palavra do objeto.** 4 de 4 abrem com "olha [objeto]" no rosto por 0,71 s (V01), 0,92 s (V03), 1,25 s (V04) e 1,29 s (V05), e cortam para o objeto na palavra do objeto ou logo depois. **Regra (4 vídeos).**

### Equivalências do V05 (único com 3D e texto grande)

| no V05 | papel | nos outros vídeos o mesmo papel é feito por |
|---|---|---|
| P24 cena 3D narrativa (15 pastas, 24 frases: mecanismo 5, ação 4, data 3) | encenar o fato narrado ou o processo | ação e data → pilha de fotos da época P08 ou cartão P06 (V01, V03, V04); mecanismo → diagrama P18 (V01), disco com etapas P14 (V03), transformação P17 (V04) |
| P23 3D com cor seletiva (8 pastas: gancho, lista, fecho) | mostrar o objeto do tema e procurar o detalhe | imagem do objeto em cartão ou tela cheia com câmera viva P06/P07 (V03-A01/A02), lupa no detalhe P15 (V01-A05), círculo à mão P19; lista de exemplos → pilha P08 (V01-A16) ou fila com lente P15 (V02-A05) |
| P03 texto grande sobre o rosto (7: viradas, anúncios, trocadilho) | dar peso à virada no rosto | rosto puro com legenda P01 (V01, V03, V04); no nome da série, título P02 (V01, V03) |
| P04 rótulo e número digitados (8) | escrever data, lugar, pessoa ou número | etiqueta de papel P05 (V03, V04), régua de anos P21 (V01), contador P21 (V02) |

---

## 4 · Como a referência escolhe O QUE mostrar

Classifiquei a "Regra de escolha" de cada uma das 192 pastas (leitura do `notes.md`, 1 categoria por pasta; contagem aproximada).

| escolha do conteúdo | pastas | % | vídeos | exemplos |
|---|---|---|---|---|
| objeto ou ação literal (o que a palavra diz, fotografado ou recortado) | 63 | 33 % | 5 | V01-A01, A02, V03-A04, V04-A02, A33, V05-A19 |
| pessoa ou grupo citado (retrato, recorte, foto de época do grupo) | 26 | 14 % | 4 | V01-A18, A28, V03-A10, A25, V04-A10, A32, V05-A36, A48 |
| diagrama ou encenação do mecanismo | 25 | 13 % | 4 | V01-A14, A34, V03-A19, V04-A19, A25, V05-A23 |
| número ou data visualizado (escrito, contado, quantidade visível) | 16 | 8 % | 5 | V01-A25, V03-A28, V04-A09, A45, V05-A26, A43 |
| documento da fonte | 13 | 7 % | 5 | V01-A42, V03-A15, A16, V04-A20, A35, V05-A21 |
| metáfora ou símbolo concreto | 13 | 7 % | 5 | V01-A43 (dinheiro → maço), V03-A31 (coroa), V04-A30 (arlequim), V05-A14 (império → frota), A34 (imortalidade → busto), A40 (expressão ao pé da letra) |
| texto ou título | 10 | 5 % | 4 | V01-A10, V03-A06, V04-A01, V05-A08 |
| lugar (mapa, foto do lugar) | 7 | 4 % | 5 | V01-A24, V02-A08, V04-A31, V05-A13, A28 |
| prova real depois da ilustração | 7 | 4 % | 3 | V01-A07, A35, A38, V04-A47, V05-A11, A20, A24 |
| callback (imagem já vista) | 6 | 3 % | 4 | V01-A46, V03-A12, A18, A30, V04-A36, V05-A53 |
| transição sem conteúdo próprio | 6 | 3 % | 3 | V01-A04, A19, A21, A23, V03-A13, V04-A43 |

**Ordem de decisão que sai daqui (para preencher qualquer lacuna):**
1. A frase tem um substantivo que se fotografa → o objeto literal, na palavra (1 em cada 3 pastas).
2. Nomeia uma pessoa ou um grupo → retrato ou foto de época dele (+ nome escrito na 1ª vez).
3. Cita uma fonte → o documento real, com a linha marcada.
4. Explica como funciona → o mecanismo desenhado ou encenado SOBRE o próprio objeto, um estado por frase.
5. Dá número ou data → o número escrito, ou a quantidade tornada visível.
6. A palavra é abstrata (valor, poder, imortalidade) → um objeto-símbolo concreto, nunca texto solto.
7. Depois de uma ilustração (diagrama, 3D) → a foto real que prova, por cima.
8. No fecho → a imagem do gancho de volta, agora com o agente agindo.

---

## 5 · Sequência e alternância

**Pares mais frequentes** (sequência de cada vídeo: trechos de rosto `R` + pastas de cena em ordem de entrada; contagem de pares seguidos):

| par | vezes | vídeos | leitura |
|---|---|---|---|
| R → P08 | 13 | V01 V03 V04 | depois da virada no rosto, abre uma pilha (o fato novo com provas) |
| P08 → R | 11 | V01 V03 V04 | a pilha fecha e o rosto vira a história |
| R → P16 | 6 | V01 V04 V05 | rosto → colagem |
| R → P20 | 6 | V01 V02 V04 | rosto anuncia, documento prova |
| P20 → R | 6 | V01 V02 V03 V04 | documento lido → rosto comenta |
| P23 → P23 | 6 | V05 | o 3D encadeia zooms no mesmo plano |
| P24 → P04 | 6 | V05 | cena 3D ganha rótulo |
| R → P14 · R → P06 · P05 → R · R → P24 | 5 cada | V01 V03 · V01 V03 V04 · V03 V04 · V05 | |
| P21 ↔ P11 | 3 + 3 | V01 | régua e chicote se alternam na sequência de datas |

- **Volta ao rosto:** intervalo mediano entre duas voltas: V01 9,0 s · V02 10,7 s · V03 7,3 s · V04 12,1 s · V05 13,5 s; mínimo 1,6 a 5,9 s; máximo 18 a 24 s. Rosto ocupa 14 % (V04) a 21 % (V01) do tempo.
- **Cenas seguidas sem rosto:** mediana de 1 pasta (V01, V03), 2 (V02), 3 (V04) e 3,5 (V05) entre duas voltas; máximo 9 (V01, a sequência de datas).
- **Planos de cena seguidos (corte cena → cena, sem rosto no meio):** V01 13 de 15 trechos com 1 plano só; V03 15 de 19; V04 tem 3 trechos de 4 planos; V05 tem 4 trechos de 3 planos. Ou seja: V01 e V03 alternam rosto e cena quase a cada plano; V04 e V05 encadeiam 2 a 4 planos de cena.
- **Mesmo princípio duas vezes seguidas:** raro fora do V05: P23 6 e P24 3 (V05, 3D contínuo); P15 2, P10 2; os demais no máximo 1. Nos V01, V03 e V04 a cena seguinte quase sempre muda de princípio, ou passa pelo rosto.

---

## 6 · Sincronia: onde o evento cai em relação à palavra que o puxa

Fonte: `gatilho_offset_ms` dos `eventos.json` (tempo de entrada da pasta menos o início da palavra-gatilho; negativo = antes). 192 pastas A.

**Por tipo de entrada (calculado ANTES da remedição; a ordem de grandeza se mantém, os valores exatos mudaram pouco: ver a linha "todas" da tabela por princípio):**

| entrada | n | mediana | antes (< −40 ms) · junto (±40) · depois (> +40) |
|---|---|---|---|
| pasta que entra por corte seco | 106 | −53 ms | 60 · 40 · 6 |
| pasta que entra dentro do plano | 76 | −25 ms | 31 · 22 · 23 |
| texto sobre o rosto (P02, P03) | 10 | −32 ms | 5 · 3 · 2 |
| **todas** | **192** | **−40 ms** | **96 · 65 · 31** |

Cortes secos (das análises): V01 mediana −46 ms (34 cortes); V02 entre −46 e +56 ms; V03 de −4 a −170 ms antes da 1ª palavra do plano; V04 os cortes caem na pausa entre frases (100 a 190 ms); V05 ≈ −55 ms. Legenda (P01): troca mediana +12 ms (V01), 0 ms (V03), +8 ms (V04) da 1ª palavra do bloco.

**Por princípio (recalculado em 2026-11-20, depois da conferência e da remedição, a partir dos `eventos.json` corrigidos):**

| princípio | n | vídeos | mediana (ms) | faixa (ms) | antes · junto · depois |
|---|---|---|---|---|---|
| P02 Título sobre o rosto | 3 | V01, V03, V04 | -73 | -80 a -47 | 3 · 0 · 0 |
| P03 Texto grande palavra a palavra sobre o rosto | 7 | V05 | -8 | -55 a +177 | 2 · 3 · 2 |
| P04 Rótulo e número digitados sobre a cena | 8 | V05 | +46 | -140 a +187 | 2 · 2 · 4 |
| P05 Etiqueta de papel na imagem | 9 | V03, V04 | -59 | -403 a -18 | 6 · 3 · 0 |
| P06 Imagem em cartão com câmera viva | 12 | V01, V03, V04, V05 | -43 | -105 a +10 | 6 · 6 · 0 |
| P07 Imagem em tela cheia em deriva | 8 | V03, V05 | -56 | -109 a +103 | 5 · 2 · 1 |
| P08 Pilha de cartões | 19 | V01, V03, V04 | -103 | -176 a +265 | 12 · 6 · 1 |
| P09 Cartão que cai por cima da cena | 6 | V01, V05 | -42 | -67 a +71 | 3 · 2 · 1 |
| P10 Troca de cartão por empurrão ou cobertura | 7 | V03, V04 | -22 | -296 a +242 | 2 · 3 · 2 |
| P11 Viagem de câmera entre peças | 7 | V01, V03, V04, V05 | -60 | -422 a +33 | 4 · 3 · 0 |
| P12 Faixa de b-roll em letterbox | 4 | V04 | -14 | -68 a +4 | 1 · 3 · 0 |
| P13 Afastamento que revela a quantidade | 6 | V03, V04, V05 | -6 | -286 a +228 | 2 · 3 · 1 |
| P14 Disco creme com recorte | 11 | V01, V03 | -68 | -293 a +208 | 6 · 2 · 3 |
| P15 Lupa e janela circular | 9 | V01, V02, V04 | +18 | -38 a +196 | 0 · 7 · 2 |
| P16 Colagem de recortes | 12 | V01, V02, V04, V05 | -47 | -123 a -18 | 7 · 5 · 0 |
| P17 Objeto que se transforma pela ação narrada | 8 | V04, V05 | -32 | -94 a +112 | 3 · 4 · 1 |
| P18 Diagrama chapado com estados | 8 | V01 | -101 | -167 a +83 | 6 · 1 · 1 |
| P19 Marcação e desenho à mão | 5 | V01, V02, V03, V04 | +4 | -114 a +622 | 2 · 1 · 2 |
| P20 Documento com marca-texto | 11 | V01, V02, V03, V04, V05 | -36 | -269 a +342 | 4 · 3 · 4 |
| P21 Linha do tempo e dado em papel | 6 | V01, V02 | +21 | -72 a +267 | 1 · 3 · 2 |
| P22 Mapa com marcação | 3 | V02, V05 | -5 | -7 a +100 | 0 · 2 · 1 |
| P23 B-roll 3D com cor seletiva | 8 | V05 | -36 | -195 a +313 | 4 · 1 · 3 |
| P24 Cena 3D narrativa | 15 | V05 | -70 | -164 a +245 | 11 · 3 · 1 |
| **todas as pastas A com gatilho** | **192** | | **-38** | -422 a +622 | **92 · 68 · 32** |

**Regra prática (valores recalculados em 2026-11-20):** imagem nova 1 a 3 quadros antes da 1ª sílaba da palavra (−40 a −110 ms; P08 −103, P18 −101, P24 −70); rótulos, números digitados, régua, lupa e marcação à mão caem junto ou logo DEPOIS da palavra (P04 +46, P21 +21, P15 +18, P19 +4), porque confirmam ou apontam o que acabou de ser dito. A faixa larga de alguns princípios (P19 até +622 ms, P20 até +342 ms) vem de casos em que a marca espera o fim da palavra citada.

---

## 7 · Esqueleto do roteiro de uma curiosidade (V01, V03, V04, V05)

Partes comuns montadas a partir das estruturas das análises (b); duração medida pelos quadros dos cortes. % = do vídeo. "rosto" = % da parte com o rosto na tela.

| parte | V01 (158,8 s) | V03 (171,8 s) | V04 (160,5 s) | V05 (165,5 s) | média |
|---|---|---|---|---|---|
| A · gancho com objeto + fato estranho + pergunta-tese | 15,7 s · 9,9 % · rosto 5 % | 19,3 s · 11,3 % · 11 % | 14,7 s · 9,2 % · 9 % | 20,0 s · 12,1 % · 6 % | 17,4 s · 10,6 % |
| B · assinatura da série + "hoje: X" | 3,8 s · 2,4 % · 41 % | 4,1 s · 2,4 % · 41 % | 4,4 s · 2,7 % · 100 % | 3,1 s · 1,9 % · 100 % | 3,9 s · 2,4 % |
| C · crença comum ou contexto do problema | 31,6 s · 19,9 % · 26 % | 14,7 s · 8,5 % · 25 % | 20,7 s · 12,9 % · 5 % | 11,5 s · 7,0 % · 0 % | 19,6 s · 12,1 % |
| D · história: origem, pessoas, datas | 25,9 s · 16,3 % · 21 % | 53,5 s · 31,2 % · 17 % | 31,2 s · 19,4 % · 15 % | 21,4 s · 13,0 % · 22 % | 33,0 s · 20,0 % |
| E · mecanismo (como funciona de verdade) | 44,1 s · 27,8 % · 13 % | 27,6 s · 16,1 % · 15 % | 19,6 s · 12,2 % · 8 % | 19,6 s · 11,9 % · 28 % | 27,7 s · 17,0 % |
| F · desdobramentos com viradas (consequências, queda, fato moderno) | 32,2 s · 20,3 % · 27 % | 47,0 s · 27,3 % · 23 % | 67,5 s · 42,0 % · 14 % | 82,3 s · 49,8 % · 16 % | 57,3 s · 34,9 % |
| G · fecho (tese + callback) | 5,6 s · 3,5 % · 46 % | 5,6 s · 3,3 % · 40 % | 2,4 s · 1,5 % · 0 % | 7,4 s · 4,5 % · 0 % | 5,3 s · 3,2 % |

Notas: no V01 a parte E inclui o desmonte da crença ("pergunte a um surfista…" → "mas a água é péssima") antes do mecanismo verdadeiro; no V03 a crença comum (C) vem logo depois da assinatura ("você vai ouvir uma palavra: sífilis"); no V05 a parte F inclui o custo (10.000 conchas), o poder, a queda e a invenção moderna. O mecanismo começa entre 34 % (V05) e 53 % (V03) do vídeo.

**O que a edição faz em cada parte:**
- **A:** 0,7 a 1,3 s de rosto no "olha", corte seco para o objeto na palavra; depois só cenas (rosto 5 a 11 % da parte), uma imagem por meia-frase; o fato estranho às vezes volta ao rosto como virada curta (V03 "Não é dele."); a pergunta-tese fica em cena, sobre a imagem do objeto (R3).
- **B:** rosto com título (P02 ou P03) ou rosto puro; quando a frase nomeia o tema, corta para o objeto recortado (V01, V03).
- **C:** pessoas que acreditam (recortes ou retratos), fotos de época do problema, ou arquivo em faixa (V04); a crença é desmentida no rosto ("Não.", "Nem tanto.").
- **D:** datas com ano escrito, retratos com nome, pilhas; o rosto volta nas viradas da história (15 a 22 % da parte).
- **E:** a parte mais densa de cena (rosto 8 a 15 %, exceto V05 com 28 %): diagrama que muda de estado, disco com etapas, transformação ou 3D; lupa no detalhe; prova real por cima depois da ilustração.
- **F:** alternância regular rosto (virada) ↔ cena (fato); documento e citação aparecem aqui (carta, livro, jornal).
- **G:** callback da imagem do gancho em 3 de 4 (V01-A46, V03-A30/A31, V05-A53); o V04 liga as duas pontas do tema com fragmentos que voam até a obra (V04-A50). Última frase no rosto em V01 e V03; em cena em V04 e V05.

**Como cada vídeo acaba:** nenhum dos 4 tem CTA falado, pedido de seguir, cartela ou música de saída. Terminam na frase-tese: V01 e V03 no rosto, V04 e V05 sobre a última cena. Só o V02 (anúncio) tem CTA: "o link está na bio", no rosto.

---

## 8 · Tabela de recomendação por beat

Para cada tipo de fala: A = a mais frequente na amostra; B e C = alternativas. Princípio que só existe em 1 vídeo entra no máximo como C, marcado **[1 vídeo]**. "Rosto" aparece sempre que o mapa mostra que é plausível.

| tipo | A | B | C |
|---|---|---|---|
| **GO** gancho com objeto | **rosto + legenda, corte seco para o objeto na palavra do objeto** · regra (4/4 vídeos; 4 de 6 frases) · sempre na 1ª frase do vídeo | **recorte do objeto sozinho**, no disco creme (P14) ou sobre fundo escuro (P16) · regra em 2 vídeos (V01, V04) · quando o objeto se recorta bem | **imagem do objeto em cartão ou tela cheia com câmera viva** (P06/P07) · V03 (P06 em 4 vídeos) · quando a imagem é rica (pintura, cena); variante 3D P23 **[1 vídeo]** |
| **PE** pergunta | **imagem do objeto da pergunta, sem responder**, com câmera viva (P06 ou P07) · regra: pergunta-tese 4/4 em cena (o princípio varia por vídeo) · para a pergunta-tese e a pergunta de crença | **rosto + legenda** · regra em 1 vídeo (V03, 3/3 perguntas curtas do meio) · pergunta curta que abre a resposta | **o termo da crença literal sobre o contexto** (P16) · ocorrência (V04-A21) · para "X deveria ser Y, né?" |
| **AN** anúncio | **rosto + legenda** (5 frases) ou, no nome da série, **rosto + título** (P02; 4 com P02/P03) · regra (4 vídeos; 9 de 14 no rosto) | **recorte do objeto-tema no disco** (P14) · regra em 2 vídeos (V01, V03) · quando o anúncio nomeia o tema | **segue a cena anterior ou arquivo em faixa** (P12) · ocorrência (V04 #7) · abertura de capítulo que muda de época |
| **CR** crença comum | **quem acredita: recortes ou retratos de pessoas** (P14 com recortes, pilha de retratos) · regra em 2 vídeos (V01-A28, V03-A07) | **documento que prova que diziam** (P20) · ocorrência (V04-A20) · quando há jornal ou texto da época | **rosto + legenda** · regra em 1 vídeo (V03 #11, #33) · palavra-resposta curta da crença |
| **CT** contexto | **foto de época do estado de coisas**, pilha (P08) ou cartão (P06) · regra em 2 vídeos (V01-A17, V04-A47) | **rosto + legenda** · ocorrência (V01 #9) · quando a frase abre um capítulo | cena 3D com rótulo de época (P24 + P04) **[1 vídeo]** |
| **DO** descrição de objeto | **imagem do objeto com a câmera percorrendo a descrição** (P06/P07) · regra em 1 vídeo no tipo (V03 #2, #60; P06/P07 juntos em 4 vídeos) | **recorte do objeto + um recorte por palavra concreta** (P16) · ocorrência no tipo (V04-A02; P16 em 4 vídeos) | **lupa no detalhe** (P15, V01-A33) ou, no batismo "se chamava X", contorno à mão (P19, V04-A49) · ocorrências |
| **ME** mecanismo | **disco creme com recortes que encenam cada etapa** (P14) · regra em 2 vídeos (V01, V03; 6 frases) | **lupa ou janela no ponto onde acontece** (P15) · regra em 2 vídeos (V01, V04; 5 frases) | **diagrama chapado que muda de estado a cada frase** (P18; 9 frases, o mais frequente) **[1 vídeo]**; alternativa: objeto que se transforma (P17, V04) |
| **NA** ação narrada | **pilha, um cartão por meia-frase** (P08) · regra em 2 vídeos no tipo (V03, V04; P08 em 3 vídeos) | **recorte que executa a ação** (P16) · V04 (2 frases; P16 em 4 vídeos) | **foto nova empurra a anterior** (P10) · V04 (3 frases; P10 em V03 e V04) · mesmo personagem, ação seguinte |
| **DA** fato com data | **foto ou retrato da época + ano em etiqueta de papel** (P06/P08 + P05) · regra em 2 vídeos no princípio; "ano escrito" é regra em 4 (16 de 21) | **régua de anos + chicote** (P21 + P11) · quando 3 datas ou mais da mesma vida vêm seguidas · regra em 1 vídeo (V01) | ano em rótulo digitado no canto (P04) **[1 vídeo]** |
| **PS** pessoa | **retrato em cartão + etiqueta com o nome** (P06/P05) · regra em 2 vídeos (V03, V04; 4 frases); retrato é regra em 4 | **retrato recortado no disco** (P14, V01-A18) ou **documento da pessoa com o nome marcado** (P20, V04-A40) · ocorrências | rótulo digitado "quem é + de onde" (P04) **[1 vídeo]** |
| **LU** lugar | **mapa sem rótulos, ponto pintado ou circulado, mergulho** (P22) · regra em 2 vídeos (V02, V05) · amostra < 5 | **chicote lateral** (P11) · ocorrência (V03-A13) · quando algo "atravessa" para o lugar | **foto do lugar entra cobrindo** (P10) · ocorrência (V04-A31) · mudança de lugar dentro da história |
| **NU** número | **afastamento que revela a quantidade** (P13) · regra (V03, V04, V05) · quantidade grande | **rosto + legenda** · regra em 2 vídeos contando o V02 (V03 #18, V02 #1) · número curto de choque | **contador ou régua em papel** (P21, V02) ou número digitado (P04, V05) · 1 vídeo cada |
| **LI** lista | **pilha, um cartão por item, na palavra** (P08) · regra em 2 vídeos (V01, V03; 5 frases) | **fila de itens com lente que passa um a um** (P15) · regra em 2 vídeos (V01, V02) | **um recorte por item** (P16) · V02, V04; variante 3D com zoom por item (P23) **[1 vídeo]** |
| **CO** comparação | **o termo comparado entra como recorte ao lado do objeto** (P16) · V04 (2 frases; P16 em 4 vídeos) | **imagem que mostra a comparação, com câmera viva** (P07) · regra em 2 vídeos (V03 #26, V05 #35) | **lado a lado com a diferença visível** (P18, número comparativo) **[1 vídeo]** |
| **CI** citação | **documento real com marca-texto no ritmo da leitura** (P20) · regra (V01, V03, V04; 4 de 8) | **documento entra e é coberto pela imagem do que ele diz** (P10) · regra em 2 vídeos (V03-A15, V04-A37/A38) | **imagem parada com push-in na frase de efeito** (P06) · ocorrência (V05-A25) |
| **VI** negação ou virada | **rosto + legenda** · regra (4 vídeos; 22 de 34) | **imagem única que mostra o fato da virada** (P07/P06) · regra em 2 vídeos (V03 #23, #56, V04 #40) · quando a virada traz um dado concreto | **rosto + texto grande palavra a palavra** (P03) **[1 vídeo]** |
| **EX** exemplo ou prova | **pilha com 2 provas, uma por meia-frase** (P08) · regra em 2 vídeos (V01, V04) | **cartão sozinho com a foto real** (P06) · regra em 2 vídeos (V01, V05) | **cartão que cai por cima da ilustração** (P09) · V05 no tipo (P09 em V01 e V05) · prova rápida no meio de um mecanismo |
| **CQ** consequência | **segue a pilha ou abre cartão novo** (P08) · regra em 2 vídeos (V01, V03) | **prova real cai por cima do diagrama** (P09) · V01 (2 frases) | **recortes de antes × depois** (P16) · V05 e V02 |
| **OP** comentário ou ponte | **rosto + legenda** · regra (V01, V03, V04; 5 de 6) | **segue a cena anterior** · ocorrência (V03 #50) | rosto + texto grande (P03) **[1 vídeo]** |
| **PI** piada | **rosto + legenda** · ocorrência (V04 #26) · amostra < 5 | **rosto + texto grande com o trocadilho escrito** (P03) **[1 vídeo]** | **imagem de época que ilustra a piada** (P08) · ocorrência (V03 #65) |
| **CL** conclusão | **callback: a imagem do gancho volta, agora com o agente agindo** (o princípio é o do gancho) · regra (V01, V03, V05) | **rosto + legenda** · regra (V01, V03, V05; 5 de 12) · última frase ou conclusão parcial | **os elementos do vídeo voam até a imagem-síntese** (P17, V04-A50) ou metáfora desenhada (P19, V03-A31) · ocorrências |
| **CTA** | **rosto + legenda** (V02) **[1 vídeo]** | documento com a frase-chave marcada (P20, V02) **[1 vídeo]** | contador (P21, V02) **[1 vídeo]** · as 4 curiosidades não têm CTA |

---

## 9 · Teste de generalização do mapa

Roteiros inventados, 8 frases cada. Para cada frase: tipo, opção A da seção 8 e com o que as lacunas seriam preenchidas. Nenhuma imagem das referências entra.

### Reel 1 · Claude Code para quem não programa

| # | frase | tipo | opção A e lacunas |
|---|---|---|---|
| 1 | "Olha esta janela preta." | GO | rosto + legenda; na palavra "janela", corte seco para o print real do terminal com o Claude Code aberto, recortado |
| 2 | "Quem usa nunca escreveu uma linha de código." | VI | rosto + legenda |
| 3 | "Então como alguém que não programa coloca um site no ar?" | PE | print do site pronto num cartão de borda clara, inclinado, zoom lento, sem resposta (P06) |
| 4 | "Este é o episódio 4 da série, e hoje o assunto é o Claude Code." | AN | 1ª metade: rosto + título em 2 linhas (P02); 2ª metade (nomeia o tema): ícone do produto recortado no disco creme (B, P14) |
| 5 | "Em 2025, ele chegou primeiro só para quem já programava." | DA | print da página de lançamento num cartão + etiqueta de papel "2025" colada na borda (P06 + P05) |
| 6 | "Você descreve o que quer; ele lê os arquivos, escreve o código e roda o teste." | ME | disco creme com recortes que entram um por etapa, na palavra: pasta de arquivos, trecho de código, sinal verde de teste (P14) |
| 7 | "Um site de cinco páginas sai numa tarde." | NU | afastamento: começa no print de 1 página e recua até as 5 páginas lado a lado (P13) |
| 8 | "Programar virou conversar." | CL | callback: a janela preta do gancho volta e o site abre dentro dela |

### Reel 2 · café especial

| # | frase | tipo | opção A e lacunas |
|---|---|---|---|
| 1 | "Olha este grão." | GO | rosto + legenda; na palavra "grão", corte seco para a foto de um grão cru recortado |
| 2 | "Ele nasce vermelho, dentro de uma fruta, num galho." | DO | foto do galho com frutos maduros em tela cheia; a câmera desce do galho à fruta acompanhando a fala (P07) |
| 3 | "Então por que o café especial custa o triplo?" | PE | pacote de café especial num cartão de borda clara, zoom lento, sem resposta (P06) |
| 4 | "Mas o preço não vem da torra." | VI | rosto + legenda |
| 5 | "Nos anos 1990, provadores criaram uma nota de 0 a 100." | DA | foto de época de uma mesa de prova num cartão + etiqueta de papel "ANOS 1990" (P06 + P05) |
| 6 | "Um quilo leva cerca de 8.000 grãos colhidos à mão." | NU | afastamento que revela a quantidade: um grão no alto encolhe e um monte de grãos cresce embaixo (P13) |
| 7 | "A nota soma aroma, acidez, corpo, doçura e final." | LI | pilha: um cartão por atributo, na palavra (nariz sobre a xícara, fruta cítrica, colher com textura, açúcar mascavo, xícara vazia) (P08) |
| 8 | "Você não paga pelo grão; paga pela nota." | CL | callback: o grão do gancho volta e recebe uma etiqueta com a nota |

O mapa se descreve nos dois temas sem citar nenhuma imagem de referência: as regras são de papel (objeto literal, ano escrito, quantidade visível, virada no rosto), não de conteúdo.

---

## 10 · Confiança e limites

- **Medido:** tempos das frases (transcrição palavra a palavra), o que estava na tela (quadros de entrada e saída das pastas e dos planos), rosto × cena, contagem de pastas por princípio, sincronia (`gatilho_offset_ms`), entrada por corte × dentro do plano (quadro de entrada contra o início dos planos, tolerância de 1 quadro).
- **Classificação minha (leitura):** o tipo de cada frase (sempre leitura; uma frase pode ter dois papéis e recebeu só o principal, com marcas de data, pessoa, lugar, número, lista, citação e comparação para os cruzamentos), a categoria de escolha do conteúdo (seção 4, 1 por pasta) e a divisão das partes do roteiro (seção 7). Tipos com fronteira difusa: anúncio × comentário-ponte × ação narrada nas frases que abrem capítulo no rosto (V01 #25, #45); virada × crença comum (V03 #11).
- **Regras de cálculo:** uma frase "tem" um princípio se a pasta entra nela (palavra-gatilho) ou cobre 50 % ou mais dela. Frases de rosto em que a cena entra na última palavra (V01 #1, V02 #20, V05 #1) foram contadas como rosto. O V02 não tem tabela de cortes separada das panorâmicas: os 13 cortes vieram da lista de eventos da análise.
- **Amostra fraca (menos de 5 frases nas 4 curiosidades):** LU lugar (3), PI piada (3), CTA (0; só no V02). No limite: CT contexto (5), GO, CR, DO, OP (6 cada).
- **Princípios de 1 vídeo** (nunca acima de C): P03, P04, P23, P24 (V05), P12 (V04), P18 (V01). P18 é o princípio mais usado para mecanismo (9 frases), mas só no V01.
- **Sincronia:** no V05 há desvio de até 270 ms em palavra dentro de fala corrida (anotado em V05-A50); no V03, ±40 a 110 ms.

**Dúvidas que só o dono do canal decide:**
1. Viradas: só rosto com legenda (V01, V03, V04) ou rosto com texto grande palavra a palavra (P03, só V05)?
2. Haverá assinatura de série com nome e número de episódio (4 de 4 referências usam), e com título sobre o rosto (P02) ou rosto puro?
3. Mecanismo de temas técnicos (ex.: Claude Code): aceitar o diagrama chapado do V01 (P18) como padrão, apesar de vir de 1 vídeo só?
4. Cenas 3D do V05 (P23, P24) entram no estilo? Se não, o papel delas fica com pilha de fotos, disco com recortes e transformação (tabela de equivalências, seção 3).
5. Os vídeos terminam sem CTA. O canal quer manter assim ou acrescentar um fecho com pedido?
6. Proporção de rosto: a referência fica entre 14 % e 21 % do tempo. Manter essa faixa nos vídeos novos?

---

## 11 · O que o reestudo acrescenta à colocação (2026-11-20)

As 204 notas da biblioteca agora dizem o **tipo de fala** de cada cena e a **leitura de editor** (por que esta cena, este
design e este movimento para esta fala). A colocação por tipo de fala das seções 3 e 8 não mudou. O que o reestudo acrescenta
é **o que a câmera, a legenda e o texto fazem dentro da cena conforme a fala**. Detalhe e números no guia, seção G12.

### 11.1 Tipos de fala registrados nas notas (192 pastas com a linha "Tipo de fala")

| tipo de fala | pastas | | tipo de fala | pastas |
|---|---|---|---|---|
| data (abre capítulo: época + quem + o quê) | 24 | | consequência | 8 |
| mecanismo | 20 | | contexto | 8 |
| ação narrada | 18 | | número | 8 |
| virada | 15 | | conclusão | 8 |
| pessoa (nome + credencial) | 14 | | lugar | 7 |
| lista | 9 | | comparação | 7 |
| descrição | 9 | | pergunta | 4 |
| exemplo | 8 | | gancho, crença, citação | 3 cada |
| anúncio | 8 | | nome, piada, CTA, callback | 1 a 2 cada |

A contagem é por pasta da biblioteca, pela 1ª palavra da linha; uma cena pode juntar dois tipos. Não substitui a tabela de
frases da seção 2, que conta frases.

### 11.2 A fala manda na câmera (regra nos 5 vídeos)

| momento da fala | o que a câmera faz | medido em |
|---|---|---|
| a frase corre, sem palavra de peso | deriva de repouso, +1,4 a +7 %/s | 5 vídeos |
| **palavra-chave** (o nome, o número, o objeto) | pico de aproximação com freio longo: +11 a +61 %/s | V03, V04, V05; saltos no mapa do V02 |
| a fala abre um assunto ou mostra a quantidade | recuo: ×0,5, ou −14 a −44 %/s | V01, V03, V04, V05 |
| virada ("mas", "só que") | aproximação que acelera até o corte: de +4 a +33 %/s | V03 |
| a fala descreve um gesto (traçar, grifar, montar o diagrama) | a câmera para ou quase para enquanto a mão trabalha e retoma depois | V01, V04 |
| a frase termina | não há parada: a câmera segue ou o plano corta em movimento | 5 vídeos |

Para o plano de edição: ao descrever um beat, diga **em que palavra cai o pico** e **onde a câmera para**. Um zoom igual do
1º ao último quadro não existe nas referências como padrão.

### 11.3 A fala manda na legenda

- Corte seco na troca de frase: o bloco novo da legenda entra **no quadro do corte**.
- Plano contínuo ou transição animada: a legenda segue a voz e atravessa a transição (1 a 5 quadros).
- Palavra-chave: costuma ficar **sozinha num bloco** (V04).
- Frase de remate dita no rosto com texto grande (V05): a legenda **some** nesse plano e volta no corte seguinte.
- Número escrito na cena (V02): a legenda some por ≈ 6 quadros.

### 11.4 Confiança

O tipo de fala foi atribuído por 9 agentes, um por lote, lendo a fala e a cena; os nomes dos tipos não foram unificados
palavra por palavra (por isso "mecanismo" e "ação narrada" se sobrepõem). As regras de câmera vêm de medidas com região
restrita e foram conferidas por amostragem (16 de 17 itens dentro de ±10 % no V04 e V05; 4 % de erro no V01, V02 e V03).
Depois da conferência, o fim de cada cena foi remedido nos 9 lotes, porque medir só o começo perdia a 2ª fase.
