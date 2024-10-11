import json
import os
import jmespath
from rich.console import Console

"""Initialization"""

console = Console()


def load_json_data(filename):
    with open(os.path.join("../data", filename), "r") as file:
        return json.load(file)


"""Variables and objects"""

TACTICS = load_json_data("tactics.json")

# Convenient DRY strings
COMPLETED = "[bold green]Completed:[/bold green]"
NOT_COMPLETED = "[bold red]Not Completed:[/bold red]"

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

# Tactics functions


def morning_slot():
    for action in startup:
        answer = console.input(f"{action}: (yes/no) ").strip().lower()
        if answer == "yes":
            console.print(f"{COMPLETED} {action}")
        else:
            console.print(f"{NOT_COMPLETED} {action}")


def work_slot():
    for action in work:
        answer = console.input(f"{action}: (yes/no) ").strip().lower()
        if answer == "yes":
            console.print(f"{COMPLETED} {action}")
        else:
            console.print(f"{NOT_COMPLETED} {action}")


def shutdown_slot():
    for action in shutdown:
        answer = console.input(f"{action}: (yes/no) ").strip().lower()
        if answer == "yes":
            console.print(f"{COMPLETED} {action}")
        else:
            console.print(f"{NOT_COMPLETED} {action}")


def writing_slot():
    for action in writing:
        answer = console.input(f"{action}: (yes/no) ").strip().lower()
        if answer == "yes":
            console.print(f"{COMPLETED} {action}")
        else:
            console.print(f"{NOT_COMPLETED} {action}")


def admin_slot():
    for action in administration:
        answer = console.input(f"{action}: (yes/no) ").strip().lower()
        if answer == "yes":
            console.print(f"{COMPLETED} {action}")
        else:
            console.print(f"{NOT_COMPLETED} {action}")


def family_slot():
    for action in family:
        answer = console.input(f"{action}: (yes/no) ").strip().lower()
        if answer == "yes":
            console.print(f"{COMPLETED} {action}")
        else:
            console.print(f"{NOT_COMPLETED} {action}")


def personal_slot():
    for action in personal:
        answer = console.input(f"{action}: (yes/no) ").strip().lower()
        if answer == "yes":
            console.print(f"{COMPLETED} {action}")
        else:
            console.print(f"{NOT_COMPLETED} {action}")


def marriage_slot():
    for action in marriage:
        answer = console.input(f"{action}: (yes/no) ").strip().lower()
        if answer == "yes":
            console.print(f"{COMPLETED} {action}")
        else:
            console.print(f"{NOT_COMPLETED} {action}")


"""Application logic"""

console.print("\n[bold]Welcome to the Tactical Report Program[/bold]\n")

input_day = console.input(
    "\n[italic]Enter the day of the week (e.g. Monday):[/italic] "
)

if input_day in ["Monday", "Tuesday", "Wednesday", "Thursday"]:
    console.print(
        """\nLet's start with your morning.\nAnswer 'yes' if completed or 'no' if not.\n"""
    )
    morning_slot()
    console.print("\nCheck your work.\nAnswer 'yes' if completed or 'no' if not.\n")
    work_slot()
    console.print(
        "\nHow about the shutdown activities?.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    shutdown_slot()

elif input_day == "Friday":
    console.print(
        "\nLet's end this week off right.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    morning_slot()
    console.print(
        "\nDid you do your writing for the week?\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    writing_slot()
    console.print(
        "\nHow about the shutdown activities?.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    shutdown_slot()

elif input_day in ["Saturday", "Sunday"]:
    console.print(
        "\nLet's start with your morning.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    admin_slot()
    console.print(
        "\nDid you serve your family?.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    family_slot()
    console.print(
        "\nIt's important to have personal time...\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    personal_slot()
    console.print(
        "\n... but even more important is your marriage.\nAnswer 'yes' if completed or 'no' if not.\n"
    )
    marriage_slot()

else:
    pass
