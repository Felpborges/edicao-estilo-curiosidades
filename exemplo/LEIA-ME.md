# Exemplo: uma edição real completa (sem mídia)

`edicao-exemplo/` é a edição de um reel de 39 s ("Claude lançou Slides, Docs e Design"), feita com este método e entregue
em 4 cortes. **É material de estudo: congelado, não é um modelo para copiar o conteúdo.** Estão aqui o texto e o
código; não estão o vídeo bruto, o clipe cortado, as imagens nem os renders (≈ 400 MB).

| pasta | o que mostra |
|---|---|
| `02-corte/` | o que sai do corte limpo: `cortes.md` (o que foi cortado e onde), `palavras-ataque.json` (início de cada palavra), `legenda-ajustes.json` |
| `03-plano/` | `beats.json` (16 trechos, 48 opções, 16 sugestões), `plano-de-edicao.html` (o painel pronto; abra pelo `servidor_painel.py`), `escolhas-r2.md` (o que o usuário colou de volta), `perfil.json` |
| `04-specs/` | `00-globais.md` (valores comuns, em px de 1080x1920) e `trecho-NN.md` (a spec de cada cena: linha do tempo nas palavras, FORMA, CONTEÚDO, imagens, piso de leitura) · `LISTA-DE-IMAGENS.md` |
| `05-cenas-r2/` | `base.py` e os `plano_*.py` (o código de cada cena) + `auditoria-r2-*.md` (gatilho pedido × quadro no render, medidas, piso de leitura) |
| `05-imagens/` | `trata.py`: como as imagens reais foram tratadas |
| `06-render/` | `CHECKLIST-corte-04.md`: medidas, sincronia evento a evento, os 15 itens e o que NÃO foi verificado |
| `07-som/` | `som.py`: o som do reel (voz −14 LUFS + 4 efeitos), pelo molde de `references/som.md` |

Observações:
- O painel de exemplo abre e funciona, mas os players do vídeo e as miniaturas ficam vazios (o clipe cortado e os quadros das referências não vêm junto).
- As specs citam caminhos do computador do autor (`Estilo 03 - …`); leia-os como "a biblioteca e o guia desta skill".
- Para rodar o motor sobre uma edição, ela precisa ter `02-corte/clipe-limpo.mp4`, `palavras-ataque.json` e `cortes.json`; aqui só
  os dois últimos estão.
- Esta edição tem uma 1ª rodada (`05-cenas`, perfil antigo) que não foi incluída; a pasta `05-cenas-r2` é a rodada final.
