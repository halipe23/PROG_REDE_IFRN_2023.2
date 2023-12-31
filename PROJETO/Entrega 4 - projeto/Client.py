import socket
import threading

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 5757))
    except ConnectionRefusedError:
        print('\nNão foi possível conectar ao servidor!\n')
        return
    
    username = input('Usuário >> ')
    print('\nConectado\n')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()

    # Aguarda a thread2 (envio de mensagens) para que o programa não termine imediatamente
    thread2.join()

    print("Encerrando conexão...")
    client.close()

def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except ConnectionResetError:
            print('\nConexão com o servidor foi perdida!\n')
            print('Pressione <Enter> para sair...')
            break

def sendMessages(client, username):
    while True:
        try:
            msg = input('')
            if msg.strip() == '':
                break
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except ConnectionResetError:
            print('\nConexão com o servidor foi perdida!\n')
            break

    print('Encerrando envio de mensagens...')

if __name__ == "__main__":
    main()
