from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.angazatech.co.ke/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

match = soup.div

print(match)
# print(soup.prettify())

# divs = soup.find_all('div', { "class " : "pricing" })

# print(divs)

# for div in divs:
#     print(div.string)

# divs = soup.find_all(“div”, {‘class’ : ‘row’})

# print(divs)

# for div in divs:
#     divs2 = div.find_all("div", class_="views-field views-field-field-reference-review-ent-prod result-title")
#     for div in divs2:
#         strongs = div.find_all("strong", class_="field-content")
#         for strong in strongs:
#             aa = strong.find_all("a")
#             for a in aa:
#                 print(a.text)
