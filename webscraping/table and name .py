### This code prints out the the data on a page on NBA site
# It prints out the table names(columns) and it's table content
# It is also wrapped around a try and except function to handle errors

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

try:
    url = 'https://www.nba.com/players'
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    table = soup.find('table').children

    joined = ' '.join([name.get_text() for name in table])
    print(joined)

except HTTPError as e:
    print('error')
except URLError as e:
    print('Network error')
