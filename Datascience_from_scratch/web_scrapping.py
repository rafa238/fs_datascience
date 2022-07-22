# -*- coding: utf-8 -*-
"""
In this example we will see the mentions of data in press-releases 
from congress enterpraises
"""

from bs4 import BeautifulSoup
import requests
import re
from typing import Dict, Set

#first we will get the represents web pages
url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")
all_urls = [a['href']
            for a in soup('a')
            if a.has_attr('href')]
#print(all_urls)


#urls start with http, https and end with .hose.gov and test it
regex = r"^https?://.*\.house\.gov/?$"
assert re.match(regex, "http://rafa.house.gov")
assert re.match(regex, "https://rafa.house.gov/")

good_urls = [url 
             for url in all_urls
             if re.match(regex, url)]
print(len(good_urls))

#lets delete duplicates
good_urls = list(set(good_urls))



#lets get press-releases
press_releases : Dict[str, Set[str]] = {}

for house_url in good_urls:
    html = requests.get(house_url).text
    soup = BeautifulSoup(html, 'html5lib')
    pr_links = [a['href'] 
                for a in soup('a') 
                if 'press releases' in a.text.lower()]
    print(f"{house_url}: {pr_links}")
    press_releases[house_url] = pr_links

#now that we have press-releases of each house, we will find the word data

def paragraph_mentions(text: str, keyword: str) -> bool:
    """
    Returns True if a <p> inside the text mentions {keyword}
    """
    soup = BeautifulSoup(text, 'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]

    return any(keyword.lower() in paragraph.lower()
               for paragraph in paragraphs)
    

for house_url, pr_links in press_releases.items():
        for pr_link in pr_links:
            url = f"{house_url}/{pr_link}"
            text = requests.get(url).text
    
            if paragraph_mentions(text, 'data'):
                print(f"{house_url}")
                break  # done with this house_url
#print(press_releases.items())

