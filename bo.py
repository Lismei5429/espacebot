from telegram.ext import Updater, CommandHandler

TOKEN = '7771234555:AAHiQY8MtKVxu30VuQdxbNwmyna6E1UnET8'

def start(update, context):
    update.message.reply_text("👋 ¡Bienvenido a Metaplus Bot!\n\nGracias por iniciar. Pronto podrás acceder a tus recompensas.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
