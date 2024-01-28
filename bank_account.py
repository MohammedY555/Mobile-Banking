from connect_db import conn, cursor_acc, read_bank_accounts


class BankAccounts:
    def __init__(self, user_id, account_number, balance=10000, status=True):
        self.__user_id = user_id
        self.__account_number = account_number
        self.__status = status
        self.__balance = balance

    def get_status(self):
        return self.__status

    def set_status(self, active=True):
        self.__status = active

    def set_balance_withdraw(self, withdraw_balance):
        self.__balance -= withdraw_balance

    def set_balance_top_up(self, top_up_balance):
        self.__balance += top_up_balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_user_id(self):
        return self.__user_id

    def print_account(self):
        print(f"Номер банковского счёта: {self.__account_number}, баланс по счёту: {self.__balance}")


cursor_acc

read_bank_accounts

rows_acc = cursor_acc.fetchall()

accounts = [BankAccounts(row[0], row[1], row[2]) for row in rows_acc]

print(rows_acc)

# accounts = [
#     BankAccounts(1, "20216972123456789012", 10000, True),
#     BankAccounts(2, "20216972123456767813", 10000, True),
#     BankAccounts(3, "20216972123456756714", 10000, True),
#     BankAccounts(4, "20216972123456783415", 10000, True),
#     BankAccounts(5, "20216972123456789136", 10000, True),
# ]


# conn = psycopg2.connect(
#     dbname="bank_service",
#     user="postgres",
#     password="Mother1505",
#     host="localhost",
#     port="5432")
# print("Подключение установлено")
#
# cursor = conn.cursor()
# for user in users_list:
#     print(f"User ID: {user.get_user_id()}, Username: {user.get_username()}, Password: {user.get_password()}")

# cursor.scroll(0, mode='absolute')
#
