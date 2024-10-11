import json
import os
import jmespath
from rich.console import Console

console = Console()


# Load JSON data from the files
def load_json_data(filename):
    with open(os.path.join("../data", filename), "r") as file:
        return json.load(file)


TACTICS = load_json_data("tactics.json")
ENV = json.dumps(load_json_data("environment_variables.json"), indent=4)

weekdays = json.dumps(jmespath.search("tactics.weekdays", TACTICS), indent=4)
fridays = json.dumps(jmespath.search("tactics.fridays", TACTICS), indent=4)
weekends = json.dumps(jmespath.search("tactics.weekends", TACTICS), indent=4)

timeblocks_string = str("\n[bold]Timeblocks:[/bold]\n\n")

console.print(
    "\n[bold]Welcome to the Timeblocking Program[/bold]\n", style="medium_spring_green"
)

input_day = console.input(
    "\n[italic]Enter the day of the week (e.g. Monday):[/italic] "
)

console.print("\n[bold]Environment Variables:[/bold]\n")

console.print(ENV, style="steel_blue")

if input_day in ["Monday", "Tuesday", "Wednesday", "Thursday"]:

    console.print(timeblocks_string, weekdays)
elif input_day == "Friday":
    console.print(timeblocks_string, fridays)
elif input_day in ["Saturday", "Sunday"]:
    console.print(timeblocks_string, weekends)
else:
    console.print("\n[bold red]Invalid day of the week[/bold red]")
