"""
This is the main entry point for the program

This program is used to analyze datasets and create visualizations regarding Internet communities

This project will be an analysis on what makes the internet TIC (be upset). 
We will find correlations of bridging topics, phrases, and overall similar mannerisms 
between a few known toxic online communities to see if we can find any similarities between them.

Notes:
This program will use the following technologies and methods
- Python
    For data analysis using pandas and other data libraries
- SQLite
    For storing our datasets locally and fetching from in the future
- Entity recognition mining
    For finding the most common words and phrases in the dataset
- Text mining
    For finding relevant information in the dataset
- Sentiment analysis
    For finding the "mood" of individual texts in the dataset

Commands:
    get <query> <count>
        Gets the specified number of tweets from the query passed
        Stores this data in the database under the UNPROCESSED table
    clean <type> <source>
        Cleans the data in the source table by running demoji, deurl, and deretweet
        Cleans the data by removing stop words
        Also adds toxicity metrics by running data through Perspective
    analyze <type> <source>
        Analyzes the data in the source table by running distance metrics and sentiment analysis
        As well as running entity recognition mining and text mining
    visualize <type> <source>
        Visualizes the data in the source table by creating graphs and charts

Usage:
    python tic <command> [<args>...]
"""

import logging
from util.configuration import Configuration
from util.parser import Parser


def main():
    """
    Main entry point for the program
    """
    # Configuration
    config = Configuration()
    config.setup_database()
    config.setup_api()
    ctx = config.ctx
    parser = Parser(ctx)
    
    # Run the CLI
    while True:
        # Get input from the user
        user_input = input('tic> ')
        args = user_input.split(' ')
        parser.parse(args)


if __name__ == "__main__":
    main()
