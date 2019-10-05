#!/usr/bin/python3
"""
    Add integer
"""


def add_integer(a, b=98):
    """ add two numbers, converted to integers """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
