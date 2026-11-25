#!/usr/bin/env python3
"""pecas.py · fábricas das peças do Estilo 03 (valores de `04-specs/00-globais.md`; px de 1080x1920).

Todas devolvem RGBA uint8 (canais em ordem B, G, R, A, como o OpenCV), com alfa reto.
Nada aqui altera a cor da imagem de origem: o estilo usa a imagem real como ela é.
"""
import os, sys, math
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import perfis

def bgr(h):
    h = h.lstrip('#'); return (int(h[4:6], 16), int(h[2:4], 16), int(h[0:2], 16))


def do_guia(h):
    """Converte um hex LIDO NO TREINO (guia, notas, specs) na cor real a pôr no quadro.
    Os reels de referência são BT.709, mas os hex do treino foram lidos por um caminho JPG que decodifica como
    BT.601: neutros não mudam, cores saturadas saem deslocadas (o amarelo da legenda, lido #f0eb32, é #f3e12a).
    Conferido em 20/11/2026: cor convertida → codificada como o vídeo final → lida pelo caminho do treino = hex do guia.
    TODO hex que vier do guia, de uma nota ou de uma spec passa por aqui antes de virar pixel."""
    hh = h.lstrip('#'); rgb = np.array([int(hh[i:i + 2], 16) for i in (0, 2, 4)], float)
    def m(kr, kb):
        kg = 1 - kr - kb
        return np.array([[kr, kg, kb], [-kr / (2 * (1 - kb)), -kg / (2 * (1 - kb)), 0.5], [0.5, -kg / (2 * (1 - kr)), -kb / (2 * (1 - kr))]])
    t = np.linalg.inv(m(0.2126, 0.0722)) @ (m(0.299, 0.114) @ rgb)
    return '#%02x%02x%02x' % tuple(int(round(min(255, max(0, v)))) for v in t)


# cores de molde (00-globais.md), já convertidas para a cor real
BORDA_CARTAO = do_guia('#e8e6e0')
CONTORNO_RECORTE = do_guia('#e6e2da')
DISCO = do_guia('#d9d3c7')
ETIQUETA = do_guia('#b5b1a8')
TINTA = '#111111'
MARCA_MAO = do_guia('#e0b830')      # amarelo-ouro (decisão adotada no treino; o P19 mede #e8d840 no V03)
MARCA_TEXTO = do_guia('#efcb3b')
LEGENDA = do_guia('#f0eb32')


def fonte(corpo, negrito=True):
    """Inter Bold embutida em motor/fontes/ (aberta, multiplataforma). Sem ela, cai para a do sistema e avisa."""
    cand = [os.path.join(AQUI, 'fontes', 'Inter-Bold.ttf' if negrito else 'Inter-Regular.ttf'),
            '/System/Library/Fonts/Supplemental/Arial Bold.ttf' if negrito else '/System/Library/Fonts/Supplemental/Arial.ttf',
            'C:/Windows/Fonts/arialbd.ttf' if negrito else 'C:/Windows/Fonts/arial.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']
    for c in cand:
        if os.path.exists(c):
            return ImageFont.truetype(c, corpo), os.path.basename(c)
    return ImageFont.load_default(), 'padrão do Pillow'


def papel(w, h, cor, grao=4, semente=1):
    """Papel liso com grão fino monocromático (±grao níveis).
    Com um perfil do reestudo ativo, o papel ganha o PONTILHADO FIXO medido na referência (`papel_fixo`, em níveis de
    desvio a 720 px): ruído de ≈ 1 px levemente amaciado, preso à peça (anda com ela). O grão VIVO vem por cima, na Cena."""
    P = perfis.ativo()
    if not P.get('antigo'):
        return papel_fixo(w, h, cor, P['papel_fixo'] * P.get('ganho_papel', 1.0), semente)
    rng = np.random.default_rng(semente)
    r = rng.normal(0, grao / 2, (h, w, 1)).astype(np.float32)
    r = cv2.GaussianBlur(r, (0, 0), 0.6)[..., None] if r.ndim == 3 and False else r
    base = np.array(bgr(cor), np.float32)[None, None]
    return np.clip(base + r, 0, 255).astype(np.uint8)


# fator que leva o desvio pedido (medido a 720 px, com passa-alta de σ=2, depois de codificar) ao ruído gerado a 1080 px.
# Calibrado em 20/11/2026 com `motor/calibra_grao.py` (ver ESTADO-EDICAO.md).
CAL_PAPEL = 1.45
def papel_fixo(w, h, cor, desvio, semente=1, desfoque=0.9):
    rng = np.random.default_rng(semente)
    r = rng.standard_normal((h, w)).astype(np.float32)
    r = cv2.GaussianBlur(r, (0, 0), desfoque); r /= max(1e-6, float(r.std()))
    base = np.array(bgr(cor), np.float32)[None, None]
    # o pontilhado é do papel: multiplica a cor (papel mais escuro = pontilhado mais fraco). `desvio` vale para o papel
    # claro da medida (luma ≈ 207, o disco da referência).
    return np.clip(base * (1 + (r * desvio * CAL_PAPEL / 207.0)[..., None]), 0, 255).astype(np.uint8)


def com_sombra(rgba, tipo='cartao', sombra=None, k=1.0):
    """Acrescenta a sombra do perfil ativo a uma peça RGBA: preta, multiplicada, caída para baixo (longa embaixo, média dos
    lados, quase nada em cima). `tipo`: 'cartao', 'recorte', 'disco', 'etiqueta'. Perfil sem sombra (V04) devolve a peça igual.
    A peça cresce de uma margem transparente; o centro continua no centro.
    `k` = fator em que a peça foi desenhada (peça feita K× maior e posta na cena com escala 1/K): a sombra é feita K× maior
    para ficar com o tamanho certo na TELA."""
    sp = sombra if sombra is not None else perfis.ativo().get('sombra_' + tipo)
    if not sp: return rgba
    dy, sg, op = int(round(sp['dy'] * k)), float(sp['sigma']) * k, float(sp['op'])
    m = int(math.ceil(dy + 3 * sg)) + 2
    a = rgba[:, :, 3].astype(np.float32) / 255.0
    h, w = a.shape
    A = np.zeros((h + 2 * m, w + 2 * m), np.float32); A[m:m + h, m:m + w] = a
    S = np.zeros_like(A); S[m + dy:m + dy + h, m:m + w] = a
    S = cv2.GaussianBlur(S, (0, 0), sg) * op
    cor = np.zeros((h + 2 * m, w + 2 * m, 3), np.float32); cor[m:m + h, m:m + w] = rgba[:, :, :3]
    at = A + S * (1 - A)
    out = np.dstack([np.where(at[..., None] > 1e-4, cor * A[..., None] / np.maximum(at[..., None], 1e-4), 0), at * 255])
    return np.clip(out, 0, 255).astype(np.uint8)


def _cobre(img, w, h):
    """Redimensiona e corta a imagem para preencher w x h (cover), sem deformar."""
    ih, iw = img.shape[:2]
    k = max(w / iw, h / ih)
    nw, nh = max(w, int(round(iw * k))), max(h, int(round(ih * k)))
    r = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_AREA if k < 1 else cv2.INTER_LANCZOS4)
    x0, y0 = (nw - w) // 2, (nh - h) // 2
    return r[y0:y0 + h, x0:x0 + w]


def _sombra(alfa, dx, dy, desfoque, opacidade, margem):
    """Camada de sombra preta a partir de um alfa (float 0..1), já com margem em volta."""
    h, w = alfa.shape
    s = np.zeros((h + 2 * margem, w + 2 * margem), np.float32)
    s[margem + dy:margem + dy + h, margem + dx:margem + dx + w] = alfa
    return cv2.GaussianBlur(s, (0, 0), desfoque) * opacidade


def _junta(rgb, alfa, sombra, margem):
    """Põe (rgb, alfa) sobre a sombra; devolve RGBA com a margem."""
    h, w = alfa.shape
    out = np.zeros((h + 2 * margem, w + 2 * margem, 4), np.float32)
    a = np.zeros((h + 2 * margem, w + 2 * margem), np.float32); a[margem:margem + h, margem:margem + w] = alfa
    cor = np.zeros((h + 2 * margem, w + 2 * margem, 3), np.float32); cor[margem:margem + h, margem:margem + w] = rgb
    at = a + sombra * (1 - a)
    out[..., :3] = np.where(at[..., None] > 1e-4, cor * a[..., None] / np.maximum(at[..., None], 1e-4), 0)
    out[..., 3] = at * 255
    return np.clip(out, 0, 255).astype(np.uint8)


def cartao(img_bgr, largura, altura=None, borda=12, cor_borda=BORDA_CARTAO, em_pilha=False):
    """Imagem real em cartão de cantos retos: borda de papel + 1 px escuro colado (40 %).
    `largura`/`altura` são o tamanho TOTAL do cartão. `em_pilha` acrescenta a sombra curta (0, +3; 4 px; 35 %)."""
    P = perfis.ativo()
    if not P.get('antigo'): return cartao_do_perfil(img_bgr, largura, altura)
    largura = int(round(largura))
    if altura is None:
        ih, iw = img_bgr.shape[:2]; altura = int(round((largura - 2 * borda) * ih / iw)) + 2 * borda
    altura = int(round(altura))
    c = np.empty((altura, largura, 3), np.uint8); c[:] = bgr(cor_borda)
    c[borda:altura - borda, borda:largura - borda] = _cobre(img_bgr[:, :, :3], largura - 2 * borda, altura - 2 * borda)
    m = 1 if not em_pilha else 14
    alfa = np.ones((altura, largura), np.float32)
    fio = np.zeros((altura + 2 * m, largura + 2 * m), np.float32)
    fio[m - 1:m + altura + 1, m - 1:m + largura + 1] = 0.40                       # 1 px escuro em volta
    if em_pilha: fio = np.maximum(fio, _sombra(alfa, 0, 3, 4, 0.35, m))
    return _junta(c.astype(np.float32), alfa, fio, m)


def cartao_do_perfil(img_bgr, largura, altura=None, semente=21, sombra=True, k=1.0):
    """Imagem real em cartão, com o acabamento do perfil ativo: borda de papel (largura e cor do perfil, com o pontilhado
    fixo), fio escuro de 1 px por fora e por dentro quando o perfil tem, canto vivo, e a sombra do perfil caída para baixo.
    `largura`/`altura` são o tamanho TOTAL do cartão (sem a sombra). A imagem entra como é: nada muda a cor dela.
    `k` = fator em que o cartão é desenhado (cartão feito K× maior e posto na cena com escala 1/K, para aguentar zoom):
    borda, fio e sombra saem K× maiores, para terem o tamanho do perfil na TELA."""
    P = perfis.ativo(); B = P['borda']; b = int(round(B['px'] * k)); fio = max(1, int(round(k)))
    largura = int(round(largura))
    if altura is None:
        ih, iw = img_bgr.shape[:2]; altura = int(round((largura - 2 * b) * ih / iw)) + 2 * b
    altura = int(round(altura))
    c = papel_fixo(largura, altura, do_guia(B['cor']), P['papel_fixo'] * P.get('ganho_papel', 1.0), semente).astype(np.float32)
    c[b:altura - b, b:largura - b] = _cobre(img_bgr[:, :, :3], largura - 2 * b, altura - 2 * b)
    if B.get('fio_dentro'):                                   # fio escuro de 1 px entre a borda e a imagem
        kf = 1 - B['fio_dentro']
        c[b - fio:b, b - fio:largura - b + fio] *= kf; c[altura - b:altura - b + fio, b - fio:largura - b + fio] *= kf
        c[b - fio:altura - b + fio, b - fio:b] *= kf; c[b - fio:altura - b + fio, largura - b:largura - b + fio] *= kf
    rgba = np.dstack([np.clip(c, 0, 255), np.full((altura, largura), 255, np.float32)]).astype(np.uint8)
    if B.get('fio_fora'):                                     # fio escuro de 1 px colado por fora
        f = np.zeros((altura + 2 * fio, largura + 2 * fio, 4), np.uint8); f[..., 3] = int(255 * B['fio_fora'])
        f[fio:-fio, fio:-fio] = rgba; rgba = f
    return com_sombra(rgba, 'cartao', k=k) if sombra else rgba


def recorte_do_perfil(rgba, altura=None, largura=None, semente=9, sombra=True):
    """Recorte-adesivo com o contorno do perfil ativo (V03: branco de papel, 7–14 px, ONDULADO; V01: 8–10 px, de tesoura;
    V04: nenhum) e a sombra do perfil. `altura`/`largura` medem a figura sem o contorno. Entrada: BGRA com fundo removido."""
    P = perfis.ativo(); C = P.get('contorno')
    ih, iw = rgba.shape[:2]
    k = (altura / ih) if altura else (largura / iw)
    w, h = max(1, int(round(iw * k))), max(1, int(round(ih * k)))
    fig = cv2.resize(rgba, (w, h), interpolation=cv2.INTER_AREA if k < 1 else cv2.INTER_LANCZOS4).astype(np.float32)
    if not C:
        out = fig.astype(np.uint8)
        return com_sombra(out, 'recorte') if sombra else out
    r0, var = float(C['px']), float(C.get('var', 0))
    m = int(math.ceil(r0 + var)) + 4
    a = np.zeros((h + 2 * m, w + 2 * m), np.float32); a[m:m + h, m:m + w] = fig[..., 3] / 255.0
    cor_fig = np.zeros((h + 2 * m, w + 2 * m, 3), np.float32); cor_fig[m:m + h, m:m + w] = fig[..., :3]
    dist = cv2.distanceTransform((a < 0.5).astype(np.uint8), cv2.DIST_L2, 5)        # distância até a figura
    rng = np.random.default_rng(semente)
    onda = cv2.GaussianBlur(rng.standard_normal(a.shape).astype(np.float32), (0, 0), 14); onda /= max(1e-6, float(np.abs(onda).max()))
    raio = r0 + var * onda                                                          # contorno de largura que varia (tesoura à mão)
    ac = np.clip(raio - dist + 0.5, 0, 1)
    ac = np.maximum(cv2.GaussianBlur(ac, (0, 0), 0.7), a)
    base = papel_fixo(a.shape[1], a.shape[0], do_guia(C['cor']), P['papel_fixo'] * 0.6, semente + 1).astype(np.float32)
    rgb = cor_fig * a[..., None] + base * (1 - a[..., None])
    out = np.dstack([rgb, ac * 255]).clip(0, 255).astype(np.uint8)
    return com_sombra(out, 'recorte') if sombra else out


def disco_do_perfil(diametro, cor=None, semente=7, sombra=True):
    """Disco de papel do perfil ativo: cor do perfil, pontilhado fixo forte (o grão vivo vem por cima, na Cena), sem aro,
    com a sombra do perfil (no V03 ela some sobre a mesa escura e aparece onde a mesa está iluminada)."""
    P = perfis.ativo()
    d = int(round(diametro)); ss = 4
    mask = np.zeros((d * ss, d * ss), np.uint8); cv2.circle(mask, (d * ss // 2, d * ss // 2), d * ss // 2 - ss, 255, -1)
    a = cv2.resize(mask, (d, d), interpolation=cv2.INTER_AREA)
    rgb = papel_fixo(d, d, do_guia(cor or P['disco']['cor']), P['papel_fixo'] * P.get('ganho_papel', 1.0), semente)
    out = np.dstack([rgb, a])
    return com_sombra(out, 'disco') if sombra else out


def recorte(rgba, altura=None, largura=None, contorno=15, cor=CONTORNO_RECORTE, sombra=True):
    """Recorte-adesivo: silhueta com contorno off-white uniforme + sombra fina (0, 2; 3 px; 45 %).
    `altura`/`largura` medem a figura sem o contorno. Entrada: BGRA com fundo já removido."""
    ih, iw = rgba.shape[:2]
    k = (altura / ih) if altura else (largura / iw)
    w, h = max(1, int(round(iw * k))), max(1, int(round(ih * k)))
    fig = cv2.resize(rgba, (w, h), interpolation=cv2.INTER_AREA if k < 1 else cv2.INTER_LANCZOS4).astype(np.float32)
    m = contorno + 12
    a = np.zeros((h + 2 * m, w + 2 * m), np.float32); a[m:m + h, m:m + w] = fig[..., 3] / 255.0
    cor_fig = np.zeros((h + 2 * m, w + 2 * m, 3), np.float32); cor_fig[m:m + h, m:m + w] = fig[..., :3]
    if contorno:
        ker = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * contorno + 1, 2 * contorno + 1))
        ac = cv2.GaussianBlur(cv2.dilate((a > 0.5).astype(np.float32), ker), (0, 0), 0.8)
    else: ac = a
    base = np.empty_like(cor_fig); base[:] = bgr(cor)
    rgb = cor_fig * a[..., None] + base * (1 - a[..., None])
    if sombra:                                             # sombra fina: o contorno deslocado (0, +2), desfocado 3 px, a 45 %
        s = cv2.GaussianBlur(cv2.warpAffine(ac, np.float32([[1, 0, 0], [0, 1, 2]]), (ac.shape[1], ac.shape[0])), (0, 0), 3) * 0.45
    else: s = np.zeros_like(ac)
    at = ac + s * (1 - ac)
    out = np.dstack([np.where(at[..., None] > 1e-4, rgb * ac[..., None] / np.maximum(at[..., None], 1e-4), 0), at * 255])
    return np.clip(out, 0, 255).astype(np.uint8)


def disco(diametro, cor=DISCO, grao=4, sombra=False, semente=7):
    """Disco de papel creme, sem aro, com grão fino. Sombra curta opcional (só o V01 tem)."""
    d = int(round(diametro)); ss = 4
    mask = np.zeros((d * ss, d * ss), np.uint8); cv2.circle(mask, (d * ss // 2, d * ss // 2), d * ss // 2 - ss, 255, -1)
    a = cv2.resize(mask, (d, d), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
    rgb = papel(d, d, cor, grao, semente).astype(np.float32)
    m = 12 if sombra else 0
    s = _sombra(a, 0, 3, 6, 0.35, m) if sombra else np.zeros((d, d), np.float32)
    return _junta(rgb, a, s, m)


def etiqueta(texto, visiveis=None, altura=84, cor=ETIQUETA, corpo=58, folga=33, tinta=TINTA, grao=4, semente=3):
    """Tira de papel com texto em caixa-alta. Nasce no comprimento do texto COMPLETO; `visiveis` = quantas
    palavras já aparecem (a referência revela palavra a palavra, a seco, sem a tira mudar)."""
    f, _ = fonte(corpo)
    texto = texto.upper(); pal = texto.split(' ')
    larg = int(round(f.getlength(texto))) + 2 * folga
    im = Image.fromarray(cv2.cvtColor(papel(larg, altura, cor, grao, semente), cv2.COLOR_BGR2RGB))
    d = ImageDraw.Draw(im)
    mostra = ' '.join(pal[:len(pal) if visiveis is None else visiveis])
    asc = f.getbbox('H'); y = (altura - (asc[3] - asc[1])) / 2 - asc[1]
    if mostra: d.text((folga, y), mostra, font=f, fill=tuple(reversed(bgr(tinta))))
    out = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    return np.dstack([out, np.full((altura, larg), 255, np.uint8)])


def elipse_mao(largura, altura, espessura=4.5, cor=MARCA_MAO, fracao=1.0, inclinacao=0.0, semente=5, sobra=0.06):
    """Elipse desenhada à mão (sentido horário a partir do alto, pontas que se cruzam, borda irregular).
    `fracao` de 0 a 1 = quanto do traço já foi desenhado (trim path)."""
    rng = np.random.default_rng(semente)
    m = int(espessura * 3 + 8); W_, H_ = int(largura + 2 * m), int(altura + 2 * m); ss = 3
    n = 220; total = 1 + sobra
    ang = -np.pi / 2 + np.linspace(0, 2 * np.pi * total, n)
    tre = 1 + 0.035 * np.sin(np.linspace(0, 5.3, n) + rng.uniform(0, 6)) + 0.012 * rng.standard_normal(n).cumsum() / 6
    esp = np.linspace(0, 1, n)[:, None]
    rx, ry = largura / 2 * tre * (1 - 0.05 * esp[:, 0]), altura / 2 * tre * (1 - 0.05 * esp[:, 0])   # fecha por dentro
    x, y = rx * np.cos(ang), ry * np.sin(ang)
    c, s = np.cos(np.radians(inclinacao)), np.sin(np.radians(inclinacao))
    px, py = (x * c - y * s + W_ / 2) * ss, (x * s + y * c + H_ / 2) * ss
    k = max(2, int(round(n * max(0.0, min(1.0, fracao)))))
    mask = np.zeros((H_ * ss, W_ * ss), np.uint8)
    if fracao > 0:
        for i in range(k - 1):
            e = espessura * ss * (1 + 0.18 * np.sin(i * 0.37 + semente))
            cv2.line(mask, (int(px[i]), int(py[i])), (int(px[i + 1]), int(py[i + 1])), 255, max(1, int(round(e))), cv2.LINE_AA)
    a = cv2.resize(mask, (W_, H_), interpolation=cv2.INTER_AREA)
    out = np.empty((H_, W_, 4), np.uint8); out[..., :3] = bgr(cor); out[..., 3] = a
    return out


def marca_texto(largura, altura, cor=MARCA_TEXTO, semente=11):
    """Faixa do marca-texto (usar com Peca(modo='multiplica') e `revela` para a varredura da esquerda para a direita)."""
    rng = np.random.default_rng(semente)
    w, h = int(round(largura)), int(round(altura))
    a = np.full((h, w), 255, np.uint8)
    topo = (1.5 + 1.2 * np.sin(np.linspace(0, 9, w) + rng.uniform(0, 6))).astype(int)      # borda levemente irregular
    base = (1.5 + 1.2 * np.sin(np.linspace(0, 7, w) + rng.uniform(0, 6))).astype(int)
    for xx in range(w):
        a[:max(0, topo[xx]), xx] = 0; a[h - max(0, base[xx]):, xx] = 0
    out = np.empty((h, w, 4), np.uint8); out[..., :3] = bgr(cor); out[..., 3] = a
    return out


def provisoria(largura, altura, rotulo, tom=120):
    """Imagem provisória (cinza com rótulo) para construir e auditar o movimento antes de a imagem real chegar.
    NUNCA entra no vídeo final: monta.py recusa a entrega se alguma ainda estiver em uso."""
    w, h = int(largura), int(altura)
    im = np.full((h, w, 3), tom, np.uint8)
    cv2.rectangle(im, (0, 0), (w - 1, h - 1), (tom - 40,) * 3, 6)
    cv2.line(im, (0, 0), (w - 1, h - 1), (tom - 25,) * 3, 2); cv2.line(im, (w - 1, 0), (0, h - 1), (tom - 25,) * 3, 2)
    f, _ = fonte(max(18, min(w, h) // 9))
    pil = Image.fromarray(im); d = ImageDraw.Draw(pil)
    linhas = rotulo.split('\n'); y = h / 2 - len(linhas) * f.size * 0.6
    for l in linhas:
        d.text(((w - f.getlength(l)) / 2, y), l, font=f, fill=(255, 255, 255)); y += f.size * 1.2
    return np.array(pil)


def vinheta(forca=0.5, inicio=0.55, W=1080, H=1920):
    """Fator multiplicativo (H, W, 1) preso à tela: 1 no centro, 1 − força nos cantos; vale por cima das peças."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / np.sqrt(2)
    u = np.clip((r - inicio) / (1 - inicio), 0, 1); u = u * u * (3 - 2 * u)
    return (1 - forca * u)[..., None]


def mesa(W=1080, H=1920, centro='#22211d', topo='#171612', base='#10110c', cx=540, cy=768, rx=810, ry=864, semente=2):
    """Mesa: gradiente vertical topo → base + luz central elíptica difusa (smoothstep) + ruído de ±1 nível.
    Com um perfil do reestudo ativo, usa a mesa DELE (medida na referência): luz com raio diferente para cima e para baixo."""
    P = perfis.ativo()
    if not P.get('antigo'): return mesa_do_perfil(P, W, H, semente)
    centro, topo, base = do_guia(centro), do_guia(topo), do_guia(base)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    g = (yy / (H - 1))[..., None]
    fundo = np.array(bgr(topo), np.float32)[None, None] * (1 - g) + np.array(bgr(base), np.float32)[None, None] * g
    d = np.sqrt(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2)
    u = np.clip(1 - d, 0, 1); u = (u * u * (3 - 2 * u))[..., None]
    out = fundo * (1 - u) + np.array(bgr(centro), np.float32)[None, None] * u
    out += np.random.default_rng(semente).uniform(-1, 1, (H, W, 1)).astype(np.float32)
    return np.clip(out, 0, 255)


def mesa_do_perfil(P=None, W=1080, H=1920, semente=2):
    """Mesa do perfil: gradiente vertical topo → base + luz elíptica (raio para cima ≠ raio para baixo), lisa (ruído de ±0,5).
    Fica PARADA na tela: é o fundo fixo da Cena; só as peças andam."""
    M = (P or perfis.ativo())['mesa']
    centro, topo, base = (np.array(bgr(do_guia(M[k])), np.float32)[None, None] for k in ('centro', 'topo', 'base'))
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    g = (yy / (H - 1))[..., None]
    fundo = topo * (1 - g) + base * g
    ry = np.where(yy < M['cy'], M['ry_cima'], M['ry_baixo'])
    d = np.sqrt(((xx - M['cx']) / M['rx']) ** 2 + ((yy - M['cy']) / ry) ** 2)
    u = np.clip(1 - d, 0, 1); u = (u * u * (3 - 2 * u))[..., None]
    out = fundo * (1 - u) + centro * u
    out += np.random.default_rng(semente).uniform(-0.5, 0.5, (H, W, 1)).astype(np.float32)
    return np.clip(out, 0, 255)
