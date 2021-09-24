from telebot import *
import requests
from googlesearch import search


api = '2021833578:AAFsk5f2SdbsY_1MXn00ORp8oaabY0YCJcY'
bot = telebot.TeleBot(api)

   
@bot.message_handler(commands=['start'])
def selamat_datang(message):
   bot.reply_to(message, 'Hai saya ICA (Indonesia Covid Assistant)')
   chatid = message.chat.id
   bot.send_message(chatid, 'Selamat Datang')

@bot.message_handler(commands = ['fact'])
def fact(message):
    fact = get_fact()
    bot.send_message(message.chat.id, fact)
def get_fact():
    contents = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1').json()
    fact = contents['text']
    if len(fact) < 10:
        return get_fact()
    return fact

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

@bot.message_handler(commands = ['meow'])
def meow(message):
    url = get_url()
    bot.send_photo(message.chat.id, url)
def get_url():
    contents = requests.get('https://thatcopy.pw/catapi/rest/').json()
    image_url = contents['url']
    return image_url

@bot.message_handler(commands=['google'])
def google(message):
   data = message.text.replace('/google', "")
   x = search(data, num_results=2)
   for i in x:
      bot.send_message(message.chat.id, i)

@bot.message_handler(commands=['covid'])
def covid(message):
   texts = message.text
   provinsi = texts[7:]
   page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
   page_json = page.json()
   features = page_json['features']
   for i in features:
      prov = i['attributes']['Provinsi']
      pos =  i['attributes']['Kasus_Posi']
      sem = i['attributes']['Kasus_Semb']
      men = i['attributes']['Kasus_Meni']
      dirawat = int(pos)-int(sem)-int(men)
      data = ('''
Provinsi = {}
Positif = {}
Sembuh = {}
Meninggal= {}
Dirawat = {}
'''.format(prov, pos, sem, men, dirawat))
      if provinsi.upper() in prov.upper():
         bot.reply_to(message, data)
      else:
         pass

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')
bot.polling(True)



