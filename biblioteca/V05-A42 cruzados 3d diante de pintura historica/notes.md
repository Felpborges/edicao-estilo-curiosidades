# V05-A42 · cruzados (3D) diante de uma pintura histórica
- Categoria: P24 · Cena 3D narrativa (provisória do analista: (provisória) cena 3D low-poly com fundo de pintura/foto histórica (cenário-colagem), câmera que aproxima, ação de quebra)
- Fonte: V05 quadros f3012–f3111 (125,63–129,76 s; 100 quadros ≈ 4171 ms) · 23,976 fps
- Fala: "Crusaders sacked Constantinople in 1204, shattering the snail trade."
- Tipo de fala: data
- Gatilho: entra por corte seco em f3012 (125 625 ms), 15 ms antes do início da palavra nº 416 "Crusaders" (125 640 ms). Conferido: dif 28,4 em f3012 (candidato) e legenda "Crusaders sacked".
- Quadro-chave: f3090
- Camadas ativas: b-roll 3D | grafismo (V05-A43 data) | legenda | som estéreo no começo (fim do efeito de A41)
- Leitura dos strips: strip.jpg = quadros f3010 a f3045, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 36 células. strip-geral.jpg = quadros f3010 a f3111 (amostrado). detalhe-pintura-fundo-personagens.jpg = quadro f3090, região x0 y40 720x560 px, ampliada 1× sem suavizar (pintura histórica ao fundo, personagens 3D na frente, data no topo).

## LEITURA DE EDITOR
- Por que esta cena aqui: um evento histórico datado (saque + ano) que acaba com o ofício; o editor junta os agentes do evento e a vítima do ofício e põe ATRÁS deles uma pintura real do próprio evento: a cena 3D ganha a "prova" de época.
- Por que este design: personagens 3D na frente, pintura histórica de fundo cobrindo toda a metade de cima; data grande no topo entre as cabeças (A43); o objeto do ofício em 1º plano para ser quebrado.
- Por que estas cores: pintura em tons quentes de óleo envelhecido, cruz vermelha e cota de malha cinza nos agentes, avental na cor-tema no personagem do ofício.
- Por que estes efeitos: vinheta moderada (borda a 41 %, a mais leve das cenas 3D deste trecho), porque o fundo já é uma pintura escura.
- Por que este movimento: a pintura DESCE como um painel e cobre o cenário na palavra do evento ("sacked"), depois push-in leve; a quebra do objeto cai na palavra "shattering".
- Sensação do movimento: invasão: o fundo "cai" sobre a cena como uma cortina de guerra; o resto é contido e a quebra é seca.

## FORMA (fixa: reproduzir igual)
- Design: dois personagens low-poly (os agentes do evento, com o figurino da época) e um personagem do ofício com o objeto que vai ser destruído (com o material na cor-tema) em 1º plano; ao FUNDO, em vez de cenário 3D, uma PINTURA histórica do evento (colagem de imagem real atrás dos personagens), tom sépia-avermelhado; chão em tom vinho; base #2a1512 (f3100, x360 y1150, medido). Vinheta.
- Movimento (dif global, medido):
- Passos internos:

| passo | quadros | duração | tipo | curva (dif) | gatilho |
|---|---|---|---|---|---|
| fundo troca do cenário 3D para a pintura + aproximação | f3016–f3041 | ≈ 26 q ≈ 1084 ms | NÃO é dissolve (remedido, folha f3016–f3025 de 1 em 1): a pintura do evento DESCE pelo topo como um painel inclinado e cobre o cenário 3D em 4 q (f3018 só a borda de cima, f3019 até ≈ 1/3, f3021 cobre tudo); em seguida um dos agentes entra andando pela esquerda (f3026–f3036); push-in leve o tempo todo: ×1,005 → ×1,009 → ×1,019 (pico f3030–f3036, por 4–6 q) → ×1,005, ≈ ×1,06 no total de f3018 a f3060 (registro de pontos) | 8 → 14 (patamar f3023–f3027) → 10 → 6 | o verbo da ação (#417, 126 140 ms): f3019 = 125 917 ms, −223 ms |
| data (ano de 4 algarismos) | f3059–f3066 | ver A43 | | | o ano dito (corrigido na conferência: era f3063–f3066 e o ano citado) |
| o objeto é quebrado | f3078–f3085 | 8 q ≈ 334 ms | ação (estilhaços) | 10–11 → 6 | o verbo da consequência (#421, 128 480 ms): f3078 = 128 378 ms, −102 ms (corrigido na conferência: a coluna gatilho trazia as palavras citadas) |

- Saída: corte seco em f3112 (dif 41) para A44.
- Ritmo: 4,2 s; um evento a cada ≈ 1,2 s (fundo, data, quebra).
- Som: canal lateral ativo até ≈ 126,1 s (f3023): o efeito estéreo que começou na palavra da virada (A41) termina no começo desta cena.
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)

- Textura (reestudo 20/11):
  - pintura de fundo: pintura a óleo antiga fotografada (pinceladas, verniz amarelado) · #564332 · grão 7,12 · manchas 12,22 · ac1 +0,55 · anda com a câmera (a correlação com f3098 cai a +0,20 porque os personagens na frente se mexem).
  - personagens: cota de malha com textura fotográfica de metal (repetida), túnica clara lisa com cruz vermelha chapada, roupa marrom lisa, avental na cor-tema com trama; cabeças: escultura realista (agente) e retrato pintado (artesão).
- Efeitos (reestudo 20/11): vinheta global moderada (100 → 98 → 86 → 61 → 41 % da luma; nitidez → 54 %; `borda` f3090); a pintura de fundo é tão nítida quanto os personagens (sem profundidade de campo); a entrada da pintura é um painel inclinado que desce pelo topo em 4 q (remedição); estilhaços na quebra (f3078–f3085); sombra, halo, aberração, grão de filme: nenhum (medido em f3090).
- Câmera (reestudo 20/11): 2 fases: push-in leve, ≈ ×1,06 de f3018 a f3060 (remedição) e depois quase parado: +1,1 %/s (f3042→f3060) e +1,0 %/s (f3090→f3110, o deslize e o giro medidos ali vêm dos personagens). 3 pares na correção (região x40 y200 640x580, sem a data nem a legenda): começo +2,9 %/s (f3014→f3026, 167 de 600 pontos, durante a descida do painel), meio +1,0 %/s (f3055→f3067, 514 pontos), fim +1,2 %/s (f3095→f3110, 539 pontos).
- Cadência (reestudo 20/11): 24 imagens/s (o painel desce com um estado novo a cada quadro; a quebra é contínua).
- Legenda nesta cena (reestudo 20/11): tarja 68 % (direta na correção: f3060 65 % em cima e 69 % embaixo, fundo 128; f3090 61/71 %, fundo 130/105; 51 px, y 809–859; o 62 % era a estimativa do censo, que oscila com a roupa clara e escura atrás) (corrigido na conferência: era 62 %), texto #f0ea15, 28 px (34 com descendente), centro y 65,4 %; 5 blocos de 1 a 3 palavras: o 1º entra no corte, o 3º traz o ano e o 5º ATRAVESSA o corte de saída (corrigido na conferência: eram as falas entre aspas) (f3091–f3114, 3 q dentro de A44); outro texto: a data no topo (A43), longe da legenda.

## CONSTRUÇÃO
1. fundo inicial: cenário 3D da cena anterior (0–250 ms).
2. painel da pintura histórica do evento: desce pelo topo inclinado e cobre a metade de cima em 4 q (+250 → +375 ms); depois fica atrás de tudo, nítida, tons quentes.
3. agente 1 (figurino do evento, cota de malha) à esquerda, braço erguido; agente 2 entra andando pela esquerda de +584 a +1001 ms.
4. personagem do ofício à direita, com o objeto do ofício (material na cor-tema) em 1º plano.
5. quebra do objeto com estilhaços de +2753 a +3087 ms (no verbo da consequência; corrigido na conferência: era a palavra citada).
6. data no topo (A43) a partir de +1960 ms, completa em +2252 ms.
7. vinheta moderada (borda 41 %).
8. câmera: push-in ≈ ×1,06 de +250 a +2002 ms (pico de velocidade ≈ +1,9 %/4 q por volta de +800 ms), depois +1 %/s.
9. legenda amarela V05-L01.
- Linha do tempo (ms a partir do corte): 0 corte seco · +250 a pintura começa a descer (−223 ms do verbo da ação) · +375 pintura cobre o fundo · +584 agente 2 entra · +1960 data começa · +2753 quebra (−102 ms do verbo da consequência; corrigido na conferência: eram as palavras citadas) · +4171 corte seco (legenda atravessa).
- Parâmetros que dependem do conteúdo: a pintura real do evento; os figurinos dos agentes; o objeto que é destruído.
- O que NÃO fazer: dissolver o fundo (é um painel que desce); pôr a pintura desfocada; esquecer a vítima do ofício com a cor-tema.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "os agentes do evento histórico" (personagens 3D); "imagem de época do evento" (fundo); "o objeto que simboliza o que foi destruído" (a quebra).
- Nesta referência as lacunas foram preenchidas com: cruzados; pintura do saque de Constantinopla; a bacia de tinta quebrada ("shattering the snail trade").
- Receita de tratamento de cada imagem: personagens 3D low-poly na frente; pintura histórica real como fundo plano, em cor natural de óleo envelhecido, sem dessaturar (alinhado ao reestudo); objeto que quebra com estilhaços.
- Regra de escolha: evento histórico literal + metáfora (o comércio "despedaçado" vira objeto despedaçado).
- Receita de tratamento (reestudo 20/11): pintura histórica real do evento, em cor natural de óleo envelhecido, nítida, como fundo da cena 3D; vinheta moderada.
- Receita de ILUSTRAÇÃO (reestudo 20/11): 3D low-poly "colagem" (texturas fotográficas: cota de malha, tecido; cabeças de escultura/retrato) diante de uma pintura real; sem contorno.
- Teste de generalização: reel sobre Claude Code → hackers 3D diante de uma pintura/foto real de um ataque famoso, um servidor na cor-tema é quebrado na palavra "derrubou"; reel sobre café → soldados diante de uma pintura de uma revolução, uma saca na cor-tema é rasgada na palavra "destruiu".

- Confiança: tempos e dif medidos; troca de fundo remedida quadro a quadro: painel que desce pelo topo em 4 q (alinhado ao reestudo).
