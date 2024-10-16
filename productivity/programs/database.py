import os

import couchdb
from dotenv import load_dotenv

load_dotenv()

""" Connect to the database """

c = os.getenv("CONNECTION_STRING")
couch = couchdb.Server(c)
db = couch["daily_reports"]

""" Make a new entry """

doc = {}
db.save(doc)

""" Get a document by ID """

# entry = db["1"]
# print(entry)
