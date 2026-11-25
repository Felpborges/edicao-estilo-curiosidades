#!/usr/bin/env python3
"""base.py · o que é comum a todos os planos de cena DESTA edição (copie esta pasta para <edição>/05-cenas/).

Modelo extraído da edição de exemplo. O que é seu: o dicionário CORTES (quadros em que cada plano começa e acaba)
e o nome dos planos. O resto (mesa, acabamento do perfil, estalo, pop do disco, zoom por fases, âncora) vale para
qualquer vídeo e NÃO deve ser mudado: é a forma do estilo.

Perfil de acabamento: vem de `<edição>/03-plano/perfil.json` ({"perfil": "V03"}); sem o arquivo vale o padrão (V03).
Tempos: tudo em ms; 1 quadro = e3.QUADRO_MS (41,708 ms a 23,976 fps). Posições em px de tela 1080x1920.
"""
import e3, pecas, perfis

Q = e3.QUADRO_MS
PERFIL = perfis.ativo()
MESA = pecas.mesa_do_perfil(PERFIL)          # luz central do perfil; fundo fixo da Cena
VINHETA = None                              # perfil V03: nenhuma vinheta por cima das peças

# quadro em que cada plano começa e acaba [f0, f1); o que fica entre eles é rosto (A-roll).
# Preencha DEPOIS de o usuário escolher no painel: cada corte seco cai ≈ 42 ms (1 quadro) ANTES da 1ª palavra da frase,
# calculado com ctx.ataque(i) (início da palavra reconferido no áudio). Exemplo de formato:
#   'plano_02': (25, 73),   # "três ferramentas de IA totalmente gratuitas"
CORTES = {
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
