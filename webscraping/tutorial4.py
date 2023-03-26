import requests
from bs4 import BeautifulSoup
import re
pages = set()

def getLinks(pageUrl):
    global pages
    html = requests.get('http://nba.com{}'.format(pageUrl))
    soup = BeautifulSoup(html.content, 'html.parser')

    try:
        print(soup.h1.get_text())
        print(soup.find(id='__next').find_all('p')[0])
        print(soup.find(id='ca-edit').find('span')
              .find('a').attrs['href'])
        
    except:
        print('This page is missing someting')


    for link in soup.find_all('a', href=re.compile('^/')):
        if 'href' in link.attrs and link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print('-'*20)
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)

getLinks('')