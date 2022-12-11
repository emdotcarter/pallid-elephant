from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

from config.config import config
from app.main.routes import routes
from app.extensions import db

APPLICATION_NAME = "pallid_elephant"

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "..", ".env"))


def create_app(config_name):
    app = Flask(APPLICATION_NAME)
    app.config.from_object(config[config_name])

    db.init_app(app)

    app.register_blueprint(routes)

    return app


app = create_app(os.getenv("FLASK_CONFIG") or "default")
