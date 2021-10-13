"""
    Author : Thibault Chenevière
    Date : 17/09/2021
"""

from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
