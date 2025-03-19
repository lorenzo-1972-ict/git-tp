# script with app code to illustrate git branching

import logging

print("Hello Git (on the feature/logging branch!!")

text = input("Enter your name:")

if(len(text) < 3):
    logging.warning("Your name must at least be 3 chararacters long")  # will print a message to the console