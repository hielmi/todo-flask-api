from app import db
from datetime import datetime
from app.model.User import Users

class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key= True, autoincrement=True)
    todos = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text,  nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    users = db.relationship("Users", backref="user_id")
    access_token = db.Column(db.Text, nullable=False)
    refresh_token = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Todos {}>'.format(self.name)