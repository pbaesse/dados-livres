from app import app
from flask_babel import _, get_locale

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!" #criar página principal

from flask import render_template, flash, redirect, url_for, request, g
  
@app.before_request
def before_request():
    g.locale = str(get_locale())

from flask_login import current_user, login_user
from app.models import User   
from app.forms import LoginForm
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
    	return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_('Nome de usuário ou senha inválidos'))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title=_('Conecte-se'), form=form)
    
from flask_login import logout_user
def logout():
    logout_user()
    return redirect(url_for('index'))
