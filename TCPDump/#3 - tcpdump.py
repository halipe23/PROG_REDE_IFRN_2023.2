from def_tcpdump import ler_cabecalho_arquivo, ler_pacote

caminho_arquivo = input("Digite o caminho do arquivo TCPdump: ")

with open(caminho_arquivo, 'rb') as tcpdump:
    ler_cabecalho_arquivo(tcpdump)

    for _ in range(2):
        ler_pacote(tcpdump)