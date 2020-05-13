import requests 
from bs4 import BeautifulSoup


URL = 'http://as.com/' 

page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())
