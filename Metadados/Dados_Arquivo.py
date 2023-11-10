import os
import requests
import json

def ler_metadados_imagem(diretorio):
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".jpg") or arquivo.endswith(".jpeg"):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            with open(caminho_arquivo, "rb") as imagem:
                dados_imagem = imagem.read()
                url = "https://api.metadados.com/analyze"
                headers = {"Content-Type": "application/octet-stream"}
                response = requests.post(url, headers=headers, data=dados_imagem)
                if response.status_code == 200:
                    metadados = json.loads(response.text)
                    print(f"Metadados da imagem {arquivo}:")
                    print(json.dumps(metadados, indent=4))
                else:
                    print(f"Erro ao obter metadados da imagem {arquivo}")

diretorio = input("Digite o nome do diretório: ")
ler_metadados_imagem(diretorio)