import os

# Define the file where tasks will be stored
TASKS_FILE = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
    return [task.strip() for task in tasks]

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

# Function to display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] += " (Completed)"
                print(f"Task '{tasks[task_number - 1]}' marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                task = tasks.pop(task_number - 1)
                print(f"Task '{task}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

# Main function for the to-do list app
def todo_list_app():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List App")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Run the To-Do List App
todo_list_app()
