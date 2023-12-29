from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build REST API", "done": False},
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todos})


@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = {
        "id": len(todos) + 1,
        "task": request.json['task'],
        "done": False,
    }
    todos.append(new_todo)
    return jsonify({"todo": new_todo}), 201


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        return jsonify({"todo": todo})
    return jsonify({"message": "Todo not found"}), 404


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        todo['task'] = request.json['task']
        todo['done'] = request.json['done']
        return jsonify({"todo": todo})
    return jsonify({"message": "Todo not found"}), 404


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
