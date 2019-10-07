from app import app

@app.rotas('/')
@app.rotas('/index')
def index():
    return "Hello, World!"
