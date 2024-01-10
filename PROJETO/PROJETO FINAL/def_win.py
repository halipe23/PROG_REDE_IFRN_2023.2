import platform
import subprocess
import os
import sqlite3
from browser_history.browsers import Chrome, Edge, Firefox

def infohardwareW():
    def memoria_windows():
        try:
            resultado = subprocess.run(['systeminfo'], capture_output=True, text=True)
            systeminfo = resultado.stdout
            memoria_total = [linha for linha in systeminfo.split('\n') if 'Memória física total:' in linha]
            total = memoria_total[0].split(':')[-1].strip()
            memoria_dis = [linha for linha in systeminfo.split('\n') if 'Memória física disponível:' in linha]
            disponivel = memoria_dis[0].split(':')[-1].strip()

            final = f"Memória Total: {total}\nMemória Disponível: {disponivel}"
            return final
        except:
            return "Não foi possível receber a informação de memória"

    def disco_windows():
        try:
            resultado = subprocess.run(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'], capture_output=True, text=True)
            linhas = resultado.stdout.strip().split('\n')
            dados = linhas[2].split()
            vazio = int(dados[1]) / (1024 ** 3)
            total = int(dados[2]) / (1024 ** 3)

            informacoes_discos = f"Espaço livre em disco: {vazio:.2f} GB\nEspaço total em disco: {total:.2f} GB"
            return informacoes_discos
        except:
            return "Não foi possível receber a informação de disco"

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
        f"\n----- INFORMAÇÕES DE DISCO -----\n{disco_windows()}\n"
        f"\n----- INFORMAÇÕES DE MEMÓRIA -----\n{memoria_windows()}"
    )

    return informacoes

def hisgoogleW():
    try:
        b = Chrome()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)  # Linha separadora
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except:
        return "Erro ao tentar receber histórico de navegação do Google!!!"

def hisedgeW():
    try:
        b = Edge()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)  # Linha separadora
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except:
        return "Erro ao tentar receber histórico de navegação do Microsoft Edge!!!"

def hisfirefoxW():
    try:
        b = Firefox()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)  # Linha separadora
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except:
        return "Erro ao tentar receber histórico de navegação do Mozilla Firefox!!!"

def hisoperaW():
    try:
        final = ''
        con = sqlite3.connect(fr'C:\Users\{os.getlogin()}\AppData\Roaming\Opera Software\Opera Stable\Default\History')
        cur = con.cursor()
        cur.execute("select url, title, visit_count from urls")
        results = cur.fetchall()
        for result in results:
            final += (result)
        
        return final
    except:
        return "Erro ao tentar receber histórico de navegação do Opera!!!"

def infouserW():
    def gruposusuariowin():
        try:
            resultado = subprocess.run(['net', 'user', os.getlogin()], capture_output=True, text=True, encoding='cp437')
            linhas = resultado.stdout.strip().splitlines()

            imprimir = False
            inicio = 'Associações de Grupo Local'
            fim = 'Comando concluído com êxito.'
            informações = ""

            for linha in linhas:
                if fim in linha:
                    break
                if inicio in linha:
                    imprimir = True
                if imprimir:
                    linha = linha.replace('Associações', 'Associações')
                    informações += linha + '\n'
            return informações
        except:
            return 'Não foi possível obter as informações do Agente'

    def usersid():
        try:    
            sid = None
            out = subprocess.Popen("wmic useraccount get name, sid", stdout=subprocess.PIPE)
            out = out.communicate()[0].decode().replace("\r", "")
            for line in out.split("\n"):
                if line.startswith(os.getlogin()):        
                    sid = line.replace(os.getlogin(), "").strip()
                    return sid
                
        except Exception as e:
            print(f'Erro: {e}')
            return 'Não foi possível obter as informações do SID do Agente'
    
    usuario = os.getlogin()
    informacoes_usuario = f'''
    ---------------- INFORMAÇÕES DE USUÁRIO ----------------

    O Diretório Inicial do Usuário {usuario} é: '{os.environ['USERPROFILE']}'
    O SID do usuário {usuario} é: {usersid()}
    Os grupos que o usuário {usuario} está associado são:
    {gruposusuariowin()}
    Nome do Executável do usuário {usuario} é: {os.path.basename(os.environ['ComSpec'])}
    '''
    return informacoes_usuario

def progwindows():
    try:
        resultado = subprocess.run(['wmic', 'product', 'get', 'name'], capture_output=True, text=True)
        linhas = resultado.stdout.splitlines()
        informacoes = "\n---------- INFORMAÇÕES DE PROGRAMAS INSTALADOS ----------\n\n"
        for linha in linhas[2:-3]:
            informacoes += linha + "\n"

        return informacoes
    except:
        return f'Não foi possível obter as informações de programas instalados:'
