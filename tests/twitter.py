"""
This module is used to test the Twitter class
"""

from asyncio.log import logger
import os
import unittest
import src.preprocessing.twitter as twitter

class TestTwitter(unittest.TestCase):
    """
    Test the Twitter API class
    """
    def test_authentication(self):
        # Test environment variables
        if os.getenv('TWITTER_CONSUMER_KEY') is None:
            logger.error('TWITTER_CONSUMER_KEY is not set')
        if os.getenv('TWITTER_CONSUMER_SECRET') is None:
            logger.error('TWITTER_CONSUMER_SECRET is not set')
        if os.getenv('TWITTER_ACCESS_TOKEN') is None:
            logger.error('TWITTER_ACCESS_TOKEN is not set')
        if os.getenv('TWITTER_ACCESS_TOKEN_SECRET') is None:
            logger.error('TWITTER_ACCESS_TOKEN_SECRET is not set')
        
        twitter_api = twitter.Twitter(
            os.getenv("TWITTER_CONSUMER_KEY"),
            os.getenv("TWITTER_CONSUMER_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )

        # Check API exists
        self.assertIsNotNone(twitter_api.client)
        self.assertIsNotNone(twitter_api.api)
    
    def test_get_tweet(self):
        """
        OBJECTIVE: Test the get_tweet function
        """
        pass

    def test_get_mass_tweets(self):
        """
        OBJECTIVE: Test the get_mass_tweets function
        """
        pass

if __name__ == "__main__":
    unittest.main()
