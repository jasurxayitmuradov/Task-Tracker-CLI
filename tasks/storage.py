import json
import os

APP_DIR = os.path.join(os.path.expanduser("~"), ".tasks")
FILE_NAME = os.path.join(APP_DIR, "tasks.json")

def ensure_file():
    if not os.path.exists(APP_DIR):
        os.makedirs(APP_DIR)

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f, indent=4)

def load_tasks():
    ensure_file()
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, ValueError):
        return []
