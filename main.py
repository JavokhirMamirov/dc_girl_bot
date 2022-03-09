import requests
import telebot
from telebot import types

# bot_token = "1784104723:AAGWmbf5iYOCW1Z7RJsdn4E-85e4Pa2Js8U"
bot_token = "5163829016:AAFamHfuTb8g84gnjosbX_MP6QiE7vGvnJU"
bot = telebot.TeleBot(bot_token)

# base_url = "http://127.0.0.1:8000"
base_url = "http://girl.eduapp.uz"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Ism va Familyangizni kiriting!")
    req = requests.post(base_url + f"/api/get-user/{message.chat.id}/", {"step": 0})


@bot.message_handler(func=lambda message: True)
def content_text(message):
    res = requests.get(base_url + f"/api/get-user/{message.chat.id}/")
    if res.ok:
        res = res.json()
        if res['success'] == True:
            if res['data']['step'] >= 0:
                req = requests.post(base_url + f"/api/set-answer/{message.chat.id}/", {"answer": message.text})
                if req.ok:
                    req = req.json()
                    if req['success'] == True and req['finish'] == False:
                        bot.send_message(message.chat.id, req['data']['query'])
                    else:
                        bot.send_message(message.chat.id, "Siz ro'yhatdan muvofaqiyatli o'tdingiz!")
        else:
            bot.send_message(message.chat.id, "Siz ro'yhatdan muvofaqiyatli o'tdingiz!")


bot.infinity_polling()
