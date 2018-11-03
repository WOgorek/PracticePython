#In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:
#
# Draw the Tic Tac Toe game board
# Checking whether a game board has a winner
# Handle a player move from user input
# The next step is to put all these three components together to make a two-player Tic Tac Toe game!
# Your challenge in this exercise is to use the functions from those previous exercises all together
# in the same program to make a two-player game that you can play with a friend.
# There are a lot of choices you will have to make when completing this exercise,
# so you can go as far or as little as you want with it.
#
# Here are a few things to keep in mind:
#
# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again
# and keep a running tally of who won more - Player 1 or Player 2.

game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]


def rysuj_plansze(gra):
    wymiar = len(gra)
    poziom = ""
    for i in range(wymiar):
        poziom += " ---"
    for j in range(wymiar):
        print(poziom)
        pion = "|"
        for k in range(wymiar):
            pion += " " + game[j][k] + " |"
        print(pion)
    print(poziom)


def ruch_gracza(gracz, wiersz, kolumna, gra):
    znacznik = " "
    if gracz == 1:
        znacznik = "X"
    if gracz == 2:
        znacznik = "O"
    if gra[wiersz-1][kolumna-1] == " ":
        gra[wiersz-1][kolumna-1] = znacznik
    else:
        print("Pole już zajęte")
    return gra


def check_wins(game, player):
    win = False
    if player == 1:
        znacznik = "O"
    else:
        znacznik = "X"

    for i in range(3):
        if game[i][0] == game[i][1] and game[i][1] == game[i][2] and game[i][0] == znacznik:
            win = True
        if game[0][i] == game[1][i] and game[1][i] == game[2][i] and game[0][i] == znacznik:
            win = True
    if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] == znacznik:
        win = True
    if game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[0][2] == znacznik:
        win = True
    return win


def czy_koniec_gry(game):
    if check_wins(game, 1):
        return True
    elif check_wins(game, 2):
        return True
    else:
        return False


player = 1
ktory_ruch = 0
remis = False
koniec_gry = False
rysuj_plansze(game)
while not koniec_gry:
    print("-----------------------------------------------")
    ruch = input("Gracz {} : Podaj gdzie stawiasz symbol (wiersz, kolumna):".format(player))
    lista = ruch.split(",")
    wiersz = int(lista[0])
    kolumna = int(lista[1])
    game = ruch_gracza(player, wiersz, kolumna, game)
    rysuj_plansze(game)
    koniec_gry = czy_koniec_gry(game)
    if not koniec_gry:
        if player == 1:
            player = 2
        else:
            player = 1
        for i in range(8):
            print()
        ktory_ruch += 1
    if ktory_ruch == 9:
        koniec_gry = True
        remis = True

print()
if not remis:
    print(" *** Wygrał gracz {} ***".format(player))
else:
    print(" *** REMIS ***")
