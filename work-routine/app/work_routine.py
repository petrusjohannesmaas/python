import json
from datetime import datetime


def display_tasks(tasks):
    task_log = []

    # Loop through each task category and show options
    for task_name, task_options in tasks.items():
        print(f"Task: {task_name}")

        # Display the options (1, 2, or 3)
        for option in task_options:
            for key, description in option.items():
                print(f"  {key}. {description}")
        print()

        # Ask the user to pick an option or skip the task
        while True:
            response = input(f"Choose an option (1, 2, 3) or skip (S): ").lower()

            # If user selects 1, 2, or 3, log the choice
            if response in ["1", "2", "3"]:
                selected_option = [
                    opt[response] for opt in task_options if response in opt
                ]
                task_log.append(f"{task_name}: {selected_option[0]} (selected)\n")

                # After option selection, ask if they completed the full session
                session_complete = input(
                    "Did you complete a full session? (Y/N): "
                ).lower()
                if session_complete == "y":
                    task_log.append(f"  Session completed: Yes\n")
                else:
                    task_log.append(f"  Session completed: No\n")
                break

            # If user chooses to skip the task
            elif response == "s":
                task_log.append(f"{task_name}: skipped\n")
                break

            # Handle invalid input
            else:
                print("Invalid input. Please choose 1, 2, 3, or S.")

    # Write the task log to a file
    file_name = f"{datetime.now().strftime('%Y-%m-%d')}_task_log.txt"
    with open(file_name, "w") as file:
        file.writelines(task_log)

    print(f"Task log saved as: {file_name}")


def main():
    # Load the tasks and prompts from the JSON file
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Prompt the user if they are ready to start
    start_prompt = data["prompts"]["greet"][0]
    response = input(start_prompt).lower()

    # Display tasks if user is ready
    if response == "y":
        display_tasks(data["tasks"])
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
