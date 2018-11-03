# Take the code from the How To Decode A Website exercise
# (if you didn’t do it or just want to play with some different code, use the code from the solution),
# and instead of printing the results to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.

import requests
import bs4

url = "https://www.nytimes.com/"

strona = requests.get(url)
tresc = strona.text
soup = bs4.BeautifulSoup(tresc, 'html.parser')
artykuly = soup.find_all('article')

with open("test2.txt", 'a') as plik:
    for artykul in artykuly:
        #print(''.join(artykul.findAll(text=True)))
        plik.write(''.join(artykul.findAll(text=True)))