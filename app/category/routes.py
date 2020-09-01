#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, g
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import db
from app.category import bp
from app.models import Source, Software, Tag, Category

import unicodedata
def remove_accents(category):
    try:
        category = unicode(category, 'utf-8')
    except NameError: # unicode is a default on python 3
        pass
    category = unicodedata.normalize('NFD', category)\
        .encode('ascii', 'ignore')\
        .decode("utf-8")
    return str(category.replace(" ", ""))

@bp.route('/Covid19_Source', methods=['GET', 'POST'])
def Covid19_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Corona Vírus',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Covid19_Source.html', title=(_('Corona Vírus')),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Covid19_Software', methods=['GET', 'POST'])
def Covid19_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Corona Vírus',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Covid19_Software.html', title=(_('Corona Vírus')),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Health_Source', methods=['GET', 'POST'])
def Health_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Saúde',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Health_Source.html', title=_('Saúde'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Health_Software', methods=['GET', 'POST'])
def Health_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Saúde',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Health_Software.html', title=_('Saúde'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Education_Source', methods=['GET', 'POST'])
def Education_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Educação',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Education_Source.html', title=_('Educação'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Education_Software', methods=['GET', 'POST'])
def Education_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Educação',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Education_Software.html', title=_('Educação'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/MovieTheater_Source', methods=['GET', 'POST'])
def MovieTheater_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Cinema',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/MovieTheater_Source.html', title=_('Cinema'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/MovieTheater_Software', methods=['GET', 'POST'])
def MovieTheater_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Cinema',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/MovieTheater_Software.html', title=_('Cinema'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Music_Source', methods=['GET', 'POST'])
def Music_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Música',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Music_Source.html', title=_('Música'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Music_Software', methods=['GET', 'POST'])
def Music_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Música',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Music_Software.html', title=_('Música'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Technology_Source', methods=['GET', 'POST'])
def Technology_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Tecnologia',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Technology_Source.html', title=_('Tecnologia'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Technology_Software', methods=['GET', 'POST'])
def Technology_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Tecnologia',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Technology_Software.html', title=_('Tecnologia'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Science_Source', methods=['GET', 'POST'])
def Science_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Ciência',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Science_Source.html', title=_('Ciência'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Science_Software', methods=['GET', 'POST'])
def Science_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Ciência',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Science_Software.html', title=_('Ciência'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/PublicSecurity_Source', methods=['GET', 'POST'])
def PublicSecurity_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Segurança Pública',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/PublicSecurity_Source.html',
        title=_('Segurança Pública'), sources=sources)

@bp.route('/PublicSecurity_Software', methods=['GET', 'POST'])
def PublicSecurity_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Segurança Pública',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/PublicSecurity_Software.html',
        title=_('Segurança Pública'), softwares=softwares)

@bp.route('/Environment_Source', methods=['GET', 'POST'])
def Environment_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Meio Ambiente',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Environment_Source.html',
        title=_('Meio Ambiente'), sources=sources, remove_accents=remove_accents)

@bp.route('/Environment_Software', methods=['GET', 'POST'])
def Environment_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Meio Ambiente',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Environment_Software.html',
        title=_('Meio Ambiente'), softwares=softwares,
        remove_accents=remove_accents)

@bp.route('/Culture_Source', methods=['GET', 'POST'])
def Culture_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Cultura',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Culture_Source.html', title=_('Cultura'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Culture_Software', methods=['GET', 'POST'])
def Culture_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Cultura',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Culture_Software.html', title=_('Cultura'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Countries_Source', methods=['GET', 'POST'])
def Countries_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Países',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Countries_Source.html', title=_('Países'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Countries_Software', methods=['GET', 'POST'])
def Countries_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Países',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Countries_Software.html', title=_('Países'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/IBGE_Source', methods=['GET', 'POST'])
def IBGE_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='IBGE',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/IBGE_Source.html', title=_('IBGE'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/IBGE_Software', methods=['GET', 'POST'])
def IBGE_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='IBGE',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/IBGE_Software.html', title=_('IBGE'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/PublicSpending_Source', methods=['GET', 'POST'])
def PublicSpending_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Gastos Públicos',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/PublicSpending_Source.html', title=_('Gastos Públicos'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/PublicSpending_Software', methods=['GET', 'POST'])
def PublicSpending_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Gastos Públicos',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/PublicSpending_Software.html', title=_('Gastos Públicos'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Climate_Source', methods=['GET', 'POST'])
def Climate_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Clima',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Climate_Source.html', title=_('Clima'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Climate_Software', methods=['GET', 'POST'])
def Climate_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Clima',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Climate_Software.html', title=_('Clima'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Recreation_Source', methods=['GET', 'POST'])
def Recreation_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Lazer',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Recreation_Source.html', title=_('Lazer'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Recreation_Software', methods=['GET', 'POST'])
def Recreation_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Lazer',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Recreation_Software.html', title=_('Lazer'),
        softwares=softwares, remove_accents=remove_accents)
