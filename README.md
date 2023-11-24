# PROG_REDE_IFRN_2023.2

# Projeto de Servidor de Agentes com Controle via Bot no Telegram

# Descrição:
  Este projeto consiste em um servidor que gerencia agentes e permite interagir com eles via Telegram. 
  Os agentes estão conectados ao servidor e podem fornecer informações como IP, nome do host, usuário logado e tempo online. 
  O bot no Telegram permite aos usuários enviar comandos para obter essas informações dos agentes.

# Tipo de Socket:
  Utiliza socket TCP no servidor para garantir controle de transmissão.

# Funcionalidades:
  Lista de agentes online
  Comando para listar agentes conectados: 
  Informações disponíveis: IP, nome do host, usuário logado e tempo online
  Integração com Telegram
  Bot para interagir com os agentes
  Comandos específicos para recuperar informações dos agentes

# Comandos do BOT no Telegram:

 Implementação de comandos via bot no Telegram para:
  - Informações do hardware onde o servidor está sendo executado.
  ====================== /info-h =======================
  - Lista de programas instalados no servidor.
  ====================== /info-p =======================
  - Histórico de navegação em diferentes navegadores.
  ===================== /historic ======================
  - Informações detalhadas do usuário logado.
  ====================== /info-u =======================
  - Lista dos agentes online com informações básicas.
  ====================== /listclient =====================

# Tecnologias Utilizadas:
Python
Telegram API
(Outras bibliotecas nativas do python)
