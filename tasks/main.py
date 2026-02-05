import argparse

from .Add import add_task
from .Delete import delete_task_by_id
from .Mark import mark_task_by_id
from .Update import update_task_by_id
from .List import (
    list_all_tasks,
    list_done_tasks,
    list_todo_tasks,
    list_in_progress_tasks,
    list_not_done_tasks,
)

def main():
    parser = argparse.ArgumentParser(
        prog="tasks",
        description="tasks cli program helps you arrange your tasks and it is only for coders who likes terminal command line",
        epilog='Example: tasks add "Buy milk"',
        usage="tasks <command> [options]\n\nCommands:\n list\n delete <id>",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    # tasks add "text"
    p_add = sub.add_parser("add")
    p_add.add_argument("text")

    # tasks update <id> "text"
    p_update = sub.add_parser("update")
    p_update.add_argument("id", type=int)
    p_update.add_argument("text")

    # tasks delete <id>
    p_delete = sub.add_parser("delete")
    p_delete.add_argument("id", type=int)

    # tasks list [filter]
    p_list = sub.add_parser("list")
    p_list.add_argument(
        "filter",
        nargs="?",
        choices=["all", "done", "todo", "in-progress", "notdone"],
        default="all",
    )

    # tasks mark-in-progress <id>
    p_mip = sub.add_parser("mark-in-progress")
    p_mip.add_argument("id", type=int)

    # tasks mark-done <id>
    p_done = sub.add_parser("mark-done")
    p_done.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.text)

    elif args.command == "update":
        update_task_by_id(args.id, args.text)

    elif args.command == "delete":
        delete_task_by_id(args.id)

    elif args.command == "list":
        if args.filter in (None, "all"):
            list_all_tasks()
        elif args.filter == "done":
            list_done_tasks()
        elif args.filter == "todo":
            list_todo_tasks()
        elif args.filter == "in-progress":
            list_in_progress_tasks()
        elif args.filter == "notdone":
            list_not_done_tasks()

    elif args.command == "mark-in-progress":
        mark_task_by_id(args.id, "in-progress")

    elif args.command == "mark-done":
        mark_task_by_id(args.id, "done")


if __name__ == "__main__":
    main()
