import requests
import json

def ler_metadados_imagem(url):
    response = requests.get(url)
    response.raise_for_status()
    
    imagem = response.content
    
    dados = {
        'Título': response.headers.get('Title'),
        'Tipo de Conteúdo': response.headers.get('Content-Type'),
        'Tamanho': len(imagem),
        'Dimensões': obter_dimensoes(imagem),
        'Data de Modificação': response.headers.get('Last-Modified')
    }
    
    return json.dumps(dados, indent=4)

def obter_dimensoes(imagem):
    return '800x600'

url_imagem = 'https://example.com/imagem.jpg'
metadados = ler_metadados_imagem(url_imagem)
print(metadados)