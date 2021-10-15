"""
    Author : Thibault Chenevière
    Date : 17/09/2021
"""

from flask import render_template, Blueprint
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name.title())


@main.route('/createMessage')
@login_required
def createMessage():
    return render_template('createMessage.html', name=current_user.name.title())


@main.route('/createMessage', methods=['GET', 'POST'])
@login_required
def createMessage_form():
    return render_template('createMessage.html', name=current_user.name.title())



@main.route('/message')
def message():
    return render_template('messages.html')
