"""
This module is used to configure the program with various APIs
for preprocessing and analysis
"""

import logging
import os
from database.csv.database import CsvHelper
from database.sql.database import Database

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
            "twitter": None,
            "perspective": None,
            "csv_helper": None,
            "database": None,
        }
    
    def setup_csv(self) -> None:
        """
        Sets up the CSV helper
        """
        self.ctx["csv_helper"] = CsvHelper()
    
    def setup_database(self) -> None:
        """
        Sets up the database
        
        Args:
            None
        Returns:
            None
        """
        if os.path.exists(os.path.join(os.getcwd(), "src", "data", "tic.db")):
            logging.info("Database already exists")
            database = Database("tic")
            self.ctx["database"] = database
            return
        else:
            logging.info("Creating database")
            database = Database("tic")
            self.ctx["database"] = database
            # Table initialization
            database.create_table("unprocessed", "community TEXT, postID int, data TEXT, PRIMARY KEY (postID)")
            database.create_table("processed ", 
                                  "community TEXT, "
                                  "postID int, "
                                  "data TEXT, "
                                  "toxicity_score REAL, "
                                  "insult_score REAL, "
                                  "threat_score REAL, "
                                  "sexually_explicit_score REAL, "
                                  "flirtation_score REAL, "
                                  "attack_on_author_score REAL, "
                                  "attack_on_commentor_score REAL, "
                                  "inflammatory_score REAL, "
                                  "obscene_score REAL, "
                                  "PRIMARY KEY (postID)")
            database.create_table("community", "community TEXT, score REAL, topics TEXT, PRIMARY KEY (community)")
    
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
            try:
                # Twitter API
                self.ctx["twitter_api"]["consumer_key"] = os.getenv("TWITTER_CONSUMER_KEY")
                self.ctx["twitter_api"]["consumer_secret"] = os.getenv("TWITTER_CONSUMER_SECRET")
                self.ctx["twitter_api"]["access_token"] = os.getenv("TWITTER_ACCESS_TOKEN")
                self.ctx["twitter_api"]["access_token_secret"] = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
                self.ctx["twitter_api"]["bearer_token"] = os.getenv("TWITTER_BEARER_TOKEN")
                self.ctx["twitter_api"]["client_id"] = os.getenv("TWITTER_CLIENT_ID")
                self.ctx["twitter_api"]["client_secret"] = os.getenv("TWITTER_CLIENT_SECRET")
                # Perspective API
                self.ctx["perspective_api"]["api_key"] = os.getenv("GOOGLE_PERSPECTIVE_API_KEY")
            except Exception as e:
                logging.error(f"Error: {e}")
        else:
            # Twitter API
            logging.info("Entering API keys manually")
            self.ctx["twitter_api"]["consumer_key"] = input("Enter Twitter consumer key: ")
            self.ctx["twitter_api"]["consumer_secret"] = input("Enter Twitter consumer secret: ")
            self.ctx["twitter_api"]["access_token"] = input("Enter Twitter access token: ")
            self.ctx["twitter_api"]["access_token_secret"] = input("Enter Twitter access token secret: ")
            self.ctx["twitter_api"]["bearer_token"] = input("Enter Twitter bearer token: ")
            self.ctx["twitter_api"]["client_id"] = input("Enter Twitter client id: ")
            self.ctx["twitter_api"]["client_secret"] = input("Enter Twitter client secret: ")
            # Perspective API
            self.ctx["perspective_api"]["api_key"] = input("Enter Google Perspective API key: ")
        
        # API configuration
        perspective = Perspective(self.ctx["perspective_api"]['api_key'])
        twitter = Twitter(
            self.ctx["twitter_api"]['consumer_key'],
            self.ctx["twitter_api"]['consumer_secret'],
            self.ctx["twitter_api"]['access_token'],
            self.ctx["twitter_api"]['access_token_secret']
        )
        self.ctx["perspective"] = perspective
        self.ctx["twitter"] = twitter
