from datetime import datetime

from src.storage import load_tasks, save_tasks

VALID_STATUSES = [
    "todo",
    "in-progress",
    "done"
]


def get_current_time():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def create_task(description):

    description = description.strip()
    if not description.strip():
        raise ValueError("Description cannot be empty")
    
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
    """
    Generate the next available task ID.

    Uses the maximum existing ID instead of the number of tasks
    because tasks can be deleted.
    """

    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


def update_task(task_id, description):
    tasks = load_tasks()
    description = description.strip()

    if not description.strip():
        raise ValueError("Description cannot be empty")

    for task in tasks:
        if task["id"] == int(task_id):
            task["description"] = description
            task["updatedAt"] = get_current_time()

            save_tasks(tasks)
            return task

    return None


def delete_task(task_id):
    """
    Delete a task by its ID.

    Returns:
        True if the task was deleted, otherwise False.
    """    

    tasks = load_tasks()

    original_length = len(tasks)

    tasks = [
        task
        for task in tasks
        if task["id"] != int(task_id)
    ]

    if len(tasks) == original_length:
        return False

    save_tasks(tasks)
    return True


def change_status(task_id, status):
    """
    Update the status of a task.

    Raises:
        ValueError: If the provided status is not valid.
    
    Returns:
        The updated task if found, otherwise None.
    """    

    if status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid status. Choose one of: {VALID_STATUSES}"
)

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = status
            task["updatedAt"] = get_current_time()

            save_tasks(tasks)
            return task

    return None


def get_tasks(status=None):
    """
    Retrieve tasks, optionally filtered by status.

    Args:
        status: Optional task status filter.

    Returns:
        A list of matching tasks.
    """

    tasks = load_tasks()

    if status is None:
        return tasks

    return [
        task
        for task in tasks
        if task["status"] == status
    ]