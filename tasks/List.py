import json
import os
import sys
from .storage import load_tasks , FILE_NAME
from rich import print

def print_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[blue][{task['id']}][/blue] [bold][green]{task['description']}[/green][/bold]  --->  [yellow]{task['status']}[/yellow]")


# List all tasks
def list_all_tasks():[blue]
    tasks = load_tasks()
    print_tasks(tasks)


# List all tasks that are done
def list_done_tasks():
    tasks = load_tasks()
    done = []
    for t in tasks:
        if t['status'] == 'done':
            done.append(t)
    print_tasks(done)

# List all tasks that are todo
def list_todo_tasks():
    tasks = load_tasks()
    todo = []
    for t in tasks:
        if t['status'] == 'todo':
            todo.append(t)
    print_tasks(todo)


# List all tasks that are not done (todo + in-progress)
def list_not_done_tasks():
    tasks = load_tasks()
    not_done = []
    for t in tasks:
        if t['status'] == 'todo' or t['status'] == 'in-progress':
            not_done.append(t)
    print_tasks(not_done)


# List all tasks that are in progress
def list_in_progress_tasks():
    tasks = load_tasks()
    in_progress = []
    for t in tasks:
        if t["status"] == "in-progress":
            in_progress.append(t)
    print_tasks(in_progress)



