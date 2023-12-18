from app import bcrypt, db, app
from app.model import Users
from app.utils import response, singleTransformUser, transformUsers
from app.utils.PasswordGenerate import setPassword, checkPassword
from flask import request

def index():
    try:
        users = Users.query.all()
        data = transformUsers(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest("", "failed to get users")

def addUser():
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

def show(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if user is None:
            return response.badRequest("", "user not found")
        data = singleTransformUser(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest("", "failed to get user")
    
def update(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if user is None:
            return response.badRequest("", "user not found")
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        user.name = name
        user.email = email
        user.password = setPassword(password)
        db.session.commit()
        return response.ok({"id": user.id, "name": user.name, "email": user.email}, "user updated")
    except Exception as e:
        print(e)
        return response.badRequest("", "failed to update user")
    
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if user is None:
            return response.badRequest("", "user not found")
        db.session.delete(user)
        db.session.commit()
        return response.ok("", "user deleted")
    except Exception as e:
        print(e)
        return response.badRequest("", "failed to delete user")




