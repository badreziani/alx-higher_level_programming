#!/usr/bin/python3
"""
base module
This module contains the definition of the class Base
"""

import json
import csv
import turtle


class Base:
    """Class Base.
    Attributes:
        - __nb_objects: private class attribute, counts the number
        of instanciated objects.
        - id: instance attribute, the id of the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instanciate a new object."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries."""
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of
        the JSON string representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file."""

        filename = "{}.json".format(cls.__name__)
        objs = []
        if list_objs is not None:
            objs = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w+") as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def load_from_file(cls):
        """Loads content of a file and
        returns a list of instances.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename) as f:
                json_data = cls.from_json_string(f.read())
                data = [cls.create(**obj) for obj in json_data]
                return data
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes list_objs to a csv file."""

        filename = "{}.csv".format(cls.__name__)
        objs = ""
        if list_objs is not None:
            if cls.__name__ == "Rectangle":
                for o in list_objs:
                    s = "{},{},{},{},{}\n".format(
                            o.id,
                            o.width,
                            o.height,
                            o.x, o.y)
                    objs += s
            elif cls.__name__ == "Square":
                for o in list_objs:
                    s = "{},{},{},{}\n".format(
                            o.id, o.size, o.x, o.y)
                    objs += s
        with open(filename, mode="w") as f:
            f.write(objs)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes list_objs from a csv file."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename) as f:
                objs = []
                data = [line[:-1].split(",") for line in f.readlines()]
                if cls.__name__ == "Rectangle":
                    for r in data:
                        objs.append(cls(
                            int(r[1]),
                            int(r[2]),
                            int(r[3]),
                            int(r[4]),
                            id=int(r[0])
                            ))
                elif cls.__name__ == "Square":
                    for r in data:
                        objs.append(cls(
                            int(r[1]),
                            int(r[2]),
                            int(r[3]),
                            id=int(r[0])
                            ))
                return objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares."""
        screen = turtle.Screen()
        screen.bgcolor("#0F0F1E")
        trtl = turtle.Turtle()
        if list_rectangles is not None and len(list_rectangles) > 0:
            for rect in list_rectangles:
                trtl.goto(rect.x, rect.y)
                trtl.begin_fill()
                trtl.color("#fcb900")
                trtl.fd(rect.width)
                trtl.lt(90)
                trtl.fd(rect.height)
                trtl.lt(90)
                trtl.fd(rect.width)
                trtl.lt(90)
                trtl.fd(rect.height)
                trtl.end_fill()

        if list_squares is not None and len(list_squares) > 0:
            for sq in list_squares:
                trtl.goto(sq.x + 200, sq.y + 200)
                trtl.speed(2)
                trtl.begin_fill()
                trtl.color("white")
                trtl.fd(sq.size)
                trtl.lt(90)
                trtl.fd(sq.size)
                trtl.lt(90)
                trtl.fd(sq.size)
                trtl.lt(90)
                trtl.fd(sq.size)
                trtl.end_fill()
        turtle.done()
