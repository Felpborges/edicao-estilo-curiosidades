#!/usr/bin/env python3
"""trata.py · prepara as imagens reais desta edição: originais/ → tratadas/ (nomes que os planos pedem).
Cada entrada diz de onde veio o arquivo. Nada é redesenhado: só recorte, fundo removido e redimensionamento.
Rodar: python3 trata.py   (leve)"""
import os, cv2, numpy as np
AQUI = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(AQUI, 'originais'); T = os.path.join(AQUI, 'tratadas')
os.makedirs(T, exist_ok=True)
feito = []

def salva(nome, im): cv2.imwrite(os.path.join(T, nome + '.png'), im); feito.append((nome, im.shape))
def existe(f): return os.path.exists(os.path.join(O, f))

# cédula de US$ 100 (frente, série 2009) · Wikimedia Commons, domínio público (obra do governo dos EUA)
# spec trecho-03: recorte justo, cor original dessaturada com os detalhes de cor ainda legíveis (grau não medido: 45 %)
if existe('nota-100-wikimedia.jpg'):
    n = cv2.imread(os.path.join(O, 'nota-100-wikimedia.jpg')).astype(np.float32)
    cinza = cv2.cvtColor(n.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)[..., None]
    n = n * 0.55 + cinza * 0.45
    salva('nota-100', np.dstack([np.clip(n, 0, 255).astype(np.uint8), np.full(n.shape[:2], 255, np.uint8)]))

# ícone oficial do Gamma · static.gamma.app/favicons/favicon_light.svg (convertido em PNG de 1600 px, fundo branco)
if existe('gamma-icone-1600.png'):
    g = cv2.imread(os.path.join(O, 'gamma-icone-1600.png'))[:, :, :3]
    nb = (g.min(axis=2) < 245).astype(np.uint8)                      # o que não é o branco do fundo
    ys, xs = np.where(nb); x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    g = g[y0:y1, x0:x1]; d = min(g.shape[:2])
    m = np.zeros(g.shape[:2], np.uint8); cv2.circle(m, (g.shape[1] // 2, g.shape[0] // 2), d // 2 - 1, 255, -1, cv2.LINE_AA)
    salva('logo-gamma', np.dstack([g, m]))                           # o ícone é um disco: alfa = o próprio disco

# ícone oficial do Canva · static.canva.com/.../android-192x192-2.png (192 px, já com alfa; ampliado 2,5× por Lanczos)
if existe('canva-icone-192.png'):
    c = cv2.imread(os.path.join(O, 'canva-icone-192.png'), cv2.IMREAD_UNCHANGED)
    salva('logo-canva', cv2.resize(c, (480, 480), interpolation=cv2.INTER_LANCZOS4))

# logos do PowerPoint e do Google Slides · Wikimedia Commons, domínio público (marcas registradas dos donos)
for src, dst in (('logo-powerpoint.png', 'logo-powerpoint'), ('logo-google-slides.png', 'logo-google-slides'), ('logo-instagram.png', 'logo-instagram')):
    if existe(src): salva(dst, cv2.imread(os.path.join(O, src), cv2.IMREAD_UNCHANGED))

# ───────── capturas da conta do Felipe no claude.ai (Claude no Chrome, 20/11/2026, com a autorização dele) ─────────
# Conversa nova "Apresentação comercial Grão Vizinho": negócio fictício de exemplo, dados inventados pelo próprio Claude.
# As capturas saem a 760x1085 px (janela estreita, zoom de página 1,6); nada foi redesenhado. Na tela inicial ficaram
# escondidos só o aviso de um conector de terceiros, a sugestão de vídeo e os artefatos recentes (dados da conta).
le = lambda f: cv2.imread(os.path.join(O, f))
def rec(im, x0, y0, w, h, lw=None, lh=None):
    c = im[y0:y0 + h, x0:x0 + w]
    return cv2.resize(c, (lw, lh), interpolation=cv2.INTER_LANCZOS4) if lw else c
alfa = lambda im: np.dstack([im, np.full(im.shape[:2], 255, np.uint8)])

if existe('01-pedido-digitado.png'):                       # caixa de mensagem com o pedido digitado, sem enviar (trecho 7)
    salva('print-pedido', rec(le('01-pedido-digitado.png'), 24, 0, 711, 1085, 1080, 1649))
if existe('02-chat.png'):                                  # tela inicial do chat (trecho 5)
    salva('print-chat', rec(le('02-chat.png'), 29, 0, 702, 1085, 1180, 1824))
for n in range(1, 13):                                     # os 12 slides do deck feito no Claude Slides (PDF baixado → PNG 1920x1080)
    f = f'03-slides/slide-{n:02d}.png'
    if existe(f): salva(f'slide-{n:02d}', le(f))
if existe('03-slides/slide-01.png'): salva('card-slides', le('03-slides/slide-01.png'))        # capa (trecho 4)
if existe('03-slides/slide-07.png'): salva('print-slides', alfa(le('03-slides/slide-07.png')))  # slide de número grande (trechos 2 e 15)
if existe('05-roteiro-claude-docs.png'):                   # o roteiro aberto no Claude Docs
    d = le('05-roteiro-claude-docs.png')
    salva('card-docs', rec(d, 0, 225, 618, 412))                    # 3:2 (trecho 4)
    salva('print-docs', alfa(rec(d, 72, 150, 407, 935)))            # vertical 1:2,3 (trechos 2 e 15)
    salva('print-roteiro', rec(d, 53, 240, 565, 269, 1130, 538))    # 2,1:1 (trecho 12)
if existe('08-carrossel-claude-design.png'):               # o carrossel aberto no Claude Design (trecho 4)
    salva('card-design', rec(le('08-carrossel-claude-design.png'), 0, 394, 780, 439))
if existe('06-conversa-pedido-roteiro.png'):               # a mesma conversa, com o pedido do roteiro (trecho 12)
    salva('print-conversa-roteiro', rec(le('06-conversa-pedido-roteiro.png'), 0, 80, 760, 950))
for n in (1, 2):                                           # cartões do carrossel feito no Claude Design (PDF → PNG 1080x1350)
    f = f'09-carrossel/slide-{n:02d}.png'
    if existe(f): salva(f'carrossel-{n}', le(f))
if existe('09-carrossel/slide-01.png'): salva('print-design', alfa(le('09-carrossel/slide-01.png')))  # trechos 2 e 15
if existe('07-conversa-final.png'):                        # fim da conversa, com o campo de resposta (trecho 15)
    salva('print-conversa-final', rec(le('07-conversa-final.png'), 0, 320, 760, 765))
if existe('10-interface-conversa-e-design.png'):          # a interface inteira: conversa à esquerda, Claude Design à direita (fecho, trecho 15)
    salva('print-interface', rec(le('10-interface-conversa-e-design.png'), 0, 0, 868, 868))   # 1:1; captura a 1384x868, zoom de página 1,3
if existe('04-menu-download.png'):                         # menu de download do Claude Slides: PDF, PNG, PowerPoint (trecho 10)
    salva('print-powerpoint', rec(le('04-menu-download.png'), 0, 40, 780, 488))

for n, s in feito: print(f'{n:22} {s[1]}x{s[0]}  canais {s[2]}')
