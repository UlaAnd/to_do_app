import os
import json
from flask import Flask, current_app
from controller.tasks import TaskController

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    return app

def display_menu():
    print("\nTask Manager Menu")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")


def main():
    app = create_app()
    with app.app_context():
        controller = TaskController()

        while True:
                display_menu()
                choice = input("Choose an option (1-3): ")

                if choice == '1':
                    title = input("Enter task title: ")
                    description = input("Enter task description: ")
                    if not title or not description:
                        print("Error: Both title and description are required.")
                    else:
                        data = {
                            'title': title,
                            'description': description,
                        }
                        task = controller.add_task(data)
                        print(f"Task added: {task}")

                elif choice == '2':
                    tasks = controller.list_tasks()
                    if not tasks:
                        print("No tasks found.")
                    for task in tasks:
                        print(
                            f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {task['status']}")

                elif choice == '3':
                    print("Exiting...")
                    break

                else:
                    print("Invalid choice, please choose a valid option (1-3).")


if __name__ == '__main__':
    main()
