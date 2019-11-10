from datetime import datetime
from time import time
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db, login

class tipoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<tipoUsuario {}>'.format(self.nome)
        
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), index=True, unique=True)
    email = db.Column(db.String(200), index=True, unique=True)
    password_hash = db.Column(db.String(150))
    about_me = db.Column(db.String(300))
    nickname = db.Column(db.String(150))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
 
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    sphere = db.Column(db.String(200), index=True)
    description = db.Column(db.String(800), index=True)
    officialLink = db.Column(db.String(250), index=True)
    datasetLink = db.Column(db.String(250), index=True)
    
    def __repr__(self):
        return '<Source {}>'.format(self.title)
        
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    palavraChave = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<Palavra Chave {}>'.format(self.palavraChave)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return '<ID {}>'.format(self.id)
                        
class softwareDados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(500), index=True)
    descricao = db.Column(db.String(500), index=True)
    dataCriacao = db.Column(db.String(200), index=True)
    dataLancamento = db.Column(db.String(200), index=True)
    linkDownload = db.Column(db.String(500), index=True)
    desenvolvimentoAtivo = db.Column(db.String(200), index=True)
    licenca = db.Column(db.String(200), index=True)
    proprietario = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<Titulo {}>'.format(self.titulo) 

class Favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gostei = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<Gostei {}>'.format(self.gostei)

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200), index=True)
    texto = db.Column(db.String(500), index=True)
    
    def __repr__(self):
        return '<Data {}>'.format(self.data)
        
class Denuncia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(500), index=True)
    tipo = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<Tipo {}>'.format(self.tipo)
