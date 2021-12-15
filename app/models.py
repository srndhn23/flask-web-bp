# from datetime import datetime
from app import db, login_manager, bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return loginn.query.get(int(user_id))


class loginn(db.Model,UserMixin):
    id = db.Column('id', db.Integer, primary_key=True)
    nama = db.Column('nama', db.String(100), nullable=False)
    username = db.Column('username', db.String(20), unique=True, nullable=False)
    email = db.Column('email', db.String(50), unique=True, nullable=False)
    password = db.Column('password', db.String(60), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
   
    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.licenceplate}')"

# class LUser(db.Model,UserMixin):
#     __bind_key__ = 'db2'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)

    # def __repr__(self):
    #     return f"LUser('{self.username}', '{self.email}''{self.image_file}',)"

