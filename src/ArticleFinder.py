from os import readlink
from typing import Counter
import requests
from bs4 import BeautifulSoup
class Finder():
    def findArticle(self, crypto):
        url = "https://www.google.com/search?q=site%3Acoinmarketcap.com+alexandria+article+" + crypto
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        listOfLinks = {}
        count = 0 
        for link in soup.find_all('a'):
            href = link.get('href')
            if "https://coinmarketcap.com/" in href:
                realLink = "https://www.google.com"+href
                req = requests.get(realLink)
                moresoup = BeautifulSoup(req.content, 'html.parser')
                article = moresoup.find('article')
                try:
                    text = article.get_text()
                    listOfLinks[realLink] = text
                    count = count + 1
                except:
                    print("can't find")
                    pass
        return listOfLinks




