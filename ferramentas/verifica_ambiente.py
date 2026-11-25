#!/usr/bin/env python3
"""verifica_ambiente.py · confere, em 5 segundos, se esta máquina tem tudo que o motor do Estilo Curiosidades precisa.

Uso: python3 verifica_ambiente.py
Não instala nada: diz o que falta e como instalar (macOS, Windows, Linux). Sai com código 0 se o essencial está ok.
"""
import os, sys, shutil, subprocess, platform

SO = platform.system()
ok_tudo = True
def linha(ok, nome, detalhe=''):
    print(('  [ok]  ' if ok else '  [FALTA] ') + nome + (f' · {detalhe}' if detalhe else ''))

print(f'Sistema: {SO} · Python {sys.version.split()[0]}')
if sys.version_info < (3, 9):
    linha(False, 'Python 3.9 ou mais novo'); ok_tudo = False

print('\nBibliotecas Python (pip install -r requirements.txt):')
for mod, pip, obrig in [('numpy', 'numpy', True), ('cv2', 'opencv-python', True), ('PIL', 'Pillow', True), ('psutil', 'psutil', False)]:
    try:
        m = __import__(mod); v = getattr(m, '__version__', '')
        linha(True, pip, v)
    except Exception:
        linha(not obrig, pip + ('' if obrig else ' (opcional: dá o teto de memória no Windows)'), 'não instalada')
        ok_tudo = ok_tudo and not obrig

print('\nFerramentas de linha de comando:')
for exe, dica in [('ffmpeg', 'macOS: brew install ffmpeg · Windows: winget install ffmpeg · Linux: apt install ffmpeg'),
                  ('ffprobe', 'vem junto com o ffmpeg')]:
    p = shutil.which(exe)
    linha(bool(p), exe, p or dica); ok_tudo = ok_tudo and bool(p)
p = shutil.which('whisper-cli')
linha(bool(p), 'whisper-cli (whisper.cpp)', p or 'macOS: brew install whisper-cpp · outros: github.com/ggml-org/whisper.cpp')
ok_tudo = ok_tudo and bool(p)

cands = [os.environ.get('WHISPER_MODEL', ''), os.path.expanduser('~/.cache/whisper-cpp/ggml-large-v3-turbo.bin'),
         os.path.expanduser('~/whisper.cpp/models/ggml-large-v3-turbo.bin'), os.path.expanduser('~/whisper.cpp/models/ggml-large-v3.bin')]
mod = next((c for c in cands if c and os.path.exists(c)), None)
linha(bool(mod), 'modelo do whisper', mod or 'baixe ggml-large-v3-turbo.bin (huggingface.co/ggerganov/whisper.cpp) e aponte WHISPER_MODEL=caminho')
ok_tudo = ok_tudo and bool(mod)

print('\nFonte da legenda:')
aqui = os.path.dirname(os.path.abspath(__file__))
fonte = os.path.join(aqui, '..', 'motor', 'fontes', 'Inter-Bold.ttf')
linha(os.path.exists(fonte), 'Inter-Bold.ttf (licença OFL, vai na skill)'); ok_tudo = ok_tudo and os.path.exists(fonte)

print('\nMemória:')
try:
    import psutil
    gb = psutil.virtual_memory().total / 2**30
    linha(gb >= 8, f'{gb:.0f} GB de RAM', 'o render do exemplo pico em ≈ 1,8 GB; 8 GB bastam se nada pesado rodar junto')
except Exception:
    linha(True, 'não medida (sem psutil)')

print('\nNão testado pelo autor: Windows e Linux (o motor foi feito e conferido no macOS). Se algo falhar lá, '
      'mande a mensagem de erro para o Claude: ele ajusta o caminho ou o comando.')
print('\nRESULTADO:', 'tudo certo, pode editar.' if ok_tudo else 'falta algo marcado acima.')
sys.exit(0 if ok_tudo else 1)
