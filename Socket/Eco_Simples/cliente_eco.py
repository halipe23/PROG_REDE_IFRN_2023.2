import socket

def cliente_echo():
    # Cria um socket TCP/IP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define o endereço e a porta do servidor
    endereco_servidor = ('localhost', 8080)

    # Conecta ao servidor
    cliente.connect(endereco_servidor)

    # Envia uma mensagem para o servidor
    mensagem = input('Digite uma mensagem: ')
    cliente.sendall(mensagem.encode())

    # Recebe a mensagem de volta do servidor
    mensagem_de_volta = cliente.recv(1024)

    print(f'Mensagem recebida do servidor: {mensagem_de_volta.decode()}')

    # Fecha a conexão
    cliente.close()

if __name__ == '__main__':
    cliente_echo()
