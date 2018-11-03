# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

import datetime
name = input("Podaj imie: ")
age = int(input("Podaj wiek:"))
ile_powtorzen = int(input("Ile powtorzen?:"))

rok_obecny = int(datetime.datetime.now().year)
rok_urodzin = rok_obecny - age
urodziny100 = rok_urodzin + 100

for i in range(ile_powtorzen):
    print("{}. Drogi {} , Twoje setne urodziny będą w : {}".format(i+1,name,urodziny100 ))