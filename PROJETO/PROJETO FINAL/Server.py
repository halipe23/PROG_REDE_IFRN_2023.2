import socket
import threading

def handle_client(client_socket):
    while True:
        command = client_socket.recv(1024).decode('utf-8')
        if command == 'exit':
            client_socket.send('exit'.encode('utf-8'))
            break

        client_socket.send('comando não executado'.encode('utf-8'))
        response = client_socket.recv(4096)
        print("Resposta do cliente:", response.decode('utf-8'))

    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 5757

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    server.listen(5)
    print(f"Servidor ouvindo em {host}:{port}")

    while True:
        try:
            client_socket, addr = server.accept()
            print(f"Conexão recebida de {addr[0]}:{addr[1]}")

            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
        except KeyboardInterrupt:
            print("Servidor encerrado.")
            break
        except Exception as e:
            print(f"Erro ao aceitar conexão: {e}")

if __name__ == "__main__":
    start_server()
