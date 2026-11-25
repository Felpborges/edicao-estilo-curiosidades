#!/usr/bin/env python3
"""ve_ataques.py · desenha o espectrograma do clipe limpo com o início de cada palavra (branco = whisper,
amarelo = ataque adotado), para conferência visual. Uso: python3 ve_ataques.py <02-corte> <pasta_saida> [seg_por_linha=4]"""
import sys, os, json, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont
P, OUT = sys.argv[1], sys.argv[2]; SEG = float(sys.argv[3]) if len(sys.argv) > 3 else 4.0
os.makedirs(OUT, exist_ok=True)
w = wave.open(os.path.join(P, 'audio-corte.wav')); sr = w.getframerate(); ch = w.getnchannels()
x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, ch).mean(axis=1) / 32768.0
hop, win = int(sr * 0.005), int(sr * 0.020); n = (len(x) - win) // hop
jan = np.hanning(win); nb = int(6000 / (sr / win)) + 1
S = np.empty((nb, n), np.float32)
for i in range(n):
    S[:, i] = 20 * np.log10(np.abs(np.fft.rfft(x[i * hop:i * hop + win] * jan))[:nb] + 1e-6)
S = np.clip((S - (S.max() - 70)) / 70, 0, 1)
arq = 'palavras-ataque.json' if os.path.exists(os.path.join(P, 'palavras-ataque.json')) else 'palavras-corte.json'
ws = json.load(open(os.path.join(P, arq), encoding='utf-8'))['palavras']
try: fonte = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 15)
except Exception: fonte = ImageFont.load_default()
ESC, H = 2, 150                       # 1 passo de 5 ms = 2 px; altura do espectro por linha
cols = int(SEG * 200); linhas = int(np.ceil(n / cols)); por_img = 3
for g in range(0, linhas, por_img):
    im = Image.new('RGB', (cols * ESC + 20, por_img * (H + 62)), (18, 18, 18)); d = ImageDraw.Draw(im)
    for r in range(por_img):
        L = g + r
        if L >= linhas: break
        a = L * cols; b = min(n, a + cols); y0 = r * (H + 62) + 40
        bloco = (S[::-1, a:b] * 255).astype(np.uint8)
        sp = Image.fromarray(bloco).resize(((b - a) * ESC, H), Image.BILINEAR)
        im.paste(Image.merge('RGB', (sp, sp, sp.point(lambda v: v // 2))), (10, y0))
        for s in range(int(a * 5 / 100), int(b * 5 / 100) + 1):        # régua de 100 ms
            xx = 10 + (s * 100 / 5 - a) * ESC
            if 10 <= xx <= 10 + (b - a) * ESC:
                d.line([(xx, y0 + H), (xx, y0 + H + (8 if s % 10 == 0 else 4))], fill=(150, 150, 150))
                if s % 5 == 0: d.text((xx + 2, y0 + H + 6), f'{s/10:.1f}', fill=(170, 170, 170), font=fonte)
        for k, wd in enumerate(ws):
            for campo, cor, topo in (('ini_ms', (255, 255, 255), 0), ('ataque_ms', (255, 220, 0), 1)):
                if campo not in wd: continue
                i = (wd[campo] - 10) / 5
                if a <= i < b:
                    xx = 10 + (i - a) * ESC
                    d.line([(xx, y0 - (4 if topo else 0)), (xx, y0 + H)], fill=cor, width=1 if campo == 'ini_ms' else 2)
                    if topo: d.text((xx + 2, y0 - 36 + (k % 2) * 16), f"{k}:{wd['palavra']}", fill=cor, font=fonte)
    nome = os.path.join(OUT, f'ataques-{g//por_img+1:02d}.png'); im.save(nome); print(nome, im.size)
