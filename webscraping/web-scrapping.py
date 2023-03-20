# this code scraps the first page on the NBA  power-ranking sites

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.nba.com/news/category/power-rankings').text
soup = BeautifulSoup(page, 'html.parser')
players = soup.find_all('p')

for player in players:
    name = player.text

    print(name)
