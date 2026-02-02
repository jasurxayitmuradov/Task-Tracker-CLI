# update tasks by id
import json
from storage import load_tasks , FILE_NAME

def update_task_by_id(tasks_id , new_note):
    tasks = load_tasks()
    for t in tasks:
        if t.get('id') == tasks_id:
            t['description'] = new_note

    with open(FILE_NAME ,'w') as f:
        json.dump(tasks , f , indent=4)
    
    print(f"Updated id={tasks_id}")




