# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def remove_dup(lista):
    zbior = set(lista)
    lista_nowa = list(zbior)
    return lista_nowa


def remove_dup2(lista):
    lista_nowa = []
    for pole in lista:
        if pole not in lista_nowa:
            lista_nowa.append(pole)
    return lista_nowa


lista_main = ["Adam", "Ewa", "Jacek", "Placek", "Placek", "Ewa", "Ewa", "Marysia"]

print(lista_main)
print(remove_dup(lista_main))
print(remove_dup2(lista_main))