def mark_done(tasks):
    """Mark a task as Done."""
    if not tasks:
        print("\nNo tasks available.\n")
        return

    try:
        task_id = int(input("Enter task ID to mark as done: "))
        for task in tasks:
            if task['id'] == task_id:
                if task['status'] == "Done":
                    print("Task is already marked as done!\n")
                else:
                    task['status'] = "Done"
                    print(f"Task '{task['task']}' marked as done!\n")
                return
        print("Task not found!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")
