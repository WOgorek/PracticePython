# As you may have guessed, we are trying to build up to a full tic-tac-toe board.
# However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
#
# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe,
# not worrying about how the moves were made.
# If a game of Tic Tac Toe is represented as a list of lists, like so:
#
# game = [[1, 2, 0],
#         [2, 1, 0],
#         [2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any.
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

gra = [[1, 2, 0],
       [2, 1, 0],
       [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

def check_wins(game, player):
    win = False
    for i in range(3):
        if game[i][0] == game[i][1] and game[i][1] == game[i][2] and game [i][0] == player:
            win = True
        if game[0][i] == game[1][i] and game[1][i] == game[2][i] and game [0][i] == player:
            win = True
    if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] == player:
        win = True
    if game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[0][2] == player:
        win = True
    return win


def gra_pelna(game):
    if check_wins(game,1):
        print("Wygral gracz nr 1")
    elif check_wins(game,2):
        print("Wygral gracz nr 2")
    else:
        print("REMIS")

gra_pelna(winner_is_2)
gra_pelna(winner_is_1)
gra_pelna(winner_is_also_1)
gra_pelna(no_winner)
gra_pelna(also_no_winner)