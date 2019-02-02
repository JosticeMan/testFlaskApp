"""
File: flask_app.py
Version: 1.0
Description: First flask app for educational and testing purposes
Author: Justin Yau
"""
from flask import Flask
app = Flask(__name__)


# Use set FLASK_APP=python_file_name.py to start flask
@app.route("/")
def hello():
    return "Hello World!"
