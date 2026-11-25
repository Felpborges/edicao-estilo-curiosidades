#!/usr/bin/env python3
"""comum_discos.py · os 3 grupos disco + recorte do gancho (trecho 2) que voltam idênticos no callback (trecho 15).

Disposição = `04-specs/trecho-02.md` §2, tabela "Disposição final (q46)": px de tela 1080x1920, com a câmera em
repouso (deslocamento 0, escala de grupo 1). O trecho 15 usa a mesma tabela ×1,00 (`trecho-15.md` §2).
Ordem das camadas (trecho-02 §2): disco 1 → disco 2 → disco 3 → recorte 1 → recorte 2 → recorte 3 (todos os discos
atrás de todos os recortes; o disco mais novo por cima do mais velho).
Não começa com `plano_`: o monta.py não o carrega como plano; os planos importam."""
import numpy as np
import cv2
import e3, pecas, base

# disco creme: trecho-02 §2 "#cac3b1 na luz" (A28 f1910, medido) → convertido pelo caminho do treino
COR_DISCO = pecas.do_guia('#cac3b1')

# 20/11 (principal): com os prints reais (retangulares) os recortes do 1º tamanho cobriam quase todo o disco; na Ref
# V01-A28 o disco aparece em volta da figura. Recortes reduzidos para ≈ 45–87 % do diâmetro do seu disco; discos iguais.
GRUPOS = [
    # disco: (centro x, centro y, diâmetro) · recorte: (imagem, centro x, centro y, largura, altura da figura sem contorno, rótulo)
    dict(disco=(381, 644, 674), recorte=('print-docs', 388, 668, 300, 690, 'print-docs\nClaude Docs\n1:2,3')),
    dict(disco=(759, 593, 492), recorte=('print-design', 766, 572, 290, 362, 'print-design\nClaude Design\n4:5')),
    dict(disco=(557, 1035, 460), recorte=('print-slides', 560, 1030, 400, 225, 'print-slides\nClaude Slides\n16:9')),
]
Z_DISCO = (10, 11, 12)
Z_RECORTE = (20, 21, 22)


def imagens(ctx):
    """[(rgba_disco, rgba_recorte)] dos 3 grupos no tamanho da disposição. Disco com grão e sombra curta na borda
    (0, 3 px; 6 px; 35 %); recorte com contorno de adesivo 15 px (pecas.recorte) + sombra fina (sombra_fina, molde do global)."""
    out = []
    for k, g in enumerate(GRUPOS):
        d = g['disco'][2]
        nome, _, _, w, h, rot = g['recorte']
        # 2ª rodada: disco e recorte com o acabamento do perfil (cor, pontilhado fixo, contorno ondulado, sombra caída)
        out.append((pecas.disco_do_perfil(d, semente=7 + k),
                    pecas.recorte_do_perfil(ctx.rgba(nome, w, h, rot), altura=h, semente=9 + k)))
    return out


def sombra_fina(rgba, dy=2, desfoque=3, opacidade=0.45):
    """Sombra fina do recorte-adesivo (0, 2 px; 3 px; 45 %, 00-globais §3). Feita aqui porque
    `pecas.recorte(..., sombra=True)` quebra no motor atual (_sombra com margem 0 e dy=2 estoura o array).
    A margem transparente que o recorte já traz (contorno + 12 px) comporta a sombra."""
    a = rgba[:, :, 3].astype(np.float32) / 255.0
    s = np.zeros_like(a); s[dy:, :] = a[:-dy, :]
    s = cv2.GaussianBlur(s, (0, 0), desfoque) * opacidade
    return pecas._junta(rgba[:, :, :3].astype(np.float32), a, s, 0)


def centro_disco(k):
    """Centro do disco k no mundo."""
    x, y, _ = GRUPOS[k]['disco']
    return base.mundo(x, y)


def no_grupo(k, x_tela, y_tela, escala_grupo):
    """Funções (x(t), y(t)) de um ponto preso ao grupo k, que cresce em torno do centro do disco k."""
    dx, dy = centro_disco(k)
    px, py = base.mundo(x_tela, y_tela)
    return (lambda t: dx + (px - dx) * escala_grupo(t)), (lambda t: dy + (py - dy) * escala_grupo(t))


def poe(c, ctx, de, pops_disco, pops_recorte, escalas_grupo=None):
    """Põe os 3 grupos na cena `c`.
    de = [(t_disco, t_recorte)] por grupo (ms) · pops_* = [função t → fator] por grupo (estalo, em torno do centro
    da própria peça) · escalas_grupo = [função t → fator] por grupo (crescimento do grupo em torno do centro do
    disco) ou None (= 1). Devolve as peças, na ordem disco1, recorte1, disco2, …"""
    ims = imagens(ctx); pecas_ = []
    for k, g in enumerate(GRUPOS):
        S = escalas_grupo[k] if escalas_grupo else e3.const(1.0)
        dx, dy = centro_disco(k)
        rx, ry = no_grupo(k, g['recorte'][1], g['recorte'][2], S)
        pd, pr = pops_disco[k], pops_recorte[k]
        dsc, rec = ims[k]
        pecas_.append(c.poe(e3.Peca(dsc, x=dx, y=dy, escala=(lambda t, S=S, pd=pd: S(t) * pd(t)), z=Z_DISCO[k],
                                    de=de[k][0], nome=f'disco {k + 1}')))
        pecas_.append(c.poe(e3.Peca(rec, x=rx, y=ry, escala=(lambda t, S=S, pr=pr: S(t) * pr(t)), z=Z_RECORTE[k],
                                    de=de[k][1], nome=f'recorte {k + 1} · {g["recorte"][0]}')))
    return pecas_


def pop(t0, valores):
    """Estalo/pop em degraus de 2 q (cada valor dura 2 quadros, sem interpolar), começando em t0."""
    return e3.Trilha(e3.tabela(t0, valores, passo_q=2), degrau=2 * e3.QUADRO_MS, t0=t0)
