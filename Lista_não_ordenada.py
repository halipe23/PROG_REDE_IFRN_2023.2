import random

n = int(input("Informe o numero de elementos que vai ser gerada: "))

lista_nao_ordenada = [random.randint(1, 10000) for _ in range(n)]

print(lista_nao_ordenada)

nome_arquivo = "lista_nao_ordenada.txt"

with open(nome_arquivo, "w") as arquivo:
    for numero in lista_nao_ordenada:
        arquivo.write(str(numero) + "\n")

print(f"A lista foi gerada e salva no arquivo '{nome_arquivo}'.")