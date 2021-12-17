from Classes import Client
from modules.functions import views, cashier_main, message, system_gab_main, customer_account_main

# Create a liste vide of Customers
Customers: list[Client] = []

# Create three customers for initialization the program
customer1: Client = Client(last_name="Kumbembula", firstname="Jean Elie", birthday="25/01/1999",
                           adress="50 rue nkouma brazzaville congo", email="jeaneliekubembula@gmail.com",
                           sexe="M", tel="064838870")
customer1.gab_account.set_username("elie")
customer1.gab_account.set_password("elie1234")

customer2: Client = Client(last_name="Walter", firstname="Elijah", birthday="25/01/1999",
                           adress="241 rue bandza brazzaville congo", email="elijahwalter2018@gmail.com",
                           sexe="M", tel="064838870")
customer2.gab_account.set_username("walter")
customer2.gab_account.set_password("walter1234")

customer3: Client = Client(last_name="Poba", firstname="Emmanuella", birthday="25/07/2003",
                           adress="50 rue nkouma brazzaville congo", email="pobamanu@gmail.com",
                           sexe="F", tel="064838070")
customer3.gab_account.set_username("manue")
customer3.gab_account.set_password("manue1234")

# add them into list
Customers.append(customer1)
Customers.append(customer2)
Customers.append(customer3)

launch = True  # start the program

while launch:
    choice = views("Cashier Account", "Customer Account", "System ATM", "EveryOne")
    if choice == 1:
        cashier_main(Customers)
    elif choice == 2:
        customer_account_main(Customers)
    elif choice == 3:
        system_gab_main(Customers)
    else:
        message("A bientôt :)")  # Exit programme
        launch = False
