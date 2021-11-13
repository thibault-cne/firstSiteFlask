"""
    Author : Thibault Chenevière
    Date : 26/09/2021
"""

from flask import render_template, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from py.site.models import User
from main import db

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
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    password = request.form['password']
    confPassword = request.form['confirmationPassword']
    remember = request.form['remember']

    user = User.query.filter_by(email=email).first()
    
    if password != confPassword:
        flash("Les mots de passes ne sont pas identiques.", "")
        return redirect(url_for('auth.signup'))
    elif len(password) < 4 or len(password) > 20:
        flash("Merci de rentrer un mot de passes entre 4 et 20 caractères.", "")
        return redirect(url_for('auth.signup'))
    elif user is None:
        new_user = User(email=email, firstName=firstName, password=generate_password_hash(password, method='sha256'), role=0, lastName=lastName, adress="")

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user, remember=remember)
        profileData = {
            "firstName": firstName,
            "role": "Citoyen",
            "email": email,
            "lastName": lastName,
            "adress": ""
        }
        return render_template('profile.html', profileData=profileData)
    else:
        flash(f"Il existe déjà un compte avec cette adresse mail.", "site_flash")
        return redirect(url_for('auth.signup'))


@auth.route('/login', methods=['GET', 'POST'])
def login_validation():
    email = request.form['eMail']
    password = request.form['password']
    remember = request.form['remember']
    print(remember)

    user = User.query.filter_by(email=email).first()

    if user is None:
        flash("Il n'existe pas de compte avec cet adresse mail", "")
        return redirect(url_for('auth.signup'))
    elif check_password_hash(user.password, password):
        login_user(user, remember=remember)
        return redirect(url_for('profile.profile_route'))
    else:
        flash("Compte ou mot de passe incorrect", "")
        return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))