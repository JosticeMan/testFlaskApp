"""
File: flask_app.py
Version: 1.1
Description: First flask app for educational and testing purposes
Author: Justin Yau
Source: Tutorial followed can be found at https://www.youtube.com/watch?v=QnDWIZuWYW0
Packages: Flask
"""
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = 'cc567a24de5382dff2a86adcc98c3589'

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


if __name__ == '__main__':
    app.run(debug=True)

