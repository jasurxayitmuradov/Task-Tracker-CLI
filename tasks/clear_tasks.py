import json
from .storage import load_tasks , FILE_NAME

def clear_tasks():
    with open(FILE_NAME , "w") as f:
        json.dump({} , f)
    print("All tasks are cleared.")
