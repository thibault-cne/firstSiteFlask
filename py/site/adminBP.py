"""
    Author : Thibault Chenevière
    Date : 09/11/2021
"""

from flask import render_template, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from py.core.formatting import format_users_list, format_deleted_survey_list
from py.site.models import DeletedMessage, User
from main import db

admin = Blueprint('admin', __name__)

@admin.route('/usersList')
@login_required
def users_list_panel():
    if current_user.role == 1:
        usersList = User.query.all()
    
        return render_template("usersList.html", usersList=format_users_list(usersList))

    else:
        flash("Vous n'avez pas la permission pour accéder à cette page", "Red_flash")
        return render_template("home.html")


@admin.route('/deletedSurveysList')
@login_required
def deletedSurveysList_panel():
    if current_user.role == 1:
        deletedSurveys = DeletedMessage.query.all()

        return render_template("deletedMessageList.html", deletedMessageList=format_deleted_survey_list(deletedSurveys))
    
    else:
        flash("Vous n'avez pas la permission pour accéder à cette page", "Red_flash")
        return render_template("home.html")


@admin.route('/usersList', methods=['GET', 'POST'])
def users_panel_validation():
    userId = request.form['userId']
    newUsername = request.form['username']
    newRole = request.form['role']

    user = User.query.filter_by(id=userId).first()

    if int(newRole) not in [0, 1]:
        flash(f"Merci de choisir un role dans la plage {[0, 1]}.", "Red_flash")
        return users_list_panel()
        
    elif newUsername != user.firstName or newRole != user.role:
        user.role = newRole
        user.firstName = newUsername

        db.session.commit()

        flash("Les modifications ont bien été apportée", "Green_flash")
        return users_list_panel()
    
    else:
        return users_list_panel()