import api as keys
from telegram.ext import *
import balasan as R
import fitur as F

#print("Bot Berjalan")
def start_command(update, context):
    namauser = update.message.chat.first_name
    update.message.reply_text(f'''Halo {namauser}\n\nSaya adalah ICA(Indonesian Covid Asistant) !\nSaya bisa membantu anda mencari informasi tentang Covid 19.\n\nAnda bisa mulai dengan mengirim\n/help untuk melihat segala fitur yang saya miliki''')
def help_command(update, context):
    update.message.reply_text('Butuh bantuan? maaf, bot belum dikembangkan sejauh itu')

def handle_message(update, context):
    text = str(update.message.text).lower()
    namauser = update.message.chat.first_name

    print(f"{namauser} : Mengirimkan pesan > {text} <")

    response = R.sample_responses(text, namauser)

    update.message.reply_text(response)

def error(update, context):
    print(f"update {update} menyebabkan error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("google", google))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
