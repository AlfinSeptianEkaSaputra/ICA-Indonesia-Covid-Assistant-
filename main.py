from telegram.ext import *
import api as keys
import balasan as R
import fitur as F
import JaringanAI as AI

print("Bot Berjalan")

def handle_message(update, context):
    text = str(update.message.text).lower()
    namauser = update.message.chat.first_name

    print(f"{namauser} : Mengirimkan pesan > {text} <")

    response = R.sample_responses(text, namauser)

    update.message.reply_text(response)


def error(update, context):
    print(f"update {update} menyebabkan error {context.error}")

QUERY = range(1)
def carijudulhoax(update, context):
    update.message.reply_text("Masukkan berita yang menurut anda kurang meyakinkan.")
    return QUERY

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", F.start_command))
    dp.add_handler(CommandHandler("help", F.help_command))
    dp.add_handler(CommandHandler("berita", F.google))
    dp.add_handler(CommandHandler("indonesia", F.indonesia))
    dp.add_handler(CommandHandler("cuaca", F.cuaca))


    obrolancarijudulhoax = ConversationHandler(
        entry_points=[CommandHandler('deteksiberita', carijudulhoax)],
        states={QUERY: [MessageHandler(Filters.text, F.hasilcarijudulhoax)]},
        fallbacks=[]
    )
    dp.add_handler(obrolancarijudulhoax)

    dp.add_handler(CommandHandler("adminlatihbot", AI.train))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
