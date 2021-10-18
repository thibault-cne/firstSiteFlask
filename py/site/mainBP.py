"""
    Author : Thibault Chenevière
    Date : 17/09/2021
"""

from flask import render_template, Blueprint, request
from flask_login import login_required, current_user
from main import db
from py.core.survey2list import survey2list

from py.site.models import Survey


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
    surveyTitle = request.form['surveyTitle']
    surveyContent = request.form['surveyArea']
    author_id = current_user.id

    if len(surveyTitle) < 100:
        newSurvey = Survey(title=surveyTitle, content=surveyContent, voteYes=0, author_id=author_id)
        db.session.add(newSurvey)
        db.session.commit()

    return message()



@main.route('/message')
@login_required
def message():
    surveys = Survey.query.all()
    print('yes')
    surveyList = survey2list(surveys)
    return render_template('messages.html', surveys=surveyList)


@main.route('/message')
@login_required
def addLike():
    user = current_user
    userId = user.id
    
