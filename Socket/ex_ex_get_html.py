import socket, sys

# Definir as constantes
PORT = 80
CODE_PAGE = 'utf-8'
BUFFER_SIZE = 1024

# Solicitar o nome do host ou URL do site
host = input('\nInforme o nome do HOST ou URL do site: ')

# Criar o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Estabelecer a conexão
    tcp_socket.connect((host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
else:
    # Configurar o timeout
    tcp_socket.settimeout(5)

    # Enviar a requisição GET
    requisicao = f'GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
    try:
        tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    else:
        # Receber e exibir os dados
        print('-'*50)
        while True:
            resposta = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
            if not resposta:
                break
            print(resposta)
        print('-'*50)

    # Fechar o socket
    tcp_socket.close()
tcp_socket.close()
