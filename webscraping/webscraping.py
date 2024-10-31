from bs4 import BeautifulSoup


with open('web.html', 'r') as html:
    content = html.read()



soup = BeautifulSoup(content, 'html.parser')
names = soup.find_all('td', class_='name')
ages = soup.find_all('td', class_='age')
occupations = soup.find_all('td', class_='occupation')
for name, age, occupation in zip(names, ages, occupations):
    print(f"{name.text} is {age.text} and is also a {occupation.text}")

links = soup.find_all('a', class_='external-link')
for link in links:
    print(f"Link Text: {link.text}, URL: {link['href']}")

lists = soup.find_all('li')
for list in lists:
    print(list.text)