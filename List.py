import json
import os

FILE_NAME = "tasks.json"


def ensure_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f, indent=4)

def load_tasks():
    ensure_file()
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def print_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['title']}  --->  {task['status']}")


# 1) List all tasks
def list_all_tasks():
    tasks = load_tasks()
    print_tasks(tasks)


# 2) List all tasks that are done
def list_done_tasks():
    tasks = load_tasks()
    done = []
    for t in tasks:
        if t['status'] == 'done':
            done.append(t)
    print_tasks(done)


# 3) List all tasks that are not done (todo + in-progress)
def list_not_done_tasks():
    tasks = load_tasks()
    not_done = []
    for t in tasks:
        if t['status'] == 'todo' or t['status'] == 'in-progress':
            not_done.append(t)
    print_tasks(not_done)


# 4) List all tasks that are in progress
def list_in_progress_tasks():
    tasks = load_tasks()
    in_progress = []
    for t in tasks:
        if t["status"] == "in-progress":
            in_progress.append(t)
    print_tasks(in_progress)

list_all_tasks()
list_done_tasks()
list_not_done_tasks()
list_in_progress_tasks()