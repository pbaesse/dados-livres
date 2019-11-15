from app import app, db, cli
from app.models import User, Source, Software

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Source': Source, 'Software': Software}
