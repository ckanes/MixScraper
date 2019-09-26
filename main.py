#!/usr/bin/env python3

""" main.py executes the main functionality of the mix scraper.

    Information is pulled from www.1001tracklists.com, placed in a database and then processed by the user.
"""

# Defining full package imports

# Importing the functions created as part of this software
from functions import databasehandler as dbh
from functions import webscraper


if __name__ == "__main__":
    database_connection = dbh.create_connection("MixScraper.db")    # Defining the database connection
    dbh.create_all_tables(database_connection, dbh.TABLES)          # Creating all tables in the database

