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