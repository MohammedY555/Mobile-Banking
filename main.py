from user import *
from bank_account import *
import service_bank_account
from user_service import *


def menu(user_id):
    while True:
        print('==========================================')

        print("Главное Меню")
        print("0. Exit")
        print("1. Добавление счёта")
        print("2. Получение списка счетов")
        print("3. Удаление счета")
        print("4. Снятие денег со счета")
        print("5. Перевод денежные средства на другой счет")

        print('==========================================')

        command = input("Пожалуйста, введите номер тип операции: ")
        if command == "0":
            break
        elif command == "1":
            service_account = service_bank_account.create_account(user_id)
            accounts.append(service_account)
        elif command == "2":
            user_accounts = get_account_user_id(accounts, user_id)
            service_bank_account.print_account_bulk(user_accounts)
        elif command == "3":
            acc_number = input("Введите номер счета: ")
            service_bank_account.delete_account(accounts, user_id, acc_number)
        elif command == "4":
            acc_number = input("Введите номер счета: ")
            amount = input("Сумма: ")
            amount = int(amount)
            service_bank_account.balance_withdraw(accounts, acc_number, amount)
        elif command == "5":
            first_account = input('Какому счету отправить: ')
            second_account = input('Снимать с какого счета: ')
            amount = int(input('Сумма трансфера: '))
            service_bank_account.transfers(accounts, first_account, second_account, amount)

        else:
            print("Такая комманда не существует. Пожалуйста введите правильную комманду!")


print("Добро пожаловать в сервис Онлайн-банкинг")
while True:
    print("Для проведение операции со своего аккаунта введите свой логин и пароль")
    username = input("login: ")
    password = input("Pass: ")

    found_user = find_user(users, username, password)
    if found_user is not None:
        print(f"Добро пожаловать, Чувак {found_user.get_username()}")
        menu(found_user.get_user_id())
    else:
        print("User not found.")
