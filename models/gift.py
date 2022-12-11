from .base import Base

from app import db

class Gift(Base):
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
        }
