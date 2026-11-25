# Lições aprendidas e armadilhas (leia antes de medir, construir ou entregar)

Tudo o que custou caro durante o treino e a primeira edição real. Cada item diz o que deu errado e o que fazer.

## Medida e confiança
- **Vale a nota.** Onde a decupagem de um vídeo e a `notes.md` de uma Ref discordarem, vale a nota. As notas da 1ª passada
  erravam muito: na conferência de 25 animações, mais da metade tinha erro; 144 de 179 foram corrigidas na remedição.
  **A remedição não foi conferida de novo por amostragem.** Antes de copiar a forma de uma Ref, reconfira as 2 ou 3 medidas
  que mais pesam na cena (tamanho da peça principal, nº de quadros da entrada, giro) contra a imagem/relato; diga se bateu.
  (Nesta skill só há `notes.md` e `thumb.jpg`; os `strip.jpg` e clipes não foram incluídos.)
- Margem das medidas: ±1 quadro nos tempos, ±12 px (em 720) na geometria, 1 a 3 quadros nos gatilhos de início de frase.
- A câmera da cena inteira, não só do começo: medir a câmera só no começo foi a causa de vários erros achados na conferência.
- **"Parado" quase não existe:** a câmera deriva mesmo quando nenhum elemento novo entra.
- 4 erros em notas da biblioteca, descobertos ao escrever as specs (V04-A08: traço em degraus e deslize de ≈ 17 q; V04-A45:
  altura da coluna 83 %; V01-A45: estalo medido na peça errada; V04-A09: etiqueta em 5 q). As notas não foram alteradas;
  as specs do exemplo dizem o que valeu.
- Curva do marca-texto: acelera e freia no V02; quase constante no V01 e no V04. Escolha uma e diga qual.
- Amostra: 5 vídeos de 1 criador; o V02 é anúncio (pesa pouco em roteiro e proporção). Algo que só aparece em 1 vídeo é
  **opção, não regra**.

## Cor (o achado mais traiçoeiro)
- Os reels de referência são BT.709, mas os hex do treino foram lidos em quadros JPG, que decodificam como BT.601. Neutros
  não mudam; **cores saturadas saem deslocadas**: a legenda lida como #f0eb32 é, na tela, **#f3e12a**; o amarelo-ouro #e0b830 é
  #e5b42a; o marca-texto #efcb3b é #f4c634. **Todo hex do guia passa por `pecas.do_guia(hex)` antes de virar pixel.** Os hex
  saturados dos outros arquivos do guia estão deslocados do mesmo jeito.
- **Para amostrar cor de um vídeo**, use um PNG extraído com a matriz do arquivo, não JPG.
- O leitor de vídeo do OpenCV decodifica como BT.601 (erro médio de 3,5 níveis no rosto): o motor lê o clipe pelo ffmpeg.
- A conversão padrão do ffmpeg entre YUV e RGB escurece ≈ 1,6 nível de luma a cada passagem: o motor lê com
  `-sws_flags accurate_rnd+full_chroma_int` e converte para YUV BT.709 pela conta exata (`monta.yuv709`). Não "simplifique".

## Corte e sincronia
- A transcrição adianta inícios de frase em 1 a 3 quadros: use `ataques.py` e confira 5 palavras no áudio.
- Todo evento começa num quadro inteiro (`t0 = ctx.t(q)`); estalos e pops não interpolam (degraus de 2 quadros; o disco, 1).
- **Os quadros escritos nas specs foram calculados com tempos antigos da transcrição**: recalcule tudo com `ctx.ataque(i)`.
- Fala mais rápida que a referência (3,95 contra 3,2 a 3,4 palavras/s): a peça entra na palavra (a sincronia manda), registre a
  diferença; não estique a cena (ver `folha-de-tempos.md` seção 3).
- Prints retangulares dentro de disco creme: com o 1º tamanho, os recortes cobriam quase todo o disco; na referência o disco
  aparece em volta da figura. Reduza o recorte para ≈ 45 a 87 % do diâmetro do disco.

## Acabamento
- **Um perfil por vídeo, inteiro, sem misturar** (a vinheta de um com o grão de outro não existe em nenhum reel).
- O grão foi igualado ao arquivo BAIXADO da referência; depois de subir, a plataforma comprime e ele enfraquece.
- Com grão vivo, `--crf 14` dá ≈ 200 MB para 40 s; `--crf 21` dá ≈ 90 MB com o mesmo grão medido.
- A sombra de baixo do V03 ficou um pouco mais escura que numa cena da referência (−48 % contra −32 %), dentro da faixa medida
  no vídeo (−40 a −77 %). Os perfis V01 e V04 rendem, mas não foram medidos contra a referência como o V03.
- **Vinheta ou véu por cima das peças só se o usuário pedir por escrito** (no exemplo, um véu atrás de logos no trecho 10).
- Texto grande e rótulo digitado (P03, P04): só as curvas medidas estão em `perfis.py`; a peça animada não foi construída.

## Máquina e sistema
- **Um pesado por vez** (render, ffmpeg em vídeo, whisper, remoção de fundo): a máquina de 16 GB do autor travou com agentes
  pesados em paralelo. A trava é `ferramentas/leve.py`; pico típico do render do exemplo: 1,8 GB, 58 s para 942 quadros.
- `ffmpeg` do autor **não tem o filtro `drawtext`**: o motor não precisa dele (tudo é desenhado em Python, com OpenCV e Pillow).
- **Não envolva `transcreve.py` nem `corte.py` na trava por fora:** eles já a usam por dentro. (A trava agora detecta isso e roda
  direto; antes, a de dentro esperava para sempre pela de fora e o comando pendurava.) `monta.py --render` e o recorte de fundo
  NÃO usam a trava: envolva-os.
- O `corte.py --renderiza` precisa de `01-bruto/audio-48k.wav`; o `transcreve.py` gera. Se rodar o corte sem transcrever, ele falha.
- A transcrição do whisper varia dezenas de ms entre execuções e entre modelos; por isso os tempos de uma edição vivem em
  `02-corte/palavras-ataque.json` (com ajustes manuais em `ataques-manuais.json`) e as cenas conferem o piso de leitura com
  `assert`. Se uma cena falhar nessa conferência depois de retranscrever, é o piso funcionando: ajuste o evento, não o piso.
- `python3 -m http.server` não serve para o painel (sem Range). Use `ferramentas/servidor_painel.py`.
- **Não testado:** Windows e Linux (o motor foi feito e conferido no macOS); duplo clique no painel (`file://`); o corte
  limpo e o render nunca foram ouvidos nem assistidos em tempo real por terceiros no exemplo.
- Fonte da legenda: Inter Bold (OFL) vai em `motor/fontes/`. Sem ela o motor cai numa fonte provisória (Arial Bold).

## Processo
- **Analista mede, um segundo agente remede tudo, e só então se escreve o guia.** (Lição do treino; relevante se o usuário
  quiser treinar um estilo novo no mesmo método.)
- Não construa nada antes de o usuário escolher no painel.
- Entrega com "o que NÃO foi verificado". Corte automático em minutos foi reprovado; a meta realista é ≈ 1 h por reel.
