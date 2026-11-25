---
name: edicao-estilo-curiosidades
description: Edita reels e shorts talking head (9:16) no "Estilo Curiosidades", o documentário em colagem (rosto pouco; o resto é imagem real tratada como papel sobre uma mesa escura, legenda amarela, câmera viva), com o motor de edição completo e o painel de plano de edição que divide o vídeo em trechos (beats) e oferece 3 designs por trecho com recomendação. Carrega o design system, o ritmo, o tempo exato de cada arte na tela, a câmera por fases, o acabamento por perfil, as 25 animações medidas e o som. Use SEMPRE que o usuário pedir para editar um reel/short/vídeo vertical nesse estilo, "abrir o painel de edição", "plano de edição", "dividir o vídeo em beats", "editar igual aos reels do fineasjackson", "estilo curiosidades", "colagem de papel sobre mesa escura", ou entregar um vídeo bruto para editar neste método, mesmo sem citar a skill. NÃO use para vídeos longos horizontais, para motion graphics sem apresentador, nem para outros estilos de edição.
---

# Edição de reels no Estilo Curiosidades + painel de plano de edição

Você edita o vídeo do usuário (de qualquer tema) com **edição, design e ritmo extremamente iguais** aos 5 reels de referência
(@fineasjackson), medidos quadro a quadro. Tudo o que o treino aprendeu está nesta skill: o guia (25 animações), o mapa de
"que fala puxa que cena", o som, o motor de render em Python e o painel em HTML. **Forma fixa, conteúdo variável:** a forma é
copiada com precisão; o conteúdo (imagens, palavras, números) é sempre do tema do usuário.

`<SKILL>` = a pasta onde este `SKILL.md` está instalada. `<EDIÇÃO>` = `edicoes/AAAA-MM-DD-slug/` na pasta de trabalho do usuário.
Responda em **português do Brasil**.

## Antes de tudo (1ª vez)
```bash
python3 "<SKILL>/ferramentas/verifica_ambiente.py"     # ffmpeg, whisper.cpp + modelo, numpy/opencv/Pillow
pip install -r "<SKILL>/requirements.txt"
```
Se algo falta, diga o comando de instalação do sistema do usuário e espere. Windows e Linux não foram testados pelo autor.

## Regras inegociáveis
1. **Todo corte começa pelo painel.** Depois do corte limpo, gere o painel, **pare** e peça ao usuário para escolher. Em cada trecho:
   **exatamente 3 opções** (A, B, C) tiradas da biblioteca, **com a sua recomendação marcada** ("Minha sugestão"). Nada é
   construído antes da escolha. → `references/painel.md`
2. **Forma fixa, conteúdo variável.** Nenhum quadro, miniatura, imagem ou clipe das referências entra no vídeo final. Toda
   lacuna de imagem é descrita pelo PAPEL que cumpre e pela receita de tratamento, e preenchida com conteúdo do tema do usuário.
   → `references/imagens-e-conteudo.md`
3. **Medido, não "parece que".** Tempo em quadros/ms, posição em px de 1080x1920, cor amostrada. Marque **medido**, **observado**
   ou **inferido**; o que não mediu, escreva "não medido". Onde o guia e a `notes.md` da Ref discordarem, **vale a nota**.
4. **Tempos pelas palavras, nunca fixos.** Todo evento é amarrado ao início da palavra (`ctx.ataque(i)`, reconferido no áudio) e cai
   num quadro inteiro. → `references/folha-de-tempos.md`
5. **Piso de leitura: nada fica só 1 segundo em tela.** Cena ≥ 1,5 s · texto parado ≥ 700 ms · imagem de série ≥ 1,2 s · último
   item de lista ≥ 700 ms · rosto fora do piso. Fala rápida: junte peças num plano contínuo; **não estique a cena**.
6. **A câmera medida na referência manda** (depois a linha aprovada no painel, depois a regra geral). Não acrescente ênfase por conta própria.
7. **Um perfil de acabamento por vídeo, inteiro** (V03 por padrão), nunca misturado. Cor do guia passa por `pecas.do_guia`.
8. **Máquina comum: um comando pesado por vez**, sempre por `ferramentas/leve.py` (render, ffmpeg em vídeo, whisper, recorte de fundo).
9. **Baixar da internet exige o "sim" do usuário** (lista com arquivo, fonte, licença, tamanho). Nunca imagem falsa que pareça real;
   nunca dado de terceiros à mostra.
10. **Entregue dizendo o que NÃO foi verificado.** Corte automático em minutos foi reprovado: qualidade antes da velocidade
    (≈ 1 h por reel). As decisões do autor que o usuário pode trocar estão em `references/decisoes-do-autor.md`.

## O estilo em uma tela (números completos em `references/design-system.md` e `folha-de-tempos.md`)
- **Proporção:** 79 a 86 % do tempo é cena de tela cheia; o rosto fica com 14 a 21 %. **Um único enquadramento frontal fixo** no
  rosto (sem zoom, punch-in, troca de ângulo); rosto ↔ cena só por **corte seco** (nenhum dissolve), caindo ≈ 42 ms antes da 1ª palavra.
- **Quando o rosto volta:** virada curta, pergunta, anúncio, comentário, conclusão. **Todo dado concreto** (data, nome, número, lugar,
  citação, objeto, mecanismo) **vira imagem**.
- **O mundo:** fundo quase preto quente (#100e0c nas bordas, #221f1d na luz central). Imagens reais em **cartão de borda clara**
  (≈ 12 px em 1080, giro de ±1° a ±5°), recortes grandes (50 a 85 % da largura) sobre **discos creme**, etiquetas de papel,
  documentos reais com marca-texto amarelo, marcação amarela à mão. Nada de ícone, emoji, glow, degradê colorido ou ilustração genérica.
- **Câmera viva por fases** (repouso, pico na palavra-chave, freio longo, recuo, pausa no gesto); entre cenas, troca por movimento
  (empurrão, cobertura, chicote, pilha) mais que por corte.
- **Entrada de cartão:** estalo de 4 quadros (167 ms) em degraus de 2 quadros. **Ritmo:** 3,2 a 3,4 palavras/s; pausas de 80 a 110 ms;
  uma imagem nova a cada ≈ 1,1 s; 2,1 a 2,6 cortes secos por 10 s. Respira em ondas (adensa em mecanismo/lista, alonga em narrativa).
- **Sincronia:** a imagem entra junto ou um pouco antes da palavra (mediana −38 ms). Lista: uma peça por item. Mecanismo: um passo por frase.
- **Legenda:** uma só, amarela, sans bold (Inter Bold), tarja preta translúcida fixa a ≈ 67 % da altura, 1 a 3 palavras por bloco,
  troca seca, sem palavra destacada.
- **Som:** só a voz (≈ −14 LUFS), sem música; efeitos raros e baixos (foley de caneta/marca-texto, no máximo uma subida grave na virada).
- **Abertura e fecho:** abre no rosto por 0,7 a 1,3 s com "olha isto" e corta para o objeto; pergunta-tema entre 11 e 17 s; fecha sem
  CTA e sem cartela, de preferência com a imagem do gancho de volta.

## O fluxo (detalhe, comandos e armadilhas em `references/fluxo-completo.md`)
0. Verificar ambiente · 1. Receber o bruto, criar `<EDIÇÃO>`, `ffprobe` (conferir enquadramento frontal fixo).
2. **Corte limpo:** `transcreve.py` → `corte.py` (silêncios → ≈ 90/110 ms; erros de gravação por `manuais.json`; legenda) → `ataques.py`.
   Confira 5 palavras no áudio. Entregue a lista do que foi cortado.
3. **Beats + painel:** divida a fala em trechos, escolha 3 opções por trecho, grave `beats.json`, `gera_plano.py`,
   `servidor_painel.py`. **PARE e espere as escolhas do usuário.**
4. **Specs** por trecho (forma medida da Ref + gatilhos nas palavras + conteúdo por lacuna) e **lista de imagens** (peça o "sim").
5. **Imagens:** obter e tratar; enquanto não chegam, o motor usa provisórias.
6. **Construir** cena por cena (`05-cenas/plano_XX.py`), auditar quadro a quadro; pode delegar um plano por subagente
   (`references/briefings/`), sem render em paralelo.
7. **Render** pela trava; **checklist de 15 itens**; medir no próprio render; `CHECKLIST-corte-NN.md` com o que não foi verificado.
8. **Revisão** do usuário (cada rodada = corte novo) → perguntar se está pronto para o som → **som** (só voz por padrão) → entrega.

## O que ler e quando (não leia o guia inteiro: são ≈ 8.700 linhas)
| etapa | leia |
|---|---|
| sempre | este arquivo · `references/decisoes-do-autor.md` · `references/folha-de-tempos.md` |
| montar o painel | `references/painel.md` · `references/mapa-roteiro-animacao.md` (seções 1, 3, 4, 5, 6, 7, 8) · `references/principios/_INDICE.md` |
| escolher o perfil | `references/acabamento-perfis-camera-legenda.md` (G12.2) · `references/diferencas-entre-os-videos.md` (G10) |
| escrever uma spec ou cena | `biblioteca/<ID …>/notes.md` da Ref · o `references/principios/Pxx-*.md` **só dos princípios escolhidos** · a `familia-*.md` dele · `references/molde-do-motor-00-globais.md` |
| imagens | `references/imagens-e-conteudo.md` · `references/design-system.md` (G5) |
| câmera e movimento | `references/movimento.md` (G6) · `references/acabamento-perfis-camera-legenda.md` (G12.3) |
| ritmo, abertura, fecho | `references/tempos-e-ritmo.md` (G7) · `references/rosto-cena-abertura-fecho.md` (G8, G9) |
| legenda | `references/principios/P01-*.md` · G12.4 |
| som | `references/som.md` (seções 5 e 6) |
| antes de entregar | `references/checklist-de-reproducao.md` · `references/licoes-e-armadilhas.md` |
| dúvida de estilo sem resposta | `references/duvidas-e-baixa-confianca.md` (G11): ofereça como opção no painel, não decida sozinho |

Observação sobre os arquivos extraídos do guia: onde citam `still.png`, `strip.jpg` ou `clip.mp4` de uma Ref (ex.: V01-A28), nesta
skill só existe `biblioteca/<ID …>/notes.md` (a medida); a versão pública não traz miniaturas, e o painel segue sem a imagem. Onde citam "o Felipe", é o autor do método.

## Mapa da skill
```
SKILL.md                       este arquivo
LEIA-ME.md                     instalação e uso, para quem recebe a skill
requirements.txt
references/                    guia dividido por tema, mapa, som, folha de tempos, fluxo, painel, decisões, lições, briefings
references/principios/         as 25 animações (Pxx) + as 7 famílias, uma por arquivo
biblioteca/                    209 animações medidas: <ID nome>/notes.md · index.json (id → pasta)
motor/                         o motor de render e do painel (Python): transcreve, corte, ataques, e3, pecas, perfis, legenda, monta, gera_plano
modelo-edicao/05-cenas/        base.py modelo para uma edição nova
ferramentas/                   leve.py (trava de memória) · servidor_painel.py (Range) · verifica_ambiente.py
exemplo/edicao-exemplo/        uma edição real inteira (sem mídia): beats, painel, specs, cenas, auditorias, checklist, som
```
