# Fluxo completo: do vídeo bruto ao corte final

`<SKILL>` = a pasta onde esta skill está instalada (a que contém o `SKILL.md`). `<EDIÇÃO>` = a pasta do vídeo, criada na pasta
de trabalho do usuário: `edicoes/AAAA-MM-DD-slug/`. Português do Brasil. Marque cada afirmação sobre medida como
**medido**, **observado** ou **inferido**; o que não deu para medir, escreva "não medido" e por quê.

**Máquina comum (16 GB):** todo comando pesado (render, ffmpeg em vídeo, whisper, remoção de fundo) roda **um por vez** pela
trava (`transcreve.py` e `corte.py` já usam a trava por dentro: chame-os direto; `monta.py --render` e o recorte de fundo NÃO usam, então envolva-os): `python3 "<SKILL>/ferramentas/leve.py" --teto-gb 4 --rotulo nome -- <comando>`. Comandos leves (folha de quadros,
um quadro, listar blocos) podem rodar sem a trava.

## 0 · Antes da primeira edição
```bash
python3 "<SKILL>/ferramentas/verifica_ambiente.py"      # diz o que falta (ffmpeg, whisper, bibliotecas) e como instalar
pip install -r "<SKILL>/requirements.txt"
```
Leia `references/decisoes-do-autor.md` e `references/folha-de-tempos.md`. Se o usuário não definiu: tema do vídeo, perfil
(padrão V03) e se quer só voz no som (padrão).

## 1 · Receber o bruto e preparar a pasta
```bash
mkdir -p "<EDIÇÃO>"/{01-bruto,02-corte,03-plano,04-specs,05-cenas,05-imagens/originais,05-imagens/tratadas,06-render,07-som}
cp "<SKILL>/modelo-edicao/05-cenas/base.py" "<EDIÇÃO>/05-cenas/base.py"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,nb_frames -of default=nw=1 bruto.mp4
```
O estilo pede **um único enquadramento frontal fixo** (sem zoom, sem troca de ângulo). Se o bruto for diferente, diga antes de seguir.
Se for horizontal (16:9), o corte recorta 9:16: `--largura` = altura × 9/16 (ex.: 1440 → 810) e `--crop` = x inicial do recorte
(centralize no rosto; no exemplo, x = 903 em 2560 de largura). Se já for vertical 1080x1920: `--crop 0 --largura 1080`.

## 2 · Corte limpo (silêncios e erros de gravação)
```bash
python3 "<SKILL>/motor/transcreve.py" bruto.mp4 "<EDIÇÃO>/01-bruto" pt         # whisper.cpp: palavras com tempo em ms
python3 "<SKILL>/motor/corte.py" bruto.mp4 "<EDIÇÃO>/01-bruto" "<EDIÇÃO>/02-corte" --crop X0 --largura W    # só planeja (leve)
# revise 02-corte/cortes.md; corrija texto da transcrição com --corrige "12=Claude,40=Gamma"; depois, o vídeo:
python3 "<SKILL>/motor/corte.py" bruto.mp4 "<EDIÇÃO>/01-bruto" "<EDIÇÃO>/02-corte" --crop X0 --largura W --renderiza
python3 "<SKILL>/motor/ataques.py" "<EDIÇÃO>/02-corte"                      # reconfere no áudio o início de cada palavra
python3 "<SKILL>/motor/ve_ataques.py" "<EDIÇÃO>/02-corte" <pasta-de-saida>  # espectrograma para conferir a olho (opcional)
```
- Silêncio = envelope abaixo de −45 dBFS por ≥ 140 ms; encurtado para ≈ 110 ms no fim de frase e ≈ 90 ms no meio, em
  quadros inteiros, com emenda de 5 ms no áudio. Cabeça e cauda ficam.
- **Erros de gravação** (frase repetida, recomeço, gaguejo, muleta longa): o motor não os acha sozinho. Leia a transcrição e,
  se houver, grave `02-corte/manuais.json` (lista de `{"f0": quadro_do_bruto, "n": nº_de_quadros, "tipo": "erro de gravação",
  "entre": "…"}`) antes de rodar `--renderiza`. Em repetição, **fica a última tomada completa**; na dúvida, **não corte** e
  liste para o usuário decidir.
- Correções de texto só para o que o usuário VÊ (legenda): nomes de produto, "A" → "IA". Na legenda, número em algarismo
  (`02-corte/legenda-ajustes.json`; ver o exemplo). Não altere o que é áudio.
- **Confira 5 palavras contra o áudio** antes de confiar nos tempos (a transcrição adianta inícios de frase em 1 a 3 quadros).
- Saída: `02-corte/clipe-limpo.mp4` (1080x1920), `cortes.json`/`cortes.md` (o que foi cortado e onde),
  `palavras-ataque.json` (campo `ataque_ms` = o início de cada palavra), `audio-corte.wav`. **Entregue ao usuário a lista do
  que foi cortado, com tempos.**

## 3 · Beats e painel (parar aqui até o usuário escolher)
1. Divida a fala do clipe limpo em **beats** pelas ideias e frases (tempos em ms do clipe CORTADO, não do bruto).
2. Para cada beat escolha as 3 opções (ver `references/painel.md`, "Como escolher as 3 opções de um beat").
3. Grave `03-plano/beats.json` (esquema em `painel.md`) e gere o painel; abra pelo servidor da skill (comandos em `painel.md`).
4. **Pare.** Diga ao usuário: abra o link, escolha por beat (ou use *Usar minhas sugestões*), troque o perfil se quiser,
   escreva observações e cole o plano de volta. Aponte o que o painel mostra (% de rosto, cortes por 10 s) e qualquer beat
   em que a fala rápida aperta o piso de leitura.
5. Grave `03-plano/escolhas-rN.md` (o texto colado) e `03-plano/perfil.json`.

## 4 · Specs por beat escolhido e lista de imagens
Para cada beat com cena, escreva `04-specs/trecho-NN.md` (formato em `references/briefings/briefing-spec-de-cena.md`; exemplos
reais em `exemplo/edicao-exemplo/04-specs/`). A spec traduz a **medida** da Ref (a `notes.md` em `biblioteca/<ID>/`) para este
vídeo: linha do tempo amarrada às palavras (gatilho = "N ms antes/depois do início da palavra X"), FORMA em px de 1080x1920 e
ms, CONTEÚDO por lacuna com a receita de tratamento, imagens necessárias, piso de leitura. Antes, escreva
`04-specs/00-globais.md` a partir de `references/molde-do-motor-00-globais.md` (valores comuns a todas as cenas).
**Conversão:** o guia e as notas estão em px/% de 720x1280 e quadros da referência (V01 = 24 fps; V02 a V05 = 23,976); o motor
trabalha em **1080x1920 (px × 1,5)** e em **ms**.
Consolide as imagens em `04-specs/LISTA-DE-IMAGENS.md` (ver `references/imagens-e-conteudo.md`) e **peça o "sim" do usuário
antes de baixar qualquer arquivo da internet**.

## 5 · Imagens
Obtenha e trate (`references/imagens-e-conteudo.md`): originais em `05-imagens/originais/`, tratadas em `05-imagens/tratadas/<nome>.png`
(o motor procura pelo nome). Enquanto a imagem real não chega, o motor mostra uma **provisória cinza com rótulo**: dá para
construir e conferir movimento, posição e sincronia sem ela.

## 6 · Construir cena por cena
- Um arquivo por plano em `05-cenas/plano_XX.py`, cada um com `def plano(ctx)` devolvendo `{'nome','f0','f1','cena'}`. Os cortes
  de cada plano ficam em `base.CORTES` (cada corte seco ≈ 42 ms antes da 1ª palavra da frase, calculado com `ctx.ataque(i)`).
  Exemplos completos: `exemplo/edicao-exemplo/05-cenas-r2/plano_*.py`.
- **Tempos sempre pelas palavras** (`ctx.ataque(i)`, `ctx.q_palavra(i, desloc_ms)`), nunca quadros fixos copiados da spec.
- **Subagentes:** pode delegar um plano por agente (um agente por plano, só lendo e escrevendo código; **nunca** render nem
  ffmpeg em paralelo). Use `references/briefings/briefing-construir-cena.md` preenchido.
- Teste leve a cada plano:
```bash
python3 "<SKILL>/motor/monta.py" "<EDIÇÃO>" --so plano_02 --linha
python3 "<SKILL>/motor/monta.py" "<EDIÇÃO>" --so plano_02 --folha F0 F1 --passo 1 --cols 8 --saida folha.jpg
python3 "<SKILL>/motor/monta.py" "<EDIÇÃO>" --so plano_02 --quadro N --saida q.png
```
- **Audite quadro a quadro** (abra as folhas): em que quadro cada peça aparece, quantos quadros dura cada entrada, posição e
  tamanho assentados, giro, câmera, nada some nem pisca, nada fica atrás da tarja da legenda (y 1266 a 1336). Compare com a
  `notes.md` da Ref. Grave `05-cenas/auditoria-plano_XX.md` (modelo: `exemplo/.../auditoria-r2-*.md`).

## 7 · Render e checklist
```bash
python3 "<SKILL>/ferramentas/leve.py" --teto-gb 4 --rotulo render -- python3 "<SKILL>/motor/monta.py" "<EDIÇÃO>" --render --final --crf 21 --saida "<EDIÇÃO>/06-render/corte-01.mp4"
```
(`--de F0 --ate F1` renderiza um trecho; `--sem-legenda` para ver sem legenda; `--cenas outra-pasta`, `--perfil V01` quando preciso.
`--final` **recusa a entrega** se ainda houver imagem provisória; sem ela, o render sai marcado como PROVISÓRIO.)
`--crf 21` com grão vivo dá ≈ 90 MB para 40 s; `--crf 14` dá ≈ 200 MB.
Rode o **checklist de 15 itens** (`references/checklist-de-reproducao.md`) e **meça no próprio render**: % de rosto, cortes por
10 s, intervalo entre imagens, deslocamento de cada entrada em relação à palavra, piso de leitura. Grave
`06-render/CHECKLIST-corte-NN.md` com as medidas e **com o que NÃO foi verificado**.

## 8 · Revisão do usuário
Ele assiste e pede ajustes pontuais. Cada rodada vira um corte novo (`corte-02`, `corte-03`…), com um checklist curto do que
mudou. Quando ele pedir algo só para aquele reel (ex.: um véu escuro atrás de logos), registre como exceção da edição, não
do estilo. **Pergunte se está pronto para o som antes de mexer nele.**

## 9 · Som
Padrão: só a voz, normalizada (≈ −14 LUFS). Efeitos só se o usuário pedir, raros e baixos, como em `references/som.md` e
`exemplo/edicao-exemplo/07-som/som.py` (que usa efeitos gerados por IA; o aluno pode usar efeitos próprios). Junte sem
recodificar o vídeo: `ffmpeg -i corte-NN.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k saida.mp4`.

## 10 · Entrega
Entregue o arquivo, o checklist, a lista do que mudou entre cortes e **o que não foi verificado** (não foi assistido em tempo
real? não foi ouvido? Windows/Linux? grão sobre print muito branco?). Não diga "perfeito"; diga o que foi medido.
