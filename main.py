
# Import libraries
import requests
from bs4 import BeautifulSoup
#from PyPDF2 import PdfReader


# reader = PdfReader("./forms/test_form_1.pdf")
# # with open("./forms/test.pdf", "rb") as fh
# pages = reader.pages[0]
# print(pages.extract_text())


url = "https://forms.iebc.or.ke/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
# Requests URL and get response object
response = requests.get(url, headers=headers)

print(url)

# Parse response obtained
soup = BeautifulSoup(response.text, 'lxml')

# print(soup)


app = soup.find('body')
print(app)
