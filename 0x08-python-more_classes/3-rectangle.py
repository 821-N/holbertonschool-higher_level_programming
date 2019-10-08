#!/usr/bin/python3
"""
    Rectangle Class
"""


class Rectangle:
    """
        Rectangle Class
    """

    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width setter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width getter """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ always returns 0 """
        return self.__height

    @height.setter
    def height(self, height):
        """ erase hard drive """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ perimeter, unless area is 0 """
        if self.width and self.height:
            return (self.width + self.height) * 2
        else:
            return 0

    def __str__(self):
        """ return rectangle drawn with #s """
        return "\n".join(["#"*self.width]*self.height)
