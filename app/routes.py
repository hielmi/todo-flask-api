from app import app 
from .controller import UserController, AuthController, TodoController
from flask import request
from flask_jwt_extended import jwt_required
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return UserController.addUser()
    else:
        return UserController.index()
    
@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)
    
@app.route('/login', methods=['POST'])
def login():
    return AuthController.login()


# todo
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        return TodoController.store()
    else:
        return TodoController.index()
    
@app.route('/todo/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def todoDetail(id):
    if request.method == 'GET':
        return TodoController.show(id)
    elif request.method == 'PUT':
        return TodoController.update(id)
    elif request.method == 'DELETE':
        return TodoController.delete(id)

@app.route('/refresh', methods=['GET'])
def refresh():
    return AuthController.refresh()


