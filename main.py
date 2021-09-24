from telebot import *
import requests
from googlesearch import search


api = '2021833578:AAFsk5f2SdbsY_1MXn00ORp8oaabY0YCJcY'
bot = telebot.TeleBot(api)

   #menu start
@bot.message_handler(commands=['start'])
def selamat_datang(message):
   bot.reply_to(message, 'Hai saya ICA (Indonesia Covid Assistant)')
   chatid = message.chat.id
   bot.send_message(chatid, 'Selamat Datang')
   
   #menu google
@bot.message_handler(commands=['google'])
def google(message):
   data = message.text.replace('/google', "")
   x = search(data, num_results=2)
   for i in x:
      bot.send_message(message.chat.id, i)
      
   #sticker
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
      
    # menu Akses ke layanan kesehatan terdekat  
@bot.message_handler(commands=['rumahsakit'])
def rumahsakit(message):
   texts = message.text
   Wilayah = texts[7:]
   page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/RS_Rujukan_Update_May_2020/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
   page_json = page.json()
   features = page_json['features']
   for i in features:
      nam = i['attributes']['nama']
      koders =  i['attributes']['kode_rs']
      almt = i['attributes']['alamat']
      wlyh = i['attributes']['wilayah']
      tlpn = i['attributes']['telepon']
      data = ('''
Nama rumah rakit = {}
Kode rumah sakit = {}
Alamat = {}
Wilayah = {}
No. Telepon = {}
'''.format(nam, koders, almt, wlyh, tlpn))
      if Wilayah.upper() in wlyh.upper():
         bot.reply_to(message, data)
      else:
         pass

    # menu angka penyebaran covid setiap provinsi
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



