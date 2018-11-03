# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

numer = int(input("Podaj numer:"))

if numer % 2 == 0:
    print("Parzysta!")
    if numer % 4 == 0:
        print("Dodatkowo podzielna przez 4!")
else:
    print("Nieparzysta!")

numer2 = int(input("Podaj numer do podzielenia:"))
numer3 = int(input("Przez co dzielić:"))

if numer2 % numer3 == 0:
    print("Dzielą się bez reszty")
else:
    print("Nie dzielą się bez reszty")

