from src.task_service import (
    create_task,
    update_task,
    delete_task,
    change_status,
    get_tasks,
)


def handle_add(arguments):
    if not arguments:
        print("Error: task description is required.")
        return

    description = arguments[0]

    task = create_task(description)

    print(f"Task added successfully (ID: {task['id']})")


def handle_update(arguments):
    if len(arguments) < 2:
        print("Error: task id and description are required.")
        return

    task_id = arguments[0]
    description = arguments[1]

    update_task(task_id, description)

    print("Task updated successfully.")


def handle_delete(arguments):
    if not arguments:
        print("Error: task id is required.")
        return

    task_id = arguments[0]

    delete_task(task_id)

    print("Task deleted successfully.")


def handle_mark_in_progress(arguments):
    if not arguments:
        print("Error: task id is required.")
        return

    task_id = arguments[0]

    change_status(task_id, "in-progress")

    print("Task marked as in-progress.")


def handle_mark_done(arguments):
    if not arguments:
        print("Error: task id is required.")
        return

    task_id = arguments[0]

    change_status(task_id, "done")

    print("Task marked as done.")


def handle_list(arguments):
    status = None

    if arguments:
        status = arguments[0]

    tasks = get_tasks(status)

    for task in tasks:
        print(task)