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

