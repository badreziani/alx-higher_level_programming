#!/usr/bin/python3
"""This file defines a class 'Square'
with a private 'size' attribute
"""


class Square:
    """Square class

    Attributes:
        size: a private integer attr
        position: a private tuple attr

    Raises:
        TypeError: if size is not an integer
        ValueError: if if size is less than 0
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if isinstance(position, tuple) and\
                len(position) == 2 and\
                all(isinstance(x, int) and x >= 0 for x in position):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        my_str = "\n".join(["#" * self.__size] * self.__size)
        print(my_str)

    @property
    def position(self):
        """Gets the postion

        Returns:
            the position
        """
        return self__position

    @position.setter
    def position(self, value):
        """Sets the postion
        Args:
            value: the value of postion

        Raises:
            TypeError: if value is not a tuple
            or the length of value is != 2
            or x or y are note integer or less then 0
        """

        if isinstance(value, tuple) and\
                len(value) == 2 and\
                all(isinstance(x, int) and x >= 0 for x in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
