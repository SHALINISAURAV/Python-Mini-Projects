#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

# File to store tasks
FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from file (if exists)."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.read().splitlines()
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display the to-do list."""
    if not tasks:
        print("\n✅ No tasks in your list!")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("➕ Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

def remove_task(tasks):
    """Remove a task from the list."""
    show_tasks(tasks)
    try:
        task_num = int(input("❌ Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"✅ Removed task: {removed_task}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    """Main function to run the To-Do List app."""
    tasks = load_tasks()
    while True:
        print("\n📌 To-Do List Menu:")
        print("1️⃣ View Tasks")
        print("2️⃣ Add Task")
        print("3️⃣ Remove Task")
        print("4️⃣ Exit")
        choice = input("👉 Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Your tasks are saved!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-4.")

# Run the app
main()


# In[ ]:




