# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

slowo = input("Podaj slowo: ")

if slowo == slowo[::-1]:
    print("PALINDROM")
else:
    print("nie PALINDROM")
