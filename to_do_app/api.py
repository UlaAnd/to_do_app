from flask import Blueprint, jsonify, request

from controller.tasks import TaskController

api_bp = Blueprint("api", __name__)


@api_bp.route("/tasks", methods=["POST"])
def add_task() -> tuple:
    data = request.json
    controller = TaskController()
    response = controller.add_task(data)
    return jsonify(response), response["code"]


@api_bp.route("/tasks", methods=["GET"])
def get_tasks() -> tuple:
    controller = TaskController()
    response = controller.get_tasks()
    return jsonify(response), 200


@api_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id: int) -> tuple:
    controller = TaskController()
    response = controller.get_task(task_id=task_id)
    return jsonify(response), 200


@api_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id: int) -> tuple:
    data = request.json
    controller = TaskController()
    response = controller.update_task(task_id=task_id, data=data)
    return jsonify(response), response["code"]


@api_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int) -> tuple:
    controller = TaskController()
    response = controller.delete_task(task_id=task_id)
    return jsonify(response), response["code"]


# @api_bp.errorhandler(400)
# def handle_400_error(e):
#     return jsonify({'error': str(e)}), 400
#
# @api_bp.errorhandler(404)
# def handle_404_error(e):
#     return jsonify({'error': str(e)}), 404
#
#
# @api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     global tasks
#     task = find_task(task_id)
#     if task is None:
#         abort(404, description="Task not found")
#
#     tasks = [t for t in tasks if t['id'] != task_id]
#     return jsonify({'message': f'Task {task_id} deleted successfully'}), 200
