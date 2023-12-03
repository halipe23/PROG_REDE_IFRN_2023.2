import socket

def client():
    host = 'localhost'
    port = 12345

    # Criação do socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    while True:
        # Solicita ao usuário o comando a ser enviado ao servidor
        comando = input("Digite o comando: ")

        # Envia o comando para o servidor
        sock.send(comando.encode())

        # Recebe a resposta do servidor
        response = sock.recv(1024).decode()
        print("Resposta do servidor:", response)

        # Encerra a conexão se o comando for "/exit"
        if comando == "/exit":
            break

    # Fecha a conexão
    sock.close()

if __name__ == '__main__':
    client()
