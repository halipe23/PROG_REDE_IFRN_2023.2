import socket
import threading
import platform

def handle_client(client_socket):
    while True:

        command = input("Digite um comando para enviar ao cliente ('exit' para sair): ")

        if command == 'exit':
            client_socket.send(command.encode('utf-8'))
            break

        client_socket.send(command.encode('utf-8'))
        response = client_socket.recv(4096)
        print("Resposta do cliente:", response.decode('utf-8'))

    client_socket.close()

def start_server():

    host = '127.0.0.1'  
    port = 5757  
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    server.listen(5)
    print(f"[*] Servidor ouvindo em {host}:{port}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"[*] Conexão recebida de {addr[0]}:{addr[1]}")
       
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
