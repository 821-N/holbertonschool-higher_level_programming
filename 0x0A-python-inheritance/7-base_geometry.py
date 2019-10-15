#!/usr/bin/python3
"""
    6. Improve Geometry
"""


class BaseGeometry:
    """ Base Geometry class """

    def area(self):
        """ ... """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check if value is positive int """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise TypeError(name + " must be greater than 0")
