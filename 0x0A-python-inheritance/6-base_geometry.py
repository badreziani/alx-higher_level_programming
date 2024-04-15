#!/usr/bin/python3
"""
Defines the class BaseGeometry
    Methods:
        - area: that raises an Exception with
        the message area() is not implemented
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        raise NotImplemented("area() is not implemented")
