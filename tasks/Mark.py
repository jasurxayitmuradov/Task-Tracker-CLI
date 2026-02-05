import json
from .storage import load_tasks , FILE_NAME

# mark taks by id
#done or in-progres

def mark_task_by_id(task_id , status):
    tasks = load_tasks()
    for t in tasks:
        if t.get('id') == task_id:
            t['status'] = status
    with open(FILE_NAME , 'w') as f:
        json.dump(tasks , f , indent=4)
    print(f"Updated task id={task_id}")