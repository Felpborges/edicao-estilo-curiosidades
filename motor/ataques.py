#!/usr/bin/env python3
"""ataques.py · Estilo 03 · reconfere no áudio o início de cada palavra (o whisper adianta inícios de frase).

Uso: python3 ataques.py <02-corte>
Lê audio-corte.wav e palavras-corte.json; grava palavras-ataque.json (campo ataque_ms) e ataques.md.
Método: energia de 300 a 8000 Hz, janela de 20 ms, passo de 5 ms. Todo silêncio (pausa ou oclusão) de 30 ms ou
mais termina num ataque; esse ataque vai para a palavra cujo início do whisper está mais perto (até 160 ms).
Palavra colada na anterior, sem silêncio: fica o tempo do whisper (margem ≈ ±50 ms). Correções feitas olhando o
espectrograma entram em ataques-manuais.json ({"índice": ms}).
"""
import sys, os, json, wave
import numpy as np
P = sys.argv[1]
w = wave.open(os.path.join(P, 'audio-corte.wav')); sr = w.getframerate(); ch = w.getnchannels()
x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, ch).mean(axis=1) / 32768.0
hop, win = int(sr * 0.005), int(sr * 0.020)
n = (len(x) - win) // hop
jan = np.hanning(win); fr = np.fft.rfftfreq(win, 1 / sr); banda = (fr >= 300) & (fr <= 8000)
e = np.empty(n)
for i in range(n):
    s = np.abs(np.fft.rfft(x[i * hop:i * hop + win] * jan)) ** 2
    e[i] = 10 * np.log10(s[banda].sum() + 1e-10)
e = np.convolve(e, np.ones(3) / 3, mode='same')
t = lambda i: i * 5 + 10          # centro da janela, ms
D = json.load(open(os.path.join(P, 'palavras-corte.json'), encoding='utf-8')); ws = D['palavras']
# silêncios: energia da banda abaixo do piso + 14 dB por 30 ms ou mais (pausa ou oclusão de consoante)
piso = np.percentile(e, 4); LIM = piso + 14
sil, i = [], 0
while i < n:
    if e[i] < LIM:
        j = i
        while j + 1 < n and e[j + 1] < LIM: j += 1
        if (j - i + 1) * 5 >= 30: sil.append((int(t(i)), int(t(j + 1))))
        i = j + 1
    else: i += 1
for wd in ws: wd['ataque_ms'], wd['ataque_fonte'], wd['silencio_antes_ms'] = wd['ini_ms'], 'whisper', 0
# cada fim de silêncio vai para a palavra cujo início (whisper) está mais perto, se estiver a até 160 ms
for s0, s1 in sil:
    k = min(range(len(ws)), key=lambda q: abs(ws[q]['ini_ms'] - s1))
    if abs(ws[k]['ini_ms'] - s1) <= 160 and (ws[k]['ataque_fonte'] == 'whisper' or abs(ws[k]['ini_ms'] - s1) < abs(ws[k]['ini_ms'] - ws[k]['ataque_ms'])):
        ws[k]['ataque_ms'], ws[k]['ataque_fonte'], ws[k]['silencio_antes_ms'] = s1, 'áudio (fim do silêncio)', s1 - s0
man = os.path.join(P, 'ataques-manuais.json')
if os.path.exists(man):
    for k, v in json.load(open(man, encoding='utf-8')).items():
        ws[int(k)]['ataque_ms'], ws[int(k)]['ataque_fonte'] = int(v), 'conferido no espectrograma'
for k in range(1, len(ws)):
    if ws[k]['ataque_ms'] <= ws[k - 1]['ataque_ms']:
        ws[k]['ataque_ms'], ws[k]['ataque_fonte'] = ws[k - 1]['ataque_ms'] + 40, 'ajuste de ordem'
json.dump(D, open(os.path.join(P, 'palavras-ataque.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
np.save(os.path.join(P, 'energia-5ms.npy'), e.astype(np.float32))
with open(os.path.join(P, 'ataques.md'), 'w', encoding='utf-8') as f:
    f.write('# Início de cada palavra reconferido no áudio\n\n| i | palavra | whisper (ms) | ataque (ms) | diferença | silêncio antes (ms) | fonte |\n|---|---|---|---|---|---|---|\n')
    for k, wd in enumerate(ws):
        f.write(f"| {k} | {wd['palavra']} | {wd['ini_ms']} | {wd['ataque_ms']} | {wd['ataque_ms']-wd['ini_ms']:+d} | {wd['silencio_antes_ms']} | {wd['ataque_fonte']} |\n")
d = np.array([wd['ataque_ms'] - wd['ini_ms'] for wd in ws if wd['ataque_fonte'] != 'whisper'])
print(len(d), 'de', len(ws), 'palavras com ataque medido no áudio; diferença mediana', int(np.median(d)), 'ms; p10', int(np.percentile(d, 10)), 'p90', int(np.percentile(d, 90)))
