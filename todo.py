# todo.py - Simple Command Line To-Do App

tasks = []

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

def main():
    print("Welcome to Todo App!")
    print("Commands: add | show | quit")
    while True:
        command = input("\nEnter command: ").strip().lower()
        if command == "add":
            task = input("Enter task: ").strip()
            add_task(task)
        elif command == "show":
            show_tasks()
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try: add | show | quit")

if __name__ == "__main__":

    main()
def main():
    print("Welcome to Todo App!")
    print("Commands: add | show | complete | quit")
    while True:
        command = input("\nEnter command: ").strip().lower()
        if command == "add":
            task = input("Enter task: ").strip()
            add_task(task)
        elif command == "show":
            show_tasks()
        elif command == "complete":
            show_tasks()
            num = int(input("Enter task number to complete: "))
            complete_task(num)
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try: add | show | complete | quit")