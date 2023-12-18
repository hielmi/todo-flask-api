from flask import request
from app import db
from app.utils import response
from app.model import Users
from app.utils.PasswordGenerate import checkPassword, setPassword

def login():
    try: 
        email = request.json['email']
        paswd = request.json['password']

        user = Users.query.filter_by(email=email).first()
        if user is None:
            return response.badRequest("", "user not found")
        if checkPassword(user.password, paswd):
            return response.ok({"id": user.id, "name": user.name, "email": user.email}, "user logged in")
        else:
            return response.badRequest("", "invalid credentials")
    except Exception as err:
        print(err)
        return response.badRequest("", "failed to login")

def register():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        if Users.query.filter_by(email=email).first() is not None:
            return response.badRequest("", "email already exists")
        
        user = Users(name=name, email=email)
        user.password = setPassword(password)
        
        db.session.add(user)
        db.session.commit()
        return response.ok({"id": user.id, "name": user.name, "email": user.email}, "user added")
    except Exception as e:
        print(e)
        return response.badRequest("", "failed to add user")