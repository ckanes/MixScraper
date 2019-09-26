#!/usr/bin/env python3

""" databasehandler.py provides the database utilities used by MixScraper.

    Defines functions for the creation and manipulation of databases or data in the database structure.
"""

# Defining full package imports
import sqlite3
import os

# Defining specific imports
from sqlite3 import Error

# Importing the functions created as part of this software
from functions import utilities as ut

# Defining variables used to define the MIXTIMESTAMPS string
MIX_MAX = 5
KEYS = ", ".join(["TrackID_{} INTEGER NOT NULL, TimeStamp_{} TIME (0) NOT NULL".format(i, i) for i in range(MIX_MAX)])
REFS = ", ".join(["FOREIGN KEY (TrackID_{}) REFERENCES tracks (TrackID)".format(i) for i in range(MIX_MAX)])


# Defining the table creation strings
ARTISTS         = """CREATE TABLE IF NOT EXISTS artists (   ArtistID INTEGER PRIMARY KEY,
                                                            ArtistName VARCHAR NOT NULL,
                                                            GenreID INTEGER NOT NULL,
                                                            FOREIGN KEY (GenreID) REFERENCES genres (GenreID)   )"""
GENRES          = """CREATE TABLE IF NOT EXISTS genres (    GenreID INTEGER PRIMARY KEY,
                                                            GenreName VARCHAR NOT NULL  )"""
MIXARTISTS      = """CREATE TABLE IF NOT EXISTS mixes (     MixID INTEGER PRIMARY KEY,
                                                            MixName VARCHAR NOT NULL,
                                                            ArtistID INTEGER NOT NULL,
                                                            FOREIGN KEY (ArtistID) REFERENCES artists (ArtistID)    )"""
TRACKS          = """CREATE TABLE IF NOT EXISTS tracks (    TrackID INTEGER PRIMARY KEY,
                                                            TrackName VARCHAR NOT NULL,
                                                            ArtistID INTEGER NOT NULL,
                                                            FOREIGN KEY (ArtistID) REFERENCES artists (ArtistID)    )"""
MIXTIMESTAMPS   = "CREATE TABLE IF NOT EXISTS tracklist (   MixID INTEGER PRIMARY KEY, " + KEYS + ", " + REFS + ")"


# Compiling all tables together into one data structure
TABLES          = [ARTISTS, GENRES, MIXARTISTS, TRACKS, MIXTIMESTAMPS]


# Defining utility functions
def obtain_database_name():
    """ obtain_database_name        Obtains the database name from the user. If the database doesn't exist it is created
                                    otherwise the user is notified.
        ----------------------------------------------------------------------------------------------------------------
        Variable(s)
                                    No input variables

        Output(s)
                                    Creates the database filename or indicates that the filename already exists.
        ================================================================================================================
    """

    while True:
        # Obtaining the filename from the user
        user_input = input("Please enter the name of the database you wish to create or connect to, inc. extension: ")
        # Checking to see if the file exists
        if os.path.exists(f'./{user_input}'):
            # Asserting that the user wishes to connect to this database
            if ut.assertion(user_input, "You database name you entered already exists"):
                return user_input
            # Asking the user to enter the filename again
            else:
                continue
        # 
        else:



def create_connection(database_name):
    """ create_connection           Creates a connection to a database. Throws an error if this is not possible.
        ----------------------------------------------------------------------------------------------------------------
        Variable(s)
            database_name           The name of the database to connect to.

        Output(s)
                                    Returns the connection to the database.
        ================================================================================================================
    """

    # Defining an empty connection
    conn = None

    # Attempting connection to the database
    try:
        conn = sqlite3.connect(database_name)
        return conn
    # Printing the error if failure occurs
    except Error as e:
        print(e)

    # Returning the connection to the database
    return conn


def create_table(conn, create_table_sql):
    """ create_table                Creates a table in the database connected. Throws an error if this is not possible.
        ----------------------------------------------------------------------------------------------------------------
        Variable(s)
            conn                    The connection to the database.
            create_table_sql        The table creation SQL string.

        Output(s)
                                    Adds the table to the database.
        ================================================================================================================
    """

    # Attempting to create the table in the database
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    # Printing the error if failure occurs
    except Error as e:
        print(e)

    # Returning void
    return


def create_all_tables(conn, tables):
    """ create_all_tables           Caller function to create multiple tables.
        ----------------------------------------------------------------------------------------------------------------
        Variable(s)
            conn                    The connection to the database.
            tables                  List of table creation SQL strings.

        Output(s)
                                    Adds the tables to the database.
        ================================================================================================================
    """

    # Looping over the list of creation strings
    for table in tables:
        # Attempting to create the table in the database
        try:
            print(table)
            create_table(conn, table)
        # Printing the error if failure occurs
        except Error as e:
            print(e)
            continue

    # Returning void
    return


if __name__ == "__main__":
    pass
