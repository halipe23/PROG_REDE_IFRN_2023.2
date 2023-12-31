import socket
import threading

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 5757))
        server.listen()
    except Exception as e:
        print(f'\nNão foi possível iniciar o servidor: {e}\n')
        return
    
    print("Servidor iniciado. Aguardando conexões...")
    
    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=(client,))
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            if not msg:
                break
            broadcast(msg, client)
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            deleteClient(client)
            break

def broadcast(msg, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(msg)
            except Exception as e:
                print(f"Erro ao enviar mensagem para o cliente: {e}")
                deleteClient(client)

def deleteClient(client):
    if client in clients:
        client.close()
        clients.remove(client)

main()
