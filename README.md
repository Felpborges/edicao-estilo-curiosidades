# Skill · Edição de reels no Estilo Curiosidades

Skill para o **Claude Code** que edita reels e shorts verticais (9:16) no estilo *documentário em colagem*: você aparece
pouco e o resto do vídeo é imagem real do seu tema, tratada como papel sobre uma mesa escura, com legenda amarela e câmera
viva. O Claude corta o bruto, divide o vídeo em trechos, abre um painel com 3 designs por trecho, você escolhe, e ele
constrói e renderiza.

Criada por Felipe Borges ([@FelipeBorgesFalaIA](https://www.youtube.com/@FelipeBorgesFalaIA)).

## Instalar

Clone direto na pasta de skills do Claude:

**macOS / Linux**

```bash
git clone https://github.com/Felpborges/edicao-estilo-curiosidades.git ~/.claude/skills/edicao-estilo-curiosidades
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/Felpborges/edicao-estilo-curiosidades.git "$env:USERPROFILE\.claude\skills\edicao-estilo-curiosidades"
```

Sem git: clique em **Code → Download ZIP**, descompacte e renomeie a pasta para `edicao-estilo-curiosidades` dentro de
`.claude/skills`.

Depois instale as dependências, dentro da pasta da skill:

```bash
pip install -r requirements.txt
```

Você também precisa de **ffmpeg** e **whisper.cpp** (`whisper-cli`) com o modelo `ggml-large-v3-turbo.bin`. Para conferir
o que falta:

```bash
python3 ferramentas/verifica_ambiente.py
```

## Usar

Abra o Claude Code na pasta onde estão seus vídeos e peça:

> Edita esse vídeo no estilo curiosidades. O bruto é `meu-reel.mp4`, o tema é [o assunto].

Calcule cerca de 1 hora por reel.

## Atualizar

```bash
git -C ~/.claude/skills/edicao-estilo-curiosidades pull
```

## Mais detalhes

O passo a passo completo, as regras que a skill segue, os limites e o mapa da pasta estão no [LEIA-ME.md](LEIA-ME.md).
Testado no macOS; Windows e Linux ainda não foram testados pelo autor.

## Licença

© 2026 Felipe Borges. Esta skill (textos, medidas e código) é distribuída sob a licença
[Creative Commons Atribuição-NãoComercial 4.0 Internacional (CC BY-NC 4.0)](LICENSE): você pode usar, adaptar e
compartilhar, com crédito ao autor, **sem revender nem redistribuir comercialmente**. Os vídeos que você edita com a skill
são seus e podem ser usados como quiser, inclusive comercialmente.

A fonte **Inter** (`motor/fontes/Inter-Bold.ttf`) não é do autor desta skill: pertence ao The Inter Project Authors e segue
a licença própria dela, a [SIL Open Font License 1.1](motor/fontes/OFL.txt).
