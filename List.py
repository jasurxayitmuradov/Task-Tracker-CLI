import json
import os
import sys
from storage import TASKS , FILE_NAME

def print_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['title']}  --->  {task['status']}")


# 1) List all tasks
def list_all_tasks():
    print_tasks(TASKS)


# # 2) List all tasks that are done
# def list_done_tasks():
#     tasks = TASKS
#     done = []
#     for t in tasks:
#         if t['status'] == 'done':
#             done.append(t)
#     print_tasks(done)


# # 3) List all tasks that are not done (todo + in-progress)
# def list_not_done_tasks():
#     tasks = TASKS
#     not_done = []
#     for t in tasks:
#         if t['status'] == 'todo' or t['status'] == 'in-progress':
#             not_done.append(t)
#     print_tasks(not_done)


# # 4) List all tasks that are in progress
# def list_in_progress_tasks():
#     tasks = TASKS
#     in_progress = []
#     for t in tasks:
#         if t["status"] == "in-progress":
#             in_progress.append(t)
#     print_tasks(in_progress)

list_all_tasks()
# list_done_tasks()
# list_not_done_tasks()
# list_in_progress_tasks()