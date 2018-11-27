import requests, json
from bs4 import BeautifulSoup, SoupStrainer
from random import *
import os

working_url = 'https://www.poetryfoundation.org/poems/43521/beowulf-old-english-version'

response = requests.get(working_url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
destination = open("old_english.txt", "w")
for temp in soup.find_all('div', class_='o-poem'):
    destination.write(temp.get_text() + '\n')

  
    

