#!/usr/bin/python3
"""
12-pascal_triangle module
"""


def pascal_triangle(n):
    """pascal_triangle.
    returns a list of lists of integers
    representing the Pascal's triangle of n:
    Returns an empty list if n <= 0
    """

    if n <= 0:
        return []

    tr = [[1 for _ in range(i)] for i in range(1, n + 1)]
    for i in range(1, n):
        for j in range(1, i):
            tr[i][j] = tr[i - 1][j - 1] + tr[i - 1][j]
    return tr
