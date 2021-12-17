from __future__ import annotations
from Classes import Client
from messages import insufficient_balance_error, check_int, check_balance


def message(m: str, count: str | int = ""):
    """
        Print a messages
    :param m: message to print must be String
    :param count:
    :return:
    """
    print("---------------------------------------------------------------------------------------------")
    print(m, count)
    print("---------------------------------------------------------------------------------------------")


def app_bar(title: str):
    """
        Print an app bar
    :param title: title of app bar must be String
    :return: void or None
    """
    print("---------------------------------------------------------------------------------------------")
    print(f"|                               {title}                                   |")
    print("---------------------------------------------------------------------------------------------")


def __input__():
    """
        Just inputing something
    :return:
    """
    print("Appuyez sur une touche pour repartir")
    rep = input("Enter>> ")


# --------------------------------------------------------------------------------------------------------#
#               the functions below are used in the pragrammain  interface
# -------------------------------------------------------------------------------------------------------#
def views(q1, q2, q3, title) -> int:
    """
        Display all fuctionnalyty
    :param q1: string
    :param q2: string
    :param q3: string
    :param title: string
    :return: int
    """
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


def programme_views() -> int:
    """
    display the programme view
    :return: void or None
    """
    rep = views("Casier Account", " Customer Account", "System GAB (Customer login)", "EveryOne")
    return rep


# ------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------- #


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

    app_bar("CASHIER ACCOUNT LOGIN")
    user = input("Cashier username    : ")
    passwd = input("Cashier password  : ")

    while user != cahier and passwd != passwd_cashier:
        print("Username or password incorect :(")
        print()
        user = input("Cashier username    : ")
        passwd = input("Cashier password  : ")

    message("Login succesfully :)")
    return True


def cashier_base():
    """
        Display the programme views of cashier interface
    :return:
    """
    rep = views("Lister les Client", "Ajouter un Client", "Supprimer un Client", "CASHIER")
    return rep


def cashier_main(clients: list[Client]):
    """
        it is in this function that all the program takes place on the cashier interface
    :param clients: listof all customer or client account
    :return: void or None
    """
    i = True
    if cashier_login():
        while i:
            r = cashier_base()
            if r == 1:
                show_all_customers(clients)
                __input__()
            elif r == 2:
                new_customers: Client = create_customer()
                clients.append(new_customers)
                __input__()
            elif r == 3:
                print("Coming soon")
                # del_client(clients, 5)
                __input__()
            else:
                message("Deconnexion\nA bientôt :)")
                i = False


# ------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------#
#               the functions below are used in the gab system
# -------------------------------------------------------------------------------------------------------#

def choose_type_account():
    """
        Allowing the choice between current account and savings account
    :return:
    """
    print("Choisir le type de compte : ")
    print("1 : Courant")
    print("2 : Epargne")
    choose = input("Enter>> ")
    choosed = check_int(choose)

    if choosed == 1:
        return 1
    return 2


def system_gab_login(clients: list[Client]) -> int:
    """
        this function allows the ATM account to authenticate and returns a boolean
        Return the position of client
        :param clients: list of Client
        :return: int
    """
    found = False
    position: int = 0
    app_bar("SYSTEM ATM LOGIN")
    user = input("Username : ")
    passwd = input("Password : ")

    while not found:
        for client in clients:
            if user == client.gab_account.username and passwd == client.gab_account.password:
                return position

            position += 1
        position = 0
        print("Username or password incorect :(")
        print()
        user = input("Username : ")
        passwd = input("Password : ")


def system_gab_check_balance(client: Client):
    """
        Display the solde
    :param client: object
    :return: void or None
    """
    print("--------------------------------- CONSULTATION DU SOLDE -----------------------------------------")
    rep = choose_type_account()
    if rep == 1:
        print("--------------------------------------------------------------------------")
        print("Numero de Compte   :", client.current_account.get_account_number())
        print("Type de Compte     : Courant")
        print("Votre solde est de :", client.current_account.get_amount(), "F CFA")
        print("--------------------------------------------------------------------------")
        return

    print("--------------------------------------------------------------------------")
    print("Numero de Compte     :", client.savings_account.get_account_number())
    print("Type de Compte       : Epargne")
    print("Votre solde est de   :", client.savings_account.get_amount(), "F CFA")
    print("--------------------------------------------------------------------------")


def system_gab_base():
    """
        Display the programme views of ATM system interface
    :return:
    """
    rep = views("Consulter son Solde", "Dépot d'argent", "Retrait d'argent", "GAB System")
    return rep


def money_deposit(client: Client):
    """
    allow the money deposit
    :param client: object
    :return: void or None
    """
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
    """
     Allow the withdrawing money in a current account bank on abject
    :param client: object
    :return: void or None
    """
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

    if not client.savings_account.withdraw_money(amount_verified):
        insufficient_balance_error("ERREUR: Echec de retrait")
        return

    check_balance(client.savings_account.get_amount(), "Retrait éffectué avec succès :)")


def system_gab_main(clients: list[Client]):
    """
       it is in this function that all the program takes place on the ATM system interface
   :param clients: listof all customer or client account
   :return: void or None
   """
    i = True
    customer_index: int = system_gab_login(clients)
    while i:
        r = system_gab_base()
        if r == 1:
            system_gab_check_balance(clients[customer_index])
            __input__()
        elif r == 2:
            money_deposit(clients[customer_index])
            __input__()
        elif r == 3:
            withdraw_money(clients[customer_index])
            __input__()
        else:
            message("Deconnexion\nA bientôt :)")
            i = False


# ------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------#
#               the functions below are used in the customer account interface
# -------------------------------------------------------------------------------------------------------#

def customer_programme() -> int:
    """
    Display all fuctionnalyty
    :return: int
    """
    app_bar("CUSTOMER ACCOUNT ACTIVITY")
    print()
    print("1 : Profile")
    print("2 : Transfert d'argent")
    print("3 : Payement")
    print("4 : Transfert d'argent (Courant vers Epargne)")
    print("5 : Transfert d'argent (Epargne vers Courant)")
    print("6 : Bloquer mon Compte (Epargne)")
    print("7 : Exit")

    response = input("Enter>> ")
    i = True
    while i:
        response_verified = check_int(response)
        if 1 <= response_verified <= 7:
            response = response_verified
            i = False

    return int(response)


def login_customer_account(clients: list[Client]) -> int:
    """
        this function allows the Customer or Client account to authenticate and returns a boolean
        Return the position of client
        :param clients: list of Client
        :return: int
    """
    found = False
    position: int = 0
    app_bar("CUSTOMER ACCOUNT LOGIN")
    account_number = input("Client Number      : ")
    account_number_verify = check_int(account_number)
    passwd = input("Client Password  : ")

    while not found:
        for client in clients:
            if account_number_verify == client.__ID__ and passwd == client.gab_account.password:
                return position

            position += 1
        position = 0
        print("Username or password incorrect :(")
        print()
        account_number = input("Client Number      : ")
        account_number_verify = check_int(account_number)
        passwd = input("Client Password  : ")


def customer_account_main(clients: list[Client]):
    """
       it is in this function that all the program takes place on the Customer interface
   :param clients: listof all customer or client account
   :return: void or None
   """
    i = True
    customer_index: int = login_customer_account(clients)
    while i:
        r: int = customer_programme()
        if r == 1:
            clients[customer_index].profile()
            __input__()
        elif r == 2:
            print("Coming soon")
            __input__()
        elif r == 3:
            clients[customer_index].current_account.payment_invoice()
            __input__()
        elif r == 4:
            clients[customer_index].current_account.transfer_of_current_to_saving(clients[customer_index])
            __input__()
        elif r == 5:
            clients[customer_index].savings_account.current_savings_transfer(clients[customer_index])
            __input__()
        elif r == 6:
            clients[customer_index].savings_account.lock_account()
            __input__()
        else:
            message("Deconnexion\nA bientôt :)")
            i = False
