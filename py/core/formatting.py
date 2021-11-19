"""
    Author : Thibault Cheneviere
    Date : 09/11/2021
"""

from py.site.models import User


def format_email(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    extendedUsername = username.split(".")
    domainName = domain.split(".")[0]
    domainType = domain.split(".")[1]
    
    formatedMail = ""
    for subUsername in extendedUsername:
        formatedMail += subUsername[0] + "*" * (len(subUsername)-1) + "."
    
    for i in range(1, len(domainName)):
        domainName = domainName[0] + "*" * (len(domainName)-1)
    
    for i in range(1, len(domainType)):
        domainType = domainType[0] + "*" * (len(domainType)-1)
    
    return formatedMail + "@" + domainName + "." + domainType


def format_users_list(usersList):
    userList = []
    for users in usersList:
        if users.firstName != "admin":
            temp = [users.id, users.firstName, users.lastName, format_email(users.email), users.role]
            userList.append(temp)

    return userList


def format_deleted_survey_list(deletedSurveyList):
    deletedSurveys = []

    for surveys in deletedSurveyList:
        user = User.query.filter_by(id=surveys.author_id).first()
        authorName = user.firstName.title() + " " + user.lastName.title()

        temp = [authorName, surveys.title, surveys.content, surveys.voteYes, surveys.reason]

        deletedSurveys.append(temp)
    
    return deletedSurveys