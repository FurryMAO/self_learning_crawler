import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'  # Wikipedia的主页
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
links = [a['href'] for a in soup.find_all('a', href=True)]

for link in links:
    print(link)