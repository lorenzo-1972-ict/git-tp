# script with app code

import logging

print("Hello Git sur la branche Feature/logging!!")

text = input("Veuillez rentrer votre nom")

if(len(text) < 3):
    logging.warning('Le nom doit avoir au moins 3 char')  # will print a message to the console
