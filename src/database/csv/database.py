"""
This module assists in reading and writing to the CSV file that
contains the data that is gathered by and analyzed by the program

The dataset is set up as follows:
    - Each row is a tweet
    - Different tables are represented by different CSV files
        - unprocessed
        - processed
        - analyzed
    
    - Columns for unprocessed data:
        - community
        - tweet text
    
    - Columns for processed data:
        - community
        - tweet text
        - toxicity score
        - insult score
        - threat score
        - sexually explicit score
        - flirtation score
        - attack on author score
        - attack on commenter score
        - inflammatory score
        - obscene score
    
    - Columns for analyzed data:
        -
"""

import csv
import os

class CsvHelper():
    """
    Assists in reading and writing to the CSV file that contains the data
    """
    def __init__(self) -> None:
        """
        Initializes the CSV files that will be used
        These include
            - unprocessed
            - processed
            - analyzed
        """
        # Initialize the CSV files
        self.unprocessed_writer = csv.writer(open(os.path.join(os.getcwd(), "data", "unprocessed.csv"), "w"))
        self.unprocessed_reader = csv.reader(open(os.path.join(os.getcwd(), "data", "unprocessed.csv"), "r"))

        self.processed_writer = csv.writer(open(os.path.join(os.getcwd(), "data", "processed.csv"), "w"))
        self.processed_reader = csv.reader(open("processed.csv", "r"))

        self.analyzed_writer = csv.writer(open(os.path.join(os.getcwd(), "data", "analyzed.csv"), "w"))
        self.analyzed_reader = csv.reader(open(os.path.join(os.getcwd(), "data", "analyzed.csv"), "r"))
    
    def write_unprocessed(self, community: str, text: str) -> None:
        """
        Writes a row to the unprocessed CSV file    
        
        Args:
            community: The community that the tweet belongs to
            text: The text of the tweet
        """
        self.unprocessed_writer.writerow([community, text])
    
    def write_processed(self, community: str, text: str, perspective_attr: dict) -> None:
        """
        Writes a row to the processed CSV file
        
        Args:
            community (str): The community that the tweet belongs to
            text (str): The text of the tweet
            perspective_attr (dict): The dictionary containing the perspective attributes
        Returns:
            None
        """
        self.processed_writer.writerow(
            [community,
             text,
             perspective_attr["toxicity"],
             perspective_attr["insult"],
             perspective_attr["threat"],
             perspective_attr["sexually_explicit"],
             perspective_attr["flirtation"],
             perspective_attr["attack_on_author"],
             perspective_attr["attack_on_commenter"],
             perspective_attr["inflammatory"],
             perspective_attr["obscene"]]
        )
    
    def write_analyzed(self) -> None:
        """
        Writes a row to the analyzed CSV file
        
        Args:
        Returns:
        """
