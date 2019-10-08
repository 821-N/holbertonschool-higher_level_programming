#!/usr/bin/python3
"""
    Rectangle Class
"""


class Rectangle:
    """
        Rectangle Class
    """

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        row = ""
        for x in range(self.width):
            row += str(Rectangle.print_symbol)
        return "\n".join([row]*self.height)

    def __repr__(self):
        """ return "Rectangle(width, height)" """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ print message when rectangle is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")  # :(
