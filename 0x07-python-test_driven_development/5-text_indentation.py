#!/usr/bin/python3
"""
    Add Linebreaks To Text
"""


def text_indentation(text):
    """ insert 2 linebreaks after ? . : """
    if type(text) != str:
        raise TypeError("text must be a string")
    broke = False
    for c in text:
        if not(c == ' ' and broke):
            print(end=c)
        broke = False
        if c in ('.', '?', ':'):
            print()
            print()
            broke = True
