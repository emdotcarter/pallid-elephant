from app.extensions import db

from .base import Base


class Gift(Base):
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
        }
