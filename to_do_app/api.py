import json
import os

from flask import jsonify, request, abort, Blueprint, current_app

from controller.tasks import TaskController

api_bp = Blueprint('api', __name__)



@api_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    controller = TaskController()
    response = controller.add_task(data)
    return response

# @api_bp.route('/tasks', methods=['GET'])
# def get_tasks():
#     controller = TaskController()
#     response = controller.add_task()
#     return jsonify(tasks), 200


# @api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = find_task(task_id)
#     if task is None:
#         abort(404, description="Task not found")
#
#     data = request.json
#     if 'title' in data:
#         task['title'] = data['title']
#     if 'description' in data:
#         task['description'] = data['description']
#     if 'status' in data:
#         if data['status'] not in STATUS_OPTIONS:
#             abort(400, description=f"Status must be one of {STATUS_OPTIONS}")
#         task['status'] = data['status']
#
#     return jsonify(task), 200
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
#
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
