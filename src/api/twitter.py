"""
This module contains the analysis/preprocessing functions using Twitter's API
"""

import tweepy

class Twitter():
    """
    This class is used set up a Twitter API object
    for use in tweet/data gathering.

    Attributes:

    Functions:
    """
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        """
        This function is used to set up the Twitter API object
        """
        # Authentication
        # callback_uri = 'oob'
        auth = tweepy.OAuthHandler(
            consumer_key, consumer_secret, 'oob')
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)
    
    def get_tweets(self, query: str, count: int=10):
        """
        This function is used to get tweets from the Twitter API
        """
        tweets = self.api.search(q=query, count=count)
        return tweets
        

# TODO: test scraping for my own account

# TODO: test my own tweet against perspective's analysis in main
