from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user

# remember that routes.py functions are called VIEW functions


# this callback creates an association b/w this function and the url
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # prevents a logged in user from accessing the login page
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # handles the login information
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('main.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

