from googlesearch import search
import requests
import datetime
import json
import pandas as pd
from telegram.ext import *

# =====================================
data = pd.read_csv('data.csv')

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
                              "/berita => _Berita Seputar Covid19_ 📺\n"
                              "/deteksiberita => _Mendeteksi berita seputar covid, apakah hoax atau tidak_ 📺\n"
                              "/cuaca => _Prediksi cuaca di Indonesia maupun di Dunia_ ☁️\n\n"
                              "Anda bisa juga konsultasi gejala covid, saya akan membantu anda"
                              "Atau anda hanya ingin mengobrol? Tidak apa-apa. Saya akan menemani anda :)",
                              parse_mode="MARKDOWN")

def google(update, context):
    data = update.message.text

    if (data == "/berita"):
        update.message.reply_text(
            "Cari berita dengan mengetikkan: \n_/berita_ *ketik informsi apa yang ingin anda cari*.\nMisalkan _/berita_ situasi indonesia saat ini.",
            parse_mode="Markdown")
    else:
        x = search(data, num_results=2)
        for i in x:
            update.message.reply_text(i)

    update.message.reply_text("Ketik /help untuk kembali ke *MENU FITUR*.", parse_mode="MARKDOWN")


def indonesia(update, context):
    waktu = datetime.datetime.now()
    date = waktu.strftime('%x')
    day = waktu.strftime('%A')

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
                .format(negara, positif, sembuh, meninggal, dirawat, date, day))
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

    if (input == "/cuaca"):
        update.message.reply_text(
            "Tolong tambahkan nama provinsi/kota/daerah. 🏙️🏙️\nMisalkan _/cuaca kediri_.\nAtaupun _/cuaca jawa timur_.\nAtaupun _/cuaca Indonesia_.",
            parse_mode="Markdown")
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
                   '☀️🌤️⛅🌥️☁️🌦️🌧️⛈️🌩️🌨️\n'
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
                   .format(kota, kota, long, lat, temp, max_temp, min_temp, wind_speed, pressure, humidity, date, day))
            update.message.reply_text(msg, parse_mode="Markdown")
        else:
            pass

    update.message.reply_text("Ketik /help untuk kembali ke *MENU FITUR*.", parse_mode="MARKDOWN")

def hasilcarijudulhoax(update, context):
    pesan = update.message.text.strip().lower()

    datum = data[data['judul'].str.lower().str.contains(pesan)].copy()
    text = 'Berikut adalah artikel yang saya temukan' + '\n\n'
    for row in datum.itertuples():

        text += '[' + str(row.tanggal) + ']' + '\n' + row.judul + '\n' + row.link + '\n\n'
        if len(text) > 3500:
            print(pesan, len(text))
            update.message.reply_text(text)
            text = ''

    print(pesan, len(text))
    update.message.reply_text(text)

    update.message.reply_text(
        "Jika tidak terdapat artikel kemungkinan berita yang anda cari bukanlah *HOAX*", parse_mode="MARKDOWN")
    update.message.reply_text(
        "Ketik /help untuk kembali ke *MENU FITUR*, atau Ketik /deteksiberita untuk kembali mencari berita yang menurut anda kurang meyakinkan.",
        parse_mode="MARKDOWN")

    return ConversationHandler.END
