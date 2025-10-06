def add_task(tasks):
    """Add a new task to the list (max 8 tasks)."""
    if len(tasks) >= 8:
        print("\nTask limit reached! Maximum 8 tasks allowed.\n")
        return

    task_desc = input("Enter task description: ").strip()
    if not task_desc:
        print("Task description cannot be empty!")
        return

    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "task": task_desc, "status": "Pending"})
    print(f"Task '{task_desc}' added successfully!\n")
