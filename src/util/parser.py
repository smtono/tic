"""
This module contains the definition of the Parser class
This parser is used to parse the command line arguments

Commands include:
    twitter -query <query> --count <count>
    perspective --text <text> --attributes <attributes>
"""    

import argparse

class Parser():
    """
    Class definiton for CLI parser
    """
    def __init__(self, ctx: dict) -> None:
        """
        Sets up the parser

        Args:
            ctx: dict
                The context dictionary containing the configuration
        """
        self.parser = argparse.ArgumentParser(
            prog='tic',
            description='TIC - Toxic Internet Communities',
            epilog='This program is used to analyze datasets and create visualizations regarding Internet communities'
        )
        subparser = self.parser.add_subparsers(dest='command')
        
        # Admin Command
        admin = subparser.add_parser('admin', help='Admin commands')
        finish = admin.add_subparsers(dest='admin_command')
        finish.add_parser('finish', help='End the program')
        
        # Twitter Command
        twitter = subparser.add_parser('twitter')
        get = twitter.add_subparsers(dest='twitter')
        get.add_argument('--query', type=str, help='The query to search for', required=True)
        get.add_argument('--count', type=int, help='The count of tweets to return', required=False)
        
        # Perspective Command
        perspective = subparser.add_parser('perspective')
        analyze = perspective.add_subparsers(dest='perspective')
        analyze.add_argument('--text', type=str, help='The text to analyze', required=True)
        analyze.add_argument('--attributes', type=str, nargs='*', help='The attributes to analyze', required=False)
        
        # Database Command
        database = subparser.add_parser('database')
