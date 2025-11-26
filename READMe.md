TASK MANAGER – Python Project

Overview

This Task Manager lets users maintain a list of tasks within a program.
It stores tasks temporarily in a Python list and permanently in a text file (tasks.txt).

Features
✔Add a new task

Users can input any task they want to save.

✔View all tasks

Displays all tasks with numbering.

✔Delete a task

Removes any selected task by number.

✔ Save tasks to a file

Writes all tasks from the Python list into tasks.txt.

✔ Load tasks from a file

Reads tasks from tasks.txt and restores them into the list.

✔ Exit

Cleanly closes the program.

📂 Project Structure
Task Manager
│
├── task_manager.py   # Main program file
└── tasks.txt         # Automatically created when saving

How It Works
1. In-memory storage

All tasks are stored in a Python list:

tasks = []

2. Saving tasks

When the user chooses "Save Task", each task in the list is written as a separate line into tasks.txt.

3. Loading tasks

When the user chooses "Load Task", each line from the file is read and placed back into the list.

How to Run the Program

Make sure Python 3 is installed.

Save the code in a file named task_manager.py.

Open your terminal or command prompt.

Run:

python task_manager.py


Choose options from the menu:

1 - Add Task
2 - Save Task
3 - View Task
4 - Delete Task
5 - Load Task
6 - Exit

Sample Output
1 - Add Task
2 - Save Task
3 - View Task
4 - Delete Task
5 - Load Task
6 - Exit

Enter your choice: 1
Enter a new task: Study Python
Task Added!

Educational Concepts Used

This project demonstrates:

List operations (append, pop, clear)

Functions

Menu-driven logic

While loops

If–elif–else

File handling (open, write, read)

Exception handling (FileNotFoundError)

Perfect for college first-year Python assignments.

Future Improvements (Optional)

Add task priority levels

Add due dates

Save tasks using JSON

Create a GUI using Tkinter

Add task editing option
Educational Concepts Used

This project demonstrates:

List operations (append, pop, clear)

Functions

Menu-driven logic

While loops

If–elif–else

File handling (open, write, read)

Exception handling (FileNotFoundError)

Perfect for college first-year Python assignments.

Future Improvements (Optional)

Add task priority levels

Add due dates

Save tasks using JSON

Create a GUI using Tkinter

Add task editing option
