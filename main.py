import telebot

bot_token = "1784104723:AAGWmbf5iYOCW1Z7RJsdn4E-85e4Pa2Js8U"
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
