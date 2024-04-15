#!/usr/bin/python3

"""This module contains the definition
of class `MyList`
"""


class MyList(list):

    """Class MyList"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)."""

        sorted_str = ", ".join(str(x) for x in sorted(self))
        print("[{}]".format(sorted_str))
