from app import app

# remember that routes.py functions are called VIEW functions

# this callback creates an association b/w this function and the url
@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"