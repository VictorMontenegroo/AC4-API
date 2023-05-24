import requests
from flask import Flask

app = Flask(__name__)

API_URL = 'http://localhost:5000'

@app.route('/todos', methods=['GET'])
def get_todos():
    response = requests.get(f'{API_URL}/todos')
    return response.text, response.status_code

@app.route('/todos', methods=['POST'])
def create_todo():
    todo = {'title': 'Example Todo', 'completed': False}
    response = requests.post(f'{API_URL}/todos', json=todo)
    return response.text, response.status_code

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo():
    response = requests.delete(f'{API_URL}/todos')
    return '', response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5001)