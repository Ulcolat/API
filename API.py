#Librerías y token
from config import *
import telebot

#Inicializar el bot
API=telebot.TeleBot(tokenAPI)

#Comando /start
@API.message_handler(commands=["start"])
def start(message):
    #Da la bienvenida al usuario
    API.reply_to(message,"Hola, bienvenido a mi bot :D")

#Carecteres diferentes al comando /start
@API.message_handler(content_types=["text"])
def messsage_txt(message):
    if message.text.startswith("/"):
        API.send_message(message.chat.id,"Comando no disponible")
    else:
        API.send_message(message.chat.id,"No sé que decirte...")


#          MAIN    ##################
if __name__ =='__main__':
    print("Iniciando API")
    API.infinity_polling()