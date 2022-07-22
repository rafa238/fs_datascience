# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:46:38 2022

@author: PC
"""

from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p') # or just soup.p
first_paragraph = soup.p['id'] #get the id from the tag
print(first_paragraph)

"""
How to get multiple tags
"""
important_paragraphs = soup.find_all('p') # or soup('p')
print(important_paragraphs)
important_paragraphs_with_ids = [p for p in soup('p') if p.get('id')]
print(important_paragraphs_with_ids)

important_class = soup('p', {'class': 'important'})
print(important_class)
important_class = [p for p in soup('p')
                     if 'important' in p.get('class', [])]
print(important_class)