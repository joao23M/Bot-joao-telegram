# JOAZINHO STORE - Bot de Vendas de Contas Premium

## Requisitos

- Python 3.x
- Bibliotecas: `pyTelegramBotAPI`, `psycopg2`
- Banco de dados: PostgreSQL (ou SQLite)

## Como rodar o bot

1. Faça o deploy no Railway (ou outro serviço de hospedagem).
2. Defina as variáveis de ambiente:
   - `DB_HOST` (host do seu banco de dados)
   - `DB_NAME` (nome do seu banco de dados)
   - `DB_USER` (usuário do banco)
   - `DB_PASSWORD` (senha do banco)
   - `TELEGRAM_TOKEN` (seu token do Telegram)
3. Execute o bot com o comando:
   ```bash
   python bot.py
   ```

## Notas

- Se for usar SQLite, altere a configuração do banco no `bot.py`.
