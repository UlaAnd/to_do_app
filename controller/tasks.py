import json
import os

from flask import jsonify, request, abort, current_app


class TaskController:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1
        self.STATUS_OPTIONS = ['to do', 'in progress', 'done']
        self.file_path = os.path.join(current_app.config['TEXT_FILE_DIR'], 'to_do_list.txt')
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                try:
                    self.tasks = json.load(f)
                    if self.tasks:
                        self.task_id_counter = max(task['id'] for task in self.tasks)
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    def add_task(self, data):
        if not data or not 'title' in data or not 'description' in data:
            abort(400, description="Title and description are required")

        new_task = {
            'id': self.task_id_counter+1,
            'title': data['title'],
            'description': data['description'],
            'status': 'to do'
        }
        self.tasks.append(new_task)

        with open(self.file_path, 'w') as f:
            json.dump(self.tasks, f, indent=4)
        return jsonify({"message": "Text saved", "file_path": self.file_path}), 201

    def list_tasks(self):
        return self.tasks