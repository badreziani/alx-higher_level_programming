#!/usr/bin/python3
"""
Defines the class BaseGeometry
    Methods:
        - area: that raises an Exception with
        the message area() is not implemented
        - integer_validator: that validates value
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(str(value)))
        if value <= 0:
            raise ValueError("{:d} must be greater than 0".format(value))
