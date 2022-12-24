from datetime import datetime

import sqlalchemy
from flask_sqlalchemy.model import Model


class Base(Model):
    __abstract__ = True

    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True)
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, nullable=False, default=datetime.now()
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime, nullable=False, onupdate=datetime.now()
    )
