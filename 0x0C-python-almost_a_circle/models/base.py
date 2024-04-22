#!/usr/bin/python3
"""
base module
This module contains the definition of the class Base
"""

import json


class Base:
    """Class Base.
    Attributes:
        - __nb_objects: private class attribute, counts the number
        of instanciated objects.
        - id: instance attribute, the id of the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instanciate a new object."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries."""
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file."""

        filename = "{}.json".format(cls.__name__)
        if obj is not None and len(list_objs) > 0:
            objs = [obj.to_dictionary() for obj in list_objs]
        else:
            objs = "[]"
        with open(filename, mode="w") as f:
            f.write(cls.to_json_string(objs))
