import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def connect():
        databasefile = r"GSGD_ANN.db3"
        connlite = create_connection(db_file=databasefile)
        connlite.row_factory = sqlite3.Row
        return connlite
