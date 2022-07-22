# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 19:51:53 2022

@author: PC
"""
from bs4 import BeautifulSoup
import requests

url = "https://www.saes.escom.ipn.mx/"
text = requests.get(url).text
soup = BeautifulSoup(text, 'html5lib')
fields = [entry 
          for entry in soup('input')]
print(fields)
