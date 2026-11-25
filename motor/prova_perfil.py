#!/usr/bin/env python3
"""prova_perfil.py · Estilo 03 · prancha de prova de um perfil de acabamento, para conferir contra a referência.

Monta duas cenas de teste com imagens reais de uma edição (nada da referência entra):
  A · cartão com etiqueta sobre a mesa (como a referência usa numa imagem com data ou nome);
  B · disco de papel com recorte-adesivo e um cartão pequeno por cima.
Serve para medir, no arquivo já codificado, o que o reestudo mediu na referência: luz da mesa, borda, sombra nos 4
lados, pontilhado fixo do papel, grão vivo (diferença entre 2 quadros seguidos) e a tarja da legenda.

Uso:
  python3 prova_perfil.py <pasta da edição> --perfil V03 --saida <pasta>            grava A.png e B.png (leve)
  python3 prova_perfil.py <pasta da edição> --perfil V03 --saida <pasta> --video    grava também prova.mp4, 24 quadros por
                                                                                    cena (PESADO: rodar pela trava leve.py)
"""
import os, sys, argparse, subprocess
import numpy as np
import cv2

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import e3, pecas, perfis, legenda as leg
from monta import Ctx, yuv709

Q = e3.QUADRO_MS


def cenas(ctx, P):
    mesa = pecas.mesa_do_perfil(P)
    mundo = lambda x, y: (x - e3.W / 2, y - e3.H / 2)
    # A · cartão a 87 % da largura, centro em (50 %, 39 %), giro +1,2°, etiqueta no topo; câmera em deriva de +4 %/s
    za = e3.ZoomPorTaxa(0, [(0, 4.0)])
    A = e3.Cena(mesa, e3.Camera(zoom=za), perfil=P, semente=1)
    img = ctx.img('print-pedido', 900, 1300)
    car = pecas.cartao_do_perfil(img, 940)
    x, y = mundo(540, 750)
    A.poe(e3.Peca(car, x=x, y=y, giro=1.2, z=10, nome='cartão'))
    et = pecas.com_sombra(pecas.etiqueta('2026, Claude', cor=pecas.do_guia(P['etiqueta']['cor'])), 'etiqueta')
    ex, ey = mundo(540, 750 - car.shape[0] / 2 + 30)
    A.poe(e3.Peca(et, x=ex, y=ey, giro=-1.5, z=20, nome='etiqueta'))
    # B · disco de 86 % da largura com recorte por cima e um cartão pequeno ao lado
    B = e3.Cena(mesa, e3.Camera(zoom=e3.ZoomPorTaxa(0, [(0, 3.0)])), perfil=P, semente=2)
    dx, dy = mundo(500, 640)
    B.poe(e3.Peca(pecas.disco_do_perfil(900), x=dx, y=dy, z=10, nome='disco'))
    rec = pecas.recorte_do_perfil(ctx.rgba('logo-powerpoint', 500, 460), altura=440)
    B.poe(e3.Peca(rec, x=dx - 40, y=dy + 60, giro=-4, z=20, nome='recorte'))
    c2 = pecas.cartao_do_perfil(ctx.img('print-interface', 400, 400), 380)
    cx, cy = mundo(800, 1180)
    B.poe(e3.Peca(c2, x=cx, y=cy, giro=-2.0, z=30, nome='cartão pequeno'))
    return [('A', A), ('B', B)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('edicao'); ap.add_argument('--perfil', default=perfis.PADRAO); ap.add_argument('--saida', required=True)
    ap.add_argument('--video', action='store_true'); ap.add_argument('--quadros', type=int, default=24)
    a = ap.parse_args()
    P = perfis.usa(a.perfil)
    ctx = Ctx(os.path.abspath(a.edicao))
    os.makedirs(a.saida, exist_ok=True)
    L = leg.Legenda([{'i0': 0, 'i1': 1, 'texto': 'peça de prova', 'de_ms': 0, 'ate_ms': 1e9}], Q)
    cs = cenas(ctx, P)
    for nome, c in cs:
        f = L.poe(c.quadro(6 * Q), 6)
        cv2.imwrite(os.path.join(a.saida, f'{nome}.png'), f)
    print('perfil', a.perfil, '· fonte da legenda', L.nome_fonte, '· gravado em', a.saida)
    if a.video:
        dest = os.path.join(a.saida, 'prova.mp4')
        marca = ['-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
        cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-s', f'{e3.W}x{e3.H}', '-r', f'{e3.FPS_N}/{e3.FPS_D}', *marca,
               '-i', '-', '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', *marca, '-movflags', '+faststart', dest]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for nome, c in cs:
            for n in range(a.quadros):
                p.stdin.write(yuv709(L.poe(c.quadro(n * Q), n)))
        p.stdin.close(); p.wait(); print('vídeo:', p.returncode, dest)


if __name__ == '__main__':
    main()
