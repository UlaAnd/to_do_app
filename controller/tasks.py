import json
import os
from typing import Any, Dict, List, Optional

from flask import abort, current_app


class TaskController:
    def __init__(self) -> None:
        self.tasks: list = []
        self.task_id_counter: int = 1
        self.STATUS_OPTIONS = ["to do", "in progress", "done"]
        self.file_path = os.path.join(
            current_app.config["TEXT_FILE_DIR"], "to_do_list.txt"
        )
        self.load_tasks()

    def load_tasks(self) -> None:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    self.tasks = json.load(f)
                except json.JSONDecodeError:
                    self.tasks = []

    def add_task(self, data: dict) -> dict:
        if not data or "title" not in data or "description" not in data:
            return {"code": 400, "message": "Title and description are required"}
        if self.tasks:
            self.task_id_counter = max(task["id"] for task in self.tasks) + 1
        new_task = {
            "id": self.task_id_counter,
            "title": data["title"],
            "description": data["description"],
            "status": "to do",
        }
        self.tasks.append(new_task)

        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)
        return {
            "message": f"Task '{data['title']}' has been saved.",
            "task": new_task,
        }

    def get_tasks(self) -> List:
        return self.tasks

    def get_task(self, task_id: int) -> Optional[Dict[str, Any]]:
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            return {"code": 404, "message": "Task not found"}
        return task

    def update_task(self, task_id: int, data: dict) -> Optional[Dict]:
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if task is None:
            return {"code": 404, "description": "Task not found"}
        if "title" in data:
            task["title"] = data["title"]
        if "description" in data:
            task["description"] = data["description"]
        if "status" in data:
            if data["status"] in [1, 2, 3]:
                task["status"] = self.STATUS_OPTIONS[data["status"] - 1]
            else:
                return {
                    "code": 404,
                    "message": "Invalid status. Please enter a number between 1 and 3:\n"
                    "1 - 'to do'\n"
                    "2 - 'in progress'\n"
                    "3 - 'done'",
                }

        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)
        return {
            "code": 200,
            "message": f"Task with id: {task_id} has been updated.",
        }

    def delete_task(self, task_id: int) -> Optional[Dict]:
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if task is None:
            return {"code": 404, "description": "Task not found"}
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)
        return {
            "code": 200,
            "message": f"Task with id: {task_id} has been deleted.",
        }
