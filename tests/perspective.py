"""
This module is used to test the Perspective API class
and its functions for analyzing pieces of text
"""

import os
import unittest
import src.api.perspective as perspective

class TestPerspective(unittest.TestCase):
    """
    OBJECTIVE: Test the Perspective API class
    """
    def test_configuration(self):
        """
        OBJECTIVE: Test the configuration of the Perspective API
        """
        # Test with valid API key
        perspective = perspective.Perspective(os.getenv("GOOGLE_PERSPECTIVE_API_KEY"))
        self.assertIsNotNone(perspective.client)
        
        # Test without API key
        perspective = perspective.Perspective()
        self.assertIsNone(perspective.client)
        
        # Test with invalid API key
        perspective = perspective.Perspective("bubba gump shrimp co")
        self.assertIsNone(perspective.client)
        
        # Maybe change following statement if not using exception handling
        self.assertRaises(Exception, perspective.client)
    
    def test_analyze(self):
        """
        OBJECTIVE: Test the analyze function
        """
    
