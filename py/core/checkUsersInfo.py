"""
    Author : Thibault Cheneviere
    Date : 17/11/2021
"""

def checkUsersInfo(user):
    return user.adress == "" or user.gender == "" or user.birthDate == None or user.postalCode == None or user.city == ""