class Admin:

    def __init__(self, username, password):
        self.__user = username
        self.__password = password

    def user(self):
        return self.__user

    def password(self):
        return self.__password

