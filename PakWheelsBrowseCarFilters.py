import requests
from bs4 import BeautifulSoup
import csv
from os import system

filters = {}
filterList = []
filename = 'BrowseCarFilters.csv'

system('clear')
print("\t\t\t\tGetting web content from source ...")
page = requests.get("https://www.pakwheels.com/")
soup = BeautifulSoup(page.content, 'html5lib')

filters['Categories'] = soup.find('div', {'id': 'browesCTGSlider'})
filters['Make'] = soup.find('div', {'id': 'browesMKSlider'})
filters['Model'] = soup.find('div', {'id': 'browesMDSlider'})
filters['Body Type'] = soup.find('div', {'id': 'browesBTSlider'})
filters['City'] = soup.find('div', {'id': 'browesCTSlider'})

print("\t\t\t\tArranging web content ...")
for key in filters:
    for f in filters[key].findAll('li', attrs = {'class': 'col-sm-2'}):
        filterDetails = {}
        filterDetails['Filter Type'] = key

        if f.a.span is not None:
            filterDetails['Filter Name'] = f.a.span.text.strip()
        if f.span is not None:
            filterDetails['Filter Name'] = f.span.text.strip()
        if f.a.text is not None:
            filterDetails['Filter Name'] = f.a.text.strip()

        if f.img == None:
            filterDetails['Logo'] = ''
        else:
            filterDetails['Logo'] = f.img['src']

        filterDetails['Url'] = 'https://www.pakwheels.com' + f.a['href']
        filterList.append(filterDetails)

print("\t\t\t\tSaving into file ...")
with open(filename, 'w') as f:
    w = csv.DictWriter(f,['Filter Type','Filter Name','Url', 'Logo'])
    w.writeheader()
    for filter in filterList:
        w.writerow(filter)

print("\t\t\t\tWeb content scrapped successfully ...!")
