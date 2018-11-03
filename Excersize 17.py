# Use the BeautifulSoup and requests Python packages to print out
# a list of all the article titles on the New York Times homepage.

import requests
import bs4

url = "https://www.nytimes.com/"

strona = requests.get(url)


tresc = strona.text

soup = bs4.BeautifulSoup(tresc, 'html.parser')

artykuly = soup.find_all('article')

for artykul in artykuly:
    print(''.join(artykul.findAll(text=True)))






