import requests
from bs4 import BeautifulSoup

url = 'https://mfd.ru/currency/?currency=USD'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', attrs={"class":{"mfd-u","mfd-d"}})
tags = soup.find_all('td')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    print('\n')

