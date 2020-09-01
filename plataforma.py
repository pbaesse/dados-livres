from app import create_app, db, cli
from app.models import User, Source, Software, Tag, Category, Comment, Report

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Source': Source, 'Software': Software,
        'Tag': Tag, 'Category': Category, 'Comment': Comment,
        'Report': Report}
