import telebot

# Substitua pelo seu Token do bot
TOKEN = "7394421070:AAErGwoahdNdkMA4McSWbG6VehgP4avmNDI"
bot = telebot.TeleBot(TOKEN)

# Comandos do bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bem-vindo ao JOAZINHO STORE! Como posso te ajudar?")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Aqui estão os comandos disponíveis:\n/start - Iniciar o bot\n/help - Ajuda")

# Comando de venda
@bot.message_handler(commands=['comprar'])
def comprar_produto(message):
    bot.reply_to(message, "Você deseja comprar um produto. Escolha a opção abaixo:")

# Comando de saldo
@bot.message_handler(commands=['saldo'])
def verificar_saldo(message):
    bot.reply_to(message, "Seu saldo está em R$0,00. Faça um pagamento para continuar.")

# Comando de Pix (Exemplo simples)
@bot.message_handler(commands=['pix'])
def pix(message):
    bot.reply_to(message, "Para realizar um pagamento via Pix, use a chave: 62484d81-b9de-4b27-9fff-0c32f6e4c916")

# Outros comandos e funcionalidades podem ser adicionados aqui

# Starta o bot
bot.polling(none_stop=True)
