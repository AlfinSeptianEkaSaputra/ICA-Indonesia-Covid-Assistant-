from googlesearch import search
import requests

def start_command(update, context):
   namauser = update.message.chat.first_name
   update.message.reply_text(
      f'''Halo {namauser}\n\nSaya adalah ICA(Indonesian Covid Asistant) !\nSaya bisa membantu anda mencari informasi tentang Covid 19.\n\nAnda bisa mulai dengan mengirim\n/help untuk melihat segala fitur yang saya miliki''')

def help_command(update, context):
   update.message.reply_text('Butuh bantuan? maaf, bot belum dikembangkan sejauh itu')

def google(update, context):
   text = str(update.message.text).lower()
   hasilpencarian = search(text, num_results=1)
   update.message.reply_text(hasilpencarian)

def covid(update, context):
   text = str(update.message.text).lower()
   provinsi = text
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

      update.message.reply_text(data)
