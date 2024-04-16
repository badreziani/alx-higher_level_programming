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

        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            s_attrs = {k: v for k, v in s_attrs.items() if k in attrs}
        return s_attrs

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """

        for key in json:
            self.__dict__.update({key: json[key]})
