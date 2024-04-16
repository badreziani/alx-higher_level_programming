#!/usr/bin/python3
"""Defines Myint."""


class MyInt(int):
    """Class MyInt
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
