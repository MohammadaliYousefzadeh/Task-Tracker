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

## Task Commands

### Add a task

```bash
python -m src.main add "Buy groceries"
```

### Update a task

```bash
python -m src.main update 12 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python -m src.main delete 12
```

### Delete a non-existing task

```bash
python -m src.main delete 112
```

### Mark a task as in-progress

```bash
python -m src.main mark-in-progress 12
```

### Mark a task as done

```bash
python -m src.main mark-done 12
```

### List all tasks

```bash
python -m src.main list
```

### List tasks by status

```bash
python -m src.main list todo

python -m src.main list in-progress

python -m src.main list done
```

---

## Project Structure

```text
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
```

