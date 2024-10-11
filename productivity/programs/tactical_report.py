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

TACTICS = load_json_data("tactics.json")

# Assorted days of the week
weekdays = jmespath.search("tactics.weekdays", TACTICS)
fridays = jmespath.search("tactics.fridays", TACTICS)
weekends = jmespath.search("tactics.weekends", TACTICS)

# All tactics
startup = jmespath.search("STARTUP.actions", weekdays)
work = jmespath.search("WORK.actions", weekdays)
shutdown = jmespath.search("SHUTDOWN.actions", weekdays)
writing = jmespath.search("WRITING.actions", fridays)
administration = jmespath.search("ADMINISTRATION.actions", weekends)
family = jmespath.search("FAMILY.actions", weekends)
personal = jmespath.search("PERSONAL.actions", weekends)
marriage = jmespath.search("MARRIAGE.actions", weekends)

"""Functions for each slot"""


def morning_slot():
    responses = []
    for action in startup:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        responses.append((action, answer))
    return responses


def work_slot():
    responses = []
    for action in work:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        responses.append((action, answer))
    return responses


def shutdown_slot():
    responses = []
    for action in shutdown:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        responses.append((action, answer))
    return responses


def writing_slot():
    responses = []
    for action in writing:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        responses.append((action, answer))
    return responses


def admin_slot():
    responses = []
    for action in administration:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        responses.append((action, answer))
    return responses


def family_slot():
    responses = []
    for action in family:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        responses.append((action, answer))
    return responses


def personal_slot():
    responses = []
    for action in personal:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
        responses.append((action, answer))
    return responses


def marriage_slot():
    responses = []
    for action in marriage:
        answer = console.input(f"{action}: [yes/no] ").strip().lower()
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
        "\nHow about the shutdown activities?.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(shutdown_slot())

elif input_day == "Friday":
    console.print(
        "\nLet's end this week off right.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(morning_slot())
    console.print(
        "\nDid you do your writing for the week?\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(writing_slot())
    console.print(
        "\nHow about the shutdown activities?.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(shutdown_slot())

elif input_day in ["Saturday", "Sunday"]:
    console.print(
        "\nLet's start with your morning.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    responses.extend(admin_slot())
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

console.print("\n[bold]Were there any exceptions?[/bold] \n")
exceptions = console.input("Explain the exception briefly: ")
mood = console.input("\nWas it a good day?: (yes/no) ")
comments = console.input("\nAny comments?: \n ->")

now = datetime.now()
file_name = f"tactical_report_{input_day}_{now.strftime('%B')}_{now.year}.txt"

with open(file_name, "w") as file:
    file.write(f"Tactical Report for {input_day}, {now.strftime('%B %d, %Y')}\n\n")
    for action, result in responses:
        file.write(f"{action}: {result}\n")
    file.write(f"\nExceptions: {exceptions}\n")
    file.write(f"Mood: {mood}\n")
    file.write(f"Comments: {comments}\n")

console.print(f"\nReport saved to {file_name}")
