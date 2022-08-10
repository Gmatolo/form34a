
# Import libraries
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader


reader = PdfReader("./forms/test_form_1.pdf")
# with open("./forms/test.pdf", "rb") as fh
pages = reader.pages[0]
print(pages.extract_text())


url = "https://forms.iebc.or.ke/#/"

# Requests URL and get response object
response = requests.get(url)

# Parse response obtained
soup = BeautifulSoup(response.text, 'html.parser')