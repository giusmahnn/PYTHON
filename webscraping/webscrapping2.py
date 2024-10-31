from bs4 import BeautifulSoup
import requests


url = "https://www.jumia.com.ng/catalog/?q=tv"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
names = soup.find_all('h3', class_='name')
prices = soup.find_all('div', class_='prc')

with open('name', 'w', encoding="utf-8") as f:
    if response.status_code == 200:
        for name, price in zip(names, prices):
            f.write(f"Product Name: {name.text.strip()}\n")
            f.write(f"Product Price: {price.text.strip()}\n")
            f.write("---------------------------------\n")
        print("finished...")
    else:
        print(f"Error getting the webpage: {response.status_code}")