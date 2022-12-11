from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

from config.config import config

APPLICATION_NAME = "pallid_elephant"

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(APPLICATION_NAME)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    return app


app = create_app(os.getenv("FLASK_CONFIG") or "default")


@app.route("/1/hello_world")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/1/gifts", methods=["POST"])
def create_gift():
    from models.gift import Gift

    gift = Gift(
        name=request.get_json()["name"], description=request.get_json()["description"]
    )
    app.db.session.add(gift)
    app.db.session.commit()

    return gift
