#!/usr/bin/env python# -*- coding: utf-8 -*-
import sys
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app, Response
import json
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.main.form import EditProfileForm, EditPasswordForm, \
    SourceForm, EditSourceForm, SoftwareForm, EditSoftwareForm, \
    CommentForm, ReportForm, ContactForm
from app.models import User, Source, Software, Tag, Category, \
    Comment, Report
from flask_mail import Message
from app import mail
from app.main import bp

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())

@bp.route('/_title', methods=['GET'])
def title():
    source_title = Source.query.all()
    software_title = Software.query.all()
    sources = [r.as_dict() for r in source_title]
    softwares = [r.as_dict() for r in software_title]
    return jsonify(sources + softwares)

@bp.route('/_tag', methods=['GET'])
def tag():
    keyword = Tag.query.all()
    tags = [r.as_dict() for r in keyword]
    return jsonify(tags)

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    sources = db.session.query(Source.title, Source.sphere,
        Category.category, Tag.keyword).filter(
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).paginate(page=page, per_page=1)
    softwares = db.session.query(Software.title, Software.owner,
        Software.license, Category.category, Tag.keyword).filter(
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).paginate(page=page, per_page=1)
    return render_template('index.html', title=(_('Página Inicial')),
        sources=sources.items, softwares=softwares.items)

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/source', methods=['GET', 'POST'])
def source():
    return render_template('source.html', title=(_('Fontes')))

@bp.route('/software', methods=['GET', 'POST'])
def software():
    return render_template('software.html', title=(_('Aplicações')))

@bp.route('/register_source', methods=['GET', 'POST'])
@login_required
def register_source():
    form = SourceForm()
    if form.validate_on_submit():
        source = Source(title=form.title.data, city=form.city.data,
        state=form.state.data, country=form.country.data,
        description=form.description.data, sphere=form.sphere.data,
        officialLink=form.officialLink.data, author=current_user)
        db.session.add(source)
        db.session.flush()
        category = Category(category=form.category.data, source_id=source.id)
        db.session.add(category)
        db.session.flush()
        tag = Tag(keyword=form.keyword.data)
        db.session.add(tag)
        db.session.flush()
        source.tags.append(tag)
        db.session.commit()
        flash(_('A fonte "%s" foi registrada com sucesso.' % source.title))
    return render_template('register_source.html',
        title=(_('Cadastrar Fonte')), form=form)

@bp.route('/source_profile/<title>', methods=['GET', 'POST'])
def source_profile(title):
    source = Source.query.filter_by(title=title).first_or_404()
    return render_template('source_profile.html',
        title=(_('Perfil da Fonte')), source=source)

@bp.route('/edit_source/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_source(id):
    source = Source.query.get_or_404(id)
    tag = Tag.query.filter(Source.tags, Source.id == id).first_or_404()
    category = Category.query.filter(
        Category.source_id == Source.id, Source.id == id).first_or_404()
    form = EditSourceForm()
    if form.validate_on_submit():
        #source.title = form.title.data
        tag.keyword = form.keyword.data
        category.category = form.category.data
        source.officialLink = form.officialLink.data
        source.sphere = form.sphere.data
        source.city = form.city.data
        source.state = form.state.data
        source.country = form.country.data
        source.description = form.description.data
        db.session.add(source)
        db.session.flush()
        db.session.add(tag)
        db.session.flush()
        db.session.add(category)
        db.session.flush()
        db.session.commit()
        flash(_('A fonte "%s" foi editada com sucesso.' % source.title))
    form.title.data = source.title
    form.keyword.data = tag.keyword
    form.category.data = category.category
    form.officialLink.data = source.officialLink
    form.sphere.data = source.sphere
    form.city.data = source.city
    form.state.data = source.state
    form.country.data = source.country
    form.description.data = source.description
    return render_template('edit_source.html', title=(_('Editar Fonte')),
            form=form, source=source, tag=tag, category=category)

@bp.route("/deletar_source/<int:id>")
@login_required
def deletar_source(id):
    source = Source.query.filter_by(id=id).first()
    category = Category.query.filter(
        Category.source_id == Source.id, Source.id == id).first_or_404()
    db.session.delete(source)
    db.session.flush()
    db.session.delete(category)
    db.session.flush()
    db.session.commit()
    flash(_('A fonte "%s" foi apagada com sucesso.' % source.title))
    return redirect(url_for("main.index"))

@bp.route('/register_software', methods=['GET', 'POST'])
@login_required
def register_software():
    form = SoftwareForm()
    if form.validate_on_submit():
        software = Software(title=form.title.data,
        description=form.description.data, officialLink=form.officialLink.data,
        license=form.license.data, owner=form.owner.data,
        dateCreation=form.dateCreation.data, author=current_user)
        db.session.add(software)
        db.session.flush()
        category = Category(category=form.category.data, software_id=software.id)
        db.session.add(category)
        db.session.flush()
        tag = Tag(keyword=form.keyword.data)
        db.session.add(tag)
        db.session.flush()
        software.tags.append(tag)
        db.session.commit()
        flash('A aplicação "%s" foi registrada com sucesso.' % software.title)
    return render_template('register_software.html',
        title=(_('Cadastrar Aplicação')), form=form)

@bp.route('/software_profile/<title>', methods=['GET', 'POST'])
def software_profile(title):
    software = Software.query.filter_by(title=title).first_or_404()
    return render_template('software_profile.html',
        title=(_('Perfil da Aplicação')), software=software)

@bp.route('/edit_software/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_software(id):
    software = Software.query.get_or_404(id)
    tag = Tag.query.filter(Software.tags, Software.id == id).first_or_404()
    category = Category.query.filter(
        Category.software_id == Software.id, Software.id == id).first_or_404()
    form = EditSoftwareForm()
    if form.validate_on_submit():
        #software.title = form.title.data
        tag.keyword = form.keyword.data
        category.category = form.category.data
        software.officialLink = form.officialLink.data
        software.owner = form.owner.data
        software.dateCreation = form.dateCreation.data
        software.license = form.license.data
        software.description = form.description.data
        db.session.add(software)
        db.session.flush()
        db.session.add(tag)
        db.session.flush()
        db.session.add(category)
        db.session.flush()
        db.session.commit()
        flash(_('A aplicação "%s" foi editada com sucesso.' % software.title))
    form.title.data = software.title
    form.keyword.data = tag.keyword
    form.category.data = category.category
    form.officialLink.data = software.officialLink
    form.owner.data = software.owner
    form.dateCreation.data = software.dateCreation
    form.license.data = software.license
    form.description.data = software.description
    return render_template('edit_software.html', title=(_('Editar Aplicação')),
        form=form, software=software, tag=tag, category=category)

@bp.route("/deletar_software/<int:id>")
@login_required
def deletar_software(id):
    software = Software.query.filter_by(id=id).first()
    category = Category.query.filter(
        Category.software_id == Software.id, Software.id == id).first_or_404()
    db.session.delete(software)
    db.session.flush()
    db.session.delete(category)
    db.session.flush()
    db.session.commit()
    flash(_('A aplicação "%s" foi apagada com sucesso.' % software.title))
    return redirect(url_for("main.index"))

@bp.route('/user/<nickname>', methods=['GET', 'POST'])
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first_or_404()
    sources = db.session.query(Source.title, Source.sphere,
        Category.category, Tag.keyword).filter(
        Category.source_id == Source.id, Source.tags,
        Source.user_id == user.id).order_by(Source.timestamp.desc()).all()
    softwares = db.session.query(Software.title, Software.owner,
        Software.license, Category.category, Tag.keyword).filter(
        Category.software_id == Software.id, Software.tags,
        Software.user_id == user.id).order_by(Software.timestamp.desc()).all()
    return render_template('user.html', title=(_('Perfil do Usuário')),
        user=user, sources=sources, softwares=softwares)

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.nickname)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.nickname = form.nickname.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Suas alterações foram salvas'))
        return redirect(url_for('main.user', nickname=current_user.nickname))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.nickname.data = current_user.nickname
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=(_('Editar Perfil')),
                           form=form)

@bp.route('/deletar_user/<int:id>')
@login_required
def deletar_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    flash(_('O usuário "%s" foi excluído.' % user.username))
    return redirect(url_for("main.index"))

@bp.route('/edit_password', methods=["GET", "POST"])
@login_required
def edit_password():
    form = EditPasswordForm(current_user.username)
    if form.validate_on_submit():
        current_user.password_hash = form.senha
        db.session.commit()
        flash(_('Sua nova senha foi salva'))
        return redirect(url_for('main.user', username=current_user.username))
    elif request.method == 'GET':
        form.senha = current_user.password_hash
    return render_template('edit_password.html', title=(_('Editar Senha')), form=form)

@bp.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html', title=(_('Sobre')))

@bp.route('/how_to_contribute', methods=['GET', 'POST'])
def how_to_contribute():
    return render_template('how_to_contribute.html', title=(_('Como contribuir')))

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    while current_user.is_authenticated:
        if form.validate_on_submit():
            current_user.username = form.username.data
        elif request.method == 'GET':
            form.username.data = current_user.username
        if request.method == 'POST':
            msg = Message(form.username.data, sender='dadoslivres.testes@gmail.com',
            recipients=['m.carolina.soares1@gmail.com'])
            msg.body = """
            Enviado por: %s
            E-mail: %s
            Assunto: %s
            Mensagem: %s""" % (form.username.data, form.email.data, form.subject.data, form.message.data)
            mail.send(msg)
            flash(_('Seu e-mail foi enviado, agradecemos pelo contato'))
            return render_template('contact.html', title=(_('Contato')), form=form)
        elif request.method == 'GET':
            return render_template('contact.html', title=(_('Contato')), form=form)

    if request.method == 'POST':
        msg = Message(form.username.data, sender='dadoslivres.testes@gmail.com',
        recipients=['m.carolina.soares1@gmail.com'])
        msg.body = """
        Enviado por: %s
        E-mail: %s
        Assunto: %s
        Mensagem: %s""" % (form.username.data, form.email.data, form.subject.data, form.message.data)
        mail.send(msg)
        flash(_('Seu e-mail foi enviado, agradecemos pelo contato'))
        return render_template('contact.html', title=(_('Contato')), form=form)
    elif request.method == 'GET':
        return render_template('contact.html', title=(_('Contato')), form=form)
