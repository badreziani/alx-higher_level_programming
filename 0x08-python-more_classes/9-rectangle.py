#!/usr/bin/python3
"""This module contains the definition of
the class Rectangle.
"""


class Rectangle:
    """Defines a Rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Insantciate the object with values width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the value of with."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value of height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height."""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area."""

        return self.__width * self.height

    def perimeter(self):
        """returns the rectangle perimeter."""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area."""

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size."""

        return cls(size, size)

    def __str__(self):
        """returns the representation of a rectangle object"""

        if self.__width == 0 or self.__height == 0:
            return ""
        my_repr = "".join(str(self.print_symbol) for _ in range(self.width))
        return "\n".join(my_repr for _ in range(self.height))

    def __repr__(self):
        """returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """runs when the object is deleted.
        And prints 'Bye rectangle...'."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
