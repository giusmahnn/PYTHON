# I scrapped two different sites for blog post 
# I obtained the title, body, time and url



import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title,time, body):
        self.url = url
        self.title = title
        self.time = time
        self.body = body
def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')
def scrapeMedium(url):
    bs = getPage(url)
    title = bs.find("h1").text
    time = bs.find('span')
    lines = bs.find_all("p")
    body = '\n'.join([line.text for line in lines])
    return Content(url, title,time, body)
def scrapeNBA(url):
    bs = getPage(url)
    title = bs.find("h1").text
    time = bs.find("time", class_="ArticleHeader_ahDate__J3fwr").text
    body = ''
    for p in bs.find_all('p'):
        body += p.text.strip() + '\n'
    return Content(url, title, time, body)

url = 'https://www.nba.com/news/10-must-watch-1990s-nba-finals-games'
content = scrapeNBA(url)
print('Title: {}'.format(content.title))
print('Time: {}'.format(content.time))
print('URL: {}\n'.format(content.url))
print(content.body)


url = 'https://medium.com/@mikldd/data-salaries-at-faang-companies-in-2022-29d5b56b2428'
content = scrapeMedium(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)