from __future__ import print_function, unicode_literals
from mongoengine import *
from mongoengine.connection import disconnect
import click
from PyInquirer import prompt, print_json
from .note_obj import Note
from datetime import datetime
from .controller import *
from .utils import *
# from controller import *
# from .controller import findNoteById, saveNote, removeNote, findByStatus, updateNoteText, updateNoteBullet, updateNoteDetails
# from . import controller
# from .controller import *
# import controller
# from p_utils import *


@click.command()
@click.option("--quiet", is_flag=True, help="Turning on this flag, quites details")
@click.option("-v", is_flag=True, help="V is to intiate view, combine with n, t, f")
@click.option("-a", is_flag=True, help="Combine with V to view ASAP")
@click.option("-t", is_flag=True, help="Combine with V to view TODO")
@click.option("-u", is_flag=True, help="Combine with V to view UPCOMING")
@click.option("-c", is_flag=True, help="Create")
@click.option("-r", is_flag=True, help="Remove")
@click.option("-m", is_flag=True, help="Modify")
def cli(quiet, v, a, t, u, c, r, m):
    # saveNote({"bs": "its bs i did not hit her"})  
    # print(sch)
    if v:
        if a:
            printMachine(findByStatus("Asap"), quiet)
        if t:
            printMachine(findByStatus("Todo"), quiet)
        if u:
            printMachine(findByStatus("Upcoming"), quiet)
    else:
        answers = prompt({
            "type": "list",
            "name": "status",
            "choices": [ "Upcoming", "Todo", "Asap" ],
            "message": "Choose"
        })

        try:
            status = answers["status"]
        except KeyError:
            print("Error, aborting...")
            return
        if c:
            if status == "Upcoming":
                fillingsAnswers = fillings()
                dateOf = createDateTime()
                note = Note(status = status, note = fillingsAnswers["note"], bulletPoint = fillingsAnswers["bulletPoint"], details = fillingsAnswers["details"], dateTime = dateOf)
            elif status == "Todo" or status == "Asap":
                fillingsAnswers = fillings()
                note = Note(status = status, note = fillingsAnswers["note"], bulletPoint = fillingsAnswers["bulletPoint"], details = fillingsAnswers["details"])
            else:
                print("issue with your input")
                print(f"Said input: {status}")
            saveNote(note)
        elif r:
            # see all of that particular status before deleting
            printMachine(findByStatus(status), quiet)
            # init empty array for notes that will be displayed as options
            notes = []
            # get documents that match the status
            data = findByStatus(status)
            # create notes as options
            id = chooseNote(data)
            # send id to be removed
            removeNote(id)
        elif m:
            # find any doc that matches the status
            data = findByStatus(status)
            # get the users selection's id
            id = chooseNote(data)
            # get the one note in particular
            data = findNoteById(id)
            # ask for what kind of modification the would like to make, all listed in choices
            wantedMod = prompt({
                "type": "list",
                "name": "mod",
                "choices": ["Edit Note", "Edit Bullet Point", "Insert Detail", "Append Details", "Remove Details", "Edit Details"],
                "message": "What do you want to edit? "
            })

            if wantedMod["mod"] == "Edit Note":
                # allow user to enter new note text
                newNote = input("Enter the new note text: ")
                # if it is not emppty update the note
                if newNote != "":
                    updateNoteText(id, newNote)
                else:
                    print("Enterned nothing, now exiting")
            elif wantedMod["mod"] == "Edit Bullet Point":
                # print out the current bullet point
                print("Current: " + data[0]["bulletPoint"])
                # allow for input for new bullet point
                newBulletPoint = input("Enter the new bullet point: ")
                # as long as there is input take it and update the bulletPoint
                if newBulletPoint != "":
                    updateNoteBullet(id, newBulletPoint)
                else:
                    print("Enterned nothing, now exiting")
            else:
                details = data[0]["details"]
                # if there are any details print details header
                if len(details) > 0:
                    print("Current Details")
                # then print through all details
                for x in details:
                    print(x)
                # append details
                if wantedMod["mod"] == "Append Details":
                    # all for new input
                    newDetail = input("Enter a new detail: ")
                    # as long as it is not empty
                    while(newDetail != ""):
                        # append the new detail and prompt again
                        details.append(newDetail)
                        newDetail = input("Enter a new detail: ")
                # else it is remove, edit, or insert
                else:
                    # while user does confirm
                    while(click.confirm("Continue? ")):
                # TODO
                # insert to details 
                        # clear each loop
                        click.clear()
                        # loop through details and print with their index
                        for it, x in enumerate(details):
                            print(f"{it}: {x}")
                        # TODO
                        # maybe print new line here
                        # get index from choosen element
                        index = chooseDetailIndex(details)
                        # if we are removing
                        if wantedMod["mod"] == "Remove Details":
                            # pop from details
                            details.pop(index)
                        # else we are editing
                        elif wantedMod["mod"] == "Edit Details":
                            # enter new detail
                            newDetail = input("Enter new detail: ")
                            # re assign element to the new detail
                            details[index] = newDetail 
                # after all is said and done update the details
                updateNoteDetails(id, details)
    disconnect()


# if __name__ == "__main__":
#     cli()
