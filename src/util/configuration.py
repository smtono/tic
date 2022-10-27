"""
This module is used to configure the program with various APIs
for preprocessing and analysis
"""

import logging
import os
from database.database import Database

from preprocessing.perspective import Perspective
from collection.twitter import Twitter


class Configuration():
    """
    This class defines the configuration of the program
    It is used to configure the program with various APIs
    for preprocessing and analysis
    """

    def __init__(self) -> None:
        """
        Sets up a context dictionary containing the configuration
        """
        self.ctx = {
            "twitter_api": {},
            "perspective_api": {},
            "database": None,
        }
    
    def setup_database(self) -> None:
        """
        Sets up the database
        
        Args:
            None
        Returns:
            None
        """
        database = Database("tic")
        self.ctx["database"] = database
        
        # Table initialization
        database.create_table("unprocessed", "")
        database.create_table("processed", "")
        database.create_table("community", "")
    
    def setup_api(self) -> None:
        """
        Sets up the configuration context
        
        Args:
            None
        Reutrns:
            None
        """
        # Keys
        if os.path.exists(".env"):
            twitter_api_key = os.getenv("TWITTER_API_KEY")
            perspective_api_key = os.getenv("PERSPECTIVE_API_KEY")
            if twitter_api_key:
                self.ctx["twitter_api"] = twitter_api_key
            else:
                logging.warning("No Twitter API key found in .env file")
            if perspective_api_key:
                self.ctx["perspective_api"] = perspective_api_key
            else:
                logging.warning("No Perspective API key found in .env file")
        else:
            # TODO: fix this so it asks for EVERY key needed
            logging.info("Entering API keys manually")
            twitter_api_key = input("Enter Twitter API key: ")
            perspective_api_key = input("Enter Perspective API key: ")
            self.ctx["twitter_api"] = twitter_api_key
            self.ctx["perspective_api"] = perspective_api_key
        
        # API configuration
        perspective = Perspective(self.ctx["perspective_api"])
        twitter = Twitter(self.ctx["twitter_api"])
        
        self.ctx["perspective"] = perspective
        self.ctx["twitter"] = twitter
