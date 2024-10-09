"""Class object definition the category of problem"""

import json
import jmespath


class Problem:
    data = ""

    def __init__(self):
        pass

    def load_data(self):
        """Extract JSON data from a specific file"""
        with open("tapie.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def case_1(self):
        """Find and print the category of problem called People"""
        q = jmespath.search("categories.People", self.data)
        people = json.dumps(q, indent=4)
        print("People: \n", people)

    def case_2(self):
        """Find and print the category of problem called Product"""
        q = jmespath.search("categories.Product", self.data)
        product = json.dumps(q, indent=4)
        print("Product: \n", product)

    def case_3(self):
        """Find and print the category of problem called Process"""
        q = jmespath.search("categories.Process", self.data)
        process = json.dumps(q, indent=4)
        print("Process: \n", process)

    # def case_4(self):
    #     """Koos"""
    #     print("4")

    def invalid(self):
        """User feedback on an invalid input"""
        print("Invalid input")
