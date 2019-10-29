from app import app
from flask_babel import _, get_locale

@app.before_request
def before_request():
    # ...
    g.locale = str(get_locale())

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!" #criar página principal

from flask import render_template, flash, redirect, url_for, g
  
from app.forms import LoginForm
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(_('Login solicitado para o usuário {}, Lembre de mim={}').format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title=_('Fazer Login'), form=form)
