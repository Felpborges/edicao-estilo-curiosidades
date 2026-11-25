# Imagens: o maior trabalho deste estilo

Quase toda cena precisa de **imagem real do tema do usuário**, tratada pela receita da referência. O estilo é um documentário
em colagem: o apresentador aparece pouco e o resto é imagem real tratada como papel sobre uma mesa escura. Sem imagem real,
o resultado não é o estilo.

## Regra-mãe: forma fixa, conteúdo variável
- **Forma (fixa, copiada com precisão):** composição, posições, tamanhos, giro, borda, sombra, textura, tipo e duração de cada
  animação, curvas, cadência, sincronia, som. Está nas `notes.md` das Refs e no guia.
- **Conteúdo (variável, sempre do tema do usuário):** qual foto, qual print, qual documento, qual logo, qual palavra, qual número.
- **Nenhum `thumb.jpg`, quadro, clipe ou asset da referência entra no vídeo.** As miniaturas servem só para o usuário ver a forma.
- **Receita de tratamento é forma.** Cada lacuna de imagem leva a receita (tipo: foto, print, documento, mapa, logo; enquadramento;
  recorte; fundo; paleta; textura; contorno; sombra; nível de detalhe), que garante que uma imagem nova, de outro tema, fique
  com a mesma cara. A receita global está em `design-system.md` (G5) e a de cada princípio na seção "Construção" e "Conteúdo"
  de `principios/Pxx-*.md`.
- **Regra de escolha:** a referência decide O QUE mostrar pelo que é dito. Dado concreto vira imagem (123 de 128 frases):
  objeto literal, pessoa citada, documento, número, lugar. Ver `mapa-roteiro-animacao.md` seção 4.
- **Teste de generalização:** se uma regra só se explica citando a imagem original, ela está mal extraída; releia a nota.

## De onde vêm as imagens (do mais forte para o mais fraco)
1. **Captura de tela do próprio usuário** (a prova mais forte: é o produto, a conversa, o resultado dele). Peça ao usuário, com a
   lista do que capturar e o tamanho mínimo (modelo: `exemplo/edicao-exemplo/04-specs/LISTA-DE-IMAGENS.md`, parte A).
2. **Logo ou ícone oficial** da marca citada, do site oficial (uso editorial). Prefira SVG ou PNG com transparência.
3. **Wikimedia Commons e acervos de domínio público ou licença aberta**, com a licença conferida e anotada.
4. **Foto ou documento do próprio usuário.**
5. Imagem **gerada por IA** só quando a fala NÃO cita nada real e específico, e nunca imagem "de mentira" que pareça real
   (cédula falsa, print falso, rosto de pessoa real, documento forjado).
Nada de imagem genérica de banco quando a fala cita uma coisa específica.

## Antes de baixar
**Baixar arquivo da internet exige o "sim" do usuário.** Peça uma vez, com a lista: nome do arquivo, fonte, licença e tamanho
(modelo: parte B da lista do exemplo). Respeite direitos autorais e marcas: uso editorial de logos é diferente de usar a
marca como se fosse sua. Dados e telas de terceiros (e-mail, nome, cliente) **nunca** aparecem: confira antes de capturar.
Se a captura exigir esconder algo (aviso, barra lateral, outros chats), diga que foi escondido só para a captura.

## Fato antes de imagem
Confira o fato que a imagem sustenta. No exemplo, a fala dizia "pra PowerPoint ou pra Google Slides", mas o produto exportava
só para PowerPoint; no corte o Google Slides aparece só como logo, sem simular uma exportação que não existe.

## Tratar (o `trata.py` do exemplo é o modelo)
`exemplo/edicao-exemplo/05-imagens/trata.py` mostra o padrão: `originais/` → `tratadas/<nome>.png`, cada entrada dizendo de onde
veio o arquivo e que tratamento recebeu (recorte justo, fundo removido, dessaturação parcial de cédula, ampliação por Lanczos,
alfa). Nada é redesenhado.
- **Recorte de fundo** (rembg/u2net/isnet) é pesado: rode pela trava `leve.py`.
- **PDF → PNG:** o exemplo usou um script de macOS; em qualquer sistema use `pdftoppm -r 150 -png arquivo.pdf pasta/pag`
  (poppler) ou PyMuPDF.
- O motor procura `05-imagens/tratadas/<nome>.(png|jpg|jpeg|webp)` pelo nome que o plano pede (`ctx.img(nome, …)` e
  `ctx.rgba(nome, …)`). Sem o arquivo, entra uma **provisória cinza com rótulo** com a proporção certa, e
  `monta.py --render --final` **recusa a entrega** enquanto houver provisória.
- Print muito branco (luma ≈ 250) corta o grão vivo no branco: o grão fica com metade da força. Avise.
- Logo pequeno ampliado (ex.: 192 px × 2,5) é a imagem mais fraca do lote: busque SVG.
