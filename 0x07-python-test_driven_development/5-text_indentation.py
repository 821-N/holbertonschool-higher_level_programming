#!/usr/bin/python3
"""
    Add Linebreaks To Text
"""


def text_indentation(text):
    """ insert 2 linebreaks after ? . : """
    if type(text) != str:
        raise TypeError("text must be a string")
    for dl in '?', '.', ':':
        text = (dl+"\n\n").join(line.strip(" ") for line in text.split(dl))
    print(end=text)
