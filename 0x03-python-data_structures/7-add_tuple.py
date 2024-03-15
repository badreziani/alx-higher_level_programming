#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples.
    """
    if len(tuple_a) == 2:
        a, b = tuple_a
    elif len(tuple_a) == 1:
        a, b = tuple_a[0], 0
    else:
        a, b = 0, 0

    if len(tuple_b) == 2:
        c, d = tuple_b
    elif len(tuple_b) == 1:
        c, d = tuple_b[0], 0
    else:
        c, d = 0, 0
    return (a + c, b + d)
