# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000,
# and the other .txt file has a list of happy numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
# The explanation is easier with an example, which I will describe below.)

prime = []
happy = []

with open('primenumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        prime.append(int(line))
        line = open_file.readline()

with open('happynumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        happy.append(int(line))
        line = open_file.readline()

for liczba in prime:
    if liczba in happy:
        print("Prime and happy: {}".format(liczba))
    else:
        print("Only Prime: {}".format(liczba))
