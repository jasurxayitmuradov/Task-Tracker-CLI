from main import FILE_NAME, TASKS
import json
def delete_task_by_id(task_id):
    # 1 read
    tasks = TASKS
    # print(tasks) #for debuging
    new_tasks = []
    for t in tasks:
        if t.get("id") != task_id:
            new_tasks.append(t)

    for i in range(len(new_tasks)):
        new_tasks[i]['id'] = i+1

    with open(FILE_NAME , "w") as f:
        json.dump(new_tasks , f , indent=4)
    print(f"Deleted id={task_id}")

id = int(input("Please enter id which is you wanted to delet: "))

delete_task_by_id(id)