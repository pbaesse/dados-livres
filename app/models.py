from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    senha = db.Column(db.String(128))
    apelido = db.Column(db.String(40), index=True)
    descricao = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<Usuario {}>'.format(self.nome)

class tipoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70), index=True)
    
    def __repr__(self):
        return '<tipoUsuario {}>'.format(self.nome)  
        
class Denuncia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), index=True)
    tipo = db.Column(db.String(70), index=True)
    
    def __repr__(self):
        return '<Tipo {}>'.format(self.tipo)

class fonteDados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70), index=True)
    esfera = db.Column(db.String(110), index=True)
    descricao = db.Column(db.String(200), index=True)
    linkOficial = db.Column(db.String(200), index=True)
    linkDataset = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<Titulo {}>'.format(self.titulo)
        
class softwareDados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70), index=True)
    descricao = db.Column(db.String(200), index=True)
    dataCriacao = db.Column(db.String(10), index=True)
    dataLancamento = db.Column(db.String(10), index=True)
    linkDownload = db.Column(db.String(200), index=True)
    desenvolvimentoAtivo = db.Column(db.String(200), index=True)
    licenca = db.Column(db.String(10), index=True)
    proprietario = db.Column(db.String(10), index=True)
    
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
    texto = db.Column(db.String(70), index=True)
    
    def __repr__(self):
        return '<Data {}>'.format(self.data)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    palavraChave = db.Column(db.String(200), index=True)
    
    def __repr__(self):
        return '<Palavra Chave {}>'.format(self.palavraChave)
