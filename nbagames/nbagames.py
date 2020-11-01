# Script that when called upon will display games avaiable to stream
import click
import re
import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("..")

import scraper
import game_obj
import utils

# pass in a number to represent the day difference between today
# and the day's schedule being requested
# -1 yesterday, 0 today, 1 tomorrow
@click.command()
@click.option("-d", default=0, show_default=True, help="Fetches data from previous schedule id\nExamples\t-1 previous day schedule\n\t1 for tomorrow\n\tNo input needed for today")
def cli(d):
    dayDiff = d
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    URL = "https://www.cbssports.com/nba/scoreboard/{}/".format(utils.scheduleDate(dayDiff))
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    
    games = []
    
    gameDivs = soup.find_all("div", class_="live-update")
    
    for game in gameDivs:
        
        gameTime = scraper.complexScrape(game, "time")
        teamNames = game.find_all("a", class_="team helper-team-name")
        if bool(re.match(r"\b((2[0-2]|0?[1-9]):([0-5][0-9])([AaPp][Mm]))", gameTime)) == False:
            boxScores = scraper.boxScore(game)
            if len(boxScores[0]) > 5:
                gameTime += "\tQ1\tQ2\tQ3\tQ4\tOT"
            else:
                gameTime += "\t\tQ1\tQ2\tQ3\tQ4"
            games.append(game_obj.Game(gameTime, teamNames[0].text.strip(), teamNames[1].text.strip(), boxScores[0], boxScores[1]))
        else:
            overUnder = scraper.complexScrape(game, "overUnder")
            spread = overUnder if overUnder == "-" else scraper.complexScrape(game, "spread")
        # add to our list of game objects 
            games.append(game_obj.Game(gameTime, teamNames[0].text.strip(), teamNames[1].text.strip(), overUnder, spread))
    # loop if finished gathering data, print it
    utils.printMachine(games)

if __name__ == "__main__":
    cli()