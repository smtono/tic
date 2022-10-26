"""
This module is used to define functions used in cleaning the data.
Cleaning the data takes place in the following steps:
    - Restructuring data to conform to the format required by the model.
    - Adding toxicity metrics by running data through Perspective
    - Adding other sentiment metrics by running data through other libs
    - Using classifiers to classify the data into different categories
    - Dividing data into clusters by community
"""

