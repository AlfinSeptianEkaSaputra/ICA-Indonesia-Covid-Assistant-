from googlesearch import search
import requests
import datetime
import json
import pandas as pd
import calendar
from telegram.ext import *
from telegram import *
# =====================================
data = pd.read_csv('data.csv')
data.tanggal = pd.to_datetime(data.tanggal, dayfirst=True)
data.tanggal = data.tanggal.dt.date
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

print('Block 1, function to show calendar, get from github')
def create_callback_data(action, year, month, day):
    """ Create the callback data associated to each button"""
    return ";".join([action, str(year), str(month), str(day)])


def separate_callback_data(data):
    """ Separate the callback data"""
    return data.split(";")


def create_calendar(year=None, month=None):
    """
    Create an inline keyboard with the provided year and month
    :param int year: Year to use in the calendar, if None the current year is used.
    :param int month: Month to use in the calendar, if None the current month is used.
    :return: Returns the InlineKeyboardMarkup object with the calendar.
    """
    now = datetime.datetime.now()
    if year == None: year = now.year
    if month == None: month = now.month
    data_ignore = create_callback_data("IGNORE", year, month, 0)
    keyboard = []
    # First row - Month and Year
    row = []
    row.append(InlineKeyboardButton(calendar.month_name[month] + " " + str(year), callback_data=data_ignore))
    keyboard.append(row)
    # Second row - Week Days
    row = []
    for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]:
        row.append(InlineKeyboardButton(day, callback_data=data_ignore))
    keyboard.append(row)

    my_calendar = calendar.monthcalendar(year, month)
    for week in my_calendar:
        row = []
        for day in week:
            if(day == 0):
                row.append(InlineKeyboardButton(" ", callback_data=data_ignore))
            else:
                row.append(InlineKeyboardButton(str(day), callback_data=create_callback_data("DAY", year, month, day)))
        keyboard.append(row)
    # Last row - Buttons
    row = []
    row.append(InlineKeyboardButton("<", callback_data=create_callback_data("PREV-MONTH", year, month, day)))
    row.append(InlineKeyboardButton(" ", callback_data=data_ignore))
    row.append(InlineKeyboardButton(">", callback_data=create_callback_data("NEXT-MONTH", year, month, day)))
    keyboard.append(row)

    return InlineKeyboardMarkup(keyboard)


def process_calendar_selection(bot, update):
    """
    Process the callback_query. This method generates a new calendar if forward or
    backward is pressed. This method should be called inside a CallbackQueryHandler.
    :param telegram.Bot bot: The bot, as provided by the CallbackQueryHandler
    :param telegram.Update update: The update, as provided by the CallbackQueryHandler
    :return: Returns a tuple (Boolean,datetime.datetime), indicating if a date is selected
                and returning the date if so.
    """
    ret_data = (False, None)
    query = update.callback_query
    (action, year, month, day) = separate_callback_data(query.data)
    curr = datetime.datetime(int(year), int(month), 1)
    if action == "IGNORE":
        bot.answer_callback_query(callback_query_id=query.id)
    elif action == "DAY":
        bot.edit_message_text(text=query.message.text,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id
                              )
        ret_data = True, datetime.datetime(int(year), int(month), int(day))
    elif action == "PREV-MONTH":
        pre = curr - datetime.timedelta(days=1)
        bot.edit_message_text(text=query.message.text,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=create_calendar(int(pre.year), int(pre.month)))
    elif action == "NEXT-MONTH":
        ne = curr + datetime.timedelta(days=31)
        bot.edit_message_text(text=query.message.text,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=create_calendar(int(ne.year), int(ne.month)))
    else:
        bot.answer_callback_query(callback_query_id=query.id, text="Something went wrong!")
        # UNKNOWN
    return ret_data

def caritanggalhoax(update, context):
    update.message.reply_text("Please select a date: ",
                              reply_markup=create_calendar())


def hasilcaritanggalhoax(bot, update):
    selected, date = process_calendar_selection(bot, update)
    if selected:
        datum = data[data.tanggal == date.date()]
        if datum.empty:
            text = 'Tidak terdapat artikel hoax yang terbit pada tanggal ' + date.strftime('%d-%m-%Y')
        else:
            text = 'Berikut adalah artikel hoax yang terbit pada tanggal ' + date.strftime('%d-%m-%Y') + '\n\n'
            for row in datum.itertuples():
                text += '[' + str(row.tanggal) + ']' + '\n' + row.judul + '\n' + row.link + '\n\n'
        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=text,
                         reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
