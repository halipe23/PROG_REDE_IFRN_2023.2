import platform, subprocess, socket
from browser_history.browsers import Chrome, Edge, Firefox
import os, sqlite3
def infohardwareL():
    def memoria_linux():
        try:
            cabeçalho = subprocess.run('free | grep "total"', capture_output=True, text=True, shell=True)
            memoria = subprocess.run('free -m | grep "Mem:"', capture_output=True, text=True, shell=True)

            informacoes = f"\nInformações detalhadas sobre a memória física:\n{cabeçalho.stdout}\n{memoria.stdout}"

            return informacoes
        except:
            return f"Erro ao obter informações de memória"

    def disco_linux():
        try:
            cabeçalho = subprocess.run('df -h | grep -i "File"', shell=True, capture_output=True, text=True)
            discos = ["/dev/sda", "/dev/root", "/dev/mapper", "/dev/nvme0n1p1"]

            for disco in discos:
                try:
                    armazenamento = subprocess.run(f'df -h | grep -i "{disco}"', capture_output=True, text=True, shell=True)
                    break
                except: continue 

            informacoes = f"\nInformações detalhadas sobre o disco:\n\n{cabeçalho.stdout}{armazenamento.stdout}"

            return informacoes
        except:
            return f"Erro ao obter informações de disco"

    try:
        sistema_operacional = platform.system()
        processador = platform.processor()
        arquitetura = platform.architecture()
    except:
        return 'Não foi possível obter as informações de Hardware'

    informacoes = (
        f"\n----- INFORMAÇÕES DE CPU -----\n"
        f"Sistema Operacional: {sistema_operacional}\n"
        f"Processador: {processador}\n"
        f"Arquitetura: {arquitetura[0]} {arquitetura[1]}\n"
        f"\n----- INFORMAÇÕES DE DISCO -----\n{disco_linux()}\n"
        f"\n----- INFORMAÇÕES DE MEMÓRIA -----\n{memoria_linux()}"
    )

    return informacoes

def infouserL():
    def grupos_linux():
        try:
            usuario = os.getlogin()
            resultado = subprocess.run(['groups', usuario], capture_output=True, text=True, shell=True)
            grupos = resultado.stdout.strip().split()
            secundarios = ('\n'.join(grupos[3:]))

            saida = f"\n--- Grupo Principal ---\n{grupos[2]}\n\n--- Grupos Secundários ---\n{secundarios}"
            return saida
        except:
            return 'Não foi possível obter as informações de grupos do usuário'

    return (f"Usuário: {os.getlogin()}\n"
        f"Diretório Inicial: {os.path.expanduser('~')}\n"
        f"Identificação de usuário: UID = {os.getuid()}\n"
        f"Os grupos do usuário são: {grupos_linux()}\n"
        f"\nO Shell padrão do Usuário é: {os.environ['SHELL']}")

def hisfirefoxL():
    firefox = f"/home/{os.getlogin()}/.mozilla/firefox/"
    diretorio = [folder for folder in os.listdir(firefox) if folder.endswith(".default-esr")][0]
    caminho = os.path.join(firefox, diretorio, "places.sqlite")

    con = sqlite3.connect(caminho)
    cur = con.cursor()

    cur.execute("select url, title, visit_count from moz_places")

    resultado = cur.fetchall()

    for item in resultado:
        url, title, visit_count = item
        print(f"URL: {url}\nTitle: {title}\nVisit Count: {visit_count}\n")

    con.close()

def hisgoogleL():
    con = sqlite3.connect(f"/home/{os.getlogin()}/.config/google-chrome/Default/History")
    cur = con.cursor()
    cur.execute("select url, title, visit_count from urls")
    results = cur.fetchall()
    for result in results:
        print(result)

def hisedgeL():
    con = sqlite3.connect(f"/home/{os.getlogin()}/.config/microsoft-edge/Default/History")
    cur = con.cursor()
    cur.execute("select url, title, visit_count from urls")
    results = cur.fetchall()
    for result in results:
        print(result)

def operaL():
    con = sqlite3.connect(f"/home/{os.getlogin()}/.config/opera/Default/History")
    cur = con.cursor()
    cur.execute("select url, title, visit_count from urls")
    results = cur.fetchall()
    for result in results:
        print(result)
        
def ipagentesL():
    try:
        informacoes = (f"\n---- INFORMAÇÕES DO AGENTE ----\n\nNome do host: {socket.gethostname()}\n"
        f"Usuário logado: {os.getlogin()}\n"
        f"IP do Host: {socket.gethostbyname(socket.gethostname())}\n")
        return informacoes
    except:
        return 'Não foi possível obter as informações do Agente'
    
def proglinux():
    try:
        resultado = subprocess.run(['apt', 'list', '--installed'], capture_output=True, text=True, shell=True)
        linhas = resultado.stdout.splitlines()

        informacoes = "\n---------- INFORMAÇÕES DE PROGRAMAS INSTALADOS ----------\n\n"
        for linha in linhas[2:-3]:
            informacoes += linha + "\n"

        return informacoes
    except:
        return (f'Não foi possível obter as informações de programas instalados:')
    

    