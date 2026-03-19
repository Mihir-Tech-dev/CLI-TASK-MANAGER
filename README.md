# CLI Task Manager

A command-line task manager built in Python. Add, list, complete, and delete tasks — all from your terminal. Tasks persist between sessions via a local JSON file.

Built as a learning project covering OOP, type hints, context managers, argparse, and clean project structure.

---

## Features

- Add tasks with optional priority levels (`low`, `medium`, `high`)
- List all tasks or filter by status (`todo` / `done`)
- Mark tasks as done
- Delete tasks
- Tasks persist automatically to `store.json`

---

## Requirements

- Python 3.11+

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

**2. Create and activate a virtual environment**
```bash
# Mac/Linux
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

**3. Install the project**
```bash
pip install -e .
```

---

## Usage

All commands are run from the `task-manager/` root folder.

### Add a task
```bash
python -m task_manager add "Buy groceries"
python -m task_manager add "Submit assignment" --priority high
```
Priority options: `low`, `medium` (default), `high`

### List all tasks
```bash
python -m task_manager list
```
Output:
```
#1 [high]   Buy groceries - todo   (2024-01-15 10:30:00)
#2 [medium] Read notes    - done   (2024-01-15 11:00:00)
```

### Filter by status
```bash
python -m task_manager list --filter todo
python -m task_manager list --filter done
```

### Mark a task as done
```bash
python -m task_manager done 1
```

### Delete a task
```bash
python -m task_manager delete 1
```

---

## Project Structure

```
task-manager/
  task_manager/
    __init__.py
    __main__.py     ← entry point, argparse CLI
    models.py       ← Task dataclass
    manager.py      ← TaskManager class (add, delete, complete, list)
    storage.py      ← JSON save/load
  pyproject.toml
  .gitignore
  README.md
```

---

## How it works

- `models.py` defines the `Task` dataclass with `title`, `id`, `status`, `priority`, and `created_at`
- `storage.py` handles reading and writing tasks to `store.json` using a context manager
- `manager.py` holds all business logic — the `TaskManager` class loads tasks on startup and saves after every change
- `__main__.py` parses CLI arguments with `argparse` and routes to the right method on `TaskManager`