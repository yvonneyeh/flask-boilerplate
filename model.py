"""Models for Flask app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """An app user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    def __repr__(self):
        """Show info about user."""

        return f"<User_id: {self.user_id} Name: {self.first_name} {self.last_name}>"


# -------------------- DATABASE -------------------- #


def connect_to_db(flask_app, db_uri='postgresql:///contacts', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to DB!')        



if __name__ == '__main__':
    from app import app
    connect_to_db(app, echo=False)
    db.create_all()