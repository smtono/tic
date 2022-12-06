"""
This module contains the analysis functions using Google's Perspective API

We will be using the following technologies and methods
    - Google Perspective API
        For finding the toxicity of individual texts in the dataset
        This API has the following attributes:
            - Toxity
            - spanScores
                - begin
                - end
                - score
                    - value
                    - type
            - summaryScore
                - value
                - type
            - languages
            - detectedLanguages
"""

import logging
import os
import json
import sys
import time

from googleapiclient import discovery
class Perspective():
  """
  This class is used to configure the Perspective API and interact with it
  You can use this class to pass in data and run analysis on it
  
  Attributes:
    client: The client for the Perspective API
  
  Functions:
    analyze: Analyzes the text using the Perspective API
  """
  
  def __init__(self, api_key: str=None) -> None:
    """
    Configures the Perspective API
    
    Args:
      api_key: The API key for the Perspective API
    """
    
    if api_key:
      self.client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=api_key,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
      )
    else:
      logging.warning("No API key provided for Perspective API")
      self.client = None
      
      # TODO: specific exception handling ?
      # raise Exception("No API key provided for Perspective API")

  def analyze(self, text: str, requested_attribute: str=None) -> dict:
    """
    Analyzes the text using the Perspective API
    
    Args:
      text: The text to be analyzed
      
    Returns:
      The response from the Perspective API
    """
    response = {}
    if not self.client:
      logging.warning("No client configured for Perspective API")
      return None

    if not requested_attribute:
      requested_attribute = {
        'TOXICITY': {}
      } # default
      request = {
          'comment': { 'text': text },
          'requestedAttributes': requested_attribute
      }
      try:
        time.sleep(1) # Perspective API has a limit of 1 request per second
        res = self.client.comments().analyze(body=request).execute()
        response['TOXICITY'] = res["attributeScores"]['TOXICITY']["summaryScore"]["value"]
      except Exception as e:
          print(f"{e}\n\n")
          response['TOXICITY'] = 0.0

    elif requested_attribute == "ALL":
      attributes = [
        "INSULT",
        "THREAT",
        "SEXUALLY_EXPLICIT",
      ]
      for attribute in attributes:
        request = {
          'comment': { 'text': text },
          'requestedAttributes': {attribute: {}}
        }
        try:
          time.sleep(2) # Perspective API has a limit of 1 request per second
          res = self.client.comments().analyze(body=request).execute()
          response[attribute] = res["attributeScores"][attribute]["summaryScore"]["value"]
        except Exception as e:
          if e.resp.status == 429:
            print("API rate limit exceeded")
            sys.exit(1)
          else:
            print(f"{e}\n\n")
            response[attribute] = 0.0

      return response
  
    else:
      requested_attributes = {
        requested_attribute.upper(): {}
      }

      analyze_request = {
        'comment': { 'text': text },
        'requestedAttributes': requested_attributes
      }

      try:
        time.sleep(1) # Perspective API has a limit of 1 request per second
        res = self.client.comments().analyze(body=analyze_request).execute()
        response = res["attributeScores"][requested_attribute.upper()]["summaryScore"]["value"]
      except Exception as e:
        print(f"{e}\n\n")
        response[attribute] = 0.0
    
    return response

if __name__ == "__main__":
  # Test Perspective API
  request = "all"
  perspective = Perspective(os.environ['GOOGLE_PERSPECTIVE_API_KEY'])
  response = perspective.analyze("You are a stupid idiot", request)
  print(response)
