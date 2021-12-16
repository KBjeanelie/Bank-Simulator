from __future__ import annotations


def check_int(var: str) -> int:
    while var.isalpha():
        print("ERREUR : Entrer un nombre : ")
        var = input("Enter>> ")

    return int(var)


def insufficient_balance_error(message: str = ""):
    print("-------------------------------------------------------------------------------------------")
    print(message)
    print("Votre Solde est insuffisant ")
    print("-------------------------------------------------------------------------------------------")


def check_balance(amount: int | float, message: str = ""):
    print("-------------------------------------------------------------------------------------------")
    print(message)
    print("Votre noveau solde est de", amount, "F CFA")
    print("-------------------------------------------------------------------------------------------")


def sample_echec_message(message: str):
    print("-------------------------------------------------------------------------------------------")
    print("ERREUR: Echec de Transfert")
    print(message)
    print("-------------------------------------------------------------------------------------------")
