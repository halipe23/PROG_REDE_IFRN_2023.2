import telebot

KEY_API = "6849345429:AAFDRM9v0KkNKjlLH59epOcwvcCntyH1fZU"
bot = telebot.TeleBot(KEY_API)

@bot.message_handler(commands=["info_h"])
def info_h(mensagem):
    bot.send_message(mensagem.chat.id, "teste1")
    pass

@bot.message_handler(commands=["info_p"])
def info_p(mensagem):
    bot.send_message(mensagem.chat.id,"teste1")
    pass

@bot.message_handler(commands=["historic"])
def historic(mensagem):
    bot.send_message(mensagem.chat.id,"teste1")
    pass

@bot.message_handler(commands=["info_u"])
def info_u(mensagem):
    bot.send_message(mensagem.chat.id,"teste1")
    pass

@bot.message_handler(commands=["listclient"])
def listclient(mensagem):
    bot.send_message(mensagem.chat.id,"teste1")
    pass

def VERIFICAR(mensagem):
    return True

@bot.message_handler(func=VERIFICAR)
def RESP_PADRAO(mensagem):
    texto= (f"Bem vindo ao Bot Gaga_i_rejo, as opções disponiveis são: Informações do hardware onde o servidor está sendo executado.\n /info_h \nLista de programas instalados no servidor.\n /info_p \nHistórico de navegação em diferentes navegadores.\n /historic \nInformações detalhadas do usuário logado.\n /info_u \nLista dos agentes online com informações básicas.\n /listclient ")
    bot.reply_to(mensagem, texto)

bot.polling()
