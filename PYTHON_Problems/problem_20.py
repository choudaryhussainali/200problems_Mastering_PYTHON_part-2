# Build a command-line to-do list:
# - Show menu: Add task, View tasks, Remove task, Exit
# - Store tasks in a list
# - Run in a loop until user exits

# Example:
# 1. Add task
# 2. View tasks
# 3. Remove task
# 4. Exit

tasks = []

while True:
    print("\n--- To-Do Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == '2':
        if not tasks:
            print("No tasks.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

# Sample Interaction:
# 1. Add Task → "Learn Python"
# 2. View Tasks → 1. Learn Python
# 3. Remove Task → Removes by index
# 4. Exit


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
