#!/usr/bin/python3
"""This file defines a class 'Square'
with a private 'size' attribute
"""


class Square:
    """Square class

    Attributes:
        size: a private integer attr
    """

    def __init__(self, size=0):
        self.__size = size
