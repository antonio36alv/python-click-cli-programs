from PyInquirer import prompt, print_json
from datetime import datetime

def fuckthis():
    print("fuck this")

def createDateTime():
    # HH:MMa/p
    # prompt for time input
    time = input("Enter a time pls: ")
    # find index that contains the semicolor
    semi = time.find(":")
    # digits until the semicolon will be the hrs
    hrs = time[0:semi]
    # digits after semicolon and before last digit are the minutes
    mm = time[semi + 1:len(time) - 1]
    # if the last digit is p
    if time[-1].lower() == "p":
        # hrs will increment by 12 hours due to military time
        hrs = int(hrs) + 12
    # get todays date
    today = datetime.today()
    # get input for the date
    dateOf = input("Enter the date of the event: ")
    # determine the length of the input
    lenDate = len(dateOf)
    # if it is single or double digit the day was entered
    if lenDate == 2 or lenDate == 1:
        # if dateOf's date is a past date or current days date
        if int(dateOf) <= today.day:
            try:
                # we have to increment the date
                dateOf = datetime(today.year, today.month + 1, int(dateOf), int(hrs), int(mm), 00)
            except ValueError:
                # if we increment date past 12 we musst simply increment the year and bring back months by 11
                dateOf = datetime(today.year + 1, today.month - 11, int(dateOf), int(hrs), int(mm), 00)
        else:
            # else we can save the date within the current month
            dateOf = datetime(today.year, today.month, int(dateOf), int(hrs), int(mm), 00)
    # data could be 4 digits MMDD
    elif lenDate == 4:
        # split date first two are months = mm
        mm = dateOf[0:2]
        # split date last two are days = dd
        dd = dateOf[-2]
        print(mm)
        print(dd)
        # if month already past this year we increment the year
        if int(mm) < today.month:
            # it is a month that has already passed
            dateOf = datetime(today.year + 1, int(mm), int(dd), int(hrs), int(mm), int(dd), 00)
        else:
            dateOf = datetime(today.year, int(mm), int(dd), int(hrs), int(mm), int(dd), 00)
    else:
        raise Exception(f"Error with your date input: {dateOf}")
    return dateOf

def chooseNote(notes):
    noteChoices = []
    for x in notes: 
        noteChoices.append(x["note"])
        # prompt for an answer as to which note will be removed
        # get the index of the note wanting to be deleted
        # index = notes.index(answer["removal"])
        # get the id

    answer = prompt({
        "type": "list",
        "name": "removal",
        "choices": noteChoices,
        "message": "Choose one to be deleted:"
    })

    for x in notes:
        if x["note"] == answer["removal"]:
            return x["_id"]

def chooseDetailIndex(details):

    detailChoices = []
    for x in details: 
        detailChoices.append(x)
    answer = prompt({
        "type": "list",
        "name": "removal",
        "choices": detailChoices,
        "message": "Choose one to be deleted:"
    })

    return details.index(answer["removal"]) 

def printMachine(data, printCon):
    # for each in data
    if len(data) > 0:
        print(data[0]["status"])
    for index, x in enumerate(data, start=1):
        # get the note, bulletPoint, and determine maxLen of details
        note = x["note"]
        bulletPoint = x["bulletPoint"]
        maxLen = len(x["details"])
        # print 
        print(f"{index}:\t{note}")    
        print(f"\t***{bulletPoint}**")
        print("______________________________________")
        if maxLen > 0 and not printCon:
            print("\tDetails")
            for i in x["details"]:
                print(f"{i}")

def fillings():
    note = input("Enter the note: ")
    bulletPoint = input("Enter a highlight/bullet point: ")

    details = []
    newDetail = input("Enter a detail or just hit enter to quit: ")
    while(newDetail != ""):
        details.append(newDetail)
        newDetail = input("Enter a detail or just hit enter to quit: ")
    return { "note": note, "bulletPoint": bulletPoint, "details": details }
