#!/usr/bin/python3
"""
5-save_to_json_file.py
"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
