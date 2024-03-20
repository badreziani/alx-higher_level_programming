#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    """
    return [[val**2 for val in row] for row in matrix]
