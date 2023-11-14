import socket
import os

def download_imagem(url):
    host, image_path = url.split('/', 3)[2:]

    nome_arquivo = os.path.basename(image_path)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))

    s.sendall(f"GET /{image_path} HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())

    resposta = b""
    while True:
        dados = s.recv(4096)
        if not dados:
            break
        resposta += dados

    s.close()

    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(resposta)

    print("Imagem baixada com sucesso!")

url = input("Digite a URL completa da imagem: ")

download_imagem(url)