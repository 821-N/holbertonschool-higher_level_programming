#!/usr/bin/python3
"""
    14. Pascal's Triangle
"""


def pascal_triangle(n):
    """ return first n rows of pascal's triangle """
    if n <= 0:
        return []
    rows = [[1]]
    for i in range(n-1):
        rows += [list(map(sum, zip(rows[-1] + [0], [0] + rows[-1])))]
    return rows
