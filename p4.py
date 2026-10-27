
tasks = []

while True:
    print("\n--- Task Scheduler ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Run Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter task name: ")
        priority = input("Is it a priority task? (yes/no): ").lower()
        ready = input("Is the task ready? (yes/no): ").lower()

        tasks.append({
            "name": name,
            "priority": priority == "yes",
            "ready": ready == "yes"
        })

        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nScheduled Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(
                    i, task["name"],
                    "| Priority:", task["priority"],
                    "| Ready:", task["ready"]
                )

    elif choice == "3":
        if not tasks:
            print("No tasks to run.")
        else:
            remaining = []

            for task in tasks:
                if task["priority"] and task["ready"]:
                    print("Executing priority task:", task["name"])
                elif task["ready"] and not task["priority"]:
                    print("Executing normal task:", task["name"])
                elif not task["ready"] or not task["priority"]:
                    print("Task postponed:", task["name"])
                    remaining.append(task)
                else:
                    remaining.append(task)

            tasks = remaining

    elif choice == "4":
        print("Exiting Task Scheduler.")
        break

    else:
        print("Invalid choice. Please try again.")
