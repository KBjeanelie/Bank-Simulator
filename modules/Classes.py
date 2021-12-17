from __future__ import annotations

from dataclasses import dataclass

from messages import insufficient_balance_error, check_int, check_balance, sample_echec_message


def ms(title: str):
    """
    this function print a simple message after an action occure
    :param title: represent a message to print
    :return:
    """
    print("----------------------------------------------------------------------------------------")
    print(title)
    print("----------------------------------------------------------------------------------------")


@dataclass
class Humain:
    count = 0
    last_name: str
    firstname: str
    birthday: str
    adress: str
    email: str
    sexe: str
    tel: str

    def __post_init__(self):
        Humain.count += 1
        self.__ID__: int = Humain.count
        # self.fullname = f"{self.firstname} {self.last_name}"

    """
        GETTERS
    """

    def __ID__(self):
        return self.__ID__

    # def fullname(self):
    #    return self.fullname

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
    count: int = 0  # this variable is for counting the number of object created

    def __init__(self):
        Account.count += 1
        self.bank_code: int = 21007
        self.branch_code: int = 10000
        self.account_number: int = Account.count
        self.amount: int | float = 0
        self.tax: int | float = 0
        self.TVA: int = 1043

    def bank_code(self) -> int:
        """
            get the value of bank code
        :return: int
        """
        return self.bank_code

    def branch_code(self) -> int:
        """
            get the value of branch code
        :return: int
        """
        return self.branch_code

    def account_number(self) -> int:
        """
            get the value of account number
        :return: int
        """
        return self.account_number

    def deposit(self, sum_add: float | int) -> bool:
        """
            allow the money deposit
            Return True if all is good
        :param sum_add: amount to deposit on account bank
        :return:True | False
        """
        self.amount += sum_add
        return True

    def withdraw_money(self, sum_remove: float | int) -> bool:
        """
            Allow the withdrawing money in a current account bank on abject
            Return True if all is good
            We remove also a tax for this methode
        :param sum_remove: amount of withdrawing
        :return: True | False
        """
        self.tax = (sum_remove * 12) / 100
        if sum_remove + self.tax >= self.amount:
            return False
        self.amount -= sum_remove + self.tax
        self.tax = 0
        return True

    def get_account_number(self):
        """
            get the all value of account bank number
        :return: str
        """
        return str(self.bank_code) + str(self.branch_code) + str(self.account_number)

    def get_amount(self) -> int | float:
        """
            get the solde of an account bank maybe current account or savings account
        :return: int or float
        """
        return self.amount

    def bank_transfert(self, clients: list[Client]):
        """
        Allow sending money to another of account bank
        We remove also a tax for this methode
        :param clients: list of all account in the system
        :return: void or None
        """
        print("----------------------------------- Transfert d'argent ------------------------------")
        sender_account_number = input("Saisir le numéro du compte émetteur          : ")
        beneficiary_account_number = input("Saisir le numéro du compte bénéficiaire :")
        transfer_amount = input("Saisir le montant du virement                      : ")
        transfer_amount_cheked: int = check_int(transfer_amount)
        beneficiary_name = input("Choisir une récurrence ou non                     :")
        beneficiary_firstname = input("Choisir un Prenom                            :")

        self.tax = (transfer_amount_cheked * 25) / 100

        if sender_account_number != self.get_account_number():
            sample_echec_message("Le numéro du compte émetteur n'existe pas")
            return

        found: bool = False

        for client in clients:
            if client.current_account.get_account_number() == beneficiary_account_number:
                if client.current_account.deposit(transfer_amount_cheked):
                    self.amount -= transfer_amount_cheked + self.tax
                    found = True
                    break
                else:
                    insufficient_balance_error("ERREUR: Echec de transfert")
                    return
        if found:
            print("Non du bénéficiare               :", beneficiary_name)
            print("Prenom du bénéficiare            :", beneficiary_firstname)
            print("Numéro de compte du bénéficiare  :", beneficiary_account_number)
            print("Type de compte du bénéficiare    : Courant")
            print("Montant tranferé                 :", transfer_amount, "F CFA")
            print("TVA                              :", self.TVA)
            print("Total                            :", self.TVA + int(transfer_amount), "F CFA")
            check_balance(self.amount, "Transfert d'argent réaliser avec succès")
            return

        sample_echec_message("Le numéro du compte bénéficiaire n'existe pas")

    def payment_invoice(self):
        """
        Allow the paiement of a produit
        We use a cuurent account
        We remove also a tax for this methode
        :return: void or None
        """
        print("------------------------------ Payement de Facture ------------------------------------------")
        product_name = input("Entrer le nom du produit  :")
        amount_product = input("Entrer le montant : ")
        amount_checked = check_int(amount_product)

        if self.amount <= amount_checked + self.TVA:
            insufficient_balance_error("ERREUR: Echec de payement :(")
            return

        self.amount -= amount_checked + self.TVA
        ms("Payement effectué avec succès !")
        print("Nom du produit  :", product_name)
        print("Prix du produit :", amount_checked, "F CFA")
        print("TVA             :", self.TVA)
        print("Total           :", amount_checked + self.TVA, "F CFA")
        check_balance(self.amount)


class CurrentAccount(Account):
    def __init__(self):
        super(CurrentAccount, self).__init__()

    def transfer_of_current_to_saving(self, client):
        """
        Send money of current account to savings account
        :param client: the current object
        :return: void or None
        """
        print()
        print("-------------------------- Transfert d'argent (Courant vers Epargne) -----------------------------")
        amount = input("Entrer le montant : ")
        send_amount = check_int(amount)
        self.tax = (send_amount * 25) / 100
        if client.current_account.get_amount() <= send_amount:
            insufficient_balance_error("ERREUR: Echec de Transfert :(")
            return

        client.savings_account.deposit(send_amount)
        client.current_account.amount -= self.tax

        print("Transfert effectué avec succès :)")
        print("-------------------------------------------------------------------------------------------")
        print("Montant transferé              :", send_amount)
        print("Frais de transport             :", self.tax, "F CFA")
        print("Numéro de Compte               :", client.savings_account.get_account_number())
        print("Type de Compte                 : Epargne")
        check_balance(client.current_account.get_amount())
        self.tax = 0


class SavingsAccount(Account):
    def __init__(self):
        super(SavingsAccount, self).__init__()
        self.lock_time = 0
        self.is_lock = False

    def current_savings_transfer(self, client):
        """
            Send money of savings account to current account
            :param client: the current object
            :return: void or None
        """
        if self.is_lock:
            ms("Transfert non disponible\nVotre compte a étébloqué")
            return

        print()
        print("-------------------------- Transfert d'argent (Courant vers Epargne) -----------------------------")
        amount = input("Entrer le montant : ")
        send_amount = check_int(amount)
        self.tax = (send_amount * 35) / 100
        if client.current_account.get_amount() <= send_amount:
            insufficient_balance_error("ERREUR: Echec de Transfert :(")
            return

        client.current_account.deposit(send_amount)
        client.savings_account.amount -= self.tax

        print("Transfert effectué avec succès :)")
        print("-------------------------------------------------------------------------------------------")
        print("Montant transferé              :", send_amount, "F CFA")
        print("Frais de transport             :", self.tax, "F CFA")
        print("Numéro de Compte               :", client.current_account.get_account_number())
        print("Type de Compte                 : Courant")
        check_balance(client.current_account.get_amount())
        self.tax = 0

    def lock_account(self):
        """
        Lock a savings account
        :return:void or None
        """
        print()
        print("-------------------------- Transfert d'argent (Courant vers Epargne) -----------------------------")
        print("Voulez vous bloqué votre compte ? (o/n) ")
        rep = input("Enter>> ")
        while rep != "o" and rep != "n":
            rep = input("Enter>> ")

        if rep == "o":
            self.is_lock = True
            ms("Votre compte épargne a été bloqué\nVous ne pouvez plus éffectuer des virement ou payement")
            return

        self.is_lock = False
        ms("Compte non bloqué ou débloqué")


@dataclass()
class SystemGAB:

    def __init__(self):
        self.username = ""
        self.password = ""

    def username(self) -> str:
        return self.username

    def password(self) -> str:
        return self.password

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_passwd):
        self.password = new_passwd


class Client(Humain):

    def __post_init__(self):
        super(Client, self).__post_init__()
        self.current_account = CurrentAccount()
        self.savings_account = SavingsAccount()
        self.gab_account = SystemGAB()

    def profile(self):
        """
            Display all information about a client of custemer account
        :return: void or None
        """
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
        print()
