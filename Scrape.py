import requests
from bs4 import BeautifulSoup
list = []
list_1 = []
result = requests.get('https://currencykart.com/live-rates')
#print(result.status_code)
#print(result.headers)

src = result.content
soup = BeautifulSoup(src,'html.parser')
#print(soup.prettify)
div_1 = soup.find(id = 'refresh_div')
elem = soup.find_all("div",{"class":"table-responsive"})
#for i in elem:
    #print(i.contents)

title = soup.title
#print(title)
#print(type(title.string))

para = soup.find_all('p')
#print(para)


anchor = soup.find_all('a')
#print(anchor)
#for link in anchor:#
    #print(link.get("href"))

#print(soup.find('table')['class'])
#print(soup.find_all('table',class_='table'))
#print(soup.find('table').get_text())

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup , features="html5lib")
#print(type(soup2.p.string))

#div = soup.find(id = 'select_rate_alert_currency')
div = soup.select('td:nth-child(1)')
for item in div:
   list.append(item.text)

#for item in div.parents:
   # print(item.name)

#print(div.next_sibling.next_sibling)

#print(div.previous_sibling.previous_sibling)
rates = soup.select('td~ td+ td')
for rate in rates:
    list_1.append(rate.text)
