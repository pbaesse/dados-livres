from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from flask_babel import _, lazy_gettext as _l

class LoginForm(FlaskForm):
    username = StringField(_l('Nome'), validators=[DataRequired()])
    password = PasswordField(_l('Senha'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Lembre de mim'))
    submit = SubmitField(_l('Entrar'))
