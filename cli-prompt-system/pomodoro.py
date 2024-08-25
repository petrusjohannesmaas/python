import json
import os

os.chdir("models")
with open("test.json", "r") as file:
    data = json.load(file)
    print(data[""])