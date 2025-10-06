def update_task(tasks):
    """Update a task's description based on ID."""
    if not tasks:
        print("\nNo tasks to update.\n")
        return

    try:
        task_id = int(input("Enter task ID to update: "))
        for task in tasks:
            if task['id'] == task_id:
                new_desc = input("Enter new task description: ").strip()
                if new_desc:
                    task['task'] = new_desc
                    print("Task updated successfully!\n")
                else:
                    print("Description cannot be empty!\n")
                return
        print("Task not found!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")
