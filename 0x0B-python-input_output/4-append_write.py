#!/usr/bin/python3
"""
    4. Append to a file
"""


def append_write(filename="", text=""):
    """ append text to a file """
    with open(filename, "w+") as f:
        return f.write(text)
