from telebot import *
import api

bot = telebot.TeleBot(api.API_KEY)

@bot.message_handler(commands=['google'])
def google(message):
   data = message.text.replace('/google', "")
   x = search(data, num_results=2)
   for i in x:
      bot.send_message(message.chat.id, i)

bot.polling()
