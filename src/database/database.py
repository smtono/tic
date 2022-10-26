"""
This module is used to define the database for the system
As well as functions used to interact with the database
This system uses a SQLite database
"""

import sqlite3
from sqlite3 import Error

class Database():
    """
    This class is used to create a database and manipulate it.
    """
    def __init__(self, db_name:str) -> None:
        self.connector = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.connector.cursor()

    def create_db(self, db_name: str):
        """
        Creates a database with the given name

        Args:
            db_name: str
                The name of the database to be created
        """
        self.connector = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.connector.cursor()

    #######################
    # Query Manipulation
    ########################
    def select_data(self, query_for: str, query_table: str):
        """
        Selects data from a table

        Args:
            query_for: str
                The data to be queried
            query_table: str
                The table to be queried
        """
        try:
            self.cursor.execute(f"SELECT {query_for} FROM {query_table};")
            print(self.cursor.fetchall())
        except Error as err:
            if err != 0:
                print("Problem with table Select.")
                print(f"error code: {err}")
            else:
                print("An unknown problem has occured.")

    def insert_data(self, table_name: str, columns: str, data: str):
        """
        Inserts data into a table

        Args:
            table_name: str
                The name of the table to be updated
            columns: str
                The columns to be updated
            data: str
                The data to be inserted
        """
        try:
            self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({data});")
        except Error as err:
            if err != 0:
                print("Problem with Data Insertion.")
                print(f"error code: {err}")
            else:
                print("An unknown problem has occured.")

    def custom_query(self, sql_query:str):
        """
        Executes a custom query

        Args:
            sql_query: str
                The query to be executed
        """
        try:
            self.cursor.execute(sql_query)
        except Error as err:
            if err != 0:
                print("Problem with Custom Query.")
                print(f"error code: {err}")
            else:
                print("An unknown problem has occured.")

    #######################
    # Table Manipulation
    ########################
    def create_table(self, table_name: str, table_args: str):
        """
        Creates a table with the given name

        Args:
            table_name: str
                The name of the table to be created
            table_args: str
                The arguments for the table to be created
        """
        try:
            self.cursor.execute(f"CREATE TABLE {table_name} ({table_args});")
        except Error as err:
            if err != 0:
                print("Table already exists.")
                print(f"error code: {err}")
            else:
                print("An unknown problem has occured.")

    def alter_table(self, table_name: str, table_args: str):
        """
        Alters a table with the given name

        Args:
            table_name: str
                The name of the table to be altered
            table_args: str
                The arguments for the table to be altered
        """
        try:
            self.cursor.execute(f"ALTER TABLE {table_name} {table_args}")
        except Error as err:
            if err != 0:
                print("Problem with table Alter.")
                print(f"error code: {err}")
            else:
                print("An unknown problem has occured.")

    def delete_table(self, table_name: str):
        """
        Deletes a table with the given name

        Args:
            table_name: str
                The name of the table to be deleted
        """
        try:
            self.cursor.execute(f"DROP TABLE {table_name}")
        except Error as err:   
            if err != 0:
                print("Problem with table Delete.")
                print(f"error code: {err}")
            else:
                print("An unknown problem has occured.")

    def update_table(self, table_name:str, data_args:str):
        """
        Updates a table with the given name

        Args:
            table_name: str
                The name of the table to be updated
            data_args: str
                The arguments for the table to be updated
        """
        try:
            self.cursor.execute(f"UPDATE {table_name} SET {data_args}")
        except Error as err:   
            if err != 0:
                print("Problem with table Update.")
                print(f"error code: {err}")
            else:
                print("An unknown problem has occured.")

