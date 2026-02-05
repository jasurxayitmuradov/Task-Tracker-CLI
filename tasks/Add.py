# Add.py
import json
import os
import sys
from .storage import load_tasks , FILE_NAME

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
    tasks = load_tasks()

    while True:

        status_option = input("Choose task's status\n1) todo  2) in-progress: ").strip()

        if status_option in ("1" , "2"):
            break
        
        print("You have to choose 1 or 2.")

    status = "todo" if status_option == "1" else "in-progress"
    task_id = get_next_id(tasks)

    new_task = {
        "id": task_id,
        "description": new_task,
        "status": status
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")




