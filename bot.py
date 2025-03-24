from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bem-vindo ao JOAZINHO STORE!')

def main() -> None:
    # Token do seu bot (substitua pelo token correto)
    updater = Updater("7394421070:AAErGwoahd-NdkMA4McSWbG6Vegh-P4avmNDI")

    dispatcher = updater.dispatcher

    # Adiciona o comando /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
