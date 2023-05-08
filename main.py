# File Created by Thomas Trombatore
# works cited: https://www.youtube.com/watch?v=Nt7WJa2iu0s
# https://www.youtube.com/watch?v=QhD015WUMxE

# imports library requests
import requests
from bs4 import BeautifulSoup 

# pulls standings/stats from website
url = 'https://www.baseball-reference.com/leagues/majors/2023.shtml'
response = requests.get(url)

# adds in html parser which assists with webscrapin
soup = BeautifulSoup(response.text, 'html.parser')


# defines the hit stats that are pulled from the website
Hits = soup.findAll("td", attrs={"data-stat":"H"})

# Defines the at bats and what part of the website is at bats
AtBats = soup.findAll("td", attrs={"data-stat":"AB"})


# Defines the batting average and what part of the website is batting average
BattingAverage = soup.findAll("td", attrs={"data-stat":"batting_avg"})


# a loop that will print the stats of the certain categories from the website
for i in range(len(Hits)):
    print(Hits[i].text + " Hits " + AtBats[i].text + " AtBats " + BattingAverage[i].text 
          + " BattingAverage ") 

# loop through the hits and at-bats data to calculate the predicted batting average for each player  
for i in range(len(Hits)):
    hits = int(Hits[i].text)
    at_bats = int(AtBats[i].text)
    if at_bats > 0:
        predicted_batting_average = hits / at_bats
        print(f"Predicted batting average for player {i+1}: {predicted_batting_average:.3f}")
    else:
        print(f"No at-bats for player {i+1}")



# Initializes the variables to keep track of the index of the player and the player batting average
highest_batting_average = 0
highest_batting_average_index = 0

# create a list to store the names of the players
player_names = [name.text for name in Names]

# loop through the hits and at-bats data to calculate the predicted batting average for each player
for i in range(len(Hits)):
    hits = int(Hits[i].text)
    at_bats = int(AtBats[i].text)
    if at_bats > 0:
        predicted_batting_average = hits / at_bats
        if predicted_batting_average > highest_batting_average:
            highest_batting_average = predicted_batting_average
            highest_batting_average_index = i

# print out the name of the player with the highest predicted batting average
print(f"{player_names[highest_batting_average_index]} has the highest predicted batting average of {highest_batting_average:.3f}")