# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list
# and returns (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search.


def wyszukaj_z_listy(lista, liczba):
    if liczba in lista:
        return True
    else:
        return False

def binarnie_wyszukaj(lista, liczba):
    if len(lista) == 1:
        if lista[0] == liczba:
            # print(lista[0])
            print("True")
        else:
            # print(lista[0])
            print("False")
    else:
        polowa = int(len(lista)/2)
        podzial = lista[polowa]
        # print(lista)
        # print(polowa)
        if podzial <= liczba:
            binarnie_wyszukaj(lista[polowa:], liczba)
        else:
            binarnie_wyszukaj(lista[:polowa], liczba)

lista_testowa = [0, 2, 4, 5, 7, 11, 23, 150,1983,222000]
print(wyszukaj_z_listy(lista_testowa, 5))
print(wyszukaj_z_listy(lista_testowa, 23))
print(wyszukaj_z_listy(lista_testowa, 25))
print("************")
binarnie_wyszukaj(lista_testowa, 3)
