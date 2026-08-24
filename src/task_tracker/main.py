import sys
from task_tracker.database import ( 
    add_task,
    update_task,
    get_task,
    get_all_tasks,
    delete_task
)


command = sys.argv[1]
if command not in ["add", "update", "delete", "get", "list"]:
    print("Invalid command")
    sys.exit(1)
if command == "add":
    title = sys.argv[2]
    add_task(title)
    sys.exit(0)
if command == "update":
    id = sys.argv[2]
    title = sys.argv[3]
    update_task(id, title)
    sys.exit(0)
if command == "delete":
    id = sys.argv[2]
    delete_task(id)
    sys.exit(0)
if command == "get":
    id = sys.argv[2]
    task = get_task(id)
    print(task)
    sys.exit(0)
if command == "list":
    tasks = get_all_tasks()
    for task in tasks:
        print(task)
    sys.exit(0)

# print(sys.argv)

