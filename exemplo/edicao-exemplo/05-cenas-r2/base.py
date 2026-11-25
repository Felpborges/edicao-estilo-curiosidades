#!/usr/bin/env python3
"""base.py (2ª rodada, corte 04) · o que é comum a todos os planos desta edição, no perfil de acabamento do plano
(`03-plano/perfil.json`, V03): mesa do perfil PARADA na tela, sem vinheta por cima, grão vivo e sombra do perfil,
câmera descrita em %/s por fase (`zoom_fases`). Os cortes e os gatilhos são os mesmos do corte 03.
Original da 1ª rodada: `../05-cenas/base.py`.
Valores de `04-specs/00-globais.md`. Os cortes saem dos ataques reconferidos no áudio (`02-corte/palavras-ataque.json`):
corte seco 42 ms (1 q) antes da 1ª palavra da frase."""
import e3, pecas, perfis

Q = e3.QUADRO_MS
PERFIL = perfis.ativo()
MESA = pecas.mesa_do_perfil(PERFIL)          # luz central do perfil; fundo fixo da Cena
VINHETA = None                              # perfil V03: nenhuma vinheta por cima das peças

# quadro em que cada plano começa e acaba [f0, f1); o que fica entre eles é rosto
CORTES = {
    'plano_02': (25, 73),        # "três ferramentas de IA totalmente gratuitas"         (entra 42 ms antes de "três", i5)
    'plano_03': (73, 145),       # "que podem fazer você economizar centenas de dólares por ano."  ("que", i11)
    'plano_04_05': (145, 262),   # "Elas se chamam Slides, Docs e Design / e ficam dentro do chat que você já utiliza."
    'plano_07_08': (290, 412),   # "é só você pedir … pro seu negócio. / A partir daí então,"
    'plano_09_10': (412, 579),   # "ele vai preparar todos os slides … / você pode exportar … Google Slides."
    'plano_12_13': (619, 789),   # "Na mesma conversa … um roteiro / que depois … nesse material."
    'plano_14': (789, 845),      # "Então, ao invés de você pagar pelo Gamma ou pelo Canva,"
    'plano_15': (845, 888),      # "você tem tudo em uma única conversa."
}


def cena(camera=None, borrao=(), semente=0, luz=None):
    """Cena com a mesa e o acabamento do perfil (iguais em todos os planos). `semente` muda o sorteio do grão vivo
    (dê uma por plano). `luz` só vale em perfil com luz de cena (V04): quanto sobra na borda, de 0 a 1."""
    return e3.Cena(MESA, camera, borrao, VINHETA, perfil=PERFIL, luz=luz, semente=semente)


def zoom_fases(t0, chaves, z0=1.0):
    """Zoom de câmera por FASES: chaves = [(t_ms, taxa em %/s), ...] (ver e3.ZoomPorTaxa, e3.fases_pico, e3.pausa).
    É assim que a referência anda: repouso, pico logo depois da palavra-chave com freio longo, recuo, pausa no gesto."""
    return e3.ZoomPorTaxa(t0, chaves, z0)


def mundo(x_tela, y_tela):
    """Posição no mundo (origem no centro do quadro, câmera em zoom 1) de um ponto dado em px de tela 1080x1920."""
    return x_tela - e3.W / 2, y_tela - e3.H / 2


def estalo(t0, escala=1.0, giro=0.0, fatores=(1.12, 1.04), giros=(3.5, 1.0)):
    """Entrada em estalo, degraus de 2 q (167 ms): q1–q2 ×fatores[0] e giro a mais, q3–q4 ×fatores[1], q5 assentado.
    O giro a mais vai no sentido do giro do cartão. Devolve (trilha_escala, trilha_giro)."""
    s = 1 if giro >= 0 else -1
    esc = e3.Trilha([(t0, escala * fatores[0]), (t0 + 2 * Q, escala * fatores[1]), (t0 + 4 * Q, escala)], degrau=2 * Q, t0=t0)
    gir = e3.Trilha([(t0, giro + s * giros[0]), (t0 + 2 * Q, giro + s * giros[1]), (t0 + 4 * Q, giro)], degrau=2 * Q, t0=t0)
    return esc, gir


def pop_disco(t0, escala=1.0, valores=(0.49, 0.81, 1.0)):
    """Disco que nasce: um valor por quadro (125 ms, 3 q)."""
    return e3.Trilha(e3.tabela(t0, [escala * v for v in valores]), degrau=Q, t0=t0)


def zoom_linear(t0, taxa_por_s, z0=1.0):
    """Zoom de câmera linear: z0 em t0, variando taxa_por_s (ex.: 0.07 = +7 %/s) do valor inicial por segundo."""
    return lambda t: z0 * (1 + taxa_por_s * (t - t0) / 1000.0)


def ancora(zoom, x_tela, y_tela):
    """Centro de câmera (cx, cy) que mantém parado na tela o ponto (x_tela, y_tela) enquanto o zoom muda."""
    px, py = mundo(x_tela, y_tela)
    return (lambda t: px * (1 - 1 / zoom(t))), (lambda t: py * (1 - 1 / zoom(t)))
