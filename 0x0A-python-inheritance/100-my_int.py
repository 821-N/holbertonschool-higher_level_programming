#!/usr/bin/python3
"""
    12. My integer
"""


class MyInt(int):
    """ just a normal integer """

    __eq__ = int.__ne__
    __ne__ = int.__eq__
