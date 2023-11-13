import socket

def verificar_portas(host):
    portas = [
        (0, "TCP", "Porta de sistema"),
        (21, "TCP", "FTP"),
        (22, "TCP", "SSH"),
        (80, "TCP", "HTTP"),
        (443, "TCP", "HTTPS"),
        (53, "UDP", "DNS"),
        (123, "UDP", "NTP"),
        (3389, "TCP", "RDP"),
    ]

    for porta, protocolo, descricao in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocolo == "TCP" else socket.SOCK_DGRAM)
        resultado = sock.connect_ex((host, porta))
        status = "Responde (Aberta)" if resultado == 0 else "Não Responde (Fechada)"
        print(f"Porta {porta}: Protocolo: {protocolo}: ({descricao}) / Status: {status}")

host = input("Digite o endereço do HOST: ")
verificar_portas(host)
