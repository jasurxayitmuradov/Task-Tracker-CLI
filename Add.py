# Add.py
import json
import os
import sys
from storage import TASKS , FILE_NAME

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    
    ids = [t.get("id", 0) for t in tasks if isinstance(t, dict)]
    return (max(ids) if ids else 0) + 1

def add_task(new_task):
    """
    Adds a new task to tasks.json with status 'todo'.
    """
    tasks = TASKS
    status_options = input("Choose taks's status\n1)todo 2)in-progres: ")
    id = get_next_id(tasks)
    while int(status_options) != 1 and int(status_options) != 2:
        status_options = input("You have to choose 1 or 2: ")
    
    status = "todo"
    if status_options == 2:
        status = "in-progres"
    new_task = {
        "id": id,
        "description": new_task,
        "status": status
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {id})")




