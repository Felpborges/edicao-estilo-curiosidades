# V05-A17 · objeto salta da mão para a câmera, com rótulo de nome
- Categoria: P24 · Cena 3D narrativa (provisória do analista: (provisória) objeto citado salta para o primeiro plano (escala gigante) e volta; rótulo de nome digitado)
- Fonte: V05 quadros f1054–f1095 (43,96–45,67 s; 42 quadros ≈ 1752 ms) · 23,976 fps
- Fala: "(called the) murex. So the snail (is purple…)"
- Tipo de fala: mecanismo (nome do objeto: "chamado X")
- Gatilho: o objeto começa a crescer em f1054 (43 966 ms), 114 ms antes do início da palavra nº 161 "murex." (44 080 ms). Conferido no `perfil` (dif 2 em f1053 → 4 em f1054 → 7 → 16 → 29 em f1057) e no strip.
- Quadro-chave: f1062
- Camadas ativas: b-roll 3D (A15) | grafismo (objeto em escala gigante + rótulo) | legenda
- Leitura dos strips: strip.jpg = quadros f1052 a f1075, de 1 em 1, 8 colunas, da esquerda para a direita, linha a linha; 24 células. strip-saida.jpg = quadros f1088 a f1097, de 1 em 1, 8 colunas; 10 células. detalhe-meio-do-salto-f1056.jpg = quadro f1056, região x0 y150 720x900 px, ampliada 1× sem suavizar (meio do salto: objeto nítido, sem borrão de movimento; a 1ª letra do nome já aparece fraca). detalhe-superficie.jpg = quadro f1062, região x230 y180 240x240 px, ampliada 2× sem suavizar (superfície do objeto: relevo, brilho úmido, sujeira). detalhe-nome-digitando-f1061.jpg = quadro f1061, região x90 y760 140x50 px, ampliada 3× sem suavizar (nome em digitação: 2 letras cheias, as seguintes em degradê).

## LEITURA DE EDITOR
- Por que esta cena aqui: na palavra do nome do objeto, ele salta da mão do personagem para a cara do espectador: o nome técnico ganha imagem e escala.
- Por que este design: o objeto em close gigante sangrando as 4 bordas (87 × 88 % do quadro) e o nome numa palavra só, em sans bold branca, no canto inferior esquerdo, logo acima da legenda.
- Por que estas cores: o objeto em cor natural quente (#7a583b na superfície, brilho dourado) sobre o fundo sépia escuro; nome branco.
- Por que estes efeitos: a vinheta continua por cima do objeto (borda 27 %), então ele parece estar "dentro" da cena, iluminado pela mesma luz quente lateral; brilho úmido e relevo mostram que é real.
- Por que este movimento: estalo: cresce em 4 q a partir da mão e freia em 4 q, fica ≈ 0,25 s parado e volta à mão em 5 q; o nome sobrevive ao objeto e só apaga depois.
- Sensação do movimento: "olha isso de perto!" e devolve; produzida pela escala com pico de dif 29 no 4º quadro, freio curto e volta com estalo (dif 32 → 1 em 5 q).

## FORMA (fixa: reproduzir igual)
- Design: o objeto que o personagem segura cresce até SANGRAR as 4 bordas do quadro: em f1062 as pontas tocam x0 e x720 e o objeto é cortado em cima (y0) e embaixo (y1280) (remedido, observado no still f1062); a parte clara do objeto (matiz 15–50°, saturação ≥ 0,3, brilho ≥ 0,45) ocupa x48–674 y39–1171 (87 % × 88,5 % do quadro, centro 50 %, 47 %) (remedido, f1062; antes "x110–647 y103–1130, 74,6 % × 80,2 %": as pontas escurecidas pela vinheta ficavam fora da caixa); fica NA FRENTE do personagem e da legenda não (a legenda amarela continua por cima). Iluminação quente lateral, sombra interna marrom #5e3c27 (f1062, x200 y200). Rótulo de nome: palavra única em sans bold branca, x100–213 y771–800 (15,8 % × 2,3 %; esquerda em 13,9 %, y 60–62,5 %) (medido), sem linha cinza, sobre o canto inferior esquerdo do objeto.
- Movimento:
- Passos internos:

| passo | quadros | duração | tipo | curva (dif) | gatilho |
|---|---|---|---|---|---|
| objeto cresce da mão até gigante | f1054–f1057 (assenta ≈ f1061) | 4 q de salto + 4 de freio ≈ 334 ms | escala a partir da posição da mão, para o centro | 4 → 7 → 16 → 29 (pico f1057) → 13 → 9 → 8 → 6 | o nome do objeto (#161) −114 ms |
| objeto parado grande (deriva lenta) | f1062–f1067 | 6 q ≈ 250 ms | quase parado | 3 | — |
| rótulo do nome (1 palavra, 5 letras) digitado | f1056–f1065 | 10 q ≈ 417 ms (remedido; antes f1060–f1065, 6 q) | letras da esquerda para a direita, cada uma com fade e desfoque: f1056 1ª letra fraca e borrada, f1059 3 letras, f1061 as 5 letras com as 2 últimas fracas, f1065 nítido (folha recortada); cada letra leva 5 q (≈ +20–25 %/q), 1 letra nova por quadro (medido por letra na correção) | — | o nome do objeto −36 ms (f1056 = 44 044 ms) |
| objeto volta para a mão | f1068–f1072 | 5 q ≈ 209 ms | escala inversa, rápida no começo (estalo) | 32 (f1068) → 15 → 7 → 3 → 1 | fim do nome falado (44 600 ms): f1068 = 44 550 ms |
| rótulo fica sozinho | f1072–f1092 | 21 q ≈ 876 ms | parado | — | a frase seguinte (3 palavras) |
| rótulo apaga | f1093–f1097 (corrigido na correção: era f1093–f1095) | 5 q ≈ 209 ms (corrigido: era 3 q) | apaga da esquerda para a direita (1276 → 760 → 462 → 0 px claros; por letra 100 → ≈ 75 → ≈ 45 → ≈ 15 → 0 em 4 q, 1 letra por quadro, vazio em f1098) | — | o verbo da pergunta seguinte (#165) |

- Ritmo: o objeto fica gigante só ≈ 0,46 s (f1057–f1067, 11 q; assentado de f1062 a f1067, 6 q ≈ 250 ms) (remedido; antes "≈ 0,6 s"); o nome sobrevive ao objeto por ≈ 0,9 s.
- Som: nenhum efeito detectado (lateral −120 dB).
- (passada de vazamento, 2026-11-20: termos de conteúdo da referência trocados pelo PAPEL; medidas intactas)
- Textura (reestudo 20/11):
  - Objeto: família foto/render realista de concha. Superfície `textura` f1062 região 160,560,90,140: #7a583b, grão 5,7, manchas 23,0, ac1 +0,75 / ac2 +0,34 (relevo largo e sujeira); interior (380,320,140,140): #4c321e, grão 1,4, liso e escuro; f1062 × f1064 anda junto (correlação alinhada +0,88). Detalhe f1062: estrias de crescimento, pontas, manchas de sujeira e reflexo úmido especular; luz quente vinda da esquerda.
  - Fundo: o mesmo de A15 (sépia desfocada).
- Efeitos (reestudo 20/11): vinheta por cima do objeto (`borda` f1062: luma 100 · 87 · 70 · 48 · 27 %; nitidez cai junto); brilho especular úmido no próprio objeto (é do material, sem halo). Sem sombra projetada no fundo, sem contorno, sem desfoque de movimento no salto (detalhe f1056: bordas nítidas a meio caminho). Sem grão de filme.
- Câmera (reestudo 20/11): a câmera da cena segue parada; o que se mexe é o objeto (escala a partir da mão). Durante o "parado grande" (f1062→f1067) o objeto ainda deriva ×1,020 (+0,40 %/q) e gira +0,25°/q: não congela.
- Cadência (reestudo 20/11): 24 imagens/s (dif do salto muda em todos os quadros, nota antiga; o nome avança 1 letra por quadro).
- Legenda nesta cena (reestudo 20/11): a legenda amarela fica POR CIMA do objeto gigante (o bloco com o nome do objeto visível sobre o objeto no still), tarja ≈ 66–70 %; o nome do objeto (y771–800) fica 9 px acima da tarja (topo ≈ y809), alinhado à esquerda em x99, e repete a palavra que a legenda está mostrando (o nome aparece na legenda e no rótulo ao mesmo tempo: ênfase dupla). Blocos: o nome com o artigo f1047–f1073, 3 palavras f1074–f1087, a pergunta de 4 palavras f1088–f1121; o nome apaga no início do último.
- Entrada do texto (reestudo 20/11): nome, 1 palavra de 5 letras: 1ª letra fraca já em f1056 (detalhe), p98 na caixa f1057 95 · f1058 134 · f1059 170 · f1060 209 · f1061 250 (1ª letra em fade de ≈ 5 q); borda direita f1060 x129 · f1061 153 · f1062 169 · f1063 191 · f1064 213 (completo); opacidade por letra (medido na correção: miolo de cada letra × anel de fundo local no mesmo quadro, com a máscara da letra tirada do quadro completo): 1ª f1056 3 · 15 · 33 · 56 · 80 · 99 (f1061); 2ª f1058 13 · 30 · 53 · 79 · 100 (f1062); 3ª f1059 11 · 29 · 51 · 75 · 99 (f1063); 4ª f1060 8 · 21 · 42 · 75 · 99 (f1064); 5ª f1061 11 · 25 · 50 · 77 · 100 (f1065): cada letra leva 5 q (≈ +20–25 %/q), 1 letra nova por quadro; f1056–f1065 = 10 q (corrigido na conferência: era fade+desfoque de ≈ 4 q por letra e fim em f1064). Saída: apaga da esquerda para a direita em 5 q, f1093–f1097 (por letra: 1ª 72 → 43 → 14 → 0; 5ª 98 → 78 → 50 → 15 → 1, f1094–f1098), vazio em f1098 (corrigido na correção: era 3 q, f1093–f1095, pela contagem de pixels claros). Letra (f1070): sans bold, maiúscula 30 px (y771–800), altura-x 22 px (y779–800), haste 5 px → 0,23; largura 114 px ÷ 5 ÷ 22 = 1,04; cor #fff9f4. O nome é MAIOR que o dos rótulos de canto (maiúscula 30 × 24 px): é o mesmo corpo do nome no mapa (A13).

## CONSTRUÇÃO
1. cena A15 por baixo (parada).
2. objeto: foto/render realista do objeto citado, recortado, cor natural quente, luz lateral da esquerda; parte do mesmo objeto que o personagem segura (a escala sai da posição da mão: x ≈ 33 %, y ≈ 36 %).
3. vinheta da cena POR CIMA do objeto (borda 27 %).
4. animação do objeto (ms a partir de f1054, 114 ms antes da palavra do nome): 0–167 ms escala da mão até 87 × 88 % do quadro, ease-in (dif 4 → 29), centro indo para (50 %, 47 %); 167–334 ms freio (dif 13 → 6); 334–584 ms quase parado com deriva +0,4 %/q e giro +0,25°/q; 584–792 ms volta para a mão, ease-out invertido (estalo: mais rápido no 1º quadro).
5. nome: sans bold, maiúscula 30 px, altura-x 22 px, branco #fff9f4, alinhado à esquerda em x99 (13,8 %), base em y800 (62,5 %, logo acima da tarja); digitado de 83 a 459 ms (1 letra nova por quadro, cada letra 15 → 33 → 56 → 80 → 100 % em 5 q, com desfoque); fica até ≈ 1626 ms; apaga da esquerda para a direita em 209 ms (cada letra 100 → 72 → 43 → 14 → 0 em 4 q, 1 letra por quadro) (corrigido na conferência: era fade de ≈ 4 q por letra, completo em 417 ms e saída em 125 ms).
6. legenda amarela por cima de tudo.
- Linha do tempo (ms a partir de f1054): 0 começa o salto · 83 1ª letra do nome · 167 pico · 334 assentado · 459 nome completo (corrigido na correção: era 375) · 584 volta · 792 objeto na mão · 792–1626 nome sozinho · 1626–1835 nome apaga (vazio em f1098; corrigido na correção: era 1626–1752).
- Parâmetros que dependem do conteúdo: o objeto (foto/render de alta resolução para o close), a palavra do nome, a posição da mão.
- O que NÃO fazer: não pôr o objeto acima da legenda; não tirar a vinheta do objeto; não usar borrão de movimento; não deixar o objeto grande por mais de ≈ 0,5 s; não usar linha cinza nesse rótulo (é 1 palavra só); não apagar o nome junto com a volta do objeto.

## CONTEÚDO (variável: muda a cada vídeo)
- Lacunas: "o objeto que acabou de ser nomeado" ; "nome do objeto" (rótulo).
- Nesta referência as lacunas foram preenchidas com: a concha do murex / "Murex".
- Receita de tratamento de cada imagem: o mesmo objeto 3D (ou foto recortada do objeto real) da cena, com detalhe alto e cor natural, iluminação quente lateral; nenhum contorno; aparece em escala gigante sem moldura.
- Regra de escolha: nomeação. Quando a fala dá o NOME de uma coisa nova ("called the murex"), a coisa salta para a câmera e o nome é escrito na tela.

- Receita de tratamento de cada imagem (reestudo 20/11): foto/render do objeto real em cor natural, luz quente lateral, recortado, sob a vinheta da cena; detalhe alto (relevo, brilho do material).
- Receita de ILUSTRAÇÃO (reestudo 20/11): objeto 3D/foto realista sem contorno nem sombra; revelado por escala explosiva a partir da mão do personagem e devolvido.
- Teste de generalização: reel sobre Claude Code: "um modelo chamado Claude" → o personagem segura um chip e ele salta até encher a tela, com "Claude" digitado à esquerda. Reel sobre café: "uma fruta chamada cereja do café" → o pastor segura a fruta, ela salta para a câmera, "Cereja" digitado.

- Confiança: tempos e caixas medidos; "volta para a mão" observado no strip; a ordem "na frente da cena, atrás da legenda" observada.
