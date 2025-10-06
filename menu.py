from add_task import add_task
from view_tasks import view_tasks
from update_task import update_task
from mark_done import mark_done
from delete_task import delete_task

def menu():
    tasks = []
    while True:
        print("===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")
