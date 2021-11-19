"""
    Author : Thibault Chenevière
    Date : 28/09/2021
"""

from flask_login import UserMixin
from main import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    role = db.Column(db.Integer)
    adress = db.Column(db.String(1000))
    city = db.Column(db.String(100))
    postalCode = db.Column(db.Integer)
    birthDate = db.Column(db.Date)
    gender = db.Column(db.String(100))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer)
    title = db.Column(db.String(100))
    content = db.Column(db.String)
    voteYes = db.Column(db.Integer)


class Likes(db.Model):
    message_id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer, primary_key = True)


class DeletedMessage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer)
    title = db.Column(db.String(100))
    content = db.Column(db.String)
    voteYes = db.Column(db.Integer)
    reason = db.Column(db.String)