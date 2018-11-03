# In this exercise, we will finish building Hangman. In the game of Hangman,
#  the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
#
# In Part 1, we loaded a random word list and picked a word from it.
# In Part 2, we wrote the logic for guessing the letter and displaying that information to the user.
# In this exercise, we have to put it all together and add logic for handling guesses.
#
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
#
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed,
# don’t penalize them - let them guess again.
# Optional additions:
#
# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left",
# display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help you!

import random


def wylosuj_linie(plik):
    with open(plik, 'r') as open_file:
        line = random.choice(open_file.readlines())
    return line


def zagraj(word):
    dlugosc = len(word)
    odgadniete = ("_" * dlugosc)
    podzielone = list(word)
    odgadniete_podzielone = list(odgadniete)
    odgadniete = ("_ " * dlugosc)
    print("Welcome to HANGMAN!")
    print(odgadniete)
    ilosc_trafionych = 0
    ilosc_prob = 0
    koniec = False
    while not koniec:
        ilosc_prob += 1
        litera_zgadywana = input("Podaj literę:")
        i = 0
        for litera in podzielone:
            if litera == litera_zgadywana:
                odgadniete_podzielone[i] = litera
                ilosc_trafionych += 1
            i += 1
        odgadniete = " ".join(odgadniete_podzielone)
        print(odgadniete)
        if ilosc_trafionych == dlugosc:
            koniec = True
        if ilosc_prob == 7:
            koniec = True

    print()
    if ilosc_prob <= 6:
        print(" BRAWO - ZGADLES!!!")
        print(" Zajelo Ci to {} prób".format(ilosc_prob))
    else:
        print("KONIEC - Nie zgadłeś!")
        print("Szukane słowo to: {}".format(word))
    print()


slowo = wylosuj_linie("sowpods.txt")
zagraj(slowo)

# s = 'shak#spea#e'
# c = '#'
# print [pos for pos, char in enumerate(s) if char == c]