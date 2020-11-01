# Contains web scraping functionality
from bs4 import BeautifulSoup
# Get all divs of games
# def getGameDivs():


# Contains pre-determined sets for scraping
# A set in this case 

# Game status will look for either: time game starts,
# time left, postgame (final)
gameStatus = [{ "tag": "span", "searchCondition": "game-status pregame-date"},
              { "tag": "div", "searchCondition": "game-status emphasis"},
              { "tag": "div", "searchCondition": "game-status postgame"}]

gamblingStuff = [{"tag": "td", "searchCondition": "in-progress-odds in-progress-odds-total"},
                 {"tag": "td", "searchCondition": "in-progress-odds in-progress-odds-home"}]

def complexScrape(game, detailWanted):

    # while the element we want is not found/none
    # print(game)
    if detailWanted == "time":
        for x in range(len(gameStatus)):
        # loop again
            # print(gameStatus[x]["tag"])
            # print(gameStatus[x]["searchCondition"])
            data = game.find(gameStatus[x]["tag"], gameStatus[x]["searchCondition"])
            if data is not None:
                data = data.text.strip()
                break
    else:
        control = 0 if detailWanted == "overUnder" else 1
        data = game.find(gamblingStuff[control]["tag"], gamblingStuff[control]["searchCondition"])
        if data is None:
            data = "-"
        else:
            data = data.text.strip()
    return data

def stripText(arr):
    for x in range(len(arr)):
        arr[x] = arr[x].text.strip()
    return arr

def boxScore(game):

    tableRows = game.find_all("tr")
    awayTeamScores = stripText(tableRows[1].find_all("td"))
    homeTeamScores = stripText(tableRows[2].find_all("td"))
    del awayTeamScores[0]
    del homeTeamScores[0]
    return [awayTeamScores, homeTeamScores]
