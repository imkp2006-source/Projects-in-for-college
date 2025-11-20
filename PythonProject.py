# TASK MANAGER
tasks = []

def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print("Task Added!\n")

def view_task():
    if len(tasks) == 0:
        print("No task found!\n")
        return
    for i in range(len(tasks)):
        print(i+1, ":", tasks[i])
    print()

def save_task():
    f = open("tasks.txt", "w")
    for t in tasks:
        f.write(t + "\n")
    f.close()
    print("Tasks saved successfully!\n")

def load_task():
    try:
        f = open("tasks.txt", "r")
        tasks.clear()  
        for line in f:
            tasks.append(line.strip())
        f.close()
        print("Tasks loaded!\n")
    except FileNotFoundError:
        print("No saved file found!\n")

def delete_task():
    view_task()
    if len(tasks) == 0:
        return
    try:
        n = int(input("Enter the task number to delete: "))
        if 1 <= n <= len(tasks):
            tasks.pop(n - 1)
            print("Task deleted!\n")
        else:
            print("Invalid number\n")
    except ValueError:
        print("Please enter a valid number!\n")

# MAIN MENU
while True:
    print("1 - Add Task")
    print("2 - Save Task")
    print("3 - View Task")
    print("4 - Delete Task")
    print("5 - Load Task")
    print("6 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        save_task()
    elif choice == "3":
        view_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        load_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Enter a valid choice!\n")