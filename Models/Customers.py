from dataclasses import dataclass


@dataclass
class Customers:
    last_name: str
    firstname: str
    birthday: str
    adress: str
    email: str
    sexe: str
    tel: str

    def __init__(self, name, firstname, birthday, adress, email, sex, tel):
        self.last_name = name
        self.firstname = firstname
        self.birthday = birthday
        self.adress = adress
        self.email = email
        self.sexe = sex
        self.tel = tel

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
        print("Email                :", self.email)
        print("Sexe                 :", self.sexe)
        print("Numero de Télépjone  :", self.tel)

        print("--------------------------- Information bancaire ----------------------------------")
        print("________")
        print("Montant              :")
        print("Code banque          :")
        print("Code guichet         :")
        print("N° de Compte         :")
        print("N° de Compte bancaire:")
        print("Type de Compte       : Courant")

        print("________")
        print("Montant              :")
        print("Code banque          :")
        print("Code guichet         :")
        print("N° de Compte         :")
        print("N° de Compte bancaire:")
        print("Type de Compte       : Epargne")
        print()

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
