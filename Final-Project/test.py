# File created by Abdullah Anwar 

# Imports the libraries needed for this program
# Beautiful Soup is 
from bs4 import BeautifulSoup
import requests
import pandas as pd

page_to_scrape = requests.get("https://www.espn.com/soccer/stats/_/league/ENG.1/season/2017/english-premier-league")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
goals = soup.findAll("td", attrs={"class":"tar"})
scorers = soup.findAll("a",attrs={"class":"AnchorLink"})
titles = soup.find("header", attrs={"class:db Site__Header__Wrapper sticky top-0"})

# Remove the element if found
if titles:
    titles.extract()

data = []
for i in range(len(goals)):
    scorer = scorers[i].text
    goal = goals[i].text
    data.append([scorer, goal])

df = pd.DataFrame(data, columns=["Scorer", "Goals"])
print(df)






























# pulls standings/stats from website

# url = 'https://www.espn.com/soccer/stats/_/league/ENG.1/season/2017/english-premier-league'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# # defines the hit stats that are pulled from the website
# Hits = soup.findAll("td", attrs={"data-stat":"H"})
# # Defines the at bats and what part of the website is at bats
# AtBats = soup.findAll("td", attrs={"data-stat":"AB"})
# # Defines the games and what part of the website is games
# Games = soup.findAll("td", attrs={"data-stat":"G"})
# # Defines the batting average and what part of the website is batting average
# BattingAverage = soup.findAll("td", attrs={"data-stat":"batting_avg"})
# # a loop that will print the stats of the certain categories from the website
# for i in range(len(Hits)):
#     print(Hits[i].text + " Hits " + AtBats[i].text + " AtBats " + Games[i].text + " Games " + BattingAverage[i].text + " BattingAverage ")]