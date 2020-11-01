from mongoengine import *

class dbConnection(Document):
    """
    need a name for refrencing
    host
    username
    db_type = mongo/mysql, more to come maybe...

    password if mongo
    """
    name = StringField(required=True)
    command = StringField(required=True)
    db_type = StringField(required=True)
    description = StringField(required=True, min_length=20, max_length=400)