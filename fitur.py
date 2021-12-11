from googlesearch import search
import requests
import datetime
import json
import pandas as pd
from telegram.ext import *

# ================ Import Data ============================

page = requests.get('https://data.covid19.go.id/public/api/update.json').json()
dataCovid = page['update']['penambahan']

# ================ Eksekusi Perintah ==========================

def start_command(update, context):
    namauser = update.message.chat.first_name
    update.message.reply_text(
        f'''Halo {namauser} !!\n\n'''
        "Aku adalah ICA(Indonesian Covid Asistant). Aku akan membantu kamu mencari informasi tentang Covid 19.\n\n"
        "Kamu bisa langsung mulai chat ke aku 🤗. Apa aja bisa kok, mulai dari kasus terbaru, berita seputar covid, atau cuma mau ngobrol juga gapapa kok\n\n"
        "Lihat di /help untuk ngeliat semua fitur yang aku miliki 👍")


def help_command(update, context):
    update.message.reply_text("Saya akan membantu anda mencari informasi seputar Covid-19\n\n"
                              "Perintahkan saya  dengan klik atau masukkan command dibawah\n\n"
                              "Info Covid\n"
                              "/kasusbaru => _Kasus covid-19 di Indonesia_ 🇮🇩\n"
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

def kasusbaru(update, context):
    tambahKasus = dataCovid['jumlah_positif']
    tambahMeninggal = dataCovid['jumlah_meninggal']
    tambahSembuh = dataCovid['jumlah_sembuh']
    tanggalUpdate = dataCovid['created']

    kirim = (
        "_Perkembangan Kasus Covid-19 di Indonesia saat ini: _\n\n"
        f"Kasus terbaru = *{tambahKasus}*\n"
        f"Sembuh = *{tambahSembuh}*\n"
        f"Meninggal = *{tambahMeninggal}*\n\n"
        "#====================#\n\n"
        f"Di update per : *{tanggalUpdate}*")

    update.message.reply_text(kirim, parse_mode="Markdown")
    update.message.reply_text(
        "Untuk informasi Covid19 setiap provinsi di Indonesia, kamu bisa mengakses link berikut ini:\n\nhttps://drive.google.com/file/d/1vs502pTin6eAHQmMesa9MKNJ_rZQZk6K/view?usp=sharing\n(Catatan: Jika kamu menginginkan Data terupdate, kamu bisa membuka Microsoft Excel kemudian klik tombol REFRESH)")

    update.message.reply_text("Mari kita bersama tetap menjaga protokol kesehatan demi melawan pandemi ini 😷😷")
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

