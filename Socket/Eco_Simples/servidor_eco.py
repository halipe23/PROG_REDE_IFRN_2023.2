import socket

def servidor_echo():
    # Cria um socket TCP/IP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define o endereço e a porta do servidor
    endereco_servidor = ('localhost', 8080)

    # Vincula o socket à porta
    servidor.bind(endereco_servidor)

    # Escuta por conexões
    servidor.listen(1)

    print('Servidor de Eco iniciado. Aguardando conexões...')

    while True:
        # Aguarda por uma conexão
        conexao, endereco_cliente = servidor.accept()

        print(f'Conexão estabelecida com {endereco_cliente}')

        # Recebe a mensagem do cliente
        mensagem = conexao.recv(1024)

        # Envia a mensagem de volta ao cliente
        conexao.sendall(mensagem)

        # Fecha a conexão
        conexao.close()

if __name__ == '__main__':
    servidor_echo()
