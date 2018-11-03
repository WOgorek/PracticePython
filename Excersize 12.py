# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#  and makes a new list of only the first and last elements of the given list.
#  For practice, write this code inside a function.

def first_and_last(lista):
    first = lista[0]
    last = lista[-1]
    wynik = []
    wynik.append(first)
    wynik.append(last)
    return wynik

a = [5, 10, 15, 20, 25]
print(first_and_last(a))
