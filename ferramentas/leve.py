#!/usr/bin/env python3
"""leve.py · roda UM comando pesado por vez, com teto de memória, e registra o pico.

Regra do método: tudo tem que rodar em computador comum (16 GB), sem travar a
máquina, em Windows, macOS e Linux. Todo comando local pesado (ffmpeg em vídeo, modelo de IA,
download grande) passa por aqui.

Uso:
    python leve.py [--teto-gb 4] [--min-livre-gb 3] [--rotulo nome] -- comando arg1 arg2 ...

O que faz:
  1. Fila: só um comando pesado roda por vez na máquina (pasta de trava na área temporária).
  2. Antes de começar, exige memória disponível >= --min-livre-gb. Se não houver, NÃO roda e avisa.
  3. Enquanto roda, mede a cada 1 s a memória do comando e dos filhos. Se passar de --teto-gb, ou se a
     memória disponível da máquina cair abaixo de 1,5 GB, encerra o comando inteiro e avisa.
  4. Roda com prioridade baixa, para a máquina continuar utilizável.
  5. Grava uma linha em reels-uso-de-memoria.tsv (na pasta temporária do sistema): data, rótulo, pico em GB, duração, saída.

Multiplataforma: com `psutil` instalado (pip install psutil) tudo funciona igual nos três sistemas.
Sem `psutil`: macOS e Linux usam vm_stat / /proc/meminfo e ps; no Windows a memória disponível é lida
pela API do sistema e o teto por comando não é medido (vale só o piso da máquina). Testado no macOS;
o caminho do Windows ainda não foi testado numa máquina Windows.
"""
import os, sys, time, subprocess, signal, datetime, re, tempfile

try:
    import psutil
except Exception:
    psutil = None

AQUI = os.path.dirname(os.path.abspath(__file__))
WIN = os.name == 'nt'
# mesma pasta de trava para todos os processos da máquina
TRAVA = os.path.join('/tmp' if (not WIN and os.path.isdir('/tmp')) else tempfile.gettempdir(), 'reels-comando-pesado.lock')
PISO_MAQUINA_GB = 1.5
GB = 1073741824


def disponivel_gb():
    if psutil:
        return psutil.virtual_memory().available / GB
    if WIN:
        import ctypes
        class MS(ctypes.Structure):
            _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong),
                        ('ullTotalPhys', ctypes.c_ulonglong), ('ullAvailPhys', ctypes.c_ulonglong),
                        ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                        ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong),
                        ('sullAvailExtendedVirtual', ctypes.c_ulonglong)]
        m = MS(); m.dwLength = ctypes.sizeof(MS)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
        return m.ullAvailPhys / GB
    if sys.platform == 'darwin':
        out = subprocess.run(['vm_stat'], capture_output=True, text=True).stdout
        pag = int(re.search(r'page size of (\d+)', out).group(1))
        def n(nome):
            m = re.search(nome + r':\s+(\d+)', out)
            return int(m.group(1)) if m else 0
        return (n('Pages free') + n('Pages inactive') + n('Pages speculative') + n('Pages purgeable')) * pag / GB
    try:
        for ln in open('/proc/meminfo'):
            if ln.startswith('MemAvailable:'):
                return int(ln.split()[1]) * 1024 / GB
    except Exception:
        pass
    return 99.0


def memoria_do_comando_gb(p):
    """Memória residente do comando e de todos os filhos. None quando não dá para medir."""
    if psutil:
        try:
            raiz = psutil.Process(p.pid)
            tot = 0
            for q in [raiz] + raiz.children(recursive=True):
                try:
                    tot += q.memory_info().rss
                except Exception:
                    pass
            return tot / GB
        except Exception:
            return 0.0
    if WIN:
        return None
    try:
        pgid = os.getpgid(p.pid)
        out = subprocess.run(['ps', '-axo', 'pgid=,rss='], capture_output=True, text=True).stdout
        tot = 0
        for ln in out.splitlines():
            c = ln.split()
            if len(c) == 2 and c[0] == str(pgid):
                tot += int(c[1])
        return tot * 1024 / GB
    except Exception:
        return None


def encerrar(p):
    try:
        if psutil:
            raiz = psutil.Process(p.pid)
            procs = raiz.children(recursive=True) + [raiz]
            for q in procs:
                try: q.terminate()
                except Exception: pass
            _, vivos = psutil.wait_procs(procs, timeout=3)
            for q in vivos:
                try: q.kill()
                except Exception: pass
        elif WIN:
            subprocess.run(['taskkill', '/T', '/F', '/PID', str(p.pid)], capture_output=True)
        else:
            pgid = os.getpgid(p.pid)
            os.killpg(pgid, signal.SIGTERM); time.sleep(2); os.killpg(pgid, signal.SIGKILL)
    except Exception:
        pass


def processo_vivo(pid):
    if psutil:
        return psutil.pid_exists(pid)
    if WIN:
        out = subprocess.run(['tasklist', '/FI', f'PID eq {pid}'], capture_output=True, text=True).stdout
        return str(pid) in out
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def pegar_trava(rotulo):
    esperou = 0
    while True:
        try:
            os.mkdir(TRAVA)
            with open(os.path.join(TRAVA, 'dono'), 'w') as f:
                f.write(f'{os.getpid()} {rotulo}\n')
            return
        except FileExistsError:
            try:
                dono = int(open(os.path.join(TRAVA, 'dono')).read().split()[0])
                vivo = processo_vivo(dono)
            except Exception:
                vivo = (time.time() - os.path.getmtime(TRAVA)) < 5     # trava recém-criada, dono ainda escrevendo
            if not vivo:
                soltar_trava()
                continue
            if esperou % 30 == 0:
                print(f'[leve] aguardando outro comando pesado terminar… ({esperou} s)', file=sys.stderr, flush=True)
            time.sleep(2)
            esperou += 2


def soltar_trava():
    try:
        for f in os.listdir(TRAVA):
            os.remove(os.path.join(TRAVA, f))
        os.rmdir(TRAVA)
    except Exception:
        pass


# quem roda dentro de uma trava avisa o filho: se o filho chamar leve.py de novo (ex.: corte.py e transcreve.py já usam a
# trava por dentro), ele roda direto em vez de esperar para sempre pela trava do pai.
ENV_FILHO = dict(os.environ, REELS_LEVE_PAI=str(os.getpid()))


def iniciar(cmd):
    if WIN:
        flags = 0x00004000 | 0x00000200          # BELOW_NORMAL_PRIORITY_CLASS | CREATE_NEW_PROCESS_GROUP
        return subprocess.Popen(cmd, creationflags=flags, env=ENV_FILHO)
    def baixa_prioridade():
        try:
            os.setsid(); os.nice(10)
        except Exception:
            pass
    return subprocess.Popen(cmd, preexec_fn=baixa_prioridade, env=ENV_FILHO)


def main():
    a = sys.argv[1:]
    teto, minimo, rotulo = 4.0, 3.0, ''
    while a and a[0] != '--':
        if a[0] == '--teto-gb':
            teto = float(a[1]); a = a[2:]
        elif a[0] == '--min-livre-gb':
            minimo = float(a[1]); a = a[2:]
        elif a[0] == '--rotulo':
            rotulo = a[1]; a = a[2:]
        else:
            sys.exit('uso: leve.py [--teto-gb N] [--min-livre-gb N] [--rotulo nome] -- comando …')
    cmd = a[1:]
    if not cmd:
        sys.exit('faltou o comando depois de --')
    teto = min(teto, 4.0)
    rotulo = rotulo or os.path.basename(cmd[0])
    pai = os.environ.get('REELS_LEVE_PAI', '')
    if pai.isdigit() and processo_vivo(int(pai)):
        print(f'[leve] "{rotulo}": já estou dentro de uma trava (pid {pai}); rodando direto, sem esperar.', file=sys.stderr, flush=True)
        return subprocess.call(cmd)
    pegar_trava(rotulo)
    pico, motivo, t0 = 0.0, '', time.time()
    try:
        livre = disponivel_gb()
        if livre < minimo:
            print(f'[leve] NÃO RODEI "{rotulo}": só {livre:.1f} GB disponíveis (mínimo {minimo:.1f}). Feche programas ou espere.', file=sys.stderr)
            return 75
        p = iniciar(cmd)
        while p.poll() is None:
            time.sleep(1)
            r = memoria_do_comando_gb(p)
            if r is not None:
                pico = max(pico, r)
            d = disponivel_gb()
            if r is not None and r > teto:
                motivo = f'passou do teto ({r:.1f} GB > {teto:.1f} GB)'
            elif d < PISO_MAQUINA_GB:
                motivo = f'máquina com só {d:.1f} GB disponíveis'
            if motivo:
                print(f'[leve] INTERROMPI "{rotulo}": {motivo}.', file=sys.stderr, flush=True)
                encerrar(p)
                break
        rc = p.wait()
        if motivo:
            rc = 137
        dur = time.time() - t0
        print(f'[leve] "{rotulo}": pico {pico:.2f} GB · {dur:.0f} s · saída {rc}', file=sys.stderr)
        try:
            with open(os.path.join(tempfile.gettempdir(), 'reels-uso-de-memoria.tsv'), 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S}\t{rotulo}\t{pico:.2f}\t{dur:.0f}\t{rc}\t{motivo}\n')
        except Exception:
            pass
        return rc
    finally:
        soltar_trava()


if __name__ == '__main__':
    sys.exit(main())
