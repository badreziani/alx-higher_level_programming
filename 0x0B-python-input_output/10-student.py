#!/usr/bin/python3
"""
9-student module
"""


class Student:
    """Class Student.
    Attributes:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """

        s_attrs = self.__dict__

        if type(attrs) is list and all(type(attr) in attrs is str):
            s_attrs = {key: value for s_attrs.items() if key in attrs}
        return s_attrs
