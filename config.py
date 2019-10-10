import os

class Config(object):
    SECRECT_KEY = os.environ.get('SECRET_KEY') or 'senha-secreta'
