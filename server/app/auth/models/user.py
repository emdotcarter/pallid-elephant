import sqlalchemy
from flask_login import UserMixin

from server.app.extensions import db, login_manager


class User(db.Model, UserMixin):
    email_address = sqlalchemy.Column(
        sqlalchemy.Text,
        nullable=False,
        index=True,
        unique=True,
    )
    password = sqlalchemy.Column(
        sqlalchemy.Text,
        nullable=False,
    )


@login_manager.user_loader
def user_loader(email_address):
    return db.session.query(User).filter_by(email_address=email_address).one_or_none()


@login_manager.request_loader
def request_loader(request):
    email_address = request.form.get("email_address")
    return db.session.query(User).filter_by(email_address=email_address).one_or_none()
