
import json
FILE_NAME = "tasks.json"

def ensure_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f, indent=4)
def load_tasks():

    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, ValueError):
        return []

TASKS = load_tasks()

