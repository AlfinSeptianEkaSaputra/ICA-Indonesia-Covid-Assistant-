from googlesearch import search
import requests

def start_command(update, context):
   namauser = update.message.chat.first_name
   update.message.reply_text(
      f'''Halo {namauser}\n\n'''
      "Saya adalah ICA(Indonesian Covid Asistant). Saya bisa membantu anda mencari informasi tentang Covid 19.\n\n"
      "Anda bisa mulai dengan mengirim\n/help untuk melihat segala fitur yang saya miliki")

def help_command(update, context):
   update.message.reply_text("Saya akan membantu anda mencari informasi seputar Covid-19\n\n"
                             "Perintahkan saya  dengan klik atau masukkan command dibawah\n\n"
                             "Info Covid\n"
                             "/covid >provinsi< - Jumlah kasus covid di provinsi tersebut\n"
                             ">>fitur<<\n"
                             ">>fitur<<\n"
                             ">>fitur<<\n"
                             ">>fitur<<\n\n"
                             "Anda bisa juga konsultasi gejala covid, saya akan membantu anda\n\n"
                             "Kami juga.... >>tambahkan<<\n"
                             ">>fitur<<\n"
                             ">>fitur<<\n"
                             ">>fitur<<\n\n"
                             "Atau hanya anda ingin mengobrol? Tidak apa-apa. Saya akan menemani anda :)")
   
def google(update, context):
   text = str(update.message.text).lower()
   hasilpencarian = search(text, num_results=1)
   update.message.reply_text(hasilpencarian)

def covid(update, context):
   provinsi = update.message.text
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
