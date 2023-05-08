import requests
from bs4 import BeautifulSoup
url = 'https://www.espn.com/soccer/stats/_/league/ENG.1/season/2017/english-premier-league'
response = requests.get(url)
soup = BeautifulSoup(resposne.text, 'html.parser')
for anchor_tag in soup.find_all('a'):
    print(anchor_tag.get('href'))