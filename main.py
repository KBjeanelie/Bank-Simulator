import os.path
import sqlite3

path_to_database = os.path.join("Database", "bank_database.db")

connexion = sqlite3.connect(path_to_database)

cursor = connexion.cursor()

customers = cursor.execute("SELECT * FROM Customers;").fetchall()
accounts = cursor.execute("SELECT * FROM Account;").fetchall()
current_accounts = cursor.execute("SELECT * FROM CurrentAccount;").fetchall()
savings_account = cursor.execute("SELECT * FROM SavingsAccount;").fetchall()
sysgab = cursor.execute("SELECT * FROM SystemGABUser;").fetchall()

print(customers)
print(accounts)
print(current_accounts)
print(savings_account)
print(sysgab)


def login(s):
    username = input("Username :")
    pasword = input("Password  :")
    for m in s:
        if m[1] == username:
            print("trouver")

        if m[2] == pasword:
            print("Password found")


login(sysgab)
