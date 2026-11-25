# Skill · Edição no Estilo Curiosidades + painel de plano de edição

Edite seus reels e shorts verticais (9:16) no estilo **documentário em colagem**: você aparece pouco e o resto do vídeo é imagem
real do seu tema, tratada como papel sobre uma mesa escura, com legenda amarela e câmera viva. O Claude faz o corte limpo, divide
o vídeo em trechos, **abre um painel com 3 designs por trecho (e a recomendação dele)**, você escolhe, e ele constrói e renderiza.

Criada por Felipe Borges (@FelipeBorgesFalaIA) a partir da análise quadro a quadro de 5 reels de referência.

## O que vem aqui
- **O conhecimento:** o guia de estilo (design system, paleta, tipografia, composição), o ritmo, o **tempo que cada arte fica na
  tela**, a câmera por fases, o acabamento por perfil, o som, as **25 animações** com a medida de cada uma e o mapa de "que fala
  puxa que cena".
- **O motor:** o programa em Python que corta, transcreve, monta as cenas, desenha a legenda e renderiza.
- **O painel:** a página HTML que divide o vídeo em beats e deixa você escolher o design de cada um.
- **Um exemplo real completo** (sem os vídeos): plano, specs, cenas, auditorias, checklist e som de uma edição de 39 s.

## Instalar
Esta skill roda **no seu computador**, com o Claude Code (ou o app do Claude com acesso a arquivos e terminal), porque usa
ffmpeg, whisper e Python locais. Ela não funciona só no chat do navegador.

1. Copie a pasta `edicao-estilo-curiosidades` para a pasta de skills do Claude:
   - macOS / Linux: `~/.claude/skills/edicao-estilo-curiosidades`
   - Windows: `%USERPROFILE%\.claude\skills\edicao-estilo-curiosidades`
2. Instale o que ela precisa (uma vez):
   ```bash
   pip install -r requirements.txt
   ```
   - **ffmpeg** (inclui ffprobe): macOS `brew install ffmpeg` · Windows `winget install ffmpeg` · Linux `apt install ffmpeg`.
   - **whisper.cpp** (`whisper-cli`) e o modelo `ggml-large-v3-turbo.bin`
     (github.com/ggml-org/whisper.cpp). Aponte o modelo com a variável `WHISPER_MODEL` ou deixe em
     `~/.cache/whisper-cpp/ggml-large-v3-turbo.bin`.
3. Confira: `python3 ferramentas/verifica_ambiente.py`. Ele diz o que falta.

## Usar
Abra o Claude na pasta onde você guarda seus vídeos e diga, por exemplo:

> Edita esse vídeo no estilo curiosidades. O bruto é `meu-reel.mp4`, o tema é [o assunto].

> Abre o painel de edição desse vídeo.

O Claude vai: preparar a pasta da edição → cortar silêncios e erros → **abrir o painel** → esperar a sua escolha → pedir as imagens
(prints seus, logos oficiais; ele só baixa algo da internet com o seu "sim") → construir as cenas → renderizar → conferir o
checklist → te dizer **o que não foi verificado**. Calcule ≈ 1 hora por reel.

No painel: escolha **A, B ou C** em cada trecho (ou clique em *Usar minhas sugestões*), escolha o perfil de acabamento no topo,
escreva observações, clique em **Copiar plano** e cole no chat.

## Regras que a skill segue (e que você pode ajustar pedindo)
Forma idêntica à referência, conteúdo sempre do seu tema · sempre 3 opções por trecho com recomendação · nada fica só 1 s na
tela · a câmera medida na referência manda · só a voz no som por padrão. As decisões do autor e o que dá para trocar:
`references/decisoes-do-autor.md`.

## Limites honestos
- **Testado no macOS.** Windows e Linux não foram testados pelo autor; se algo falhar, mande a mensagem de erro para o Claude.
- A amostra é de 5 reels de 1 criador. O que aparece em 1 só (texto grande, rótulo digitado, cenas 3D, diagrama) é opção, não regra.
- A transcrição é em português por padrão (`pt`); outros idiomas funcionam trocando o parâmetro.
- O som de exemplo usou efeitos gerados por IA; você pode usar efeitos próprios ou ficar só com a voz.

## Avisos
- A pasta `biblioteca/` traz, para cada animação, a **medida** em texto (`notes.md`), tirada dos reels de referência de
  @fineasjackson. Esta versão pública **não inclui nenhum quadro dos vídeos de referência**: no painel, cada opção aparece com
  nome, categoria e descrição, sem miniatura. Para ver a forma, peça ao Claude a medida da referência ou assista aos reels originais.
- A fonte **Inter** (`motor/fontes/`) tem licença aberta (SIL OFL 1.1).
- Use só imagens que você tem direito de usar. Logos são marcas dos donos; use como referência editorial.

## Mapa da pasta
```
SKILL.md · LEIA-ME.md · requirements.txt
references/          guia por tema, mapa, som, folha de tempos, fluxo, painel, decisões, lições, briefings
references/principios/   as 25 animações + 7 famílias
biblioteca/          209 animações: notes.md (medida) · index.json
motor/               o motor de render e o gerador do painel
modelo-edicao/       base.py para uma edição nova
ferramentas/         leve.py · servidor_painel.py · verifica_ambiente.py
exemplo/             uma edição real completa, sem mídia
```
