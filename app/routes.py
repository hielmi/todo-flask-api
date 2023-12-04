from app import app 
from .controller import UserController

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users')
def getUsers():
    return UserController.index()


