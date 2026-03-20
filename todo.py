# todo.py - Simple Command Line To-Do App
import json
import os

SAVE_FILE = "tasks.json"
tasks = []

def save_tasks():
    """Save tasks to a JSON file"""
    with open(SAVE_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
    print("Tasks saved!")

def load_tasks():
    """Load tasks from JSON file if it exists"""
    global tasks
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            tasks = json.load(f)
        print(f"Loaded {len(tasks)} task(s) from save file.")

def add_task(task):
    """Add a new task to the list"""
    tasks.append({"task": task, "done": False})
    print(f"Task added: {task}")

def show_tasks():
    """Display all tasks"""
    if not tasks:
        print("No tasks yet! Add one with: add")
        return
    print("\n--- Your To-Do List ---")
    for i, item in enumerate(tasks, 1):
        status = "Done" if item["done"] else "Pending"
        print(f"{i}. [{status}] {item['task']}")
    print("-----------------------\n")

def complete_task(task_number):
    """Mark a task as completed"""
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number!")
        return
    tasks[task_number - 1]["done"] = True
    print(f"Task completed: {tasks[task_number - 1]['task']}")

def delete_task(task_number):
    """Delete a task from the list"""
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number!")
        return
    removed = tasks.pop(task_number - 1)
    print(f"Task deleted: {removed['task']}")

def main():
    print("Welcome to Todo App v1.1.0!")
    load_tasks()
    print("Commands: add | show | complete | delete | save | quit")
    while True:
        command = input("\nEnter command: ").strip().lower()
        if command == "add":
            task = input("Enter task: ").strip()
            if not task:
                print("Task cannot be empty!")
            else:
                add_task(task)
        elif command == "show":
            show_tasks()
        elif command == "complete":
            show_tasks()
            try:
                num = int(input("Enter task number to complete: "))
                complete_task(num)
            except ValueError:
                print("Please enter a valid number!")
        elif command == "delete":
            show_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("Please enter a valid number!")
        elif command == "save":
            save_tasks()
        elif command == "quit":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try: add | show | complete | delete | save | quit")

if __name__ == "__main__":
    main()