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
- MySQL
    For storing our datasets locally and fetching from in the future
- Entity recognition mining
    For finding the most common words and phrases in the dataset
- Text mining
    For finding relevant information in the dataset
- Sentiment analysis
    For finding the "mood" of individual texts in the dataset

Commands:
    twitter --query <query> --count <count>
    perspective --text <text> --attributes <attributes>

Usage:
    python main.py <command> [<args>...]
"""

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
    parser = Parser(config.ctx)
    
    # Run the parser
    parser.parser.parse_args()


if __name__ == "__main__":
    main()
