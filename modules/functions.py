from __future__ import annotations

from Classes import Client
from messages import insufficient_balance_error, check_int, check_balance


def message(m: str, count: str | int = ""):
    print("---------------------------------------------------------------------------------------------")
    print(m, count)
    print("---------------------------------------------------------------------------------------------")


# -------------------------------------------------------------------------------------------------------#
#               the functions below are used in the gab system
# -------------------------------------------------------------------------------------------------------#

def choose_type_account():
    print("Choisir le type de compte : ")
    print("1 : Courant")
    print("2 : Epargne")
    choose = input("Enter>> ")
    choosed = check_int(choose)

    if choosed == 1:
        return 1
    return 2


def money_deposit(client: Client):
    print("----------------------------- DEPOT D'ARGENT -----------------------------------")
    rep = choose_type_account()
    amount = input("Entrer la somme : ")
    amount_verified = check_int(amount)
    if rep == 1:
        client.current_account.deposit(amount_verified)
        check_balance(client.current_account.get_amount(), "Dépot éffectuer avec succès :)")
        return

    client.savings_account.deposit(amount_verified)
    check_balance(client.savings_account.get_amount(), "Dépot éffectuer avec succès :)")


def withdraw_money(client: Client):
    print("----------------------------- RETIRER DE L'ARGENT -----------------------------------")
    rep = choose_type_account()
    amount = input("Entrer le montant : ")
    amount_verified = check_int(amount)
    if rep == 1:
        if not client.current_account.withdraw_money(amount_verified):
            insufficient_balance_error("ERREUR: Echec de retrait")
            return
        check_balance(client.current_account.get_amount(), "Retrait éffectué avec succès :)")
        return

    if client.savings_account.withdraw_money(amount_verified):
        insufficient_balance_error("ERREUR: Echec de retrait")
        return

    check_balance(client.savings_account.get_amount(), "Retrait éffectué avec succès :)")


# -------------------------------------------------------------------------------------------------------#
#               the functions below are used in the cashien client interface
# -------------------------------------------------------------------------------------------------------#
cahier = "uba"
passwd_cashier = "uba1234"


def create_customer() -> Client:
    """
    this function is used to create a new customer with all the necessary information and also to create an ATM
    account for him
    :return: objet of Client
    """
    print("---------------------------------- CREATION D'UN COMPTE CLIENT ---------------------------------------")
    name = input("Nom du Client                 : ")
    fname = input("Prenom du Client             : ")
    dbirth = input("Date de Naissance du Client : ")
    sex = input("Sexe du Client                 : ")
    adress = input("Adresse du Client           : ")

    print("-------------------------------- Information supplementaire -------------------------------")
    email = input("Email du Client              :")
    tel = input("Numero de téléphone du Client  : ")
    customer = Client(last_name=name, firstname=fname, birthday=dbirth, email=email, sexe=sex, adress=adress, tel=tel)
    print("-------------------------- Information sur le system GAB -----------------------------------")
    username = input("Nom d'utilisateur du Client : ")
    passwd = input("Mot de passe du Client        : ")
    customer.gab_account.set_username(username)
    customer.gab_account.set_password(passwd)
    message("Nouveau Client créé avec succès :)")
    return customer


def del_client(clients: list[Client], index: int):
    """
    This function is used to delete all information about client by his index
    :param clients: list of Client objet
    :param index: the indice of object in the list
    :return: none
    """
    print("---------------------------------------------------------------------------------------------")
    rep = input("Voulez vraiment supprimez ce client ? (o/n) : ")
    print(rep)
    while rep != "o" and rep != "n":
        rep = input("Saisi incorect\nEnter>> ")
    del clients[index]
    message("Le client a été supprimer")


def show_all_customers(clients: list[Client]):
    """
    Display all the customer account in the programme
    :param clients: list of Client
    :return: None
    """
    print("-------------------------------------- Liste de Client --------------------------------------")
    print()
    count = len(clients)

    if count == 0:
        message("Aucun client enregistrer")
        return

    for client in clients:
        print("---------------------------------------------------------------------------------------------")
        print(client.__ID__, "| -  |", client.last_name, "|  -  |", client.firstname, "|  -  |", client.birthday,
              "|  -  |", client.sexe, "|  -  |", client.adress, "|  -  |", client.email, "|  -  |", client.tel)
    message("Total :", count)


def cashier_login():
    """
    this function allows the cashier to authenticate and returns a boolean
    :return: bool
    """

    print("---------------------------------- CASSIER CONNECTION ----------------------------------------------")
    user = input("Cashier username    : ")
    passwd = input("Cashier password  : ")

    while user != cahier and passwd != passwd_cashier:
        print("Username or password incorect :(")
        print()
        user = input("Cashier username    : ")
        passwd = input("Cashier password  : ")

    message("Login succesfully :)")
    return True


# --------------------------------------------------------------------------------------------------------#
#               the functions below are used in the pragrammain  interface
# -------------------------------------------------------------------------------------------------------#
def views(q1, q2, q3, title) -> int:
    print("---------------------------------------------------------------------------------------------")
    print(f"|                                 KUB'S BANK For {title}                                     |")
    print("---------------------------------------------------------------------------------------------")
    print()
    print(f"1 : {q1}")
    print(f"2 : {q2}")
    print(f"3 : {q3}")
    print(f"4 : exit")

    response = input("Enter>> ")
    i = True
    while i:
        response_verified = check_int(response)
        if 1 <= response_verified <= 4:
            response = response_verified
            i = False

    return int(response)


def cashier_base():
    rep = views("Lister les Client", "Ajouter un Client", "Supprimer un Client", "CASHIER")
    return rep


def cashier_main(clients: list[Client]):
    i = True
    if cashier_login():
        while i:
            r = cashier_base()
            if r == 1:
                show_all_customers(clients)
                r1 = input("Appuyez sur touche pour repartir\nEnter")
            elif r == 2:

                new_customers: Client = create_customer()
                clients.append(new_customers)
                r1 = input("Appuyez sur touche pour repartir\nEnter")
            elif r == 3:
                print("Coming soon")
                # del_client(clients, 5)
                r1 = input("Appuyez sur touche pour repartir\nEnter")
            else:
                message("Deconnexion\nA bientôt :)")
                i = False


def system_gab():
    rep = views("Consulter son Solde", "Dépot d'argent", "Retrait d'argent", "GAB System")


def programme_views() -> int:
    rep = views("Casier Account", " Customer Account", "System GAB (Customer login)", "EveryOne")
    return rep
