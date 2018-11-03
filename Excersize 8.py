# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

while True:
    gracz1 = input("GRACZ 1 wybierz: {R)ock , (S)cissors, (P)aper:")
    gracz2 = input("GRACZ 2 wybierz: {R)ock , (S)cissors, (P)aper:")

    if gracz1 == gracz2:
        print("REMIS")
    elif (gracz1 == "R" and gracz2 == "S") or (gracz1 == "S" and gracz2 == "P") or (gracz1 == "P" and gracz2 == "R"):
        print("GRACZ 1 WYGRAL")
    elif (gracz2 == "R" and gracz1 == "S") or (gracz2 == "S" and gracz1 == "P") or (gracz2 == "P" and gracz1 == "R"):
        print("GRACZ 2 WYGRAL")
    else:
        print("Bledne wejscie - gra niewazna")

    print("*" * 40)
    print()
    exit = input("Czy chcesz wyjsc z gry T/N:")
    if exit == "T" or exit == "t":
        break
