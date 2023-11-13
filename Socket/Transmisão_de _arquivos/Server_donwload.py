import socket

def enviar_arquivo(nome_arquivo, endereco_cliente, porta):
    # Cria o socket do servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define o endereço e a porta do servidor
    endereco_servidor = ('localhost', 1234)
    
    # Vincula o socket do servidor ao endereço e porta especificados
    servidor.bind(endereco_servidor)
    
    # Coloca o servidor em modo de escuta
    servidor.listen(1)
    
    print('Servidor pronto para receber conexões...')
    
    while True:
        # Aceita a conexão do cliente
        conexao, endereco_cliente = servidor.accept()
        
        print('Conexão estabelecida com o cliente:', endereco_cliente)
        
        # Abre o arquivo solicitado pelo cliente
        try:
            arquivo = open(nome_arquivo, 'rb')
        except FileNotFoundError:
            print('Arquivo não encontrado.')
            conexao.sendall('Arquivo não encontrado.')
            conexao.close()
            continue
        
        # Lê o conteúdo do arquivo
        conteudo = arquivo.read()
        
        # Envia o conteúdo do arquivo para o cliente
        conexao.sendall(conteudo)
        
        print('Arquivo enviado com sucesso.')
        
        # Fecha a conexão com o cliente
        conexao.close()
        
        break
    
    # Fecha o socket do servidor
    servidor.close()

# Exemplo de uso da função enviar_arquivo
enviar_arquivo('arquivo.txt', 'localhost', 8000)
