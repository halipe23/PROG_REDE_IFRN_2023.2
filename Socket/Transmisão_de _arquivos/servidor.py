import socket

def conexao():
    # Configuração do servidor
    host = 'localhost'
    porta = 12345

    # Criação do socket
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket ao endereço e porta
    servidor.bind((host, porta))

    # Coloca o servidor em modo de escuta
    servidor.listen(1)

    print('Servidor de Transmissão de Arquivos iniciado.')

    while True:
        # Aceita uma conexão do cliente
        cliente, endereco = servidor.accept()
        print('Conexão estabelecida com', endereco)

        # Recebe o nome do arquivo do cliente
        nome_arquivo = cliente.recv(1024).decode()

        try:
            # Abre o arquivo em modo de leitura binária
            arquivo = open(nome_arquivo, 'rb')

            # Lê o conteúdo do arquivo
            conteudo = arquivo.read()

            # Envia o conteúdo do arquivo de volta ao cliente
            cliente.send(conteudo)

            # Fecha o arquivo
            arquivo.close()

            print('Arquivo', nome_arquivo, 'enviado com sucesso.')

        except FileNotFoundError:
            print('Arquivo', nome_arquivo, 'não encontrado.')

        # Fecha a conexão com o cliente
        cliente.close()

if __name__ == '__main__':
    conexao()
