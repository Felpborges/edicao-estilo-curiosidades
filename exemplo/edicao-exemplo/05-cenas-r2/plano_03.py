#!/usr/bin/env python3
"""plano_03 · "que podem fazer você economizar centenas de dólares por ano." · colagem de 3 cédulas que caem
na palavra (P16). Spec: `04-specs/trecho-03.md`. Ref: V01-A43. Saída por corte seco (ajuste adotado).
2ª rodada (corte 04): sombra do perfil V03 ('recorte', direto sobre a cédula: recorte justo, sem contorno de adesivo),
grão vivo do perfil sobre as cédulas, câmera por fases medida na V01-A43 (aproxima +2,6 → +2,0 %/s enquanto o monte
se forma, sem pico; o pico em "centenas" do painel não vale). Auditoria: `auditoria-r2-plano_03.md`."""
import e3, pecas, base
import comum_discos as cd

Q = e3.QUADRO_MS

NOTA = (735, 312)                                         # tamanho de cada cédula sem giro (2,36:1)
# (centro x, centro y, giro °) · trecho-03 §2 (nota 1 medida; 2 e 3 = nota 1 + deslocamento observado)
NOTAS = [(492, 664, -6.0), (492 + 53, 664 + 110, 4.0), (492 - 5, 664 + 203, -3.0)]
CENTRO_MONTE = (520, 754)                                 # centro do monte final x 108–932 × y 465–1042


def plano(ctx):
    f0, f1 = base.CORTES['plano_03']
    t = ctx.t

    q_n1 = max(f0, ctx.q_palavra(11, -50))     # nota 1 já no quadro do corte ("que", i11)
    q_n2 = ctx.q_palavra(16, 1)                # "centenas" (i16), +1 ms
    q_n3 = ctx.q_palavra(16, 252)              # +252 ms de "centenas" = 6 q depois da nota 2

    # câmera por fases, sem pan, âncora no centro do monte (G12.3). Ref V01-A43 (reestudo 20/11, medido): o monte
    # aproxima +2,6 %/s logo depois de completo (f3510–f3522) e freia a +2,0 %/s (f3520–f3530) até sair; sem pico.
    # Antes de "centenas" a nota 1 fica sozinha 1,3 s, momento que a Ref não tem (lá são 167 ms): vale o repouso do
    # painel, +3 %/s. O pico de +30 %/s em "centenas" do painel contradiz a Ref medida: não entra. Corta andando.
    t_c = t(q_n3 + 4)                                       # monte completo (nota 3 assentada, 4 q como na Ref)
    zoom = base.zoom_fases(t(f0), [(t(f0), 3.0), (t(q_n2), 3.0), (t(q_n2) + 2 * Q, 2.6),
                                   (t_c + 6 * Q, 2.6), (t_c + 15 * Q, 2.0)])
    cx, cy = base.ancora(zoom, *CENTRO_MONTE)
    c = base.cena(e3.Camera(zoom=zoom, cx=cx, cy=cy), semente=3)

    # cédula: recorte justo (sem contorno de adesivo) + sombra caída do perfil, tipo 'recorte'
    nota = pecas.com_sombra(ctx.rgba('nota-100', NOTA[0], NOTA[1], 'nota-100\ncédula US$ 100\n2,35:1'), 'recorte')
    entradas = [
        (q_n1, [1.05, 1.0], [0, 0]),                    # 105 % → 100 % em 1 imagem (2 q)
        (q_n2, [1.03, 1.005, 1.0], [-15, -2.5, 0]),     # 103 → 100,5 → 100 %, "cai" ≈ 15 px enquanto encolhe
        (q_n3, [1.03, 1.005, 1.0], [-15, -2.5, 0]),
    ]
    for k, ((x, y, g), (q0, esc, dy)) in enumerate(zip(NOTAS, entradas)):
        mx, my = base.mundo(x, y)
        t0 = t(q0)
        cai = cd.pop(t0, dy)
        c.poe(e3.Peca(nota, x=mx, y=lambda tt, my=my, cai=cai: my + cai(tt), escala=cd.pop(t0, esc), giro=g,
                      z=10 + k, de=t0, nome=f'nota {k + 1}'))

    return {'nome': 'plano_03 · 3 cédulas empilham em "centenas"', 'f0': f0, 'f1': f1, 'cena': c,
            'gatilhos': {'nota1': q_n1, 'nota2': q_n2, 'nota3': q_n3}}
