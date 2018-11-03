# Write a password generator in Python. Be creative with how you generate passwords
#  - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import string
import random


def password_generator():
    dlugosc = random.randint(15, 50)
    haslo = []
    for i in range(1, dlugosc):
        rodzaj = random.randint(1, 10)
        if rodzaj <= 7:
            zbior = string.ascii_letters
        elif rodzaj <= 9:
            zbior = string.digits
        else:
            zbior = string.punctuation
        znak = random.choice(zbior)
        haslo.append(znak)
    haslo_finalne = "".join(haslo)
    return haslo_finalne


h1 = password_generator()
h2 = password_generator()
h3 = password_generator()
print(h1)
print(h2)
print(h3)