import os.path
import sqlite3

from Models.Admin import Admin
from messages import app_bar, successful_account_creation, basic_message_view


def admin_login(root: Admin):
    app_bar("Administration Login")
    username = input("Admin Email : ")
    pasword = input("Admin Password : ")
    print(username + " " + str(root.user()))
    print(pasword + " " + str(root.password()))
    if username == root.user() and pasword == root.password():
        return True
    else:
        return admin_login(root)


def admin_logout():
    pass


def add_customer():
    app_bar("Ajouter un nouveau client")
    name = input("Nom du Client                 :")
    firstname = input("Prenom du Client         :")
    bithday = input("Date de naissance          :")
    sex = input("Sexe du Client                 :")
    adresse = input("Adresse du Client          :")
    email = input("Email du Client              :")
    tel = input("Numéro de téléphone            :")

    path_to_database = os.path.join("..", "Database", "bank_database.db")
    connexion = sqlite3.connect(path_to_database)
    cursor = connexion.cursor()
    request = f'INSERT INTO Customers(lastname, firstname, birthday, sex, adress, email, tel) ' \
              f'VALUES("{name}", "{firstname}", "{bithday}", "{sex}", "{adresse}", "{email}", "{tel}")'
    cursor.execute(request)
    customer_id = cursor.lastrowid

    cursor.execute("INSERT INTO Account (customer_id) VALUES(" + str(customer_id) + ")")

    account_number = cursor.lastrowid

    cursor.execute("INSERT INTO CurrentAccount (account_number, amount) VALUES (" + str(account_number) + ", 0)")

    cursor.execute("INSERT INTO SavingsAccount (account_number, amount) VALUES (" + str(account_number) + ", 0)")

    connexion.commit()
    connexion.close()
    successful_account_creation()


def del_customer(customer_id):
    pass


def show_all_customers(request="SELECT * FROM Customers"):
    path_to_database = os.path.join("..", "Database", "bank_database.db")
    connexion = sqlite3.connect(path_to_database)
    cursor = connexion.cursor()

    customers = cursor.execute(request).fetchall()
    connexion.close()
    for customer in customers:
        print("-------------------------------------------------------------")
        print(f"CLIENT N° {customer[0]} : ")
        print("-------------------------------------------------------------")
        print(f"    ID                          : {customer[0]}")
        print(f"    Nom de famille              : {customer[1]}")
        print(f"    Prenom                      : {customer[2]}")
        print(f"    Date de Naissance           : {customer[3]}")
        print(f"    Sexe du Client              : {customer[4]}")
        print(f"    Adresse du Client           : {customer[5]}")
        print(f"    Email du Client             : {customer[6]}")
        print(f"    Numero du téléphone Client  : {customer[7]}")
        print()


def filter_customers_by_lastname(name):
    if name == "":
        basic_message_view("Aucun filtre selectionné")
        return

    request = f'SELECT * FROM Customers WHERE lastname = "{name.upper()}"'
    show_all_customers(request)


def filter_customers_by_tel(tel):
    if tel == "":
        basic_message_view("Aucun filtre selectionné")
        return

    request = f'SELECT * FROM Customers WHERE tel = "{tel}"'
    show_all_customers(request)


def found_a_customer(tel):
    # request = f'SELECT * FROM Customers WHERE tel = "{tel}"'
    # show_all_customers(request)
    pass


show_all_customers()
