import sys
from Add import add_task
from Delete import delete_task_by_id
from Mark import mark_task_by_id
from Update import update_task_by_id
from List import list_all_tasks , list_done_tasks
terminal_commands = sys.argv

USAGE_TEXT = """
Task Tracker CLI

Usage:
  task-cli <command> [arguments]

Commands:
  add "<description>"
      Add a new task.
      Example:
        task-cli add "Buy groceries"

  update <id> "<new_description>"
      Update task description by id.
      Example:
        task-cli update 1 "Buy groceries and cook dinner"

  delete <id>
      Delete a task by id.
      Example:
        task-cli delete 1

  mark-in-progress <id>
      Mark a task as in-progress.
      Example:
        task-cli mark-in-progress 1

  mark-done <id>
      Mark a task as done.
      Example:
        task-cli mark-done 1

  list
      List all tasks.
      Example:
        task-cli list

  list <status>
      List tasks by status.
      Status values: todo, in-progress, done
      Examples:
        task-cli list todo
        task-cli list in-progress
        task-cli list done

Notes:
  - Task id must be a number (integer).
  - Wrap descriptions in quotes if they contain spaces.
"""
# print(terminal_commands)
if len(terminal_commands) < 2:
    print(USAGE_TEXT)
    sys.exit(1)
#add
if terminal_commands[1] == 'add':
    add_task(terminal_commands[2])

#delete   
if terminal_commands[1] == 'delete':
    id = int(terminal_commands[2])
    delete_task_by_id(id)


#mark-in-progress
if terminal_commands[1] == 'mark-in-progress':
    id = int(terminal_commands[2])
    mark_task_by_id(id, 'in-progress')
    
#mark-done
if terminal_commands[1] == 'mark-done':
    id = int(terminal_commands[2])
    mark_task_by_id(id, 'done')

#update
if terminal_commands[1] == 'update':
    id = int(terminal_commands[2])
    new_note = terminal_commands[3]
    update_task_by_id(id, new_note)

#list
if terminal_commands[1] == 'list':
  list_all_tasks()
