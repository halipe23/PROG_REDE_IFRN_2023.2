import socket

def server():
    host = 'localhost'
    port = 12345

    # Criação do socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)

    print("Aguardando conexão do cliente...")

    # Aceita a conexão do cliente
    conexao, add = sock.accept()
    print("Cliente conectado:", add)

    while True:
        # Recebe a mensagem do cliente
        data = conexao.recv(1024).decode()
        if not data:
            break

        # Verifica a mensagem recebida e envia a resposta adequada
        if data == "/info-h":
            response = "Essas são as informações do hardware."
        elif data == "/info-p":
            response = "Essas são os programas instalados."
        elif data == "/historic":
            response = "Essas são os históricos de navegação."
        elif data == "/info-u":
            response = "Essas são as informações detalhadas do usuário logado."
        elif data == "/listclient":
            response = "Essas são as informações dos agentes online."
        else:
            response = "Comando inválido."

        # Envia a resposta para o cliente
        conexao.send(response.encode())

    # Fecha a conexão
    conexao.close()

if __name__ == '__main__':
    server()
