# Corte 04 · o reel no treino reestudado (perfil V03, câmera por fases)

Arquivo: `corte-04-com-som.mp4` · 1080x1920 · 23,976 quadros/s · 942 quadros · 39,29 s · 88,7 MB (≈ 18 Mbit/s).
Plano: 2ª rodada do painel, "Siga as sugestões" (`../03-plano/escolhas-r2.md`), perfil de acabamento V03
(`../03-plano/perfil.json`). Cenas: `../05-cenas-r2/` (as do corte 03 continuam em `../05-cenas/`).
Comparação lado a lado com o corte 03, 12 quadros: `comparacao-corte-03-x-04.jpg`.
**Ninguém assistiu ao arquivo em tempo real nem ouviu o som: tudo abaixo é medido em quadros, folhas e funções. O Felipe
precisa assistir.**

## O que é igual ao corte 03 (de propósito)
- Os 11 cortes secos: detectados no arquivo final nos quadros 25, 73, 145, 262, 290, 412, 579, 619, 789, 845 e 888.
- Os gatilhos de todas as peças (impressos antes e depois em cada cena: idênticos) e a composição (quais imagens, onde,
  que tamanho). Rosto em 15,6 % do tempo; 2,8 cortes por 10 s.
- O som: a mesma mixagem do corte 03 (`../07-som/mix.wav`), juntada sem recodificar o vídeo. Medido no arquivo:
  −14,2 LUFS, pico real −0,9 dBTP, faixa de 3,2 LU. Os 4 efeitos caem nos mesmos quadros (223, 358, 382, 619).

## O que mudou · acabamento (perfil V03, medido contra a referência)
| | corte 03 | corte 04 | referência V03 |
|---|---|---|---|
| Mesa | escura com vinheta por cima de tudo | luz central no terço de cima, parada na tela, sem vinheta | lateral do meio 31, base 16 (motor: 31 e 16) |
| Papel | liso | pontilhado fixo + grão vivo sorteado a cada quadro, só sobre as peças | disco: grão 11,4 (motor 10,4) |
| "Ferver" entre 2 quadros | 0 | 12,5 no disco parado | 13,2 |
| Borda do cartão | branca lisa | papel off-white de 12 px (8 px em 720) com fio escuro | 8 px, luma 196–217 (motor 191–207) |
| Sombra | 3 px, em volta | caída para baixo: longa embaixo, média dos lados, some na mesa escura | lateral 31 → 26 (motor 31 → 24–27) |
| Recorte e disco | contorno liso, disco creme do V01 | contorno branco ondulado, disco #ded8cb | #ded8cb (motor #ded8ca) |
| Tarja da legenda | 70 px, raio 12, folga 9, 75 %, cor única | 69 px (46 em 720), raio ≈ 7, folga ≈ 7, 73,5 %, cor do V03 | y 847–892, 46 px, 73,5 % (motor: 847–892, 72,8 %) |
| Vinhetas de cena | no pedido (trecho 7), na parede de slides, no fecho | nenhuma (o véu do trecho 10, pedido do Felipe, ficou) | nenhuma por cima das peças |

Grão no arquivo final (crf 21): 10,35 no disco, contra 10,45 em crf 14. O arquivo em crf 14 dava 206 MB; fiquei com 21.

## O que mudou · câmera de cada cena
A regra usada: primeiro a câmera MEDIDA na referência da cena; onde ela não diz nada sobre aquele momento da fala, a linha
de câmera do painel. Onde as duas se contradizem, vale a referência.

| Cena | Câmera no corte 04 | Painel × referência |
|---|---|---|
| Trecho 2 · três discos | repouso +3,4 %/s; recuo −3,8 %/s com os três na mesa; **pico de +25 %/s em "gratuitas"**; corta andando a +17 %/s | o pico veio do painel (a referência não tem esse momento); o recuo veio da referência |
| Trecho 3 · cédulas | +3,0 %/s na 1ª cédula; +2,6 → +2,0 %/s enquanto o monte se forma; corta andando | **o pico de +30 %/s em "centenas" não entrou**: a referência só aproxima devagar |
| Trecho 4 · pilha de nomes | +6,6 %/s; quase parada na lista (−2,7 e −1,4 %/s); **pico de +13,6 %/s em "Design"**; freio de 0,9 s | pico menor que o da referência (até +29,6) para as etiquetas não saírem do quadro |
| Trecho 5 · print do chat e elipse | +13,5 %/s no deslize; +9,5 e +6,2 durante o traço; +4,1 → +2,5 até o corte | o painel pedia parar no traço; a referência desacelera sem parar: valeu a referência |
| Trechos 7 e 8 · pedido com marca-texto | +2,7 %/s; +2,0 %/s durante as duas varreduras; +1,9 no corte | **o pico de +20 %/s em "apresentação comercial" não entrou**: a referência é quase constante |
| Trecho 9 · parede de slides | recuo que acelera em "todos" até **−33,9 %/s**, freia, para em "prontos" e retoma +3 %/s | o painel pedia −30; a referência mede −34 |
| Trecho 10 · menu e adesivos | +3 %/s; quase para (+0,3 %/s) do 1º ao 2º adesivo; corta andando; o fundo escurece | igual ao painel |
| Trecho 12 · conversa e roteiro | +7,7 → +8,7 %/s; freia para +0,9 %/s quando o roteiro cai em "roteiro" | o painel pedia +3; a referência mede +8 |
| Trecho 13 · carrossel | +0,9 %/s até o empurrão; +3,5 %/s até o corte, andando | sem o pan da referência, que cortaria o maço |
| Trecho 14 · Gamma e Canva | +8 %/s; vira em "pagar"; recuo de −11 a −12,7 %/s a cada logo | **o "pico leve em Canva" não entrou**: na referência o 2º item entra no recuo |
| Trecho 15 · interface | +7,7 → +8,7 %/s contínuo, cartão descendo | o painel pedia +8 constante |

Em todas as cenas, a taxa que sai da função bate com a pedida (tabela em cada `../05-cenas-r2/auditoria-r2-*.md`).

## Ajustes de quadro seguro feitos por causa da câmera nova
- Trecho 5: a âncora passou para o centro da elipse, para ela ficar inteira até o corte.
- Trecho 13: o pivô da última fase mudou para o canto do 2º cartão não sair do quadro.
- Trecho 15: a âncora foi para (500, 700); à direita, a 3ª miniatura corta 13 px a mais que no corte 03.
- Trecho 9: a parede termina ≈ 29 % maior que no corte 03 (menos slides à vista), porque o recuo segue a referência.

## O que NÃO foi conferido, e o que eu faria diferente se você pedir
1. **Movimento em tempo real e som:** só folhas de quadros e medidas. As viradas de câmera (trechos 9, 12 e 14) e a quase
   parada de 1,5 s sobre o print (trecho 12, quadros 690 a 726) precisam do seu olho.
2. **Ênfase da câmera:** três picos que propus no painel não entraram porque a cena de referência não tem pico.
   **Decidido pelo Felipe em 20/11: "Manter como está".**
3. **Grão sobre print branco:** nos prints do Claude (fundo branco) o grão aparece como pontinhos escuros, com cara de papel
   impresso. Dá para tirar o grão só dos prints, se preferir a tela limpa.
4. **Cédulas grandes:** desde o corte 03 as cédulas estão ≈ 63 % maiores que na spec e saem pelas laterais. Não mexi,
   porque você aprovou assim.
5. **Papel do trecho 14:** virou papel pardo pontilhado (o pontilhado do perfil); se parecer lixa, eu suavizo.
6. **Sombra de baixo do V03:** −48 % no contato, contra −32 % na cena de referência usada na comparação (faixa do vídeo:
   −40 a −77 %).
7. **Depois de subir:** a plataforma comprime de novo e o grão enfraquece; igualei ao arquivo baixado da referência.
8. Nada testado em Windows.
