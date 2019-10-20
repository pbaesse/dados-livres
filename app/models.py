from app import db

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    senha = db.Column(db.String(128))
    
    def __repr__(self):
        return '<Login {}>'.format(self.nome)
