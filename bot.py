from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bem-vindo ao JOAZINHO STORE!')

def main() -> None:
    updater = Updater("7954905234:AAGibTxa20RT_rv2kl_fC4Yk9yq8kadgW4o")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
