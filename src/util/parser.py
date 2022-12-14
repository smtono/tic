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

from analysis.cluster import get_representative
from analysis.distance import get_distance
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
            "cluster": self.cluster,
            "distance": self.distance,
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
    
    def cluster(self, args: list):
        """
        Clusters the data in the source table by running kmeans
        Finds representatives of each cluster
        
        Examples:
            cluster kmeans <dataset> <k>
            cluster community <dataset>
        """
        method = args[0] # clustering method
        
        if method == 'community':
            data = []
            
            # Get data
            gaming_data = self.ctx['database'].select_data('*', 'processed', "community = 'gaming'")
            politics_data = self.ctx['database'].select_data('*', 'processed', "community = 'politics'")
            youtube_data = self.ctx['database'].select_data('*', 'processed', "community = 'youtube'")
            stem_data = self.ctx['database'].select_data('*', 'processed', "community = 'stem'")
            
            data.append(gaming_data)
            data.append(politics_data)
            data.append(youtube_data)
            data.append(stem_data)
            
            # 0 = community,
            # 1 = postID, 
            # 2 = data
            # 3 = toxicity_score
            # 4 = insult_score
            # 5 = threat_score
            # 6 = sexually_explicit_score
            for community in data:
                scores = {} # container for scores

                for row in community: # Add scores
                    scores[row[1]] = [row[3], row[4], row[5], row[6]]
            
                # Find the representative
                cluster = get_representative(scores)
                
                # Add cluster rep to DB
                self.ctx['database'].insert_data(
                    "clusters",
                    "cluster, "
                    "representative, "
                    "toxicity_score, "
                    "insult_score, "
                    "threat_score, "
                    "sexually_explicit_score",
                    f"'{community[0][0]}', "
                    f"'{cluster[0]}', "
                    f"'{cluster[1][0]}', "
                    f"'{cluster[1][1]}', "
                    f"'{cluster[1][2]}', "
                    f"'{cluster[1][3]}'"
                )

            self.ctx['database'].commit()

        else:
            print("Not implemented yet")
    
    def distance(self, args: list):
        """
        Finds the distance between two objects

        Args:
            args (list): _description_
        """
        distances = {
            'gaming': {},
            'politics': {},
            'youtube': {},
            'stem': {}
        }
        data = self.ctx['database'].select_data('*', 'clusters')

        for cluster in data:
            community = cluster[0]
            post_id = cluster[1]
            toxicity_score = cluster[2]
            insult_score = cluster[3]
            threat_score = cluster[4]
            sexually_explicit_score = cluster[5]
            
            metrics = []
            for other_cluster in data:
                if other_cluster[0] != community:
                    other_post_id = other_cluster[1]
                    other_toxicity_score = other_cluster[2]
                    other_insult_score = other_cluster[3]
                    other_threat_score = other_cluster[4]
                    other_sexually_explicit_score = other_cluster[5]
                    
                    
                    mesaures = [
                        (toxicity_score, other_toxicity_score), 
                        (insult_score, other_insult_score), 
                        (threat_score, other_threat_score), 
                        (sexually_explicit_score, other_sexually_explicit_score)
                    ]
                    
                    distance = 0
                    for value1, value2 in mesaures:
                        distance += ((value1 - value2) ** 2) ** 0.5
                    
                    distances[f"{community}"][f"{other_cluster[0]}"] = distance
        
        clusters = ['gaming', 'politics', 'youtube', 'stem']
        
        for cluster in clusters:
            self.ctx['database'].insert_data( # Add this cluster to the DB
                "results",
                f"cluster",
                f"'{cluster}'"
            )
        
        # Add the distances to the DB
        for community, metrics in distances.items():
            for other_community in metrics:
                try:
                    self.ctx['database'].update_row(
                        "results",
                        f"{other_community} = '{metrics[other_community]}'",
                        f"cluster = '{community}'"
                    )
                except KeyError:
                    continue
        self.ctx['database'].commit()
        
        '''
        for cluster in distances.keys():
            for community in distances.values():
                self.ctx['database'].insert_data( # Add this cluster to the DB
                    "results",
                    f"cluster",
                    f"'{cluster}'"
                )
            for comm in clusters:
                try:
                    self.ctx['database'].update_row(
                        "results",
                        f"{comm} = '{community[comm]}'",
                        f"cluster = '{cluster}'"
                    )
                except KeyError:
                    continue
        self.ctx['database'].commit()
        '''
    
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
