import os
import json

def obter_metadados_imagem(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            arquivo.seek(0)
            imagem = arquivo.read()

        metadados = {}
        metadados['Tamanho'] = os.path.getsize(caminho_arquivo)
        metadados['Nome'] = os.path.basename(caminho_arquivo)
        metadados['Extensao'] = os.path.splitext(caminho_arquivo)[1]
        metadados['Diretorio'] = os.path.dirname(caminho_arquivo)

        return metadados
    except Exception as e:
        print(f"Erro ao obter metadados da imagem {caminho_arquivo}: {str(e)}")
        return None

def imprimir_metadados(metadados):
    if metadados:
        for chave, valor in metadados.items():
            print(f"{chave}: {valor}")
        print("\n")

def ler_metadados_imagem(diretorio):
    for arquivo in os.listdir(diretorio):
        nome_arquivo, extensao = os.path.splitext(arquivo)
        if extensao.lower() in [".jpg", ".jpeg"]:
            caminho_arquivo = os.path.join(diretorio, arquivo)
            metadados = obter_metadados_imagem(caminho_arquivo)
            imprimir_metadados(metadados)

diretorio = input("Digite o nome do diretório: ")
ler_metadados_imagem(diretorio)
