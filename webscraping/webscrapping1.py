import requests
from bs4 import BeautifulSoup


r =  requests.get('https://www.jumia.com.ng/nexus-32-inches-fhd-tv-h620bsa-black-2-years-warranty-103636244.html')


soup = BeautifulSoup(r.text, 'html.parser')
tag = soup.find('h1', class_ = '-fs20 -pts -pbxs')
price = soup.find('div', class_ ='df -i-ctr -fw-w')
print(tag.text)
print(price.text)
descriptions = soup.find_all('font', face = 'helvetica, arial, sans-serif')
for desc in descriptions:
    print(desc.text)

