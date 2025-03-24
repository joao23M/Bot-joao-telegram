from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Token do seu bot (substitua pelo seu token)
TOKEN = "7394421070:AAEr@woahdNdkMA4McSWb66VehgP4avmNDI"

# Função para responder ao comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Eu sou seu bot do Telegram. Como posso ajudar?')

# Função para responder a mensagens de texto
def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    update.message.reply_text(f'Você disse: {user_message}')

def main():
    # Inicializa o Updater com o token do bot
    updater = Updater(TOKEN)

    # Obtém o dispatcher para registrar os handlers
    dispatcher = updater.dispatcher

    # Registra o comando /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Registra um handler para mensagens de texto
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Inicia o bot
    updater.start_polling()

    # Mantém o bot em execução até que você pressione Ctrl+C
    updater.idle()

if __name__ == "__main__":
    main()
