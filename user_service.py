from bank_account import BankAccounts


def find_user(users, username, password):
    for us in users:
        if us.get_username() == username and us.get_password() == password:
            return us
    return None


def get_account_user_id(accounts, user_id):
    my_list = []
    for account in accounts:
        if account.get_user_id() == user_id:
            my_list.append(account)
    return my_list
