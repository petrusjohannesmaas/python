from components.switch import Problem

# GREETER (Make a greeting variable from JSON)
print(
    """
Welcome!\n
Work-related problems can generally be categorized by the area they impact most.\n
That’s not to say a problem can’t impact multiple areas, but usually there \
is an area of primary impact.\n 
I find it useful to categorize problems into the following three categories.\n
"""
)

problem = Problem()

problem.load_data()

problem_categories = {
    "1": problem.case_1,
    "2": problem.case_2,
    "3": problem.case_3,
    "4": problem.case_4,
    "5": problem.case_5,
}
# steps = {"1": case_1, "2": case_2, "3": case_3, "4": case_4, "5": case_5}


def problem_switch(user_input):
    return problem_categories.get(user_input, problem.invalid)()


# STEP 0: Identify the problem category
while True:
    print("\nWhat type of problem is it? (q to Quit)\n")
    result = input("[1] People, [2] Product, [3] Processes, [4] 4, [5] 5\n")

    if result == "q":
        break

    problem_switch(result)

# STEP 1: Triage step

# STEP 2: Analyze step

# STEP 3: Plan step

# STEP 4: Implement step

# STEP 5: Evaluate step
