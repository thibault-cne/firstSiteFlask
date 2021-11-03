"""
    Author : Chenevière Thibault
    Date : 03/11/2021
"""

from main import db, create_app

if __name__ == "__main__":
    db.create_all(app=create_app())