"""Koos"""

import json
import jmespath


class Problem:
    data = ""

    def __init__(self):
        pass

    # JSON EXTRACTION
    def load_data(self):
        """Koos"""
        with open("tapie.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def case_1(self):
        """Koos"""
        q = jmespath.search("categories.People", self.data)
        people = json.dumps(q, indent=4)
        print("People: \n", people)

    def case_2(self):
        """Koos"""
        q = jmespath.search("categories.Product", self.data)
        product = json.dumps(q, indent=4)
        print("Product: \n", product)

    def case_3(self):
        """Koos"""
        q = jmespath.search("categories.Process", self.data)
        process = json.dumps(q, indent=4)
        print("Process: \n", process)

    def case_4(self):
        """Koos"""
        print("4")

    def case_5(self):
        """Koos"""
        print("5")

    def invalid(self):
        """Koos"""
        print("Invalid input")
