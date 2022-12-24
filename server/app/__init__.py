import os

from dotenv import load_dotenv

from .main.models import *

APPLICATION_NAME = "pallid_elephant"

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "..", ".env"))


def create_app(config_name):
    from flask import Flask
    local_app = Flask(APPLICATION_NAME)

    from server.config.config import config
    local_app.config.from_object(config[config_name])

    from .extensions import db
    db.init_app(local_app)

    from .extensions import migrate
    migrate.init_app(local_app, db)

    from .main.routes import routes
    local_app.register_blueprint(routes)

    return local_app


app = create_app(os.getenv("FLASK_CONFIG") or "default")
