#!/usr/bin/python3
"""
    0. Read file
"""


def read_file(filename=""):
    """ Print the contents of a file """
    with open(filename) as f:
        print(f.read())
