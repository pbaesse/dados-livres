#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import request
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SelectField, TextField, TextAreaField, \
    DateField, PasswordField, RadioField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, \
    Email, EqualTo, Regexp
from app.util.validators import Unique
from datetime import datetime
from flask_babel import _, lazy_gettext as _l
from app.models import User, Source, Software, Tag, Category, \
    Comment, Report


class EditProfileForm(FlaskForm):
    username = StringField(_l('Nome: *'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite um nome de usuário"})
    nickname = StringField(_l('Apelido: *'), validators=[DataRequired(),
        Length(max=10)], render_kw={"placeholder": "Digite seu apelido de usuário"})
    about_me = TextAreaField(_l('Sobre mim:'), validators=[Length(max=250)],
        render_kw={"rows": 6, "placeholder": "Digite uma breve descrição sobre você"})
    submit = SubmitField(_l('Salvar'))

    def __init__(self, original_nickname, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_nickname = original_nickname

    def validate_nickname(self, nickname):
        if nickname.data != self.original_nickname:
            user = User.query.filter_by(nickname=self.nickname.data).first()
            if user is not None:
                raise ValidationError(_('Esse apelido já está cadastrado. Escolha um apelido diferente'))


class EditPasswordForm(FlaskForm):
    senha = PasswordField(_l('Senha: *'), validators=[DataRequired(),
        Length(min=8)], render_kw={"placeholder": "Digite sua nova senha \
(mínimo 8 caracteres)"})
    password2 = PasswordField(_l('Repetir senha: *'), validators=[DataRequired(),
        EqualTo('senha'), Length(min=8)],
        render_kw={"placeholder": "Repita a senha anterior (mínimo 8 caracteres)"})
    submit = SubmitField(_('Salvar'))


class SourceForm(FlaskForm):
    title = StringField(_l('Título: *'), validators=[DataRequired(),
        Length(min=3), Unique(Source, Source.title,
        message='Já existe uma fonte registrada com esse título.')],
        render_kw={"placeholder": "Digite o título da Fonte de Dados Abertos"})
    keyword = StringField(_l('Palavras-Chaves: *'), id="tags", validators=[DataRequired()],
        render_kw={"placeholder": "Digite as palavras-chaves da fonte"})
    category = SelectField(_l('Categoria: *'), validators=[DataRequired()],
        choices=[('Corona Vírus','Corona Vírus'), ('Saúde', 'Saúde'),
        ('Educação', 'Educação'), ('Cinema', 'Cinema'), ('Música', 'Música'),
        ('Tecnologia', 'Tecnologia'), ('Ciência', 'Ciência'),
        ('Segurança Pública', 'Segurança Pública'), ('Meio Ambiente', 'Meio Ambiente'),
        ('Cultura', 'Cultura'), ('Países', 'Países'), ('IBGE', 'IBGE'),
        ('Gastos Públicos', 'Gastos Públicos'), ('Clima', 'Clima'), ('Lazer', 'Lazer')], default=1)
    officialLink = StringField(_l('Página Oficial: *'), validators=[DataRequired('URL verificada!'),
        Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
               'URL inválida. Use https:// no início da URL')],
               render_kw={"placeholder": "Digite a URL da fonte (https://www.exemplo.com/)"})
    sphere = SelectField(_l('Esfera: *'), id="esfera", choices=[
        ('Municipal', 'Municipal'), ('Estadual', 'Estadual'), ('Federal', 'Federal'),
        ('Internacional','Internacional')], validators=[DataRequired()])
    city = StringField(_l('Município:'), id="municipal",
        render_kw={"placeholder": "Digite o município da fonte de dados abertos"})
    state = StringField(_l('Estado:'), id="estadual",
        render_kw={"placeholder": "Digite o estato da fonte de dados abertos"})
    country = StringField(_l('País:'), id="internacional",
        render_kw={"placeholder": "Digite o país da fonte de dados abertos"})
    description = TextAreaField(_l('Descrição: *'), validators=[DataRequired(),
        Length(max=550)], render_kw={"rows": 6, "placeholder": "Digite uma breve descrição sobre a Fonte de Dados Abertos"})
    submit = SubmitField(_l('Registrar'))


class EditSourceForm(FlaskForm):
    title = StringField(_l('Título: *'), render_kw={"placeholder":
        "Digite o título da Fonte de Dados Abertos", "disabled": " "},
        description='Campo de editar título em implementação.')
    keyword = StringField(_l('Palavras-Chaves: *'), id="tags", validators=[DataRequired()],
        render_kw={"placeholder": "Digite as palavras-chaves da fonte"})
    category = SelectField(_l('Categoria: *'), validators=[DataRequired()],
        choices=[('Corona Vírus','Corona Vírus'), ('Saúde', 'Saúde'),
        ('Educação', 'Educação'), ('Cinema', 'Cinema'), ('Música', 'Música'),
        ('Tecnologia', 'Tecnologia'), ('Ciência', 'Ciência'),
        ('Segurança Pública', 'Segurança Pública'), ('Meio Ambiente', 'Meio Ambiente'),
        ('Cultura', 'Cultura'), ('Países', 'Países'), ('IBGE', 'IBGE'),
        ('Gastos Públicos', 'Gastos Públicos'), ('Clima', 'Clima'), ('Lazer', 'Lazer')], default=1)
    officialLink = StringField(_l('Página Oficial: *'), validators=[DataRequired('URL verificada!'),
        Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
               'URL inválida. Use https:// no início da URL')],
               render_kw={"placeholder": "Digite a URL da fonte (https://www.exemplo.com/)"})
    sphere = SelectField(_l('Esfera: *'), id="esfera", choices=[
        ('Municipal', 'Municipal'), ('Estadual', 'Estadual'), ('Federal', 'Federal'),
        ('Internacional','Internacional')], validators=[DataRequired()])
    city = StringField(_l('Município:'), id="municipal",
        render_kw={"placeholder": "Digite o município da fonte de dados abertos"})
    state = StringField(_l('Estado:'), id="estadual",
        render_kw={"placeholder": "Digite o estato da fonte de dados abertos"})
    country = StringField(_l('País:'), id="internacional",
        render_kw={"placeholder": "Digite o país da fonte de dados abertos"})
    description = TextAreaField(_l('Descrição: *'), validators=[DataRequired(),
        Length(max=550)], render_kw={"rows": 6, "placeholder": "Digite uma breve descrição sobre a Fonte de Dados Abertos"})
    submit = SubmitField(_l('Registrar'))


class SoftwareForm(FlaskForm):
    title = StringField(_l('Título: *'), validators=[DataRequired(),
        Length(min=3), Unique(Software, Software.title,
        message='Já existe uma aplicação registrada com esse título.')],
        render_kw={"placeholder": "Digite o título da Aplicação"})
    keyword = StringField(_l('Palavras-Chaves: *'), id="tags", validators=[DataRequired()],
        render_kw={"placeholder": "Digite as palavras-chaves da Aplicação"})
    category = SelectField(_l('Categoria: *'), validators=[DataRequired()],
        choices=[('Corona Vírus','Corona Vírus'), ('Saúde', 'Saúde'),
        ('Educação', 'Educação'), ('Cinema', 'Cinema'), ('Música', 'Música'),
        ('Tecnologia', 'Tecnologia'), ('Ciência', 'Ciência'), ('IBGE', 'IBGE'),
        ('Segurança Pública', 'Segurança Pública'), ('Países', 'Países'),
        ('Meio Ambiente', 'Meio Ambiente'), ('Cultura', 'Cultura'),
        ('Gastos Públicos', 'Gastos Públicos'), ('Clima', 'Clima'), ('Lazer', 'Lazer')], default=1)
    officialLink = StringField(_l('Página Oficial: *'),
        validators=[DataRequired('URL verificada!'),
        Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
               'URL inválida. Use https:// no início da URL')],
        render_kw={"placeholder": "Digite a URL da aplicação (https://www.exemplo.com/)"})
    owner = StringField(_l('Desenvolvedor: *'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite qual a pessoa desenvolvedora/empresa da aplicação"})
    dateCreation = StringField(_l('Data de Criação:'),
        render_kw={"placeholder": "Digite a data de criação (formato: 12/02/2020)"})
    license = SelectField(_l('Licença: *'), validators=[DataRequired()],
        choices=[('Apache License 2.0', 'Apache License 2.0'),
        ('GNU General Public License v3.0','GNU General Public License v3.0'),
        ('MIT License','MIT License'), ('BSD 2-Clause "Simplified" License','BSD 2-Clause "Simplified" License'),
        ('BSD 3-Clause "New" or "Revised" License','BSD 3-Clause "New" or "Revised" License'),
        ('Boost Software License 1.0','Boost Software License 1.0'),
        ('Creative Commons Zero v1.0 Universal','Creative Commons Zero v1.0 Universal'),
        ('Eclipse Public License 2.0','Eclipse Public License 2.0'),
        ('GNU Alffero General Public License v3.0','GNU Alffero General Public License v3.0'),
        ('GNU General Public License v2.0','GNU General Public License v2.0'),
        ('GNU Lesser General Public License v2.1','GNU Lesser General Public License v2.1'),
        ('Mozilla Public License 2.0','Mozilla Public License 2.0')], default=1)
    description = TextAreaField(_l('Descrição: *'), validators=[DataRequired(),
        Length(max=550)], render_kw={"rows": 6, "placeholder": "Digite uma breve descrição sobre a Aplicação"})
    submit = SubmitField(_l('Registrar'))


class EditSoftwareForm(FlaskForm):
    title = StringField(_l('Título: *'), render_kw={"placeholder":
        "Digite o título da Aplicação", "disabled": " "},
        description='Campo de editar título em implementação.')
    keyword = StringField(_l('Palavras-Chaves: *'), id="tags", validators=[DataRequired()],
        render_kw={"placeholder": "Digite as palavras-chaves da Aplicação"})
    category = SelectField(_l('Categoria: *'), validators=[DataRequired()],
        choices=[('Corona Vírus','Corona Vírus'), ('Saúde', 'Saúde'),
        ('Educação', 'Educação'), ('Cinema', 'Cinema'), ('Música', 'Música'),
        ('Tecnologia', 'Tecnologia'), ('Ciência', 'Ciência'), ('IBGE', 'IBGE'),
        ('Segurança Pública', 'Segurança Pública'), ('Países', 'Países'),
        ('Meio Ambiente', 'Meio Ambiente'), ('Cultura', 'Cultura'),
        ('Gastos Públicos', 'Gastos Públicos'), ('Clima', 'Clima'), ('Lazer', 'Lazer')], default=1)
    officialLink = StringField(_l('Página Oficial: *'),
        validators=[DataRequired('URL verificada!'),
        Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
               'URL inválida. Use https:// no início da URL')],
        render_kw={"placeholder": "Digite a URL da aplicação (https://www.exemplo.com/)"})
    owner = StringField(_l('Desenvolvedor: *'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite qual a pessoa desenvolvedora/empresa da aplicação"})
    dateCreation = StringField(_l('Data de Criação:'),
        render_kw={"placeholder": "Digite a data de criação (formato: 12/02/2020)"})
    license = SelectField(_l('Licença: *'), validators=[DataRequired()],
        choices=[('Apache License 2.0', 'Apache License 2.0'),
        ('GNU General Public License v3.0','GNU General Public License v3.0'),
        ('MIT License','MIT License'), ('BSD 2-Clause "Simplified" License','BSD 2-Clause "Simplified" License'),
        ('BSD 3-Clause "New" or "Revised" License','BSD 3-Clause "New" or "Revised" License'),
        ('Boost Software License 1.0','Boost Software License 1.0'),
        ('Creative Commons Zero v1.0 Universal','Creative Commons Zero v1.0 Universal'),
        ('Eclipse Public License 2.0','Eclipse Public License 2.0'),
        ('GNU Alffero General Public License v3.0','GNU Alffero General Public License v3.0'),
        ('GNU General Public License v2.0','GNU General Public License v2.0'),
        ('GNU Lesser General Public License v2.1','GNU Lesser General Public License v2.1'),
        ('Mozilla Public License 2.0','Mozilla Public License 2.0')], default=1)
    description = TextAreaField(_l('Descrição: *'), validators=[DataRequired(),
        Length(max=550)], render_kw={"rows": 6, "placeholder": "Digite uma breve descrição sobre a Aplicação"})
    submit = SubmitField(_l('Registrar'))


class SimilarForm(FlaskForm):
    name = StringField(_l('Título: *'), id='autocomplete', validators=[DataRequired(),
        Length(min=0, max=100)], render_kw={"placeholder": "Digite o nome de um título registrado em Dados Livres"})
    submit = SubmitField(_l('Registrar'))


class CommentForm(FlaskForm):
    username = StringField(_l('Nome: *'), validators=[DataRequired()])
    text = TextAreaField(_l('Comentário: *'), validators=[DataRequired()])
    submit = SubmitField(_l('Enviar'))


class ReportForm(FlaskForm):
    name = StringField(_l('Nome: *'), validators=[DataRequired()])
    description = TextAreaField(_l('Descrição: *'), validators=[DataRequired(),
        Length(min=0, max=150)])
    type = StringField(_l('Tipo: *'), validators=[DataRequired()])
    submit = SubmitField(_l('Enviar'))


class ContactForm(FlaskForm):
    username = StringField(_l('Nome: *'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite seu nome"})
    email = StringField(_l('E-mail: *'), validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Digite seu e-mail"})
    subject = StringField(_l('Assunto: *'), validators=[DataRequired()],
        render_kw={"placeholder": "Digite o assunto do e-mail"})
    message = TextAreaField(_l('Mensagem: *'), validators=[DataRequired(),
        Length(min=4, max=500)], render_kw={"rows": 6, "placeholder": "Digite a mensagem do e-mail"})
    submit = SubmitField(_l('Enviar'))
