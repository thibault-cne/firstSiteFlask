"""
    Author : Thibault Cheneviere
    Date : 20/11/2021
"""

# Import de module
from datetime import datetime


def checkFormatBirthDate(birthDate):
    format = "%d/%m/%Y"

    try:
        date = datetime.strptime(birthDate, format)
        return True, date
    
    except ValueError:
        return False, None