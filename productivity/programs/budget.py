import os
import json
import couchdb
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

print("This is an Expenses module that has to be integrated with the Daily Report.")


class Item:
    def __init__(self, number, price, description):
        self.number = number
        self.description = description
        self.price = float(price)  # Convert price to float for accurate summation


todays_items = []
item_count = 1
total_in_zar = 0

while True:
    describe = input("Describe your purchase: ")
    price = input("What is the price? (rounded up to the nearest ZAR): ")
    item = Item(item_count, price, describe)
    todays_items.append(item)
    total_in_zar += item.price  # Add price to total_in_zar
    item_count += 1

    more = input(
        "Do you want to add another item? [Type anything, or 'no' to finish]: "
    ).lower()
    if more == "no":
        break

# Convert items to dictionary format
items_dict = [
    {"number": item.number, "description": item.description, "price": item.price}
    for item in todays_items
]

# Create the document with total_in_zar
doc = {
    "items": items_dict,
    "date": datetime.now().strftime("%Y-%m-%d"),
    "total_in_zar": total_in_zar,
}

"""Closing message"""
print("Here is your expense report:")
for item in todays_items:
    print(f"{item.number}. Description: {item.description}, Price: {item.price}")

""" Connect to the database """
c = os.getenv("CONNECTION_STRING")
couch = couchdb.Server(c)
db = couch["expenses"]

""" Make a new entry """
db.save(doc)

print("Document saved to CouchDB")
