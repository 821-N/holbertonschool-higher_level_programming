#!/usr/bin/python3
"""
    2. First Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ no. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ get area of rectangle """
        return self.width * self.height

    def display(self):
        """ Print rectangle using #s """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return "[Rectangle] (%d) %d/%d - %d/%d" % (
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ There must be a better way to do this """
        if len(args) >= 5:
            self.y = args[4]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 1:
            self.id = args[0]
        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]

    def to_dictionary(self):
        """ get dictionary representation """
        return {
            "id": self.id, "x": self.x, "y": self.y,
            "width": self.width, "height": self.height
        }
            
    # after this is just getters and setters so don't even bother
    
    @property
    def width(self):
        """ one """
        return self.__width

    @width.setter
    def width(self, width):
        """ two """
        self.check_size("width", width)
        self.__width = width

    @property
    def height(self):
        """ oatmeal """
        return self.__height

    @height.setter
    def height(self, height):
        """ kirby """
        self.check_size("height", height)
        self.__height = height

    @property
    def x(self):
        """ is """
        return self.__x

    @x.setter
    def x(self, x):
        """ a """
        self.check_pos("x", x)
        self.__x = x

    @property
    def y(self):
        """ pink """
        return self.__y

    @y.setter
    def y(self, y):
        """ guy """
        self.check_pos("y", y)
        self.__y = y

