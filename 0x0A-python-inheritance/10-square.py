#!/usr/bin/python3
"""
    10. Square #1
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ init """
        super().__init__(size, size)
