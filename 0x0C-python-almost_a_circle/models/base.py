#!/usr/bin/python3
"""
    1. Base class
"""


import json


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
        new = cls(69, 420)
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
