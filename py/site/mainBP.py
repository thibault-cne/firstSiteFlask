"""
    Author : Thibault Chenevière
    Date : 17/09/2021
"""

from flask import render_template, Blueprint, request, flash
from flask_login import login_required, current_user
from main import db
from py.core.survey2list import survey2list
from py.core.checkUsersInfo import checkUsersInfo

from py.site.models import DeletedMessage, Message, Likes, User


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


### message.html configuration : 


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

    user = User.query.filter_by(id=author_id).first()

    if checkUsersInfo(user):
        flash("Merci de referencer votre adresse avant de poster un message", "Red_flash")

        return createMessage()

    elif len(surveyTitle) < 100:
        newSurvey = Message(title=surveyTitle, content=surveyContent, voteYes=0, author_id=author_id)
        db.session.add(newSurvey)
        db.session.commit()

        return message()
    
    else:
        flash("Merci de rentrer un titre de moins de 100 caractères", "Red_flash")

        return createMessage()


@main.route('/message')
@login_required
def message():
    surveys = Message.query.all()
    surveyList = survey2list(surveys)
    return render_template('messages.html', surveys=surveyList)


@main.route('/message', methods=['GET', 'POST'])
@login_required
def addLike():
    userId = current_user.id
    msgId = request.form['messageID']
    
    if msgId == "" or msgId is None:
        flash("Une erreur est arrivé, merci de soumettre votre vote a nouveau", "Red_flash")
        return message()
    
    checkMsg = Likes.query.filter_by(message_id=msgId, author_id=userId).first()

    if checkMsg is None:
        newLike = Likes(message_id=msgId, author_id=userId)
        msg = Message.query.filter_by(id=msgId).first()
        msg.voteYes += 1

        db.session.add(newLike)
        db.session.commit()

        return message()
    
    else:
        flash("Vous ne pouvez pas voter 2 fois pour un même sondage", "Red_flash")
        return message()
    
    
@main.route('/removeMessage', methods=['GET', 'POST'])
@login_required
def removeMessage():
    userRole = current_user.role
    msgId = request.form['deleteBtn']
    print("validate")

    if userRole == 1:
        msg = Message.query.filter_by(id=msgId).first()
        user = User.query.filter_by(id=msg.author_id).first()

        deletedMessage = {
            "id": msgId,
            "title": msg.title,
            "content": msg.content,
            "voteYes": msg.voteYes,
            "author": user.firstName.title() + " " + user.lastName.title()
        }
        print("validate")
        return render_template('deleteMessage.html', deletedMessage=deletedMessage)
    
    else:
        flash("Vous n'avez pas les permissions pour supprimer un message", "Red_flash")

        return message()


@main.route('/removedMessage', methods=['GET', 'POST'])
@login_required
def deleteMessage():
    if current_user.role == 1:
        msgId = request.form['deleteBtn']
        reason = request.form['reasonDelet']
        msg = Message.query.filter_by(id=msgId).first()

        deletedMsg = DeletedMessage(id=msg.id, author_id=msg.author_id, content=msg.content, title=msg.content, voteYes=msg.voteYes, reason=reason)

        db.session.delete(msg)
        db.session.add(deletedMsg)
        db.session.commit()

        flash("Le message a bien été supprimé", "Green_flash")
        return message()
    
    else:
        flash("Vous n'avez pas les permissions pour supprimer un message", "Red_flash")
        return message()