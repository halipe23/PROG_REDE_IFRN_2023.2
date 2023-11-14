import socket
import os
from urllib.parse import urlparse

def download_image(url):
  
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    path = parsed_url.path

    if not path:
        path = "/"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       
        if parsed_url.scheme == "https":
            s.connect((hostname, 443))
        else:
            s.connect((hostname, 80))
   
        request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
        s.sendall(request.encode())

        response = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data

        double_line_break = b"\r\n\r\n"
        idx = response.find(double_line_break)
        image_data = response[idx + len(double_line_break):]

        image_filename = os.path.basename(path)
        if not image_filename:
            image_filename = "image.jpg"
            
        with open(image_filename, "wb") as image_file:
            image_file.write(image_data)

        print(f"Imagem baixada com sucesso como '{image_filename}'.")

url = input("Digite a URL completa da imagem: ")
download_image(url)