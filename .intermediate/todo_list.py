# todo_list.py
import json

TODO_FILE = "todos.json"

def load_todos():
    try:
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)

def add_task(task):
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print(f"Task '{task}' added.")

def list_tasks():
    todos = load_todos()
    print("To-Do List:")
    for i, task in enumerate(todos, 1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    add_task("Learn Python")
    add_task("Build a project")
    list_tasks()
