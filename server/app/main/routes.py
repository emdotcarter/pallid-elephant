import flask_login
from flask import Blueprint, make_response, request

from server.app.extensions import db

from .models import Gift

routes = Blueprint("routes", __name__)


@routes.route("/1/gifts", methods=["POST"])
def create_gift():
    gift = Gift(
        name=request.get_json()["name"], description=request.get_json()["description"]
    )
    db.session.add(gift)
    db.session.commit()

    return make_response(gift.serialize())


@routes.route("/1/gifts", methods=["GET"])
@flask_login.login_required
def list_gifts():
    return make_response([g.serialize() for g in db.session.query(Gift).all()])
