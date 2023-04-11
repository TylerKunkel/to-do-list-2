# define an empty list to hold the tasks
tasks = []

# define a function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

# define a function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Your tasks:")
        for task in tasks:
            print("- " + task)

# define a function to delete a task
def delete_task():
    task_to_delete = input("Enter the task you want to delete.\n The task is case sensitive: ")
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        print("Task deleted successfully!")
    else:
        print("Task not found.")

# main loop
#print() is used for spacing preferences in the output. 
while True:
    print("\n")
    print("To-Do App")
    print()
    print("------------------")
    print("1. Add a new task")
    print()
    print("2. View all tasks")
    print()
    print("3. Delete a task")
    print()
    print("4. Quit")
    print("------------------")
    print()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print()
        print("Thank you for playing!")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
