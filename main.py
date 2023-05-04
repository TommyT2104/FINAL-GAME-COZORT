# File Created by Thomas Trombatore
# works cited: https://www.youtube.com/watch?v=Nt7WJa2iu0s

# imports library requests
import requests
from bs4 import BeautifulSoup 

# pulls standings/stats from website
url = 'https://www.baseball-reference.com/leagues/majors/2023.shtml'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


# defines the hit stats that are pulled from the website
Hits = soup.findAll("td", attrs={"data-stat":"H"})

# Defines the at bats and what part of the website is at bats
AtBats = soup.findAll("td", attrs={"data-stat":"AB"})

# Defines the games and what part of the website is games
Games = soup.findAll("td", attrs={"data-stat":"G"})

# Defines the batting average and what part of the website is batting average
BattingAverage = soup.findAll("td", attrs={"data-stat":"batting_avg"})





# a loop that will print the stats of the certain categories from the website
for i in range(len(Hits)):
    print(Hits[i].text + " Hits " + AtBats[i].text + " AtBats " + Games[i].text + " Games " + BattingAverage[i].text 
          + " BattingAverage ")