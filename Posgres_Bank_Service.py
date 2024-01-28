import psycopg2
import pandas as pd
from psycopg2._psycopg import cursor

conn = psycopg2.connect(
    dbname="bank_service",
    user="postgres",
    password="Mother1505",
    host="localhost",
    port="5432")
print("Подключение установлено")

# create_users

# cursor = conn.cursor()
#
# query_create = '''CREATE TABLE users(
#                             id SERIAL PRIMARY KEY NOT NULL,
#                             username VARCHAR(50),
#                             password VARCHAR(255)
#                         );'''
#
# psgres = cursor.execute(query_create)
#
# saved = conn.commit()


# ALTER TABLE
# cursor = conn.cursor()
#
# query_create = '''CREATE TABLE users(
#                             id SERIAL PRIMARY KEY NOT NULL,
#                             username VARCHAR(50),
#                             password VARCHAR(255)
#                         );'''
#
# psgres = cursor.execute(query_create)
#
# saved = conn.commit()


# insert_users

# cursor = conn.cursor()
#
# query_insert = '''INSERT INTO users (id, username, password) VALUES
#   (1, 'Username1', 'pass1'),
#   (2, 'Username2', 'pass2'),
#   (3, 'Username3', 'pass3'),
#   (4, 'Username4', 'pass4'),
#   (5, 'Username5', 'pass5'),
#   (6, 'Username6', 'pass6'),
#   (7, 'Username7', 'pass7'),
#   (8, 'Username8', 'pass8'),
#   (9, 'Username9', 'pass9'),
#   (10, 'Username10', 'pass10');'''
#
# psgres = cursor.execute(query_insert)
#
# conn.commit()


# селект запрос (проверка добавление информации)
# cursor = conn.cursor()
#
# query_select_1 = '''select id, username, password from users'''
#
# psgres = cursor.execute(query_select_1)
#
# df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
#
# print(df)


# ======================================================================================================================


# create_bank_accounts

# cursor = conn.cursor()
#
# query_create_bank_accounts = '''CREATE TABLE bank_accounts (
#                                 id SERIAL PRIMARY KEY NOT NULL,
#                                 accounts VARCHAR(20),
#                                 amount DECIMAL(20,2),
#                                 status BOOLEAN DEFAULT TRUE
#                             );'''
#
# psgres = cursor.execute(query_create_bank_accounts)
#
# saved = conn.commit()


# insert_bank_accounts

# cursor = conn.cursor()
#
# query_insert = '''INSERT INTO bank_accounts (user_id, accounts, amount) VALUES
# ('2021-001', 1000.00),
# ('2021-002', 2500.50),
# ('2021-003', 500.75),
# ('2021-004', 1200.00),
# ('2021-005', 800.25),
# ('2021-006', 3000.50),
# ('2021-007', 1500.75),
# ('2021-008', 200.00),
# ('2021-009', 400.25),
# ('2021-010', 1800.50),
# ('2021-011', 900.75),
# ('2021-012', 3500.00),
# ('2021-013', 2200.50),
# ('2021-014', 750.75),
# ('2021-015', 3200.00),
# ('2021-016', 1800.25),
# ('2021-017', 100.50),
# ('2021-018', 2400.25),
# ('2021-019', 300.50),
# ('2021-020', 1200.75);'''
#
# psgres = cursor.execute(query_insert)
#
# conn.commit()


# селект запрос (проверка добавление информации)
# cursor = conn.cursor()
#
# query_select_1 = '''select * from bank_accounts'''
#
# psgres = cursor.execute(query_select_1)
#
# df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
#
# print(df)

# ======================================================================================================================
