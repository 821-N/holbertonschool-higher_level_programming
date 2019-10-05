#!/usr/bin/python3
"""
    Print Square
"""


def print_square(size):
    """ print a square with #s """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#"*size)
