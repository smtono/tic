"""
This module is used to test file manipulation functions
Files are used throughout the program to read from datasets
and write to output files

Functions being tested:
    - read_file
    - write_file
"""

import unittest
import src.util as util

class TestFileManipulation(unittest.TestCase):
    """
    OBJECTIVE: Test the file manipulation functions
    """
    def test_read_file(self):
        """
        OBJECTIVE: Test the read_file function
        """
        self.assertEqual(util.read_file("tests/resources/test_file.txt"), "This is a test file")

    def test_write_file(self):
        """
        OBJECTIVE: Test the write_file function
        """
        util.write_file("This is a test", "tests/test_file.txt")
        self.assertEqual(util.read_file("tests/resources/test_file.txt"), "This is a test")

        # reset file
        with open("tests/test_file.txt", "w") as file:
            file.write("This is a test file")

if __name__ == "__main__":
    unittest.main()
