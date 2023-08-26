from pymongo.collection import Collection

from .core import Database

__ALL__ = ['user_collection', 'teams_collection']

# get and import collections for other apps from here

db = Database()
user_collection: Collection = db.collections['users']
teams_collection: Collection = db.collections['teams']
