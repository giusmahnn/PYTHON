# import our modules

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# we create a function to get the image tag
def getImage(url):
    # we define our html variable
    try:
        html = urlopen(url)

    # we anticipate for errors to stop our program from breaking
    except HTTPError as e:
        print('Server could not be found')

    except URLError as e:
        print('url error')

    # we set our soup to read from the html variable and set the tag to find
    try:
        soup = BeautifulSoup(html.read(), 'html.parser')
        image = soup.body.img     # we can substitue the other tags and see if it works

    # we set an attribute error incase the tag is not found
    except AttributeError as e:
        return None
    return image

# set our function link
image = getImage('https://www.nba.com')


if image == None:
    print('img not found')
else:
    print(image)
