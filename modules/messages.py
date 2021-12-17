from __future__ import annotations


def check_int(var: str) -> int:
    """
        check if the param send is an Integer
        if False : an error print
    :param var: value send
    :return: int
    """
    while var.isalpha():
        print("ERREUR : Entrer un nombre : ")
        var = input("Enter>> ")

    return int(var)


def insufficient_balance_error(message: str = ""):
    """
        Print the message of insufficient balance
    :param message: another message to print but facultative
    :return: void or None
    """
    print("-------------------------------------------------------------------------------------------")
    print(message)
    print("Votre Solde est insuffisant ")
    print("-------------------------------------------------------------------------------------------")


def check_balance(amount: int | float, message: str = ""):
    """
        Print the message of a new balance after a traitment
    :param amount: amount of an account bank to print
    :param message:  another message to print but facultative
    :return: void or None
    """
    print("-------------------------------------------------------------------------------------------")
    print(message)
    print("Votre noveau solde est de", amount, "F CFA")
    print("-------------------------------------------------------------------------------------------")


def sample_echec_message(message: str):
    """
        Print the message of error after echec of sending money
    :param message: message to print must be a string
    :return: void or None
    """
    print("-------------------------------------------------------------------------------------------")
    print("ERREUR: Echec de Transfert")
    print(message)
    print("-------------------------------------------------------------------------------------------")
