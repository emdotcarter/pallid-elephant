import os

from dotenv import load_dotenv

from .main.models import *

APPLICATION_NAME = "pallid_elephant"

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "..", ".env"))


def create_app(config_name):
    from flask import Flask

    from server.config.config import config

    from .auth.routes import routes as auth_routes
    from .extensions import db, login_manager, migrate
    from .main.routes import routes as main_routes

    local_app = Flask(APPLICATION_NAME)
    local_app.config.from_object(config[config_name])

    db.init_app(local_app)
    login_manager.init_app(local_app)

    local_app.register_blueprint(auth_routes)
    local_app.register_blueprint(main_routes)

    migrate.init_app(local_app, db)

    return local_app


app = create_app(os.getenv("FLASK_CONFIG") or "default")
