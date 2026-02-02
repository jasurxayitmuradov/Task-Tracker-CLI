import json
from main import FILE_NAME , TASKS

# mark taks by id
#done or in-progres

def mark_task_by_id(task_id , status):
    tasks = TASKS
    for t in tasks:
        if t.get('id') == task_id:
            t['status'] = status
    with open(FILE_NAME , 'w') as f:
        json.dump(tasks , f , indent=4)
    print(f"Updated task id={id}")

id = int(input("Id: "))
status = int(input("Choose status\n1)done 2)in-progres: "))
if status == 1:
    mark_task_by_id(id, 'done')
elif status == 2:
    mark_task_by_id(id, 'in-progres')
