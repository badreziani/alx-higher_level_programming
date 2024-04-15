#!/usr/bin/python3

"""defines the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """The definition of function
    is_kind_of_class

    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class
        that inherited from, the specified class
        otherwise False.
    """
    return isinstance(obj, a_class)
