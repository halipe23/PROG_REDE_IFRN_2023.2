import socket

def verificar_portas(host):
    portas = [
        (0, "TCP", "Porta de sistema"),
        (21, "TCP", "FTP"),
        (22, "TCP", "SSH"),
        (23, "TCP", "TELNET"),
        (25, "TCP", "SMTP"),
        (53, "UDP", "DNS"),
        (80, "TCP", "HTTP"),
        (110, "TCP", "POP3"),
        (115, "TCP", "SFTP"),
        (123, "UDP", "NTP"),
        (137, "UDP", "NetBIOS"),
        (138, "UDP", "NetBIOS Datagram Service"),
        (139, "TCP", "NetBIOS Session Service"),
        (143, "TCP", "IMAP"),
        (161, "UDP", "SNMP"),
        (179, "TCP", "BGP"),
        (443, "TCP", "HTTPS"),
        (465, "TCP", "SMTPS"),
        (514, "UDP", "Syslog"),
        (546, "UDP", "DHCPv6 Client"),
        (547, "UDP", "DHCPv6 Server"),
        (587, "TCP", "SMTP Submission"),
        (636, "TCP", "LDAPS"),
        (993, "TCP", "IMAPS"),
        (995, "TCP", "POP3S"),
    ]
    for porta, protocolo, descricao in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocolo == "TCP" else socket.SOCK_DGRAM)
        resultado = sock.connect_ex((host, porta))
        status = "Responde (Aberta)" if resultado == 0 else "Não Responde (Fechada)"
        print(f"Porta {porta}: Protocolo: {protocolo}: ({descricao}) / Status: {status}")

host = input("Digite o endereço do HOST: ")
verificar_portas(host)
