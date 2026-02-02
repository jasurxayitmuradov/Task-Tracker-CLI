# Add.py
import json
import os
import sys

FILE_NAME = "tasks.json"

def ensure_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f, indent=4)

def load_tasks():
    ensure_file()
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, ValueError):
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    
    ids = [t.get("id", 0) for t in tasks if isinstance(t, dict)]
    return (max(ids) if ids else 0) + 1

def add_task(description):
    """
    Adds a new task to tasks.json with status 'todo'.
    """
    tasks = load_tasks()
    status_options = input("Choose taks's status\n1)todo 2)in-progres:")

    while int(status_options) != 1 and int(status_options) != 2:
        status_options = input("You have to choose 1 or 2: ")
    
    status = "todo"
    if status_options == 2:
        status = "in-progres"
    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": status
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task

task = input("Write your new task: ")
add_task(task)

