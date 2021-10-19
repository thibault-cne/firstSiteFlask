"""
    Author : Thibault Chenevière
    Date : 18/10/2021
"""

from py.site.models import User


def survey2list(surveys: list) -> list:
    """
        Description :
            Take a list of Survey object and return a list of 3 items
            list with first item being the author name than in second the
            survey title, in third the survey content and in fourth the
            number of likes.

        
        Parameters :
            - survey (list[Survey]) : list of Survey objects

        Returns :
            - returnList (list[list]) : list of list with author name,
            survey title, survey content and numbers of likes
    """
    resultList = []
    for survey in surveys:
        temp = [0, 0, 0, 0, 0]
        user = User.query.filter_by(id=survey.author_id).first()
        userName = user.name

        temp[0] = userName
        temp[1] = survey.title
        temp[2] = survey.content
        temp[3] = survey.voteYes
        temp[4] = survey.id

        resultList.append(temp)
    
    return resultList

