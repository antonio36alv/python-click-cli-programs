import utils

def test_addNote():

    data = [
            { "id": 2, "note": "go to the bank"},
            { "id": 7, "note": "die"}
            ]
    
    newNoteText = "karate guitar lessons"
    newNoteDetails = ["\tGuitares must be gluten free", "\teat bernies chicken", "\tlet the boy die"]

    assert utils.addNote(data) == [
            { "id": 1, "note": "go to the bank"},
            { "id": 2, "note": "die"},
            { ""}