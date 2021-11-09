"""
    Author : Thibault Chenevière
    Date : 09/11/2021
"""

from flask import render_template, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from py.core.formatting import format_users_list
from py.site.models import User
from main import db

admin = Blueprint('admin', __name__)

@admin.route('/adminPanel')
@login_required
def admin_panel():
    if current_user.role == 1:
        usersList = User.query.all()
    
        return render_template("adminPanel.html", usersList=format_users_list(usersList))

    else:
        flash("Vous n'avez pas la permission pour accéder à cette page", "")
        return render_template("home.html")