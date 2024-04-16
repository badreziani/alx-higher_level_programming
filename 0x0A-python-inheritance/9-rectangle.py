#!/usr/bin/python3
"""
    Definition of class Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectancle"""

    def __init__(self, width, height):
        """Instantiate a new Rectangle
        with width and height"""

        self.integer_validator("w", width)
        self.__width = width
        self.integer_validator("h", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """returns a formatted string of Rectangle."""

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
