from datetime import datetime

from src.storage import load_tasks, save_tasks

def get_current_time():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def create_task(description):
    tasks = load_tasks()

    new_id = get_next_id(tasks)
    current_time = get_current_time()

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time,
    }

    tasks.append(task)

    save_tasks(tasks)

    return task


def get_next_id(tasks):
    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


def update_task(task_id, description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(task_id):
            task["description"] = description
            task["updatedAt"] = get_current_time()

            save_tasks(tasks)
            return task

    return None


def delete_task(task_id):
    tasks = load_tasks()

    updated_tasks = [
        task for task in tasks
        if task["id"] != int(task_id)
    ]

    save_tasks(updated_tasks)


def change_status(task_id, status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = status
            task["updatedAt"] = get_current_time()

            save_tasks(tasks)
            return task

    return None


def get_tasks(status=None):
    tasks = load_tasks()

    if status is None:
        return tasks

    return [
        task
        for task in tasks
        if task["status"] == status
    ]