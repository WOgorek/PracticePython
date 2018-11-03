# Generate a random number between 1 and 9 (including 1 and 9).
#  Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

gry = 0
win = 0

while True:
    liczba = random.randint(1, 9)
    proba = int(input("O jakiej liczbie mysle? (0 for exit): "))
    if proba == 0:
        break
    gry += 1
    if liczba > proba:
        print("Wybrales za małą")
    elif liczba < proba:
        print("Wybrales za duza")
    else:
        print("BRAWO")
        win += 1
print("Grales {} razy i zwyciezyles {} razy".format(gry, win))
