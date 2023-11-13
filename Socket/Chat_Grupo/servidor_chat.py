import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode()
        if message == "exit":
            break
        broadcast_message(message, client_address)
    client_socket.close()

def broadcast_message(message, sender_address):
    for client in clients:
        if client != sender_address:
            client.send(message.encode())

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(5)
    print("Servidor iniciado. Aguardando conexões...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_address)
        print(f"Cliente {client_address} conectado.")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

clients = []

if __name__ == "__main__":
    start_server()
