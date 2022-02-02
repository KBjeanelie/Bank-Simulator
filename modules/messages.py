def basic_message_view(message):
    print("----------------------------------------------------------------------------------")
    print(message)
    print("----------------------------------------------------------------------------------")


def get_amount(amount):
    new_message = f"Votre solde est de {amount} XAF"
    basic_message_view(new_message)


def insufficient_balance(amount):
    error_message = f"ERREUR: Votre solde est insuffisante\nSolde : {amount}"
    basic_message_view(error_message)


def transfer_failure():
    pass


def successful_transfer():
    basic_message_view("Votre transfert a été effectuer avec succès :)")


def beneficiary_not_found():
    message = "Aucun bénéficiaire n'a été trouvé :( \nReverifier les information avant l'envoi"
    basic_message_view(message)


def successful_deposit(amount, new_amount):
    message = f"Vous avez éffectué un depôt de {amount} XAF\nNouveau solde : {new_amount}"
    basic_message_view(message)


def successful_registration(customer_id):
    message = f"Enregistrement reussit :)\nLe client{customer_id} a été enregistré avec succès"
    basic_message_view(message)


def successful_account_creation():
    message = "Création du compte banquaire\n" \
              "     ---> Création du compte courant du client reussit :)\n" \
              "     ---> Création du compte epargne du client réussit :)"

    basic_message_view(message)


def registration_failed():
    message = "ERROR: Sothing went wrong :(\nEchec d'enregistrement du client"
    basic_message_view(message)


def deletion_succeeds():
    basic_message_view("Suppression reussit :)")


def logout_succeeded():
    basic_message_view("Deconexion ressit :)\nA bientôt !")


def app_bar(title):
    print("#################################################################################")
    print(f"              {title}")
    print("#################################################################################")


