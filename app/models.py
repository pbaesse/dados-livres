#!/usr/bin/env python -*- coding: utf-8 -*-
from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db, login


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    about_me = db.Column(db.String(500))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    sources = db.relationship('Source', backref='author', lazy='dynamic')
    softwares = db.relationship('Software', backref='author', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.nickname)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def set_password(self, senha):
        self.password_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.password_hash, senha)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode( {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class Source(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    sphere = db.Column(db.String(200), index=True)
    city = db.Column(db.String(200), index=True)
    state = db.Column(db.String(200), index=True)
    country = db.Column(db.String(200), index=True)
    description = db.Column(db.String(800), index=True)
    officialLink = db.Column(db.String(300), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    tags = db.relationship('Tag', backref='source_tag', lazy='dynamic')
    categories = db.relationship('Category', backref='source_category', lazy='dynamic')
    comments = db.relationship('Comment', backref='source_comment', lazy='dynamic')
    reports = db.relationship('Report', backref='source_report', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '{}'.format(self.title)

    def as_dict(self):
        return {'title': self.title}


class Software(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    description = db.Column(db.String(800), index=True)
    officialLink = db.Column(db.String(300), index=True)
    license = db.Column(db.String(200), index=True)
    owner = db.Column(db.String(200), index=True)
    dateCreation = db.Column(db.String(200), index=True, default=datetime.utcnow)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    tags = db.relationship('Tag', backref='software_tag', lazy='dynamic')
    categories = db.relationship('Category', backref='software_category', lazy='dynamic')
    comments = db.relationship('Comment', backref='software_comment', lazy='dynamic')
    reports = db.relationship('Report', backref='software_report', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '{}'.format(self.title)

    def as_dict(self):
        return {'title': self.title}


class Tag(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '{}'.format(self.tag)


class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '{}'.format(self.category)


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), index=True)
    text = db.Column(db.String(600), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '{}'.format(self.username)


class Report(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    description = db.Column(db.String(500), index=True)
    type = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '{}'.format(self.name)
