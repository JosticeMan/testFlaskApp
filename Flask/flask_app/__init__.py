"""
File: __init__.py
Version: 1.1
Description: First flask app for educational and testing purposes
Author: Justin Yau
Source: Tutorial followed can be found at https://www.youtube.com/watch?v=QnDWIZuWYW0
Packages: Flask, Flask-SQlAlchemy, Flask-BCrypt, Flask-Login
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'cc567a24de5382dff2a86adcc98c3589'
# 3 forward slashes tell the program to create the database within relative directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flask_app import routes