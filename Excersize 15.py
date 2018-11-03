# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
#
#     My name is Michele
# Then I would see the string:
#
# Michele is name My
# shown back to me.


def odwroc_kolejnosc(string):
    lista_slow = string.split(" ")
    lista_odwrotna = lista_slow[::-1]
    lancuch_odwrocony = " ".join(lista_odwrotna)
    return lancuch_odwrocony


a = input("Podaj lancuch:")
print(odwroc_kolejnosc(a))
