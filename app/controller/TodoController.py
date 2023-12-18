from app.model.Todo import Todos as Todo
from flask import request, jsonify
from app import db
from app.utils.transform import transformTodos, singleTransformTodo
from app.utils import response
from datetime import datetime

def index():
    try:
        id = request.args.get('user_id')
        todo = Todo.query.filter_by(user_id=id).all()
        data = transformTodos(todo)
        return response.ok(data, "Get data succes")
    except Exception as e:
        print(e)
        return response.badRequest([], "failed to get data")
    
def store():
    try:
        todo = request.json['todo']
        desc = request.json['description']
        user_id = request.json['user_id']

        todo = Todo(user_id= user_id, todos=todo, description=desc)
        db.session.add(todo)
        db.session.commit()
        return response.ok(singleTransformTodo(todo),  "Todo added")
    except Exception as err:
        print(err)
        return response.badRequest([], "failed to add todo")
    
def update(id):
    try:
        todoUpdate = request.json['todo']
        desc = request.json['description']
        todo = Todo.query.filter_by(id=id).first()
        todo.todos = todoUpdate
        todo.description = desc
        todo.updated_at = datetime.utcnow()
        db.session.add(todo)
        db.session.commit()

        todo_data= singleTransformTodo(todo)
        
        return response.ok([todo_data], f"Todo updated: {todo.id}, Todo updated")
    except Exception as e:
        print(e)
        return response.badRequest([], "failed to update todo")
    
def delete(id):
    try:
        todo = Todo.query.filter_by(id=id).first()
        if todo is None:
            return response.badRequest([], "Todo not found")
        db.session.delete(todo)
        db.session.commit()
        return response.ok([], "Todo deleted")
    except Exception as e:
        print(e)
        return response.badRequest([], "failed to delete todo")

def show(id):
    try:
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            return response.badRequest([], "Todo not found")
        
        data = singleTransformTodo(todo)
        return response.ok(data, "Get todo success")
    except Exception as e:
        print(e)
        return response.badRequest([], "failed to update todo")
