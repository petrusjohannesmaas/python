import json


def show_tasks(tasks):
    for task_id, task_data in tasks.items():
        print(f"[Task:] {task_id}")

        for item in task_data:
            print(f"  8=>  {item}")
        print()

        while True:
            response = input("Next task (N) or skip (S)? ").lower()

            if response in ["n", "next"]:
                print(f"{task_id} completed.")
                break  # Move to the next task

            elif response in ["s", "skip"]:
                print(f"{task_id} skipped.")
                break  # Skip the current task

            else:
                print("Invalid input. Please enter 'N' or 'S'.")


def main():
    # Load the data from the JSON file
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ask the user if they're ready
    welcome_prompt = data["prompts"]["welcome"][0]
    response = input(welcome_prompt).lower()  # Print the welcome prompt
    if response == "y":
        # Show tasks if the user agrees
        show_tasks(data["tasks"])
    else:
        print("It's all good homie.")


if __name__ == "__main__":
    main()
