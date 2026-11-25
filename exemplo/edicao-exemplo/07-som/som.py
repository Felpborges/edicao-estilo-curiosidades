#!/usr/bin/env python3
"""som.py · som deste reel (Estilo 03), pelo molde de `Estilo 03 - Curiosidades/treino/SOM.md` (seções 5 e 6).

Só o que a referência tem:
  · voz mono no centro, −14 LUFS, compressão forte (LRA ≈ 3 LU), pico real ≤ −1 dBTP; sem música;
  · foley de papel e caneta só onde a cena anota à mão (regra 11, V02): a elipse do trecho 5 e as 2 passadas de
    marca-texto do trecho 7; o som do marcador começa 60 a 300 ms antes do traço; RMS ≈ 30 dB abaixo da voz;
  · 1 subida grave que para no corte da virada (regra 12, V05-R2): "Mas a novidade não para só nos slides." → corte.
Nada em corte seco, pop de cartão, adesivo, etiqueta, legenda, zoom ou véu (regras 3, 4 e 5: nunca levam efeito).

Os sons são GERADOS (Higgsfield, modelo mirelo_text_to_audio; arquivos em `gerados/`) e depois moldados aqui em duração,
faixa de frequência e volume pelas medidas da referência. Uso: python3 som.py   (leve; não mexe no motor)
"""
import os, sys, json, wave, subprocess
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__)); ED = os.path.dirname(AQUI)
SR = 48000; Q = 1000.0 * 1001 / 24000
VOZ_REF = -16.5                                   # RMS médio da fala na referência (dBFS) = base dos níveis relativos

# quadros dos eventos (dos planos; ver 06-render/CHECKLIST-corte-01.md)
Q_ELIPSE, Q_MARCA1, Q_MARCA2, Q_CORTE_VIRADA = 223, 358, 382, 619


def le(nome):
    w = wave.open(os.path.join(AQUI, 'gerados', nome)); assert w.getframerate() == SR
    return np.frombuffer(w.readframes(w.getnframes()), np.int16).reshape(-1, w.getnchannels()).astype(np.float64).mean(1) / 32768


def grava(nome, y):
    w = wave.open(os.path.join(AQUI, nome), 'w'); w.setnchannels(y.shape[1]); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()


def faixa(x, f0, f1):
    """Passa-faixa por FFT, bordas suaves de meia oitava."""
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.clip((np.log2(np.maximum(f, 1) / f0) + 0.5), 0, 1) * np.clip((np.log2(f1 / np.maximum(f, 1)) + 0.5), 0, 1)
    return np.fft.irfft(X * g, len(x))


def rms_db(x): return 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-12)
def pico_10ms(x):
    n = len(x) // 480; return 20 * np.log10(np.sqrt((x[:n * 480].reshape(n, 480) ** 2).mean(1)).max() + 1e-12)


def traco(textura, ini_s, dur_ms, f0, f1, rms_rel, forma, desloc_r=0.41):
    """Um risco de caneta ou marcador: textura de atrito gerada, recortada, filtrada e com envelope.
    L e R saem de trechos diferentes da mesma textura (som estéreo aberto, como os efeitos do V02)."""
    n = int(SR * dur_ms / 1000); t = np.linspace(0, 1, n)
    env = forma(t)
    out = []
    for off in (ini_s, ini_s + desloc_r):
        a = int(off * SR); s = faixa(textura[a:a + n + 4096], f0, f1)[2048:2048 + n]
        out.append(s * env)
    y = np.stack(out, 1)
    return y * 10 ** ((VOZ_REF + rms_rel - rms_db(y.mean(1))) / 20)


def bordas(t, ataque, queda):          # ataque e queda em fração da duração
    return np.clip(t / ataque, 0, 1) ** 1.5 * np.clip((1 - t) / queda, 0, 1) ** 1.5


def main():
    voz_in = os.path.join(ED, '02-corte', 'audio-corte.wav'); voz = os.path.join(AQUI, 'voz-master.wav')
    # 1 · voz: compressão 2:1 + limitador + ganho, ajustados até −14 LUFS / LRA ≈ 2,7 / pico −1,1 dBTP (medido)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', voz_in, '-af',
                    'acompressor=threshold=-24dB:ratio=2:attack=10:release=250:makeup=1,volume=14.3dB,'
                    'alimiter=limit=0.87:attack=3:release=60:level=false', '-ar', str(SR), '-ac', '2', voz], check=True)
    w = wave.open(voz); v = np.frombuffer(w.readframes(w.getnframes()), np.int16).reshape(-1, 2).astype(np.float64) / 32768
    N = len(v); fx = np.zeros((N, 2))
    def poe(y, t_ms):
        a = int(round(t_ms / 1000 * SR)); b = min(N, a + len(y)); fx[a:b] += y[:b - a]
    tex = le('marcador-4.wav')                   # atrito agudo e contínuo (79 % da energia em 2–12 kHz)
    tex = np.tile(tex / (np.abs(tex).max() + 1e-9), 3)
    rel = {}

    # 2 · elipse à mão (trecho 5): caneta riscando. Ref V02-E7: 600 ms, 2–12 kHz, começa 92 ms antes do traço,
    #     RMS −24 dB e pico −8 dB em relação à voz. Aqui mais baixo (−27 dB), por ser 1 traço só e a pedido ("sem exagero").
    forma_elipse = lambda t: bordas(t, 0.06, 0.18) * (0.62 + 0.38 * np.sin(np.pi * (t * 2.0 + 0.15)) ** 2)   # 2 voltas de velocidade
    y = traco(tex, 0.20, 600, 2000, 12000, -27.0, forma_elipse); poe(y, Q_ELIPSE * Q - 92); rel['elipse'] = y

    # 3 · marca-texto, 2 passadas (trecho 7). Ref V02-E3/E4/E8/E11: 150 a 590 ms, médio-agudo (2–6 kHz), começa 60 a 310 ms
    #     antes do traço, RMS −26 a −36 dB abaixo da voz. Passada 1: 12 q de varredura; passada 2: 6 q.
    forma_marca = lambda t: bordas(t, 0.10, 0.22) * (0.8 + 0.2 * np.sin(np.pi * t))
    y = traco(tex, 1.10, 600, 1500, 7000, -30.0, forma_marca); poe(y, Q_MARCA1 * Q - 150); rel['marca-texto 1'] = y
    y = traco(tex, 2.30, 360, 1500, 7000, -31.0, forma_marca); poe(y, Q_MARCA2 * Q - 110); rel['marca-texto 2'] = y

    # 4 · subida grave da virada. Ref V05-R2: < 500 Hz (pico 107 Hz), sobe 1,0 a 1,5 s, pico 40 a 50 ms antes do corte,
    #     para seco no corte (+20 ms); RMS −20 a −24 dB e pico −7 a −11 dB em relação à voz. Aqui: 1,15 s, RMS ≈ −21 dB e pico −11 dB.
    r = le('subida-1.wav')                      # ronco gerado, contínuo, a 41 Hz
    r = np.concatenate([r[2400:-2400], r[2400:-2400][::-1]])   # ida e volta, para ter duração de sobra sem emenda brusca
    k = 2.6                                     # tocado 2,6× mais rápido: o pico vai de 41 para ≈ 107 Hz (o da referência)
    dur = 1.15 + 0.065; n = int(SR * dur)
    def trecho(off):
        idx = (off * SR + np.arange(n) * k); i0 = idx.astype(int); fr = idx - i0
        return faixa(r[i0] * (1 - fr) + r[i0 + 1] * fr, 60, 500)
    t = np.arange(n) / SR; t_pico = 1.15
    env = 10 ** ((-48 * np.clip(1 - t / t_pico, 0, 1)) / 20)                           # −48 dB → 0 dB, reta em dB (RMS ≈ 10 dB abaixo do pico, como no V05)       # −30 dB → 0 dB, acelerando no fim
    env *= np.clip((dur - t) / 0.015, 0, 1)                                              # para seco: 15 ms de saída
    env *= np.clip(t / 0.05, 0, 1)
    y = np.stack([trecho(0.02) * env, trecho(0.07) * env], 1)
    y *= 10 ** ((VOZ_REF - 11.0 - pico_10ms(y.mean(1))) / 20)
    poe(y, Q_CORTE_VIRADA * Q - 45 - t_pico * 1000); rel['subida da virada'] = y

    grava('efeitos.wav', fx)
    mix = v + fx
    pico = np.abs(mix).max()
    if pico > 0.89: mix *= 0.89 / pico
    grava('mix.wav', mix)
    fala_rms = rms_db(v.mean(1)[np.abs(v.mean(1)) > 10 ** (-40 / 20)])
    print(f'voz masterizada: RMS da fala {fala_rms:.1f} dBFS (referência {VOZ_REF})')
    for nome, y in rel.items():
        m = y.mean(1); lat = (y[:, 0] - y[:, 1]) / 2
        print(f'  {nome:18} {len(y)/SR*1000:5.0f} ms · RMS {rms_db(m):6.1f} dBFS ({rms_db(m)-VOZ_REF:+.0f} dB da voz) · pico {pico_10ms(m):6.1f} dBFS ({pico_10ms(m)-VOZ_REF:+.0f}) · lateral RMS {rms_db(lat):6.1f}')
    print('pico da mixagem (amostra):', round(20 * np.log10(np.abs(mix).max()), 2), 'dBFS')


main()
