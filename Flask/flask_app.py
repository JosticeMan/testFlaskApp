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
@app.route("/home")
def home():
    return "Hello World!"


@app.route("/about-me")
def about():
    return "Justin Yau RIT CS Student"


if __name__ == '__main__':
    app.run(debug=True)
