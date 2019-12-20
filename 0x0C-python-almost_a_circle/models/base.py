#!/usr/bin/python3
"""
    1. Base class
"""


import json
import turtle
import random


class Base:
    """eeeee"""

    __nb_objects = 0

    @classmethod
    def check_size(self, name, value):
        """ check if value is int > 0 """
        if type(value) != int:
            raise TypeError("%s must be an integer" % name)
        if value <= 0:
            raise ValueError("%s must be > 0" % name)

    @classmethod
    def check_pos(self, name, value):
        """ check if value is int >= 0 """
        if type(value) != int:
            raise TypeError("%s must be an integer" % name)
        if value < 0:
            raise ValueError("%s must be >= 0" % name)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ literally just ... """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string([x.to_dictionary() for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ string -> obj """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create new from aaa """
        new = cls(0, 0)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ load objs from json file """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [
                    cls.create(**x) for x in cls.from_json_string(f.read())
                ]
        except OSError:
            return []

    def __init__(self, id=None):
        """ Init function """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def turtle_rect(self):
        """ draw rect with turtle """
        random.seed(self.id)
        turtle.setworldcoordinates(0,0,200,200)
        turtle.speed(0)
        turtle.delay(0)
        turtle.up()
        turtle.hideturtle()
        turtle.goto(self.x, self.y)
        turtle.seth(90)
        turtle.fillcolor("#%02x%02x%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
            ))
        turtle.begin_fill()
        for i in range(2):
            turtle.fd(self.width)
            turtle.right(90)
            turtle.fd(self.height)
            turtle.right(90)
        turtle.end_fill()

    @staticmethod
    def draw(rectangles, squares):
        """ draw many """
        for rect in rectangles:
            rect.turtle_rect()
        for square in squares:
            square.turtle_rect()
