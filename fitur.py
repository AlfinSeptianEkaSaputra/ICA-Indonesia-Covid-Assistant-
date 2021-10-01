from telebot import *
import api

bot = telebot.TeleBot(api.API_KEYS)
def sample_responses(input_text, namauser):
    pesan_user = str(input_text).lower()
    
@bot.message_handler(commands=['google'])
def google(message):
   data = message.text.replace('/google', "")
   x = search(data, num_results=2)
   for i in x:
      bot.send_message(message.chat.id, i)
