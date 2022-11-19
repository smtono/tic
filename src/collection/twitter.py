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
        
        Args:
            consumer_key: str
                The consumer key for the Twitter API
            consumer_secret: str
                The consumer secret for the Twitter API
            access_token: str
                The access token for the Twitter API
            access_token_secret: str
                The access token secret for the Twitter API
        
        Returns:
            None
        """
        # Authentication
        self.client = tweepy.Client(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret
        )
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        self.api = tweepy.API(auth)
    
    def get_tweets(self, query: str, count: int=10):
        """
        This function is used to get tweets from the Twitter API
        
        Args:
            query: str
                The query to search for
            count: int
                The number of tweets to return
        
        Returns:
            tweets: list
        """
        tweets = self.api.search_tweets(q=query, count=count)
        return tweets
