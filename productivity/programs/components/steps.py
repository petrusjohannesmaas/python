"""Class object definition for the TAPIE framework steps"""

import json
import jmespath


class Steps:
    data = ""

    def __init__(self):
        pass

    def load_data(self):
        """Extract JSON data from a specific file"""
        with open("tapie.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def case_1(self):
        """The Preparation step in the TAPIE framework is Triage."""
        q = jmespath.search("tapie_framework.Steps[0]", self.data)
        steps = json.dumps(q, indent=4)
        print("Triage: \n\n", steps)
        pass

    def case_2(self):
        """The second step in the TAPIE framework is Analyze."""
        q = jmespath.search("tapie_framework.Steps.[1]", self.data)
        steps = json.dumps(q, indent=4)
        print("Analyze: \n\n", steps)

    def case_3(self):
        """The third step in the TAPIE framework is Plan."""
        q = jmespath.search("tapie_framework.Steps.[2]", self.data)
        steps = json.dumps(q, indent=4)
        print("Plan: \n\n", steps)

    def case_4(self):
        """The fourth step in the TAPIE framework is Implement."""
        q = jmespath.search("tapie_framework.Steps.[3]", self.data)
        steps = json.dumps(q, indent=4)
        print("Implement: \n\n", steps)

    def case_5(self):
        """The fifth step in the TAPIE framework is Evaluate."""
        q = jmespath.search("tapie_framework.Steps.[4]", self.data)
        steps = json.dumps(q, indent=4)
        print("Evaluate: \n\n", steps)

    def invalid(self):
        """User feedback on an invalid input"""
        print("Invalid input")
