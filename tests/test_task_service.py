import pytest

from src import storage

from src.task_service import (
    create_task,
    get_tasks,
    update_task,
    delete_task,
    change_status,
)


@pytest.fixture
def test_file(tmp_path):
    """
    Provide an isolated JSON file for each test.

    The storage module is redirected to this file
    to prevent tests from modifying real task data.
    """

    file = tmp_path / "tasks.json"

    # Redirect storage to a temporary file so tests do not modify real data.
    storage.TASKS_FILE = file  

    return file


# -------------------------
# Create task tests
# -------------------------

def test_create_task(test_file):

    task = create_task("Buy groceries")

    assert task["id"] == 1
    assert task["description"] == "Buy groceries"
    assert task["status"] == "todo"

    assert "createdAt" in task
    assert "updatedAt" in task


def test_create_multiple_tasks(test_file):

    task1 = create_task("Task 1")
    task2 = create_task("Task 2")

    assert task1["id"] == 1
    assert task2["id"] == 2

    tasks = get_tasks()

    assert len(tasks) == 2


def test_update_task_empty_description(test_file):

    create_task("Homework")

    with pytest.raises(ValueError):
        update_task(1, "")

def test_create_task_whitespace_description(test_file):

    with pytest.raises(ValueError):
        create_task("     ")
# -------------------------
# Read/List tests
# -------------------------

def test_get_all_tasks(test_file):

    create_task("Task 1")
    create_task("Task 2")

    tasks = get_tasks()

    assert len(tasks) == 2


def test_get_tasks_by_status(test_file):

    create_task("Finish homework")

    change_status(1, "done")

    tasks = get_tasks("done")

    assert len(tasks) == 1
    assert tasks[0]["status"] == "done"


# -------------------------
# Update tests
# -------------------------

def test_update_task(test_file):

    create_task("Old description")

    updated_task = update_task(
        1,
        "New description"
    )

    assert updated_task["description"] == "New description"


def test_update_non_existing_task(test_file):

    result = update_task(
        999,
        "New description"
    )

    assert result is None


# -------------------------
# Delete tests
# -------------------------

def test_delete_task(test_file):

    create_task("Delete me")

    delete_task(1)

    tasks = get_tasks()

    assert len(tasks) == 0


def test_delete_non_existing_task(test_file):

    create_task("Keep me")

    delete_task(999)

    tasks = get_tasks()

    assert len(tasks) == 1


# -------------------------
# Status tests
# -------------------------

def test_mark_task_done(test_file):

    create_task("Homework")

    task = change_status(
        1,
        "done"
    )

    assert task["status"] == "done"


def test_invalid_status(test_file):

    create_task("Homework")

    with pytest.raises(ValueError):

        change_status(
            1,
            "finished"
        )