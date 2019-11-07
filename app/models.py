from datetime import datetime
from time import time
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), index=True, unique=True)
    email = db.Column(db.String(200), index=True, unique=True)
    password_hash = db.Column(db.String(150))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
class tipoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<tipoUsuario {}>'.format(self.nome)  

class fonteDados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(500), index=True)
    esfera = db.Column(db.String(150), index=True)
    descricao = db.Column(db.String(500), index=True)
    linkOficial = db.Column(db.String(500), index=True)
    linkDataset = db.Column(db.String(500), index=True)
    
    def __repr__(self):
        return '<Titulo {}>'.format(self.titulo)
        
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
