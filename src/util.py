"""
This module is used to store utility functions when interacting with the program
Some of these utility functions include:
    - Reading and writing to files
    -
"""

import logging
import os


def read_file(file_path):
    """
    Reads a file and returns the contents of the file
    
    Args:
        file_path (str): The path to the file to read
    Returns:
        str: The contents of the file
    """
    logging.info(f"Reading file: {file_path}")
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")

def write_file(content: str, file_path: str=None):
    """
    Writes content to a file
    
    Args:
        content (str): The content to write to the file
        file_path (str): The path to the file to write to
    Returns:
        None
    """
    if file_path:
        logging.info(f"Writing to file: {file_path}")
        if not os.path.exists(os.path.join(os.getcwd(), file_path)):
            logging.warning(f"File does not exist, creating file: {file_path}")
            with open(file_path, "w") as file:
                file.write(content)

    else:
        logging.warning("No file path provided")
        logging.info("Writing to default file output.txt")

        with open("output.txt", "w") as file:
            file.write(content)
