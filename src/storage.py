import json
from pathlib import Path


TASKS_FILE = Path("tasks.json")


def load_tasks():
    """
    Load tasks from JSON file.
    Creates an empty file if it does not exist.
    """

    if not TASKS_FILE.exists():
        save_tasks([])
        return []

    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    """
    Save tasks to JSON file.
    """

    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)