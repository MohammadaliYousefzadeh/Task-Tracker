import json
from pathlib import Path


TASKS_FILE = Path("tasks.json")


def load_tasks():
    """
    Load tasks from JSON file.
    If the file does not exist, create it with an empty task list.
    """

    if not TASKS_FILE.exists():
        save_tasks([])
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    """
    Save the task list to the JSON storage file.

    The file is written with indentation for readability.
    """

    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)