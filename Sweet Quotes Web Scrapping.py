import requests
from bs4 import BeautifulSoup
import csv
from os import system

quotes = []
filename = 'sweetQuotes.csv'

system('clear')
print("\t\t\t\tGetting web content from source ...")
page = requests.get("http://www.values.com/inspirational-quotes")
soup = BeautifulSoup(page.content, 'html5lib')
quotesGrid = soup.find('div', attrs = { 'id': 'all_quotes'})
rows = quotesGrid.findAll('div', attrs = {'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'})

print("\t\t\t\tArranging web content ...")
for q in rows:
    quote = {}
    quote['theme'] = q.h5.text
    quote['image'] = q.a.img['src']
    quote['url'] = 'https://www.passiton.com' + q.a['href']
    quotes.append(quote)

print("\t\t\t\tSaving into file ...")
with open(filename, 'w') as f:
    w = csv.DictWriter(f,['theme','image','url'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

print("\t\t\t\tWeb content scrapped successfully ...!")
