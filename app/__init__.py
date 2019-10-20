from flask import Flask
app = Flask(__name__)

from config import Config
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from flask_migrate import Migrate
migrate = Migrate(app, db)

from flask_babel import Babel
babel = Babel(app)
from flask import request
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app import routes, models
