def delete_task(tasks):
    """Delete a task based on ID."""
    if not tasks:
        print("\nNo tasks to delete.\n")
        return

    try:
        task_id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)
                print("Task deleted successfully!\n")
                # Reassign IDs
                for i, t in enumerate(tasks, start=1):
                    t['id'] = i
                return
        print("Task not found!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")
