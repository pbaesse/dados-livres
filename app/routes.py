from flask_babel import _, get_locale
from app import app
  
@app.before_request
def before_request():
    g.locale = str(get_locale())

from flask_login import current_user, login_user, login_required
from app.models import User   
from app.forms import LoginForm
from flask import request
from werkzeug.urls import url_parse
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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '';
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title=_('Conecte-se'), form=form)
    
from flask_login import logout_user
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/')
@app.route('/index')
@login_required
def index():
    return "Hello, World!" #criar página principal

from flask import render_template, flash, redirect, url_for, request, g
