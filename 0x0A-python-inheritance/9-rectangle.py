#!/usr/bin/python3
"""
    9. Full Rectangle
"""


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ get area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ convert to string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
