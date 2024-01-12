import socket
import threading
import platform
import telebot

KEY_API = "6849345429:AAFDRM9v0KkNKjlLH59epOcwvcCntyH1fZU"
bot = telebot.TeleBot(KEY_API)

def send_info_to_bot(message, chat_id):
    try:
        bot.send_message(chat_id=chat_id, text=message)
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Erro ao enviar mensagem para o bot: {e}")

def handle_client(client_socket, addr, chat_id):
    print(f"Conexão estabelecida com {addr[0]}:{addr[1]}")

    while True:
        try:
            command = client_socket.recv(1024).decode('utf-8')
            if command.lower() == '/exit':
                break

            if command.lower() == '/get_cpu_info':
                response = get_cpu_info()
                client_socket.send(response.encode('utf-8'))
                send_info_to_bot(response, chat_id)

        except ConnectionResetError:
            print(f"A conexão com {addr[0]}:{addr[1]} foi encerrada abruptamente.")
            break
        except Exception as e:
            print(f"Erro durante a comunicação com {addr[0]}:{addr[1]}: {e}")
            break

    print(f"Conexão encerrada com {addr[0]}:{addr[1]}")
    client_socket.close()

def get_cpu_info():
    try:
        system_info = platform.uname()
        return f"Informações da CPU: {system_info.processor}"
    except Exception as e:
        return f"Erro ao obter informações da CPU: {e}"

def start_server():
    host = '127.0.0.1'
    port = 5757

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(50000)
    print(f"Servidor ouvindo em {host}:{port}")

    try:
        while True:
            client_socket, addr = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr, "YOUR_CHAT_ID"))
            client_thread.start()

    except KeyboardInterrupt:
        print("Servidor encerrado.")

    except Exception as e:
        print(f"Erro durante a execução do servidor: {e}")

    finally:
        server.close()

if __name__ == "__main__":
    start_server()



    