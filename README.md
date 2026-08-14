# Task Tracker CLI

A simple command-line task management application built with Python.

This project allows users to create, update, delete, and track tasks using a CLI interface. Tasks are stored locally in a JSON file.

The goal of this project is to practice:

- Command-line applications
- File system operations
- JSON data storage
- Software architecture
- Unit testing
- Git workflow

---

## Features

The application supports:

- Add a new task
- Update an existing task
- Delete a task
- Mark a task as in-progress
- Mark a task as done
- List all tasks
- Filter tasks by status

Supported statuses:

- `todo`
- `in-progress`
- `done`

---

## Running the Application

Run the application from the project root directory.

### Task Useable commands

python -m src.main add "Buy groceries"

python -m src.main update 12 "Buy groceries and cook dinner"

python -m src.main delete 12

python -m src.main delete 112

python -m src.main mark-in-progress 12

python -m src.main mark-done 12

python -m src.main list

python -m src.main list todo
python -m src.main list in-progress
python -m src.main list done


## Project Structure

task-tracker/
│
├── README.md
├── pytest.ini
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── command.py
│   ├── task_service.py
│   └── storage.py
│
└── tests/
    └── test_task_service.py

