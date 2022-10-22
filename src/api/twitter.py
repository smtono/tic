"""
This module contains the analysis/preprocessing functions using Twitter's API
"""

class Twitter():
  """
  This class is used to configure the Perspective API and interact with it
  You can use this class to pass in data and run analysis on it
  
  Attributes:
  
  Functions:
  """

import tweepy

consumer_key = "XXXX" #Your API/Consumer key 
consumer_secret = "XXXX" #Your API/Consumer Secret Key
access_token = "XXXX"    #Your Access token key
access_token_secret = "XXXX" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

# TODO: test scraping for my own account

# TODO: test my own tweet against perspective's analysis in main
