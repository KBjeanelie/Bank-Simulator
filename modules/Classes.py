from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Humain:
    last_name: str
    firstname: str
    birthday: str
    adress: str
    email: str
    sexe: str
    tel: str

    def __post_init__(self):
        self.fullname = f"{self.firstname} {self.last_name}"

    """
            GETTERS
        """

    def fullname(self):
        return self.fullname

    def lastname(self) -> str:
        """
        retourn the name of objet
        :return: str
        """
        return self.last_name

    def firstname(self) -> str:
        """
        retourn the firstname of objet
        :return: str
        """
        return self.firstname

    def birthday(self) -> str:
        """
        retourn the birthday of objet
        :return: str
        """
        return self.birthday

    def sexe(self) -> str:
        """
        retourn the sex of objet
        :return: str
        """
        return self.sexe

    def adress(self) -> str:
        """
        retourne l'adress
        :return: str
        """
        return self.adress

    def email(self) -> str:
        """
        retourn the email of objet
        :return: str
        """
        return self.email

    def tel(self) -> str:
        """
        retourn the telephone number of objet
        :return: str
        """
        return self.tel

    """
        SETTERS
    """

    def set_last_name(self, name):
        """
        modify the value of
        :param name: str
        :return: None
        """
        self.last_name = name

    def set_firstname(self, first_name: str):
        """
        modify the value of
        :param first_name: str
        :return: None
        """
        self.firstname = first_name

    def set_birthday(self, birthday: str):
        """
        modify the value of
        :param birthday: str
        :return: None
        """
        self.birthday = birthday

    def set_sexe(self, sex: str):
        """
        modify the value of
        :param sex: str
        :return: None
        """
        self.sexe = sex

    def set_adress(self, adress: str):
        """
        modify the value of
        :param adress: str
        :return: None
        """
        self.adress = adress

    def set_email(self, email: str):
        """
        modify the value of
        :param email: str
        :return: None
        """
        self.email = email

    def set_tel(self, tel: str):
        """
        modify the value of
        :param tel: str
        :return: None
        """
        self.tel = tel


class Account:
    count = 0

    def __init__(self):
        Account.count += 1
        self.bank_code = 21007
        self.branch_code = 10000
        self.account_number = Account.count
        self.amount = 0
        self.tax = 0
        self.TVA = 1043

    def bank_code(self):
        return self.bank_code

    def branch_code(self):
        return self.branch_code

    def account_number(self):
        return self.account_number

    def deposit(self, sum_add: float | int) -> bool:
        self.amount += sum_add
        return True

    def withdraw_money(self, sum_remove: float) -> bool:
        self.tax = (sum_remove * 12) / 100
        if sum_remove + self.tax >= self.amount:
            return False
        self.amount -= sum_remove + self.tax
        self.tax = 0
        return True

    def get_account_number(self):
        return str(self.bank_code) + str(self.branch_code) + str(self.account_number)

    def get_amount(self):
        return self.amount


class CurrentAccount(Account):
    def __init__(self):
        super(CurrentAccount, self).__init__()

    def transfer_of_current_to_saving(self, client):
        print("----------------------------------- Transfert d'argent ------------------------------")
        amount = input("Entrer le montant : ")
        send_amount = check_int(amount)
        self.tax = (send_amount * 25) / 100
        if client.current_account.get_amount() <= send_amount:
            print("Impossible de transferer de l'argent :(")
            print("Fonds Insuffisant !")
            return

        client.savings_account.deposit(send_amount)
        client.current_account.amount -= self.tax

        print("Transfert effectué avec succès :)")
        print("Montant transferé              :", send_amount)
        print("Frais de transport             :", self.tax, "F CFA")
        print("Numéro de Compte               :", client.savings_account.get_account_number())
        print("Type de Compte                 : Epargne")
        print("-------------------------------------------------------------------------------------------")
        self.tax = 0


class SavingsAccount(Account):
    def __init__(self):
        super(SavingsAccount, self).__init__()
        self.lock_time = 0
        self.is_lock = False

    def current_savings_transfer(self, client):
        print("----------------------------------- Transfert d'argent ------------------------------")
        amount = input("Entrer le montant : ")
        send_amount = check_int(amount)
        self.tax = (send_amount * 35) / 100
        if client.current_account.get_amount() <= send_amount:
            print("Impossible de transferer de l'argent :(")
            print("Fonds Insuffisant !")
            return

        client.current_account.deposit(send_amount)
        client.savings_account.amount -= self.tax

        print("Transfert effectué avec succès :)")
        print("Montant transferé              :", send_amount, "F CFA")
        print("Frais de transport             :", self.tax, "F CFA")
        print("Numéro de Compte               :", client.current_account.get_account_number())
        print("Type de Compte                 : Courant")
        print("-------------------------------------------------------------------------------------------")
        self.tax = 0


class SystemGAB:

    def __init__(self):
        self.username = ""
        self.password = ""

    def username(self):
        return self.username

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_passwd):
        self.password = new_passwd

    def login(self, client: Client):
        print("---------------------------- SE CONNECTER -------------------------------------")
        user = input("Username : ")
        passwd = input("Password : ")

        while user != client.gab_account.username or passwd != client.gab_account.password:
            print("ERREUR: Username ou password est incorect\n")
            user = input("Username : ")
            passwd = input("Password : ")

        self.username = client.gab_account.username
        self.password = client.gab_account.password
        return user, passwd

    """
    def check_balance(self, client: Client):
        print("--------------------------------- CONSULTATION DU SOLDE -----------------------------------------")
        rep = choose_type_account()
        if rep == 1:
            print("Numero de Compte  : ", self.account_number)
            print("Votre solde est de:", client.current_account.get_amount())
            print("--------------------------------------------------------------------------")
            return

        print("Numero de Compte  : ", self.account_number)
        print("Votre solde est de:", client.savings_account.get_amount())
        print("--------------------------------------------------------------------------")
    """


class Client(Humain):

    def __post_init__(self):
        super(Client, self).__post_init__()
        self.current_account = CurrentAccount()
        self.savings_account = SavingsAccount()
        self.gab_account = SystemGAB()

    def profile(self):
        print("--------------------------- Information  Personnelle -------------------------------")
        print("Nom                  :", self.lastname().upper())
        print("Prenom               :", self.firstname)
        print("Date de Naissance    : ", self.birthday)
        print("Sexe                 :", self.sexe)
        print("Domicile             :", self.adress)
        print("--------------------------- Information bancaire ----------------------------------")
        print("________")
        print("Montant              :", self.current_account.get_amount(), "F CFA")
        print("Code banque          :", self.current_account.bank_code)
        print("Code guichet         :", self.current_account.branch_code)
        print("N° de Compte         :", self.current_account.account_number)
        print("N° de Compte bancaire:", self.current_account.get_account_number())
        print("Type de Compte       : Courant")

        print("________")
        print("Montant              :", self.savings_account.get_amount(), "F CFA")
        print("Code banque          :", self.savings_account.bank_code)
        print("Code guichet         :", self.savings_account.branch_code)
        print("N° de Compte         :", self.savings_account.account_number)
        print("N° de Compte bancaire:", self.savings_account.get_account_number())
        print("Type de Compte       : Epargne")
        if self.savings_account.is_lock:
            print("Compte bloqué : YES")
        else:
            print("Compte bloqué : NO")
