from flask import render_template, current_app
from flask_babel import _
from app.email import send_email

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(_('[Dados Livres] Renomeie sua senha'),
                sender=current_app.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt',
                                        user=user, token=token),
                html_body=render_template('email/reset_password.html',
                                        user=user, token=token))

def send_register_confirm_email(user):
    token = user.get_confirm_register_token()
    send_email(_('[Dados Livres] Conclua sua inscrição'),
                sender=current_app.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/confirm_email.txt',
                                        user=user, token=token),
                html_body=render_template('email/confirm_email.html',
                                        user=user, token=token))
