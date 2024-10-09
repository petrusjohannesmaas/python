from components.problems import Problem
from components.steps import Steps

# GREETER
print(
    "\nHello, welcome to the TAPIE framework!\nI'm here to help you analyze and solve problems.\n"
)

problem = Problem()
problem.load_data()

problem_categories = {"1": problem.case_1, "2": problem.case_2, "3": problem.case_3}

steps = Steps()
steps.load_data()

steps_dict = {
    "1": steps.case_1,
    "2": steps.case_2,
    "3": steps.case_3,
    "4": steps.case_4,
    "5": steps.case_5,
}

answers = {}  # global variable


def problem_switch(user_input):
    return problem_categories.get(user_input, problem.invalid)()


# STEP 0: Identify the problem category
while True:
    print("\nWhat type of problem is it?\n")
    print("[1] People, [2] Product, [3] Processes, [q] Quit\n")
    result = input("\nYour answer: ")

    if result == "q":
        break

    if result in ["1", "2", "3"]:
        ("Great let's look at some examples:\n")
        problem_switch(result)
        break

answers[0] = input("\nWhat is your specific problem?: ")
answers[1] = input("\nWhat is its impact?: ")
print("\n")

# STEP 1: Triage step
print(steps_dict["1"]())
input("Still there?")
# questions[1] = input("\nSecond answer: ")
# questions[2] = input("\nThird answer: ")
# questions[3] = input("\nFourth answer: ")
# questions[4] = input("\nFifth answer: ")

print("\nGood job!, up next is the Analyze step.\n")

# STEP 2: Analyze step
# STEP 3: Plan step

# STEP 4: Implement step

# STEP 5: Evaluate step
