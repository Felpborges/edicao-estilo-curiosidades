#!/usr/bin/env python3
"""transcreve.py · Estilo 03 · áudio 16 kHz, envelope de 10 ms e palavras com tempo (whisper.cpp + DTW).

Uso: python3 transcreve.py <video> <pasta_saida> [idioma=pt]
Grava em <pasta_saida>: audio-16k.wav, audio-48k.wav, whisper.json, envelope.csv, palavras.json, palavras.md
Todo comando pesado passa pela trava ferramentas/leve.py (um por vez, com teto de memória).
"""
import os, sys, json, re, subprocess, wave, csv
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
LEVE = os.path.join(AQUI, '..', 'ferramentas', 'leve.py')   # trava: um comando pesado por vez, com teto de memória
# modelo do whisper.cpp: variável WHISPER_MODEL, ou o primeiro que existir nos lugares comuns
_CAND = [os.environ.get('WHISPER_MODEL', ''), os.path.expanduser('~/.cache/whisper-cpp/ggml-large-v3-turbo.bin'),
         os.path.expanduser('~/whisper.cpp/models/ggml-large-v3-turbo.bin'), os.path.expanduser('~/whisper.cpp/models/ggml-large-v3.bin')]
MODELO = next((c for c in _CAND if c and os.path.exists(c)), _CAND[1])
# o preset de DTW (tempo por palavra) tem de casar com o modelo: ggml-large-v3-turbo -> large.v3.turbo, etc.
def _dtw(nome):
    n = os.path.basename(nome).lower()
    for chave, preset in [('large-v3-turbo', 'large.v3.turbo'), ('large-v3', 'large.v3'), ('large-v2', 'large.v2'), ('large-v1', 'large.v1'),
                          ('medium', 'medium'), ('small', 'small'), ('base', 'base'), ('tiny', 'tiny')]:
        if chave in n: return preset
    return 'large.v3.turbo'
DTW = _dtw(MODELO)


def leve(rotulo, cmd, teto='4', minimo='2.5'):
    r = subprocess.run([sys.executable, LEVE, '--min-livre-gb', minimo, '--teto-gb', teto, '--rotulo', rotulo, '--'] + cmd,
                       stdout=subprocess.DEVNULL)
    if r.returncode != 0:
        sys.exit(f'falhou ({r.returncode}): {rotulo}')


def envelope(wav):
    w = wave.open(wav); sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    passo = sr // 100
    n = len(x) // passo
    rms = np.sqrt((x[:n * passo].reshape(n, passo) ** 2).mean(axis=1) + 1e-12)
    return 20 * np.log10(rms + 1e-9)


def main():
    video, saida = sys.argv[1], sys.argv[2]
    idioma = sys.argv[3] if len(sys.argv) > 3 else 'pt'
    os.makedirs(saida, exist_ok=True)
    wav = os.path.join(saida, 'audio-16k.wav'); base = os.path.join(saida, 'whisper')
    if not os.path.exists(wav):
        leve('e3-wav', ['ffmpeg', '-v', 'error', '-y', '-i', video, '-vn', '-ac', '1', '-ar', '16000', '-c:a', 'pcm_s16le', wav])
    wav48 = os.path.join(saida, 'audio-48k.wav')      # áudio original do vídeo inteiro (o corte.py monta o áudio final a partir dele)
    if not os.path.exists(wav48):
        leve('e3-wav48', ['ffmpeg', '-v', 'error', '-y', '-i', video, '-vn', '-ac', '2', '-ar', '48000', '-c:a', 'pcm_s16le', wav48])
    if not os.path.exists(base + '.json'):
        leve('e3-whisper', ['whisper-cli', '-m', MODELO, '-l', idioma, '-dtw', DTW, '-nfa', '-ojf', '-of', base, '-np', '-f', wav])
    env = envelope(wav)
    with open(os.path.join(saida, 'envelope.csv'), 'w', newline='') as f:
        c = csv.writer(f); c.writerow(['t_ms', 'db'])
        for i, d in enumerate(env): c.writerow([i * 10, f'{d:.1f}'])
    ord_ = np.sort(env); piso = ord_[len(ord_) // 20]; topo = ord_[int(len(ord_) * 0.95)]
    lim = max(piso + 10, topo - 30)
    j = json.load(open(base + '.json', encoding='utf-8'))
    ws, frases, ant = [], [], 0
    for seg in j['transcription']:
        frases.append({'ini_ms': seg['offsets']['from'], 'fim_ms': seg['offsets']['to'], 'texto': seg['text'].strip()})
        for tk in seg['tokens']:
            t = tk['text']
            if t.startswith('[_') or not t.strip(): continue
            dtw = tk.get('t_dtw', -1)
            fim = dtw * 10 if dtw is not None and dtw >= 0 else tk['offsets']['to']
            if not re.search(r"[A-Za-zÀ-ÿ0-9$%&]", t):
                if ws: ws[-1]['palavra'] += t.strip()
                ant = max(ant, fim); continue
            if t.startswith(' ') or not ws:
                ws.append({'palavra': t.strip(), 'ini_ms': ant, 'fim_ms': fim, 'ini_whisper_ms': tk['offsets']['from'], 'p': round(tk.get('p', 0), 3)})
            else:
                ws[-1]['palavra'] += t.strip(); ws[-1]['fim_ms'] = max(ws[-1]['fim_ms'], fim)
                ws[-1]['p'] = round(min(ws[-1]['p'], tk.get('p', 1)), 3)
            ant = max(ant, fim)
    sil = lambda ms: (ms // 10) < len(env) and env[ms // 10] < lim
    for w in ws:
        ini, fim = w['ini_ms'], max(w['fim_ms'], w['ini_ms'] + 40)
        ini0 = ini
        while ini < fim - 40 and sil(ini): ini += 10
        while fim > ini + 40 and sil(fim - 10): fim -= 10
        w['ini_ms'], w['fim_ms'] = int(ini), int(fim); w['aparado_ms'] = int(ini - ini0)
    json.dump({'video': video, 'idioma': idioma, 'limiar_silencio_db': round(float(lim), 1), 'palavras': ws, 'frases': frases},
              open(os.path.join(saida, 'palavras.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    with open(os.path.join(saida, 'palavras.md'), 'w', encoding='utf-8') as f:
        f.write(f'# Transcrição palavra a palavra\n\nLimiar de silêncio: {lim:.1f} dBFS\n\n## Frases\n\n')
        for fr in frases: f.write(f"- {fr['ini_ms']/1000:.2f}–{fr['fim_ms']/1000:.2f} s · {fr['texto']}\n")
        f.write('\n## Palavras\n\n| # | início ms | fim ms | pausa antes ms | palavra | p |\n|---|---|---|---|---|---|\n')
        for i, w in enumerate(ws):
            pausa = w['ini_ms'] - ws[i - 1]['fim_ms'] if i else w['ini_ms']
            f.write(f"| {i} | {w['ini_ms']} | {w['fim_ms']} | {pausa} | {w['palavra']} | {w['p']} |\n")
    print(len(ws), 'palavras;', len(frases), 'frases; limiar', round(float(lim), 1), 'dBFS')


main()
