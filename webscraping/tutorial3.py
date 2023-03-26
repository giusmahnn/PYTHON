from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random




random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen('http://nba.com{}'.format(articleUrl))
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('div', {'id':'__next'}).find_all('a', href=re.compile('^/'))

links = getLinks('/player/2544/lebron-james')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)


