# Decisões do autor (e o que o usuário pode mudar)

O treino foi feito por Felipe Borges (canal @FelipeBorgesFalaIA) sobre 5 reels de referência. Onde o guia diz "o Felipe",
é o autor do método. **Estas são as escolhas dele; elas vêm marcadas por padrão, mas o usuário desta skill manda no vídeo
dele.** Se o usuário pedir diferente, siga o usuário e diga o que mudou na forma.

## A · Regras que valem sempre (não negocie sem o usuário pedir)
1. **Forma fixa, conteúdo variável.** O corte fica "extremamente igual" às referências em estilo, design, edição e ritmo; o
   que muda é o tema do usuário. Nenhuma imagem, ilustração ou asset de referência entra no vídeo final.
2. **Toda edição passa pelo painel de plano de edição.** Antes de construir qualquer corte: abrir o painel e parar para o
   usuário escolher. **Três opções em cada trecho, sempre, e a sua recomendação marcada** ("Minha sugestão").
3. **Qualidade antes da velocidade.** Corte automático em minutos foi reprovado pelo autor. Medir, construir cena por cena,
   auditar quadro a quadro. Tempo esperado: ≈ 1 h por reel.
4. **Nada fica só 1 segundo em tela** (piso de leitura, `folha-de-tempos.md` seção 3).
5. **A câmera medida na referência manda.** Não acrescente ênfase de câmera por conta própria.
6. **Máquina comum (16 GB):** um comando pesado por vez, sempre pela trava `ferramentas/leve.py`. Subagentes em paralelo só
   para ler/escrever, nunca para render, ffmpeg, whisper ou remoção de fundo.
7. **Diga o que não foi verificado** ao entregar (Windows e Linux não foram testados pelo autor).

## B · Escolhas adotadas (o usuário pode trocar)
| tema | adotado pelo autor |
|---|---|
| Perfil de acabamento | **V03** marcado por padrão; troca por vídeo no topo do painel; dentro de um vídeo é um só |
| Som | só a voz (≈ −14 LUFS); no máx. 4 efeitos de foley baixos, "sem muito efeito para não ficar exagerado", parecidos com os da referência; sem música |
| Piso de leitura | cena ≥ 1,5 s · texto parado ≥ 700 ms · imagem de série ≥ 1,2 s · último item de lista ≥ 700 ms · rosto fora do piso |
| Pausas no corte | ≈ 90 ms no meio da frase, ≈ 110 ms no fim de frase (a referência deixa 80 a 110) |
| Legenda | 1 a 3 palavras, amarela, tarja a ≈ 67 % da altura, tamanho da referência (37,5 px em 1080); número em algarismo |
| Imagem de arquivo | é o TEMA do usuário, não o estilo: a forma é o tratamento (cartão, borda, mesa escura, recorte) |
| Cenas 3D (P23, P24) | só opção, quando o tema não tem imagem real; sem ferramenta definida |
| Texto grande (P03) e rótulo digitado (P04) | só opção (existem só em 1 dos 5 reels) |
| Assinatura de série (P02) | sem série, P02 não tem uso |
| Marcação à mão | amarelo-ouro sempre |
| Diagrama chapado (P18) | opção para mecanismo; cores do tema, em aberto |
| Fecho | sem CTA e sem cartela, igual à referência; CTA só no rosto, se o roteiro tiver |
| Recorte | com contorno de adesivo (de tesoura, ondulado) |
| Cadência de imagens | 24/s |

## C · Princípios que existem em poucos vídeos = opção, não padrão
O que só aparece em 1 dos 5 vídeos de referência (P03, P04, P12, P18, P23, P24 e a cadência de 12 imagens/s) é **opção**,
nunca padrão. Algo que aparece 1 vez é "ocorrência", não "regra".

## D · Dúvidas que o autor nunca respondeu
`duvidas-e-baixa-confianca.md` (G11) lista 27 dúvidas e os pontos de baixa confiança, cada um com a alternativa. Se uma
delas decidir o vídeo, pergunte ao usuário no painel (como uma das 3 opções) em vez de decidir sozinho.
