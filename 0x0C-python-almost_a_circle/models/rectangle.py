#!/usr/bin/python3
"""
rectangle module
This modules contains the definion of the Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle.

    Attributes:
        => private attributes:
            - width: the width of the rectangle
            - height: the height of the reactangle
            - x: the x coord
            - y: the y coord
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate a new Rectangle object."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter of width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter of width."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter of height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter of height."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter of x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter of x."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """Getter of y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter of y."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the Rectangle object."""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #."""
        blanks = "".join(" " for _ in range(self.x))
        hashtags = "".join("#" for _ in range(self.width))
        line = "{}{}".format(blanks, hashtags)
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(line)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute."""
        if len(args) > 0:
            self.id = args[0]
            self.width = args[1] if len(args) > 1 else self.width
            self.height = args[2] if len(args) > 2 else self.height
            self.x = args[3] if len(args) > 3 else self.x
            self.y = args[4] if len(args) > 4 else self.y
        else:
            if (v := kwargs.get("id")) is not None:
                self.id = v
            if (v := kwargs.get("width")) is not None:
                self.width = v
            if (v := kwargs.get("height")) is not None:
                self.height = v
            if (v := kwargs.get("x")) is not None:
                self.x = v
            if (v := kwargs.get("y")) is not None:
                self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return dict({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            })

    def __str__(self):
        """returns the string representaion of a rectangla object."""
        s = "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return s.format(
                self.__class__.__name__,
                self.id, self.x, self.y, self.width, self.height)
