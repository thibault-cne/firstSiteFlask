"""
    Author : Thibault Chenevière
    Date : 17/09/2021
"""

from flask import render_template, Blueprint, request, flash
from flask_login import login_required, current_user
from main import db
from py.core.survey2list import survey2list

from py.site.models import Survey, Likes, User


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/createMessage')
@login_required
def createMessage():
    return render_template('createMessage.html', name=current_user.firstName.title())


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
    surveyList = survey2list(surveys)
    return render_template('messages.html', surveys=surveyList)


@main.route('/message', methods=['GET', 'POST'])
@login_required
def addLike():
    userId = current_user.id
    msgId = request.form['messageID']
    
    if msgId == "" or msgId is None:
        flash("Une erreur est arrivé, merci de soumettre votre vote a nouveau", "")
        return message()
    
    checkMsg = Likes.query.filter_by(message_id=msgId, author_id=userId).first()

    if checkMsg is None:
        newLike = Likes(message_id=msgId, author_id=userId)
        msg = Survey.query.filter_by(id=msgId).first()
        msg.voteYes += 1

        db.session.add(newLike)
        db.session.commit()

        return message()
    
    else:
        flash("Vous ne pouvez pas voter 2 fois pour un même sondage", "")
        return message()
    
    
