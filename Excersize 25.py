# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#
# This time, we’re going to do exactly the opposite.
# You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#
# At the end of this exchange, your program should print out how many guesses it took to get your number.
#
# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy.
# An alternate strategy might be to guess 50 (right in the middle of the range),
# and then increase / decrease by 1 as needed.
# After you’ve written the program, try to find the optimal strategy!
# (We’ll talk about what is the optimal one next week with the solution.)

dolny_zakres = 0
gorny_zakres = 100
odgadl = False
proba = 0
liczba = 0

while not odgadl:
    szerokosc = gorny_zakres - dolny_zakres
    liczba = int(dolny_zakres+szerokosc/2)
    proba += 1
    test_odpowiedzi = False
    odpowiedz = input("Próba nr {}. Czy liczba o której myśliśz jest większa od {} (W), mniejsza (M) czy równa (R)?".format(proba, liczba))
    odpowiedz.upper()
    if odpowiedz == "R":
        odgadl = True
    elif odpowiedz == "W":
        dolny_zakres = liczba
    elif odpowiedz == "M":
        gorny_zakres = liczba
    else:
        print("Odpowiedz nieprawidlowa!")
print()
print("Udało mi się zgadnąć po {} próbach!".format(proba))

