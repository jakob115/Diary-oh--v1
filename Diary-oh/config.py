from os import environ, path

BASE_DIR = path.abspath(path.dirname(__file__))

# General Flask configuration
SECRET_KEY = environ.get('SECRET_KEY') or 'long and hard to guess string'
FLASK_APP = 'app.py'  # Webapp filename
FLASK_DEBUG = 1

# Database configuration
SQLITE_DB = 'sqlite:///' + path.join(BASE_DIR, 'diary.sqlite')  # Database filename
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or SQLITE_DB
SQLALCHEMY_TRACK_MODIFICATIONS = False
