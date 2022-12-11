"""Flask config."""
import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = URL.create(drivername="postgresql", username=os.environ.get("POSTGRES_USERNAME"), password=os.environ.get("POSTGRES_PASSWORD"), host=os.environ.get("POSTGRES_HOST"), port=os.environ.get("POSTGRES_PORT"), database=os.environ.get("POSTGRES_DATABASE"))

config = {
    "development": DevConfig,
    "testing": DevConfig,
    "production": ProdConfig,
    "default": DevConfig
}