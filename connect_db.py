import psycopg2


conn = psycopg2.connect(
    dbname="new_bank_service",
    user="postgres",
    password="Mother1505",
    host="localhost",
    port="5432")
print("Подключение установлено")

cursor_acc = conn.cursor()

query_bank_accounts = "SELECT user_id, accounts, amount FROM bank_accounts;"

read_bank_accounts = cursor_acc.execute(query_bank_accounts)

cursor_us = conn.cursor()

query_users = "SELECT * FROM users;"

read_users = cursor_us.execute(query_users)



