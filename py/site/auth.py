"""
    Author : Thibault Chenevière
    Date : 26/09/2021
"""

from flask import render_template, url_for, request, Blueprint
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from py.site.models import User
from __init__ import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup_validation():
    email = request.form['eMail']
    name = request.form['username']
    password = request.form['password']
    confPassword = request.form['confirmationPassword']
    print(f"{password}, {confPassword}")

    user = User.query.filter_by(email=email).first()

    if user is None:
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.home'))
    else:
        return redirect(url_for('auth.login'))