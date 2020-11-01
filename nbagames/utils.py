from datetime import date, timedelta
# import sys
# sys.path.append("..")

# returns the difference between todays date and days back/foward desired 
# change function name
def scheduleDate(dayDiff):
    queryDate = date.today() + timedelta(days=dayDiff)
    return queryDate.strftime("%Y%m%d") 

def formatStringTabs(str):
    # print games with a box score
    if len(str) > 7:
        return str + "\t"
    elif len(str) <= 7:
        return str + "\t\t"
    else:
        return str

# Responsible for printing out games in a nice format
def printMachine(games):
    print("-------------------------------------------------------------")
    for game in games:

        if isinstance(game.spread, list):
            game.total = "\t".join(game.total)
            game.spread = "\t".join(game.spread)

        print(f"{formatStringTabs(game.gameTime)}\n{formatStringTabs(game.awayTeam)}{game.total}\n{formatStringTabs(game.homeTeam)}{game.spread}")
        print("-------------------------------------------------------------")
