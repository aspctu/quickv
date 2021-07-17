from replit import db
from replit.database.database import ObservedList

def checkIsList(value):
    # Replit's internal implementaion of this list is actually
    # a ObservedList
    return type(value) == ObservedList

def checkKeyExists(key):
    # Check to see if the key exists in the DB
    return key in db.keys()