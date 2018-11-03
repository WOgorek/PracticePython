# In this exercise, the task is to write a function
# that picks a random word from a list of words from the SOWPODS dictionary.
# Download this file and save it in the same directory as your Python code.
# This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
# Each line in the file contains a single word.
#
# Hint: use the Python random library for picking a random word.

import random


with open('sowpods.txt', 'r') as open_file:
    line = random.choice(open_file.readlines())
    print( str(line))
