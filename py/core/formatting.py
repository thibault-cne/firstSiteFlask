"""
    Author : Thibault Cheneviere
    Date : 09/11/2021
"""

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
        temp = [users.name, format_email(users.email), users.role]
        userList.append(temp)

    return userList

    