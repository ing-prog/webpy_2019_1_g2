import sqlite3


conn = sqlite3.connect('your_database_name.db')
cur = conn.cursor()
"""Make nice docstring for each function or method"""

#
def create_db():
    cur.execute("blah blah blah")

def update_db(*some_parameters):
    cur.execute("blah blah blah")

def reopen_connect():   #should open connect to db, if it closed

def IsClose(): ## check closed connection with db
    return True/False

def ....
