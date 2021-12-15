from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'j\xd6\xafq\xab\x08-F\xf1\xd7d\xc0\xe74o\n{A0g9\xe4Q>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://susi:root@localhost/bp'

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# class login(db.Model):
#     __tablename__ = 'login'
#     id = db.Column('id', db.Integer, primary_key=True)
#     nama = db.Column('nama', db.String(100), unique=True, nullable=False)
#     username = db.Column('username', db.String(20), unique=True, nullable=False)
#     email = db.Column('email', db.String(50), unique=True, nullable=False)
#     password = db.Column('password', db.Unicode(20), nullable=False)

from app import routes