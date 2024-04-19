#!/usr/bin/python3
"""
base module
This module contains the definition of the class Base
"""


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
