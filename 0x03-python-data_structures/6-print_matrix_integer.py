#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    """
    for row in matrix:
        for idx, value in enumerate(row):
            print("{:d}".format(value), end="")
            if idx != len(row) - 1:
                print(end=" ")
        print()
