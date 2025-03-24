from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7394421070:AAErGwoahdNdkMA4McSWbG6VehgP4avmNDI"

# Função para o comando /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(
        f"👋 **Olá, {user.first_name}! Bem-vindo(a) à JoaoStore.**\n\n"
        "Aqui você encontra os melhores serviços de streamings, contas premium e muito mais!\n\n"
        "📋 **Comandos disponíveis:**\n"
        "/start - Iniciar o bot\n"
        "/pix - Recarregar saldo\n"
        "/historico - Ver suas compras\n"
        "/saldo - Ver seu saldo atual\n"
        "/termos - Ler os termos de uso\n"
        "/suporte - Falar com o suporte\n"
        "/ranking - Ver ranking de usuários\n"
        "/afiliados - Ganhe saldo indicando o bot\n"
        "/alertas - Receber avisos de abastecimentos"
    )

# Função para o comando /pix
def pix(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📲 **Recarregar Saldo via PIX**\n\n"
        "Envie o valor que deseja recarregar para esta chave PIX:\n\n"
        "Chave PIX: 62484d81-b9de-4b27-9fff-0c32f6e4c916\n\n"
        "Após o pagamento, envie o comprovante para @suporte_joaostore.\n\n"
        "⚠️ **Atenção:** O valor mínimo para recarga é R$10,00."
    )

# Função para o comando /saldo
def saldo(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"💰 **Seu saldo atual é: R$0,00**\n\nID: {user.id}")

# Função para o comando /termos
def termos(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📜 **Termos de Uso da JoaoStore**\n\n"
        "Ao utilizar os serviços da JoaoStore, você concorda com os seguintes termos:\n\n"
        "1. Todos os serviços são fornecidos com garantia de 30 dias.\n"
        "2. O valor mínimo para recarga via PIX é R$10,00.\n"
        "3. Em caso de problemas, entre em contato com o suporte.\n\n"
        "Leia os termos completos em: [link dos termos]"
    )

# Função para o comando /suporte
def suporte(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🛠 **Suporte JoaoStore**\n\n"
        "Para falar com o suporte, envie uma mensagem para @suporte_joaostore.\n\n"
        "Estamos aqui para ajudar! 😊"
    )

# Função para o comando /historico
def historico(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📚 **Histórico de Compras**\n\n"
        "Aqui estão suas compras recentes:\n\n"
        "1. Netflix Padrão - R$8,50\n"
        "2. IPTV +30000 Conteúdos - R$18,00\n"
        "3. Spotify Premium - R$5,00\n"
        "4. Disney+ - R$10,00\n"
        "5. HBO Max - R$12,00\n\n"
        "Para mais detalhes, entre em contato com o suporte."
    )

# Função para o comando /ranking
def ranking(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🏆 **Ranking de Usuários**\n\n"
        "1. @usuario1 - R$150,00\n"
        "2. @usuario2 - R$120,00\n"
        "3. @usuario3 - R$100,00\n\n"
        "Participe e suba no ranking!"
    )

# Função para o comando /afiliados
def afiliados(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🤝 **Programa de Afiliados**\n\n"
        "Indique o JoaoStore para seus amigos e ganhe saldo!\n\n"
        "Compartilhe seu link de afiliado:\n"
        "https://t.me/joaostore_bot?start=afiliado123\n\n"
        "Para cada compra feita através do seu link, você ganha 10% de comissão!"
    )

# Função para o comando /alertas
def alertas(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🔔 **Alertas de Abastecimentos**\n\n"
        "Você será notificado sobre novos abastecimentos de serviços.\n\n"
        "Ative as notificações para não perder nada!"
    )

# Função principal
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Adiciona os handlers para cada comando
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("pix", pix))
    dispatcher.add_handler(CommandHandler("saldo", saldo))
    dispatcher.add_handler(CommandHandler("termos", termos))
    dispatcher.add_handler(CommandHandler("suporte", suporte))
    dispatcher.add_handler(CommandHandler("historico", historico))
    dispatcher.add_handler(CommandHandler("ranking", ranking))
    dispatcher.add_handler(CommandHandler("afiliados", afiliados))
    dispatcher.add_handler(CommandHandler("alertas", alertas))

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
