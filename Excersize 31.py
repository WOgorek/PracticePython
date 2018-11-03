# Let’s continue building Hangman.
# In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter.
# The player guesses one letter at a time until the entire word has been guessed.
# (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a letter and displays letters
# in the clue word that were guessed correctly. For now, let the player guess an infinite number of times
# until they get the entire word. As a bonus, keep track of the letters the player guessed and display
# a different message if the player tries to guess that letter again.
# Remember to stop the game when all the letters have been guessed correctly!
# Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining
#  - we will deal with those in a future exercise.


def zgadnij(word):
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
    print()
    print(" BRAWO - ZGADLES!!!")
    print(" Zajelo Ci to {} prób".format(ilosc_prob))
    print()


zgadnij("TUTAJ")
zgadnij("MASTODONT")
