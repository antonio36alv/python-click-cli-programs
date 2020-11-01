from mongoengine import *
from .note_obj import Note

connect("notes_cli", host="localhost", port=27017)

def findNoteById(id):
    return Note.objects(id = id).as_pymongo()

def saveNote(note):
    note.save()

def removeNote(id):
    note = Note.objects(id = id)
    note.delete()

def findByStatus(status):
    return Note.objects(status = status).as_pymongo()

def updateNoteText(id, newNote):
    note = Note.objects(id = id)
    note.modify(note = newNote)

def updateNoteBullet(id, newBulletPoint):
    note = Note.objects(id = id)
    note.modify(bulletPoint = newBulletPoint)

def updateNoteDetails(id, details):
    note = Note.objects(id = id)
    note.modify(details = details)

# if __name__ == '__main__':
#     _test()
