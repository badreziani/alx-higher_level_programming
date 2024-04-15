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
        """Raises Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
