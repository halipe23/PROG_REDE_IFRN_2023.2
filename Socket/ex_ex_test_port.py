import socket, sys

strhost = input('\nInforme o nome do HOST ou URL do site: ')
iphost = socket.gethostbyname(strhost)
lstport = [22, 23, 25, 80, 443, 8080]

for port in lstport:
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    #sock.timeout(3)
    try:
        sock.connect((iphost, port))
    except:
        print(f'ERRO {port} {sys.exc_info()[0]}')
    else:
        print(f'porta: {port} ok')
        sock.close()