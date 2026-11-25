# Briefing · construir planos de cena

Modelo para delegar a **construção de um ou mais planos de cena** (`05-cenas/plano_XX.py`) a um subagente. Preencha os `<…>` e
cole no prompt. Um agente por plano. **O agente só lê e escreve código e roda comandos leves; nunca render nem ffmpeg.**

---

Você escreve o código de alguns **planos de cena** de um reel, seguindo à risca a spec de cada trecho (que já traz a forma medida
nos reels de referência) e usando o motor que já existe. Se as imagens reais ainda não chegaram, construa com **imagens
provisórias** (o motor dá cartões cinza com rótulo) e deixe o movimento, as posições e a sincronia prontos e conferidos.
Português do Brasil.

`<SKILL>` = pasta da skill · `<EDIÇÃO>` = pasta do vídeo · motor = `<SKILL>/motor/`.

## Leia antes
1. `<SKILL>/references/decisoes-do-autor.md` (regra-mãe: forma fixa, conteúdo variável).
2. `<EDIÇÃO>/04-specs/00-globais.md` inteiro e os `<EDIÇÃO>/04-specs/trecho-NN.md` do seu pedido, inteiros.
3. `<EDIÇÃO>/04-specs/LISTA-DE-IMAGENS.md` (decisões já tomadas valem por cima da spec).
4. O código: `<SKILL>/motor/e3.py`, `pecas.py`, `perfis.py`, `monta.py` (classe `Ctx` e os comandos) e `<EDIÇÃO>/05-cenas/base.py`.
5. Exemplos prontos: `<SKILL>/exemplo/edicao-exemplo/05-cenas-r2/plano_*.py` e o `auditoria-r2-*.md` de cada um.
6. A `notes.md` da Ref de cada opção escolhida: `<SKILL>/biblioteca/<ID …>/notes.md` (blocos "Câmera", "Cadência", "Sensação do
   movimento" e "Construção").

## Regras
- **A spec manda.** Posições, tamanhos, giros, cores, durações, curvas e gatilhos vêm dela; onde ela deixar em aberto, use
  `00-globais.md`. Não invente forma.
- **Tempos pelas palavras, nunca fixos.** Recalcule tudo com `ctx.ataque(i)` (início da palavra i, reconferido no áudio) e
  `ctx.q_palavra(i, desloc_ms)`; todo evento começa num quadro inteiro: `t0 = ctx.t(q)`.
- **Os cortes do plano são fixos:** `base.CORTES['<nome do plano>']` = (f0, f1). Se um gatilho recalculado cair fora do plano,
  ajuste o evento (e registre), não o corte.
- **Imagens:** só por `ctx.img(nome, largura, altura, rotulo)` (BGR) e `ctx.rgba(nome, largura, altura, rotulo)` (recorte com alfa), com
  os nomes da tabela de imagens da edição; o motor troca a provisória pela real quando o arquivo existir. Dê à provisória a
  mesma proporção da real. Não baixe nada, não use imagem dos reels de referência, não crie imagem "de mentira".
- **Mesa e acabamento:** sempre `base.cena(camera, semente=N)` (uma semente por plano). Entrada em estalo: `base.estalo(...)`.
  Disco que nasce: `base.pop_disco(...)`. Mundo × tela: `base.mundo(x, y)`. Texto do editor ou traço à mão: `e3.Peca(..., sem_grao=True)`.
- **Acabamento do perfil** (`<EDIÇÃO>/03-plano/perfil.json`, padrão V03): use `pecas.cartao(...)`, `pecas.papel(...)`,
  `pecas.recorte_do_perfil`, `pecas.disco_do_perfil` e **`pecas.com_sombra(rgba, 'cartao'|'recorte'|'disco'|'etiqueta')`**, que já
  trazem borda e sombra do perfil. Não faça sombra à mão. **Nenhuma vinheta, véu ou escurecimento por cima das peças**, a não ser
  o que o usuário pediu por escrito. Cartão do perfil cresce uma margem transparente igual dos 4 lados: lembre da margem se
  posicionar outra peça pelo tamanho do RGBA.
- **Movimento em degraus:** estalos e pops não interpolam (cada valor dura 2 quadros; o disco, 1). Use
  `e3.Trilha(..., degrau=…, t0=…)` ou `e3.tabela(...)`.
- **Câmera por fases, nunca zoom linear do 1º ao último quadro** (a menos que a Ref medida seja assim): `ZoomPorTaxa`,
  `fases_pico`, `pausa` em `e3.py`; `base.zoom_fases(t0, chaves)` e `base.ancora(zoom, x_tela, y_tela)`. `chaves` = [(t_ms, taxa
  em %/s)] com a taxa variando em linha reta entre as chaves. **Quem manda:** (1º) a câmera medida na nota da Ref; (2º) a linha
  "Câmera" aprovada no painel; (3º) G12.3. Onde o painel contradiz a Ref, vale a Ref: relate a diferença. O pico cai ≈ 135 ms
  DEPOIS do início da palavra-chave e freia longo; a câmera quase para enquanto a mão trabalha (traço, marca-texto); a cena pode
  cortar andando; sem desfoque de movimento, salvo chicote ou peça que deixa a mesa, se a Ref tiver.
- **Quadro seguro:** confira no último quadro e no fim de cada pico que o conteúdo que a fala cita continua inteiro e legível.
- **Tempo de leitura:** nada pode ficar só 1 segundo em tela; a câmera não tira da tela, antes de dar para ler, algo que acabou de
  entrar.
- **A legenda não é sua:** o `monta.py` a desenha por cima (tarja a ≈ y 1270–1338 em 1080x1920); nenhuma informação de cena dentro
  dessa faixa.
- **Proibido:** `monta.py --render`, ffmpeg, qualquer comando pesado. Não edite `<SKILL>/motor/*.py` nem `base.py` (se faltar
  algo no motor, resolva dentro do seu plano e relate). Grave só em `<EDIÇÃO>/05-cenas/` (os arquivos do seu pedido) e no scratchpad.

## Nomes das imagens (`<EDIÇÃO>/05-imagens/tratadas/<nome>.png`)
| nome | o que será | proporção |
|---|---|---|
| <preencha a partir de LISTA-DE-IMAGENS.md> | | |

## Formato de um plano (`<EDIÇÃO>/05-cenas/plano_XX.py`)
```python
import e3, pecas, base
Q = e3.QUADRO_MS

def plano(ctx):
    f0, f1 = base.CORTES['plano_XX']
    cam = e3.Camera(zoom=..., cx=..., cy=...)
    c = base.cena(cam, semente=N)
    c.poe(e3.Peca(rgba, x=..., y=..., escala=..., giro=..., z=1, de=ctx.t(q_entrada), nome='…'))
    return {'nome': 'plano_XX · …', 'f0': f0, 'f1': f1, 'cena': c}
```
`Peca`: `x, y, escala, giro, alfa` aceitam número ou função do tempo (ms absolutos do clipe); `de`/`ate` = intervalo visível; `z` = ordem;
`fixa=True` prende à tela; `modo='multiplica'` + `revela=função` = marca-texto que varre; `variantes=[(t, rgba)]` troca a imagem a
seco (traço em degraus, etiqueta que ganha palavras). Giro positivo = horário. Um plano pode devolver também `gatilhos`
(dicionário com os quadros dos eventos; o som se cola neles).

## Como testar (leve, pode rodar à vontade; para render use a trava)
```bash
python3 "<SKILL>/motor/monta.py" "<EDIÇÃO>" --so plano_XX --linha
python3 "<SKILL>/motor/monta.py" "<EDIÇÃO>" --so plano_XX --folha F0 F1 --passo 1 --cols 8 --saida "<scratchpad>/folha.jpg"
python3 "<SKILL>/motor/monta.py" "<EDIÇÃO>" --so plano_XX --quadro N --saida "<scratchpad>/q.png"
```
Para planos de uma 2ª rodada em outra pasta: `--cenas 05-cenas-r2`. Abra as folhas e confira **quadro a quadro**: em que quadro cada peça
aparece, quantos quadros dura cada entrada, posição e tamanho assentados, giro, o que a câmera faz, se nada some ou pisca, se nada
fica atrás da legenda. Compare com a nota da Ref: a composição e o movimento têm de bater; só o conteúdo muda.

## Como conferir a câmera (obrigatório)
1. Tabela por fase: taxa pedida × taxa que sai da função (100·ln(z(t2)/z(t1))/(t2−t1) em %/s), zoom no 1º e no último quadro,
   quadro e palavra de cada pico.
2. Folha de quadros da cena inteira (passo 4) e do trecho de cada pico (passo 1 ou 2): sombra do perfil nos lugares certos,
   nenhuma vinheta sobrando, nada cortado no fim, legenda legível.
3. Gatilhos: imprima o dicionário `gatilhos` antes e depois de qualquer mudança; tem de ficar igual.

## O que entregar
- Os `plano_XX.py` do seu pedido, funcionando com `--so`.
- `<EDIÇÃO>/05-cenas/auditoria-plano_XX.md` para cada um: tabela "evento · gatilho (palavra, deslocamento) · quadro pedido · quadro em
  que apareceu no render · bate?", a Ref lida e o que ela mede de câmera, a tabela da câmera, medidas assentadas (posição, largura,
  giro) lidas do render × spec, tempo de cada peça na tela × piso de leitura, o que ficou diferente da spec e por quê, e o que você
  não conseguiu conferir.
- Resposta final ao principal em no máximo 15 linhas: arquivos, o que bate, o que não bate, divergências entre painel e Ref,
  problemas de quadro seguro, dúvidas. Sem colar código.
