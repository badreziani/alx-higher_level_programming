#!/usr/bin/python3
"""This modules contains a definition for
matrix_divided function.
"""

def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    print("")
    list_type_err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(list_type_err)
    if type(matrix[0]) is not list:
        raise TypeError(list_type_err)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(list_type_err)
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(list_type_err)
    lengths = [len(row) for row in matrix]
    if len(lengths) > 1:
        for idx in range(len(lengths) - 1):
            if lengths[idx] != lengths[idx + 1]:
                raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
    return new_matrix
