def view_tasks(tasks):
    """Display all tasks in the list."""
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n===== To-Do List =====")
    for task in tasks:
        print(f"ID: {task['id']} | Task: {task['task']} | Status: {task['status']}")
    print()
