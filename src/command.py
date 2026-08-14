from src.task_service import (
    create_task,
    update_task,
    delete_task,
    change_status,
    get_tasks,
)

ERROR_TASK_ID_REQUIRED = "Error: task id is required."

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

    result = update_task(task_id, description)

    if result:
        print("Task updated successfully.")
    else:
        print("Error: Task not found.")


def handle_delete(arguments):
    if not arguments:
        print(ERROR_TASK_ID_REQUIRED)
        return

    task_id = arguments[0]

    result = delete_task(task_id)

    if result:
        print("Task deleted successfully.")
    else:
        print("Error: Task not found.")


def handle_mark_in_progress(arguments):
    if not arguments:
        print(ERROR_TASK_ID_REQUIRED)
        return

    task_id = arguments[0]

    task = change_status(task_id, "in-progress")

    if task:
        print("Task marked as in-progress.")
    else:
        print("Error: Task not found.")


def handle_mark_done(arguments):
    if not arguments:
        print(ERROR_TASK_ID_REQUIRED)
        return

    task_id = arguments[0]

    task = change_status(task_id, "done")

    if task:
        print("Task marked as done.")
    else:
        print("Error: Task not found.")


def handle_list(arguments):
    status = None

    if arguments:
        status = arguments[0]

    tasks = get_tasks(status)

    for task in tasks:
        print(task)


def handle_command(command, arguments):
    """
    Dispatch a CLI command to its corresponding handler.

    Args:
        command: The command entered by the user.
        arguments: Additional command-line arguments.
    """    

    if command == "add":
        handle_add(arguments)

    elif command == "update":
        handle_update(arguments)

    elif command == "delete":
        handle_delete(arguments)

    elif command == "mark-in-progress":
        handle_mark_in_progress(arguments)

    elif command == "mark-done":
        handle_mark_done(arguments)

    elif command == "list":
        handle_list(arguments)

    else:
        print(f"Unknown command: {command}")        