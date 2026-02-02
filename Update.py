# update tasks by id
import json
from main import FILE_NAME , TASKS

def update_task_by_id(tasks_id , new_note):
    tasks = TASKS
    for t in tasks:
        if t.get('id') == tasks_id:
            t['description'] = new_note

    with open(FILE_NAME ,'w') as f:
        json.dump(tasks , f , indent=4)
    
    print(f"Updated id={tasks_id}")


id = int(input("Please enter id which you need to update: "))
new_note = input("Enter new description: ")
update_task_by_id(id ,new_note)

