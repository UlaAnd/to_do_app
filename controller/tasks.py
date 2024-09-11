import json
import os
from typing import Dict, List, Optional

from flask import current_app


class TaskController:
    def __init__(self) -> None:
        self.tasks: list = []
        self.task_id_counter: int = 1
        self.STATUS_OPTIONS = ["to do", "in progress", "done"]
        self.file_path = os.path.join(
            current_app.config["TEXT_FILE_DIR"], "to_do_list.json"
        )
        self.load_tasks()

    def load_tasks(self) -> None:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    self.tasks = json.load(f)
                except json.JSONDecodeError:
                    self.tasks = []

    def save_tasks(self) -> None:
        with open(self.file_path, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, data: dict) -> dict:
        if not data or "title" not in data or not data["title"].strip():
            return {"code": 400, "message": "Title is required and cannot be empty."}
        if "description" not in data or not data["description"].strip():
            return {
                "code": 400,
                "message": "Description is required and cannot be empty.",
            }

        if self.tasks:
            self.task_id_counter = max(task["id"] for task in self.tasks) + 1
        new_task = {
            "id": self.task_id_counter,
            "title": data["title"].strip(),
            "description": data["description"].strip(),
            "status": "to do",
        }
        self.tasks.append(new_task)
        self.save_tasks()
        return {
            "code": 201,
            "message": f"Task '{data['title']}' has been saved.",
            "task": new_task,
        }

    def get_tasks(self) -> List:
        return self.tasks

    def get_task(self, task_id: int) -> Dict[str, int | str]:
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            return {"code": 404, "message": "Task not found"}
        return {"code": 200, "task": task}

    def update_task(self, task_id: int, data: dict) -> Dict[str, int | str]:
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        changes = ""
        if task is None:
            return {"code": 404, "message": "Task not found"}
        if "title" in data and data["title"]:
            task["title"] = data["title"].strip()
            changes += "- title"
        if "description" in data and data["description"]:
            task["description"] = data["description"].strip()
            changes += " - decscription"
        if "status" in data and data["status"]:
            if data["status"] in [1, 2, 3]:
                task["status"] = self.STATUS_OPTIONS[data["status"] - 1]
                changes += " - status"
            else:
                return {
                    "code": 400,
                    "message": "Invalid status. Please enter a number between 1 and 3:\n"
                    "1 - 'to do'\n"
                    "2 - 'in progress'\n"
                    "3 - 'done'",
                }

        self.save_tasks()
        return {
            "code": 200,
            "message": f"Task with id: {task_id} has been updated. You changed : {changes}",
        }

    def delete_task(
        self, task_id: Optional[int] = None, task_title: Optional[str] = None
    ) -> Dict:
        if not task_id and not task_title:
            return {
                "code": 400,
                "message": "Please provide either task ID or task title.",
            }
        task = None
        if task_id is not None:
            task = next((t for t in self.tasks if t["id"] == task_id), None)
        elif task_title:
            task = next(
                (t for t in self.tasks if t["title"].lower() == task_title.lower()),
                None,
            )
        if not task:
            return {
                "code": 404,
                "message": "Task not found.",
            }
        self.tasks = [t for t in self.tasks if t != task]
        self.save_tasks()
        return {
            "code": 200,
            "message": "Task has been deleted.",
        }

    def get_tasks_by_status(self, status_choice: int) -> List:
        status = self.STATUS_OPTIONS[status_choice - 1]
        filtered_tasks = [task for task in self.tasks if task["status"] == status]
        return filtered_tasks
