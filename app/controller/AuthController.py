from flask import request
from app import db
from app.utils import response
from app.model import Users
from app.utils.PasswordGenerate import checkPassword, setPassword
from app.utils.transform import singleTransformUser
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, jwt_required

def login():
    try: 
        email = request.json['email']
        paswd = request.json['password']

        user = Users.query.filter_by(email=email).first()
        if user is None:
            return response.badRequest("", "user not found")
        if not checkPassword(user.password, paswd):
            return response.badRequest("", "invalid credentials")
        

        data = singleTransformUser(user, withTodo=False)
        expires = timedelta(days=1)
        expires_refresh = timedelta(days=3)
        access_token = create_access_token(identity=data, expires_delta=expires)
        refresh_token = create_refresh_token(identity=data, expires_delta=expires_refresh)

        return response.ok({"data": data, "access_token": access_token, "refresh_token": refresh_token}, "user logged in")
        
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
    
@jwt_required(refresh=True)
def refresh():
    try:
        user = get_jwt_identity()
        access_token = create_access_token(identity=user, expires_delta=timedelta(days=1))
        return response.ok({"access_token": access_token}, "user logged in")
    except Exception as e:
        print(e)
        return response.badRequest("", "failed to refresh token")