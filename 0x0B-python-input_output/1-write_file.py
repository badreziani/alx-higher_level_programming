#!/usr/bin/python3
"""
1-write_file.py
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, mode="w") as file:
        return file.write(text)
