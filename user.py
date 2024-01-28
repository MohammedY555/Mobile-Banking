from connect_db import conn, cursor_us, read_users


class Users:
    def __init__(self, user_id=0, username="", password=""):
        self.__user_id = user_id
        self.__username = username
        self.__password = password

    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


cursor_us

read_users

rows_user = cursor_us.fetchall()

users = [Users(row[0], row[1], row[2]) for row in rows_user]

cursor_us.close()
