from flask import render_template
from app import app
from app.forms import LoginForm

# remember that routes.py functions are called VIEW functions

# this callback creates an association b/w this function and the url
@app.route('/')
@app.route('/index')
@app.route('/about')
def index():
    form = LoginForm()
    # user = {'username': 'Rolo'}
    return render_template('index.html', 
                           title='Sign In to Rolo!',
                           form=form)
