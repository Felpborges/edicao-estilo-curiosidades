#!/usr/bin/env python3
"""servidor_painel.py · abre uma pasta num servidor local que aceita pedidos por faixa (Range).

Por que existe: o painel de plano de edição tem um player do SEU vídeo posicionado em cada trecho. O navegador só
consegue pular para o trecho se o servidor responder a pedidos de faixa de bytes; o `python3 -m http.server` comum não
responde, e todos os players abririam no começo do vídeo.

Uso:  python3 servidor_painel.py <pasta> [porta=8765]      (a pasta é a RAIZ DA EDIÇÃO, ex.: edicoes/2026-12-01-meu-reel)
Abra:  http://localhost:8765/03-plano/plano-de-edicao.html
Só escuta em 127.0.0.1 (a sua máquina). Ctrl+C para parar. Roda igual em macOS, Windows e Linux.
"""
import os, sys, re, http.server, socketserver

RAIZ = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
PORTA = int(sys.argv[2]) if len(sys.argv) > 2 else 8765


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=RAIZ, **k)

    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def do_GET(self):
        rng = self.headers.get('Range')
        caminho = self.translate_path(self.path)
        if not rng or not os.path.isfile(caminho):
            return super().do_GET()
        m = re.match(r'bytes=(\d*)-(\d*)$', rng.strip())
        tam = os.path.getsize(caminho)
        if not m or (m.group(1) == '' and m.group(2) == ''):
            return super().do_GET()
        if m.group(1) == '':                       # últimos N bytes
            ini, fim = max(0, tam - int(m.group(2))), tam - 1
        else:
            ini = int(m.group(1)); fim = int(m.group(2)) if m.group(2) else tam - 1
        fim = min(fim, tam - 1)
        if ini > fim or ini >= tam:
            self.send_response(416); self.send_header('Content-Range', f'bytes */{tam}'); self.end_headers(); return
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(caminho))
        self.send_header('Content-Range', f'bytes {ini}-{fim}/{tam}')
        self.send_header('Content-Length', str(fim - ini + 1))
        self.end_headers()
        try:
            with open(caminho, 'rb') as f:
                f.seek(ini); resto = fim - ini + 1
                while resto > 0:
                    b = f.read(min(1 << 20, resto))
                    if not b: break
                    self.wfile.write(b); resto -= len(b)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def log_message(self, *a):
        pass


class S(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == '__main__':
    with S(('127.0.0.1', PORTA), H) as srv:
        print(f'Servindo {RAIZ}\nAbra: http://localhost:{PORTA}/03-plano/plano-de-edicao.html   (Ctrl+C para parar)')
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print('\nparado.')
