"""
This module contains the class definition for the Admin class
This class contains definitions for administrative commands

Command include:
    -finish - Ends the program
"""

import logging
import sys

class Admin():
    """
    Class definition for the Admin class
    """
    def __init__(self, ctx: dict) -> None:
        """
        Sets up the Admin class

        Args:
            ctx: dict
                The context dictionary containing the configuration
        """
        self.ctx = ctx

    def finish(self) -> None:
        """
        Ends the program
        """
        sys.exit(0)

    def read_command(self, args: dict) -> None:
        """
        Reads the command given by the user

        Args:
            args: dict
                The arguments given by the user
        """
        try:
            getattr(self, args.command)()
        except AttributeError:
            logging.error('Invalid command')
