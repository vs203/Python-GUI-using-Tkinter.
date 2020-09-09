import requests
from bs4 import BeautifulSoup
list = []
list_1 = []
result = requests.get('https://currencykart.com/live-rates')


src = result.content
soup = BeautifulSoup(src,'html.parser')

div_1 = soup.find(id = 'refresh_div')
elem = soup.find_all("div",{"class":"table-responsive"})

title = soup.title
anchor = soup.find_all('a')

div = soup.select('td:nth-child(1)')
for item in div:
   list.append(item.text)


rates = soup.select('td~ td+ td')
for rate in rates:
    list_1.append(rate.text)
