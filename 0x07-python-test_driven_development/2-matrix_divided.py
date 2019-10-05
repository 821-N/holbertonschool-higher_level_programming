#!/usr/bin/python3
"""
    Matrix divide function
"""


def matrix_divided(matrix, div):
    """ return copy of `matrix` divided by `div`, rounded to .01 """
    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    row_len = None
    if type(matrix) != list:
        raise TypeError(type_error)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    temp = 1 / div  # throw div by 0 error even if matrix is empty
    new = []
    for row in matrix:
        if type(row) != list:
            raise TypeError(type_error)
        if row_len is None:
            row_len = len(row)
        elif row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new.append([])
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(type_error)
            new[-1].append(round(item / div, 2))
    return new
