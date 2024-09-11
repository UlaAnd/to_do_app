import click

from controller.tasks import TaskController
from to_do_app import create_app

app = create_app()


@click.command()
def show_menu():
    with app.app_context():
        controller = TaskController()
        options = {
            1: add_task,
            2: delete_task,
            3: update_task,
            4: display_tasks,
            5: filter_tasks_by_status,
            6: exit_program,
        }

        while True:
            click.echo("\n--- To-Do List Menu ---")
            click.echo("1. Add Task")
            click.echo("2. Delete Task")
            click.echo("3. Update Task")
            click.echo("4. Display All Tasks")
            click.echo("5. Filter Tasks by Status")  # New option in the menu
            click.echo("6. End Program")
            choice = click.prompt("Select an option (1-6)", type=int)
            if choice in options:
                options[choice](controller)
            else:
                click.echo("Invalid choice, please try again.")


def exit_program(controller):
    click.echo("Exiting program.")
    exit()


def add_task(controller):
    title = click.prompt("Enter task title")
    description = click.prompt("Enter task description")
    result = controller.add_task({"title": title, "description": description})
    click.echo(result["message"])


def delete_task(controller):
    identifier_type = click.prompt("Do you want to delete by 'id' or 'title'?", type=click.Choice(['ID', 'title'], case_sensitive=False))

    if identifier_type.lower() == 'id':
        task_id = click.prompt("Enter task ID", type=int)
        result = controller.delete_task(task_id=task_id)
    else:
        task_title = click.prompt("Enter task title")
        result = controller.delete_task(task_title=task_title)

    click.echo(result["message"])


def update_task(controller):
    task_id = click.prompt("Enter task ID to update", type=int)
    title = click.prompt(
        "Enter new title (or leave blank to skip)", default="", show_default=False
    )
    description = click.prompt(
        "Enter new description (or leave blank to skip)", default="", show_default=False
    )
    status_input = click.prompt(
        "Enter new status (1 - 'to do', 2 - 'in progress', 3 - 'done') or leave blank to skip",
        type=int,
        default="",
        show_default=False,
    )
    data = {"title": title, "description": description, "status": status_input}
    result = controller.update_task(task_id, data)
    click.echo(result["message"])


def display_tasks(controller):
    tasks = controller.get_tasks()
    if tasks:
        click.echo("--- All Tasks ---")
        for task in tasks:
            click.echo(
                f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {task['status']}"
            )
    else:
        click.echo("No tasks available.")


def filter_tasks_by_status(controller):
    status_choice = click.prompt(
        "Filter by status: 1 - 'to do', 2 - 'in progress', 3 - 'done'",
        type=int,
        default=None,
        show_choices=False
    )
    if status_choice not in [1, 2, 3]:
        click.echo("Invalid choice. Please select 1, 2, or 3.")
    tasks = controller.get_tasks_by_status(status_choice)
    if tasks:
        click.echo(f"--- Tasks with selected status ---")
        for task in tasks:
            click.echo(
                f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {task['status']}"
            )
    else:
        click.echo(f"No tasks found with selected status.")

if __name__ == "__main__":
    show_menu()
