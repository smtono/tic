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

import os
import json

from googleapiclient import discovery

API_KEY = os.getenv("GOOGLE_PERSPECTIVE_API_KEY")
print(API_KEY)

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

analyze_request = {
  'comment': { 'text': 'this is a test' },
  'requestedAttributes': {'TOXICITY': {}}
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))
