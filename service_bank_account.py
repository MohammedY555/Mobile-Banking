from bank_account import BankAccounts
from connect_db import conn

cursor_create = conn.cursor()


def create_account(user_id):
    account_number = input("Пожалуйсте, введите новый счёт: ")
    cursor_create.execute("INSERT INTO bank_accounts (user_id, accounts, amount, status) VALUES (%s, %s, %s, %s)",
                          (user_id, account_number, 10000, True))
    conn.commit()

    return BankAccounts(user_id, account_number, 10000, True)


def print_account_bulk(accounts):
    for account in accounts:
        if account.get_status():
            account.print_account()


cursor_delete = conn.cursor()


def delete_account(accounts, user_id, account_number):
    for account in accounts:
        if account.get_user_id() == user_id and account.get_account_number() == account_number:
            cursor_delete.execute("DELETE FROM bank_accounts WHERE user_id = %s AND accounts = %s",
                                  (user_id, account_number))
            conn.commit()

            accounts.remove(account)
            print(f"Счет {account_number} удален.")
            break


cursor_bal_with = conn.cursor()


def balance_withdraw(accounts, account_number, amount):
    for account in accounts:
        if account.get_account_number() == account_number:
            # account.set_balance_withdraw(amount)
            cursor_bal_with.execute("UPDATE bank_accounts SET amount = amount - %s WHERE accounts = %s",
                                    (amount, account_number))
            conn.commit()

            account.set_balance_withdraw(amount)
            print(f"С баланса счета {account_number} списано {amount}.")
            break


cursor_transfers = conn.cursor()


def transfers(accounts, one_acc, second_acc, amount):
    for account in accounts:
        if account.get_account_number() == one_acc:
            # account.set_balance_top_up(amount)
            cursor_transfers.execute("UPDATE bank_accounts SET amount = amount + %s WHERE accounts = %s",
                                     (amount, one_acc))
            conn.commit()

            account.set_balance_top_up(amount)
            print(f"На счет {one_acc} зачислено {amount}.")

        elif account.get_account_number() == second_acc:
            # account.set_balance_withdraw(amount)
            cursor_transfers.execute("UPDATE bank_accounts SET amount = amount - %s WHERE accounts = %s",
                                     (amount, second_acc))
            conn.commit()

            account.set_balance_withdraw(amount)
            print(f"С счета {second_acc} списано {amount}.")
