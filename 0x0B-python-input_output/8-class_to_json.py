#!/usr/bin/python3
"""
8-class_to_json module
"""


def class_to_json(obj):
    """class_to_json function.
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    return obj.__dict__
