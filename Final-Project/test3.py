
import pandas as pd
from bs4 import BeautifulSoup
import requests

base_url = "https://www.bbc.com/sport/football/world-cup/scores-fixtures/2022-11-20"
start_date = "11-20-2022"
end_date = "12-18-2022"

tournament_dates = pd.date_range(start_date, end_date)
# print(tournament_dates)

for dt in tournament_dates[:5]:
    print(f"{base_url}/{dt.date()}")

urls = [f"{base_url}/{dt.date()}" for dt in tournament_dates]
response = requests.get(urls[0])
response.text

soup = BeautifulSoup(response.text, 'html.parser')

# fixtures = soup.find_all('article',{'class':'sp-c-fixture'})
fixtures = soup.findAll("td", attrs={"class":"sp-c-fixture"})

home = fixtures[0].select_one('.sp-c-fixture__team-name--home .sp-c-fixture__team-name-trunc').text




# home = fixtures[0].select_one('.sp-c-fixture__team-name sp-c-fixture__team-name--home').text 
away = fixtures[0].select_one('.sp-c-fixture__team-name--away .sp-c-fixture__team-name-trunc').text
# away = fixtures[0].select_one('.sp-c-fixture__team-name.sp-c-fixture__team-name-away').text 
home_goals = fixtures[0].select_one('.sp-c-fixture__number--home').text
away_goals = fixtures[0].select_one('.sp-c-fixture__number--away').text

def show_result(home, home_goals, away, away_goals) -> str:
    return f"{home}  {home_goals}  -  {away}  {away_goals}"

show_result(home, home_goals, away, away_goals)