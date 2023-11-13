import http.client

def make_get_request(url):
    # Extrai o nome do host e o caminho da URL
    host = url.split('/')[2]
    path = '/' + '/'.join(url.split('/')[3:])

    # Cria uma conexão com o servidor web
    conn = http.client.HTTPConnection(host)

    # Envia a solicitação GET
    conn.request("GET", path)

    # Obtém a resposta do servidor
    response = conn.getresponse()

    # Lê o conteúdo da resposta
    data = response.read()

    # Fecha a conexão
    conn.close()

    # Imprime a resposta recebida
    print(data.decode())

# Exemplo de uso
make_get_request("http://www.bancocn.com")
