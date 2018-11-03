# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes care of for us.
# All you need is some variables and if statements!


def maksimum(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)


maksimum(1, 2, 3)
maksimum(5, 123, 4)
maksimum(2, 7, 7)
maksimum(8, 1, 8)
maksimum(4, 3, 8)
maksimum(7, 11, 1000)
maksimum(0, 0, 0)

