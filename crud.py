from model import db, connect_to_db, User
from datetime import date, datetime


# -------------------- USERS -------------------- #


def create_user(email, first_name, last_name, username, password, join_date, website, city, pronouns):
    """Create and return a new user."""

    user = User(email=email, first_name=first_name, last_name=last_name, username=username, password=password, join_date=join_date, website=website, city=city, pronouns=pronouns)

    db.session.add(user)
    db.session.commit()

    return user


def get_all_users():
    """Return all users."""

    return User.query.all()


def get_user_by_email(email):
    """Return a user given an email address."""

    return User.query.filter(User.email == email).first()

    
def get_user_by_username(username):
    """Return user given their username"""

    return User.query.filter(User.username == username).first() 

def get_user_by_id(user_id):
    """Return user given their ID"""

    return User.query.filter(User.user_id == user_id).first() 

def get_user_by_email_id(email, username):

    return User.query.filter((User.email == email) |
                             (User.username == username)).all()