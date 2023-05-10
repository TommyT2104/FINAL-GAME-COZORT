# File Created by Thomas Trombatore
# works cited: https://www.youtube.com/watch?v=Nt7WJa2iu0s
# https://www.youtube.com/watch?v=QhD015WUMxE
# https://www.codecademy.com/resources/blog/web-scraping-python-beautiful-soup-mlb-stats/

# imports library requests
import requests
from bs4 import BeautifulSoup 
import pandas as pd

# pulls standings/stats from websites
url = 'https://www.baseball-reference.com/leagues/majors/2023.shtml'
response = requests.get(url)

# adds in html parser which assists with webscraping
soup = BeautifulSoup(response.text, 'html.parser')


# defines the name of each team
Name = soup.findAll("th", attrs={"data-stat":"team_name"})
# defines the hit stats that are pulled from the website
Hits = soup.findAll("td", attrs={"data-stat":"H"})
# Defines the at bats and what part of the website is at bats
AtBats = soup.findAll("td", attrs={"data-stat":"AB"})

# Defines the batting average and what part of the website is batting average
BattingAverage = soup.findAll("td", attrs={"data-stat":"batting_avg"})

# a loop that will print the stats of the certain categories from the website
for i in range(len(Hits)-1):
    print(Name[i].text + " " + Hits[i].text + " Hits " + AtBats[i].text + " AtBats " 
          + BattingAverage[i].text + " BattingAverage ") 
    
# initializes variables to keep track of batting average
highest_batting_average = 0
highest_batting_average_index = 0

# loops through data needed from the website to predict the average for each team
for i in range(len(Hits)):
    hits = int(Hits[i].text)
    at_bats = int(AtBats[i].text)
    if at_bats > 0:
        predicted_batting_average = hits / at_bats
        highest_batting_average = predicted_batting_average 
        highest_batting_average_index = i

# prints the team with the predicted highest batting average in the MLB
print(f"{Name[highest_batting_average_index].text} has the highest predicted batting average in the MLB of {highest_batting_average:.3f}")

