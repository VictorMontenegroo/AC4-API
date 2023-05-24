import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/pg1/todos', methods=['GET'])
def get_todos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response.json()
    return jsonify(todos), response.status_code

@app.route('/pg2/todos', methods=['POST'])
def create_todo():
    todo = {"userId": 1, "title": "Buy milka", "completed": False}
    response = requests.post('https://jsonplaceholder.typicode.com/todos', json=todo)
    return jsonify(response.json()), response.status_code

@app.route('/pg3/todos', methods=['DELETE'])
def delete_todo():
    response = requests.delete(f'https://jsonplaceholder.typicode.com/todos/10')
    return '', response.status_code

if __name__ == '__main__':
    app.run()