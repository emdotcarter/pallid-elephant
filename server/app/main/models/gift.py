import sqlalchemy

from server.app.extensions import db


class Gift(db.Model):
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
        }
