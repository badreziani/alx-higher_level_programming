#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string.
    """
    return "".join([ch for ch in my_string if ch not in "cC"])
