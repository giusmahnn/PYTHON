from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup


internalLinks = set()
externalLinks = set()

def getAllExternalLinks(url):
    html = urlopen(url)
    domain = '{}://{}'.format(urlparse(url).scheme,
                              urlparse(url).netloc)
    
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            if domain in href and href not in internalLinks:
                internalLinks.add(href)
                print('Internal Link: {}'.format(href))
            elif 'http' in href and domain not in href and href not in externalLinks:
                externalLinks.add(href)
                print('External Link: {}'.format(href))


internalLinks.add('http://nba.com')
getAllExternalLinks('http://nba.com')