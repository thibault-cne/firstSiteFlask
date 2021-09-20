"""
    Author : Thibault Chenevière
    Date : 17/09/2021
"""

import sqlite3 as sq
import bcrypt


def connection():
    """
        Description : return the connection and cursor object
        of the database project.
    """
    con = sq.connection('firstSite.db')
    cursor = con.cursor()
    return con, cursor


def queryDB(query, args=None):
    """
        Description : function to push queries to teh DB

        Arguments :
            - query (str) : query to push in the database
            - args (can be None or tuple) : arguments for the query 
    """
    if args is None:
        con, cursor = connection()
        cursor.execute(query)
        con.close()
    else:
        con, cursor = connection()
        cursor.execute(query, args)
        con.close()


def add_user(userName, eMail, password):
    """
        Description : function to add a new user in the database, using hash to secure the password

        Arguments :
            - userName (str) : username of the user to add in the DB
            - eMail (str) : email of the user to add in the DB
            - password (str) : password of the user to add in the DB
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    query = "insert into users values (?, ?, ?)"
    args = (userName, eMail, hashed)

    queryDB(query, args)

 
def create_table(name, columns):
    """
        Description : function to create a new table in the DB

        Arguments :
            - name (str) : name of the table about to be created
            - columns (list) : list of the columns of the new table
    """
    query = "create table " + name
    for i in range(len(columns)):
        if i == 0:
            query += " (" + columns[i] + ","
        elif i == len(columns) - 1:
            query += " " + columns[i] + ")"
        else:
            query += " " + columns[i] + ","
    
    queryDB(query)
