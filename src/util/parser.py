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
        # Top level parser
        self.parser = argparse.ArgumentParser(
            prog='tic',
            description='TIC - Toxic Internet Communities',
            epilog='This program is used to analyze datasets and create visualizations regarding Internet communities'
        )
        subparser = self.parser.add_subparsers(dest='command')

        # Admin parser
        admin = subparser.add_parser('admin', help='Admin commands')
        finish = argparse.ArgumentParser(parents=[self.parser], add_help=False)
        finish.add_argument('finish', action='store_true', help='Finish the program')
        
        # Twitter parser
        twitter = subparser.add_parser('twitter')
        get = argparse.ArgumentParser(parents=[self.parser], add_help=False)
        get.add_argument('--query', type=str, help='The query to search for', required=True)
        get.add_argument('--count', type=int, help='The count of tweets to return', required=False)
        
        # Perspective parser
        perspective = subparser.add_parser('perspective')
        analyze = argparse.ArgumentParser(parents=[self.parser], add_help=False)
        analyze.add_argument('--text', type=str, help='The text to analyze', required=True)
        analyze.add_argument('--attributes', type=str, nargs='*', help='The attributes to analyze', required=False)
        
        # Database parser
        database = argparse.ArgumentParser(parents=[self.parser], add_help=False)
