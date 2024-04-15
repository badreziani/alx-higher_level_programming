#!/usr/bin/python3
"""
    Definition of class Rectangle
"""


class Rectangle(BaseGeometry):
    """Class Rectancle"""

    def __init__(self, width, height):
        """Instantiate a new Rectangle
        with width and height"""

        super.integer_validator("w", width);
        self.__width = width
        super.integer_validator("h", height)
        self.__height = height
