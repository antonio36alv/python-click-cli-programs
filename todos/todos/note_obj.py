from mongoengine import *
import datetime

class Note(Document):
    # either upcoming, asap, or todo
    """
    upcoming = something that is a planned event usually
               or simply something that cannot be done until
               whenever the given document cannot be completed
    asap = do today hopefully, rollover untill completed

    todo = meets the criteria for obviously not getting done today
            or even tomorrow
    purpose of all these statuses is only certain statuses
    """
    status = StringField(required = True)
    # as simple as it sounds the actual note
    note = StringField(required = True)
    # bullet point - important detail will show up when no details are shown
    bulletPoint = StringField()
    # details are shown only when details are asked for
    details = ListField(StringField())
    # date will either be present date if asap or todo
    # date will be the day of the event + time for upcoming
    dateTime = DateTimeField(default = datetime.datetime.now)