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

    @property
    def size(self):
        """Gets the size of the square

        Returns:
            the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value: the value to set for size

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        """
        print(f"{'\n'.join(['#' * self.__size] * self.__size))}")
