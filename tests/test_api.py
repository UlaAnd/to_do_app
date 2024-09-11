import json
import os

import pytest

from config import TestConfig
from to_do_app import create_app

test_file_path = os.path.join(TestConfig.TEXT_FILE_DIR, "to_do_list.txt")


@pytest.fixture
def client() -> None:
    app = create_app()
    app.config.from_object(TestConfig)
    app.config["TESTING"] = True
    if not os.path.exists(app.config["TEXT_FILE_DIR"]):
        os.makedirs(app.config["TEXT_FILE_DIR"])

    with open(test_file_path, "w") as f:
        initial_tasks = [
            {
                "id": 1,
                "title": "Task 1",
                "description": "Description 1",
                "status": "to do",
            },
            {
                "id": 2,
                "title": "Task 2",
                "description": "Description 2",
                "status": "in progress",
            },
        ]
        json.dump(initial_tasks, f, indent=4)
    with app.test_client() as client:
        yield client

    if os.path.exists(test_file_path):
        os.remove(test_file_path)


def test_get_task(client) -> None:
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json[0]["title"] == "Task 1"
    assert len(response.json) == 2


def test_add_task(client) -> None:
    new_task_data = {"title": "Test Task", "description": "This is a test task"}
    response = client.post("/tasks", json=new_task_data)
    with open(test_file_path, "r") as f:
        tasks = json.load(f)
    new_task = tasks[2]
    assert response.status_code == 201
    assert response.json["message"] == "Task 'Test Task' has been saved."
    assert new_task["title"] == "Test Task"
    assert new_task["id"] == 3


def test_update_task(client) -> None:
    response = client.put(
        "/tasks/1",
        json={
            "description": "Updated Description 1",
            "status": 3,
        },
    )
    with open(test_file_path, "r") as f:
        tasks = json.load(f)
    assert response.status_code == 200
    assert (
        response.json["message"]
        == "Task with id: 1 has been updated. You changed :  - decscription - status"
    )
    assert tasks[0]["description"] == "Updated Description 1"
    assert tasks[0]["status"] == "done"


def test_delete_task(client) -> None:
    response = client.delete("/tasks/1")
    with open(test_file_path, "r") as f:
        tasks = json.load(f)
    assert response.status_code == 200
    assert response.json["message"] == "Task with id: 1 has been deleted."
    assert len(tasks) == 1
