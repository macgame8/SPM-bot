import telebot

# Insérer ici votre token d'accès Telegram
bot_token = "votre_token_ici"

# Initialisation de l'objet bot avec le token d'accès
bot = telebot.TeleBot(bot_token)

# Fonction de réponse au message "/mines"
@bot.message_handler(commands=['mines'])
def send_hello(message):
    bot.reply_to(message, "Hello !")

# Boucle de réception des messages entrants
bot.polling()
