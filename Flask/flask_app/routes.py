"""
File: routes.py
Version: 1.1
Description: First flask app for educational and testing purposes
Author: Justin Yau
Source: Tutorial followed can be found at https://www.youtube.com/watch?v=QnDWIZuWYW0
Packages: Flask, Flask-SQlAlchemy
"""
from flask import render_template, url_for, flash, redirect
from flask_app import app
from flask_app.forms import RegistrationForm, LoginForm
from flask_app.models import User, Post

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


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
