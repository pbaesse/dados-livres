from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), index=True, unique=True)
    email = db.Column(db.String(200), index=True, unique=True)
    senha = db.Column(db.String(200))
    apelido = db.Column(db.String(150), index=True)
    descricao = db.Column(db.String(500), index=True)
    
    def __repr__(self):
        return '<Usuario {}>'.format(self.nome)

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
