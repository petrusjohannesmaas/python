import json
from datetime import datetime


def show_tasks(tasks):
    task_results = []

    for task_id, task_data in tasks.items():
        print(f"[Task:] {task_id}")
        for item in task_data:
            print(f"  - {item}")
        print()

        task_results.append(f"[Task:] {task_id}\n")
        task_results.extend([f"  - | {item}\n" for item in task_data])

        response = input("Next task (N) or skip (S)? ").lower()
        result = (
            f"{task_id} completed.\n" if response == "n" else f"{task_id} skipped.\n"
        )
        task_results.append(result)

    file_name = f"{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(file_name, "w") as file:
        file.writelines(task_results)

    print(f"Remember to file your report! {file_name}")


def main():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    response = input(data["prompts"]["greet"][0]).lower()
    if response == "y":
        show_tasks(data["tasks"])
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
