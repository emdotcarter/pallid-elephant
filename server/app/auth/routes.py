import flask_login
from flask import Blueprint, abort, redirect, render_template, request, url_for

from server.app.extensions import db, login_manager

from .models.user import User

routes = Blueprint(
    "auth", __name__, url_prefix="/1/auth", template_folder="./templates"
)


@routes.route("/login", methods=["GET"])
def get_login_page():
    return render_template("login.html")


@routes.route("/login", methods=["POST"])
def do_login():
    email_address = request.form["email_address"]
    password = request.form["password"]
    user = (
        db.session.query(User)
        .filter_by(email_address=email_address, password=password)
        .one_or_none()
    )

    if user:
        flask_login.login_user(user)
        return redirect(url_for("routes.list_gifts"))

    abort(401)


@routes.route("/logout", methods=["GET", "POST"])
def logout():
    flask_login.logout_user()
    return redirect(url_for("auth.get_login_page"))


@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for("auth.get_login_page"))
