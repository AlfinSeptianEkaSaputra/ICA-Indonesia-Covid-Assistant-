from telebot import *
from googlesearch import search
import api

bot = telebot.TeleBot(api.API_KEY)

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
      
@bot.message_handler(commands=['rumahsakit'])
def faskes(message):
   texts = message.text
   wilayah = texts[12:]
   page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/RS_Rujukan_Update_May_2020/FeatureServer/0/query?where=1%3D1&outFields=nama,kode_rs,alamat,wilayah,telepon&outSR=4326&f=json')
   page_json = page.json()
   features = page_json['features']
   for i in features:
      nama = i['attributes']['nama']
      koders =  i['attributes']['kode_rs']
      almt = i['attributes']['alamat']
      wlyh = i['attributes']['wilayah']
      tlpn = i['attributes']['telepon']
      data = ('''
Nama Rumah Sakit = {}
Kode Rumah Sakit = {}
Alamat = {}
Wilayah = {}
Telepon = {}
'''.format(nama, koders, almt, wlyh, tlpn))
      if wilayah.upper() in wlyh.upper():
         bot.reply_to(message, data)
      else:
         pass
bot.polling()
