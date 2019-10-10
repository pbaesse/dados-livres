from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

from flask import render_template    
from app.forms import LoginForm

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Fazer Login', form=form)
