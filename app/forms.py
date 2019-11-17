from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from app.models import User
from flask_babel import _

class LoginForm(FlaskForm):
    username = StringField(_('Nome'), validators=[DataRequired()])
    password = PasswordField(_('Senha'), validators=[DataRequired()])
    remember_me = BooleanField(_('Lembre de mim'))
    submit = SubmitField(_('Entrar'))
    
class RegistrationForm(FlaskForm):
    username = StringField(_('Nome'), validators=[DataRequired()])
    email = StringField(_('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_('Senha'), validators=[DataRequired()])
    password2 = PasswordField(_(
        'Repita a senha'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_('Registrar'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Por favor, use um nome de usuário diferente.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Por favor, use um endereço de e-mail diferente.'))
            
class EditProfileForm(FlaskForm):
	username = StringField(_('Nome'), validators=[DataRequired()])
	nickname = StringField(_('Apelido'), validators=[DataRequired()])
	typeUser = StringField(_('Nome'), validators=[DataRequired()])
	about_me = TextAreaField(_('Sobre mim'), validators=[Length(min=0, max=200)])
	submit = SubmitField(_('Enviar'))
