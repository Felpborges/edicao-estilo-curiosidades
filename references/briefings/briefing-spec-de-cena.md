# Briefing · spec de construção de cenas

Modelo para delegar a escrita das **specs** (`04-specs/trecho-NN.md`) a um subagente. Preencha os `<…>` e cole no prompt do agente.
Também serve como o formato que você mesmo segue quando escreve a spec sem delegar.

---

Você vai transformar o que foi medido nos reels de referência do Estilo Curiosidades em uma **spec de construção** para
algumas cenas de um vídeo novo. Outro agente (o principal) escreve o código a partir da sua spec. Português do Brasil.

## Leia antes
1. `<SKILL>/SKILL.md` e `<SKILL>/references/decisoes-do-autor.md`.
2. `<SKILL>/references/folha-de-tempos.md` e `<SKILL>/references/molde-do-motor-00-globais.md`.
3. Os `<SKILL>/biblioteca/<ID …>/notes.md` das Refs do seu pedido (e a seção do guia em `<SKILL>/references/principios/`).

## O vídeo novo
- Clipe limpo: 1080x1920, <fps> fps (1 quadro = <ms> ms), <N> quadros, <duração> s.
- Tema: "<tema>".
- Trechos e opção escolhida em cada um: `<EDIÇÃO>/03-plano/beats.json` (em cada trecho vale a opção com `"sug": true`, a menos
  que `<EDIÇÃO>/03-plano/escolhas-rN.md` diga outra).
- Palavras com tempo: `<EDIÇÃO>/02-corte/palavras-ataque.json` (`ataque_ms` = início reconferido no áudio; `ini_ms`, `fim_ms`
  = transcrição). Escreva os gatilhos como "N ms antes/depois do início da palavra X (índice i)", nunca só em tempo absoluto.

## Regras
- **Forma copiada, conteúdo novo.** A forma vem da nota da referência (posição, tamanho, giro, cor, sombra, duração de entrada,
  curva, sincronia). O conteúdo é do tema do usuário; nenhuma imagem, texto ou objeto da referência entra. Descreva cada lacuna
  pelo papel e diga com que conteúdo DESTE vídeo ela é preenchida.
- **Vale a nota** quando ela discordar do guia. As notas trazem marcas "(remedido, f123)".
- **Reconfira** as 2 ou 3 medidas que mais pesam em cada referência (tamanho da peça principal, nº de quadros da entrada,
  giro) e diga se bateu. Os `strip.jpg` e clipes não estão na skill: confira pela nota e pelo `thumb.jpg`.
- **Conversão:** o guia e as notas estão em px ou % de 720x1280 e em quadros da referência (V01 = 24 fps; V02 a V05 = 23,976).
  Entregue em **px de 1080x1920** (px × 1,5) e em **ms**, com quadros do clipe entre parênteses.
- **Piso de leitura** (adotado): cena de tela cheia ≥ 1,5 s; texto parado ≥ 700 ms depois da última palavra; imagem de série
  ≥ 1,2 s; último item de lista ≥ 700 ms. As durações de animação não mudam. Se o tempo da fala não permitir, diga onde e
  proponha a solução que preserva a sincronia (juntar as peças num plano contínuo, não esticar a cena).
- **Fala mais rápida que a referência:** a peça entra na palavra (a sincronia manda) e você registra a diferença.
- **Câmera:** a MEDIDA na nota da Ref manda; depois a linha "Câmera" aprovada no painel; depois a regra G12.3.
- Marque cada número como **medido**, **observado** ou **inferido**. O que a nota não traz: "não medido".
- **Proibido:** ffmpeg em vídeo, whisper, render ou qualquer comando pesado (isso é do principal, pela trava). Não altere arquivos
  fora de `<EDIÇÃO>/04-specs/`.

## O que gravar
Um arquivo por trecho em `<EDIÇÃO>/04-specs/trecho-NN.md`, neste formato (exemplos reais: `<SKILL>/exemplo/edicao-exemplo/04-specs/`):

```
# Trecho NN · <nome da opção> · <princípios> · Ref <IDs>
Fala: "…"   ·   Janela no clipe: <ini> a <fim> ms   ·   Entra por: corte seco | movimento

## 1 · Linha do tempo da cena (relativa às palavras)
| passo | o que acontece | gatilho (palavra, índice, deslocamento em ms) | duração (ms · quadros) | curva |
(entrada da cena, cada peça, cada etiqueta, cada traço, movimento de câmera, saída)

## 2 · FORMA (copiar igual) — px de 1080x1920
- Fundo / mesa: cor(es) hex, luz, vinheta
- Cada peça: posição do centro (x, y), largura × altura, giro (graus, sentido), borda (px, cor), sombra, cantos, ordem de
  empilhamento, o que sangra a borda do quadro
- Câmera: tipo (deriva, zoom, pan), taxa (%/s ou px/quadro), de quando a quando, curva, se corta em movimento
- Entrada e saída de cada peça: de onde, valores quadro a quadro quando a nota tiver (ex.: ×1,12 → ×1,04 → ×1,00), degraus de 1
  ou 2 quadros, borrão
- Texto (se houver): fonte e alternativa, peso, caixa, tamanho px, cor, entrelinha
- Taxa de imagem da cena (24 ou 12 imagens/s)
- Confiança de cada item

## 3 · CONTEÚDO (deste vídeo)
| lacuna (papel) | preenchida com | receita de tratamento (tipo, enquadramento, recorte, fundo, paleta, textura, contorno, sombra) |

## 4 · IMAGENS NECESSÁRIAS
| # | o que é, exatamente | papel | de onde pode vir (captura do usuário / site oficial / acervo público) | formato e tamanho mínimo | tratamento a aplicar |

## 5 · Piso de leitura e ritmo
(quanto cada peça fica na tela; o que fica abaixo do piso; solução)

## 6 · Dúvidas e o que não foi possível medir
```

## O que devolver (no máximo 20 linhas)
Arquivos gravados; por trecho, 2 linhas com o essencial da forma; o que você reconferiu e se bateu; onde o piso de leitura não
fecha; dúvidas. Não cole o conteúdo dos arquivos.
