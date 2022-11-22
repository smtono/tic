"""
This module contains the definition of the Parser class
This parser is used to parse the command line arguments

Commands include:
    - get <query> --c <count>
        Gets the specified number of tweets from the query passed
        Stores this data in the database under the UNPROCESSED table
    - clean <name>
        Cleans the data in the source table by running demoji, deurl, and deretweet
        Cleans the data by removing stop words
        Also adds toxicity metrics by running data through Perspective
    
"""

from preprocessing.clean import run_all
class Parser():
    """
    Class definiton for CLI parser
    """
    def __init__(self, ctx: list) -> None:
        """
        Constructor for the Parser class
        """
        self.ctx = ctx

        # Supported commands
        self.commands = {
            "get": self.get,
            "clean": self.clean,
            "analyze": self.analyze,
            "visualize": self.visualize
        }

    def parse(self, args: list):
        """
        Parses user args for the CLI
        
        Args:
            args: list
                List of arguments passed by the user
        Returns:
            None
        """
        command = args[0]   # command to execute
        args = args[1:]     # args to pass to command
        
        # Get the command function
        command_function = self.commands.get(command)
        
        # If the command is not found, print an error message
        if command_function is None:
            print(f'Command {command} not found')
            return
        else:
            getattr(self, command)(args)

    def get(self, args: list) -> list:
        """
        Gets tweets from the Twitter API
        
        Args:
            args: list
                List of arguments passed by the user
        Returns:
            list
                List of tweets
        """
        # Get the query and count from the args
        command = ' '.join(args)
        query = command.split('--c')[0].strip()
        count = command.split('--c')[1].strip()

        # Get tweets
        tweets = self.ctx['twitter'].get_tweets(query, count)
        
        # Insert tweets into unprocessed table in DB
        for tweet in tweets:
            self.ctx['database'].insert_data('unprocessed', 'community, postID, data', f"{query}, {tweet.id}, '{tweet.text}'")

        # Return the tweets
        for tweet in tweets:
            print(tweet.text)
        return tweets
    
    def clean(self, args: list):
        """
        Cleans the data in the source table by running demoji, deurl, and deretweet
        Cleans the data by removing stop words
        Also adds toxicity metrics by running data through Perspective
        """
        # Get the name of dataset to clean
        dataset = args[0]
        
        # Get the data that has that name from DB
        data = self.ctx['database'].select_data('*', 'unprocessed', f"community = '{dataset}'")
        
        cleaned_data = []
        # Clean the data
        for row in data:
            cleaned_data.append(run_all(row[2]))
        
        parameterized_data = []
        # Add toxicity metrics
        for row in cleaned_data:
            self.ctx['perspective'].analyze(row)
            
        for row in parameterized_data:
            # TODO: test this
            self.ctx['database'].insert_data('processed', 'community, postID, data', f"{dataset}, {row[0]}, '{row[1]}'")

    def analyze(self, args: list):
        """
        Analyzes the data in the source table by running distance metrics and sentiment analysis
        As well as running entity recognition mining and text mining
        """
    
    def visualize(self, args: list):
        """
        Visualizes the data in the source table by creating graphs and charts
        """
