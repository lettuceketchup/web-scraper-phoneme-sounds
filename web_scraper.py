import requests
import pprint
from bs4 import BeautifulSoup

phonemes = ['p', 'm', 'k', 'ɖ', 'j', 'ʈ', 'b', 's', 'ɡ']
URL = 'https://phoible.org/parameters'
page = requests.get(URL)

pp = pprint.PrettyPrinter(indent=4)

soup = BeautifulSoup(page.content, 'html.parser')

# pp.pprint(soup)

table = soup.find(id='Segments')
tbody = table.find('tbody')
rows = tbody.find_all('tr')
# print(table.prettify())
print(rows)

