# task manager program
tasks = []

def add_task():
    t = input("Enter a task: ")
    tasks.append(t)
    print("Task added\n")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet\n")
        return
    for i in range(len(tasks)):
        print(i+1, tasks[i])
    print()


def save_tasks():
    f = open("tasks.txt","w")
    for t in tasks:
        f.write(t + "\n")
    f.close()
    print("Saved\n")


def load_tasks():
    try:
        f = open("tasks.txt","r")
        tasks.clear()
        for line in f:
            tasks.append(line.strip())
        f.close()
        print("Loaded\n")
    except:
        print("No file found\n")


def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        n = int(input("which task number to delete: "))
        if n > 0 and n <= len(tasks):
            tasks.pop(n-1)
            print("deleted\n")
        else:
            print("wrong number\n")
    except:
        print("enter a number only\n")


while True:
    print("1 add")
    print("2 save")
    print("3 view")
    print("4 delete")
    print("5 load")
    print("6 exit")

    ch = input("choice: ")

    if ch == "1":
        add_task()
    elif ch == "2":
        save_tasks()
    elif ch == "3":
        view_tasks()
    elif ch == "4":
        delete_task()
    elif ch == "5":
        load_tasks()
    elif ch == "6":
        print("bye")
        break
    else:
        print("Invalid\n")
