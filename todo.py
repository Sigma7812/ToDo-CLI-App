Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# todo.py

TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid task number.")
... 
... def view_tasks():
...     tasks = load_tasks()
...     if not tasks:
...         print("No tasks found.")
...     else:
...         print("\nYour To-Do List:")
...         for i, task in enumerate(tasks):
...             print(f"{i}. {task}")
... 
... def main():
...     while True:
...         print("\nTo-Do List Menu:")
...         print("1. View tasks")
...         print("2. Add task")
...         print("3. Remove task")
...         print("4. Exit")
...         
...         choice = input("Enter your choice: ")
...         
...         if choice == "1":
...             view_tasks()
...         elif choice == "2":
...             task = input("Enter the task: ")
...             add_task(task)
...         elif choice == "3":
...             try:
...                 index = int(input("Enter the task number to remove: "))
...                 remove_task(index)
...             except ValueError:
...                 print("Please enter a valid number.")
...         elif choice == "4":
...             print("Goodbye!")
...             break
...         else:
...             print("Invalid choice.")
... 
... if __name__ == "__main__":
...     main()
