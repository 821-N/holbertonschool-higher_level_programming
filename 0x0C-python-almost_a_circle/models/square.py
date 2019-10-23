#!/usr/bin/python3
"""
    Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """eeeee"""


    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string """
        return "[Square] (%d) %d/%d - %d" % (self.id, self.x, self.y, self.size)


    def update(self, *args, **kwargs):
        """ There must be a better way to do this: 2 """
        if len(args) >= 4:
            self.y = args[3]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 1:
            self.id = args[0]
        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "size" in kwargs:
                self.size = kwargs["size"]

    def to_dictionary(self):
        """ look we had to write the entire thing again isn't inheretence great? """
        return {"id": self.id, "x": self.x, "y": self.y, "size": self.size}
    
    @property
    def size(self):
        """ someBODY once told me """
        return self.width

    @size.setter
    def size(self, size):
        """ the woooorrrrrllld is gonna roll me """
        self.width = size
        self.height = size

    
