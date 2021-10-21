from googlesearch import search
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import datetime
import json

# ===============#DATA================
my_states = ['Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Jambi', 'Sumatera Selatan', 'Bengkulu',
             'Bangka Belitung', 'Lampung', 'Kepulauan Riau', 'DKI Jakarta', 'Jawa Barat', 'Jawa Tengah',
             'Daerah Istimewa Yogyakarta', 'Jawa Timur', 'Banten', 'Bali',
             'Nusa Tenggara Barat', 'Nusa Tenggara Timur', 'Kalimantan Barat', 'Kalimantan Tengah',
             'Kalimantan Selatan', 'Kalimantan Timur', 'Kalimantan Utara', 'Sulawesi Utara', 'Sulawesi Tengah',
             'Sulawesi Selatan', 'Sulawesi Tenggara', 'Gorontalo', 'Sulawesi Barat', 'Maluku', 'Maluku Utara', 'Papua',
             'Papua Barat']

link1 = 'https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=Provinsi,Kasus_Posi,Kasus_Semb,Kasus_Meni&outSR=4326&f=json'
res = requests.get(link1).json()

regional_data = res['features']
total_states = int(len(regional_data))
# =====================================

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
                              "/indonesia => _Kasus covid-19 di Indonesia_ 🇮🇩\n"
                              "/covidprov => _Kasus COVID Per Provinsi di Indonesia_ 🦠\n"
                              "/berita => _Berita Seputar Covid19_ 📺\n"
                              "/rumahsakit => _Rumah Sakit Rujukan Nasional_ 🏥\n"
                              "/cuaca => _Prediksi cuaca di Indonesia maupun di Dunia_\n\n"
                              "Anda bisa juga konsultasi gejala covid, saya akan membantu anda"
                              "Atau anda hanya ingin mengobrol? Tidak apa-apa. Saya akan menemani anda :)", parse_mode="MARKDOWN")


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
        "_Pilih salah satu provinsi di bawah ini : _\n", reply_markup=reply_markup, parse_mode="Markdown")
    update.message.reply_text("Ketik /help untuk kembali ke *MENU FITUR*.", parse_mode="MARKDOWN")


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
    if (texts == "/rumahsakit"):
        update.message.reply_text(
            "Tolong tambahkan wilayah atau alamat rumah sakit di daerah yang anda cari.🏥🏥\nMisalkan _/rumahsakit Kediri_.\nAtaupun _/rumahsakit  JL. VETERAN..._", parse_mode="Markdown")
    else:
        pesan = texts[12:]
        page = requests.get(
            'https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/RS_Rujukan_Update_May_2020/FeatureServer/0/query?where=1%3D1&outFields=nama,alamat,wilayah,kode_rs,telepon&outSR=4326&f=json')
        page_json = page.json()
        features = page_json['features']
        for i in features:
            nam = i['attributes']['nama']
            koders = i['attributes']['kode_rs']
            wlyh = i['attributes']['wilayah']
            almt = i['attributes']['alamat']
            tlpn = i['attributes']['telepon']
            data = (
                "_Berikut ini rumah sakit yang anda cari : _\n"
                "Nama Rumah Sakit : *{}*\n"
                "Kode Rumah Sakit : *{}*\n"
                "Wilayah : *{}*\n"
                "Alamat : *{}*\n"
                "Telepon : *{}*\n".format(nam, koders, wlyh, almt, tlpn))
            if pesan.upper() in wlyh.upper():
                update.message.reply_text(data, parse_mode="Markdown")
            elif pesan.upper() in almt.upper():
                update.message.reply_text(data, parse_mode="Markdown")
            else:
                pass
    update.message.reply_text("Ketik /help untuk kembali ke *MENU FITUR*.", parse_mode="MARKDOWN")


def google(update, context):
    data = update.message.text

    if (data == "/berita"):
        update.message.reply_text(
            "Cari berita dengan mengetikkan: \n_/berita_ *ketik informsi apa yang ingin anda cari*.\nMisalkan _/berita_ situasi indonesia saat ini.", parse_mode="Markdown")
    else:
        x = search(data, num_results=2)
        for i in x:
            update.message.reply_text(i)

    update.message.reply_text("Ketik /help untuk kembali ke *MENU FITUR*.", parse_mode="MARKDOWN")

def indonesia(update, context):
    waktu = datetime.datetime.now()
    date = waktu.strftime('%x')
    day = waktu.strftime('%A')
    time = waktu.strftime('%X')
    
    api = requests.get('https://api.kawalcorona.com/indonesia/')
    api_json = api.json()
    api_content = api_json
    for wan in api_content:
        negara = wan['name']
        positif = wan['positif']
        sembuh = wan['sembuh']
        meninggal = wan['meninggal']
        dirawat = wan['dirawat']
        kirim = (
            "_Perkembangan Kasus Covid-19 di Indonesia saat ini: _\n"
            "Negara = *{}*\n"
            "Positif = *{}*\n"
            "Sembuh = *{}*\n"
            "Meninggal = *{}*\n"
            "Dirawat = *{}*\n"
            '#====================#\n'
            '*Update*:\n'
            '_Date: {}_\n'
            '_Day: {}_\n'
            '_Time: {}_\n'
                .format(negara, positif, sembuh, meninggal, dirawat, date, day, time))
        update.message.reply_text(kirim, parse_mode="Markdown")
    update.message.reply_text(
        "Mari kita terus bersama-sama menangani pandemi ini, bergotong royong, bersatu padu karena hanya dengan cara kebersamaan ini kita akan dapat mengatasinya. Kita tidak sendiri, kita bersama dengan negara-negara lain yang juga mengalami hal yang sama untuk bersama mengatasi pandemi ini. Dan tetaplah bersabar, optimis, tetap disiplin berada di rumah, jaga jarak dalam berhubungan/berinteraksi dengan orang lain, hindari kerumunan, rajin cuci tangan, pakailah masker saat keluar rumah. Ketika kedisiplinan kuat itu kita lakukan, insyaallah kita akan kembali pada situasi dan kondisi normal dan dapat bertemu dengan saudara, bertemu dengan teman, bertemu dengan kerabat dan tetangga dalam situasi yang normal. Tapi untuk saat ini marilah kita tetap berada di rumah saja.\n\n"
        "Pesan Sumber: https://kemlu.go.id/portal/id/read/1608/pidato/pesan-kepada-masyarakat-indonesia-terkait-covid-19-10-april-2020")
    update.message.reply_text("Ketik /help untuk kembali ke *MENU FITUR*.", parse_mode="MARKDOWN")

def cuaca(update, context):

    input = update.message.text
    waktu = datetime.datetime.now()
    date = waktu.strftime('%x')
    day = waktu.strftime('%A')
    time = waktu.strftime('%X')
    
    if (input == "/cuaca"):
        update.message.reply_text(
            "Tolong tambahkan nama provinsi/kota/daerah. 🏙️🏙️\nMisalkan _/cuaca kediri_.\nAtaupun _/cuaca jawa timur_.\nAtaupun _/cuaca Indonesia_.", parse_mode="Markdown")
    else:
        api_url = 'https://api.openweathermap.org/data/2.5/weather?'
        pesan = input[7:]
        r = requests.post(url=api_url,
                          params={'q': pesan, 'APPID': 'ee97eadcd52acf153e995242e383b705', 'units': 'metric'})
        if r.status_code == 200:

            response = json.loads(r.content)
            temp = str(response['main']['temp'])
            max_temp = str(response['main']['temp_max'])
            min_temp = str(response['main']['temp_min'])
            wind_speed = str(response['wind']['speed'])
            pressure = str(response['main']['pressure'])
            humidity = str(response['main']['humidity'])
            kota = str(response['name'])
            lat = str(response['coord']['lat'])
            long = str(response['coord']['lon'])

            msg = ('_Prediksi cuaca saat ini di_ *{}*\n\n'
                   '🏙️🏙️🏙️🏙️🏙️🏙️🏙️🏙️\n'
                   '#====================#\n'
                   'Lokasi provinsi/kota/daerah *{}*\n'
                   'Longitude: *{}*\n'
                   'Latitude: *{}*\n'
                   '#====================#\n'
                   'Suhu: *{} °C*\n'
                   'Suhu maksimal: *{} °C*\n'
                   'Suhu minimal: *{} °C*\n'
                   'Kecepatan angin: *{} m/s*\n'
                   'Tekanan: *{} Pa*\n'
                   'Kelembapan: *{}%*\n'
                   '#====================#\n'
                   '*Update*:\n'
                   '_Date: {}_\n'
                   '_Day: {}_\n'
                   '_Time: {}_\n'
                   .format(kota, kota, long, lat, temp, max_temp, min_temp, wind_speed, pressure, humidity, date, day, time))
            update.message.reply_text(msg, parse_mode="Markdown")
        else:
            pass

    update.message.reply_text("Ketik /help untuk kembali ke *MENU FITUR*.", parse_mode="MARKDOWN")


