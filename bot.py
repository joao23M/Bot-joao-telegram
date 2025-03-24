import telebot
import sqlite3
from telebot import types
from time import sleep
import random
import string

# Token do bot (substitua com o seu token)
TOKEN = '7394421070:AAErGwoahdNdkMA4McSWbG6VehgP4avmNDI'

bot = telebot.TeleBot(TOKEN)

# Banco de dados (SQLite)
conn = sqlite3.connect('joazinho_store.db', check_same_thread=False)
cursor = conn.cursor()

# Criação das tabelas se não existirem
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    saldo REAL,
                    compras INTEGER
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    preco REAL
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    produto_id INTEGER,
                    data TEXT,
                    status TEXT
                 )''')

conn.commit()

# Função para obter o saldo do usuário
def get_user_balance(user_id):
    cursor.execute("SELECT saldo FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0

# Função para criar um novo usuário
def create_user(user_id, username):
    cursor.execute("INSERT INTO users (id, username, saldo, compras) VALUES (?, ?, ?, ?)", 
                   (user_id, username, 0, 0))
    conn.commit()

# Função para registrar uma venda
def register_sale(user_id, produto_id):
    cursor.execute("INSERT INTO vendas (user_id, produto_id, data, status) VALUES (?, ?, datetime('now'), ?)", 
                   (user_id, produto_id, "Aguardando pagamento"))
    conn.commit()

# Função para adicionar saldo ao usuário
def add_balance(user_id, amount):
    cursor.execute("UPDATE users SET saldo = saldo + ? WHERE id = ?", (amount, user_id))
    conn.commit()

# Função para listar produtos
def list_products():
    cursor.execute("SELECT * FROM produtos")
    return cursor.fetchall()

# Definir o menu principal
def create_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Ver produtos', 'Meu saldo', 'Histórico de compras', 'Apoio ao cliente')
    return markup

# Início do bot
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    if not cursor.fetchone():
        create_user(user_id, username)

    bot.send_message(user_id, "Bem-vindo à JOAZINHO STORE! Escolha uma opção:", reply_markup=create_main_menu())

# Exibir produtos
@bot.message_handler(func=lambda message: message.text == 'Ver produtos')
def show_products(message):
    user_id = message.from_user.id
    products = list_products()
    
    if not products:
        bot.send_message(user_id, "Nenhum produto disponível no momento.")
        return

    text = "Produtos disponíveis para venda:\n"
    for product in products:
        text += f"{product[1]} - R${product[2]:.2f}\n"

    bot.send_message(user_id, text, reply_markup=create_main_menu())

# Exibir saldo
@bot.message_handler(func=lambda message: message.text == 'Meu saldo')
def show_balance(message):
    user_id = message.from_user.id
    balance = get_user_balance(user_id)
    bot.send_message(user_id, f"Seu saldo é R${balance:.2f}", reply_markup=create_main_menu())

# Comando para adicionar saldo via Pix
@bot.message_handler(func=lambda message: message.text == 'Apoio ao cliente')
def support(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Você pode adicionar saldo usando o Pix. Envie o valor que deseja adicionar.")

# Função para adicionar saldo via Pix manual
@bot.message_handler(func=lambda message: message.text.startswith('R$'))
def add_balance_via_pix(message):
    user_id = message.from_user.id
    try:
        amount = float(message.text[2:].replace(',', '.'))
        if amount > 0:
            add_balance(user_id, amount)
            bot.send_message(user_id, f"Saldo de R${amount:.2f} adicionado com sucesso!")
        else:
            bot.send_message(user_id, "Valor inválido.")
    except ValueError:
        bot.send_message(user_id, "Valor inválido. Tente novamente.")

# Comando para histórico de compras
@bot.message_handler(func=lambda message: message.text == 'Histórico de compras')
def purchase_history(message):
    user_id = message.from_user.id
    cursor.execute("SELECT p.nome, v.data, v.status FROM vendas v JOIN produtos p ON v.produto_id = p.id WHERE v.user_id = ?", (user_id,))
    purchases = cursor.fetchall()

    if not purchases:
        bot.send_message(user_id, "Você ainda não fez compras.")
        return

    text = "Seu histórico de compras:\n"
    for purchase in purchases:
        text += f"Produto: {purchase[0]}, Data: {purchase[1]}, Status: {purchase[2]}\n"

    bot.send_message(user_id, text, reply_markup=create_main_menu())

# Comando para registrar uma venda (simulação de pagamento)
@bot.message_handler(func=lambda message: message.text.startswith('Comprar'))
def buy_product(message):
    user_id = message.from_user.id
    try:
        product_id = int(message.text.split()[1])  # Supondo que a mensagem seja "Comprar 1"
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        
        if product:
            register_sale(user_id, product_id)
            bot.send_message(user_id, f"Você comprou {product[1]}! Aguardando pagamento.", reply_markup=create_main_menu())
        else:
            bot.send_message(user_id, "Produto não encontrado.")
    except ValueError:
        bot.send_message(user_id, "Seleção de produto inválida. Tente novamente.")

# Inicializar bot
bot.polling(none_stop=True)
