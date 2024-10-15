import json
import os
import jmespath
from rich.console import Console
from datetime import datetime

"""Initialization"""

console = Console()


def load_json_data(filename):
    with open(os.path.join("../data", filename), "r") as file:
        return json.load(file)


"""Variables and objects"""

TIMEBLOCKS = load_json_data("timeblocks.json")

# Assorted days of the week
weekdays = jmespath.search("timeblocks.weekdays", TIMEBLOCKS)
fridays = jmespath.search("timeblocks.fridays", TIMEBLOCKS)
weekends = jmespath.search("timeblocks.weekends", TIMEBLOCKS)

# All timeblocks
morning = jmespath.search("morning.actions", weekdays)
work = jmespath.search("work.actions", weekdays)
evening = jmespath.search("evening.actions", weekdays)
research = jmespath.search("research.actions", fridays)
sat_and_sun_morning = jmespath.search("morning.actions", weekends)
family = jmespath.search("family.actions", weekends)
personal = jmespath.search("personal.actions", weekends)
marriage = jmespath.search("marriage.actions", weekends)

"""Functions for each slot"""


def morning_slot():
    responses = []
    for action in morning:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        answer = "true" if answer == "yes" else "false"
        responses.append((action, answer))
    return responses


def work_slot():
    responses = []
    for action in work:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        answer = "true" if answer == "yes" else "false"
        responses.append((action, answer))
    return responses


def evening_slot():
    responses = []
    for action in evening:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        answer = "true" if answer == "yes" else "false"
        responses.append((action, answer))
    return responses


def research_slot():
    responses = []
    for action in research:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        answer = "true" if answer == "yes" else "false"
        responses.append((action, answer))
    return responses


def sat_and_sun_morning_slot():
    responses = []
    for action in sat_and_sun_morning:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        answer = "true" if answer == "yes" else "false"
        responses.append((action, answer))
    return responses


def family_slot():
    responses = []
    for action in family:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        answer = "true" if answer == "yes" else "false"
        responses.append((action, answer))
    return responses


def personal_slot():
    responses = []
    for action in personal:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        answer = "true" if answer == "yes" else "false"
        responses.append((action, answer))
    return responses


def marriage_slot():
    responses = []
    for action in marriage:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        answer = "true" if answer == "yes" else "false"
        responses.append((action, answer))
    return responses


"""Application logic"""

console.print("\n[bold]Welcome to the Tactical Report Program[/bold]\n")

input_day = console.input(
    "\n[italic]Enter the day of the week (e.g. Monday):[/italic] "
)

responses = []

if input_day in ["Monday", "Tuesday", "Wednesday", "Thursday"]:
    console.print(
        """\nLet's start with your morning.\nAnswer 'yes' if completed or 'no' if not.\n"""
    )
    responses.extend(morning_slot())
    console.print("\nCheck your work.\nAnswer 'yes' if completed or 'no' if not.\n")
    responses.extend(work_slot())
    console.print(
        "\nHow about the evening activities?.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(evening_slot())

elif input_day == "Friday":
    console.print(
        "\nLet's end this week off right.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(morning_slot())
    console.print(
        "\nDid you do your research for the week?\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(research_slot())
    console.print(
        "\nHow about the evening activities?.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(evening_slot())

elif input_day in ["Saturday", "Sunday"]:
    console.print(
        "\nLet's start with your morning.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(sat_and_sun_morning_slot())
    console.print(
        "\nDid you serve your family?.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(family_slot())
    console.print(
        "\nIt's important to have personal time...\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(personal_slot())
    console.print(
        "\n... but even more important is your marriage.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(marriage_slot())

else:
    pass

mood = console.input("\n[bold]Was it a good day?:[/bold] (yes/no) \n-> ")
mood = "true" if mood.lower() == "yes" else "false"

exceptions = console.input(
    "\n[bold]Were there any exceptions?:[/bold] (Brief explanation)\n-> "
)
comments = console.input("\n[bold]Any comments?:[/bold]\n-> ")
memory = console.input("\n[bold]Note a memory you'd like to retain:[/bold]\n-> ")

# Get current datetime
now = datetime.now()

# Create directory if it doesn't exist
if not os.path.exists("../reports"):
    os.makedirs("../reports")

# Create the file path
file_name = f"daily_report_{input_day}_{now.strftime('%B_%d_%Y')}.json"
file_path = os.path.join("../reports", file_name)

# Calculate performance score
total_actions = len(responses)
true_actions = sum(1 for _, result in responses if result == "true")
performance_score = (true_actions / total_actions) * 100

# Create the report data
report_data = {
    "date": now.strftime("%Y-%m-%d"),
    "day": input_day,
    "completed": {action: result for action, result in responses},
    "performance_score": performance_score,
    "good_day": mood,
    "exceptions": exceptions,
    "comments": comments,
    "memory": memory,
}

# Write to the file
with open(file_path, "w") as file:
    json.dump(report_data, file, indent=4)

# Print the path to the file
print(f"\nReport saved to {file_path}")
