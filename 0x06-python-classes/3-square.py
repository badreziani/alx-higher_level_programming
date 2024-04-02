#!/usr/bin/python3
"""This file defines a class 'Square'
with a private 'size' attribute
"""


class Square:
    """Square class

    Attributes:
        size: a private integer attr

    Raises:
        TypeError: if size is not an integer
        ValueError: if if size is less than 0
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area
        """

        return self.__size ** 2
