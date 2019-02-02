"""
File: flask_app.py
Version: 1.1
Description: First flask app for educational and testing purposes
Author: Justin Yau
"""
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

posts = [
    {
        "author": "Justin Yau",
        "date": "2/2/2019",
        "content": "RIT CS Student",
        "title": "About Me"
    },
    {
        "author": "Bob",
        "date": "2/2/2019",
        "content": "RIT Game Dev",
        "title": "Some dude"
    }
]


# Use set FLASK_APP=python_file_name.py to start flask
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about-me")
def about():
    return "Justin Yau RIT CS Student"


if __name__ == '__main__':
    app.run(debug=True)

