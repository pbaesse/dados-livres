#!/usr/bin/env python -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import logout_user, current_user, login_user, login_required
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, \
    ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
from app.auth.email import send_password_reset_email, send_register_confirm_email

@bp.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.senha.data):
			flash(_('E-mail ou senha inválido'))
			return redirect(url_for('auth.login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('main.index')
		return redirect(next_page)
	return render_template('auth/login.html', title=(_('Entrar')), form=form)

@bp.route('/register_request', methods=['GET', 'POST'])
def register_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
            nickname=form.nickname.data, confirmed=False)
        user.set_password(form.senha.data)
        db.session.add(user)
        db.session.commit()
        if user:
            send_register_confirm_email(user)
        flash(_('Verifique sua caixa de e-mail para concluir a sua inscrição.'))
        return redirect(url_for('auth.login'))
    return render_template('auth/register_request.html', title=(_('Inscreva-se')), form=form)

@bp.route('/register_confirm/<token>', methods=['GET', 'POST'])
def register_confirm(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    try:
        email = User.verify_confirm_register_token(token)
        if not email:
            return redirect(url_for('main.index'))
    except:
        flash(_('O link de confirmação é inválido ou expirou'))
    user = db.session.query(User).filter(User.id).first_or_404()
    if user.confirmed:
        flash(_('Conta já confirmada. Por favor entre.'))
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash(_('Parabéns, sua inscrição foi confirmada com sucesso.'))
    return redirect(url_for('auth.login'))

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(_('Por favor, verifique seu e-mail para concluir a sua renomeação de senha'))
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html',
                           title=(_('Renomear Senha')), form=form)

@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.senha.data)
        db.session.commit()
        flash(_('Sua senha foi alterada'))
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', title=(_('Renomear Senha')), form=form)
