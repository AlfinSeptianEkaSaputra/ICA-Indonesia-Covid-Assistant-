from googlesearch import search
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests

my_states = ['Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Jambi', 'Sumatera Selatan', 'Bengkulu', 'Bangka Belitung', 'Lampung', 'Kepulauan Riau', 'DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Daerah Istimewa Yogyakarta', 'Jawa Timur', 'Banten', 'Bali',
             'Nusa Tenggara Barat', 'Nusa Tenggara Timur', 'Kalimantan Barat', 'Kalimantan Tengah', 'Kalimantan Selatan', 'Kalimantan Timur', 'Kalimantan Utara', 'Sulawesi Utara', 'Sulawesi Tengah', 'Sulawesi Selatan', 'Sulawesi Tenggara', 'Gorontalo', 'Sulawesi Barat', 'Maluku', 'Maluku Utara', 'Papua', 'Papua Barat']

link1 = 'https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=Provinsi,Kasus_Posi,Kasus_Semb,Kasus_Meni&outSR=4326&f=json'
res = requests.get(link1).json()

regional_data = res['features']
total_states = int(len(regional_data))

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
                              "/covid => Jumlah kasus covid19 di berbagai provinsi yang ada di Indonesia\n"
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

def state_wise(update, context):
    keyboard = [[InlineKeyboardButton("Aceh", callback_data='Aceh'),
                 InlineKeyboardButton("Sumatera Utara", callback_data='Sumatera Utara')],

                [InlineKeyboardButton('Sumatera Barat', callback_data='Sumatera Barat'),
                 InlineKeyboardButton('Riau', callback_data='Riau')],

                [InlineKeyboardButton('Jambi', callback_data='Jambi'),
                 InlineKeyboardButton('Sumatera Selatan', callback_data='Sumatera Selatan')],

                [InlineKeyboardButton('Bengkulu', callback_data='Bengkulu'),
                 InlineKeyboardButton('Bangka Belitung', callback_data='Bangka Belitung')],

                [InlineKeyboardButton('Lampung', callback_data='Lampung'),
                 InlineKeyboardButton('Kepulauan Riau', callback_data='Kepulauan Riau')],

                [InlineKeyboardButton('DKI Jakarta', callback_data='DKI Jakarta'),
                 InlineKeyboardButton('Jawa Barat', callback_data='Jawa Barat')],

                [InlineKeyboardButton('Jawa Tengah', callback_data='Jawa Tengah'),
                 InlineKeyboardButton('Yogyakarta', callback_data='Daerah Istimewa Yogyakarta')],

                [InlineKeyboardButton('Jawa Timur', callback_data='Jawa Timur'),
                 InlineKeyboardButton('Banten', callback_data='Banten')],

                [InlineKeyboardButton('Bali', callback_data='Bali')],

                [InlineKeyboardButton('Nusa Tenggara Barat', callback_data='Nusa Tenggara Barat'),
                 InlineKeyboardButton('Nusa Tenggara Timur', callback_data='Nusa Tenggara Timur')],

                [InlineKeyboardButton('Kalimantan Barat', callback_data='Kalimantan Barat'),
                 InlineKeyboardButton('Kalimantan Tengah', callback_data='Kalimantan Tengah')],

                [InlineKeyboardButton('Kalimantan Selatan', callback_data='Kalimantan Selatan'),
                 InlineKeyboardButton('Kalimantan Timur', callback_data='Kalimantan Timur')],

                [InlineKeyboardButton('Kalimantan Utara', callback_data='Kalimantan Utara'),
                 InlineKeyboardButton('Sulawesi Utara', callback_data='Sulawesi Utara')],

                [InlineKeyboardButton('Sulawesi Tengah', callback_data='Sulawesi Tengah'),
                 InlineKeyboardButton('Sulawesi Selatan', callback_data='Sulawesi Selatan')],

                [InlineKeyboardButton('Sulawesi Tenggara', callback_data='Sulawesi Tenggara'),
                 InlineKeyboardButton('Gorontalo', callback_data='Gorontalo')],

                [InlineKeyboardButton('Sulawesi Barat', callback_data='Sulawesi Barat'),
                  InlineKeyboardButton('Maluku', callback_data='Maluku')],

                [InlineKeyboardButton('Maluku Utara', callback_data='Maluku Utara'),
                 InlineKeyboardButton('Papua', callback_data='Papua')],

                [InlineKeyboardButton('Papua Barat', callback_data='Papua Barat')]]


    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "_Pilih salah satu provinsi di bawah ini : _\n", reply_markup=reply_markup, parse_mode="MarkdownV2")

def tombol_(update, context):
    query = update.callback_query
    query.answer()
    if query.data in my_states:
        index = my_states.index(query.data)

        state_wise_data = f"Provinsi :  *{regional_data[index]['attributes']['Provinsi']}*\n\
Kasus Positif :  *{regional_data[index]['attributes']['Kasus_Posi']:,}*\n\
Kasus Sembuh :  *{regional_data[index]['attributes']['Kasus_Semb']:,}*\n\
Kasus Meninggal :  *{regional_data[index]['attributes']['Kasus_Meni']:,}*"

        last_data = f"{state_wise_data}"
        query.edit_message_text(last_data, parse_mode="Markdown")

def rumkit(update, context):
   texts = update.message.text
   pesan = texts[12:]
   page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/RS_Rujukan_Update_May_2020/FeatureServer/0/query?where=1%3D1&outFields=nama,alamat,wilayah,kode_rs,telepon&outSR=4326&f=json')
   page_json = page.json()
   features = page_json['features']
   for i in features:
      nam = i['attributes']['nama']
      koders =  i['attributes']['kode_rs']
      wlyh = i['attributes']['wilayah']
      almt = i['attributes']['alamat']
      tlpn = i['attributes']['telepon']
      data = ('''
Nama Rumah Sakit = {}
Kode Rumah Sakit = {}
Wilayah = {}
Alamat= {}
Telepon = {}
'''.format(nam, koders, wlyh, almt, tlpn))
      if pesan.upper() in wlyh.upper():
         update.message.reply_text(data)
      elif pesan.upper() in almt.upper():
         update.message.reply_text(data)
      else:
        pass

def google(update, context):
    text = str(update.message.text).lower()
    hasilpencarian = search(text, num_results=1)
    update.message.reply_text(hasilpencarian)
