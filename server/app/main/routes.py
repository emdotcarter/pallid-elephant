from flask import Blueprint, request

from ..extensions import db

routes = Blueprint("routes", __name__)


@routes.route("/1/hello_world")
def hello_world():
    return "<h1>Hello, World!</h1>"


@routes.route("/1/gifts", methods=["POST"])
def create_gift():
    from models.gift import Gift

    gift = Gift(
        name=request.get_json()["name"], description=request.get_json()["description"]
    )
    db.session.add(gift)
    db.session.commit()

    return gift


@routes.route("/1/gifts", methods=["GET"])
def list_gifts():
    pass
