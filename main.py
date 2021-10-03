import api
import api as keys
from telegram.ext import *
import balasan as R
import fitur as F

print("Bot Berjalan")

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

    dp.add_handler(CommandHandler("start", F.start_command))
    dp.add_handler(CommandHandler("help", F.help_command))
    dp.add_handler(CommandHandler("google", F.google))
    dp.add_handler(CommandHandler("covid", F.covid))
    dp.add_handler(CommandHandler("Indonesia", F.indonesiaCovid))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
