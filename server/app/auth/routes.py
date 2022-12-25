import flask_login
from flask import Blueprint, abort, make_response, redirect, request, url_for

from server.app.extensions import db

from .models.user import User

routes = Blueprint("auth", __name__, url_prefix="/1/auth")


@routes.route("/login", methods=["GET"])
def get_login_page():
    return make_response(
        """
            <form action='login' method='POST'>
                <input type='email' name='email_address' id='email_address' placeholder='email_address'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
            </form>
            """
    )


@routes.route("/login", methods=["POST"])
def do_login():
    email_address = request.form["email_address"]
    user = db.session.query(User).filter_by(email_address=email_address).one_or_none()

    if user:
        flask_login.login_user(user)
        return redirect(url_for("routes.list_gifts"))

    abort(401)
