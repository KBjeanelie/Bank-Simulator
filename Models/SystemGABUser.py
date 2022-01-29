from dataclasses import dataclass


@dataclass()
class SystemGABUser:
    __user_id: int
    username: str
    password: str
    __customer_id: int

    def __init__(self):
        pass

    def user_id(self):
        return self.__user_id

    def username(self) -> str:
        return self.username

    def password(self) -> str:
        return self.password

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_passwd):
        self.password = new_passwd
