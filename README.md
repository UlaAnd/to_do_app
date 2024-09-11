# To-Do List Management System

This is a simple to-do list management system built with Flask. The system allows users to manage tasks through both a terminal-based interface and a RESTful API. Each task includes a title, description, and status ("to do", "in progress", "done"). The system supports adding, deleting, updating, and displaying tasks.

## Features

- **Terminal Interface**: A simple command-line interface (CLI) to interact with the system.
- **RESTful API**: A Flask-based API to manage tasks using HTTP methods.
- **Data Persistence**: Task data is stored in a file.
- **Test Coverage**: Unit tests using `pytest`.

## Requirements

- Python 3.x
- Poetry (Dependency Management)

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/UlaAnd/to_do_app
    cd to_do_app
    ```

2. **Install dependencies** using Poetry:

    ```bash
    poetry install
    ```

3. **Activate the virtual environment**:

    ```bash
    poetry shell
    ```

4. **Set the `FLASK_APP` environment variable**:

    ```bash
    export FLASK_APP=to_do_app/run
    ```

5. **Run the Flask server**:

    To start the server using Flask's built-in command:

    ```bash
    flask run
    ```

    Alternatively, you can run the server directly from the `run.py` script:

    ```bash
    python to_do_app/run.py
    ```

   The Flask API will be available at `http://127.0.0.1:5000`.

6. **Run the Terminal Interface**:

    You can start the CLI by running the following command:

    ```bash
    python to_do_app/cli.py
    ```
   

      This will launch a text-based menu where you can add, update, delete, and display tasks.

7. **Give Execute Permissions to linter scripts**
    ```bash
    chmod +x ./td
    ```
   
8. **Run Linters (mypy, black, isort, flake8)**
    ```bash
    ./td lint
    ```


## API Endpoints

- **GET /tasks**: Retrieve all tasks.
- **GET /tasks/<id>**: Retrieve specific task by ID.
- **POST /tasks**: Add a new task (requires `title`, `description`, and `status`).
- **PUT /tasks/<id>**: Update a task (provide `id` and any fields to update).
- **DELETE /tasks/<id>**: Delete a task by ID.

## Running Tests

To run the test suite using `pytest`, execute:

```bash
pytest
