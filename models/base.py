import datetime
from app import db
from sqlalchemy.orm import declarative_base, declared_attr


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime(timezone=True), default=lambda: datetime.now(datetime.timezone.utc)
    )
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)


Base = declarative_base(cls=Base)
