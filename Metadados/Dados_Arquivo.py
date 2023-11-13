import os

from PIL import Image
from PIL.ExifTags import TAGS

def obter_metadados_imagem(caminho_arquivo):
    try:
        imagem = Image.open(caminho_arquivo)
        exif_data = imagem._getexif()

        if exif_data is not None:
            metadados = {}
            for tag, valor in exif_data.items():
                tag_nome = TAGS.get(tag, tag)
                metadados[tag_nome] = valor

            return metadados
        else:
            print(f"A imagem {caminho_arquivo} não possui metadados EXIF.")
            return None
    except Exception as e:
        print(f"Erro ao obter metadados da imagem {caminho_arquivo}: {str(e)}")
        return None

def imprimir_metadados(metadados):
    if metadados:
        print(f"Largura da foto: {metadados.get('ExifImageWidth', 'N/A')}")
        print(f"Altura da foto: {metadados.get('ExifImageHeight', 'N/A')}")
        print(f"Fabricante da câmera: {metadados.get('Make', 'N/A')}")
        print(f"Modelo da câmera: {metadados.get('Model', 'N/A')}")
        print(f"Data/Hora de captura: {metadados.get('DateTimeOriginal', 'N/A')}")
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
