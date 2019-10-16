#!/usr/bin/python3
"""
    3. Write to a file
"""


def write_file(filename="", text=""):
    """ write text to a file """
    with open(filename, "w") as f:
        f.write(text)
