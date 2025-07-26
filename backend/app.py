# === backend/app.py ===
from flask import Flask, request, jsonify
app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json.get("task")
    tasks.append({"task": task})
    return jsonify({"message": "Task added"}), 201
