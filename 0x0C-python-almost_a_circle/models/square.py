#!/usr/bin/python3
"""
square module
Represents the definition of the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square.
    Attribute:
        - size: the size of the square
        - x: the x coord
        - y: the y coord
        - id: the id of the square object
    """

    def __init__(self, size, x=0, y=0, id=None):
        """instantiate the a new square object."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of size."""
        return self.width

    @size.setter
    def size(self, size):
        """Setter of size."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y
        else:
            if (v := kwargs.get("id")) is not None:
                self.id = v
            if (v := kwargs.get("size")) is not None:
                self.size = v
            if (v := kwargs.get("x")) is not None:
                self.x = v
            if (v := kwargs.get("y")) is not None:
                self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return dict({
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            })

    def __str__(self):
        """."""
        s = "[{}] ({:d}) {:d}/{:d} - {:d}"
        return s.format(
                self.__class__.__name__,
                self.id, self.x, self.y, self.size)
