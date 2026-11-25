# O painel de plano de edição

Toda edição neste estilo passa por aqui, **antes** de construir qualquer cena. O painel divide o vídeo já cortado em
**beats** (trechos), mostra para cada beat **três designs** tirados da biblioteca de referências, com a **sua recomendação
marcada**, e deixa o usuário escolher e escrever observações. "Copiar plano" devolve o resultado para você.

## Como gerar e abrir
```bash
python3 "<SKILL>/motor/gera_plano.py" "<EDIÇÃO>/03-plano"            # lê beats.json, grava plano-de-edicao.html e refs/
python3 "<SKILL>/ferramentas/servidor_painel.py" "<EDIÇÃO>" 8765       # servidor local com suporte a Range
# abra: http://localhost:8765/03-plano/plano-de-edicao.html
```
- Use o servidor da skill, **não** `python3 -m http.server`: sem pedidos por faixa (Range) os players não pulam para o
  trecho. Duplo clique no arquivo (`file://`) não foi testado: os players podem abrir no começo.
- O gerador copia as miniaturas e notas usadas para `03-plano/refs/`: o painel é autossuficiente (pode zipar a pasta
  `03-plano` + o clipe e mandar para alguém).
- O plano salva sozinho no navegador (chave por edição e rodada). Para uma 2ª rodada do mesmo vídeo, aumente `"rodada"`.
- Depois de gerar, **pare e peça ao usuário para abrir, escolher e colar o plano de volta.** Não construa nada antes.

## O que o painel mostra
- **Cabeçalho:** título, clipe, duração · nº de trechos, estilo; "o plano salva sozinho"; botões *Usar minhas sugestões no que
  falta*, *Limpar*, *Copiar plano*.
- **Perfil de acabamento (topo):** V03 marcado por padrão, V01 e V04 ao lado, cada um com miniaturas e os pontos que o definem.
  Vale para o vídeo inteiro (nunca misturar).
- **Linha do tempo dos beats:** blocos numerados com largura proporcional à duração. Cinza = rosto (A-roll + legenda), azul
  claro = overlay sobre o rosto, azul = cena de corte. Contas ao vivo: trechos escolhidos, **% de rosto** e **cortes por 10 s
  e por 100 palavras** (compare com a referência: rosto 14 a 21 %, 2,1 a 2,6 cortes por 10 s).
- **Um cartão por beat:** intervalo de tempo; caixa de observações; **opções A, B e C** (miniatura da Ref = só a FORMA, nome,
  categoria `Pxx · tipo`, descrição com o conteúdo DESTE vídeo, linha de **câmera**, `Ref V0X-A0Y` que abre a medida,
  selo "Minha sugestão", botão *Usar este*); à direita o **roteiro** do beat, o **player** do clipe posicionado no trecho e
  **Visto nos reels** (a justificativa, tirada do `mapa-roteiro-animacao.md`).

## Regras do painel (o gerador recusa o que as violar)
1. **Exatamente 3 opções por beat** e **exatamente 1** com `"sug": true`. Mesmo num beat óbvio, ofereça 3 caminhos reais.
2. Uma das opções deve ser **ficar no rosto com legenda** quando o mapa indicar que é plausível (anúncio, pergunta, virada,
   conclusão).
3. As opções vêm da **biblioteca** (`Ref` = id de uma pasta em `biblioteca/index.json`), nunca de gosto seu. Toda `Ref` tem de
   existir, ou o gerador para com a lista do que falta.
4. A miniatura mostra a FORMA. A **`desc` diz, com as palavras e o tema deste vídeo, com o que cada lacuna será preenchida**
   (ex.: "foto recortada de [objeto citado no beat], mesmo tratamento da Ref"). Nunca cite a imagem da referência como conteúdo.
5. Toda opção leva **`camera`**: em que palavra cai o pico da aproximação, onde a câmera para e como sai (G12.3). Opção de rosto:
   "Nenhuma". Opção com texto grande: dizer que a legenda some naquele plano. **A câmera medida na `notes.md` da Ref manda.**
6. Se o usuário já pediu algo num corte anterior do mesmo vídeo, a sugestão passa a ser o que ele pediu, com `nota_sug` dizendo isso.
7. Linha do tempo com 3 cores descreve mal um estilo com ≈ 80 % de tela cheia: avise o usuário que "azul" é a maior parte.

## Esquema do `03-plano/beats.json`
```json
{
  "titulo": "Título do vídeo",
  "clipe": "../02-corte/clipe-limpo.mp4",          // caminho do clipe JÁ CORTADO, relativo a 03-plano/
  "fonte": "bruto.mp4 (2560x1440, 40,9 s) → corte limpo 1080x1920, 39,3 s, 23,976 fps",
  "estilo": "Estilo Curiosidades (referência @fineasjackson)",
  "duracao_ms": 39289,
  "referencia": {"rosto_pct": [14, 21], "cortes_10s": [2.1, 2.6]},
  "perfil_padrao": "V03",
  "rodada": 1,                                      // aumente a cada nova rodada do mesmo vídeo
  "beats": [{
    "n": 2, "ini": 960, "fim": 3178,                // ms NO CLIPE JÁ CORTADO
    "tipo": "LI · lista / NU · número",             // tipo(s) de fala (mapa, "Tipos de fala"); só exibição
    "fala": "três ferramentas de IA totalmente gratuitas",
    "visto": "R7: o objeto-tema nomeado sozinho puxa disco creme com recorte (V01, V03). R6: lista de 3 itens nunca fica no rosto.",
    "nota_sug": "(opcional) por que a sugestão mudou",
    "opcoes": [
      {"k": "A", "sug": true, "tipo": "cena", "entrada": "corte",
       "nome": "Três discos creme, um por ferramenta + etiqueta", "cat": "P14 + P05 · cena de corte",
       "refs": ["V01-A28", "V04-A09"],
       "desc": "Três discos creme entram um a um (em “três”, “ferramentas”, “de IA”), cada um com o recorte do ícone oficial de uma ferramenta…",
       "camera": "Repouso de +3 %/s; pico em “gratuitas”, quando a etiqueta cola (+25 %/s com freio longo); corta andando."},
      {"k": "B", "tipo": "cena", "entrada": "corte", "…": "…"},
      {"k": "C", "tipo": "rosto", "entrada": "corte", "…": "…"}
    ]
  }]
}
```
- `tipo` da opção: `cena` (tela cheia) · `rosto` (A-roll) · `overlay` (peça sobre o rosto) · `segue` (continua a cena do beat anterior).
- `entrada`: `corte` (corte seco) ou `movimento` (troca por empurrão, cobertura, chicote, sem corte).
- Um exemplo completo e funcionando: `exemplo/edicao-exemplo/03-plano/beats.json` (16 beats, 48 opções).

## Como escolher as 3 opções de um beat
1. Classifique a fala do beat pelos **tipos de fala** do `mapa-roteiro-animacao.md` (seção 1) e leia a **tabela de recomendação
   por beat** (seção 8) e as **regras de colocação** (seção 3).
2. Para cada tipo, pegue 3 princípios plausíveis e **uma Ref concreta de cada** (a que melhor casa com o conteúdo do beat).
3. Leia o `notes.md` de cada Ref antes de propor: a descrição e a câmera da opção saem da MEDIDA, não da imagem.
4. Marque como sugestão a que o mapa mais cita para aquele tipo de fala, e diga por quê em `visto`.
5. Confira o conjunto: ≈ 80 % de tela cheia, 2,1 a 2,6 cortes por 10 s, nada abaixo do piso de leitura.

## Colar o plano de volta
O botão *Copiar plano* gera texto com, por beat: tempo, fala, opção escolhida, Ref, câmera e observações; mais o perfil. Grave
em `03-plano/escolhas-rN.md`, grave o perfil em `03-plano/perfil.json` (`{"perfil": "V03"}`) e siga para as specs.
