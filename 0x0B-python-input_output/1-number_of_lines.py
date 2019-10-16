#!/usr/bin/python3
"""
    1. Number of lines
"""


def number_of_lines(filename=""):
    """ Return number of lines in a file """
    with open(filename) as f:
        lines = 0
        for line in f:
            lines += 1
    return lines  # this line could be indented 1 more level!
