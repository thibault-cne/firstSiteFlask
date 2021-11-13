"""
    Author : Thibault Chenevière
    Date : 13/11/2021
"""

from flask import render_template, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from py.core.formatting import format_users_list
from py.site.models import User
from main import db

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@login_required
def profile_route():
    userId = current_user.id
    user = User.query.filter_by(id=userId).first()
    if user.role == 0:
        role = "Citoyen"
    elif user.role == 1:
        role = "Administrateur"

    profileData = {
        "firstName": current_user.firstName,
        "lastName": user.lastName,
        "role": role,
        "email": user.email,
        "adress": user.adress
    }
    print(profileData)
    return render_template('profile.html', profileData=profileData)

@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_form_validation():
    email = request.form['emailValue']
    adress = request.form['adressValue']

    user = User.query.filter_by(email=email).first()

    user.adress = adress
    db.session.commit()

    flash("Les modifications que vous avez apportez on bien été enregistrée", "Green_flash")

    return profile_route()

