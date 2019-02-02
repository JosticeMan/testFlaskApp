"""
File: __init__.py
Version: 1.1
Description: First flask app for educational and testing purposes
Author: Justin Yau
Source: Tutorial followed can be found at https://www.youtube.com/watch?v=QnDWIZuWYW0
Packages: Flask, Flask-SQlAlchemy
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'cc567a24de5382dff2a86adcc98c3589'
# 3 forward slashes tell the program to create the database within relative directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flask_app import routes