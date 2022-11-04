"""
This module contains the definition of the Parser class
This parser is used to parse the command line arguments

Commands include:
    - get <query> <count>
        Gets the specified number of tweets from the query passed
        Stores this data in the database under the UNPROCESSED table
    - clean <type> <source>
        Cleans the data in the source table by running demoji, deurl, and deretweet
        Cleans the data by removing stop words
        Also adds toxicity metrics by running data through Perspective
    
"""

class Parser():
    """
    Class definiton for CLI parser
    """
