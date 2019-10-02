#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):  # going insane aaaaaaaa
        if (type(position) != tuple or len(position) != 2 or
                type(position[0]) != int or type(position[1]) != int or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        print(end="\n" * self.position[1])
        print("\n".join([" "*self.position[0] + "#"*self.size] * self.size))
