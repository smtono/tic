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

  def analyze(self, text: str, requested_attributes: dict=None) -> dict:
    """
    Analyzes the text using the Perspective API
    
    Args:
      text: The text to be analyzed
      
    Returns:
      The response from the Perspective API
    """
    if not self.client:
      logging.warning("No client configured for Perspective API")
      return None

    if not requested_attributes:
      requested_attributes = {'TOXICITY': {}} # default
    else:
        # TODO: create structs for requested attributes / different combos
        pass

    analyze_request = {
      'comment': { 'text': text },
      'requestedAttributes': requested_attributes
    }
    
    return self.client.comments().analyze(body=analyze_request).execute()
