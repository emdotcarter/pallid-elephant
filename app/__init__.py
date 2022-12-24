import os

from dotenv import load_dotenv
from flask import Flask

from app.extensions import db, migrate
from app.main.routes import routes
from config.config import config

APPLICATION_NAME = "pallid_elephant"

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "..", ".env"))


def create_app(config_name):
    local_app = Flask(APPLICATION_NAME)
    local_app.config.from_object(config[config_name])

    db.init_app(local_app)
    migrate.init_app(local_app, db)

    local_app.register_blueprint(routes)

    return local_app


app = create_app(os.getenv("FLASK_CONFIG") or "default")
