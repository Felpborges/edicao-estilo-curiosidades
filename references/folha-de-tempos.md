# Folha de tempos: quanto dura cada coisa (consulta rápida)

Resumo operacional de `tempos-e-ritmo.md` (G7), `rosto-cena-abertura-fecho.md` (G8–G9), `movimento.md` (G6) e
`acabamento-perfis-camera-legenda.md` (G12), mais as decisões já adotadas pelo autor. **Medido** = contado nos 5 reels de
referência; **adotado** = decisão do autor para a edição (você pode mudar, ver `decisoes-do-autor.md`). Margem das medidas:
±1 quadro nos tempos, 1 a 3 quadros nos gatilhos de início de frase. Para número exato, abra o guia na seção citada.

## 1 · Ritmo geral (medido)
| o quê | valor |
|---|---|
| Fala | 3,2 a 3,4 palavras/s; pausa mediana entre frases 80 a 110 ms (máx. 190 a 320 ms) |
| Cortes secos | 2,1 a 2,6 por 10 s (no exemplo: 2,8 por 10 s e 7,1 por 100 palavras) |
| Eventos visuais (corte, peça nova, passo interno) | 7 a 10 por 10 s; um evento novo a cada 0,75 a 1,13 s |
| Duração de plano (corte a corte) | mediana 2,4 a 3,6 s; mais curto 0,5 s (só rosto: virada de 2 a 3 palavras); mais longo 12 a 17,5 s |
| Rosto × cena | tela cheia 79 a 86 % · rosto 14 a 21 % (rosto puro 8 a 20 %) |
| Curva ao longo do vídeo | **respira em ondas**: adensa em mecanismo/lista, alonga em narrativa/callback; não acelera sempre |
| O que NUNCA há | dissolve ou fade entre planos · fade para preto, flash, wipe · punch-in/zoom/troca de ângulo no rosto · palavra destacada ou animada na legenda · ícone, emoji ou seta gráfica |

## 2 · Sincronia com a fala (medido; o que mais pesa na sensação de "igual")
- **A imagem entra junto ou um pouco ANTES da palavra que ilustra:** mediana **−38 ms** (p10 −137, p90 +106). Dos 192
  casos: 92 antes (< −40 ms), 68 junto (±40 ms), 32 depois.
- **Corte seco** (rosto ↔ cena): cai **≈ 42 ms (1 quadro) antes da 1ª palavra** da frase.
- **Reconfira o início das palavras no áudio** (`motor/ataques.py`): o whisper adianta inícios de frase em 1 a 3 quadros.
- Lista → **uma peça por item falado**. Mecanismo → **um passo por frase**. Todo dado concreto (data, nome, número, lugar,
  citação, objeto) vira imagem (123 de 128 frases na referência); anúncio, pergunta, virada e conclusão ficam no rosto.
- **Legenda:** bloco novo entra inteiro no 1º quadro (sem animação), junto da 1ª palavra (entre −60 e +50 ms); em corte
  seco a troca cai no quadro do corte; as peças passam por BAIXO da tarja e a tarja não acompanha a câmera.

## 3 · Quanto cada arte fica na tela
| arte | tempo na tela (medido na referência) | piso adotado |
|---|---|---|
| Cena de tela cheia (cartão, recorte, disco, documento) | mediana 2,6 a 3,9 s · mín. 1,0 s · máx. 6 a 12 s. Só 4,1 % das cenas ficam abaixo de 1,5 s e nenhuma abaixo de 1,0 s | **≥ 1,5 s** |
| Peça de série (pilha, colagem, lista) | peças de pilha ficam 0,75 a 1,1 s antes de serem cobertas; a referência solta um cartão a cada ≈ 1,2 s | **≥ 1,2 s por peça** |
| Texto ou etiqueta parado depois da última palavra | etiquetas ≈ 0,46 a 1,3 s; texto grande (V05, só opção) 0,29 a 0,71 s | **≥ 700 ms** |
| Último item de uma lista, parado antes do corte | 0,2 a 1,6 s (os que ficam abaixo de 0,7 s são exceção) | **≥ 700 ms** |
| Marca-texto / elipse à mão (traço) | traço avança no tempo da fala; passo a 12 imagens/s | vale a fala |
| Legenda (1 a 3 palavras por bloco) | mediana 540 a 790 ms por bloco | fora do piso (é fala transcrita) |
| Rosto | planos de 0,5 a 1 s existem (viradas de 2 a 3 palavras e a abertura) | fora do piso |

**Regra do autor:** "nada pode ficar só 1 segundo em tela; não dá tempo de ler, de entender a imagem, de ler o texto."
A câmera também não pode tirar da tela, antes de dar para ler, algo que acabou de entrar.
**Se a fala do usuário for mais rápida que a referência** (o exemplo tem 3,95 palavras/s), NÃO estique a cena: esticar
empurra a entrada da seguinte para depois da palavra. Junte as peças curtas num plano contínuo (deslize ou empurrão), como a
referência faz, ou reduza o número de peças.

## 4 · Entradas e movimentos de peça (medido; ver `movimento.md` G6 e `molde-do-motor-00-globais.md`)
- **Estalo do cartão:** 4 quadros a 24 fps (≈ 167 ms), em **degraus de 2 quadros**: q1–q2 ×1,12 e giro a mais (+3,5°),
  q3–q4 ×1,04 (+1°), q5 assentado. **Não interpola.** (`base.estalo`)
- **Disco que nasce:** 3 quadros, um valor por quadro (0,49 → 0,81 → 1,0), 125 ms. (`base.pop_disco`)
- **Giro do cartão:** 1,5° alternando o sentido de um cartão para o seguinte (pilhas até ±5°).
- Troca entre cenas: a maioria é por **movimento** (empurrão, cobertura, chicote, pilha que cresce), não por corte.
- Fade só em elemento (etiqueta, texto), nunca em troca de plano.
- Cadência: 24 imagens/s (perfil V03 e V04). O perfil V01 desenha a cena a 12 imagens/s; o rosto e a legenda ficam a 24.

## 5 · Câmera (medido; `acabamento-perfis-camera-legenda.md` G12.3)
A câmera quase nunca para e **não é um zoom linear do 1º ao último quadro**: cada cena tem FASES amarradas à fala.
1. **Repouso:** deriva lenta, +1,4 a +7 %/s.
2. **Pico na palavra-chave, com freio longo:** começa ≈ **135 ms DEPOIS** do início da palavra-chave; +11 a +61 %/s
   (V03 até +54, V04 +44 a +61, V05 +11 a +40).
3. **Recuo que abre o assunto:** −14 a −44 %/s (V04), −7,5 %/s no recuo final (V01).
4. **Aceleração até o corte** nas viradas: +4 a +33 %/s.
5. **Pausa enquanto a mão ou a ferramenta trabalha** (traço, marca-texto) e durante enumeração: a câmera para ou quase para.
6. Pode **cortar andando**; não force parada no último quadro.
7. **Quem manda:** (1º) a câmera MEDIDA na `notes.md` da Ref da cena escolhida; (2º) a linha "Câmera" que o usuário aprovou no
   painel; (3º) a regra geral acima. Não acrescente ênfase de câmera por conta própria (decisão do autor no corte 04).
8. **Quadro seguro:** com a câmera, confira no último quadro e no fim de cada pico que o conteúdo citado na fala continua
   inteiro e legível.

## 5b · Acabamento (perfil, ver `acabamento-perfis-camera-legenda.md` G12.2)
Um perfil por vídeo, inteiro, sem misturar: **V03 (padrão, "mundo de papel")**, V01, V04. Luz da mesa, grão vivo do papel,
pontilhado, borda do cartão, sombra, contorno do recorte, cadência e tarja da legenda vêm do mesmo reel. O rosto fica fora
do acabamento (sem vinheta, sem grão, sem luz de cena). Detalhe numérico em `perfis.py` (o motor já aplica).

## 6 · Abertura e fecho (medido; G9)
- Abre no **rosto por 0,7 a 1,3 s** com "olha isto", **corta seco para o objeto** na palavra que o descreve.
- Fato contraintuitivo ou negação, depois a prova, depois a **pergunta-tema entre 11 e 17 s** ("então como/por que…?").
- Fecha **sem CTA e sem cartela**, de preferência voltando à imagem do gancho (callback) ou numa imagem longa em movimento;
  CTA só se o roteiro do usuário tiver (e, então, no rosto).
- A referência tem 2,5 a 3 min (e 56 s no anúncio). Vídeos mais curtos (o exemplo tem 39 s) funcionam: o esqueleto é o mesmo,
  só encolhe.

## 7 · Legenda (P01; medido)
Uma só, **amarela**, sans bold, tarja preta translúcida **fixa** a ≈ 67 % da altura, 1 a 3 palavras por bloco, troca seca,
**sem palavra destacada**. No motor: Inter Bold, tarja a 73,5 % (V03), 46 px de altura em 720 = 69 px em 1080. Cor: o hex do
guia (#f0eb32) NÃO vai direto para o pixel; passa por `pecas.do_guia` (a cor real na tela é #f3e12a). Número em algarismo.

## 8 · Som (medido; `som.md`)
- **Só a voz** em ≈ −14 LUFS, compressão forte (LRA ≈ 3 LU), pico real ≤ −1 dBTP. **Sem música** nos 5 reels.
- Efeitos **raros e baixos**: foley de caneta/marca-texto começando 60 a 300 ms ANTES do traço, ≈ 30 dB abaixo da voz; no
  máximo uma subida grave que para no corte de uma virada. **Nada** em corte seco, pop de cartão, etiqueta, legenda, zoom ou véu.
- Na edição de exemplo o som tem 4 efeitos no total (ver `exemplo/edicao-exemplo/07-som/som.py`).
