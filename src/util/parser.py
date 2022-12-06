"""
This module contains the definition of the Parser class
This parser is used to parse the command line arguments

Commands include:
    - get <query> --c <count>
        Gets the specified number of tweets from the query passed
        Stores this data in the database under the UNPROCESSED table
    - clean <dataset>
        Cleans the data in the source table by running demoji, deurl, and deretweet
        Cleans the data by removing stop words
    -gain <method> <dataset>
        Run perspective API to gain toxicity metrics
        Run distance metrics to gain similarity metrics
        Run entity recognition mining to gain topically relevant words
    -analyze <method> <dataset>
        Analyzes the data in the source table by running distance metrics and sentiment analysis
    -visualize <method> <args> <dataset>
        Visualizes the data in the source table by creating graphs and charts
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
            # Data collection and analysis
            "get": self.get,
            "clean": self.clean,
            "gain": self.gain,
            "analyze": self.analyze,
            "visualize": self.visualize,
            
            # Administative commands
            "sql": self.sql,
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
        community = args[0]
        query = args[1]
        count = command.split('--c')[1].strip()

        # Get tweets
        tweets = self.ctx['twitter'].get_tweets(query, count)
        
        # Insert tweets into unprocessed table in DB
        for tweet in tweets:
            self.ctx['database'].insert_data('unprocessed', 'community, postID, data', f"'{community}', '{tweet.id}', '{tweet.text}'")
        
        self.ctx['database'].commit()

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
        
        # Clean the data
        for row in data:
            res = run_all(row[2])

            # Insert the cleaned data into the processed table
            self.ctx['database'].insert_data(
                'processed',
                'community, postID, data',
                f"'{dataset}', '{row[1]}', '{res}'")
        
        self.ctx['database'].commit()

    def gain(self, args: list):
        """
        Gains the data in the source table by running perspective API
        """
        # Create args
        method = args[0]
        
        if method == 'perspective':
            valid_attributes = [
                "ALL",
                "TOXICITY",
                "INSULT",
                "THREAT",
                "SEXUALLY_EXPLICIT",
                "FLIRTATION",
                "ATTACK_ON_AUTHOR",
                "ATTACK_ON_COMMENTER",
                "INFLAMMATORY",
                "OBSCENE",
            ]
            
            # Args
            if args[1].upper() in valid_attributes:
                attribute = args[1].upper()
            else:
                attribute = 'TOXICITY'

            print("Beginning Perspective analysis")
            # Get the data that has that name from DB
            try:
                data = self.ctx['database'].select_data('*', 'processed')
            except Exception as e:
                print(e)
                return

            for row in data:
                metrics = self.ctx['perspective'].analyze(row[2], attribute)
                
                for metric in metrics:
                    # Insert metrics into DB
                    self.ctx['database'].update_row(
                        'processed', 
                        f"{metric.lower()}_score = '{metrics[metric]}'",
                        f"postID = '{row[1]}'")
                    self.ctx['database'].commit()
            
            print("Perspective analysis complete")

    def analyze(self, args: list):
        """
        Analyzes the data in the source table by running distance metrics and sentiment analysis
        As well as running entity recognition mining and text mining
        """
    
    def visualize(self, args: list):
        """
        Visualizes the data in the source table by creating graphs and charts
        """
    
    def sql(self, args: list):
        """
        Executes a SQL query on the database
        """
        # Get the query
        query = ' '.join(args)
        
        # Execute the query
        self.ctx['database'].custom_query(query)
