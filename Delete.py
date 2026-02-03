import json
from storage import load_tasks , FILE_NAME


def delete_task_by_id(task_id):

    tasks = load_tasks()

    new_tasks = []
    for t in tasks:
        if t.get("id") != task_id:
            new_tasks.append(t)

    if len(new_tasks) == len(tasks):
        print(f"Task not found: id={task_id}")
        return
    
    with open(FILE_NAME , "w") as f:
        json.dump(new_tasks , f , indent=4)

    print(f"Deleted id={task_id}")

