# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen.
# I have a .txt file for you, if you want to use it!
#
# Extra:
#
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
# and count how many of each “category” of each image there are.
# This text file is actually a list of files corresponding to the SUN database scene recognition database,
# and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file,
# it will be clear which part represents the scene category.
# To do this, you’re going to have to remember a bit about string parsing in Python 3.
# I talked a little bit about it in this post.

print(" NAME LIST: ")

imiona = dict()
with open('nameslist.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        if line in imiona:
            imiona[line] += 1
        else:
            imiona[line] = 1
        line = open_file.readline()
print(imiona)

print()
print("*" * 60)
print()
print("IMAGE SET:")

kategoria = dict()
with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        linia_podzielona = line.split("/")
        pojedyncza_kategoria = str(linia_podzielona[2])
        if pojedyncza_kategoria in kategoria:
            kategoria[pojedyncza_kategoria] += 1
        else:
            kategoria[pojedyncza_kategoria] = 1
        line = open_file.readline()
for kat, ile in kategoria.items():
    print(str(kat) + " : " + str(ile))
