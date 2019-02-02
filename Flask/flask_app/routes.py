"""
File: routes.py
Version: 1.1
Description: First flask app for educational and testing purposes
Author: Justin Yau
Source: Tutorial followed can be found at https://www.youtube.com/watch?v=QnDWIZuWYW0
Packages: Flask, Flask-SQlAlchemy, Flask-BCrypt, Flask-Login
"""
from flask import render_template, url_for, flash, redirect, request
from flask_app import app, db, bcrypt
from flask_app.forms import RegistrationForm, LoginForm
from flask_app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data.lower(), password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
